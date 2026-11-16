"""Comando para cargar quizzes/exámenes desde JSON trazable (Fase 4)."""

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.services_carga_evaluaciones import cargar_quizzes


class Command(BaseCommand):
    help = "Carga o actualiza quizzes/exámenes desde un archivo JSON trazable."

    def add_arguments(self, parser):
        parser.add_argument(
            "--ruta",
            dest="ruta",
            default=None,
            help="Ruta al JSON de quizzes (por defecto apps/roadmaps/data/quizzes.json).",
        )
        parser.add_argument(
            "--reemplazar",
            action="store_true",
            help="Reemplaza las preguntas existentes de cada quiz versionado.",
        )

    def handle(self, *args, **options):
        try:
            resumen = cargar_quizzes(options.get("ruta"), reemplazar=options["reemplazar"])
        except FileNotFoundError as exc:
            raise CommandError(f"No se encontró el archivo de datos: {exc}") from exc
        except Exception as exc:
            raise CommandError(f"Error al cargar quizzes: {exc}") from exc

        self.stdout.write(
            self.style.SUCCESS(
                f"Quizzes cargados: {resumen['quizzes']} · preguntas: {resumen['preguntas']}."
            )
        )
        for adv in resumen.get("advertencias", []):
            self.stdout.write(self.style.WARNING(f"Advertencia: {adv}"))
