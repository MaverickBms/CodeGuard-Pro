"""Pruebas del módulo core (panel y navegación)."""

from django.test import TestCase, Client
from django.urls import reverse


class PanelTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_panel_accesible_sin_login(self):
        """Acceso al panel sin login debe devolver 200 (app monousuario sin auth)."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Panel principal")