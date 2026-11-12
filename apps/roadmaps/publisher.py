"""Generación reproducible y firma de paquetes académicos aprobados.

Este módulo solo publica snapshots editoriales activos. No descarga fuentes, no
ejecuta contenido y no despliega artefactos a un proveedor remoto.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import re
import stat
import tempfile
import uuid
import zipfile
from datetime import timezone as datetime_timezone
from pathlib import Path
from urllib.parse import urlsplit

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.utils import timezone

from .distribution import (
    validate_manifest_structure, validate_package_archive, verify_signed_manifest,
)
from .models import (
    ContenidoLeccionActivo,
    PublicacionPaqueteConocimiento,
    SecuenciaPublicacionConocimiento,
)


class PublicationError(ValueError):
    """No se puede construir o registrar una publicación segura."""


def _json_bytes(value):
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _safe_https_base_url(base_url, allowed_hosts):
    try:
        parsed = urlsplit(base_url)
        hostname = parsed.hostname
        port = parsed.port
    except (TypeError, ValueError) as exc:
        raise PublicationError("La URL base de distribución no es válida.") from exc
    hosts = {host.lower().rstrip(".") for host in allowed_hosts}
    if (
        parsed.scheme.lower() != "https"
        or not hostname
        or hostname.lower().rstrip(".") not in hosts
        or parsed.username
        or parsed.password
        or "@" in parsed.netloc
        or parsed.fragment
        or port not in {None, 443}
        or parsed.query
    ):
        raise PublicationError(
            "La URL base debe usar HTTPS, un host autorizado y no incluir credenciales, puerto alterno, query o fragmento."
        )
    return base_url.rstrip("/")


def _load_signing_key(private_key_path, password=None):
    path = Path(private_key_path).expanduser()
    if path.is_symlink() or not path.is_file():
        raise PublicationError("La clave privada debe ser un archivo regular externo al repositorio.")
    repository_root = Path(__file__).resolve().parents[2]
    try:
        path.resolve().relative_to(repository_root)
    except ValueError:
        pass
    else:
        raise PublicationError("La clave privada no puede ubicarse dentro del repositorio.")
    if os.name == "posix" and stat.S_IMODE(path.stat().st_mode) & 0o077:
        raise PublicationError("La clave privada debe tener permisos exclusivos para su propietario (por ejemplo, 0600).")
    try:
        key = serialization.load_pem_private_key(
            path.read_bytes(),
            password=password.encode("utf-8") if isinstance(password, str) else password,
        )
    except (OSError, ValueError, TypeError, UnsupportedAlgorithm) as exc:
        raise PublicationError("No se pudo cargar la clave privada PEM.") from exc
    if not isinstance(key, Ed25519PrivateKey):
        raise PublicationError("La clave privada configurada no es Ed25519.")
    return key


def _validate_published_version(version):
    if version.estado != "publicada":
        raise PublicationError("Solo se empaquetan versiones editoriales publicadas.")
    snapshot = version.snapshot
    if not isinstance(snapshot, dict) or snapshot.get("esquema_version") != 1:
        raise PublicationError(f"La versión {version.pk} tiene un snapshot académico incompatible.")
    digest = hashlib.sha256(_json_bytes(snapshot)).hexdigest()
    if digest != version.sha256:
        raise PublicationError(f"La versión {version.pk} no supera la verificación SHA-256 del snapshot.")
    if snapshot.get("leccion", {}).get("clave") != str(version.leccion.clave_contenido):
        raise PublicationError(f"La versión {version.pk} no coincide con la identidad curricular.")
    references = list(version.referencias.select_related(
        "fuente", "licencia_revisada_por_snapshot"
    ).order_by("fuente__clave"))
    if not references:
        raise PublicationError(f"La versión {version.pk} no tiene procedencia documental.")

    sources = []
    for reference in references:
        source = reference.fuente
        state = reference.estado_licencia_snapshot
        if not source.activa:
            raise PublicationError(f"La fuente '{source.titulo}' está inactiva.")
        current = (
            source.estado_revision_licencia,
            source.evidencia_licencia,
            source.alcance_licencia,
            source.nota_revision_licencia,
            source.revisada_por_id,
            source.revisada_en,
        )
        frozen = (
            state,
            reference.evidencia_licencia_snapshot,
            reference.alcance_licencia_snapshot,
            reference.nota_licencia_snapshot,
            reference.licencia_revisada_por_snapshot_id,
            reference.licencia_revisada_en_snapshot,
        )
        if current != frozen:
            raise PublicationError(
                f"La licencia de la fuente '{source.titulo}' cambió después de la revisión editorial."
            )
        if state not in {"compatible", "solo_referencia"}:
            raise PublicationError(
                f"La fuente '{source.titulo}' no tiene una decisión de licencia publicable."
            )
        if not reference.evidencia_licencia_snapshot or not reference.nota_licencia_snapshot:
            raise PublicationError(f"La fuente '{source.titulo}' carece de evidencia de licencia.")
        if state == "compatible" and not reference.alcance_licencia_snapshot.strip():
            raise PublicationError(f"La fuente '{source.titulo}' carece del alcance autorizado.")
        if state == "solo_referencia" and reference.uso_declarado != "original":
            raise PublicationError(
                f"La fuente '{source.titulo}' solo permite contenido original de CodeGuard."
            )
        sources.append({
            "clave": str(source.clave),
            "rol": reference.rol,
            "localizador": reference.localizador,
            "nota_atribucion": reference.nota_atribucion,
            "uso_declarado": reference.uso_declarado,
        })

    document = {
        "schema_version": 1,
        "resumen_cambios": version.resumen_cambios,
        "snapshot": snapshot,
        "fuentes": sources,
    }
    return _json_bytes(document)


def _build_deterministic_zip(package_id, package_version, documents):
    entries = []
    for lesson_uuid, payload in sorted(documents, key=lambda item: item[0]):
        path = f"payload/lessons/{lesson_uuid}.json"
        entries.append({
            "path": path,
            "size_bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
        })
    index = {
        "schema_version": 1,
        "package_id": str(package_id),
        "package_version": package_version,
        "content_schema_version": 1,
        "files": entries,
    }
    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        ordered = [("package-index.json", _json_bytes(index))]
        ordered.extend(
            (f"payload/lessons/{lesson_uuid}.json", payload)
            for lesson_uuid, payload in sorted(documents, key=lambda item: item[0])
        )
        for name, payload in ordered:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.flag_bits = 0x800
            archive.writestr(info, payload, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def _write_temp(directory, filename, payload):
    fd, temp_name = tempfile.mkstemp(prefix=f".{filename}.", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise
    return Path(temp_name)


@transaction.atomic
def publicar_paquete_conocimiento(
    *,
    channel,
    package_version,
    minimum_app_version,
    base_url,
    allowed_hosts,
    key_id,
    private_key_path,
    output_directory,
    key_password=None,
):
    """Construye, firma y registra un paquete inmutable de snapshots activos."""
    if channel not in {"stable", "beta"}:
        raise PublicationError("El canal debe ser stable o beta.")
    if not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?",
        package_version or "",
    ):
        raise PublicationError("package_version debe usar SemVer MAJOR.MINOR.PATCH.")
    if not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?",
        minimum_app_version or "",
    ):
        raise PublicationError("minimum_app_version debe usar SemVer MAJOR.MINOR.PATCH.")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,80}", key_id or ""):
        raise PublicationError("key_id no cumple el formato permitido.")
    safe_base_url = _safe_https_base_url(base_url, allowed_hosts)
    signing_key = _load_signing_key(private_key_path, key_password)

    active_versions = list(
        ContenidoLeccionActivo.objects.select_related(
            "version", "leccion"
        ).prefetch_related(
            "version__referencias__fuente"
        ).filter(
            version__estado="publicada"
        ).order_by("leccion__clave_contenido")
    )
    if not active_versions:
        raise PublicationError("No hay lecciones con una versión editorial activa para publicar.")

    documents = []
    for pointer in active_versions:
        version = pointer.version
        if version.leccion_id != pointer.leccion_id:
            raise PublicationError("Un puntero activo no coincide con su lección.")
        payload = _validate_published_version(version)
        documents.append((str(pointer.leccion.clave_contenido), payload))

    counter, _ = SecuenciaPublicacionConocimiento.objects.get_or_create(
        channel=channel, defaults={"siguiente": 1}
    )
    counter = SecuenciaPublicacionConocimiento.objects.select_for_update().get(channel=channel)
    sequence = counter.siguiente
    counter.siguiente = sequence + 1
    counter.save(update_fields=["siguiente"])

    content_digest = hashlib.sha256(b"".join(
        lesson_uuid.encode("ascii") + b"\\0" + payload
        for lesson_uuid, payload in sorted(documents, key=lambda item: item[0])
    )).hexdigest()
    package_id = uuid.uuid5(
        uuid.NAMESPACE_URL,
        f"codeguard:{channel}:{sequence}:{package_version}:{content_digest}",
    )
    package_bytes = _build_deterministic_zip(package_id, package_version, documents)
    package_hash = hashlib.sha256(package_bytes).hexdigest()

    published_at = timezone.now().astimezone(datetime_timezone.utc)
    package_filename = f"codeguard-{channel}-{sequence}-{package_id}.zip"
    manifest_filename = f"manifest-{channel}-{sequence}.json"
    signature_filename = f"manifest-{channel}-{sequence}.ed25519"
    package_url = f"{safe_base_url}/{package_filename}"
    manifest = {
        "manifest_version": 1,
        "channel": channel,
        "sequence": sequence,
        "published_at": published_at.isoformat().replace("+00:00", "Z"),
        "minimum_app_version": minimum_app_version,
        "content_schema_version": 1,
        "package": {
            "package_id": str(package_id),
            "package_version": package_version,
            "url": package_url,
            "size_bytes": len(package_bytes),
            "sha256": package_hash,
        },
        "key_id": key_id,
    }
    manifest_bytes = _json_bytes(manifest)
    validate_manifest_structure(manifest_bytes, allowed_hosts=allowed_hosts)
    validate_package_archive(package_bytes, manifest=manifest)
    signature = base64.b64encode(signing_key.sign(manifest_bytes))
    public_bytes = signing_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )
    verify_signed_manifest(
        manifest_bytes,
        signature,
        trusted_public_keys={key_id: base64.b64encode(public_bytes).decode("ascii")},
        allowed_hosts=allowed_hosts,
        expected_channel=channel,
        app_version=minimum_app_version,
    )
    manifest_hash = hashlib.sha256(manifest_bytes).hexdigest()

    directory = Path(output_directory).expanduser()
    if directory.is_symlink():
        raise PublicationError("El directorio de salida no puede ser un symlink.")
    directory.mkdir(parents=True, exist_ok=True)
    if not directory.is_dir():
        raise PublicationError("La salida debe ser un directorio.")
    targets = [
        directory / package_filename,
        directory / manifest_filename,
        directory / signature_filename,
    ]
    if any(target.exists() or target.is_symlink() for target in targets):
        raise PublicationError("No se sobrescriben artefactos de una publicación anterior.")

    staged = []
    try:
        staged = [
            _write_temp(directory, package_filename, package_bytes),
            _write_temp(directory, manifest_filename, manifest_bytes),
            _write_temp(directory, signature_filename, signature),
        ]
        release = PublicacionPaqueteConocimiento.objects.create(
            package_id=package_id,
            package_version=package_version,
            channel=channel,
            sequence=sequence,
            content_schema_version=1,
            package_sha256=package_hash,
            manifest_sha256=manifest_hash,
            signature_key_id=key_id,
            package_url=package_url,
            package_filename=package_filename,
            manifest_filename=manifest_filename,
            signature_filename=signature_filename,
            published_at=published_at,
        )
        for temporary, target in zip(staged, targets):
            os.replace(temporary, target)
        return {
            "release": release,
            "package_path": str(targets[0]),
            "manifest_path": str(targets[1]),
            "signature_path": str(targets[2]),
            "manifest_sha256": manifest_hash,
            "package_sha256": package_hash,
            "lesson_count": len(documents),
        }
    except (OSError, IntegrityError, ValidationError) as exc:
        for temporary in staged:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
        raise PublicationError("No se pudo completar y registrar la publicación de forma íntegra.") from exc
