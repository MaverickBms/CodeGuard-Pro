"""Restaura una copia local validada sobre el perfil de datos actual."""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from apps.core.backup import BackupError
from apps.core.restore import restore_backup


class Command(BaseCommand):
    help = (
        "Restaura base de datos y media desde un backup ZIP verificado. "
        "Cierra CodeGuard Pro antes de ejecutar este comando."
    )

    def add_arguments(self, parser):
        parser.add_argument("archive", help="Ruta del archivo ZIP de backup.")
        parser.add_argument(
            "--confirm",
            action="store_true",
            help="Confirma que se reemplazará el perfil actual.",
        )

    def handle(self, *args, **options):
        archive = Path(options["archive"]).expanduser()
        try:
            result = restore_backup(
                archive,
                data_dir=settings.DATA_DIR,
                confirm=bool(options["confirm"]),
            )
        except (BackupError, OSError) as exc:
            raise CommandError(str(exc)) from exc

        manifest = result["manifest"]
        self.stdout.write(self.style.SUCCESS("Perfil restaurado y verificado correctamente."))
        self.stdout.write(f"Fecha UTC del backup: {manifest['created_at']}")
        self.stdout.write(f"Archivos restaurados: {len(manifest['files'])}")
        self.stdout.write(f"Migraciones aplicadas: {result['applied_migrations']}")
        if result["pending_migrations"]:
            self.stdout.write(
                self.style.WARNING(
                    "Migraciones pendientes: "
                    f"{result['pending_migrations']}. Se aplicarán al arrancar CodeGuard Pro."
                )
            )
        if result["rollback_path"]:
            self.stdout.write(
                self.style.WARNING(
                    "Copia de reversión del perfil anterior: "
                    f"{result['rollback_path']}"
                )
            )
        self.stdout.write(
            "Conserva el archivo de backup original: la restauración no lo modifica."
        )
