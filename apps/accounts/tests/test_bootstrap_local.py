"""Pruebas del propietario local para el modo sin autenticación."""

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from apps.accounts.bootstrap import USERNAME_PROPIETARIO_LOCAL, asegurar_propietario_local
from apps.core.models import ConfiguracionSistema


@override_settings(AUTH_DISABLED=True)
class PropietarioLocalTests(TestCase):
    def test_crea_un_unico_propietario_sin_credenciales(self):
        usuario = asegurar_propietario_local()

        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.username, USERNAME_PROPIETARIO_LOCAL)
        self.assertFalse(usuario.has_usable_password())
        self.assertTrue(usuario.is_active)
        self.assertTrue(usuario.is_staff)
        self.assertIsNotNone(usuario.fecha_configuracion_inicial)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertTrue(ConfiguracionSistema.cargar().configuracion_inicial_completada)

    def test_es_idempotente_y_reutiliza_un_usuario_existente(self):
        primero = asegurar_propietario_local()
        segundo = asegurar_propietario_local()
        self.assertEqual(primero.pk, segundo.pk)

        existente = get_user_model().objects.create_user(
            username="propietario-personalizado"
        )
        tercero = asegurar_propietario_local()
        self.assertEqual(tercero.pk, primero.pk)
        self.assertNotEqual(tercero.pk, existente.pk)

    def test_no_crea_usuarios_si_la_autenticacion_esta_activa(self):
        with override_settings(AUTH_DISABLED=False):
            self.assertIsNone(asegurar_propietario_local())
        self.assertFalse(get_user_model().objects.exists())
