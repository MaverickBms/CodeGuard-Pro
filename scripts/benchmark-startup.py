#!/usr/bin/env python3
"""Banco de pruebas reproducible del arranque de CodeGuard Pro.

Uso:
    .venv/bin/python scripts/benchmark-startup.py
    .venv/bin/python scripts/benchmark-startup.py --json
    .venv/bin/python scripts/benchmark-startup.py --packaged-server dist-server/CodeGuardServer/CodeGuardServer --json
    .venv/bin/python scripts/benchmark-startup.py --appimage dist/CodeGuard-Pro-1.0.0-x86_64.AppImage --json

No toca el perfil real del propietario: siempre usa directorios temporales.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
OBJETIVO_NORMAL_MS = 10_000
LIMITE_PRIMER_ARRANQUE_MS = 30_000
OBJETIVO_FRIO_EXISTENTE_MS = 15_000

CODIGO_HIJO = r"""
import json
import os
import sys
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")

inicio = time.perf_counter()
import django
import_ms = (time.perf_counter() - inicio) * 1000

inicio = time.perf_counter()
django.setup()
setup_ms = (time.perf_counter() - inicio) * 1000

from apps.roadmaps.bootstrap import preparar_perfil_local
inicio = time.perf_counter()
resultado = preparar_perfil_local()
preparar_ms = (time.perf_counter() - inicio) * 1000

resultado["import_django_ms"] = round(import_ms, 2)
resultado["django_setup_ms"] = round(setup_ms, 2)
resultado["preparar_ms"] = round(preparar_ms, 2)
resultado["total_ms"] = round(import_ms + setup_ms + preparar_ms, 2)
print("BENCHMARK_JSON=" + json.dumps(resultado, ensure_ascii=False))
"""

CODIGO_SEMBRAR_DATOS = r"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")
import django
django.setup()
from apps.audit.models import AuditLog
AuditLog.objects.bulk_create([
    AuditLog(evento="acceso_panel", descripcion=f"Evento histórico {i}") for i in range(20_000)
])
print("SEMBRADO_OK")
"""


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _ejecutar(codigo: str, data_dir: Path, timeout: int = 180) -> tuple[dict | None, float]:
    entorno = {
        **os.environ,
        "CODEGUARD_DATA_DIR": str(data_dir),
        "DJANGO_SETTINGS_MODULE": "config.settings.desktop",
        "PYTHONPATH": str(RAIZ),
    }
    inicio = time.perf_counter()
    proceso = subprocess.run(
        [sys.executable, "-c", codigo],
        cwd=RAIZ,
        env=entorno,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    transcurrido_ms = (time.perf_counter() - inicio) * 1000
    if proceso.returncode != 0:
        raise RuntimeError(
            "El proceso de medición falló.\n"
            f"STDOUT:\n{proceso.stdout[-4000:]}\nSTDERR:\n{proceso.stderr[-4000:]}"
        )
    resultado = None
    for linea in proceso.stdout.splitlines():
        if linea.startswith("BENCHMARK_JSON="):
            resultado = json.loads(linea.split("=", 1)[1])
    return resultado, transcurrido_ms


def _sembrar(data_dir: Path) -> None:
    entorno = {
        **os.environ,
        "CODEGUARD_DATA_DIR": str(data_dir),
        "DJANGO_SETTINGS_MODULE": "config.settings.desktop",
        "PYTHONPATH": str(RAIZ),
    }
    proceso = subprocess.run(
        [sys.executable, "-c", CODIGO_SEMBRAR_DATOS],
        cwd=RAIZ,
        env=entorno,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if proceso.returncode != 0:
        raise RuntimeError(proceso.stderr[-4000:])


def _poll_health(port: int, timeout_s: float) -> tuple[bool, float, dict | None]:
    deadline = time.monotonic() + timeout_s
    last = None
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/healthz/", timeout=2) as r:
                body = json.loads(r.read().decode("utf-8", "replace"))
                last = body
                if r.status == 200:
                    return True, time.monotonic(), body
        except Exception:
            pass
        time.sleep(0.2)
    return False, time.monotonic(), last


def _medir_packaged_server(server_path: Path, data_dir: Path, label: str, timeout_s: int = 300) -> dict:
    port = _free_port()
    env = {
        **os.environ,
        "CODEGUARD_DATA_DIR": str(data_dir),
        "CODEGUARD_PORT": str(port),
        "DJANGO_SETTINGS_MODULE": "config.settings.desktop",
        "PYTHONUNBUFFERED": "1",
    }
    log_path = data_dir / f"bench-{label}.log"
    t0 = time.monotonic()
    with open(log_path, "w", encoding="utf-8") as logf:
        server_abs = server_path.resolve()
        p = subprocess.Popen(
            [str(server_abs)],
            cwd=str(server_abs.parent),
            env=env,
            stdout=logf,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            ok, t_ready, health = _poll_health(port, timeout_s)
            t_health = (t_ready - t0) * 1000
            # measure first page
            page_ms = None
            page_status = None
            if ok:
                try:
                    t1 = time.monotonic()
                    req = urllib.request.Request(f"http://127.0.0.1:{port}/", headers={"Host": "127.0.0.1"})
                    with urllib.request.urlopen(req, timeout=30) as r:
                        r.read()
                        page_status = r.status
                        page_ms = (time.monotonic() - t1) * 1000
                except Exception as e:
                    page_status = str(e)
        finally:
            p.terminate()
            try:
                p.wait(timeout=10)
            except Exception:
                p.kill()
                p.wait(timeout=5)
    perf = {}
    perf_file = data_dir / "startup-perf.json"
    if perf_file.exists():
        try:
            perf = json.loads(perf_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "label": label,
        "healthz_ok": ok,
        "healthz_ms": round(t_health, 1),
        "healthz_body": health,
        "page_ms": round(page_ms, 1) if page_ms is not None else None,
        "page_status": page_status,
        "server_perf": perf,
        "log": str(log_path),
    }


def benchmark_packaged_server(server_path: Path, conservar: bool = False) -> dict:
    temporal = Path(tempfile.mkdtemp(prefix="codeguard-bench-srv-"))
    mediciones = {}
    fallos = []
    try:
        mediciones["primer_arranque_fresco"] = _medir_packaged_server(server_path, temporal, "fresh")
        mediciones["segundo_arranque_mismo_perfil"] = _medir_packaged_server(server_path, temporal, "warm")
        _sembrar(temporal)
        mediciones["perfil_con_historial"] = _medir_packaged_server(server_path, temporal, "history")
        for k, v in mediciones.items():
            if not v.get("healthz_ok"):
                fallos.append(f"{k}: /healthz/ no respondió 200 a tiempo")
        warm = mediciones["segundo_arranque_mismo_perfil"]["healthz_ms"]
        if warm > OBJETIVO_NORMAL_MS:
            fallos.append(f"Segundo arranque empaquetado {warm:.0f} ms > {OBJETIVO_NORMAL_MS} ms")
        fresh = mediciones["primer_arranque_fresco"]["healthz_ms"]
        if fresh > LIMITE_PRIMER_ARRANQUE_MS:
            fallos.append(f"Primer arranque empaquetado {fresh:.0f} ms > {LIMITE_PRIMER_ARRANQUE_MS} ms")
    finally:
        if not conservar:
            shutil.rmtree(temporal, ignore_errors=True)
        else:
            print(f"Perfil temporal conservado: {temporal}", file=sys.stderr)
    return {
        "modo": "packaged-server",
        "server": str(server_path),
        "objetivo_normal_ms": OBJETIVO_NORMAL_MS,
        "limite_primer_arranque_ms": LIMITE_PRIMER_ARRANQUE_MS,
        "mediciones": mediciones,
        "fallos": fallos,
    }


def benchmark_django(conservar: bool = False) -> dict:
    temporal = Path(tempfile.mkdtemp(prefix="codeguard-bench-"))
    mediciones: dict[str, dict] = {}
    fallos: list[str] = []
    try:
        primero, pared_primero = _ejecutar(CODIGO_HIJO, temporal)
        mediciones["primer_arranque"] = {
            "interno_ms": round(primero["total_ms"], 1) if primero else None,
            "pared_ms": round(pared_primero, 1),
            "migraciones": primero.get("migraciones_pendientes") if primero else None,
            "roadmap_cargado": primero.get("roadmap_cargado") if primero else None,
            "fases_ms": (primero or {}).get("fases_ms"),
        }

        segundo, pared_segundo = _ejecutar(CODIGO_HIJO, temporal)
        mediciones["segundo_arranque"] = {
            "interno_ms": round(segundo["total_ms"], 1) if segundo else None,
            "pared_ms": round(pared_segundo, 1),
            "roadmap_reutilizado": segundo.get("roadmap_reutilizado") if segundo else None,
            "lecciones": segundo.get("lecciones") if segundo else None,
            "fases_ms": (segundo or {}).get("fases_ms"),
        }

        _sembrar(temporal)
        tercero, pared_tercero = _ejecutar(CODIGO_HIJO, temporal)
        mediciones["perfil_con_historial"] = {
            "interno_ms": round(tercero["total_ms"], 1) if tercero else None,
            "pared_ms": round(pared_tercero, 1),
            "roadmap_reutilizado": tercero.get("roadmap_reutilizado") if tercero else None,
            "fases_ms": (tercero or {}).get("fases_ms"),
        }

        if segundo is None or not segundo.get("roadmap_reutilizado"):
            fallos.append("El segundo arranque reconstruyó el roadmap.")
        if tercero is None or not tercero.get("roadmap_reutilizado"):
            fallos.append("El arranque con historial reconstruyó el roadmap.")
        if primero and pared_primero > LIMITE_PRIMER_ARRANQUE_MS:
            fallos.append(f"Primer arranque {pared_primero:.0f} ms > {LIMITE_PRIMER_ARRANQUE_MS} ms.")
        if pared_segundo > OBJETIVO_NORMAL_MS:
            fallos.append(f"Segundo arranque {pared_segundo:.0f} ms > {OBJETIVO_NORMAL_MS} ms.")
        if pared_tercero > OBJETIVO_NORMAL_MS:
            fallos.append(f"Arranque con historial {pared_tercero:.0f} ms > {OBJETIVO_NORMAL_MS} ms.")
    finally:
        if conservar:
            print(f"Perfil temporal conservado: {temporal}", file=sys.stderr)
        else:
            shutil.rmtree(temporal, ignore_errors=True)
    return {
        "modo": "django",
        "objetivo_normal_ms": OBJETIVO_NORMAL_MS,
        "limite_primer_arranque_ms": LIMITE_PRIMER_ARRANQUE_MS,
        "mediciones": mediciones,
        "fallos": fallos,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Salida JSON.")
    parser.add_argument("--conservar", action="store_true", help="No elimina el perfil temporal.")
    parser.add_argument("--packaged-server", help="Ruta al binario CodeGuardServer empaquetado.")
    parser.add_argument("--appimage", help="Ruta al AppImage (medición best-effort; requiere entorno gráfico).")
    args = parser.parse_args()

    if args.packaged_server:
        server = Path(args.packaged_server)
        if not server.exists():
            print(f"No existe: {server}", file=sys.stderr)
            return 2
        salida = benchmark_packaged_server(server, conservar=args.conservar)
    elif args.appimage:
        # Best-effort: launch AppImage with temp profile and wait for startup-perf-electron.json
        appimage = Path(args.appimage)
        if not appimage.exists():
            print(f"No existe: {appimage}", file=sys.stderr)
            return 2
        temporal = Path(tempfile.mkdtemp(prefix="codeguard-bench-appimg-"))
        mediciones = {}
        fallos = []
        try:
            for label in ["primer_arranque_fresco", "segundo_arranque_mismo_perfil"]:
                env = {**os.environ, "CODEGUARD_DATA_DIR": str(temporal), "APPIMAGE_EXTRACT_AND_RUN": "1"}
                log_path = temporal / f"appimage-{label}.log"
                perf_path = temporal / "startup-perf-electron.json"
                if perf_path.exists():
                    perf_path.unlink()
                t0 = time.monotonic()
                appimage_abs = appimage.resolve()
                with open(log_path, "w", encoding="utf-8") as logf:
                    p = subprocess.Popen([str(appimage_abs), "--no-sandbox", "--disable-gpu"], cwd=str(appimage_abs.parent), env=env, stdout=logf, stderr=subprocess.STDOUT)
                    ready = None
                    try:
                        for _ in range(300):
                            time.sleep(1)
                            if perf_path.exists():
                                try:
                                    perf = json.loads(perf_path.read_text(encoding="utf-8"))
                                    if perf.get("usable") or perf.get("marks_ms", {}).get("main_load_resolved"):
                                        ready = (time.monotonic() - t0) * 1000
                                        mediciones[label] = {"usable_ms": round(ready, 1), "electron_perf": perf, "log": str(log_path)}
                                        break
                                except Exception:
                                    pass
                            if p.poll() is not None:
                                break
                        if label not in mediciones:
                            mediciones[label] = {"usable_ms": None, "log": str(log_path), "error": "no usable mark"}
                            fallos.append(f"{label}: AppImage no marcó usable en tiempo límite")
                    finally:
                        p.terminate()
                        try:
                            p.wait(timeout=10)
                        except Exception:
                            p.kill()
                            p.wait(timeout=5)
                # keep profile for second run
        finally:
            if not args.conservar:
                shutil.rmtree(temporal, ignore_errors=True)
            else:
                print(f"Perfil temporal conservado: {temporal}", file=sys.stderr)
        salida = {"modo": "appimage", "appimage": str(appimage), "mediciones": mediciones, "fallos": fallos}
    else:
        salida = benchmark_django(conservar=args.conservar)

    if args.json:
        print(json.dumps(salida, ensure_ascii=False, indent=2))
    else:
        print("CodeGuard Pro — benchmark de arranque")
        for k, v in salida.get("mediciones", {}).items():
            print(f"- {k}: {v}")
        if salida.get("fallos"):
            print("\nFALLOS:")
            for f in salida["fallos"]:
                print(f"  - {f}")
        else:
            print("\nSin fallos reportados.")
    return 1 if salida.get("fallos") else 0


if __name__ == "__main__":
    raise SystemExit(main())
