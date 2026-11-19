"""Creación y verificación de copias de seguridad locales de CodeGuard Pro.

El módulo no restaura perfiles ni administra la interfaz. La restauración requiere
que el servidor esté detenido y un flujo transaccional separado; no debe simularse
desde un proceso Django que mantiene abierta la base de datos.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import stat
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

FORMAT_NAME = "codeguard-backup"
FORMAT_VERSION = 1
DEFAULT_MAX_ENTRIES = 10_000
DEFAULT_MAX_FILE_SIZE = 512 * 1024 * 1024
DEFAULT_MAX_TOTAL_SIZE = 2 * 1024 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024


class BackupError(ValueError):
    """La copia no puede crearse o no supera las validaciones."""


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_archive_path(name: str) -> str:
    if not isinstance(name, str) or not name or "\\" in name:
        raise BackupError("La copia contiene una ruta inválida.")
    raw_parts = name.split("/")
    path = PurePosixPath(name)
    if name.startswith("/") or any(part in {"", ".", ".."} for part in raw_parts):
        raise BackupError("La copia contiene una ruta fuera de su raíz.")
    if path.parts and ":" in path.parts[0]:
        raise BackupError("La copia contiene una ruta absoluta no permitida.")
    return path.as_posix()


def _validate_payload_path(name: str) -> str:
    """Solo admite la base y archivos bajo media/; evita rutas arbitrarias."""
    name = _safe_archive_path(name)
    if name != "database.sqlite3" and not name.startswith("media/"):
        raise BackupError("La copia contiene un archivo fuera del conjunto permitido.")
    if name == "media/":
        raise BackupError("La copia contiene una ruta multimedia vacía.")
    return name


def _check_sqlite(path: Path) -> None:
    try:
        with sqlite3.connect(str(path)) as connection:
            result = connection.execute("PRAGMA integrity_check").fetchone()
    except sqlite3.DatabaseError as exc:
        raise BackupError("La base de datos de la copia no es válida.") from exc
    if not result or result[0] != "ok":
        raise BackupError("La comprobación de integridad de SQLite falló.")


def _iter_media_files(media_root: Path):
    if media_root.is_symlink():
        raise BackupError("La carpeta media no puede ser un enlace simbólico.")
    if not media_root.exists():
        return
    if not media_root.is_dir():
        raise BackupError("La carpeta media no es un directorio seguro.")

    def raise_walk_error(error):
        raise BackupError("No se pudo leer completamente la carpeta media.") from error

    for current, directories, filenames in os.walk(
        media_root, followlinks=False, onerror=raise_walk_error
    ):
        current_path = Path(current)
        for directory in list(directories):
            candidate = current_path / directory
            if candidate.is_symlink():
                raise BackupError("No se permiten enlaces simbólicos en media.")
        for filename in filenames:
            candidate = current_path / filename
            if candidate.is_symlink() or not candidate.is_file():
                raise BackupError("Media contiene un archivo no regular o un enlace simbólico.")
            relative = candidate.relative_to(media_root).as_posix()
            yield candidate, _validate_payload_path(f"media/{relative}")


def create_backup(
    destination: str | os.PathLike,
    *,
    data_dir: str | os.PathLike | None = None,
    codeguard_version: str = "1.0.0",
    max_entries: int = DEFAULT_MAX_ENTRIES,
    max_file_size: int = DEFAULT_MAX_FILE_SIZE,
    max_total_size: int = DEFAULT_MAX_TOTAL_SIZE,
) -> dict:
    """Crea un ZIP consistente para SQLite y verifica el artefacto antes de publicarlo.

    Se incluyen db.sqlite3 y media/. Nunca se incluye .secret_key, logs ni archivos
    WAL/SHM. El destino debe estar fuera del perfil de datos.
    """
    root_input = Path(data_dir or os.environ.get("CODEGUARD_DATA_DIR", "data")).expanduser()
    if root_input.is_symlink():
        raise BackupError("La carpeta de datos no puede ser un enlace simbólico.")
    root = root_input.resolve()
    destination_path = Path(destination).expanduser()
    if destination_path.is_symlink():
        raise BackupError("El destino no puede ser un enlace simbólico.")
    destination_path = destination_path.resolve()
    if not destination_path.parent.is_dir():
        raise BackupError("La carpeta de destino no existe.")
    if destination_path == root or root in destination_path.parents:
        raise BackupError("El backup debe guardarse fuera de la carpeta de datos.")
    if destination_path.exists():
        raise BackupError("El destino ya existe; elige otro nombre para conservar el backup anterior.")
    if max_entries < 1 or max_file_size < 1 or max_total_size < 1:
        raise BackupError("Los límites de tamaño deben ser positivos.")

    database = root / "db.sqlite3"
    if database.is_symlink() or not database.is_file():
        raise BackupError("No se encontró una base de datos local regular.")
    media_root = root / "media"
    media_files = list(_iter_media_files(media_root))
    if len(media_files) + 1 > max_entries:
        raise BackupError("El perfil contiene demasiados archivos para una copia.")

    fd, temporary_name = tempfile.mkstemp(
        prefix=".codeguard-backup-", suffix=".tmp", dir=destination_path.parent
    )
    os.close(fd)
    temporary_path = Path(temporary_name)

    try:
        with tempfile.TemporaryDirectory(prefix="codeguard-snapshot-") as work:
            snapshot = Path(work) / "database.sqlite3"
            try:
                with sqlite3.connect(str(database)) as source, sqlite3.connect(str(snapshot)) as target:
                    source.backup(target)
            except sqlite3.DatabaseError as exc:
                raise BackupError("No se pudo obtener un snapshot de SQLite.") from exc
            _check_sqlite(snapshot)

            files = []
            total_size = 0
            candidates = [(snapshot, "database.sqlite3"), *media_files]
            for source_path, archive_name in candidates:
                size = source_path.stat().st_size
                if size > max_file_size:
                    raise BackupError(f"El archivo supera el límite permitido: {archive_name}")
                total_size += size
                if total_size > max_total_size:
                    raise BackupError("El tamaño total del perfil supera el límite permitido.")
                files.append({
                    "path": archive_name,
                    "size": size,
                    "sha256": _sha256_file(source_path),
                })

            manifest = {
                "format": FORMAT_NAME,
                "format_version": FORMAT_VERSION,
                "codeguard_version": str(codeguard_version),
                "created_at": datetime.now(timezone.utc).isoformat(),
                "files": files,
            }
            with zipfile.ZipFile(temporary_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                for source_path, archive_name in candidates:
                    if source_path.is_symlink() or not source_path.is_file():
                        raise BackupError("Un archivo cambió o dejó de ser seguro durante el backup.")
                    archive.write(source_path, archive_name)
                archive.writestr(
                    "manifest.json",
                    json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8"),
                )

        verified = inspect_backup(
            temporary_path,
            max_entries=max_entries,
            max_file_size=max_file_size,
            max_total_size=max_total_size,
        )
        try:
            os.link(temporary_path, destination_path)
        except FileExistsError as exc:
            raise BackupError("El destino ya existe; no se sobrescribió.") from exc
        temporary_path.unlink()
        try:
            destination_path.chmod(stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass
        return verified
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def inspect_backup(
    archive_path: str | os.PathLike,
    *,
    max_entries: int = DEFAULT_MAX_ENTRIES,
    max_file_size: int = DEFAULT_MAX_FILE_SIZE,
    max_total_size: int = DEFAULT_MAX_TOTAL_SIZE,
) -> dict:
    """Valida estructura, límites, CRC, hashes y la integridad de SQLite."""
    path = Path(archive_path)
    if path.is_symlink() or not path.is_file():
        raise BackupError("El archivo de backup no existe o no es seguro.")
    try:
        with zipfile.ZipFile(path, "r") as archive:
            infos = archive.infolist()
            if len(infos) < 2 or len(infos) > max_entries + 1:
                raise BackupError("La copia contiene una cantidad de entradas no válida.")
            names = []
            total_size = 0
            for info in infos:
                name = _safe_archive_path(info.filename)
                if name != "manifest.json":
                    _validate_payload_path(name)
                if info.is_dir():
                    raise BackupError("No se permiten entradas de directorio explícitas.")
                if info.flag_bits & 0x1:
                    raise BackupError("No se admiten entradas ZIP cifradas.")
                if name in names:
                    raise BackupError("La copia contiene rutas duplicadas.")
                names.append(name)
                mode = (info.external_attr >> 16) & 0xFFFF
                if stat.S_ISLNK(mode):
                    raise BackupError("La copia contiene enlaces simbólicos.")
                if info.file_size > max_file_size:
                    raise BackupError("La copia supera el tamaño máximo por archivo.")
                total_size += info.file_size
                if total_size > max_total_size + 1024 * 1024:
                    raise BackupError("La copia supera el tamaño total permitido.")
            if "manifest.json" not in names or "database.sqlite3" not in names:
                raise BackupError("La copia no contiene manifiesto o base de datos.")
            if archive.testzip() is not None:
                raise BackupError("La comprobación CRC de la copia falló.")
            manifest = json.loads(archive.read("manifest.json").decode("utf-8"))
            if not isinstance(manifest, dict):
                raise BackupError("El manifiesto debe ser un objeto JSON.")
            if manifest.get("format") != FORMAT_NAME or manifest.get("format_version") != FORMAT_VERSION:
                raise BackupError("La versión del formato de backup no es compatible.")
            declared = manifest.get("files")
            if not isinstance(declared, list) or len(declared) != len(names) - 1:
                raise BackupError("El manifiesto no coincide con el contenido de la copia.")
            expected_names = set()
            for item in declared:
                if not isinstance(item, dict):
                    raise BackupError("El manifiesto contiene una entrada inválida.")
                name = _validate_payload_path(item.get("path"))
                if name in expected_names:
                    raise BackupError("El manifiesto contiene rutas duplicadas.")
                expected_names.add(name)
                if name not in names:
                    raise BackupError("Falta un archivo declarado en el manifiesto.")
                info = archive.getinfo(name)
                if item.get("size") != info.file_size:
                    raise BackupError("El tamaño de un archivo no coincide con el manifiesto.")
                digest = hashlib.sha256()
                with archive.open(info, "r") as stream:
                    for chunk in iter(lambda: stream.read(CHUNK_SIZE), b""):
                        digest.update(chunk)
                if digest.hexdigest() != item.get("sha256"):
                    raise BackupError("El hash de un archivo no coincide con el manifiesto.")
            if expected_names != set(names) - {"manifest.json"}:
                raise BackupError("La copia contiene archivos no declarados.")
            with tempfile.TemporaryDirectory(prefix="codeguard-verify-") as work:
                database = Path(work) / "database.sqlite3"
                with archive.open("database.sqlite3") as source, database.open("wb") as target:
                    shutil.copyfileobj(source, target, length=CHUNK_SIZE)
                _check_sqlite(database)
            return manifest
    except BackupError:
        raise
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError, UnicodeDecodeError, KeyError, TypeError) as exc:
        raise BackupError("El archivo de backup está dañado o tiene un formato inválido.") from exc
