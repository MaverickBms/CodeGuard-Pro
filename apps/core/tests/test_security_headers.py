"""Pruebas de cabeceras de seguridad y CSP de la aplicación local."""
from django.test import TestCase, override_settings
from django.urls import reverse


class SecurityHeadersTests(TestCase):
    @override_settings(AUTH_DISABLED=True)
    def test_panel_aplica_cabeceras_y_csp_estricta(self):
        respuesta = self.client.get(reverse("core:panel"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta["X-Frame-Options"], "DENY")
        self.assertEqual(respuesta["X-Content-Type-Options"], "nosniff")
        self.assertEqual(respuesta["Referrer-Policy"], "same-origin")
        self.assertContains(respuesta, '<meta name="referrer" content="same-origin">')
        self.assertIn("camera=()", respuesta["Permissions-Policy"])

        csp = respuesta["Content-Security-Policy"]
        for directiva in (
            "default-src 'self'",
            "script-src 'self'",
            "object-src 'none'",
            "frame-src 'self'",
            "frame-ancestors 'none'",
            "form-action 'self'",
            "base-uri 'self'",
        ):
            self.assertIn(directiva, csp)

    @override_settings(AUTH_DISABLED=True)
    def test_pagina_con_datos_no_se_cachea(self):
        respuesta = self.client.get(reverse("core:panel"))
        self.assertIn("no-store", respuesta["Cache-Control"])
        self.assertIn("private", respuesta["Cache-Control"])
