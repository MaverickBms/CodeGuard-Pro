"""Pruebas del módulo core (panel y navegación)."""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class PanelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_panel_redirige_sin_login(self):
        """El acceso anónimo al panel debe redirigir al inicio de sesión."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))

    def test_panel_accesible_con_login(self):
        """El acceso autenticado al panel debe devolver 200."""
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Panel principal")
