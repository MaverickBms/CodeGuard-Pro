"""Comando para cargar el roadmap oficial ASCENSO 3.1."""

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.models import Etapa, Leccion, Modulo, Prerrequisito, Roadmap
from apps.roadmaps.services import cargar_ascenso


class Command(BaseCommand):
    help = "Carga o actualiza las 33 etapas del roadmap ASCENSO 3.1 desde el JSON oficial."

    def add_arguments(self, parser):
        parser.add_argument(
            "--ruta",
            dest="ruta",
            default=None,
            help="Ruta alternativa al JSON de ASCENSO (por defecto apps/roadmaps/data/ascenso_3_1.json).",
        )
        parser.add_argument(
            "--recrear",
            action="store_true",
            help="Elimina el roadmap existente y su progreso antes de volver a cargarlo.",
        )

    def handle(self, *args, **options):
        try:
            roadmap = cargar_ascenso(options.get("ruta"), recrear=options["recrear"])
        except FileNotFoundError as exc:
            raise CommandError(f"No se encontró el archivo de datos: {exc}") from exc
        except ValueError as exc:
            raise CommandError(f"El archivo de datos no es válido: {exc}") from exc

        total_modulos = Modulo.objects.filter(etapa__roadmap=roadmap).count()
        total_lecciones = Leccion.objects.filter(modulo__etapa__roadmap=roadmap).count()
        total_etapas = Etapa.objects.filter(roadmap=roadmap).count()
        total_prerrequisitos = Prerrequisito.objects.filter(
            etapa__roadmap=roadmap
        ).count()

        self.stdout.write(
            self.style.SUCCESS(
                "Roadmap cargado correctamente: "
                f"{roadmap} · {total_etapas} etapas · {total_modulos} módulos · "
                f"{total_lecciones} lecciones · {total_prerrequisitos} prerrequisitos."
            )
        )
        self.stdout.write(
            "Recordatorio: todas las etapas quedan con desarrollada_en_mvp=False "
            "hasta que se resuelva la decisión P-002."
        )
