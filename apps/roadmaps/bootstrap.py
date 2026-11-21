"""Arranque idempotente del perfil local y verificación del roadmap instalado.

El servidor empaquetado no debe reconstruir las 1.946 lecciones en cada inicio.
Este módulo compara el manifiesto curricular distribuido con el contenido real
de SQLite y solo invoca ``cargar_ascenso`` cuando falta contenido, cambió el
manifiesto o la base de datos no coincide con la huella esperada.

Reglas de seguridad de datos:
- Nunca se elimina el progreso, los intentos, las evidencias ni las preferencias.
- Los registros ajenos a la versión actual se conservan y se contabilizan.
- Las migraciones pendientes se aplican antes de verificar el roadmap.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable

from django.db import connection

RUTA_MANIFIESTO_ASCENSO = Path(__file__).resolve().parent / "data" / "ascenso_3_1.json"

PREFIJO_EVENTO = "[CodeGuard BOOT] "
TITULO_CRITERIO_PROYECTO = "Proyecto de la etapa"


class ManifiestoInvalido(ValueError):
    """El manifiesto curricular no tiene la estructura mínima esperada."""


@dataclass(frozen=True)
class Manifiesto:
    """Representación verificable del JSON oficial de ASCENSO."""

    ruta: Path
    sha256: str
    nombre: str
    edicion: str
    estructura: tuple[dict, ...]
    total_etapas: int
    total_modulos: int
    total_lecciones: int
    total_prerrequisitos: int
    huella_contenido: str


@dataclass
class Verificacion:
    """Resultado de comparar el manifiesto con SQLite."""

    ok: bool
    motivo: str
    huella_base_datos: str | None = None
    registros_sobrantes: int = 0
    claves_faltantes: list[str] = field(default_factory=list)
    estado_desactualizado: bool = False


def _emitir(evento: dict, *, emit: Callable[[str], None] | None = None) -> None:
    linea = PREFIJO_EVENTO + json.dumps(evento, ensure_ascii=False, separators=(",", ":"))
    if emit is not None:
        emit(linea)
    else:
        print(linea, flush=True)


def _digest(lineas: Iterable[list]) -> str:
    hasher = hashlib.sha256()
    for linea in lineas:
        hasher.update(
            json.dumps(linea, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        )
        hasher.update(b"\n")
    return hasher.hexdigest()


def _texto(valor) -> str:
    return "" if valor is None else str(valor)


def _entero(valor, defecto: int = 0) -> int:
    try:
        return int(valor)
    except (TypeError, ValueError):
        return defecto


def _normalizar_etapa(datos_etapa: dict) -> dict:
    numero = _entero(datos_etapa.get("numero"), -1)
    if numero < 0:
        raise ManifiestoInvalido("Una etapa no tiene un número válido.")

    modulos = []
    for orden_modulo, datos_modulo in enumerate(
        datos_etapa.get("modulos") or [], start=1
    ):
        if not isinstance(datos_modulo, dict):
            raise ManifiestoInvalido(f"La etapa {numero} contiene un módulo inválido.")
        numero_modulo = _texto(datos_modulo.get("numero", ""))
        if not numero_modulo:
            raise ManifiestoInvalido(f"La etapa {numero} contiene un módulo sin número.")

        lecciones = []
        vistos = set()
        for orden_leccion, titulo in enumerate(
            datos_modulo.get("lecciones") or [], start=1
        ):
            titulo = _texto(titulo).strip()
            if not titulo:
                raise ManifiestoInvalido(
                    f"El módulo {numero_modulo} contiene una lección sin título."
                )
            if titulo in vistos:
                raise ManifiestoInvalido(
                    f"El módulo {numero_modulo} contiene lecciones duplicadas."
                )
            vistos.add(titulo)
            lecciones.append(
                {"titulo": titulo, "orden": orden_leccion, "tipo": "concepto"}
            )

        modulos.append(
            {
                "numero": numero_modulo,
                "titulo": _texto(datos_modulo.get("titulo", "")),
                "orden": orden_modulo,
                "lecciones": tuple(lecciones),
            }
        )

    proyecto = _texto(datos_etapa.get("proyecto", ""))
    return {
        "numero": numero,
        "titulo": _texto(datos_etapa.get("titulo", "")),
        "bloque": _texto(datos_etapa.get("bloque", "")),
        "seccion": _texto(datos_etapa.get("seccion", "")),
        "prioridad": _texto(datos_etapa.get("prioridad", "P1")),
        "prioridad_detalle": _texto(datos_etapa.get("prioridad_detalle", "")),
        "objetivo": _texto(datos_etapa.get("objetivo", "")),
        "proyecto": proyecto,
        "proyecto_titulo": _texto(datos_etapa.get("proyecto_titulo", "")),
        "notas": "\n".join(_texto(nota) for nota in (datos_etapa.get("notas") or [])),
        "orden": numero,
        "modulos": tuple(modulos),
        "prerrequisitos": tuple(
            sorted(
                {
                    _entero(item.get("etapa_requerida"), -1)
                    for item in (datos_etapa.get("prerrequisitos") or [])
                    if isinstance(item, dict)
                    and item.get("etapa_requerida") is not None
                }
                - {-1}
            )
        ),
        "criterio": (
            {
                "titulo": TITULO_CRITERIO_PROYECTO,
                "descripcion": proyecto,
                "tipo": "proyecto",
                "obligatorio": True,
                "orden": 1,
            }
            if proyecto
            else None
        ),
    }


def _lineas_manifiesto(estructura: tuple[dict, ...]) -> Iterable[list]:
    for etapa in estructura:
        yield [
            "E",
            etapa["numero"],
            etapa["titulo"],
            etapa["bloque"],
            etapa["seccion"],
            etapa["prioridad"],
            etapa["prioridad_detalle"],
            etapa["objetivo"],
            etapa["proyecto"],
            etapa["proyecto_titulo"],
            etapa["notas"],
            etapa["orden"],
        ]
        for modulo in etapa["modulos"]:
            yield [
                "M",
                etapa["numero"],
                modulo["numero"],
                modulo["titulo"],
                modulo["orden"],
            ]
            for leccion in modulo["lecciones"]:
                yield [
                    "L",
                    etapa["numero"],
                    modulo["numero"],
                    leccion["titulo"],
                    leccion["orden"],
                    leccion["tipo"],
                ]
        criterio = etapa["criterio"]
        if criterio:
            yield [
                "C",
                etapa["numero"],
                criterio["titulo"],
                criterio["descripcion"],
                criterio["tipo"],
                criterio["obligatorio"],
                criterio["orden"],
            ]
    for etapa in estructura:
        for requerida in etapa["prerrequisitos"]:
            yield ["P", etapa["numero"], requerida]


def cargar_manifiesto(ruta: str | Path | None = None) -> Manifiesto:
    """Lee y valida el manifiesto curricular sin tocar la base de datos."""
    ruta = Path(ruta) if ruta else RUTA_MANIFIESTO_ASCENSO
    try:
        contenido = ruta.read_bytes()
    except OSError as exc:
        raise ManifiestoInvalido(f"No se pudo leer el manifiesto: {exc}") from exc

    try:
        datos = json.loads(contenido.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ManifiestoInvalido(f"El manifiesto no es JSON UTF-8 válido: {exc}") from exc

    if not isinstance(datos, dict):
        raise ManifiestoInvalido("El manifiesto debe ser un objeto JSON.")
    etapas_brutas = datos.get("etapas")
    if not isinstance(etapas_brutas, list) or not etapas_brutas:
        raise ManifiestoInvalido("El manifiesto no contiene etapas.")

    estructura = tuple(
        _normalizar_etapa(item) for item in etapas_brutas if isinstance(item, dict)
    )
    numeros = [etapa["numero"] for etapa in estructura]
    if len(set(numeros)) != len(numeros):
        raise ManifiestoInvalido("El manifiesto contiene etapas duplicadas.")

    estructura = tuple(sorted(estructura, key=lambda etapa: etapa["numero"]))
    numeros_validos = {etapa["numero"] for etapa in estructura}
    for etapa in estructura:
        for requerida in etapa["prerrequisitos"]:
            if requerida not in numeros_validos:
                raise ManifiestoInvalido(
                    f"La etapa {etapa['numero']} requiere una etapa inexistente ({requerida})."
                )

    meta = datos.get("metadata") if isinstance(datos.get("metadata"), dict) else {}
    total_modulos = sum(len(etapa["modulos"]) for etapa in estructura)
    total_lecciones = sum(
        len(modulo["lecciones"])
        for etapa in estructura
        for modulo in etapa["modulos"]
    )
    total_prerrequisitos = sum(len(etapa["prerrequisitos"]) for etapa in estructura)

    return Manifiesto(
        ruta=ruta,
        sha256=hashlib.sha256(contenido).hexdigest(),
        nombre=_texto(
            meta.get("nombre", "PROYECTO ASCENSO — Roadmap Maestro Consolidado")
        ),
        edicion=_texto(meta.get("edicion", "3.1")),
        estructura=estructura,
        total_etapas=len(estructura),
        total_modulos=total_modulos,
        total_lecciones=total_lecciones,
        total_prerrequisitos=total_prerrequisitos,
        huella_contenido=_digest(_lineas_manifiesto(estructura)),
    )


def _huella_base_datos(
    roadmap, manifiesto: Manifiesto
) -> tuple[str | None, list[str], int]:
    """Calcula la huella del contenido esperado y cuenta filas sobrantes.

    Solo se serializan las filas que el manifiesto declara. Las filas ajenas
    (por ejemplo, lecciones retiradas de una versión anterior) se conservan y
    se cuentan, pero no impiden el arranque ni borran progreso.
    """
    from .models import (
        CriterioFinalizacion,
        Etapa,
        Leccion,
        Modulo,
        Prerrequisito,
    )

    etapas_db = {
        fila["numero"]: fila
        for fila in Etapa.objects.filter(roadmap=roadmap).values(
            "numero",
            "titulo",
            "bloque",
            "seccion",
            "prioridad",
            "prioridad_detalle",
            "objetivo",
            "proyecto",
            "proyecto_titulo",
            "notas",
            "orden",
        )
    }
    modulos_db = {
        (fila["etapa__numero"], fila["numero"]): fila
        for fila in Modulo.objects.filter(etapa__roadmap=roadmap).values(
            "etapa__numero", "numero", "titulo", "orden"
        )
    }
    lecciones_db = {
        (fila["modulo__etapa__numero"], fila["modulo__numero"], fila["titulo"]): fila
        for fila in Leccion.objects.filter(modulo__etapa__roadmap=roadmap).values(
            "modulo__etapa__numero", "modulo__numero", "titulo", "orden", "tipo"
        )
    }
    criterios_db = {
        (fila["etapa__numero"], fila["titulo"]): fila
        for fila in CriterioFinalizacion.objects.filter(
            etapa__roadmap=roadmap
        ).values(
            "etapa__numero",
            "titulo",
            "descripcion",
            "tipo",
            "obligatorio",
            "orden",
        )
    }
    prerrequisitos_db = set(
        Prerrequisito.objects.filter(etapa__roadmap=roadmap).values_list(
            "etapa__numero", "etapa_requerida__numero"
        )
    )

    lineas: list[list] = []
    faltantes: list[str] = []
    etapas_esperadas: set[int] = set()
    modulos_esperados: set[tuple[int, str]] = set()
    lecciones_esperadas: set[tuple[int, str, str]] = set()
    criterios_esperados: set[tuple[int, str]] = set()
    prerrequisitos_esperados: set[tuple[int, int]] = set()

    for etapa in manifiesto.estructura:
        numero = etapa["numero"]
        etapas_esperadas.add(numero)
        fila = etapas_db.get(numero)
        if fila is None:
            faltantes.append(f"etapa {numero}")
        else:
            lineas.append(
                [
                    "E",
                    fila["numero"],
                    fila["titulo"],
                    fila["bloque"],
                    fila["seccion"],
                    fila["prioridad"],
                    fila["prioridad_detalle"],
                    fila["objetivo"],
                    fila["proyecto"],
                    fila["proyecto_titulo"],
                    fila["notas"],
                    fila["orden"],
                ]
            )

        for modulo in etapa["modulos"]:
            clave_modulo = (numero, modulo["numero"])
            modulos_esperados.add(clave_modulo)
            fila_modulo = modulos_db.get(clave_modulo)
            if fila_modulo is None:
                faltantes.append(f"módulo {numero}.{modulo['numero']}")
            else:
                lineas.append(
                    [
                        "M",
                        numero,
                        fila_modulo["numero"],
                        fila_modulo["titulo"],
                        fila_modulo["orden"],
                    ]
                )

            for leccion in modulo["lecciones"]:
                clave_leccion = (numero, modulo["numero"], leccion["titulo"])
                lecciones_esperadas.add(clave_leccion)
                fila_leccion = lecciones_db.get(clave_leccion)
                if fila_leccion is None:
                    faltantes.append(
                        f"lección {numero}.{modulo['numero']} «{leccion['titulo']}»"
                    )
                else:
                    lineas.append(
                        [
                            "L",
                            numero,
                            modulo["numero"],
                            fila_leccion["titulo"],
                            fila_leccion["orden"],
                            fila_leccion["tipo"],
                        ]
                    )

        criterio = etapa["criterio"]
        if criterio:
            clave_criterio = (numero, criterio["titulo"])
            criterios_esperados.add(clave_criterio)
            fila_criterio = criterios_db.get(clave_criterio)
            if fila_criterio is None:
                faltantes.append(f"criterio de la etapa {numero}")
            else:
                lineas.append(
                    [
                        "C",
                        numero,
                        fila_criterio["titulo"],
                        fila_criterio["descripcion"],
                        fila_criterio["tipo"],
                        fila_criterio["obligatorio"],
                        fila_criterio["orden"],
                    ]
                )

    for etapa in manifiesto.estructura:
        for requerida in etapa["prerrequisitos"]:
            clave = (etapa["numero"], requerida)
            prerrequisitos_esperados.add(clave)
            if clave not in prerrequisitos_db:
                faltantes.append(f"prerrequisito {requerida} → {etapa['numero']}")
            else:
                lineas.append(["P", etapa["numero"], requerida])

    sobrantes = (
        len(set(etapas_db) - etapas_esperadas)
        + len(set(modulos_db) - modulos_esperados)
        + len(set(lecciones_db) - lecciones_esperadas)
        + len(set(criterios_db) - criterios_esperados)
        + len(prerrequisitos_db - prerrequisitos_esperados)
    )
    if faltantes:
        return None, faltantes[:10], sobrantes
    return _digest(lineas), [], sobrantes


def verificar_instalacion(roadmap, manifiesto: Manifiesto) -> Verificacion:
    """Comprueba que SQLite contiene exactamente el contenido del manifiesto."""
    if roadmap is None:
        return Verificacion(
            ok=False,
            motivo="No existe el roadmap ASCENSO en el perfil local.",
            estado_desactualizado=True,
        )

    huella, faltantes, sobrantes = _huella_base_datos(roadmap, manifiesto)
    if faltantes:
        return Verificacion(
            ok=False,
            motivo="El perfil local está incompleto.",
            huella_base_datos=huella,
            registros_sobrantes=sobrantes,
            claves_faltantes=faltantes,
            estado_desactualizado=True,
        )

    if huella != manifiesto.huella_contenido:
        return Verificacion(
            ok=False,
            motivo="El contenido local no coincide con el manifiesto distribuido.",
            huella_base_datos=huella,
            registros_sobrantes=sobrantes,
            estado_desactualizado=True,
        )

    estado = getattr(roadmap, "estado_instalacion", None)
    esperado = {
        "huella_manifiesto": manifiesto.sha256,
        "huella_contenido": manifiesto.huella_contenido,
        "total_etapas": manifiesto.total_etapas,
        "total_modulos": manifiesto.total_modulos,
        "total_lecciones": manifiesto.total_lecciones,
        "total_prerrequisitos": manifiesto.total_prerrequisitos,
        "registros_sobrantes": sobrantes,
        "esquema_version": _esquema_actual(),
    }
    desactualizado = estado is None or any(
        getattr(estado, campo, None) != valor for campo, valor in esperado.items()
    )

    return Verificacion(
        ok=True,
        motivo=(
            "Contenido verificado."
            if not desactualizado
            else "Contenido verificado; metadatos de instalación actualizados."
        ),
        huella_base_datos=huella,
        registros_sobrantes=sobrantes,
        estado_desactualizado=desactualizado,
    )


def _esquema_actual() -> int:
    from .models import EstadoInstalacionRoadmap

    return EstadoInstalacionRoadmap.ESQUEMA_ACTUAL


def registrar_estado_instalacion(
    roadmap,
    *,
    ruta: str | Path | None = None,
    manifiesto: Manifiesto | None = None,
    huella: str | None = None,
    sobrantes: int | None = None,
) -> "EstadoInstalacionRoadmap":
    """Persiste los metadatos de integridad tras una carga correcta."""
    from .models import EstadoInstalacionRoadmap

    manifiesto = manifiesto or cargar_manifiesto(ruta)
    if huella is None or sobrantes is None:
        huella, faltantes, sobrantes = _huella_base_datos(roadmap, manifiesto)
        if faltantes:
            raise ManifiestoInvalido(
                "El roadmap recién cargado no coincide con el manifiesto: "
                + ", ".join(faltantes)
            )
    if huella is None:
        raise ManifiestoInvalido("No se pudo calcular la huella del roadmap instalado.")

    # Los recuentos persistidos son los del manifiesto, no los de la base:
    # las filas históricas sobrantes se contabilizan aparte y no deben hacer
    # que el estado parezca desactualizado en cada arranque.
    estado, _ = EstadoInstalacionRoadmap.objects.update_or_create(
        roadmap=roadmap,
        defaults={
            "huella_manifiesto": manifiesto.sha256,
            "huella_contenido": huella,
            "total_etapas": manifiesto.total_etapas,
            "total_modulos": manifiesto.total_modulos,
            "total_lecciones": manifiesto.total_lecciones,
            "total_prerrequisitos": manifiesto.total_prerrequisitos,
            "registros_sobrantes": sobrantes,
            "esquema_version": EstadoInstalacionRoadmap.ESQUEMA_ACTUAL,
        },
    )
    return estado


def asegurar_roadmap_instalado(
    ruta: str | Path | None = None,
) -> tuple[object, bool]:
    """Devuelve (roadmap, cargado). Solo reconstruye si hay una discrepancia."""
    from .models import Roadmap
    from .services import cargar_ascenso

    manifiesto = cargar_manifiesto(ruta)
    roadmap = Roadmap.objects.filter(
        nombre=manifiesto.nombre, edicion=manifiesto.edicion
    ).first()

    if roadmap is not None:
        verificacion = verificar_instalacion(roadmap, manifiesto)
        if verificacion.ok:
            cambios = []
            if not roadmap.activo:
                roadmap.activo = True
                cambios.append("activo")
            if cambios:
                roadmap.save(update_fields=cambios)
            if verificacion.estado_desactualizado:
                registrar_estado_instalacion(
                    roadmap,
                    manifiesto=manifiesto,
                    huella=verificacion.huella_base_datos,
                    sobrantes=verificacion.registros_sobrantes,
                )
            return roadmap, False

    roadmap = cargar_ascenso(ruta)
    return roadmap, True


def _sembrar_contenido_inicial(*, emit: Callable[[str], None] | None = None) -> int:
    """Carga una sola vez el lote académico inicial en estado borrador."""
    from django.conf import settings

    from .models import ContenidoLeccion

    if not getattr(settings, "AUTH_DISABLED", False):
        # En modo con autenticación, la siembra requiere un editor humano
        # explícito y nunca eleva privilegios de una cuenta existente.
        return 0
    if ContenidoLeccion.objects.exists():
        return 0
    ruta = Path(__file__).resolve().parent / "data" / "contenido_academico_0_1.json"
    if not ruta.is_file():
        return 0
    try:
        import json

        from .management.commands.cargar_contenido_academico import (
            _validar_lote,
            cargar_lote,
        )

        datos = json.loads(ruta.read_text(encoding="utf-8"))
        _validar_lote(datos)
        resumen = cargar_lote(datos)
        _emitir(
            {
                "phase": "content",
                "status": "seeded",
                "lessons": resumen.get("lecciones", 0),
                "drafts": resumen.get("versiones", 0),
            },
            emit=emit,
        )
        return int(resumen.get("lecciones", 0))
    except Exception as exc:  # noqa: BLE001 — el arranque no se bloquea por contenido
        import logging

        logging.getLogger("codeguard").warning(
            "No se pudo sembrar el contenido académico inicial: %s", exc
        )
        _emitir(
            {"phase": "content", "status": "unavailable"},
            emit=emit,
        )
        return 0


def preparar_perfil_local(
    *,
    ruta: str | Path | None = None,
    emit: Callable[[str], None] | None = None,
) -> dict:
    """Migra y verifica el perfil local, emitiendo eventos de progreso.

    Los eventos van a stdout con el prefijo ``[CodeGuard BOOT]`` para que
    Electron pueda mostrar el estado real en la pantalla de inicio.
    """
    inicio = time.monotonic()
    resultado: dict = {
        "migraciones_pendientes": 0,
        "roadmap_cargado": False,
        "roadmap_reutilizado": False,
        "etapas": 0,
        "modulos": 0,
        "lecciones": 0,
        "prerrequisitos": 0,
        "sobrantes": 0,
        "milisegundos": 0,
    }

    _emitir({"phase": "database", "status": "start"}, emit=emit)
    from django.core.management import call_command

    pendientes = 0
    verificar_migraciones = True
    try:
        from django.db.migrations.executor import MigrationExecutor

        ejecutor = MigrationExecutor(connection)
        plan = ejecutor.migration_plan(ejecutor.loader.graph.leaf_nodes())
        pendientes = len(plan)
    except Exception:
        # Si el estado de migraciones no se puede inspeccionar, se delega en
        # ``migrate``, que aplicará lo necesario y fallará con un error claro.
        verificar_migraciones = False
        pendientes = -1

    resultado["migraciones_pendientes"] = max(pendientes, 0)
    if pendientes == 0:
        _emitir(
            {"phase": "database", "status": "ready", "pending": 0, "migrated": False},
            emit=emit,
        )
    else:
        _emitir(
            {
                "phase": "database",
                "status": "migrating",
                "pending": max(pendientes, 0),
                "inspected": verificar_migraciones,
            },
            emit=emit,
        )
        call_command("migrate", interactive=False, verbosity=1)
        _emitir(
            {"phase": "database", "status": "ready", "pending": 0, "migrated": True},
            emit=emit,
        )

    # El perfil monousuario necesita una fila de usuario para asociar progreso
    # aunque el login esté desactivado. Se crea una sola vez, sin credenciales.
    from apps.accounts.bootstrap import asegurar_propietario_local

    _emitir({"phase": "profile", "status": "checking"}, emit=emit)
    propietario = asegurar_propietario_local()
    resultado["propietario_local_id"] = propietario.pk if propietario else None
    _emitir(
        {
            "phase": "profile",
            "status": "ready" if propietario else "unavailable",
            "owner": bool(propietario),
        },
        emit=emit,
    )

    _emitir({"phase": "roadmap", "status": "verifying"}, emit=emit)
    roadmap, cargado = asegurar_roadmap_instalado(ruta)
    resultado["roadmap_cargado"] = cargado
    resultado["roadmap_reutilizado"] = not cargado

    from .models import Etapa, Leccion, Modulo, Prerrequisito

    resultado["etapas"] = Etapa.objects.filter(roadmap=roadmap).count()
    resultado["modulos"] = Modulo.objects.filter(etapa__roadmap=roadmap).count()
    resultado["lecciones"] = Leccion.objects.filter(
        modulo__etapa__roadmap=roadmap
    ).count()
    resultado["prerrequisitos"] = Prerrequisito.objects.filter(
        etapa__roadmap=roadmap
    ).count()

    estado = getattr(roadmap, "estado_instalacion", None)
    resultado["sobrantes"] = estado.registros_sobrantes if estado else 0

    # Siembra el contenido académico inicial como borradores editoriales. No
    # publica ni aprueba nada: permite estudiar con el aviso correspondiente y
    # deja el flujo editorial en manos del propietario.
    resultado["contenido_sembrado"] = _sembrar_contenido_inicial(emit=emit)

    resultado["milisegundos"] = round((time.monotonic() - inicio) * 1000)

    _emitir(
        {
            "phase": "roadmap",
            "status": "loaded" if cargado else "ready",
            "reused": not cargado,
            "stages": resultado["etapas"],
            "modules": resultado["modulos"],
            "lessons": resultado["lecciones"],
            "prerequisites": resultado["prerrequisitos"],
            "preserved": resultado["sobrantes"],
            "ms": resultado["milisegundos"],
        },
        emit=emit,
    )
    _emitir(
        {
            "phase": "ready",
            "status": "ok",
            "ms": resultado["milisegundos"],
        },
        emit=emit,
    )
    return resultado
