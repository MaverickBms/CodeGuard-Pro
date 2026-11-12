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

        for fuente, rol, localizador, nota_atribucion in fuentes:
            if not fuente.activa:
                raise ValidationError(
                    f"La fuente '{fuente}' está inactiva y no puede asociarse a una versión nueva."
                )
            ReferenciaFuenteContenido.objects.create(
                version=version,
                fuente=fuente,
                rol=rol,
                localizador=localizador,
                nota_atribucion=nota_atribucion,
            )

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


@transaction.atomic
def enviar_version_a_revision(version_id: int, *, actor) -> VersionContenidoLeccion:
    """Congela el snapshot y lo mueve de borrador a revisión."""
    _validar_actor_editorial(actor)
    version = VersionContenidoLeccion.objects.select_for_update().get(pk=version_id)
    if version.estado != "borrador":
        raise ValidationError("Solo una versión en borrador puede enviarse a revisión.")
    _validar_version_para_revision(version)
    version.estado = "revision"
    version.save(update_fields=["estado"])
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
    return version
