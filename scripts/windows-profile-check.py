"""Utilidad de aceptación Windows: siembra y verifica progreso local.

Se ejecuta contra el mismo CODEGUARD_DATA_DIR que la aplicación empaquetada.
No forma parte del runtime de usuario; solo lo usa la matriz de CI.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Al ejecutar el script desde scripts/, Python añade ese directorio a sys.path;
# el proyecto y sus apps viven un nivel arriba.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django  # noqa: E402

django.setup()

from django.contrib.auth import get_user_model  # noqa: E402

from apps.roadmaps.models import Leccion, Progreso  # noqa: E402
from apps.roadmaps.services import iniciar_leccion  # noqa: E402


def _usuario():
    Usuario = get_user_model()
    usuario = Usuario.objects.filter(username="aceptacion-windows").first()
    if usuario is None:
        usuario = Usuario.objects.create_user(
            username="aceptacion-windows",
            password="ClaveTemporalCI-123!",
        )
    return usuario


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    usuario = _usuario()
    if args.verify:
        total = Progreso.objects.filter(usuario=usuario).count()
        print(f"PROGRESS={total}")
        return 0 if total >= 1 else 1

    leccion = Leccion.objects.order_by("id").first()
    if leccion is None:
        print("No hay lecciones cargadas en el perfil.", file=sys.stderr)
        return 2
    iniciar_leccion(usuario, leccion)
    print("SEED_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
