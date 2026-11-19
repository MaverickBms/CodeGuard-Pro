"""Pruebas de la pantalla local de copias de seguridad."""
import sqlite3
import tempfile
from pathlib import Path

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.audit.models import AuditLog


class BackupViewsTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="backup-ui", password="ClaveSegura123!"
        )
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.profile = self.base / "profile"
        self.profile.mkdir()
        (self.profile / "media").mkdir()
        (self.profile / "media" / "nota.txt").write_text("contenido", encoding="utf-8")
        with sqlite3.connect(self.profile / "db.sqlite3") as connection:
            connection.execute("CREATE TABLE muestra (id INTEGER PRIMARY KEY)")

    def tearDown(self):
        self.temporary.cleanup()

    def test_pantalla_muestra_carpeta_y_estado_vacio(self):
        with override_settings(AUTH_DISABLED=True, DATA_DIR=self.profile):
            respuesta = self.client.get(reverse("core:backups"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Copias de seguridad")
        self.assertContains(respuesta, "Todavía no hay copias")

    def test_crear_copia_desde_la_interfaz(self):
        with override_settings(AUTH_DISABLED=True, DATA_DIR=self.profile):
            respuesta = self.client.post(
                reverse("core:backups"), {"accion": "crear"}, follow=True
            )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Copia creada y verificada")
        archivos = list((self.base / "CodeGuard Backups").glob("*.zip"))
        self.assertEqual(len(archivos), 1)
        self.assertTrue(
            AuditLog.objects.filter(evento="backup_creado").exists()
        )

    def test_verificar_copia_existente(self):
        with override_settings(AUTH_DISABLED=True, DATA_DIR=self.profile):
            self.client.post(reverse("core:backups"), {"accion": "crear"})
            archivo = next((self.base / "CodeGuard Backups").glob("*.zip")).name
            respuesta = self.client.post(
                reverse("core:backups"),
                {"accion": "verificar", "archivo": archivo},
                follow=True,
            )
        self.assertContains(respuesta, "Copia verificada correctamente")

    def test_rechaza_ruta_fuera_de_la_carpeta(self):
        with override_settings(AUTH_DISABLED=True, DATA_DIR=self.profile):
            respuesta = self.client.post(
                reverse("core:backups"),
                {"accion": "verificar", "archivo": "../perfil.zip"},
                follow=True,
            )
        self.assertContains(respuesta, "no es válido")
