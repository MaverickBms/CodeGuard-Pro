"""Interfaz local de creación y verificación de copias de seguridad.

La restauración no se ejecuta desde esta vista: reemplazar la base con el
servidor Django en marcha no es seguro. La pantalla explica el procedimiento
CLI y exige cerrar la aplicación antes de restaurar.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from apps.accounts.identity import (
    obtener_actor_auditoria,
    obtener_usuario_local,
    requiere_acceso,
)
from apps.audit.services import registrar_evento
from apps.core.backup import BackupError, create_backup, inspect_backup


def _backup_dir() -> Path:
    """Carpeta de backups fuera del perfil, estable entre ejecuciones."""
    return Path(settings.DATA_DIR).expanduser().resolve().parent / "CodeGuard Backups"


def _archivos(directory: Path) -> list[dict]:
    if not directory.is_dir():
        return []
    archivos = []
    for path in sorted(
        directory.glob("*.zip"), key=lambda item: item.stat().st_mtime, reverse=True
    ):
        try:
            stat = path.stat()
        except OSError:
            continue
        archivos.append(
            {
                "nombre": path.name,
                "tamano_mb": round(stat.st_size / (1024 * 1024), 2),
                "modificado": datetime.fromtimestamp(stat.st_mtime),
            }
        )
    return archivos


def _destino_nuevo(directory: Path) -> Path:
    marca = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    destino = directory / f"CodeGuard-backup-{marca}.zip"
    contador = 2
    while destino.exists():
        destino = directory / f"CodeGuard-backup-{marca}-{contador}.zip"
        contador += 1
    return destino


@requiere_acceso
def backups(request):
    """Crea y verifica copias locales; nunca restaura con el servidor activo."""
    directory = _backup_dir()
    error_entorno = None
    try:
        directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    except OSError:
        error_entorno = (
            "No se pudo preparar la carpeta de copias. Revisa los permisos del "
            "directorio de datos."
        )

    if request.method == "POST" and error_entorno is None:
        accion = (request.POST.get("accion") or "").strip()

        if accion == "crear":
            destino = _destino_nuevo(directory)
            try:
                manifest = create_backup(destino, data_dir=settings.DATA_DIR)
            except (BackupError, OSError) as exc:
                messages.error(request, f"No se pudo crear la copia: {exc}")
            else:
                registrar_evento(
                    "backup_creado",
                    usuario=obtener_actor_auditoria(request),
                    descripcion=(
                        "Copia de seguridad creada desde la interfaz local "
                        f"({len(manifest['files'])} archivos)."
                    ),
                )
                messages.success(
                    request,
                    f"Copia creada y verificada: {destino.name}",
                )
            return redirect("core:backups")

        if accion == "verificar":
            nombre = (request.POST.get("archivo") or "").strip()
            candidato = (directory / nombre).resolve()
            if (
                not nombre
                or Path(nombre).name != nombre
                or candidato.parent != directory.resolve()
                or candidato.suffix.lower() != ".zip"
            ):
                messages.error(request, "El archivo seleccionado no es válido.")
            elif not candidato.is_file():
                messages.error(request, "El archivo seleccionado no existe.")
            else:
                try:
                    manifest = inspect_backup(candidato)
                except (BackupError, OSError) as exc:
                    messages.error(request, f"La copia no superó la verificación: {exc}")
                else:
                    messages.success(
                        request,
                        "Copia verificada correctamente "
                        f"({len(manifest['files'])} archivos, "
                        f"{manifest['created_at']}).",
                    )
            return redirect("core:backups")

        messages.error(request, "Acción de backup no reconocida.")
        return redirect("core:backups")

    usuario = obtener_usuario_local(request)
    return render(
        request,
        "core/backups.html",
        {
            "backup_dir": directory,
            "archivos": _archivos(directory),
            "error_entorno": error_entorno,
            "usuario_disponible": usuario is not None,
        },
    )
