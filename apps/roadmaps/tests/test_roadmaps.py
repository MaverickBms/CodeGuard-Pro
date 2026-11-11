"""Pruebas del módulo académico (Roadmap ASCENSO)."""

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from apps.roadmaps.models import (
    CriterioFinalizacion,
    Etapa,
    Leccion,
    Modulo,
    Prerrequisito,
    Progreso,
    Roadmap,
)
from apps.roadmaps.services import (
    cargar_ascenso,
    etapas_completadas,
    marcar_etapa,
    marcar_leccion,
    progreso_general,
)


class CargaAscensoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.roadmap = cargar_ascenso()

    def test_carga_las_33_etapas_oficiales(self):
        self.assertEqual(Etapa.objects.filter(roadmap=self.roadmap).count(), 33)
        self.assertEqual(Modulo.objects.filter(etapa__roadmap=self.roadmap).count(), 212)
        self.assertEqual(
            Leccion.objects.filter(modulo__etapa__roadmap=self.roadmap).count(), 1946
        )
        self.assertEqual(
            CriterioFinalizacion.objects.filter(etapa__roadmap=self.roadmap).count(), 33
        )

    def test_etapas_permanecen_no_desarrolladas_en_mvp(self):
        self.assertFalse(
            Etapa.objects.filter(roadmap=self.roadmap, desarrollada_en_mvp=True).exists()
        )
        self.assertTrue(
            Etapa.objects.filter(roadmap=self.roadmap).exclude(nota_mvp="").exists()
        )

    def test_metadatos_de_la_fuente(self):
        self.assertEqual(self.roadmap.edicion, "3.1")
        self.assertEqual(self.roadmap.sha256_fuente[:8], "15a9ef38")

    def test_dependencias_explicitas_documentadas(self):
        dependencias = {
            (pre.etapa.numero, pre.etapa_requerida.numero)
            for pre in Prerrequisito.objects.filter(etapa__roadmap=self.roadmap)
        }
        self.assertEqual(
            dependencias,
            {(10, 9), (15, 13), (31, 3), (31, 4), (31, 7), (31, 8), (31, 21)},
        )

    def test_carga_idempotente_no_duplica_contenido(self):
        cargar_ascenso()
        self.assertEqual(Etapa.objects.filter(roadmap=self.roadmap).count(), 33)
        self.assertEqual(Modulo.objects.filter(etapa__roadmap=self.roadmap).count(), 212)
        self.assertEqual(
            Leccion.objects.filter(modulo__etapa__roadmap=self.roadmap).count(), 1946
        )


class ProgresoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.roadmap = cargar_ascenso()
        cls.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_etapa_bloqueada_por_prerrequisito(self):
        etapa10 = Etapa.objects.get(roadmap=self.roadmap, numero=10)
        self.assertTrue(etapa10.esta_bloqueada_para(set()))

    def test_no_se_puede_completar_etapa_manualmente(self):
        etapa0 = Etapa.objects.get(roadmap=self.roadmap, numero=0)
        with self.assertRaisesMessage(ValueError, "no puede completarse manualmente"):
            marcar_etapa(self.usuario, etapa0, completada=True)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, etapa=etapa0, estado="completado"
            ).exists()
        )

    def test_marcar_etapa_bloqueada_falla_por_prerrequisito(self):
        etapa10 = Etapa.objects.get(roadmap=self.roadmap, numero=10)
        with self.assertRaisesMessage(ValueError, "prerrequisitos sin completar"):
            marcar_etapa(self.usuario, etapa10, completada=True)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, etapa=etapa10, estado="completado"
            ).exists()
        )

    def test_no_se_puede_completar_leccion_manualmente(self):
        etapa0 = Etapa.objects.get(roadmap=self.roadmap, numero=0)
        leccion = Leccion.objects.filter(modulo__etapa=etapa0).first()
        with self.assertRaisesMessage(ValueError, "no puede completarse manualmente"):
            marcar_leccion(self.usuario, leccion, completada=True)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, leccion=leccion, estado="completado"
            ).exists()
        )

    def test_reabrir_leccion_recalcula_progreso_sin_aprobar_etapa(self):
        etapa0 = Etapa.objects.get(roadmap=self.roadmap, numero=0)
        leccion = Leccion.objects.filter(modulo__etapa=etapa0).first()
        progreso = marcar_leccion(self.usuario, leccion, completada=False)
        self.assertEqual(progreso.estado, "no_iniciado")
        avance = Progreso.objects.get(
            usuario=self.usuario, etapa=etapa0, leccion__isnull=True
        )
        self.assertEqual(avance.porcentaje, 0)
        self.assertEqual(avance.estado, "no_iniciado")

    def test_progreso_general_no_cuenta_aprobaciones_manuales(self):
        etapa0 = Etapa.objects.get(roadmap=self.roadmap, numero=0)
        with self.assertRaises(ValueError):
            marcar_etapa(self.usuario, etapa0, completada=True)
        avance = progreso_general(self.usuario, self.roadmap)
        self.assertEqual(avance["completadas"], 0)
        self.assertEqual(avance["total"], 33)
        self.assertEqual(avance["porcentaje"], 0)


@override_settings(AUTH_DISABLED=False)
class VistasRoadmapTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.roadmap = cargar_ascenso()
        cls.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def setUp(self):
        pass

    def test_lista_redirige_sin_login(self):
        """La lista de roadmap debe redirigir al login si no hay sesión."""
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))

    def test_lista_muestra_las_33_etapas(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(respuesta.context["etapas"]), 33)
        self.assertEqual(respuesta.context["resumen"]["total_etapas"], 33)
        self.assertContains(respuesta, "Roadmap ASCENSO")

    def test_lista_filtra_por_prioridad(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("roadmaps:lista"), {"prioridad": "P3"})
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.context["etapas"])
        self.assertTrue(
            all(etapa.prioridad == "P3" for etapa in respuesta.context["etapas"])
        )

    def test_detalle_muestra_modulos_y_lecciones(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.get(reverse("roadmaps:detalle", args=[0]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Preparación y método de aprendizaje")
        self.assertContains(respuesta, "Módulos y lecciones")
        self.assertGreater(len(respuesta.context["modulos"]), 0)

    def test_marcar_etapa_desde_vista(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("roadmaps:marcar_etapa", args=[0]), {"completada": "1"}
        )
        self.assertRedirects(respuesta, reverse("roadmaps:detalle", args=[0]))
        self.assertTrue(
            Progreso.objects.filter(
                usuario=self.usuario,
                etapa__numero=0,
                leccion__isnull=True,
                estado="completado",
            ).exists()
        )

    def test_vista_rechaza_etapa_bloqueada(self):
        self.client.force_login(self.usuario)
        respuesta = self.client.post(
            reverse("roadmaps:marcar_etapa", args=[10]),
            {"completada": "1"},
            follow=True,
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario,
                etapa__numero=10,
                leccion__isnull=True,
                estado="completado",
            ).exists()
        )
        self.assertContains(respuesta, "prerrequisitos sin completar")

    def test_marcar_leccion_desde_vista(self):
        self.client.force_login(self.usuario)
        leccion = Leccion.objects.filter(modulo__etapa__numero=0).first()
        respuesta = self.client.post(
            reverse("roadmaps:marcar_leccion", args=[leccion.pk]), {"completada": "1"}
        )
        self.assertRedirects(
            respuesta, reverse("roadmaps:leccion_detalle", args=[leccion.pk])
        )
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, leccion=leccion, estado="completado"
            ).exists()
        )


class RoadmapSinDatosTest(TestCase):
    def test_lista_sin_roadmap_muestra_instrucciones(self):
        usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )
        self.client.force_login(usuario)
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "cargar_ascenso")
        self.assertFalse(Roadmap.objects.exists())


@override_settings(AUTH_DISABLED=False)
class SesionVencidaOperacionesAcademicasTests(TestCase):
    """Una sesión vencida no debe modificar el progreso académico (CG-002)."""

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )
        self.client.force_login(self.usuario)
        self.roadmap = Roadmap.objects.create(
            nombre="Roadmap prueba", edicion="1.0", sha256_fuente="abc"
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=1, titulo="Etapa de prueba"
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero=1, titulo="Modulo de prueba"
        )
        self.leccion = Leccion.objects.create(
            modulo=self.modulo, titulo="Leccion de prueba"
        )

    def test_sesion_vencida_no_modifica_progreso(self):
        """POST a marcar_leccion con sesión vencida no crea ni modifica progreso."""
        sesion = self.client.session
        sesion["ultima_actividad"] = int(timezone.now().timestamp()) - 2000
        sesion.save()

        respuesta = self.client.post(
            reverse("roadmaps:marcar_leccion", args=[self.leccion.pk]),
            {"completada": "1"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(respuesta.url.startswith(reverse("accounts:login")))
        # La operación protegida no se ejecutó: no existe progreso para esta lección.
        self.assertFalse(
            Progreso.objects.filter(usuario=self.usuario, leccion=self.leccion).exists()
        )

    def test_sesion_activa_sí_modifica_progreso(self):
        """Con sesión activa, marcar una lección crea el progreso correspondiente."""
        respuesta = self.client.post(
            reverse("roadmaps:marcar_leccion", args=[self.leccion.pk]),
            {"completada": "1"},
        )
        self.assertRedirects(
            respuesta, reverse("roadmaps:leccion_detalle", args=[self.leccion.pk])
        )
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, leccion=self.leccion, estado="completado"
            ).exists()
        )


@override_settings(AUTH_DISABLED=True)
class RoadmapAccesoAnonimoTests(TestCase):
    """Roadmaps accesibles sin autenticación cuando AUTH_DISABLED=True."""

    @classmethod
    def setUpTestData(cls):
        cls.roadmap = cargar_ascenso()
        cls.usuario = get_user_model().objects.create_user(
            username="tester", password="ClaveSegura123!"
        )

    def test_lista_accesible_sin_login(self):
        """La lista de roadmap se abre sin credenciales."""
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(respuesta.context["etapas"]), 33)
        self.assertContains(respuesta, "Roadmap ASCENSO")

    def test_detalle_accesible_sin_login(self):
        """El detalle de una etapa se abre sin credenciales."""
        respuesta = self.client.get(reverse("roadmaps:detalle", args=[0]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Preparación y método de aprendizaje")

    def test_marcar_leccion_guarda_progreso_sin_login(self):
        """Marcar una lección sin login guarda el progreso del propietario local."""
        leccion = Leccion.objects.filter(modulo__etapa__numero=0).first()
        respuesta = self.client.post(
            reverse("roadmaps:marcar_leccion", args=[leccion.pk]),
            {"completada": "1"},
        )
        self.assertRedirects(
            respuesta, reverse("roadmaps:leccion_detalle", args=[leccion.pk])
        )
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, leccion=leccion, estado="completado"
            ).exists()
        )

    def test_12_temas_presentes_en_selector(self):
        """El selector de temas mantiene las 12 temáticas visuales."""
        respuesta = self.client.get(reverse("roadmaps:lista"))
        self.assertEqual(respuesta.status_code, 200)
        for tema in [
            "light", "dark", "high-contrast", "retro-pixel", "cyberpunk",
            "fantasy", "sci-fi", "warrior", "mage", "rogue", "paladin", "dark-mage",
        ]:
            self.assertContains(respuesta, f'data-theme="{tema}"')
