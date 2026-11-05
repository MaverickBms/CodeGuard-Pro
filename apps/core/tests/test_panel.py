"""Pruebas del módulo core (panel y navegación)."""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class PanelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.usuario = self.User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_panel_requiere_autenticacion(self):
        """Acceso al panel sin login debe redirigir a login."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertRedirects(respuesta, reverse("accounts:login") + "?next=/")

    def test_panel_accesible_con_login(self):
        """Acceso al panel con login debe devolver 200."""
        self.client.login(username="testuser", password="testpass123")
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Panel principal")
