"""Verifica la integridad de una copia local sin extraerla al perfil."""
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from apps.core.backup import BackupError, inspect_backup


class Command(BaseCommand):
    help = "Verifica estructura, hashes e integridad SQLite de un backup ZIP."

    def add_arguments(self, parser):
        parser.add_argument("archive", help="Ruta del archivo ZIP que se verificará.")

    def handle(self, *args, **options):
        archive = Path(options["archive"]).expanduser()
        try:
            manifest = inspect_backup(archive)
        except (BackupError, OSError) as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.SUCCESS("La copia superó todas las verificaciones."))
        self.stdout.write(f"Formato: {manifest['format']} v{manifest['format_version']}")
        self.stdout.write(f"Versión CodeGuard: {manifest.get('codeguard_version', 'desconocida')}")
        self.stdout.write(f"Fecha UTC: {manifest['created_at']}")
        self.stdout.write(f"Archivos: {len(manifest['files'])}")
