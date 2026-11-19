"""Restauración transaccional de copias de seguridad locales.

La restauración sustituye la base de datos y ``media/`` del perfil por el
contenido de un ZIP previamente validado. Se ejecuta en dos fases:

1. Validación y extracción a un directorio de staging en el mismo volumen.
2. Intercambio atómico con el perfil actual, conservando una copia de
   reversión completa para poder deshacer cualquier fallo.

Requisitos de seguridad:

- La aplicación (Electron y el servidor Django) debe estar detenida antes de
  invocar la restauración. Este módulo cierra las conexiones Django abiertas,
  pero no puede garantizar que otro proceso no esté usando la base.
- Nunca se extrae directamente sobre el perfil.
- No se restaura ``.secret_key`` ni los logs: el perfil conserva su clave local
  y sus registros. La base restaurada se migrará en el siguiente arranque.
- Se rechazan versiones de esquema futuras (migraciones desconocidas) y los
  archivos que no cumplan el formato de ``apps.core.backup``.
"""
from __future__ import annotations

import os
import shutil
import sqlite3
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from django.db import connections

from apps.core.backup import (
    BackupError,
    _check_sqlite,
    _validate_payload_path,
    inspect_backup,
)

PROFILE_DATABASE = "db.sqlite3"
PROFILE_MEDIA = "media"


class RestoreError(BackupError):
    """La copia no puede restaurarse de forma segura."""


def _resolve_profile(data_dir: str | os.PathLike | None) -> Path:
    raw = Path(data_dir or os.environ.get("CODEGUARD_DATA_DIR", "data")).expanduser()
    if raw.is_symlink():
        raise RestoreError("La carpeta de datos no puede ser un enlace simbólico.")
    root = raw.resolve()
    if not root.parent.is_dir():
        raise RestoreError("La carpeta contenedora del perfil no existe.")
    return root


def _close_connections() -> None:
    """Cierra las conexiones Django para liberar la base antes de sustituirla."""
    try:
        connections.close_all()
    except Exception as exc:  # pragma: no cover - defensivo
        raise RestoreError("No se pudieron cerrar las conexiones de base de datos.") from exc


def _disk_migrations() -> set[tuple[str, str]]:
    """Migraciones conocidas por el código actual, sin consultar la base."""
    from django.db.migrations.loader import MigrationLoader

    loader = MigrationLoader(None, ignore_no_migrations=True)
    return set(loader.disk_migrations)


def _check_schema(database: Path) -> tuple[int, int]:
    """Valida que la base restaurada no pertenezca a un esquema futuro.

    Devuelve ``(aplicadas, pendientes)``. Las migraciones pendientes son
    aceptables: el servidor empaquetado las aplica al arrancar. Una migración
    desconocida indica un esquema más nuevo que este binario y se rechaza.
    """
    try:
        with sqlite3.connect(str(database)) as connection:
            tables = {
                row[0]
                for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )
            }
            if "django_migrations" not in tables:
                raise RestoreError(
                    "La base restaurada no contiene el historial de migraciones de Django."
                )
            applied = {
                (row[0], row[1])
                for row in connection.execute(
                    "SELECT app, name FROM django_migrations"
                )
            }
    except RestoreError:
        raise
    except sqlite3.DatabaseError as exc:
        raise RestoreError("La base restaurada no se puede leer.") from exc

    disk = _disk_migrations()
    unknown = applied - disk
    if unknown:
        detalle = ", ".join(f"{app}.{name}" for app, name in sorted(unknown)[:3])
        raise RestoreError(
            "La copia pertenece a una versión más reciente de CodeGuard Pro "
            f"(migraciones desconocidas: {detalle})."
        )
    return len(applied), len(disk - applied)


def _extract_payload(archive_path: Path, staging: Path) -> None:
    """Extrae únicamente la base y media/ validados a un directorio nuevo."""
    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            for info in archive.infolist():
                if info.filename == "manifest.json":
                    continue
                name = _validate_payload_path(info.filename)
                target = staging / Path(*name.split("/"))
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info, "r") as source, target.open("wb") as destination:
                    shutil.copyfileobj(source, destination, length=1024 * 1024)
    except BackupError:
        raise
    except (OSError, zipfile.BadZipFile) as exc:
        raise RestoreError("No se pudo extraer la copia de seguridad.") from exc


def _remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.is_dir():
        shutil.rmtree(path)


def _publish_profile(
    root: Path, staging: Path, rollback: Path, moved: list[str], published: list[str]
) -> None:
    """Sustituye base y media conservando los originales en ``rollback``.

    ``moved`` y ``published`` se actualizan tras cada operación para que el
    llamador pueda revertir con precisión aunque el intercambio falle a medias.
    """
    for name in (PROFILE_DATABASE, PROFILE_MEDIA):
        current = root / name
        if current.is_symlink():
            raise RestoreError(f"El perfil actual contiene un enlace simbólico: {name}.")
        if current.exists():
            rollback.mkdir(parents=True, exist_ok=True)
            os.replace(current, rollback / name)
            moved.append(name)

    os.replace(staging / "database.sqlite3", root / PROFILE_DATABASE)
    published.append(PROFILE_DATABASE)
    staged_media = staging / PROFILE_MEDIA
    if staged_media.exists():
        os.replace(staged_media, root / PROFILE_MEDIA)
        published.append(PROFILE_MEDIA)
    else:
        # Un backup sin archivos multimedia sigue representando un perfil
        # válido; se deja media/ vacío para no romper rutas de la aplicación.
        (root / PROFILE_MEDIA).mkdir(exist_ok=True)


def _rollback(
    root: Path, rollback: Path, moved: list[str], published: list[str]
) -> None:
    """Restaura el perfil anterior; se ejecuta solo si el intercambio falló."""
    for name in published:
        _remove_path(root / name)
    for name in moved:
        previous = rollback / name
        if previous.exists():
            os.replace(previous, root / name)


def restore_backup(
    archive_path: str | os.PathLike,
    *,
    data_dir: str | os.PathLike | None = None,
    confirm: bool = False,
    max_entries: int = 10_000,
    max_file_size: int = 512 * 1024 * 1024,
    max_total_size: int = 2 * 1024 * 1024 * 1024,
) -> dict:
    """Restaura un backup validado sobre el perfil local.

    ``confirm=True`` es obligatorio para evitar sobrescrituras accidentales.
    Devuelve un resumen con el manifiesto, migraciones aplicadas/pendientes y
    la ruta de la copia de reversión (si existía un perfil previo).
    """
    if not confirm:
        raise RestoreError(
            "La restauración reemplaza la base y media actuales. "
            "Repite el comando con --confirm tras cerrar CodeGuard Pro."
        )

    root = _resolve_profile(data_dir)
    archive = Path(archive_path).expanduser()
    if archive.is_symlink() or not archive.is_file():
        raise RestoreError("El archivo de backup no existe o no es seguro.")
    archive = archive.resolve()
    if archive == root or root in archive.parents:
        raise RestoreError(
            "El archivo de backup está dentro del perfil que se va a reemplazar. "
            "Muévelo fuera antes de restaurar."
        )

    manifest = inspect_backup(
        archive,
        max_entries=max_entries,
        max_file_size=max_file_size,
        max_total_size=max_total_size,
    )

    root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".codeguard-restore-", dir=root.parent))
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rollback = root / f".restore-rollback-{timestamp}"
    moved: list[str] = []
    published: list[str] = []
    try:
        _extract_payload(archive, staging)
        applied, pending = _check_schema(staging / "database.sqlite3")

        _close_connections()
        for suffix in ("-wal", "-shm"):
            (root / f"{PROFILE_DATABASE}{suffix}").unlink(missing_ok=True)

        _publish_profile(root, staging, rollback, moved, published)
        # Verificación final sobre la base ya publicada.
        _check_sqlite(root / PROFILE_DATABASE)
        _close_connections()

        rollback_path = str(rollback) if moved else None
        if not moved:
            shutil.rmtree(rollback, ignore_errors=True)
        return {
            "manifest": manifest,
            "rollback_path": rollback_path,
            "applied_migrations": applied,
            "pending_migrations": pending,
        }
    except Exception:
        _close_connections()
        _rollback(root, rollback, moved, published)
        raise
    finally:
        shutil.rmtree(staging, ignore_errors=True)
