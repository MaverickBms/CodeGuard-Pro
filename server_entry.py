"""Punto de entrada del servidor Django empaquetado para CodeGuard Pro.

Electron inicia este binario (generado con PyInstaller) para servir Django localmente o, con
``--sync-knowledge``, para ejecutar una única comprobación de conocimiento y terminar.
El modo servidor aplica migraciones, carga ASCENSO si todavía no existe y sirve la
aplicación mediante Waitress + WhiteNoise. El modo de sincronización no ejecuta
migraciones, no inicia Waitress y no modifica el roadmap. El servidor escucha
exclusivamente en 127.0.0.1.
"""

from __future__ import annotations

import os
import sys


def main() -> int:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")

    import django

    django.setup()

    from django.core.management import call_command

    # El sincronizador se ejecuta en un proceso separado y no toca el servidor,
    # las migraciones ni el roadmap. El servidor principal ya administra esos pasos.
    if sys.argv[1:] == ["--sync-knowledge"]:
        try:
            channel = os.environ.get("CODEGUARD_SYNC_CHANNEL", "stable").strip()
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
            return 1

    # Migraciones idempotentes: no destruyen datos del usuario.
    call_command("migrate", interactive=False, verbosity=0)

    # Sembrar el roadmap oficial la primera vez que se abre la aplicación.
    try:
        from apps.roadmaps.models import Roadmap
        from apps.roadmaps.services import cargar_ascenso

        if not Roadmap.objects.exists():
            cargar_ascenso()
    except Exception as exc:  # pragma: no cover - defensivo en el binario
        print(f"[CodeGuard] No se pudo cargar el roadmap inicial: {exc}", file=sys.stderr)

    if sys.argv[1:]:
        print("[CodeGuard] Argumentos de ejecución no reconocidos.", file=sys.stderr)
        return 2

    port = os.environ.get("CODEGUARD_PORT", "8000").strip() or "8000"
    print(f"[CodeGuard] Servidor local en http://127.0.0.1:{port}/", flush=True)

    from config.wsgi import application
    from waitress import serve

    serve(
        application,
        host="127.0.0.1",
        port=int(port),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
