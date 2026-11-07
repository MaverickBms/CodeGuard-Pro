"""Pruebas de auditoría (Fase 2).

Verifica que los eventos de seguridad relevantes se registran en `AuditLog`
sin almacenar nunca contraseñas ni frases de rescate en texto plano.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.audit.models import AuditLog
from apps.accounts.models import FraseRescate
from apps.accounts.services import generar_frase_rescate
from django.contrib.auth.hashers import make_password


class AuditoriaTests(TestCase):
    """Eventos de auditoría generados por los flujos de identidad y acceso."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def _contar_eventos(self, evento):
        return AuditLog.objects.filter(usuario=self.usuario, evento=evento).count()

    def test_login_exitoso_registra_evento(self):
        self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertGreater(self._contar_eventos("login_exitoso"), 0)
        # Nunca se almacena la contraseña.
        entrada = AuditLog.objects.filter(
            usuario=self.usuario, evento="login_exitoso"
        ).first()
        self.assertNotIn("ClaveSegura123!", entrada.descripcion)

    def test_login_fallido_registra_evento(self):
        self.client.post(
            reverse("accounts:login"), {"username": "tester", "password": "incorrecta"}
        )
        self.assertGreater(AuditLog.objects.filter(evento="login_fallido").count(), 0)

    def test_logout_manual_registra_evento(self):
        self.client.force_login(self.usuario)
        self.client.post(reverse("accounts:logout"))
        self.assertGreater(self._contar_eventos("logout"), 0)

    def test_logout_inactividad_registra_evento(self):
        self.client.force_login(self.usuario)
        sesion = self.client.session
        sesion["ultima_actividad"] = 0
        sesion.save()
        self.client.get(reverse("core:panel"))
        self.assertGreater(self._contar_eventos("logout_inactividad"), 0)

    def test_setup_inicial_registra_evento(self):
        get_user_model().objects.all().delete()
        self.client.post(
            reverse("accounts:setup"),
            {
                "username": "nuevo",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
                "aceptar_terminos": True,
            },
        )
        usuario = get_user_model().objects.get(username="nuevo")
        self.assertGreater(
            AuditLog.objects.filter(usuario=usuario, evento="setup_inicial").count(), 0
        )

    def test_cambio_contraseña_registra_evento(self):
        self.client.force_login(self.usuario)
        self.client.post(
            reverse("accounts:cambiar_contraseña"),
            {
                "old_password": "ClaveSegura123!",
                "new_password1": "NuevaClave12345",
                "new_password2": "NuevaClave12345",
            },
        )
        self.assertGreater(self._contar_eventos("cambio_contraseña"), 0)

    def test_uso_frase_rescate_registra_evento(self):
        frase = generar_frase_rescate()
        FraseRescate.objects.create(
            usuario=self.usuario, hash_argon2=make_password(frase)
        )
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": frase})
        self.client.post(
            reverse("accounts:resetear_contrasena"),
            {
                "frase_rescate": frase,
                "password1": "NuevaClave12345",
                "password2": "NuevaClave12345",
            },
        )
        self.assertGreater(self._contar_eventos("uso_frase_rescate"), 0)

    def test_nunca_se_almacenan_credenciales_en_texto_plano(self):
        """Ninguna entrada de auditoría contiene contraseñas ni frases."""
        self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.client.post(
            reverse("accounts:cambiar_contraseña"),
            {
                "old_password": "ClaveSegura123!",
                "new_password1": "NuevaClave12345",
                "new_password2": "NuevaClave12345",
            },
        )
        frase = generar_frase_rescate()
        FraseRescate.objects.create(
            usuario=self.usuario, hash_argon2=make_password(frase)
        )
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": frase})

        for entrada in AuditLog.objects.all():
            self.assertNotIn("ClaveSegura123!", entrada.descripcion)
            self.assertNotIn("NuevaClave12345", entrada.descripcion)
            self.assertNotIn(frase, entrada.descripcion)
