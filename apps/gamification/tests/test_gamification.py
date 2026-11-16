from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.gamification.models import Logro, LogroObtenido, PerfilGamificacion, TransaccionMoneda
from apps.gamification.services import acreditar_monedas, otorgar_logro


class GamificationServicesTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="jugador", password="ClaveSegura123!"
        )

    def test_acreditar_monedas_actualiza_saldo_y_registra_transaccion(self):
        tx = acreditar_monedas(self.usuario, 50, "Recompensa de prueba")
        perfil = PerfilGamificacion.objects.get(usuario=self.usuario)
        self.assertEqual(perfil.saldo_monedas, 50)
        self.assertEqual(tx.monto, 50)
        self.assertEqual(tx.tipo, "credito")
        self.assertEqual(tx.saldo_resultante, 50)
        self.assertEqual(TransaccionMoneda.objects.filter(usuario=self.usuario).count(), 1)

    def test_acreditar_monedas_es_idempotente_por_referencia(self):
        acreditar_monedas(self.usuario, 30, "Bonus", referencia="bonus:1")
        acreditar_monedas(self.usuario, 30, "Bonus", referencia="bonus:1")
        perfil = PerfilGamificacion.objects.get(usuario=self.usuario)
        self.assertEqual(perfil.saldo_monedas, 30)
        self.assertEqual(
            TransaccionMoneda.objects.filter(usuario=self.usuario, referencia="bonus:1").count(),
            1,
        )

    def test_otorgar_logro_no_duplica_y_acredita_recompensa_una_vez(self):
        logro = Logro.objects.create(
            clave="primer-paso",
            nombre="Primer paso",
            recompensa_monedas=25,
            activo=True,
        )
        obtenido, creado = otorgar_logro(self.usuario, logro, origen="test")
        self.assertTrue(creado)
        self.assertEqual(LogroObtenido.objects.filter(usuario=self.usuario, logro=logro).count(), 1)

        obtenido2, creado2 = otorgar_logro(self.usuario, logro, origen="test")
        self.assertFalse(creado2)
        self.assertEqual(obtenido.id, obtenido2.id)
        self.assertEqual(LogroObtenido.objects.filter(usuario=self.usuario, logro=logro).count(), 1)

        perfil = PerfilGamificacion.objects.get(usuario=self.usuario)
        self.assertEqual(perfil.saldo_monedas, 25)
        self.assertEqual(
            TransaccionMoneda.objects.filter(usuario=self.usuario, tipo="credito").count(),
            1,
        )
