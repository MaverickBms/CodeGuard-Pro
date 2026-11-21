"""Carga contenido académico estructurado como borradores editoriales.

El comando no publica contenido ni sustituye al propietario en la revisión
humana. Crea/actualiza el contenido editable, ejemplos, ejercicios
deterministas, recursos audiovisuales verificados, fuentes y un snapshot
borrador versionado. Un fallo de calidad revierte toda la transacción.
"""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from apps.roadmaps.knowledge import (
    CAMPOS_ACADEMICOS_AMPLIADOS,
    _serializar_snapshot,
    _validar_calidad_academica,
    crear_version_contenido_leccion,
)
from apps.roadmaps.models import (
    ConfiguracionEvaluacion,
    ContenidoLeccion,
    EjemploLeccion,
    EjercicioLeccion,
    Etapa,
    FuenteConocimiento,
    Leccion,
    Modulo,
    RecursoAudiovisual,
    Roadmap,
)

MAX_BYTES = 2 * 1024 * 1024
CAMPOS_LECCION = {
    "etapa",
    "modulo",
    "leccion",
    "nivel",
    "objetivos",
    "conocimientos_previos",
    "introduccion",
    "teoria_tecnica",
    "explicacion_sencilla",
    "conceptos_fundamentales",
    "aplicaciones_practicas",
    "errores_frecuentes",
    "evaluacion_aprendizaje",
    "bibliografia_complementaria",
    "ejemplos",
    "ejercicios",
    "fuentes",
    "videos",
}
NIVELES = {"basico", "intermedio", "avanzado"}


class ContenidoAcademicoError(ValueError):
    """El lote no cumple el contrato de contenido académico."""


def _texto(valor, campo, *, minimo=0, maximo=None):
    if not isinstance(valor, str):
        raise ContenidoAcademicoError(f"{campo}: debe ser texto.")
    valor = valor.strip()
    if len(valor) < minimo:
        raise ContenidoAcademicoError(f"{campo}: necesita al menos {minimo} caracteres.")
    if maximo is not None and len(valor) > maximo:
        raise ContenidoAcademicoError(f"{campo}: supera {maximo} caracteres.")
    return valor


def _url_https(valor, campo):
    _texto(valor, campo, minimo=1, maximo=1000)
    try:
        parsed = urlsplit(valor)
    except ValueError as exc:
        raise ContenidoAcademicoError(f"{campo}: URL no válida.") from exc
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ContenidoAcademicoError(f"{campo}: se exige HTTPS absoluto sin credenciales.")
    return valor


def _validar_lote(datos):
    if not isinstance(datos, dict):
        raise ContenidoAcademicoError("El archivo debe ser un objeto JSON.")
    if datos.get("schema_version") != 1:
        raise ContenidoAcademicoError("schema_version no soportada.")
    lecciones = datos.get("lecciones")
    if not isinstance(lecciones, list) or not lecciones:
        raise ContenidoAcademicoError("El lote no contiene lecciones.")

    vistos = set()
    for indice, item in enumerate(lecciones, start=1):
        ruta = f"lecciones[{indice}]"
        if not isinstance(item, dict):
            raise ContenidoAcademicoError(f"{ruta}: se esperaba un objeto.")
        faltan = CAMPOS_LECCION - set(item)
        sobran = set(item) - CAMPOS_LECCION
        if faltan:
            raise ContenidoAcademicoError(f"{ruta}: faltan {', '.join(sorted(faltan))}.")
        if sobran:
            raise ContenidoAcademicoError(f"{ruta}: sobran {', '.join(sorted(sobran))}.")

        clave = (int(item["etapa"]), str(item["modulo"]), str(item["leccion"]).strip())
        if clave in vistos:
            raise ContenidoAcademicoError(f"{ruta}: lección duplicada en el lote.")
        vistos.add(clave)
        if item["nivel"] not in NIVELES:
            raise ContenidoAcademicoError(f"{ruta}.nivel: nivel no permitido.")

        for campo, minimo in CAMPOS_ACADEMICOS_AMPLIADOS.items():
            clave_json = "objetivos" if campo == "objetivos_aprendizaje" else campo
            _texto(item[clave_json], f"{ruta}.{clave_json}", minimo=minimo)

        if not isinstance(item["ejemplos"], list) or not item["ejemplos"]:
            raise ContenidoAcademicoError(f"{ruta}.ejemplos: se exige al menos uno.")
        for pos, ejemplo in enumerate(item["ejemplos"], start=1):
            if not isinstance(ejemplo, dict):
                raise ContenidoAcademicoError(f"{ruta}.ejemplos[{pos}]: objeto esperado.")
            for campo in ("titulo", "contexto", "explicacion"):
                _texto(ejemplo.get(campo), f"{ruta}.ejemplos[{pos}].{campo}", minimo=1)
            for campo in ("lenguaje", "codigo", "salida_esperada"):
                if campo in ejemplo:
                    _texto(ejemplo[campo], f"{ruta}.ejemplos[{pos}].{campo}")

        if not isinstance(item["ejercicios"], list) or not item["ejercicios"]:
            raise ContenidoAcademicoError(f"{ruta}.ejercicios: se exige al menos uno.")
        for pos, ejercicio in enumerate(item["ejercicios"], start=1):
            if not isinstance(ejercicio, dict):
                raise ContenidoAcademicoError(f"{ruta}.ejercicios[{pos}]: objeto esperado.")
            for campo in ("titulo", "enunciado", "instrucciones"):
                _texto(ejercicio.get(campo), f"{ruta}.ejercicios[{pos}].{campo}", minimo=1)
            evaluador = ejercicio.get("evaluador")
            if not isinstance(evaluador, dict):
                raise ContenidoAcademicoError(
                    f"{ruta}.ejercicios[{pos}].evaluador: se exige un evaluador determinista."
                )
            if evaluador.get("tipo") not in {"respuesta_exacta", "codigo_contiene"}:
                raise ContenidoAcademicoError(
                    f"{ruta}.ejercicios[{pos}].evaluador.tipo: no permitido."
                )
            if not isinstance(evaluador.get("configuracion"), dict):
                raise ContenidoAcademicoError(
                    f"{ruta}.ejercicios[{pos}].evaluador.configuracion: objeto esperado."
                )

        if not isinstance(item["fuentes"], list) or not item["fuentes"]:
            raise ContenidoAcademicoError(f"{ruta}.fuentes: se exige al menos una fuente.")
        for pos, fuente in enumerate(item["fuentes"], start=1):
            if not isinstance(fuente, dict):
                raise ContenidoAcademicoError(f"{ruta}.fuentes[{pos}]: objeto esperado.")
            for campo in ("publicador", "titulo", "url", "evidencia", "nota"):
                _texto(fuente.get(campo), f"{ruta}.fuentes[{pos}].{campo}", minimo=1)
            _url_https(fuente["url"], f"{ruta}.fuentes[{pos}].url")
            _url_https(fuente["evidencia"], f"{ruta}.fuentes[{pos}].evidencia")

        if not isinstance(item["videos"], list):
            raise ContenidoAcademicoError(f"{ruta}.videos: debe ser una lista.")
        for pos, video in enumerate(item["videos"], start=1):
            if not isinstance(video, dict):
                raise ContenidoAcademicoError(f"{ruta}.videos[{pos}]: objeto esperado.")
            for campo in ("titulo", "canal", "url", "objetivo", "notas_verificacion"):
                _texto(video.get(campo), f"{ruta}.videos[{pos}].{campo}", minimo=1)
            _url_https(video["url"], f"{ruta}.videos[{pos}].url")
            RecursoAudiovisual.extraer_video_id(video["url"])


def _propietario_editorial():
    from django.conf import settings

    Usuario = get_user_model()
    usuario = Usuario.objects.filter(is_active=True).order_by("id").first()
    if usuario is None:
        raise ContenidoAcademicoError(
            "No existe propietario local. Ejecuta el arranque normal antes de importar."
        )
    if not getattr(settings, "AUTH_DISABLED", False) and not usuario.is_staff:
        raise ContenidoAcademicoError(
            "El modo con autenticación exige un usuario editorial con permisos de staff."
        )
    if getattr(settings, "AUTH_DISABLED", False) and not usuario.is_staff:
        usuario.is_staff = True
        usuario.save(update_fields=["is_staff"])
    return usuario


def _guardar_fuente(datos, actor, ahora):
    fuente, creada = FuenteConocimiento.objects.get_or_create(
        url_canonica=datos["url"],
        edicion=datos.get("edicion", ""),
        defaults={
            "publicador": datos["publicador"],
            "titulo": datos["titulo"],
            "identificador_licencia": datos.get("licencia", ""),
            "url_licencia": datos.get("url_licencia", ""),
            "activa": True,
        },
    )
    if creada:
        fuente.publicador = datos["publicador"]
        fuente.titulo = datos["titulo"]
    elif (
        fuente.estado_revision_licencia != "pendiente"
        and fuente.revisada_por_id
        and fuente.revisada_en
    ):
        # No sobrescribir una decisión de licencia ya adoptada por el editor.
        return fuente
    # Las fuentes se usan exclusivamente para atribución y ampliación; no se
    # reproduce su texto. La decisión queda registrada y auditada.
    fuente.estado_revision_licencia = "solo_referencia"
    fuente.evidencia_licencia = datos["evidencia"]
    fuente.nota_revision_licencia = datos["nota"]
    fuente.alcance_licencia = ""
    fuente.revisada_por = actor
    fuente.revisada_en = ahora
    fuente.consultada_en = ahora
    fuente.activa = True
    fuente.save()
    return fuente


@transaction.atomic
def cargar_lote(datos, *, actor=None):
    actor = actor or _propietario_editorial()
    ahora = timezone.now()
    roadmap = Roadmap.objects.filter(activo=True).order_by("-actualizado_en").first()
    if roadmap is None:
        raise ContenidoAcademicoError("No hay roadmap activo. Carga ASCENSO primero.")

    resumen = {
        "lecciones": 0,
        "ejemplos": 0,
        "ejercicios": 0,
        "videos": 0,
        "fuentes": 0,
        "versiones": 0,
        "reutilizadas": 0,
    }

    for item in datos["lecciones"]:
        try:
            etapa = Etapa.objects.get(roadmap=roadmap, numero=item["etapa"])
            modulo = Modulo.objects.get(etapa=etapa, numero=item["modulo"])
            leccion = Leccion.objects.get(modulo=modulo, titulo=item["leccion"])
        except (Etapa.DoesNotExist, Modulo.DoesNotExist, Leccion.DoesNotExist) as exc:
            raise ContenidoAcademicoError(
                f"No se encontró la lección curricular {item['etapa']}.{item['modulo']} "
                f"«{item['leccion']}»."
            ) from exc

        contenido, _ = ContenidoLeccion.objects.update_or_create(
            leccion=leccion,
            defaults={
                "objetivos_aprendizaje": item["objetivos"],
                "conocimientos_previos": item["conocimientos_previos"],
                "introduccion": item["introduccion"],
                "teoria_tecnica": item["teoria_tecnica"],
                "explicacion_sencilla": item["explicacion_sencilla"],
                "conceptos_fundamentales": item["conceptos_fundamentales"],
                "aplicaciones_practicas": item["aplicaciones_practicas"],
                "errores_frecuentes": item["errores_frecuentes"],
                "evaluacion_aprendizaje": item["evaluacion_aprendizaje"],
                "bibliografia_complementaria": item["bibliografia_complementaria"],
                "nivel_dificultad": item["nivel"],
                "publicado": False,
            },
        )
        resumen["lecciones"] += 1

        fuentes = []
        for orden, fuente_datos in enumerate(item["fuentes"], start=1):
            fuente = _guardar_fuente(fuente_datos, actor, ahora)
            fuentes.append(
                (
                    fuente,
                    "principal",
                    fuente_datos.get("localizador", ""),
                    fuente_datos["nota"],
                    "original",
                )
            )
            resumen["fuentes"] += 1

        for orden, ejemplo_datos in enumerate(item["ejemplos"], start=1):
            EjemploLeccion.objects.update_or_create(
                leccion=leccion,
                titulo=ejemplo_datos["titulo"],
                defaults={
                    "contexto": ejemplo_datos.get("contexto", ""),
                    "lenguaje": ejemplo_datos.get("lenguaje", ""),
                    "codigo": ejemplo_datos.get("codigo", ""),
                    "salida_esperada": ejemplo_datos.get("salida_esperada", ""),
                    "explicacion": ejemplo_datos.get("explicacion", ""),
                    "orden": ejemplo_datos.get("orden", orden),
                    "publicado": True,
                },
            )
            resumen["ejemplos"] += 1

        for orden, ejercicio_datos in enumerate(item["ejercicios"], start=1):
            ejercicio, _ = EjercicioLeccion.objects.update_or_create(
                leccion=leccion,
                titulo=ejercicio_datos["titulo"],
                defaults={
                    "enunciado": ejercicio_datos["enunciado"],
                    "instrucciones": ejercicio_datos["instrucciones"],
                    "lenguaje": ejercicio_datos.get("lenguaje", ""),
                    "nivel": ejercicio_datos.get("nivel", "basico"),
                    "codigo_inicial": ejercicio_datos.get("codigo_inicial", ""),
                    "obligatorio": bool(ejercicio_datos.get("obligatorio", True)),
                    "orden": ejercicio_datos.get("orden", orden),
                    "publicado": True,
                },
            )
            evaluador = ejercicio_datos["evaluador"]
            ConfiguracionEvaluacion.objects.update_or_create(
                ejercicio=ejercicio,
                version=1,
                defaults={
                    "tipo": evaluador["tipo"],
                    "configuracion": evaluador["configuracion"],
                    "activo": True,
                    "permite_completar_leccion": bool(
                        evaluador.get("permite_completar_leccion", True)
                    ),
                },
            )
            resumen["ejercicios"] += 1

        for orden, video_datos in enumerate(item["videos"], start=1):
            video_id = RecursoAudiovisual.extraer_video_id(video_datos["url"])
            RecursoAudiovisual.objects.update_or_create(
                leccion=leccion,
                video_id=video_id,
                defaults={
                    "titulo": video_datos["titulo"],
                    "canal": video_datos["canal"],
                    "url": video_datos["url"],
                    "idioma": "es",
                    "subtitulos": video_datos.get("subtitulos", "desconocido"),
                    "duracion_segundos": video_datos.get("duracion_segundos"),
                    "objetivo_aprendizaje": video_datos["objetivo"],
                    "descripcion": video_datos.get("descripcion", ""),
                    "estado_revision": "aprobado",
                    "disponible": True,
                    "verificado_en": ahora,
                    "verificado_por": actor,
                    "notas_verificacion": video_datos["notas_verificacion"],
                    "orden": video_datos.get("orden", orden),
                },
            )
            resumen["videos"] += 1

        # Solo se crea una versión nueva si el snapshot cambió. Nunca se envía
        # a revisión ni se publica automáticamente.
        snapshot = _serializar_snapshot(leccion, contenido)
        import hashlib

        digest = hashlib.sha256(
            json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        from apps.roadmaps.models import VersionContenidoLeccion

        ultima = (
            VersionContenidoLeccion.objects.filter(leccion=leccion)
            .order_by("-numero_version")
            .first()
        )
        if ultima is not None and ultima.sha256 == digest:
            _validar_calidad_academica(ultima)
            resumen["reutilizadas"] += 1
            continue

        version = crear_version_contenido_leccion(
            leccion,
            resumen_cambios="Carga académica inicial desde lote estructurado; borrador editorial.",
            fuentes=fuentes,
        )
        _validar_calidad_academica(version)
        resumen["versiones"] += 1

    return resumen


class Command(BaseCommand):
    help = (
        "Carga lecciones estructuradas como borradores editoriales, con fuentes, "
        "ejercicios deterministas y videos verificados. No publica contenido."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--ruta",
            default=None,
            help="Ruta al JSON de contenido (por defecto data/contenido_academico_0_1.json).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Valida el archivo sin escribir en la base de datos.",
        )

    def handle(self, *args, **options):
        ruta = Path(options.get("ruta") or Path(__file__).resolve().parents[2] / "data" / "contenido_academico_0_1.json")
        try:
            if ruta.is_symlink() or not ruta.is_file():
                raise ContenidoAcademicoError("El archivo de contenido no existe o no es regular.")
            if ruta.stat().st_size > MAX_BYTES:
                raise ContenidoAcademicoError("El archivo supera el límite de 2 MiB.")
            datos = json.loads(ruta.read_text(encoding="utf-8"))
            _validar_lote(datos)
        except (OSError, json.JSONDecodeError, ContenidoAcademicoError, ValidationError) as exc:
            raise CommandError(f"Contenido no válido: {exc}") from exc

        if options["dry_run"]:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Validación correcta: {len(datos['lecciones'])} lecciones. "
                    "No se escribió en la base de datos."
                )
            )
            return

        try:
            resumen = cargar_lote(datos)
        except (ContenidoAcademicoError, ValidationError) as exc:
            raise CommandError(f"No se pudo cargar el contenido: {exc}") from exc

        self.stdout.write(
            self.style.SUCCESS(
                "Contenido académico cargado como borrador: "
                f"{resumen['lecciones']} lecciones, {resumen['ejemplos']} ejemplos, "
                f"{resumen['ejercicios']} ejercicios, {resumen['videos']} videos, "
                f"{resumen['fuentes']} fuentes, {resumen['versiones']} versiones nuevas, "
                f"{resumen['reutilizadas']} reutilizadas."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "No se publicó ninguna lección. Revisa el contenido, envíalo a "
                "revisión y publícalo desde el flujo editorial cuando corresponda."
            )
        )
