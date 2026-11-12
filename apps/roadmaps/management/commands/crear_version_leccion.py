"""Crea un snapshot editorial borrador para una lección."""
from django.core.management.base import BaseCommand, CommandError
from apps.roadmaps.knowledge import crear_version_contenido_leccion
from apps.roadmaps.models import FuenteConocimiento, Leccion


class Command(BaseCommand):
    help = "Genera un snapshot versionado de una lección; no lo publica."

    def add_arguments(self, parser):
        parser.add_argument("--leccion", type=int, required=True, help="ID local de la lección")
        parser.add_argument("--fuente-id", type=int, action="append", default=[], help="ID de una fuente activa; puede repetirse")
        parser.add_argument("--resumen", default="", help="Resumen editorial de los cambios")

    def handle(self, *args, **options):
        try:
            leccion = Leccion.objects.get(pk=options["leccion"])
        except Leccion.DoesNotExist as exc:
            raise CommandError("No existe la lección indicada.") from exc

        fuentes = []
        for fuente_id in options["fuente_id"]:
            try:
                fuente = FuenteConocimiento.objects.get(pk=fuente_id)
            except FuenteConocimiento.DoesNotExist as exc:
                raise CommandError(f"No existe la fuente con ID {fuente_id}.") from exc
            fuentes.append((fuente, "principal", "", "Fuente asociada desde el comando editorial."))

        try:
            version = crear_version_contenido_leccion(
                leccion, resumen_cambios=options["resumen"], fuentes=fuentes
            )
        except Exception as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.SUCCESS(
            f"Versión borrador creada: ID={version.pk}, UUID={version.clave}, "
            f"número={version.numero_version}, SHA-256={version.sha256}"
        ))
        if not fuentes:
            self.stdout.write(self.style.WARNING(
                "No se asociaron fuentes; esta versión no podrá enviarse a revisión."
            ))
