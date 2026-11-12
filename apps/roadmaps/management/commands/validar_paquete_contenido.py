"""Valida un lote JSON académico sin escribir en la base de datos."""

from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.content_import import ImportContentError, validar_directorio_contenido


class Command(BaseCommand):
    help = "Valida documentos académicos JSON v1 sin modificar datos."

    def add_arguments(self, parser):
        parser.add_argument("--directorio", required=True)

    def handle(self, *args, **options):
        try:
            report = validar_directorio_contenido(options["directorio"])
        except ImportContentError as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(f"Documentos analizados: {report['documents']}")
        self.stdout.write(f"Documentos válidos: {report['valid']}")
        for warning in report["warnings"]:
            self.stdout.write(self.style.WARNING(f"ADVERTENCIA: {warning}"))
        for error in report["errors"]:
            self.stdout.write(self.style.ERROR(f"ERROR: {error}"))
        if report["errors"]:
            raise CommandError("El lote no es válido; no se importó ningún documento.")
        self.stdout.write(self.style.SUCCESS("Validación completada. No se escribió ningún dato."))
