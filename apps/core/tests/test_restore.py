"""Pruebas de restauración transaccional de backups locales."""
import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.core.management import call_command
from django.test import SimpleTestCase, override_settings

from apps.core.backup import create_backup
from apps.core.restore import RestoreError, restore_backup


class RestoreBackupTests(SimpleTestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.source = self.base / "source"
        self.target = self.base / "target"
        self.source.mkdir()
        self.target.mkdir()
        self._crear_perfil(self.source, marca="origen")
        self._crear_perfil(self.target, marca="anterior")
        (self.target / ".secret_key").write_text("clave-local", encoding="utf-8")
        (self.target / "logs").mkdir()
        (self.target / "logs" / "server.log").write_text("log previo", encoding="utf-8")
        self.archive = self.base / "backup.zip"
        create_backup(self.archive, data_dir=self.source)

    def tearDown(self):
        self.temporary.cleanup()

    def _crear_perfil(self, root: Path, *, marca: str):
        with sqlite3.connect(root / "db.sqlite3") as connection:
            connection.execute(
                "CREATE TABLE django_migrations ("
                "id INTEGER PRIMARY KEY, app TEXT, name TEXT, applied DATETIME)"
            )
            connection.execute(
                "INSERT INTO django_migrations (app, name, applied) "
                "VALUES ('accounts', '0001_initial', '2026-01-01')"
            )
            connection.execute(f"CREATE TABLE datos_{marca} (valor TEXT)")
            connection.execute(f"INSERT INTO datos_{marca} VALUES ('{marca}')")
        media = root / "media"
        media.mkdir(exist_ok=True)
        (media / f"{marca}.txt").write_text(marca, encoding="utf-8")

    def _tablas(self, database: Path) -> set[str]:
        with sqlite3.connect(database) as connection:
            return {
                row[0]
                for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )
            }

    def test_restaura_base_y_media_conservando_clave_y_logs(self):
        result = restore_backup(self.archive, data_dir=self.target, confirm=True)

        tablas = self._tablas(self.target / "db.sqlite3")
        self.assertIn("datos_origen", tablas)
        self.assertNotIn("datos_anterior", tablas)
        self.assertEqual(
            (self.target / "media" / "origen.txt").read_text(encoding="utf-8"),
            "origen",
        )
        self.assertFalse((self.target / "media" / "anterior.txt").exists())
        self.assertEqual(
            (self.target / ".secret_key").read_text(encoding="utf-8"), "clave-local"
        )
        self.assertEqual(
            (self.target / "logs" / "server.log").read_text(encoding="utf-8"),
            "log previo",
        )

        rollback = Path(result["rollback_path"])
        self.assertTrue(rollback.is_dir())
        self.assertIn("datos_anterior", self._tablas(rollback / "db.sqlite3"))
        self.assertTrue((rollback / "media" / "anterior.txt").is_file())
        self.assertGreaterEqual(result["pending_migrations"], 1)

    def test_restauracion_exige_confirmacion(self):
        with self.assertRaisesMessage(RestoreError, "--confirm"):
            restore_backup(self.archive, data_dir=self.target)
        self.assertIn("datos_anterior", self._tablas(self.target / "db.sqlite3"))

    def test_rechaza_esquema_futuro(self):
        with sqlite3.connect(self.source / "db.sqlite3") as connection:
            connection.execute(
                "INSERT INTO django_migrations (app, name, applied) "
                "VALUES ('futuro', '9999_migracion_desconocida', '2026-01-01')"
            )
        archive = self.base / "futuro.zip"
        create_backup(archive, data_dir=self.source)

        with self.assertRaisesMessage(RestoreError, "versión más reciente"):
            restore_backup(archive, data_dir=self.target, confirm=True)
        self.assertIn("datos_anterior", self._tablas(self.target / "db.sqlite3"))
        self.assertTrue((self.target / "media" / "anterior.txt").is_file())

    def test_revierte_perfil_si_falla_la_verificacion_final(self):
        with patch(
            "apps.core.restore._check_sqlite",
            side_effect=RestoreError("fallo simulado"),
        ):
            with self.assertRaisesMessage(RestoreError, "fallo simulado"):
                restore_backup(self.archive, data_dir=self.target, confirm=True)

        self.assertIn("datos_anterior", self._tablas(self.target / "db.sqlite3"))
        self.assertNotIn("datos_origen", self._tablas(self.target / "db.sqlite3"))
        self.assertTrue((self.target / "media" / "anterior.txt").is_file())
        self.assertFalse((self.target / "media" / "origen.txt").exists())

    def test_restaura_en_perfil_vacio(self):
        vacio = self.base / "vacio"
        vacio.mkdir()
        result = restore_backup(self.archive, data_dir=vacio, confirm=True)

        self.assertIsNone(result["rollback_path"])
        self.assertIn("datos_origen", self._tablas(vacio / "db.sqlite3"))
        self.assertTrue((vacio / "media" / "origen.txt").is_file())

    def test_backup_sin_media_deja_carpeta_media_valida(self):
        (self.source / "media" / "origen.txt").unlink()
        archive = self.base / "sin-media.zip"
        create_backup(archive, data_dir=self.source)
        vacio = self.base / "vacio-sin-media"
        vacio.mkdir()
        restore_backup(archive, data_dir=vacio, confirm=True)
        self.assertTrue((vacio / "media").is_dir())

    def test_rechaza_backup_dentro_del_perfil(self):
        dentro = self.target / "backup.zip"
        dentro.write_bytes(self.archive.read_bytes())
        with self.assertRaisesMessage(RestoreError, "dentro del perfil"):
            restore_backup(dentro, data_dir=self.target, confirm=True)

    def test_comando_restaurar_backup(self):
        with override_settings(DATA_DIR=self.target):
            call_command("restaurar_backup", str(self.archive), confirm=True)
        self.assertIn("datos_origen", self._tablas(self.target / "db.sqlite3"))


    def test_restauraciones_rapidas_conservan_cada_copia_de_reversion(self):
        primera = restore_backup(self.archive, data_dir=self.target, confirm=True)
        rollback_primero = Path(primera["rollback_path"])
        self.assertTrue(rollback_primero.is_dir())

        segunda = restore_backup(self.archive, data_dir=self.target, confirm=True)
        rollback_segundo = Path(segunda["rollback_path"])

        self.assertNotEqual(rollback_primero, rollback_segundo)
        self.assertTrue(rollback_primero.is_dir())
        self.assertIn("datos_anterior", self._tablas(rollback_primero / "db.sqlite3"))
        self.assertTrue(rollback_segundo.is_dir())
        self.assertIn("datos_origen", self._tablas(rollback_segundo / "db.sqlite3"))
