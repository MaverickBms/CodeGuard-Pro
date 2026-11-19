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
