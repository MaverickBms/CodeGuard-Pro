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


from apps.gamification.services import evaluar_logros_academicos
from apps.roadmaps.models import Etapa, Modulo, Progreso, Roadmap


class LogrosAcademicosTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="jugador-logros", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO logros", edicion="test")

    def test_otorga_primer_modulo_y_no_duplica(self):
        etapa = Etapa.objects.create(roadmap=self.roadmap, numero=1, titulo="Etapa 1")
        modulo = Modulo.objects.create(etapa=etapa, numero="1.1", titulo="Módulo 1")
        Progreso.objects.create(
            usuario=self.usuario, etapa=etapa, modulo=modulo, leccion=None, actividad=None,
            estado="completado", porcentaje=100,
        )
        evaluar_logros_academicos(self.usuario)
        self.assertTrue(LogroObtenido.objects.filter(usuario=self.usuario, logro__clave="primer-modulo").exists())
        saldo1 = PerfilGamificacion.objects.get(usuario=self.usuario).saldo_monedas
        evaluar_logros_academicos(self.usuario)
        self.assertEqual(LogroObtenido.objects.filter(usuario=self.usuario, logro__clave="primer-modulo").count(), 1)
        saldo2 = PerfilGamificacion.objects.get(usuario=self.usuario).saldo_monedas
        self.assertEqual(saldo1, saldo2)

    def test_otorga_primera_etapa(self):
        etapa = Etapa.objects.create(roadmap=self.roadmap, numero=1, titulo="Etapa 1")
        Progreso.objects.create(
            usuario=self.usuario, etapa=etapa, modulo=None, leccion=None, actividad=None,
            estado="completado", porcentaje=100,
        )
        evaluar_logros_academicos(self.usuario)
        self.assertTrue(LogroObtenido.objects.filter(usuario=self.usuario, logro__clave="primera-etapa").exists())

from apps.gamification.models import AvatarPerfil, PersonajeGuia, ZonaMundo
from apps.gamification.services import obtener_avatar


class Fase6BaseTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="avatar-user", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO mundo", edicion="test")
        self.etapa = Etapa.objects.create(roadmap=self.roadmap, numero=1, titulo="Etapa 1")

    def test_obtener_avatar_crea_y_reutiliza(self):
        avatar = obtener_avatar(self.usuario)
        self.assertIsNotNone(avatar)
        self.assertEqual(avatar.usuario, self.usuario)
        avatar2 = obtener_avatar(self.usuario)
        self.assertEqual(avatar.id, avatar2.id)
        self.assertEqual(AvatarPerfil.objects.filter(usuario=self.usuario).count(), 1)

    def test_zona_y_personaje_guia(self):
        zona = ZonaMundo.objects.create(etapa=self.etapa, nombre="Zona 1", orden=1)
        personaje = PersonajeGuia.objects.create(zona=zona, nombre="Guía", rol="Mentor")
        self.assertEqual(str(zona), "Zona 1 (Etapa 1)")
        self.assertIn("Guía", str(personaje))
