#!/usr/bin/env python3
"""Banco de pruebas reproducible del arranque de CodeGuard Pro.

Uso:
    .venv/bin/python scripts/benchmark-startup.py
    .venv/bin/python scripts/benchmark-startup.py --json

Perfiles:
- perfil vacío, primer arranque (migraciones + siembra ASCENSO);
- mismo perfil, segundo arranque (verificación sin reconstrucción);
- perfil con datos históricos (auditoría y progreso) y tercer arranque.

El script falla con código 1 si el arranque normal supera el objetivo o si el
primer arranque excede el límite documentado. No toca el perfil real del
propietario: siempre usa directorios temporales.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
OBJETIVO_NORMAL_MS = 10_000
LIMITE_PRIMER_ARRANQUE_MS = 30_000

CODIGO_HIJO = r'''
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
total_ms = (time.perf_counter() - inicio) * 1000
resultado.update({"import_ms": round(import_ms, 1), "setup_ms": round(setup_ms, 1), "total_ms": round(total_ms, 1)})
print("BENCHMARK_JSON=" + json.dumps(resultado, ensure_ascii=False))
'''

CODIGO_SEMBRAR_DATOS = r'''
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.desktop")
import django
django.setup()

from apps.audit.models import AuditLog

AuditLog.objects.bulk_create([
    AuditLog(evento="acceso_panel", descripcion=f"Evento histórico {i}") for i in range(20_000)
])
print("SEMBRADO_OK")
'''


def _ejecutar(codigo: str, data_dir: Path) -> tuple[dict | None, float]:
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
        timeout=180,
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Salida JSON.")
    parser.add_argument(
        "--conservar",
        action="store_true",
        help="No elimina el perfil temporal (útil para diagnósticos).",
    )
    args = parser.parse_args()

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
        }

        segundo, pared_segundo = _ejecutar(CODIGO_HIJO, temporal)
        mediciones["segundo_arranque"] = {
            "interno_ms": round(segundo["total_ms"], 1) if segundo else None,
            "pared_ms": round(pared_segundo, 1),
            "roadmap_reutilizado": segundo.get("roadmap_reutilizado") if segundo else None,
            "lecciones": segundo.get("lecciones") if segundo else None,
        }

        _sembrar(temporal)
        tercero, pared_tercero = _ejecutar(CODIGO_HIJO, temporal)
        mediciones["perfil_con_historial"] = {
            "interno_ms": round(tercero["total_ms"], 1) if tercero else None,
            "pared_ms": round(pared_tercero, 1),
            "roadmap_reutilizado": tercero.get("roadmap_reutilizado") if tercero else None,
        }

        if segundo is None or not segundo.get("roadmap_reutilizado"):
            fallos.append("El segundo arranque reconstruyó el roadmap.")
        if tercero is None or not tercero.get("roadmap_reutilizado"):
            fallos.append("El arranque con historial reconstruyó el roadmap.")
        if primero and pared_primero > LIMITE_PRIMER_ARRANQUE_MS:
            fallos.append(
                f"Primer arranque {pared_primero:.0f} ms > {LIMITE_PRIMER_ARRANQUE_MS} ms."
            )
        if pared_segundo > OBJETIVO_NORMAL_MS:
            fallos.append(
                f"Segundo arranque {pared_segundo:.0f} ms > {OBJETIVO_NORMAL_MS} ms."
            )
        if pared_tercero > OBJETIVO_NORMAL_MS:
            fallos.append(
                f"Arranque con historial {pared_tercero:.0f} ms > {OBJETIVO_NORMAL_MS} ms."
            )
    finally:
        if args.conservar:
            print(f"Perfil temporal conservado: {temporal}", file=sys.stderr)
        else:
            shutil.rmtree(temporal, ignore_errors=True)

    salida = {
        "objetivo_normal_ms": OBJETIVO_NORMAL_MS,
        "limite_primer_arranque_ms": LIMITE_PRIMER_ARRANQUE_MS,
        "mediciones": mediciones,
        "fallos": fallos,
    }
    if args.json:
        print(json.dumps(salida, ensure_ascii=False, indent=2))
    else:
        print("CodeGuard Pro — benchmark de arranque")
        print(f"Objetivo normal: {OBJETIVO_NORMAL_MS} ms · primer arranque: {LIMITE_PRIMER_ARRANQUE_MS} ms")
        for nombre, valores in mediciones.items():
            print(f"- {nombre}: {valores}")
        if fallos:
            print("\nFALLOS:")
            for fallo in fallos:
                print(f"  - {fallo}")
        else:
            print("\nTodos los objetivos de arranque se cumplen.")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
