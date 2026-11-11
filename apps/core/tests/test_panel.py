"""Pruebas del módulo core (panel y navegación)."""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client, override_settings
from django.urls import reverse


class PanelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_panel_redirige_sin_login(self):
        """El acceso anónimo al panel debe redirigir al inicio de sesión (autenticación activa)."""
        with override_settings(AUTH_DISABLED=False):
            self.client = Client()
            respuesta = self.client.get(reverse("core:panel"))
            self.assertEqual(respuesta.status_code, 302)
            self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))

    def test_panel_accesible_con_login(self):
        """El acceso autenticado al panel debe devolver 200 (autenticación activa)."""
        with override_settings(AUTH_DISABLED=False):
            self.client.force_login(self.usuario)
            respuesta = self.client.get(reverse("core:panel"))
            self.assertEqual(respuesta.status_code, 200)
            self.assertContains(respuesta, "Panel principal")

    def test_panel_abre_directamente_sin_autenticacion(self):
        """El panel se abre directamente sin credenciales cuando la autenticación está desactivada."""
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("core:panel"))
            self.assertEqual(respuesta.status_code, 200)
            self.assertContains(respuesta, "Panel principal")

    def test_panel_expone_los_doce_temas_y_el_panel_de_ajustes(self):
        """El catálogo completo de temas y el diálogo de ajustes están disponibles."""
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("core:panel"))
            self.assertEqual(respuesta.status_code, 200)
            for tema in (
                "light", "dark", "high-contrast", "retro-pixel", "cyberpunk",
                "fantasy", "sci-fi", "warrior", "mage", "rogue", "paladin",
                "dark-mage",
            ):
                self.assertContains(respuesta, f'data-theme="{tema}"')
            self.assertContains(respuesta, 'id="ajustesPanel"')
            self.assertContains(respuesta, 'aria-modal="true"')
