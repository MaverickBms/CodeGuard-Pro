"""Instalación transaccional de paquetes de conocimiento firmados.

El módulo no descarga artefactos ni ejecuta contenido. Recibe bytes ya obtenidos,
verifica firma y ZIP, valida su correspondencia con ASCENSO y activa el paquete
solo después de persistir snapshots y catálogo dentro de una transacción.
"""
from __future__ import annotations

import hashlib
import os
import tempfile
from datetime import datetime
from pathlib import Path
from uuid import UUID

from django.conf import settings
from django.db import transaction
from django.utils import timezone

from .content_import import MAX_DOCUMENT_BYTES
from .distribution import (
    DistributionError,
    load_strict_json,
    validate_package_archive,
    verify_signed_manifest,
)
from .models import (
    ContenidoLeccionPaquete,
    EstadoSincronizacion,
    EjemploLeccion,
    EjercicioLeccion,
    FuenteConocimiento,
    FuentePaqueteConocimiento,
    Leccion,
    PaqueteConocimientoInstalado,
)


class InstallationError(ValueError):
    """El paquete no puede instalarse sin comprometer la integridad local."""


def _curriculum_map(payloads):
    """Comprueba UUID, pertenencia e identidad contra el roadmap local."""
    validated = []
    for path, payload in payloads.items():
        document = load_strict_json(payload, max_bytes=MAX_DOCUMENT_BYTES)
        snapshot = document["snapshot"]
        lesson_data = snapshot["leccion"]
        lesson_uuid = UUID(lesson_data["clave"])
        try:
            lesson = Leccion.objects.select_related("modulo").get(
                clave_contenido=lesson_uuid
            )
        except Leccion.DoesNotExist as exc:
            raise InstallationError(
                f"{path}: la lección no existe en el roadmap ASCENSO instalado."
            ) from exc

        if (lesson.titulo, lesson.descripcion, lesson.tipo) != (
            lesson_data["titulo"], lesson_data["descripcion"], lesson_data["tipo"]
        ):
            raise InstallationError(
                f"{path}: la identidad curricular difiere del roadmap local; "
                "se requiere una actualización curricular compatible."
            )

        example_ids = {item["clave"] for item in snapshot["ejemplos"]}
        if example_ids:
            found = set(
                EjemploLeccion.objects.filter(
                    leccion=lesson, clave_contenido__in=example_ids
                ).values_list("clave_contenido", flat=True)
            )
            if {str(value) for value in found} != example_ids:
                raise InstallationError(
                    f"{path}: uno o más UUID de ejemplo no pertenecen a la lección."
                )

        exercise_ids = {item["clave"] for item in snapshot["ejercicios"]}
        if exercise_ids:
            found = set(
                EjercicioLeccion.objects.filter(
                    leccion=lesson, clave_contenido__in=exercise_ids
                ).values_list("clave_contenido", flat=True)
            )
            if {str(value) for value in found} != exercise_ids:
                raise InstallationError(
                    f"{path}: uno o más UUID de ejercicio no pertenecen a la lección."
                )

        validated.append((lesson, document, hashlib.sha256(payload).hexdigest()))
    return validated


def _artifact_root():
    configured_value = os.environ.get("CODEGUARD_DATA_DIR")
    if configured_value is not None and not configured_value.strip():
        raise InstallationError("CODEGUARD_DATA_DIR no puede estar vacío.")
    configured = Path(
        configured_value if configured_value is not None else Path(settings.BASE_DIR) / "data"
    ).expanduser()
    if configured.is_symlink():
        raise InstallationError("CODEGUARD_DATA_DIR no puede ser un symlink.")
    configured.mkdir(parents=True, exist_ok=True)
    root = configured.resolve()
    package_root = root / "knowledge-packages"
    if package_root.exists() and package_root.is_symlink():
        raise InstallationError("El directorio de paquetes no puede ser un symlink.")
    package_root.mkdir(mode=0o700, exist_ok=True)
    return root, package_root


def _persist_artifact(package_bytes, *, channel, package_id, digest):
    root, package_root = _artifact_root()
    channel_dir = package_root / channel
    if channel_dir.exists() and channel_dir.is_symlink():
        raise InstallationError("El directorio del canal no puede ser un symlink.")
    channel_dir.mkdir(mode=0o700, exist_ok=True)
    filename = f"{package_id}-{digest}.zip"
    destination = channel_dir / filename
    try:
        destination.resolve().relative_to(root)
    except ValueError as exc:
        raise InstallationError("La ruta del artefacto sale del almacén local.") from exc

    if destination.exists():
        if destination.is_symlink() or not destination.is_file():
            raise InstallationError("El destino del paquete no es un archivo regular.")
        if hashlib.sha256(destination.read_bytes()).hexdigest() != digest:
            raise InstallationError("Ya existe un artefacto local con contenido distinto.")
        return f"knowledge-packages/{channel}/{filename}", destination, False

    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".package-", suffix=".tmp", dir=channel_dir
    )
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(package_bytes)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, destination)
        if os.name == "posix":
            directory_fd = os.open(channel_dir, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    except Exception:
        try:
            os.unlink(temporary_name)
        except OSError:
            pass
        raise
    return f"knowledge-packages/{channel}/{filename}", destination, True


def _read_artifact(storage_key):
    if not storage_key or "\\" in storage_key:
        raise InstallationError("El paquete no tiene una ruta local válida.")
    parts = Path(storage_key)
    if parts.is_absolute() or any(part in {"", ".", ".."} for part in parts.parts):
        raise InstallationError("La ruta almacenada del paquete no es relativa y segura.")
    root, _ = _artifact_root()
    path = root.joinpath(*parts.parts)
    try:
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise InstallationError("La ruta almacenada sale del almacén local.") from exc
    if path.is_symlink() or not path.is_file():
        raise InstallationError("El artefacto instalado no está disponible.")
    return path.read_bytes()


@transaction.atomic
def instalar_paquete_firmado(
    manifest_bytes: bytes,
    signature_bytes: bytes,
    package_bytes: bytes,
    *,
    trusted_public_keys: dict,
    allowed_hosts,
    expected_channel: str,
    app_version: str,
    manifest_etag: str = "",
):
    """Verifica, registra y activa un paquete completo en una sola transacción."""
    if expected_channel not in {"stable", "beta"}:
        raise InstallationError("El canal solicitado no está permitido.")
    if not isinstance(manifest_etag, str) or len(manifest_etag) > 255:
        raise InstallationError("El ETag del manifiesto supera el límite permitido.")

    state = (
        EstadoSincronizacion.objects.select_for_update()
        .filter(channel=expected_channel)
        .first()
    )
    if state is None:
        state = EstadoSincronizacion.objects.create(channel=expected_channel)

    latest = (
        PaqueteConocimientoInstalado.objects.select_for_update()
        .filter(channel=expected_channel)
        .order_by("-sequence")
        .first()
    )
    current_sequence = latest.sequence if latest else 0
    current_manifest_hash = latest.manifest_sha256 if latest else None

    try:
        verified = verify_signed_manifest(
            manifest_bytes,
            signature_bytes,
            trusted_public_keys=trusted_public_keys,
            allowed_hosts=allowed_hosts,
            expected_channel=expected_channel,
            app_version=app_version,
            current_sequence=current_sequence,
            current_manifest_sha256=current_manifest_hash,
        )
        manifest = verified["manifest"]
        archive = validate_package_archive(package_bytes, manifest=manifest)
    except DistributionError as exc:
        raise InstallationError(str(exc)) from exc

    if verified["unchanged"]:
        if latest is None or latest.estado not in {"activo", "sustituido"}:
            raise InstallationError(
                "La secuencia ya registrada no conserva un paquete instalable."
            )
        # Un rollback puede mantener activo un paquete anterior. La respuesta
        # idéntica del servidor no debe deshacer esa decisión local.
        return {
            "installed": False,
            "unchanged": True,
            "package": latest,
            "active_package": state.active_package,
            "state": state,
            "lesson_count": latest.contenidos_leccion.count(),
        }

    curriculum = _curriculum_map(archive["payloads"])
    if archive["index"]["schema_version"] == 1:
        legacy_source_ids = {
            source["clave"]
            for payload in archive["payloads"].values()
            for source in load_strict_json(
                payload, max_bytes=MAX_DOCUMENT_BYTES
            )["fuentes"]
        }
        legacy_sources = {
            str(source.clave): source
            for source in FuenteConocimiento.objects.filter(clave__in=legacy_source_ids)
        }
        if set(legacy_sources) != legacy_source_ids:
            raise InstallationError(
                "Los paquetes con índice v1 requieren que todas sus fuentes ya estén registradas localmente."
            )
        for source in legacy_sources.values():
            if (
                not source.activa
                or source.estado_revision_licencia not in {"compatible", "solo_referencia"}
                or not source.evidencia_licencia
                or not source.revisada_en
                or not source.nota_revision_licencia.strip()
                or (
                    source.estado_revision_licencia == "compatible"
                    and not source.alcance_licencia.strip()
                )
            ):
                raise InstallationError(
                    f"La fuente local '{source.titulo}' no conserva una revisión de licencia válida para instalar un índice v1."
                )
        for payload in archive["payloads"].values():
            legacy_document = load_strict_json(
                payload, max_bytes=MAX_DOCUMENT_BYTES
            )
            for source_reference in legacy_document["fuentes"]:
                source = legacy_sources[source_reference["clave"]]
                if (
                    source.estado_revision_licencia == "solo_referencia"
                    and source_reference["uso_declarado"] != "original"
                ):
                    raise InstallationError(
                        f"La fuente local '{source.titulo}' solo permite contenido original."
                    )
    manifest_package = manifest["package"]
    package_id = UUID(manifest_package["package_id"])
    if PaqueteConocimientoInstalado.objects.filter(package_id=package_id).exists():
        raise InstallationError("El UUID del paquete ya está registrado con otra secuencia.")

    storage_key, artifact_path, artifact_created = _persist_artifact(
        package_bytes,
        channel=expected_channel,
        package_id=package_id,
        digest=manifest_package["sha256"],
    )
    try:
        published_at = datetime.fromisoformat(
            manifest["published_at"].replace("Z", "+00:00")
        )
        package = PaqueteConocimientoInstalado.objects.create(
            package_id=package_id,
            package_version=manifest_package["package_version"],
            channel=expected_channel,
            sequence=manifest["sequence"],
            content_schema_version=manifest["content_schema_version"],
            sha256=manifest_package["sha256"],
            manifest_sha256=verified["manifest_sha256"],
            signature_key_id=manifest["key_id"],
            published_at=published_at,
            artifact_storage_key=storage_key,
        )
        package.estado = "verificado"
        package.save()

        for lesson, document, payload_digest in curriculum:
            ContenidoLeccionPaquete.objects.create(
                paquete=package,
                leccion=lesson,
                documento=document,
                sha256=payload_digest,
            )

        for source_uuid, metadata in archive["sources"].items():
            FuentePaqueteConocimiento.objects.create(
                paquete=package,
                source_uuid=UUID(source_uuid),
                metadatos=metadata,
            )

        previous = state.active_package
        if previous is not None:
            previous.estado = "sustituido"
            previous.save()

        package.estado = "activo"
        package.installed_at = timezone.now()
        package.save()

        state.active_package = package
        state.last_check_at = timezone.now()
        state.last_success_at = state.last_check_at
        state.last_error_code = ""
        state.manifest_etag = manifest_etag
        state.save()

        return {
            "installed": True,
            "unchanged": False,
            "package": package,
            "state": state,
            "lesson_count": len(curriculum),
            "source_count": len(archive["sources"]),
        }
    except Exception:
        if artifact_created:
            try:
                artifact_path.unlink(missing_ok=True)
            except OSError:
                pass
        raise


@transaction.atomic
def restaurar_paquete_anterior(*, channel: str, package_id):
    """Reactiva un paquete sustituido conservando todos los intentos y snapshots."""
    if channel not in {"stable", "beta"}:
        raise InstallationError("El canal solicitado no está permitido.")
    state = (
        EstadoSincronizacion.objects.select_for_update()
        .select_related("active_package")
        .filter(channel=channel)
        .first()
    )
    if state is None or state.active_package_id is None:
        raise InstallationError("No existe un paquete activo para realizar rollback.")

    target = (
        PaqueteConocimientoInstalado.objects.select_for_update()
        .filter(channel=channel, package_id=package_id, estado="sustituido")
        .first()
    )
    if target is None:
        raise InstallationError("El paquete de rollback no existe o no está sustituido.")
    if not target.contenidos_leccion.exists():
        raise InstallationError("El paquete anterior no conserva sus snapshots académicos.")
    stored_bytes = _read_artifact(target.artifact_storage_key)
    if hashlib.sha256(stored_bytes).hexdigest() != target.sha256:
        raise InstallationError("El artefacto del paquete anterior no supera la verificación SHA-256.")

    current = state.active_package
    current.estado = "sustituido"
    current.save()
    target.estado = "activo"
    target.save()
    state.active_package = target
    state.last_success_at = timezone.now()
    state.last_error_code = ""
    state.save()
    return target
