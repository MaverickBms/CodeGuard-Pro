"""Comandos de administración para copias locales de CodeGuard Pro."""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.core.backup import BackupError, create_backup


class Command(BaseCommand):
    help = "Crea una copia ZIP verificada del perfil local (base de datos y media)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            required=True,
            help="Ruta absoluta o relativa del archivo ZIP de destino.",
        )

    def handle(self, *args, **options):
        destination = Path(options["output"]).expanduser()
        if not destination.is_absolute():
            destination = Path.cwd() / destination
        try:
            manifest = create_backup(
                destination,
                data_dir=settings.DATA_DIR,
                codeguard_version=getattr(settings, "CODEGUARD_APP_VERSION", "1.0.0"),
            )
        except (BackupError, OSError) as exc:
            raise CommandError(str(exc)) from exc

        total_bytes = sum(item["size"] for item in manifest["files"])
        self.stdout.write(self.style.SUCCESS("Copia creada y verificada correctamente."))
        self.stdout.write(f"Archivo: {destination}")
        self.stdout.write(f"Fecha UTC: {manifest['created_at']}")
        self.stdout.write(f"Archivos: {len(manifest['files'])}")
        self.stdout.write(f"Datos: {total_bytes} bytes")
