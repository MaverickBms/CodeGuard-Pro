"""Pruebas de los comandos de creación y verificación de backups."""
import sqlite3
import tempfile
from pathlib import Path

from django.core.management import call_command, CommandError
from django.test import SimpleTestCase, override_settings


class BackupCommandTests(SimpleTestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "profile"
        self.root.mkdir()
        with sqlite3.connect(self.root / "db.sqlite3") as connection:
            connection.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY)")
        (self.root / "media").mkdir()

    def tearDown(self):
        self.temporary.cleanup()

    @override_settings()
    def test_create_then_verify_backup_commands(self):
        destination = Path(self.temporary.name) / "cli-backup.zip"
        with override_settings(DATA_DIR=self.root):
            call_command("crear_backup", output=str(destination))
            call_command("verificar_backup", archive=str(destination))
        self.assertTrue(destination.is_file())

    def test_create_command_requires_output(self):
        with self.assertRaises(CommandError):
            call_command("crear_backup")
