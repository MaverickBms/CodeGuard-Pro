"""Pruebas del formato de copias de seguridad de CodeGuard Pro."""
import json
import sqlite3
import tempfile
import unittest
import zipfile
from pathlib import Path

from apps.core.backup import BackupError, create_backup, inspect_backup


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "profile"
        self.root.mkdir()
        self.media = self.root / "media" / "documents"
        self.media.mkdir(parents=True)
        with sqlite3.connect(self.root / "db.sqlite3") as connection:
            connection.execute("CREATE TABLE sample (id INTEGER PRIMARY KEY, value TEXT)")
            connection.execute("INSERT INTO sample(value) VALUES ('progreso')")
        (self.media / "evidencia.txt").write_text("evidencia local", encoding="utf-8")
        (self.root / ".secret_key").write_text("NO-DEBE-INCLUIRSE", encoding="utf-8")
        (self.root / "logs").mkdir()
        (self.root / "logs" / "codeguard.log").write_text("log privado", encoding="utf-8")

    def tearDown(self):
        self.temporary.cleanup()

    def test_create_and_verify_backup_includes_database_and_media_only(self):
        destination = Path(self.temporary.name) / "respaldo.zip"
        manifest = create_backup(destination, data_dir=self.root)
        self.assertEqual(manifest["format"], "codeguard-backup")
        self.assertEqual(inspect_backup(destination)["format_version"], 1)
        with zipfile.ZipFile(destination) as archive:
            self.assertIn("database.sqlite3", archive.namelist())
            self.assertIn("media/documents/evidencia.txt", archive.namelist())
            self.assertNotIn(".secret_key", archive.namelist())
            self.assertNotIn("logs/codeguard.log", archive.namelist())

    def test_refuses_destination_inside_profile(self):
        with self.assertRaises(BackupError):
            create_backup(self.root / "backup.zip", data_dir=self.root)

    def test_rejects_path_traversal(self):
        malicious = Path(self.temporary.name) / "malicious.zip"
        manifest = {
            "format": "codeguard-backup",
            "format_version": 1,
            "files": [{"path": "../outside.txt", "size": 1, "sha256": "0" * 64}],
        }
        with zipfile.ZipFile(malicious, "w") as archive:
            archive.writestr("manifest.json", json.dumps(manifest))
            archive.writestr("database.sqlite3", "not a database")
            archive.writestr("../outside.txt", "x")
        with self.assertRaises(BackupError):
            inspect_backup(malicious)

    def test_rejects_corrupt_archive(self):
        destination = Path(self.temporary.name) / "respaldo.zip"
        create_backup(destination, data_dir=self.root)
        damaged = Path(self.temporary.name) / "damaged.zip"
        damaged.write_bytes(destination.read_bytes()[:-12])
        with self.assertRaises(BackupError):
            inspect_backup(damaged)


if __name__ == "__main__":
    unittest.main()
