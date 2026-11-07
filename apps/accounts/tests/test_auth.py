"""Pruebas del módulo de identidad y acceso (CodeGuard Pro)."""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import FraseRescate
from apps.accounts.services import generar_frase_rescate


class SetupInicialTests(TestCase):
    def test_setup_redirige_si_usuario_existe(self):
        """Si ya existe un usuario, la configuración inicial redirige al login."""
        get_user_model().objects.create_user(username="existente", password="ClaveSegura123!")
        respuesta = self.client.get(reverse("accounts:setup"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("accounts:login"))


class LoginTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_login_redirige_a_panel_si_autentica(self):
        respuesta = self.client.post(
            reverse("accounts:login"), {"username": "tester", "password": "ClaveSegura123!"}
        )
        self.assertRedirects(respuesta, reverse("core:panel"))

    def test_login_fallido_redirige_al_login_con_error(self):
        respuesta = self.client.post(
            reverse("accounts:login"), {"username": "tester", "password": "Incorrecta123"}
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Usuario o contraseña incorrectos")

    def test_login_redirige_panel_si_ya_autenticado(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("accounts:login"))
        self.assertRedirects(respuesta, reverse("core:panel"))


class LogoutTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_cerrar_sesion_redirige_y_cierra_sesion(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse("accounts:logout"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))
        respuesta_segunda = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta_segunda.status_code, 302)
        self.assertTrue(respuesta_segunda.url.startswith(reverse("accounts:login")))


class CambiarContrasenaTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_cambiar_contrasena_valida(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("accounts:cambiar_contraseña"),
            {
                "old_password": "ClaveSegura123!",
                "new_password1": "NuevaClave12345",
                "new_password2": "NuevaClave12345",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("NuevaClave12345"))


class RescateTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )
        self.frase = generar_frase_rescate()
        FraseRescate.objects.create(usuario=self.usuario, hash_argon2=make_password(self.frase))

    def test_rescate_valido_redirige_al_login(self):
        respuesta = self.client.post(reverse("accounts:rescate"), {"frase_rescate": self.frase})
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("accounts:rescate_exito"))

    def test_rescate_invalido_muestra_error(self):
        respuesta = self.client.post(reverse("accounts:rescate"), {"frase_rescate": "frase-invalida"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "incorrecta")

    def test_rescate_marca_frase_como_usada(self):
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": self.frase})
        self.assertTrue(FraseRescate.objects.get(usuario=self.usuario).usada)


class SesionInactividadTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )
        self.client.force_login(self.usuario)

    def test_sesion_activa_no_expira(self):
        """Con actividad reciente la sesión sigue activa."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)

    def test_sesion_expira_por_inactividad(self):
        """Tras superar el timeout de inactividad se cierra la sesión."""
        sesion = self.client.session
        sesion["ultima_actividad"] = int(timezone.now().timestamp()) - 2000
        sesion.save()

        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))
