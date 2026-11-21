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

    def test_no_eleva_una_cuenta_ordinaria_creada_despues(self):
        propietario = asegurar_propietario_local()
        ordinaria = get_user_model().objects.create_user(
            username="cuenta-ordinaria", password="ClaveSegura123!"
        )

        elegido = asegurar_propietario_local()

        self.assertEqual(elegido.pk, propietario.pk)
        ordinaria.refresh_from_db()
        self.assertFalse(ordinaria.es_propietario_local)
        self.assertFalse(ordinaria.is_staff)
        self.assertTrue(propietario.es_propietario_local)

    def test_recupera_el_nombre_reservado_heredado_sin_elevar_otras_cuentas(self):
        heredado = get_user_model().objects.create_user(
            username=USERNAME_PROPIETARIO_LOCAL, password="ClaveSegura123!"
        )
        ordinaria = get_user_model().objects.create_user(
            username="cuenta-ordinaria", password="ClaveSegura123!"
        )

        elegido = asegurar_propietario_local()

        self.assertEqual(elegido.pk, heredado.pk)
        heredado.refresh_from_db()
        ordinaria.refresh_from_db()
        self.assertTrue(heredado.es_propietario_local)
        self.assertTrue(heredado.is_staff)
        self.assertFalse(ordinaria.es_propietario_local)
        self.assertFalse(ordinaria.is_staff)

    def test_perfil_ambiguo_no_elige_ni_eleva_una_cuenta(self):
        get_user_model().objects.create_user(
            username="cuenta-a", password="ClaveSegura123!"
        )
        get_user_model().objects.create_user(
            username="cuenta-b", password="ClaveSegura123!"
        )

        self.assertIsNone(asegurar_propietario_local())
        self.assertFalse(
            get_user_model().objects.filter(is_staff=True).exists()
        )
        self.assertFalse(
            get_user_model().objects.filter(es_propietario_local=True).exists()
        )
