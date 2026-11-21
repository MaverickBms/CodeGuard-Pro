"""Pruebas de los índices de evaluaciones y evidencias."""
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.roadmaps.models import (
    CriterioFinalizacion,
    CumplimientoCriterio,
    Etapa,
    Modulo,
    Prerrequisito,
    Roadmap,
)
from apps.roadmaps.models_evaluacion import Pregunta, Quiz


class EvaluacionesIndexTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="indice-evaluaciones", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO índices", edicion="3.1", activo=True
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Fundamentos"
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero="0.1", titulo="Introducción"
        )
        self.quiz = Quiz.objects.create(
            nombre="Quiz publicado",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        Pregunta.objects.create(
            quiz=self.quiz,
            orden=1,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="¿Qué es una variable?",
            datos_respuesta={"respuesta_esperada": "almacena un valor"},
        )
        Quiz.objects.create(
            nombre="Quiz borrador",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            version=2,
            estado=Quiz.ESTADO_BORRADOR,
        )

    def test_indice_muestra_solo_evaluaciones_publicadas(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:evaluaciones"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Quiz publicado")
        self.assertNotContains(respuesta, "Quiz borrador")
        self.assertContains(respuesta, "1 publicada")

    def test_indice_marca_evaluacion_de_etapa_bloqueada(self):
        etapa_bloqueada = Etapa.objects.create(
            roadmap=self.roadmap, numero=1, titulo="Etapa bloqueada"
        )
        Prerrequisito.objects.create(
            etapa=etapa_bloqueada, etapa_requerida=self.etapa
        )
        modulo = Modulo.objects.create(
            etapa=etapa_bloqueada, numero="1.1", titulo="Módulo bloqueado"
        )
        Quiz.objects.create(
            nombre="Quiz bloqueado",
            tipo=Quiz.TIPO_QUIZ,
            modulo=modulo,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:evaluaciones"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Quiz bloqueado")
        self.assertContains(respuesta, "Bloqueada")


class EvidenciasIndexTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="indice-evidencias", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO evidencias", edicion="3.1", activo=True
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Fundamentos"
        )
        self.criterio = CriterioFinalizacion.objects.create(
            etapa=self.etapa,
            titulo="Proyecto registrado",
            tipo="proyecto",
            obligatorio=True,
            orden=1,
        )
        CriterioFinalizacion.objects.create(
            etapa=self.etapa,
            titulo="Criterio pendiente",
            tipo="manual",
            obligatorio=True,
            orden=2,
        )
        CumplimientoCriterio.objects.create(
            usuario=self.usuario,
            criterio=self.criterio,
            satisfecho=True,
            origen="proyecto",
            evidencia="Repositorio con pruebas y documentación.",
        )

    def test_portafolio_muestra_evidencias_y_pendientes(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:evidencias"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Repositorio con pruebas y documentación.")
        self.assertContains(respuesta, "Proyecto registrado")
        self.assertContains(respuesta, "Criterio pendiente")
        self.assertContains(respuesta, "1 registrada")


class ConocimientoIndexTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO conocimiento", edicion="3.1", activo=True
        )
        Etapa.objects.create(roadmap=self.roadmap, numero=0, titulo="Fundamentos")

    def test_panel_de_conocimiento_es_solo_lectura_y_muestra_estado(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:conocimiento"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Estado del conocimiento")
        self.assertContains(respuesta, "solo lectura")
        self.assertContains(respuesta, "Sin fuentes registradas")
        self.assertContains(respuesta, "1.946 lecciones")
        self.assertNotContains(respuesta, 'name="accion"')


class NavegacionActivaTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO navegación", edicion="3.1", activo=True
        )
        Etapa.objects.create(roadmap=self.roadmap, numero=0, titulo="Fundamentos")

    def test_solo_un_acceso_aparece_activo(self):
        import re

        for nombre in (
            "core:panel",
            "roadmaps:lista",
            "roadmaps:evaluaciones",
            "roadmaps:evidencias",
            "roadmaps:conocimiento",
            "library:lista",
        ):
            with self.subTest(vista=nombre), override_settings(AUTH_DISABLED=True):
                respuesta = self.client.get(reverse(nombre))
                self.assertEqual(respuesta.status_code, 200)
                activos = re.findall(
                    r'class="nav-item[^"]*cg-nav-active', respuesta.content.decode()
                )
                self.assertEqual(
                    len(activos),
                    1,
                    f"{nombre} tiene {len(activos)} accesos activos; revisa la navegación.",
                )


class NavegacionEntreEtapasTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO paginación", edicion="3.1", activo=True
        )
        for numero in range(3):
            Etapa.objects.create(
                roadmap=self.roadmap,
                numero=numero,
                titulo=f"Etapa {numero}",
                orden=numero,
            )

    def test_detalle_enlaza_etapa_anterior_y_siguiente(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:detalle", args=[1]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Navegación entre etapas")
        self.assertContains(respuesta, reverse("roadmaps:detalle", args=[0]))
        self.assertContains(respuesta, reverse("roadmaps:detalle", args=[2]))

    def test_primera_etapa_no_tiene_enlace_anterior(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("roadmaps:detalle", args=[0]))
        self.assertIsNone(respuesta.context["etapa_anterior"])
        self.assertContains(respuesta, reverse("roadmaps:detalle", args=[1]))
