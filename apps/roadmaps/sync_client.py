"""Cliente HTTP pull-only para sincronizar paquetes de conocimiento firmados.

No envía datos del estudiante. Descarga manifiesto y firma, verifica el manifiesto
antes de solicitar el ZIP y delega la instalación al servicio transaccional.
"""
from __future__ import annotations

import hashlib
import logging
import os
import ssl
from contextlib import contextmanager
from datetime import timedelta
import urllib.error
import urllib.request
from urllib.parse import urlsplit

from django.conf import settings
from django.utils import timezone

from .distribution import (
    MAX_MANIFEST_BYTES,
    MAX_PACKAGE_BYTES,
    MAX_SIGNATURE_BYTES,
    DistributionError,
    verify_signed_manifest,
)
from .installer import InstallationError, instalar_paquete_firmado
from .models import EstadoSincronizacion, PaqueteConocimientoInstalado


logger = logging.getLogger("codeguard.sync")

DEFAULT_TIMEOUT_SECONDS = 12
MAX_TIMEOUT_SECONDS = 60
INITIAL_RETRY_DELAY = timedelta(minutes=15)
MAX_RETRY_DELAY = timedelta(hours=24)
SUCCESS_CHECK_INTERVAL = timedelta(hours=24)
DOWNLOAD_CHUNK_BYTES = 64 * 1024


class SyncClientError(ValueError):
    """Error controlado de configuración o transporte de sincronización."""

    def __init__(self, message, *, code="sync_error"):
        super().__init__(message)
        self.code = code


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Los artefactos firmados no siguen redirecciones HTTP."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise SyncClientError(
            "El servidor intentó redirigir una descarga; las redirecciones están deshabilitadas.",
            code="redirect_rejected",
        )


def _validate_endpoint(url, *, allowed_hosts, label):
    if not isinstance(url, str) or not url or len(url) > 2048:
        raise SyncClientError(f"{label}: URL ausente o demasiado larga.", code="configuration_error")
    if any(character.isspace() for character in url):
        raise SyncClientError(f"{label}: la URL contiene espacios.", code="configuration_error")
    try:
        parsed = urlsplit(url)
        hostname = parsed.hostname
        port = parsed.port
    except ValueError as exc:
        raise SyncClientError(f"{label}: URL malformada.", code="configuration_error") from exc
    hosts = {str(host).lower().rstrip(".") for host in allowed_hosts}
    if (
        parsed.scheme.lower() != "https"
        or not hostname
        or hostname.lower().rstrip(".") not in hosts
        or parsed.username
        or parsed.password
        or "@" in parsed.netloc
        or parsed.fragment
        or port not in {None, 443}
    ):
        raise SyncClientError(
            f"{label}: se requiere HTTPS, host autorizado y ausencia de credenciales/fragmentos.",
            code="configuration_error",
        )
    return url


def _open_url(request, *, timeout):
    opener = urllib.request.build_opener(
        _NoRedirectHandler(),
        urllib.request.HTTPSHandler(context=ssl.create_default_context()),
    )
    return opener.open(request, timeout=timeout)


def _read_response(response, *, max_bytes, expected_size=None):
    status = response.status if hasattr(response, "status") else response.getcode()
    if status != 200:
        raise SyncClientError(
            f"El servidor respondió con HTTP {status}.",
            code="http_error",
        )

    header_length = response.headers.get("Content-Length")
    if header_length is not None:
        try:
            declared_length = int(header_length)
        except (TypeError, ValueError) as exc:
            raise SyncClientError("Content-Length inválido.", code="invalid_response") from exc
        if declared_length < 0 or declared_length > max_bytes:
            raise SyncClientError("La respuesta supera el límite de tamaño.", code="size_limit")
        if expected_size is not None and declared_length != expected_size:
            raise SyncClientError("Content-Length no coincide con el tamaño firmado.", code="size_mismatch")

    chunks = []
    total = 0
    while True:
        chunk = response.read(min(DOWNLOAD_CHUNK_BYTES, max_bytes + 1 - total))
        if not chunk:
            break
        total += len(chunk)
        if total > max_bytes:
            raise SyncClientError("La respuesta supera el límite de tamaño.", code="size_limit")
        chunks.append(chunk)
    if expected_size is not None and total != expected_size:
        raise SyncClientError("El tamaño descargado no coincide con el manifiesto firmado.", code="size_mismatch")
    return b"".join(chunks)


def _fetch_bytes(url, *, allowed_hosts, timeout, max_bytes, headers=None, expected_size=None, allow_not_modified=False):
    _validate_endpoint(url, allowed_hosts=allowed_hosts, label="Endpoint")
    request_headers = {
        "Accept": "application/octet-stream",
        "User-Agent": "CodeGuard-Pro-Knowledge-Sync",
        "Cache-Control": "no-cache",
    }
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, headers=request_headers, method="GET")
    try:
        with _open_url(request, timeout=timeout) as response:
            final_url = response.geturl()
            if final_url != url:
                raise SyncClientError("La descarga cambió de URL durante la petición.", code="redirect_rejected")
            payload = _read_response(
                response, max_bytes=max_bytes, expected_size=expected_size
            )
            return payload, response.headers.get("ETag", "")
    except urllib.error.HTTPError as exc:
        if exc.code == 304:
            if allow_not_modified:
                return None, exc.headers.get("ETag", "")
            raise SyncClientError("El servidor devolvió HTTP 304 sin una descarga condicional.", code="invalid_response") from exc
        if 300 <= exc.code < 400:
            raise SyncClientError("El servidor intentó redirigir una descarga.", code="redirect_rejected") from exc
        raise SyncClientError(
            f"El servidor respondió con HTTP {exc.code}.", code="http_error"
        ) from exc
    except SyncClientError:
        raise
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise SyncClientError(
            "No fue posible conectar con el servicio de conocimiento.",
            code="network_error",
        ) from exc


def _get_sync_state(channel):
    state, _ = EstadoSincronizacion.objects.get_or_create(channel=channel)
    return state


def _retry_delay_for_state(state):
    """Calcula backoff exponencial usando el intervalo persistido, sin migración."""
    if state.last_error_code and state.last_check_at and state.next_check_after:
        previous_delay = state.next_check_after - state.last_check_at
        if previous_delay > timedelta(0):
            return min(previous_delay * 2, MAX_RETRY_DELAY)
    return INITIAL_RETRY_DELAY


def _record_failure(channel, code):
    try:
        state = _get_sync_state(channel)
        now = timezone.now()
        delay = _retry_delay_for_state(state)
        state.last_check_at = now
        state.last_error_code = code[:80]
        state.next_check_after = now + delay
        state.save()
    except Exception:
        logger.exception("No fue posible registrar el error de sincronización (%s).", code)


@contextmanager
def _channel_sync_lock(channel):
    """Bloqueo entre procesos, válido en Windows y POSIX, dentro del directorio de datos."""
    lock_path = settings.DATA_DIR / f".knowledge-sync-{channel}.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = open(lock_path, "a+b")
    locked = False
    try:
        if os.name == "nt":
            import msvcrt

            handle.seek(0, os.SEEK_END)
            if handle.tell() == 0:
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                locked = True
            except OSError as exc:
                raise SyncClientError(
                    "Ya existe una sincronización activa para este canal.",
                    code="sync_in_progress",
                ) from exc
        else:
            import fcntl

            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                locked = True
            except BlockingIOError as exc:
                raise SyncClientError(
                    "Ya existe una sincronización activa para este canal.",
                    code="sync_in_progress",
                ) from exc
        yield
    finally:
        if locked:
            if os.name == "nt":
                import msvcrt

                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def _sincronizar_conocimiento_sin_bloqueo(
    *,
    channel,
    manifest_url,
    signature_url,
    trusted_public_keys,
    allowed_hosts,
    app_version,
    timeout=DEFAULT_TIMEOUT_SECONDS,
    force=False,
):
    """Consulta un canal y, si hay una publicación nueva y válida, la instala.

    El único tráfico saliente es GET a endpoints HTTPS incluidos en la allowlist.
    No se adjuntan cookies, tokens, progreso, intentos ni respuestas del estudiante.
    """
    if channel not in {"stable", "beta"}:
        raise SyncClientError("Canal de sincronización no permitido.", code="configuration_error")
    if type(timeout) not in {int, float} or not 1 <= timeout <= MAX_TIMEOUT_SECONDS:
        raise SyncClientError("Timeout fuera del intervalo permitido.", code="configuration_error")
    if not isinstance(trusted_public_keys, dict) or not trusted_public_keys:
        raise SyncClientError("No hay claves públicas de confianza configuradas.", code="trust_store_missing")
    if not isinstance(allowed_hosts, (list, tuple, set)) or not allowed_hosts:
        raise SyncClientError("No hay hosts de distribución autorizados.", code="allowlist_missing")

    _validate_endpoint(manifest_url, allowed_hosts=allowed_hosts, label="Manifiesto")
    _validate_endpoint(signature_url, allowed_hosts=allowed_hosts, label="Firma")
    state = _get_sync_state(channel)
    now = timezone.now()
    if not force and state.next_check_after and now < state.next_check_after:
        return {
            "status": "deferred",
            "reason": "backoff",
            "active_package": state.active_package,
        }

    latest = (
        PaqueteConocimientoInstalado.objects.filter(channel=channel)
        .order_by("-sequence")
        .first()
    )
    current_sequence = latest.sequence if latest else 0
    current_manifest_hash = latest.manifest_sha256 if latest else None
    request_headers = {}
    if state.manifest_etag:
        request_headers["If-None-Match"] = state.manifest_etag

    try:
        manifest_bytes, response_etag = _fetch_bytes(
            manifest_url,
            allowed_hosts=allowed_hosts,
            timeout=timeout,
            max_bytes=MAX_MANIFEST_BYTES,
            headers=request_headers,
            allow_not_modified=True,
        )
        if manifest_bytes is None:
            if not request_headers:
                raise SyncClientError("El servidor devolvió HTTP 304 sin una petición condicional.", code="invalid_response")
            if response_etag and len(response_etag) > 255:
                raise SyncClientError("ETag demasiado largo.", code="invalid_response")
            if response_etag:
                state.manifest_etag = response_etag
            state.last_check_at = now
            state.last_success_at = now
            state.last_error_code = ""
            state.next_check_after = now + SUCCESS_CHECK_INTERVAL
            state.save()
            return {
                "status": "not_modified",
                "active_package": state.active_package,
            }

        signature_bytes, _ = _fetch_bytes(
            signature_url,
            allowed_hosts=allowed_hosts,
            timeout=timeout,
            max_bytes=MAX_SIGNATURE_BYTES,
        )
        try:
            verified = verify_signed_manifest(
                manifest_bytes,
                signature_bytes,
                trusted_public_keys=trusted_public_keys,
                allowed_hosts=allowed_hosts,
                expected_channel=channel,
                app_version=app_version,
                current_sequence=current_sequence,
                current_manifest_sha256=current_manifest_hash,
            )
        except DistributionError as exc:
            raise SyncClientError(str(exc), code="manifest_rejected") from exc

        if verified["unchanged"]:
            state.last_check_at = now
            state.last_success_at = now
            state.last_error_code = ""
            state.next_check_after = now + SUCCESS_CHECK_INTERVAL
            if len(response_etag) > 255:
                raise SyncClientError("ETag demasiado largo.", code="invalid_response")
            state.manifest_etag = response_etag
            state.save()
            return {
                "status": "unchanged",
                "active_package": state.active_package,
            }

        manifest = verified["manifest"]
        if response_etag and len(response_etag) > 255:
            raise SyncClientError("ETag demasiado largo.", code="invalid_response")
        package_meta = manifest["package"]
        package_bytes, _ = _fetch_bytes(
            package_meta["url"],
            allowed_hosts=allowed_hosts,
            timeout=timeout,
            max_bytes=min(MAX_PACKAGE_BYTES, package_meta["size_bytes"]),
            expected_size=package_meta["size_bytes"],
        )
        if hashlib.sha256(package_bytes).hexdigest() != package_meta["sha256"]:
            raise SyncClientError("El ZIP descargado no coincide con el hash firmado.", code="package_hash_mismatch")

        result = instalar_paquete_firmado(
            manifest_bytes,
            signature_bytes,
            package_bytes,
            trusted_public_keys=trusted_public_keys,
            allowed_hosts=allowed_hosts,
            expected_channel=channel,
            app_version=app_version,
            manifest_etag=response_etag,
        )
        return {"status": "installed" if result["installed"] else "unchanged", **result}
    except SyncClientError as exc:
        _record_failure(channel, exc.code)
        raise
    except InstallationError as exc:
        _record_failure(channel, "installation_rejected")
        raise SyncClientError(str(exc), code="installation_rejected") from exc
    except Exception:
        _record_failure(channel, "sync_internal_error")
        logger.exception("Fallo inesperado en la sincronización del canal %s.", channel)
        raise SyncClientError(
            "La sincronización terminó con un error interno; el contenido local se conserva.",
            code="sync_internal_error",
        )



def sincronizar_conocimiento(**kwargs):
    """Ejecuta una sola sincronización por canal y directorio de datos."""
    channel = kwargs.get("channel")
    if channel not in {"stable", "beta"}:
        raise SyncClientError("Canal de sincronización no permitido.", code="configuration_error")
    with _channel_sync_lock(channel):
        return _sincronizar_conocimiento_sin_bloqueo(**kwargs)
