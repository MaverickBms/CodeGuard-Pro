"""Verifica la integridad del perfil local sin modificarlo."""

from __future__ import annotations

import json

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.bootstrap import cargar_manifiesto, verificar_instalacion
from apps.roadmaps.models import Roadmap


class Command(BaseCommand):
    help = (
        "Comprueba que el roadmap instalado coincide con el manifiesto distribuido. "
        "No aplica migraciones, no reconstruye contenido y no modifica el progreso."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--ruta",
            default=None,
            help="Manifiesto alternativo (por defecto apps/roadmaps/data/ascenso_3_1.json).",
        )
        parser.add_argument(
            "--json",
            action="store_true",
            dest="salida_json",
            help="Emite el resultado como JSON legible por máquina.",
        )

    def handle(self, *args, **options):
        try:
            manifiesto = cargar_manifiesto(options.get("ruta"))
        except ValueError as exc:
            raise CommandError(f"Manifiesto no válido: {exc}") from exc

        roadmap = Roadmap.objects.filter(
            nombre=manifiesto.nombre, edicion=manifiesto.edicion
        ).first()
        verificacion = verificar_instalacion(roadmap, manifiesto)

        datos = {
            "ok": verificacion.ok,
            "motivo": verificacion.motivo,
            "roadmap": {
                "nombre": manifiesto.nombre,
                "edicion": manifiesto.edicion,
                "sha256_manifiesto": manifiesto.sha256,
                "huella_contenido": manifiesto.huella_contenido,
                "etapas": manifiesto.total_etapas,
                "modulos": manifiesto.total_modulos,
                "lecciones": manifiesto.total_lecciones,
                "prerrequisitos": manifiesto.total_prerrequisitos,
            },
            "instalado": {
                "huella_contenido": verificacion.huella_base_datos,
                "registros_sobrantes": verificacion.registros_sobrantes,
                "claves_faltantes": verificacion.claves_faltantes,
            },
        }

        if options["salida_json"]:
            self.stdout.write(json.dumps(datos, ensure_ascii=False, indent=2))
        else:
            estado = "OK" if verificacion.ok else "ERROR"
            self.stdout.write(f"[{estado}] {verificacion.motivo}")
            self.stdout.write(
                f"Manifiesto: {manifiesto.nombre} ({manifiesto.edicion}) "
                f"{manifiesto.total_etapas} etapas · {manifiesto.total_modulos} módulos · "
                f"{manifiesto.total_lecciones} lecciones · "
                f"{manifiesto.total_prerrequisitos} prerrequisitos"
            )
            if verificacion.registros_sobrantes:
                self.stdout.write(
                    f"Registros sobrantes conservados: {verificacion.registros_sobrantes}"
                )
            for clave in verificacion.claves_faltantes:
                self.stdout.write(self.style.WARNING(f"Falta: {clave}"))

        if not verificacion.ok:
            raise CommandError(
                "El perfil local no coincide con el manifiesto. "
                "Ejecuta el arranque normal o `python manage.py cargar_ascenso`."
            )
