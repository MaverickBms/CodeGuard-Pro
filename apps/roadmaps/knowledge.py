"""Servicios para versionar contenido académico y conservar su procedencia."""

from __future__ import annotations

import hashlib
import json
from typing import Iterable

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Max

from .models import (
    ContenidoLeccion,
    ContenidoLeccionActivo,
    EjemploLeccion,
    EjercicioLeccion,
    FuenteConocimiento,
    Leccion,
    ReferenciaFuenteContenido,
    VersionContenidoLeccion,
)


def _serializar_snapshot(leccion: Leccion, contenido: ContenidoLeccion) -> dict:
    """Construye un snapshot determinista con solo recursos publicados."""
    ejemplos = EjemploLeccion.objects.filter(
        leccion=leccion, publicado=True
    ).order_by("orden", "id")
    ejercicios = EjercicioLeccion.objects.filter(
        leccion=leccion, publicado=True
    ).order_by("orden", "id")

    return {
        "esquema_version": 1,
        "leccion": {
            "clave": str(leccion.clave_contenido),
            "titulo": leccion.titulo,
            "descripcion": leccion.descripcion,
            "tipo": leccion.tipo,
        },
        "contenido": {
            "objetivos_aprendizaje": contenido.objetivos_aprendizaje,
            "teoria_tecnica": contenido.teoria_tecnica,
            "explicacion_sencilla": contenido.explicacion_sencilla,
            "notas": contenido.notas,
        },
        "ejemplos": [
            {
                "clave": str(ejemplo.clave_contenido),
                "titulo": ejemplo.titulo,
                "contexto": ejemplo.contexto,
                "lenguaje": ejemplo.lenguaje,
                "codigo": ejemplo.codigo,
                "salida_esperada": ejemplo.salida_esperada,
                "explicacion": ejemplo.explicacion,
                "orden": ejemplo.orden,
            }
            for ejemplo in ejemplos
        ],
        "ejercicios": [
            {
                "clave": str(ejercicio.clave_contenido),
                "titulo": ejercicio.titulo,
                "enunciado": ejercicio.enunciado,
                "instrucciones": ejercicio.instrucciones,
                "lenguaje": ejercicio.lenguaje,
                "nivel": ejercicio.nivel,
                "codigo_inicial": ejercicio.codigo_inicial,
                "obligatorio": ejercicio.obligatorio,
                "orden": ejercicio.orden,
            }
            for ejercicio in ejercicios
        ],
    }


def crear_version_contenido_leccion(
    leccion: Leccion,
    *,
    resumen_cambios: str = "",
    fuentes: Iterable[tuple[FuenteConocimiento, str, str, str]] = (),
) -> VersionContenidoLeccion:
    """Crea un snapshot borrador determinista; nunca publica ni altera el borrador."""
    with transaction.atomic():
        leccion = Leccion.objects.select_for_update().get(pk=leccion.pk)
        try:
            contenido = ContenidoLeccion.objects.get(leccion=leccion)
        except ContenidoLeccion.DoesNotExist as exc:
            raise ValidationError("La lección todavía no tiene contenido editorial.") from exc

        if not contenido.esta_completo:
            raise ValidationError(
                "No se puede versionar una lección sin teoría técnica y explicación sencilla."
            )

        snapshot = _serializar_snapshot(leccion, contenido)
        representacion = json.dumps(
            snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        digest = hashlib.sha256(representacion.encode("utf-8")).hexdigest()
        ultima_version = (
            VersionContenidoLeccion.objects.filter(leccion=leccion).aggregate(
                numero=Max("numero_version")
            )["numero"]
            or 0
        )

        version = VersionContenidoLeccion.objects.create(
            leccion=leccion,
            numero_version=ultima_version + 1,
            esquema_version=1,
            estado="borrador",
            snapshot=snapshot,
            sha256=digest,
            resumen_cambios=resumen_cambios,
        )

        for referencia in fuentes:
            if len(referencia) not in (4, 5):
                raise ValidationError("Cada referencia debe contener 4 o 5 elementos.")
            fuente, rol, localizador, nota_atribucion = referencia[:4]
            uso_declarado = referencia[4] if len(referencia) == 5 else "original"
            if not fuente.activa:
                raise ValidationError(
                    f"La fuente '{fuente}' está inactiva y no puede asociarse a una versión nueva."
                )
            if rol not in {choice[0] for choice in ReferenciaFuenteContenido.ROLES}:
                raise ValidationError("El rol de referencia no está permitido.")
            if uso_declarado not in {choice[0] for choice in ReferenciaFuenteContenido.USOS_DECLARADOS}:
                raise ValidationError("El uso declarado de la fuente no está permitido.")
            referencia = ReferenciaFuenteContenido(
                version=version,
                fuente=fuente,
                rol=rol,
                localizador=localizador,
                nota_atribucion=nota_atribucion,
                uso_declarado=uso_declarado,
            )
            referencia.full_clean()
            referencia.save()

        return version


def _validar_actor_editorial(actor) -> None:
    """Solo usuarios autenticados y activos con privilegios editoriales pueden cambiar estados."""
    if (
        actor is None
        or not getattr(actor, "is_authenticated", False)
        or not getattr(actor, "is_active", False)
        or not getattr(actor, "is_staff", False)
    ):
        raise ValidationError("Se requiere un usuario activo con permisos editoriales.")


def _validar_version_para_revision(version: VersionContenidoLeccion) -> None:
    """Verifica integridad, estructura mínima y procedencia antes de revisar."""
    representacion = json.dumps(
        version.snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    digest = hashlib.sha256(representacion.encode("utf-8")).hexdigest()
    if digest != version.sha256:
        raise ValidationError("El hash no coincide con el snapshot; la versión está alterada.")

    if not isinstance(version.snapshot, dict) or not {
        "esquema_version", "leccion", "contenido", "ejemplos", "ejercicios"
    }.issubset(version.snapshot):
        raise ValidationError("El snapshot no cumple la estructura académica requerida.")

    if version.snapshot["leccion"].get("clave") != str(version.leccion.clave_contenido):
        raise ValidationError("La identidad de la lección no coincide con el snapshot.")

    if not version.referencias.exists():
        raise ValidationError("La versión debe incluir al menos una fuente documentada.")

    if version.referencias.filter(fuente__activa=False).exists():
        raise ValidationError("La versión contiene fuentes inactivas; actualiza su procedencia.")

    for referencia in version.referencias.select_related("fuente").all():
        fuente = referencia.fuente
        estado = fuente.estado_revision_licencia
        if estado in {"pendiente", "requiere_permiso", "no_reutilizable"}:
            raise ValidationError(
                f"La fuente '{fuente.titulo}' no está autorizada para avanzar: "
                f"estado de licencia '{estado}'."
            )
        if not (fuente.revisada_por_id and fuente.revisada_en and fuente.evidencia_licencia):
            raise ValidationError(
                f"La fuente '{fuente.titulo}' carece de evidencia y auditoría de licencia."
            )
        if estado == "compatible" and not fuente.alcance_licencia.strip():
            raise ValidationError(
                f"La fuente '{fuente.titulo}' no documenta el alcance de reutilización."
            )
        if estado == "solo_referencia" and referencia.uso_declarado != "original":
            raise ValidationError(
                f"La fuente '{fuente.titulo}' solo permite contenido original; "
                "no se admiten citas, adaptaciones ni reproducciones."
            )
        if version.estado != "borrador":
            snapshot_licencia = (
                referencia.estado_licencia_snapshot,
                referencia.evidencia_licencia_snapshot,
                referencia.alcance_licencia_snapshot,
                referencia.nota_licencia_snapshot,
                referencia.licencia_revisada_por_snapshot_id,
                referencia.licencia_revisada_en_snapshot,
            )
            licencia_actual = (
                fuente.estado_revision_licencia,
                fuente.evidencia_licencia,
                fuente.alcance_licencia,
                fuente.nota_revision_licencia,
                fuente.revisada_por_id,
                fuente.revisada_en,
            )
            if snapshot_licencia != licencia_actual:
                raise ValidationError(
                    f"La decisión de licencia de '{fuente.titulo}' cambió después del envío a revisión."
                )


@transaction.atomic
def enviar_version_a_revision(version_id: int, *, actor) -> VersionContenidoLeccion:
    """Congela el snapshot y lo mueve de borrador a revisión."""
    _validar_actor_editorial(actor)
    version = VersionContenidoLeccion.objects.select_for_update().get(pk=version_id)
    if version.estado != "borrador":
        raise ValidationError("Solo una versión en borrador puede enviarse a revisión.")
    _validar_version_para_revision(version)
    for referencia in version.referencias.select_related("fuente").all():
        fuente = referencia.fuente
        referencia.estado_licencia_snapshot = fuente.estado_revision_licencia
        referencia.evidencia_licencia_snapshot = fuente.evidencia_licencia
        referencia.alcance_licencia_snapshot = fuente.alcance_licencia
        referencia.nota_licencia_snapshot = fuente.nota_revision_licencia
        referencia.licencia_revisada_por_snapshot = fuente.revisada_por
        referencia.licencia_revisada_en_snapshot = fuente.revisada_en
        referencia.save(update_fields=[
            "estado_licencia_snapshot", "evidencia_licencia_snapshot",
            "alcance_licencia_snapshot", "nota_licencia_snapshot",
            "licencia_revisada_por_snapshot", "licencia_revisada_en_snapshot",
        ])
    from django.utils import timezone

    version.estado = "revision"
    version.enviada_por = actor
    version.enviada_en = timezone.now()
    version.save(update_fields=["estado", "enviada_por", "enviada_en"])
    return version


@transaction.atomic
def aprobar_version_contenido(version_id: int, *, actor) -> VersionContenidoLeccion:
    """Registra la revisión editorial y aprueba una versión inmutable."""
    from django.utils import timezone

    _validar_actor_editorial(actor)
    version = VersionContenidoLeccion.objects.select_for_update().get(pk=version_id)
    if version.estado != "revision":
        raise ValidationError("Solo una versión en revisión puede aprobarse.")
    _validar_version_para_revision(version)
    version.estado = "aprobada"
    version.revisada_en = timezone.now()
    version.revisada_por = actor
    version.save(update_fields=["estado", "revisada_en", "revisada_por"])
    return version


@transaction.atomic
def publicar_version_contenido(version_id: int, *, actor) -> VersionContenidoLeccion:
    """Publica una versión aprobada y sustituye atómicamente la anterior."""
    from django.utils import timezone

    _validar_actor_editorial(actor)
    version = VersionContenidoLeccion.objects.select_for_update().select_related(
        "leccion"
    ).get(pk=version_id)
    if version.estado != "aprobada":
        raise ValidationError("Solo una versión aprobada puede publicarse.")
    _validar_version_para_revision(version)

    anterior = (
        VersionContenidoLeccion.objects.select_for_update()
        .filter(leccion=version.leccion, estado="publicada")
        .exclude(pk=version.pk)
        .first()
    )
    if anterior:
        anterior.estado = "sustituida"
        anterior.save(update_fields=["estado"])

    version.estado = "publicada"
    version.publicada_en = timezone.now()
    version.publicada_por = actor
    version.save(update_fields=["estado", "publicada_en", "publicada_por"])
    ContenidoLeccionActivo.objects.update_or_create(
        leccion=version.leccion,
        defaults={"version": version},
    )
    return version


@transaction.atomic
def retirar_version_publicada(
    version_id: int, *, actor, motivo: str
) -> VersionContenidoLeccion:
    """Retira una versión publicada sin eliminar su snapshot ni sus evidencias."""
    from django.utils import timezone

    _validar_actor_editorial(actor)
    motivo = (motivo or "").strip()
    if not motivo:
        raise ValidationError("La retirada exige un motivo documentado.")
    version = VersionContenidoLeccion.objects.select_for_update().get(pk=version_id)
    if version.estado != "publicada":
        raise ValidationError("Solo se puede retirar una versión actualmente publicada.")
    version.estado = "retirada"
    version.motivo_retiro = motivo
    version.retirada_en = timezone.now()
    version.retirada_por = actor
    version.save(update_fields=["estado", "motivo_retiro", "retirada_en", "retirada_por"])
    ContenidoLeccionActivo.objects.filter(version=version).delete()
    return version



@transaction.atomic
def revisar_licencia_fuente(
    fuente_id: int, *, actor, estado: str, evidencia: str,
    alcance: str = "", nota: str = "",
) -> FuenteConocimiento:
    """Registra una decisión de licencia auditable; no infiere derechos automáticamente."""
    from django.utils import timezone

    _validar_actor_editorial(actor)
    estados = {opcion[0] for opcion in FuenteConocimiento.ESTADOS_LICENCIA}
    if estado not in estados or estado == "pendiente":
        raise ValidationError("La decisión de licencia indicada no es válida.")
    evidencia = (evidencia or "").strip()
    alcance = (alcance or "").strip()
    nota = (nota or "").strip()
    if not evidencia or not nota:
        raise ValidationError("La revisión exige URL de evidencia y nota de decisión.")
    from urllib.parse import urlsplit
    try:
        parsed_evidence = urlsplit(evidencia)
        evidence_host = parsed_evidence.hostname
    except ValueError as exc:
        raise ValidationError("La evidencia debe ser una URL HTTPS válida.") from exc
    if (
        parsed_evidence.scheme.lower() != "https"
        or not evidence_host
        or parsed_evidence.username
        or parsed_evidence.password
    ):
        raise ValidationError("La evidencia debe ser una URL HTTPS absoluta sin credenciales.")
    if estado == "compatible" and not alcance:
        raise ValidationError("La reutilización compatible exige documentar su alcance.")
    fuente = FuenteConocimiento.objects.select_for_update().get(pk=fuente_id)
    fuente.estado_revision_licencia = estado
    fuente.evidencia_licencia = evidencia
    fuente.alcance_licencia = alcance
    fuente.nota_revision_licencia = nota
    fuente.revisada_por = actor
    fuente.revisada_en = timezone.now()
    fuente.full_clean()
    fuente.save(update_fields=[
        "estado_revision_licencia", "evidencia_licencia", "alcance_licencia",
        "nota_revision_licencia", "revisada_por", "revisada_en",
    ])
    return fuente
