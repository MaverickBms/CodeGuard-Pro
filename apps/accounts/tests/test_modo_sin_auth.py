"""Pruebas del modo sin autenticación de CodeGuard Pro.

Verifica que:

1. La aplicación abre directamente el panel principal.
2. No existe redirección obligatoria al inicio de sesión.
3. Las rutas principales funcionan sin autenticación.
4. Las funcionalidades de los roadmaps siguen funcionando.
5. Las rutas de autenticación no permiten iniciar flujos desactivados.

El sistema de autenticación original se conserva íntegro y se verifica
mediante override_settings(AUTH_DISABLED=False) en el resto de pruebas.
"""

from django.test import TestCase, override_settings
from django.urls import reverse

from apps.audit.models import AuditLog
from apps.roadmaps.models import Progreso
from apps.roadmaps.services import (
    etapas_completadas,
    marcar_etapa,
    marcar_leccion,
    mapa_progreso_lecciones,
)


@override_settings(AUTH_DISABLED=True)
class ModoSinAutenticacionTests(TestCase):
    """Comportamiento de la aplicación con autenticación desactivada."""

    def test_panel_abre_directamente_sin_credenciales(self):
        """El panel se abre directamente sin solicitar inicio de sesión."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Panel principal")
        self.assertContains(respuesta, "Acceso local sin autenticación")

    def test_no_redireccion_obligatoria_al_login(self):
        """No existe redirección obligatoria al inicio de sesión."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)

    def test_rutas_principales_funcionan_sin_autenticacion(self):
        """Panel y roadmap lista responden 200 sin autenticación."""
        for url_name in ["core:panel", "roadmaps:lista"]:
            respuesta = self.client.get(reverse(url_name))
            self.assertEqual(respuesta.status_code, 200, msg=url_name)

    def test_paneles_roadmaps_muestran_temas_visuales(self):
        """Las 12 temáticas visuales siguen presentes en el selector."""
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        for tema in [
            "light", "dark", "high-contrast", "retro-pixel", "cyberpunk",
            "fantasy", "sci-fi", "warrior", "mage", "rogue", "paladin", "dark-mage",
        ]:
            self.assertContains(respuesta, f'data-theme="{tema}"')

    def test_ruta_login_redirige_al_panel(self):
        """La ruta de login redirige al panel mientras la autenticación está desactivada."""
        respuesta = self.client.get(reverse("accounts:login"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_ruta_setup_redirige_al_panel(self):
        """La ruta de configuración inicial redirige al panel."""
        respuesta = self.client.get(reverse("accounts:setup"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_ruta_logout_redirige_al_panel(self):
        """La ruta de cierre de sesión redirige al panel."""
        respuesta = self.client.post(reverse("accounts:logout"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_ruta_rescate_redirige_al_panel(self):
        """La ruta de recuperación redirige al panel."""
        respuesta = self.client.get(reverse("accounts:rescate"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_ruta_resetear_contraseña_redirige_al_panel(self):
        """La ruta de restablecimiento redirige al panel."""
        respuesta = self.client.get(reverse("accounts:resetear_contrasena"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_ruta_cambiar_contraseña_redirige_al_panel(self):
        """La ruta de cambio de contraseña redirige al panel."""
        respuesta = self.client.get(reverse("accounts:cambiar_contraseña"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_login_post_no_autentica(self):
        """Un POST a login con credenciales válidas no inicia sesión."""
        respuesta = self.client.post(
            reverse("accounts:login"),
            {"username": "usuario", "password": "cualquiera"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.url, reverse("core:panel"))

    def test_navegacion_sin_botones_desactivados(self):
        """No aparece el formulario de cierre de sesión en la navegación."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotContains(respuesta, "Cerrar sesión")
        self.assertNotContains(respuesta, "accounts:logout")

    def test_request_user_permanece_anonimo(self):
        """request.user permanece como AnonymousUser en modo sin autenticación."""
        from django.contrib.auth.models import AnonymousUser

        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertIsInstance(respuesta.wsgi_request.user, AnonymousUser)

    def test_12_temas_presentes(self):
        """Las 12 temáticas visuales siguen presentes en la aplicación."""
        respuesta = self.client.get(reverse("core:panel"))
        self.assertEqual(respuesta.status_code, 200)
        for tema in [
            "light", "dark", "high-contrast", "retro-pixel", "cyberpunk",
            "fantasy", "sci-fi", "warrior", "mage", "rogue", "paladin", "dark-mage",
        ]:
            self.assertContains(respuesta, f'data-theme="{tema}"')


@override_settings(AUTH_DISABLED=True)
class ProgresoPersistenciaTests(TestCase):
    """Persistencia y recuperación del progreso sin autenticación.

    Verifica que el progreso se guarda y recupera utilizando el propietario
    local existente, sin crear usuarios ficticios ni modificar el esquema.
    """

    @classmethod
    def setUpTestData(cls):
        from django.contrib.auth import get_user_model
        from apps.roadmaps.models import (
            Etapa, Leccion, Modulo, Roadmap,
        )
        from apps.roadmaps.services import cargar_ascenso

        cls.usuario_local = get_user_model().objects.create_user(
            username="usuario_local", password="ClaveSegura123!"
        )
        cls.roadmap = cargar_ascenso()
        cls.etapa0 = Etapa.objects.get(roadmap=cls.roadmap, numero=0)
        cls.modulo0 = Modulo.objects.filter(etapa=cls.etapa0).first()
        cls.leccion0 = Leccion.objects.filter(modulo=cls.modulo0).first()

    def setUp(self):
        self.usuario_local = self.__class__.usuario_local
        self.assertIsNotNone(self.usuario_local)

    def test_request_user_anonimo_con_usuario_local_existente(self):
        """request.user es AnonymousUser aunque exista propietario local."""
        from django.contrib.auth.models import AnonymousUser
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertIsInstance(respuesta.wsgi_request.user, AnonymousUser)

    def test_guardar_y_recuperar_progreso_etapa(self):
        """Marcar etapa sin login guarda y recupera con el propietario local."""
        from apps.roadmaps.services import marcar_etapa, etapas_completadas
        from apps.audit.models import AuditLog

        # 1. Marcar etapa como completada sin autenticación.
        respuesta = self.client.post(
            reverse("roadmaps:marcar_etapa", args=[self.etapa0.numero]),
            {"completada": "1"},
        )
        self.assertEqual(respuesta.status_code, 302)

        # 2. Verificar que el progreso está asociado al propietario local.
        progreso = Progreso.objects.filter(
            usuario=self.usuario_local,
            etapa=self.etapa0,
            modulo__isnull=True,
            leccion__isnull=True,
        ).first()
        self.assertIsNotNone(progreso)
        self.assertEqual(progreso.estado, "completado")

        # 3. Volver a consultar el roadmap: la etapa aparece como completada.
        respuesta = self.client.get(reverse("roadmaps:detalle", args=[self.etapa0.numero]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.context["completada"])

        # 4. La lista de etapas también refleja el completado (a través de avance).
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["avance"]["completadas"], 1)
        self.assertEqual(respuesta.context["avance"]["total"], 33)

        # 5. La auditoría registra usuario=None (actor nulo), aunque el
        # progreso esté asociado al propietario local.
        evento = AuditLog.objects.filter(
            evento="roadmap_etapa_completada"
        ).first()
        self.assertIsNotNone(evento)
        self.assertIsNone(evento.usuario)
        self.assertIn(f"Etapa {self.etapa0.numero}", evento.descripcion)

    def test_guardar_y_recuperar_progreso_leccion(self):
        """Marcar lección sin login guarda y recupera con el propietario local."""
        from apps.roadmaps.services import marcar_leccion, mapa_progreso_lecciones
        from apps.audit.models import AuditLog

        # 1. Marcar lección como completada sin autenticación.
        respuesta = self.client.post(
            reverse("roadmaps:marcar_leccion", args=[self.leccion0.pk]),
            {"completada": "1"},
        )
        self.assertEqual(respuesta.status_code, 302)

        # 2. Verificar que el progreso está asociado al propietario local.
        progreso = Progreso.objects.filter(
            usuario=self.usuario_local,
            etapa=self.etapa0,
            modulo=self.modulo0,
            leccion=self.leccion0,
        ).first()
        self.assertIsNotNone(progreso)
        self.assertEqual(progreso.estado, "completado")

        # 3. Volver a consultar el detalle: la lección aparece como completada.
        respuesta = self.client.get(reverse("roadmaps:detalle", args=[self.etapa0.numero]))
        self.assertEqual(respuesta.status_code, 200)
        lecciones = respuesta.context["modulos"][0].lecciones_lista
        leccion_en_contexto = next(
            (l for l in lecciones if l.id == self.leccion0.id), None
        )
        self.assertIsNotNone(leccion_en_contexto)
        self.assertTrue(leccion_en_contexto.completada)

        # 4. La auditoría registra usuario=None.
        evento = AuditLog.objects.filter(
            evento="roadmap_leccion_completada"
        ).first()
        self.assertIsNotNone(evento)
        self.assertIsNone(evento.usuario)
        self.assertIn(self.leccion0.titulo, evento.descripcion)

    def test_progreso_recuperado_despues_de_marcar_etapa(self):
        """El progreso marcado previamente se recupera al volver a consultar."""
        from apps.roadmaps.services import etapas_completadas

        # 1. Marcar etapa.
        self.client.post(
            reverse("roadmaps:marcar_etapa", args=[self.etapa0.numero]),
            {"completada": "1"},
        )

        # 2. Consultar etapas_completadas con el propietario local.
        completadas = etapas_completadas(self.usuario_local, self.roadmap)
        self.assertIn(self.etapa0.numero, completadas)

        # 3. Consultar la lista por HTTP: la etapa aparece completada.
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.context["avance"]["completadas"], 1)
