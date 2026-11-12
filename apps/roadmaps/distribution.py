"""Validación criptográfica y estructural del protocolo de distribución.

Este módulo no realiza conexiones de red ni instala contenido. Verifica artefactos
recibidos; la descarga, la activación y el rollback son responsabilidades de
incrementos posteriores.
"""
from __future__ import annotations

import base64
import binascii
import hashlib
import io
import json
import re
import stat
import zipfile
from datetime import datetime
from urllib.parse import urlsplit
from uuid import UUID

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from .content_import import ImportContentError, _validate_document


MAX_MANIFEST_BYTES = 64 * 1024
MAX_SIGNATURE_BYTES = 256
MAX_PACKAGE_BYTES = 100 * 1024 * 1024
MAX_PACKAGE_FILES = 500
MAX_INDEX_BYTES = 1024 * 1024
MAX_CONTENT_FILE_BYTES = 2 * 1024 * 1024
MAX_TOTAL_UNCOMPRESSED_BYTES = 100 * 1024 * 1024
MAX_COMPRESSION_RATIO = 100
SUPPORTED_MANIFEST_VERSION = 1
SUPPORTED_CONTENT_SCHEMA_VERSION = 1
ALLOWED_CHANNELS = {"stable", "beta"}
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*))?$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LESSON_PATH_RE = re.compile(r"^payload/lessons/([0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})\.json$")


class DistributionError(ValueError):
    """Artefacto de distribución inválido o incompatible."""


def _reject_constant(value):
    raise DistributionError(f"Constante JSON no permitida: {value}.")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DistributionError(f"Clave JSON duplicada: {key}.")
        result[key] = value
    return result


def load_strict_json(raw: bytes, *, max_bytes: int):
    if not isinstance(raw, bytes) or not raw or len(raw) > max_bytes:
        raise DistributionError("El documento JSON está vacío o supera el límite permitido.")
    try:
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise DistributionError("El documento no contiene JSON UTF-8 válido.") from exc


def _exact_keys(value, required, label):
    if not isinstance(value, dict) or set(value) != set(required):
        raise DistributionError(f"{label}: el conjunto de propiedades no coincide con el esquema.")


def _positive_int(value, label, maximum=None):
    if type(value) is not int or value <= 0 or (maximum is not None and value > maximum):
        raise DistributionError(f"{label}: debe ser un entero positivo dentro del límite.")
    return value


def _semver(value, label):
    if not isinstance(value, str) or not SEMVER_RE.fullmatch(value):
        raise DistributionError(f"{label}: debe usar SemVer MAJOR.MINOR.PATCH.")
    return value


def _sha256(value, label):
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise DistributionError(f"{label}: SHA-256 hexadecimal inválido.")
    return value


def _aware_datetime(value, label):
    if not isinstance(value, str):
        raise DistributionError(f"{label}: fecha ISO-8601 requerida.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise DistributionError(f"{label}: fecha ISO-8601 inválida.") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise DistributionError(f"{label}: debe incluir zona horaria.")
    return parsed


def validate_manifest_structure(raw: bytes, *, allowed_hosts):
    """Valida el esquema y las URL sin confiar todavía en la firma."""
    manifest = load_strict_json(raw, max_bytes=MAX_MANIFEST_BYTES)
    _exact_keys(
        manifest,
        {
            "manifest_version", "channel", "sequence", "published_at",
            "minimum_app_version", "content_schema_version", "package", "key_id",
        },
        "manifest",
    )
    if type(manifest["manifest_version"]) is not int or manifest["manifest_version"] != SUPPORTED_MANIFEST_VERSION:
        raise DistributionError("Versión de manifiesto no compatible.")
    if not isinstance(manifest["channel"], str) or manifest["channel"] not in ALLOWED_CHANNELS:
        raise DistributionError("Canal de distribución no permitido.")
    _positive_int(manifest["sequence"], "sequence")
    _aware_datetime(manifest["published_at"], "published_at")
    _semver(manifest["minimum_app_version"], "minimum_app_version")
    if type(manifest["content_schema_version"]) is not int or manifest["content_schema_version"] != SUPPORTED_CONTENT_SCHEMA_VERSION:
        raise DistributionError("Versión del esquema de contenido no compatible.")
    if not isinstance(manifest["key_id"], str) or not re.fullmatch(r"[A-Za-z0-9._-]{1,80}", manifest["key_id"]):
        raise DistributionError("key_id inválido.")

    package = manifest["package"]
    _exact_keys(package, {"package_id", "package_version", "url", "size_bytes", "sha256"}, "package")
    if not isinstance(package["package_id"], str):
        raise DistributionError("package_id debe ser un UUID válido.")
    try:
        parsed_package_id = UUID(package["package_id"])
    except (ValueError, TypeError, AttributeError) as exc:
        raise DistributionError("package_id debe ser un UUID válido.") from exc
    if str(parsed_package_id) != package["package_id"]:
        raise DistributionError("package_id debe usar UUID canónico en minúsculas.")
    _semver(package["package_version"], "package_version")
    _positive_int(package["size_bytes"], "package.size_bytes", MAX_PACKAGE_BYTES)
    _sha256(package["sha256"], "package.sha256")
    if (
        not isinstance(package["url"], str)
        or len(package["url"]) > 2048
        or any(character.isspace() for character in package["url"])
    ):
        raise DistributionError("URL de paquete inválida.")
    try:
        parsed = urlsplit(package["url"])
        hostname = parsed.hostname
        _ = parsed.port
    except ValueError as exc:
        raise DistributionError("URL de paquete malformada.") from exc
    hosts = {host.lower().rstrip(".") for host in allowed_hosts}
    if (
        parsed.scheme.lower() != "https"
        or not hostname
        or hostname.lower().rstrip(".") not in hosts
        or parsed.username
        or parsed.password
        or "@" in parsed.netloc
        or parsed.fragment
        or parsed.port not in {None, 443}
    ):
        raise DistributionError("La URL debe usar HTTPS y un host autorizado, sin credenciales ni fragmentos.")
    return manifest


def verify_signed_manifest(
    manifest_bytes: bytes,
    signature_bytes: bytes,
    *,
    trusted_public_keys: dict,
    allowed_hosts,
    expected_channel: str,
    current_sequence: int = 0,
    current_manifest_sha256: str | None = None,
    app_version: str | None = None,
):
    """Verifica firma Ed25519, canal, compatibilidad y protección anti-replay."""
    manifest = validate_manifest_structure(manifest_bytes, allowed_hosts=allowed_hosts)
    if manifest["channel"] != expected_channel:
        raise DistributionError("El manifiesto pertenece a otro canal.")
    if not isinstance(signature_bytes, bytes) or not signature_bytes or len(signature_bytes) > MAX_SIGNATURE_BYTES:
        raise DistributionError("La firma supera el tamaño permitido.")
    try:
        signature = base64.b64decode(signature_bytes.strip(), validate=True)
    except (binascii.Error, ValueError) as exc:
        raise DistributionError("La firma debe estar codificada en Base64.") from exc
    if len(signature) != 64:
        raise DistributionError("La firma Ed25519 debe contener exactamente 64 bytes.")

    key_value = trusted_public_keys.get(manifest["key_id"])
    if key_value is None:
        raise DistributionError("La clave de firma no está en el almacén de confianza.")
    try:
        public_key_bytes = base64.b64decode(key_value, validate=True) if isinstance(key_value, str) else key_value
        public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)
        public_key.verify(signature, manifest_bytes)
    except (InvalidSignature, ValueError, TypeError, binascii.Error) as exc:
        raise DistributionError("La firma del manifiesto no es válida.") from exc

    manifest_digest = hashlib.sha256(manifest_bytes).hexdigest()
    if manifest["sequence"] < current_sequence:
        raise DistributionError("Se rechazó un manifiesto antiguo (downgrade/replay).")
    if manifest["sequence"] == current_sequence and current_sequence > 0:
        if current_manifest_sha256 != manifest_digest:
            raise DistributionError("La secuencia ya instalada presenta un manifiesto diferente.")
        return {"manifest": manifest, "manifest_sha256": manifest_digest, "unchanged": True}

    if app_version is not None:
        _semver(app_version, "app_version")
        if _version_tuple(app_version) < _version_tuple(manifest["minimum_app_version"]):
            raise DistributionError("El paquete requiere una versión más reciente de CodeGuard.")
    return {"manifest": manifest, "manifest_sha256": manifest_digest, "unchanged": False}


def _version_tuple(value):
    core, separator, prerelease = value.partition("-")
    numbers = tuple(int(part) for part in core.split("."))
    if not separator:
        return numbers + ((1, ()),)
    identifiers = tuple(
        (0, int(part)) if part.isdigit() else (1, part)
        for part in prerelease.split(".")
    )
    return numbers + ((0, identifiers),)


def validate_package_archive(package_bytes: bytes, *, manifest: dict):
    """Valida ZIP en memoria; nunca extrae rutas suministradas por el paquete."""
    if not isinstance(package_bytes, bytes) or not package_bytes:
        raise DistributionError("El paquete está vacío.")
    package_meta = manifest["package"]
    if len(package_bytes) != package_meta["size_bytes"] or len(package_bytes) > MAX_PACKAGE_BYTES:
        raise DistributionError("El tamaño del ZIP no coincide con el manifiesto o supera el límite.")
    if hashlib.sha256(package_bytes).hexdigest() != package_meta["sha256"]:
        raise DistributionError("El SHA-256 del paquete no coincide con el manifiesto.")

    try:
        archive = zipfile.ZipFile(io.BytesIO(package_bytes), "r")
    except (zipfile.BadZipFile, OSError) as exc:
        raise DistributionError("El artefacto no es un ZIP válido.") from exc

    with archive:
        infos = archive.infolist()
        if not infos or len(infos) > MAX_PACKAGE_FILES + 1:
            raise DistributionError("El ZIP está vacío o contiene demasiados archivos.")
        by_name = {}
        casefolded = set()
        total_uncompressed = 0
        for info in infos:
            name = info.filename
            if (
                not name
                or name.startswith(("/", "\\"))
                or "\\" in name
                or "\x00" in name
                or any(part in {"", ".", ".."} for part in name.split("/"))
                or info.is_dir()
            ):
                raise DistributionError("El ZIP contiene una ruta no permitida.")
            if name in by_name or name.casefold() in casefolded:
                raise DistributionError("El ZIP contiene nombres de archivo duplicados.")
            by_name[name] = info
            casefolded.add(name.casefold())
            mode = (info.external_attr >> 16) & 0xFFFF
            file_type = stat.S_IFMT(mode)
            if stat.S_ISLNK(mode) or file_type not in {0, stat.S_IFREG}:
                raise DistributionError("El ZIP contiene un tipo de archivo no permitido.")
            if info.compress_type not in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}:
                raise DistributionError("El ZIP utiliza un método de compresión no permitido.")
            if info.file_size <= 0 or info.file_size > MAX_CONTENT_FILE_BYTES and name != "package-index.json":
                raise DistributionError("Un archivo del ZIP está vacío o supera el límite.")
            total_uncompressed += info.file_size
            if total_uncompressed > MAX_TOTAL_UNCOMPRESSED_BYTES:
                raise DistributionError("El tamaño descomprimido total supera el límite.")
            if info.file_size / max(info.compress_size, 1) > MAX_COMPRESSION_RATIO:
                raise DistributionError("El ZIP supera el ratio de compresión permitido.")

        if "package-index.json" not in by_name:
            raise DistributionError("Falta package-index.json.")
        if by_name["package-index.json"].file_size > MAX_INDEX_BYTES:
            raise DistributionError("package-index.json supera el límite.")

        try:
            index = load_strict_json(archive.read("package-index.json"), max_bytes=MAX_INDEX_BYTES)
        except (RuntimeError, zipfile.BadZipFile, OSError) as exc:
            raise DistributionError("No se pudo leer el índice del paquete.") from exc
        _exact_keys(index, {"schema_version", "package_id", "package_version", "content_schema_version", "files"}, "package-index")
        if type(index["schema_version"]) is not int or index["schema_version"] != 1:
            raise DistributionError("Versión de índice no compatible.")
        if (
            index["package_id"] != package_meta["package_id"]
            or index["package_version"] != package_meta["package_version"]
            or type(index["content_schema_version"]) is not int
            or index["content_schema_version"] != manifest["content_schema_version"]
        ):
            raise DistributionError("La identidad del índice no coincide con el manifiesto.")
        files = index["files"]
        if not isinstance(files, list) or not 1 <= len(files) <= MAX_PACKAGE_FILES:
            raise DistributionError("El índice debe declarar entre 1 y 500 lecciones.")
        declared = set()
        payloads = {}
        seen_lessons = set()
        seen_resources = set()
        for item in files:
            _exact_keys(item, {"path", "size_bytes", "sha256"}, "package-index.files[]")
            path = item["path"]
            if not isinstance(path, str) or not LESSON_PATH_RE.fullmatch(path):
                raise DistributionError("El índice contiene una ruta de lección no permitida.")
            if path in declared:
                raise DistributionError("El índice contiene rutas duplicadas.")
            declared.add(path)
            _positive_int(item["size_bytes"], f"{path}.size_bytes", MAX_CONTENT_FILE_BYTES)
            _sha256(item["sha256"], f"{path}.sha256")
            if path not in by_name or by_name[path].file_size != item["size_bytes"]:
                raise DistributionError("Un recurso declarado falta o tiene tamaño distinto.")
            try:
                payload = archive.read(path)
            except (RuntimeError, zipfile.BadZipFile, OSError) as exc:
                raise DistributionError(f"No se pudo leer {path}.") from exc
            if hashlib.sha256(payload).hexdigest() != item["sha256"]:
                raise DistributionError(f"Hash incorrecto para {path}.")
            document = load_strict_json(payload, max_bytes=MAX_CONTENT_FILE_BYTES)
            if not isinstance(document, dict):
                raise DistributionError(f"{path}: cada recurso debe ser un documento JSON objeto.")
            try:
                lesson_uuid = _validate_document(document, path)
            except ImportContentError as exc:
                raise DistributionError(f"{path}: documento académico incompatible: {exc}") from exc
            if str(lesson_uuid) != LESSON_PATH_RE.fullmatch(path).group(1):
                raise DistributionError(f"{path}: el UUID del archivo no coincide con la identidad de la lección.")
            if lesson_uuid in seen_lessons or str(lesson_uuid) in seen_resources:
                raise DistributionError("El paquete repite o reasigna el UUID de una lección.")
            seen_lessons.add(lesson_uuid)
            for resource in document["snapshot"]["ejemplos"] + document["snapshot"]["ejercicios"]:
                resource_id = UUID(resource["clave"])
                if resource_id in seen_resources or resource_id in seen_lessons:
                    raise DistributionError("El paquete repite o reasigna un UUID de ejemplo/ejercicio.")
                seen_resources.add(resource_id)
            payloads[path] = payload

        if set(by_name) != declared | {"package-index.json"}:
            raise DistributionError("El ZIP contiene archivos no declarados en el índice.")
        return {"index": index, "payloads": payloads}
