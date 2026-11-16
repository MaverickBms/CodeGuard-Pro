"""Pruebas básicas de los modelos de evaluación académica (Fase 4, ADR-011)."""

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.roadmaps.models import (
    Etapa,
    Modulo,
    Pregunta,
    Quiz,
    ResultadoEvaluacion,
    ResultadoPregunta,
    Roadmap,
)


class QuizPreguntaModelTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO evaluacion", edicion="test")
        self.etapa = Etapa.objects.create(roadmap=self.roadmap, numero=0, titulo="Fundamentos")
        self.modulo = Modulo.objects.create(etapa=self.etapa, numero="0.1", titulo="Introducción")

    def test_quiz_guarda_umbral_y_valida_rango(self):
        quiz = Quiz.objects.create(
            nombre="Quiz módulo 0.1",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            umbral_aprobacion=75,
        )
        self.assertEqual(quiz.umbral_aprobacion, 75)

        quiz.umbral_aprobacion = 101
        with self.assertRaises(ValidationError):
            quiz.full_clean()

    def test_quiz_tipo_quiz_requiere_modulo(self):
        quiz = Quiz(
            nombre="Quiz sin módulo",
            tipo=Quiz.TIPO_QUIZ,
            umbral_aprobacion=70,
        )
        with self.assertRaises(ValidationError) as ctx:
            quiz.full_clean()
        self.assertIn("modulo", ctx.exception.message_dict)

    def test_pregunta_formatos_validos_y_estructura(self):
        quiz = Quiz.objects.create(nombre="Quiz formatos", tipo=Quiz.TIPO_QUIZ, modulo=self.modulo)

        seleccion = Pregunta(
            quiz=quiz,
            orden=1,
            formato=Pregunta.FORMATO_SELECCION,
            enunciado="¿Cuál es correcta?",
            datos_respuesta={"opciones": [{"texto": "A", "correcta": True}, {"texto": "B", "correcta": False}]},
        )
        seleccion.full_clean()
        seleccion.save()

        respuesta = Pregunta(
            quiz=quiz,
            orden=2,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Escribe la palabra clave.",
            datos_respuesta={"respuesta_esperada": "variable"},
        )
        respuesta.full_clean()
        respuesta.save()

        interpretacion = Pregunta(
            quiz=quiz,
            orden=3,
            formato=Pregunta.FORMATO_INTERPRETACION,
            enunciado="Interpreta el código.",
            datos_respuesta={"criterios": ["Identifica la salida"]},
        )
        interpretacion.full_clean()
        interpretacion.save()

        resolucion = Pregunta(
            quiz=quiz,
            orden=4,
            formato=Pregunta.FORMATO_RESOLUCION,
            enunciado="Resuelve el problema.",
            datos_respuesta={"criterios": ["Plantea el enfoque"]},
        )
        resolucion.full_clean()
        resolucion.save()

    def test_pregunta_rechaza_formato_invalido(self):
        quiz = Quiz.objects.create(nombre="Quiz invalido", tipo=Quiz.TIPO_QUIZ, modulo=self.modulo)
        pregunta = Pregunta(
            quiz=quiz,
            orden=1,
            formato="ensayo_libre",
            enunciado="Texto",
            datos_respuesta={},
        )
        with self.assertRaises(ValidationError) as ctx:
            pregunta.full_clean()
        self.assertIn("formato", ctx.exception.message_dict)

    def test_pregunta_seleccion_requiere_opcion_correcta(self):
        quiz = Quiz.objects.create(nombre="Quiz seleccion", tipo=Quiz.TIPO_QUIZ, modulo=self.modulo)
        pregunta = Pregunta(
            quiz=quiz,
            orden=1,
            formato=Pregunta.FORMATO_SELECCION,
            enunciado="Pregunta",
            datos_respuesta={"opciones": [{"texto": "A", "correcta": False}]},
        )
        with self.assertRaises(ValidationError) as ctx:
            pregunta.full_clean()
        self.assertIn("datos_respuesta", ctx.exception.message_dict)


class ResultadoEvaluacionModelTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-eval", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO evaluacion", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=0, titulo="Fundamentos")
        modulo = Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Introducción")
        self.quiz = Quiz.objects.create(
            nombre="Quiz módulo 0.1",
            tipo=Quiz.TIPO_QUIZ,
            modulo=modulo,
            umbral_aprobacion=70,
        )
        self.pregunta = Pregunta.objects.create(
            quiz=self.quiz,
            orden=1,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Define variable",
            datos_respuesta={"respuesta_esperada": "x"},
        )

    def test_resultado_aprobado_segun_umbral(self):
        aprobado = ResultadoEvaluacion.objects.create(
            quiz=self.quiz,
            usuario=self.usuario,
            puntuacion=70,
            aprobado=True,
            umbral_aprobacion=70,
            respuestas={"1": "x"},
            retroalimentacion="Correcto",
        )
        self.assertTrue(aprobado.esta_aprobado)
        self.assertEqual(aprobado.get_resultado_estado(), "aprobado")

        reprobado = ResultadoEvaluacion.objects.create(
            quiz=self.quiz,
            usuario=self.usuario,
            puntuacion=69,
            aprobado=False,
            umbral_aprobacion=70,
            respuestas={"1": "y"},
        )
        self.assertFalse(reprobado.esta_aprobado)
        self.assertEqual(reprobado.get_resultado_estado(), "no_aprobado")

    def test_resultado_no_puede_aprobar_bajo_umbral(self):
        resultado = ResultadoEvaluacion(
            quiz=self.quiz,
            usuario=self.usuario,
            puntuacion=60,
            aprobado=True,
            umbral_aprobacion=70,
        )
        with self.assertRaises(ValidationError):
            resultado.full_clean()

    def test_resultado_evidencia_inmutable(self):
        resultado = ResultadoEvaluacion.objects.create(
            quiz=self.quiz,
            usuario=self.usuario,
            puntuacion=80,
            aprobado=True,
            umbral_aprobacion=70,
            respuestas={"1": "x"},
        )
        resultado.puntuacion = 90
        with self.assertRaises(ValidationError):
            resultado.save()
        with self.assertRaises(ValidationError):
            resultado.delete()

    def test_resultado_pregunta_unico_por_resultado(self):
        resultado = ResultadoEvaluacion.objects.create(
            quiz=self.quiz,
            usuario=self.usuario,
            puntuacion=100,
            aprobado=True,
            umbral_aprobacion=70,
        )
        ResultadoPregunta.objects.create(
            resultado=resultado,
            pregunta=self.pregunta,
            correcta=True,
            puntuacion=100,
            respuesta={"valor": "x"},
        )
        duplicado = ResultadoPregunta(
            resultado=resultado,
            pregunta=self.pregunta,
            correcta=False,
            puntuacion=0,
        )
        with self.assertRaises(ValidationError):
            duplicado.full_clean()
