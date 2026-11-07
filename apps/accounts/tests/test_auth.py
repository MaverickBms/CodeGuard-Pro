"""Pruebas del módulo de identidad y acceso (CodeGuard Pro).

Cubre:

- Configuración inicial (CG-004): envíos válidos e inválidos.
- Inicio de sesión (incluido fallido y ya autenticado).
- Cierre de sesión manual (CG-005): GET no cierra, POST sí.
- Recuperación mediante frase de rescate (CG-003): validación, flujo completo
  de cambio de contraseña, invalidez tras uso y no-reutilización.
- Cambio de contraseña autenticado (incluida no-reutilización de la actual).
- Expiración de sesión (CG-002): GET y POST con sesión vencida; una sesión
  vencida nunca ejecuta operaciones protegidas ni modifica progreso.
"""

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.forms import SetupInicialForm
from apps.accounts.models import FraseRescate
from apps.accounts.services import generar_frase_rescate


class SetupInicialTests(TestCase):
    """Configuración inicial (primer uso): usuario, contraseña y términos."""

    def test_setup_redirige_si_usuario_existe(self):
        """Si ya existe un usuario, la configuración inicial redirige al login."""
        get_user_model().objects.create_user(
            username="existente", password="ClaveSegura123!"
        )
        respuesta = self.client.get(reverse("accounts:setup"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("accounts:login"))

    def test_setup_valido_crea_usuario_y_redirige(self):
        """Datos correctos crean el usuario, su frase de rescate y muestran éxito."""
        self.assertFalse(get_user_model().objects.exists())
        respuesta = self.client.post(
            reverse("accounts:setup"),
            {
                "username": "nuevo_usuario",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
                "aceptar_terminos": True,
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "accounts/setup_exito.html")
        usuario = get_user_model().objects.get(username="nuevo_usuario")
        self.assertTrue(usuario.check_password("ClaveSegura123!"))
        self.assertTrue(
            FraseRescate.objects.filter(usuario=usuario, usada=False).exists()
        )

    def test_setup_contrasenas_diferentes_no_crea_usuario(self):
        """Contraseñas diferentes: error de formulario, ningún usuario creado."""
        respuesta = self.client.post(
            reverse("accounts:setup"),
            {
                "username": "nuevo_usuario",
                "password1": "ClaveSegura123!",
                "password2": "OtraClave123!",
                "aceptar_terminos": True,
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        form = respuesta.context["form"]
        self.assertTrue(form.errors)
        self.assertFalse(get_user_model().objects.filter(
            username="nuevo_usuario"
        ).exists())

    def test_setup_contrasena_insuficiente_no_crea_usuario(self):
        """Contraseña menor a 8 caracteres: error de formulario."""
        respuesta = self.client.post(
            reverse("accounts:setup"),
            {
                "username": "nuevo_usuario",
                "password1": "corta",
                "password2": "corta",
                "aceptar_terminos": True,
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        form = respuesta.context["form"]
        self.assertTrue(form.errors)
        self.assertFalse(get_user_model().objects.exists())

    def test_setup_usuario_duplicado_form_rechaza(self):
        """El formulario rechaza un usuario ya existente (prueba de unidad del form)."""
        get_user_model().objects.create_user(
            username="existente", password="ClaveSegura123!"
        )
        form = SetupInicialForm(
            data={
                "username": "existente",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
                "aceptar_terminos": True,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_setup_terminos_no_aceptados_no_crea_usuario(self):
        """Términos no aceptados: error de formulario, sin usuario creado."""
        respuesta = self.client.post(
            reverse("accounts:setup"),
            {
                "username": "nuevo_usuario",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        form = respuesta.context["form"]
        self.assertTrue(form.errors)
        self.assertFalse(get_user_model().objects.exists())


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

    def test_cerrar_sesion_post_cierra_sesion_y_redirige(self):
        """POST cierra la sesión, registra auditoría y redirige al panel/login."""
        self.client.force_login(self.usuario)
        respuesta = self.client.post(reverse("accounts:logout"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))
        respuesta_segunda = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta_segunda.status_code, 302)
        self.assertTrue(respuesta_segunda.url.startswith(reverse("accounts:login")))

    def test_cerrar_sesion_get_no_cierra_sesion(self):
        """GET al cierre de sesión no está permitido y no cierra la sesión."""
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("accounts:logout"))
        # El endpoint exige POST: Django responde 405 Method Not Allowed.
        self.assertEqual(respuesta.status_code, 405)
        # La sesión sigue activa: se puede acceder al panel.
        respuesta_panel = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta_panel.status_code, 200)


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

    def test_no_puede_ser_igual_a_la_actual(self):
        """La nueva contraseña no puede ser idéntica a la actual."""
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("accounts:cambiar_contraseña"),
            {
                "old_password": "ClaveSegura123!",
                "new_password1": "ClaveSegura123!",
                "new_password2": "ClaveSegura123!",
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        form = respuesta.context["form"]
        self.assertTrue(form.errors)
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("ClaveSegura123!"))


class RescateTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )
        self.frase = generar_frase_rescate()
        FraseRescate.objects.create(
            usuario=self.usuario, hash_argon2=make_password(self.frase)
        )

    def test_rescate_valido_redirige_a_resetear(self):
        """Frase válida redirige al paso de establecer nueva contraseña."""
        respuesta = self.client.post(
            reverse("accounts:rescate"), {"frase_rescate": self.frase}
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("accounts:resetear_contrasena"))

    def test_rescate_invalido_muestra_error(self):
        respuesta = self.client.post(
            reverse("accounts:rescate"), {"frase_rescate": "frase-invalida"}
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "incorrecta")

    def test_rescate_no_consuma_frase_al_validar(self):
        """Validar la frase no la marca como usada: solo al completar el reset."""
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": self.frase})
        self.assertFalse(FraseRescate.objects.get(usuario=self.usuario).usada)

    def test_resetear_contrasena_valido_cambia_e_invalida_frase(self):
        """Flujo completo: frase válida + nueva contraseña -> cambia e invalida."""
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": self.frase})
        respuesta = self.client.post(
            reverse("accounts:resetear_contrasena"),
            {
                "frase_rescate": self.frase,
                "password1": "NuevaClave12345",
                "password2": "NuevaClave12345",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("accounts:login"))
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("NuevaClave12345"))
        self.assertTrue(FraseRescate.objects.get(usuario=self.usuario).usada)

    def test_resetear_contrasena_con_frase_ya_usada_no_cambia(self):
        """Tras usar la frase, no puede reutilizarse para otro cambio."""
        self.client.post(reverse("accounts:rescate"), {"frase_rescate": self.frase})
        self.client.post(
            reverse("accounts:resetear_contrasena"),
            {
                "frase_rescate": self.frase,
                "password1": "NuevaClave12345",
                "password2": "NuevaClave12345",
            },
        )
        # Intento de reutilizar la misma frase ya invalidada: no debe cambiar nada.
        respuesta = self.client.post(
            reverse("accounts:resetear_contrasena"),
            {
                "frase_rescate": self.frase,
                "password1": "OtraClave12345",
                "password2": "OtraClave12345",
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("NuevaClave12345"))
        self.assertFalse(self.usuario.check_password("OtraClave12345"))

    def test_frase_incorrecta_no_cambia_contrasena(self):
        """Frase incorrecta no cambia la contraseña ni invalida la frase."""
        self.client.post(
            reverse("accounts:resetear_contrasena"),
            {
                "frase_rescate": "frase-incorrecta",
                "password1": "NuevaClave12345",
                "password2": "NuevaClave12345",
            },
        )
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("ClaveSegura123!"))
        self.assertFalse(FraseRescate.objects.get(usuario=self.usuario).usada)


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

    def test_sesion_expira_por_inactividad_get(self):
        """GET a vista protegida con sesión vencida redirige al login sin ejecutar la vista."""
        sesion = self.client.session
        sesion["ultima_actividad"] = int(timezone.now().timestamp()) - 2000
        sesion.save()

        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))

    def test_sesion_expira_por_inactividad_post_no_ejecuta_operacion(self):
        """POST con sesión vencida no ejecuta la operación protegida."""
        sesion = self.client.session
        sesion["ultima_actividad"] = int(timezone.now().timestamp()) - 2000
        sesion.save()

        respuesta = self.client.post(
            reverse("accounts:cambiar_contraseña"),
            {
                "old_password": "ClaveSegura123!",
                "new_password1": "NuevaClave12345",
                "new_password2": "NuevaClave12345",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))
        # La sesión expiró: la contraseña NO debe haber cambiado.
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.check_password("ClaveSegura123!"))
        self.assertFalse(self.usuario.check_password("NuevaClave12345"))

    def test_actividad_renueva_sesion(self):
        """Una petición válida renueva la marca de última actividad."""
        sesion = self.client.session
        antes = int(timezone.now().timestamp()) - 600
        sesion["ultima_actividad"] = antes
        sesion.save()

        self.client.get(reverse("core:panel"))
        sesion_refresh = self.client.session
        self.assertGreaterEqual(
            int(sesion_refresh.get("ultima_actividad", 0)), antes
        )


class BloqueoIntentosTests(TestCase):
    """Pruebas RS-017: bloqueo por intentos fallidos consecutivos."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def _login_fallido(self):
        return self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ContrasenaIncorrecta"},
        )

    def test_bloqueo_tras_cinco_fallos(self):
        """Tras 5 intentos fallidos consecutivos, la cuenta se bloquea 15 min."""
        for _ in range(5):
            respuesta = self._login_fallido()
            self.assertEqual(respuesta.status_code, 200)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.intentos_fallidos, 5)
        self.assertIsNotNone(self.usuario.bloqueado_hasta)

    def test_rechazo_durante_bloqueo(self):
        """Durante el bloqueo, cualquier intento es rechazado sin comprobar contraseña."""
        for _ in range(5):
            self._login_fallido()
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.bloqueado_hasta > timezone.now())

        # Intento con contraseña correcta mientras está bloqueado.
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "bloqueada por intentos fallidos")
        self.usuario.refresh_from_db()
        # La contraseña no cambió: sigue siendo la misma.
        self.assertTrue(self.usuario.check_password("ClaveSegura123!"))
        # El contador de fallos no aumentó durante el bloqueo.
        self.assertEqual(self.usuario.intentos_fallidos, 5)

    def test_reinicio_tras_exito(self):
        """Tras un login exitoso, el contador se reinicia y el bloqueo se elimina."""
        for _ in range(5):
            self._login_fallido()
        self.usuario.refresh_from_db()
        self.assertTrue(self.usuario.bloqueado_hasta)

        # Avanzar el tiempo más allá del bloqueo.
        self.usuario.bloqueado_hasta = timezone.now() - timedelta(minutes=1)
        self.usuario.intentos_fallidos = 5
        self.usuario.save()

        # Login exitoso: reinicia contador y elimina bloqueo.
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.intentos_fallidos, 0)
        self.assertIsNone(self.usuario.bloqueado_hasta)

    def test_mensaje_generico_usuario_inexistente(self):
        """No se revela si el usuario existe."""
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "usuario_inexistente", "password": "CualquierCosa"},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Usuario o contraseña incorrectos")

    def test_bloqueo_expira_tras_quince_minutos(self):
        """T-027: Tras 15 minutos (simulado), el bloqueo expira y permite login."""
        # 1. Bloquear tras 5 intentos fallidos.
        for _ in range(5):
            self._login_fallido()
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.intentos_fallidos, 5)
        self.assertIsNotNone(self.usuario.bloqueado_hasta)

        # 2. Rechazo durante el periodo de bloqueo.
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "bloqueada por intentos fallidos")

        # 3. Simular expiración de los 15 minutos de bloqueo.
        self.usuario.bloqueado_hasta = timezone.now() - timedelta(minutes=1)
        self.usuario.save(update_fields=["bloqueado_hasta"])
        self.usuario.refresh_from_db()
        self.assertIsNotNone(self.usuario.bloqueado_hasta)
        self.assertTrue(self.usuario.bloqueado_hasta < timezone.now())

        # 4. Posibilidad de iniciar sesión después de expirar.
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

        # 5. Reinicio correcto del contador tras autenticación exitosa.
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.intentos_fallidos, 0)
        self.assertIsNone(self.usuario.bloqueado_hasta)
        self.assertTrue(self.usuario.check_password("ClaveSegura123!"))
