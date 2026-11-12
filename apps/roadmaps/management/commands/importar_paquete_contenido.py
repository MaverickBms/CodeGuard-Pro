"""Importa documentos académicos como borradores editoriales, nunca como publicaciones."""

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from apps.roadmaps.content_import import (
    ImportContentError,
    importar_documentos_validados,
    validar_directorio_contenido,
)


class Command(BaseCommand):
    help = "Importa un lote validado como borradores. Nunca publica contenido."

    def add_arguments(self, parser):
        parser.add_argument("--directorio", required=True)
        parser.add_argument("--confirmar", action="store_true")
        parser.add_argument("--usuario", help="Username de un editor activo; obligatorio con --confirmar")

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
            raise CommandError("Lote rechazado; no se creó ninguna versión.")

        if not options["confirmar"]:
            self.stdout.write(self.style.SUCCESS(
                "Prevalidación correcta. No se escribió ningún dato. "
                "Repite con --confirmar --usuario EDITOR para crear borradores."
            ))
            return
        if not options["usuario"]:
            raise CommandError("--usuario es obligatorio cuando se utiliza --confirmar.")

        User = get_user_model()
        try:
            actor = User.objects.get(username=options["usuario"], is_active=True, is_staff=True)
        except User.DoesNotExist as exc:
            raise CommandError("El usuario debe existir y ser editor activo (is_staff).") from exc

        try:
            result = importar_documentos_validados(report, actor=actor)
        except (ValidationError, ImportContentError) as exc:
            mensaje = "; ".join(exc.messages) if isinstance(exc, ValidationError) else str(exc)
            raise CommandError(mensaje) from exc

        self.stdout.write(self.style.SUCCESS(
            f"Importación completada: {len(result['created'])} borradores nuevos; "
            f"{len(result['duplicates'])} duplicados idempotentes."
        ))
        for version in result["created"]:
            self.stdout.write(
                f"Borrador: lección={version.leccion_id}, versión={version.numero_version}, "
                f"UUID={version.clave}, SHA-256={version.sha256}"
            )
