"""Punto de entrada del servidor Django empaquetado para CodeGuard Pro.

Electron inicia este binario (generado con PyInstaller) para servir Django localmente o, con
``--sync-knowledge``, para ejecutar una única comprobación de conocimiento y terminar.
El modo servidor sirve la aplicación mediante Waitress + WhiteNoise.
El modo de sincronización no ejecuta migraciones, no inicia Waitress y no modifica el roadmap.
El servidor escucha exclusivamente en 127.0.0.1.

Nota: las migraciones y la carga del roadmap ASCENSO se ejecutan por separado desde
``manage.py`` antes de iniciar Electron (ver ``run.sh``). El servidor empaquetado asume
que la base de datos ya está inicializada.
"""

from __future__ import annotations

import os
import sys
import traceback


def _die(message: str, code: int = 1) -> int:
    """Imprime un error y sale con el código dado."""
    print(f"[CodeGuard ERROR] {message}", file=sys.stderr, flush=True)
    traceback.print_exc(file=sys.stderr)
    return code


def main() -> int:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")

    print("[CodeGuard] Iniciando servidor Django empaquetado...", flush=True)

    try:
        import django
        print("[CodeGuard] Django importado correctamente.", flush=True)
    except Exception as exc:
        return _die(f"No se pudo importar Django: {exc}", 2)

    try:
        django.setup()
        print("[CodeGuard] Django configurado correctamente.", flush=True)
    except Exception as exc:
        return _die(f"No se pudo configurar Django: {exc}", 3)

    # El sincronizador se ejecuta en un proceso separado y no toca el servidor,
    # las migraciones ni el roadmap. El servidor principal ya administra esos pasos.
    if sys.argv[1:] == ["--sync-knowledge"]:
        from django.core.management import call_command

        try:
            channel_raw = os.environ.get("CODEGUARD_SYNC_CHANNEL", "").strip()
            channel = channel_raw if channel_raw else "stable"
            force = os.environ.get("CODEGUARD_SYNC_FORCE", "").strip().lower() in {"1", "true", "yes"}
            call_command(
                "sincronizar_conocimiento",
                channel=channel,
                force=force,
                verbosity=1,
            )
            return 0
        except Exception as exc:
            print(f"[CodeGuard Sync] {exc}", file=sys.stderr, flush=True)
            traceback.print_exc(file=sys.stderr)
            return 1

    port = os.environ.get("CODEGUARD_PORT", "8000").strip() or "8000"
    print(f"[CodeGuard] Puerto: {port}", flush=True)

    try:
        from config.wsgi import application
        print("[CodeGuard] Aplicación WSGI cargada correctamente.", flush=True)
    except Exception as exc:
        return _die(f"No se pudo importar config.wsgi: {exc}", 5)

    try:
        from waitress import serve
        print("[CodeGuard] Waitress importado correctamente.", flush=True)
    except Exception as exc:
        return _die(f"No se pudo importar waitress: {exc}", 6)

    try:
        print(f"[CodeGuard] Sirviendo en http://127.0.0.1:{port}/ ...", flush=True)
        serve(
            application,
            host="127.0.0.1",
            port=int(port),
        )
    except Exception as exc:
        print(f"[CodeGuard] Error iniciando el servidor Waitress: {exc}", file=sys.stderr, flush=True)
        traceback.print_exc(file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())