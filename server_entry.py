"""Punto de entrada del servidor Django empaquetado para CodeGuard Pro.

Electron inicia este binario (generado con PyInstaller) para servir Django localmente o, con
``--sync-knowledge``, para ejecutar una única comprobación de conocimiento y terminar.
El modo servidor sirve la aplicación mediante Waitress + WhiteNoise.
El modo de sincronización no ejecuta migraciones ni inicia Waitress.
En el modo servidor, este proceso inicializa de forma idempotente la base de datos
y el roadmap ASCENSO en el directorio de datos del usuario antes de escuchar
exclusivamente en 127.0.0.1.
"""

from __future__ import annotations

import json
import os
import sys
import time
import traceback


def _die(message: str, code: int = 1) -> int:
    """Imprime un error y sale con el código dado."""
    print(f"[CodeGuard ERROR] {message}", file=sys.stderr, flush=True)
    traceback.print_exc(file=sys.stderr)
    return code


def _initialize_database() -> dict:
    """Prepara el perfil local sin borrar ni reiniciar el progreso existente.

    Solo aplica migraciones pendientes y solo reconstruye el roadmap cuando el
    manifiesto, los recuentos o la huella del contenido no coinciden. Nunca se
    utiliza --recrear, que eliminaría el roadmap y el progreso asociado.
    """
    from apps.roadmaps.bootstrap import preparar_perfil_local

    return preparar_perfil_local()


def _emit_perf(phase: str, started: float, perf: dict, **extra) -> float:
    now = time.perf_counter()
    ms = round((now - started) * 1000, 2)
    perf[phase] = ms
    payload = {"phase": phase, "ms": ms, **extra}
    print(f"[CodeGuard PERF] {json.dumps(payload, ensure_ascii=False)}", flush=True)
    return now


def _write_perf_report(perf: dict) -> None:
    data_dir = os.environ.get("CODEGUARD_DATA_DIR", "").strip()
    if not data_dir:
        return
    try:
        path = os.path.join(data_dir, "startup-perf.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(perf, fh, ensure_ascii=False, indent=2)
    except Exception:
        pass


def main() -> int:
    t0 = time.perf_counter()
    perf = {"pid": os.getpid(), "argv": sys.argv[1:]}
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")

    print("[CodeGuard] Iniciando servidor Django empaquetado...", flush=True)

    try:
        t = time.perf_counter()
        import django  # noqa: F401
        _emit_perf("import_django_ms", t, perf)
        print("[CodeGuard] Django importado correctamente.", flush=True)
    except Exception as exc:
        perf["error"] = str(exc)
        _write_perf_report(perf)
        return _die(f"No se pudo importar Django: {exc}", 2)

    try:
        t = time.perf_counter()
        django.setup()
        _emit_perf("django_setup_ms", t, perf)
        print("[CodeGuard] Django configurado correctamente.", flush=True)
    except Exception as exc:
        perf["error"] = str(exc)
        _write_perf_report(perf)
        return _die(f"No se pudo configurar Django: {exc}", 3)

    # Restauración solicitada desde Electron con la aplicación detenida. Este
    # modo no inicia Waitress ni aplica migraciones: valida el ZIP, sustituye
    # base/media con rollback y termina. Electron reinicia la aplicación y el
    # arranque normal aplicará las migraciones pendientes.
    if len(sys.argv) == 3 and sys.argv[1] == "--restore-backup":
        from django.conf import settings

        from apps.core.restore import restore_backup

        try:
            result = restore_backup(
                sys.argv[2], data_dir=settings.DATA_DIR, confirm=True
            )
        except Exception as exc:
            print(f"[CodeGuard Restore] {exc}", file=sys.stderr, flush=True)
            traceback.print_exc(file=sys.stderr)
            return 8
        print(
            "[CodeGuard Restore] Perfil restaurado correctamente "
            f"({result['applied_migrations']} migraciones aplicadas, "
            f"{result['pending_migrations']} pendientes).",
            flush=True,
        )
        return 0

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

    try:
        print("[CodeGuard] Inicializando base de datos y roadmap local...", flush=True)
        t = time.perf_counter()
        resultado = _initialize_database()
        _emit_perf(
            "initialize_profile_ms",
            t,
            perf,
            roadmap_cargado=bool(resultado.get("roadmap_cargado")),
        )
        print(
            "[CodeGuard] Datos locales preparados correctamente "
            f"(roadmap {'reconstruido' if resultado.get('roadmap_cargado') else 'verificado'}, "
            f"{resultado.get('milisegundos', 0)} ms).",
            flush=True,
        )
    except Exception as exc:
        perf["error"] = str(exc)
        _write_perf_report(perf)
        return _die(f"No se pudo inicializar el perfil local: {exc}", 7)

    port = os.environ.get("CODEGUARD_PORT", "8000").strip() or "8000"
    print(f"[CodeGuard] Puerto: {port}", flush=True)

    try:
        t = time.perf_counter()
        from config.wsgi import application
        _emit_perf("import_wsgi_ms", t, perf)
        print("[CodeGuard] Aplicación WSGI cargada correctamente.", flush=True)
    except Exception as exc:
        perf["error"] = str(exc)
        _write_perf_report(perf)
        return _die(f"No se pudo importar config.wsgi: {exc}", 5)

    try:
        t = time.perf_counter()
        from waitress import serve
        _emit_perf("import_waitress_ms", t, perf)
        print("[CodeGuard] Waitress importado correctamente.", flush=True)
    except Exception as exc:
        perf["error"] = str(exc)
        _write_perf_report(perf)
        return _die(f"No se pudo importar waitress: {exc}", 6)

    perf["ready_to_serve_ms"] = round((time.perf_counter() - t0) * 1000, 2)
    print(
        f"[CodeGuard PERF] {json.dumps({'phase': 'ready_to_serve', 'ms': perf['ready_to_serve_ms']}, ensure_ascii=False)}",
        flush=True,
    )
    _write_perf_report(perf)

    try:
        threads = int(os.environ.get("CODEGUARD_WAITRESS_THREADS", "8"))
        threads = max(4, min(threads, 32))
        perf["waitress_threads"] = threads
        _write_perf_report(perf)
        print(f"[CodeGuard] Sirviendo en http://127.0.0.1:{port}/ (threads={threads}) ...", flush=True)
        serve(
            application,
            host="127.0.0.1",
            port=int(port),
            threads=threads,
            url_scheme="http",
            ident="CodeGuardPro/1.0.0",
        )
    except Exception as exc:
        print(f"[CodeGuard] Error iniciando el servidor Waitress: {exc}", file=sys.stderr, flush=True)
        traceback.print_exc(file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())