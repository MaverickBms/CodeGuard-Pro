"""Pruebas básicas de los modelos y corrección de evaluación (Fase 4, ADR-011)."""

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.audit.models import AuditLog
from apps.roadmaps.models import (
    CriterioFinalizacion,
    CumplimientoCriterio,
    Etapa,
    Modulo,
    Pregunta,
    Quiz,
    ResultadoEvaluacion,
    ResultadoPregunta,
    Prerrequisito,
    Roadmap,
)
from apps.roadmaps.services_evaluacion import evaluar_quiz, registrar_cumplimiento_criterio


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


class CorreccionAutomaticaQuizTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-correccion", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO correccion", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=1, titulo="Etapa 1")
        self.modulo = Modulo.objects.create(etapa=etapa, numero="1.1", titulo="Módulo 1")
        self.quiz = Quiz.objects.create(
            nombre="Quiz corrección",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            umbral_aprobacion=70,
        )
        self.p1 = Pregunta.objects.create(
            quiz=self.quiz,
            orden=1,
            formato=Pregunta.FORMATO_SELECCION,
            enunciado="Selecciona la correcta",
            datos_respuesta={
                "opciones": [
                    {"texto": "A", "correcta": True},
                    {"texto": "B", "correcta": False},
                ]
            },
        )
        self.p2 = Pregunta.objects.create(
            quiz=self.quiz,
            orden=2,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Escribe la palabra",
            datos_respuesta={"respuesta_esperada": "variable", "sensible_mayusculas": False},
        )

    def test_evaluar_quiz_aprobado_y_registra_evidencia(self):
        resultado = evaluar_quiz(
            self.usuario,
            self.quiz,
            {str(self.p1.id): 0, str(self.p2.id): "  Variable  "},
        )

        self.assertEqual(resultado.puntuacion, 100)
        self.assertTrue(resultado.aprobado)
        self.assertFalse(resultado.requiere_revision)
        self.assertEqual(resultado.temas_repaso, [])
        self.assertEqual(ResultadoPregunta.objects.filter(resultado=resultado).count(), 2)
        self.assertTrue(
            AuditLog.objects.filter(
                evento="evaluacion_resultado_registrado", usuario=self.usuario
            ).exists()
        )

    def test_evaluar_quiz_no_aprobado_bajo_umbral(self):
        resultado = evaluar_quiz(
            self.usuario,
            self.quiz,
            {str(self.p1.id): 1, str(self.p2.id): "otra"},
        )

        self.assertEqual(resultado.puntuacion, 0)
        self.assertFalse(resultado.aprobado)
        self.assertFalse(resultado.requiere_revision)
        self.assertGreaterEqual(len(resultado.temas_repaso), 1)

    def test_umbral_aprobacion_aplicado(self):
        self.quiz.umbral_aprobacion = 80
        self.quiz.save(update_fields=["umbral_aprobacion"])

        resultado = evaluar_quiz(
            self.usuario,
            self.quiz,
            {str(self.p1.id): 0, str(self.p2.id): "incorrecta"},
        )

        self.assertEqual(resultado.puntuacion, 50)
        self.assertFalse(resultado.aprobado)
        self.assertEqual(resultado.umbral_aprobacion, 80)

    def test_preguntas_abiertas_requieren_revision_y_no_autoaprueban(self):
        quiz_abierto = Quiz.objects.create(
            nombre="Quiz abierto",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            umbral_aprobacion=70,
            version=2,
        )
        Pregunta.objects.create(
            quiz=quiz_abierto,
            orden=1,
            formato=Pregunta.FORMATO_INTERPRETACION,
            enunciado="Interpreta el código",
            datos_respuesta={"criterios": ["Identifica el flujo"]},
        )
        Pregunta.objects.create(
            quiz=quiz_abierto,
            orden=2,
            formato=Pregunta.FORMATO_RESOLUCION,
            enunciado="Resuelve el problema",
            datos_respuesta={"criterios": ["Propone solución"]},
        )

        resultado = evaluar_quiz(
            self.usuario,
            quiz_abierto,
            {"1": "explicación", "2": "solución"},
        )

        self.assertTrue(resultado.requiere_revision)
        self.assertFalse(resultado.aprobado)
        self.assertEqual(resultado.puntuacion, 0)
        preguntas = ResultadoPregunta.objects.filter(resultado=resultado)
        self.assertEqual(preguntas.count(), 2)
        self.assertTrue(all(p.requiere_revision for p in preguntas))

    def test_reintento_crea_nueva_evidencia(self):
        r1 = evaluar_quiz(self.usuario, self.quiz, {str(self.p1.id): 1, str(self.p2.id): "x"})
        r2 = evaluar_quiz(self.usuario, self.quiz, {str(self.p1.id): 0, str(self.p2.id): "variable"})

        self.assertNotEqual(r1.id, r2.id)
        self.assertFalse(r1.aprobado)
        self.assertTrue(r2.aprobado)
        self.assertEqual(ResultadoEvaluacion.objects.filter(quiz=self.quiz, usuario=self.usuario).count(), 2)


class QuizViewsTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-quiz-view", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO quiz views", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=1, titulo="Etapa 1")
        modulo = Modulo.objects.create(etapa=etapa, numero="1.1", titulo="Módulo 1")
        self.quiz = Quiz.objects.create(
            nombre="Quiz publicado",
            tipo=Quiz.TIPO_QUIZ,
            modulo=modulo,
            umbral_aprobacion=70,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        self.p1 = Pregunta.objects.create(
            quiz=self.quiz,
            orden=1,
            formato=Pregunta.FORMATO_SELECCION,
            enunciado="Selecciona",
            datos_respuesta={
                "opciones": [
                    {"texto": "Correcta", "correcta": True},
                    {"texto": "Incorrecta", "correcta": False},
                ]
            },
        )
        self.p2 = Pregunta.objects.create(
            quiz=self.quiz,
            orden=2,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Responde",
            datos_respuesta={"respuesta_esperada": "ok"},
        )

    def test_detalle_quiz_publicado_accesible_sin_exponer_respuestas(self):
        url = f"/roadmaps/quiz/{self.quiz.id}/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Quiz publicado")
        self.assertContains(resp, "Correcta")
        self.assertNotContains(resp, '"correcta"')
        self.assertNotContains(resp, "respuesta_esperada")

    def test_envio_quiz_crea_resultado_y_redirige(self):
        url = f"/roadmaps/quiz/{self.quiz.id}/"
        resp = self.client.post(
            url,
            {
                f"respuesta_{self.p1.id}": "0",
                f"respuesta_{self.p2.id}": "ok",
            },
        )
        self.assertEqual(resp.status_code, 302)
        resultado = ResultadoEvaluacion.objects.get(quiz=self.quiz, usuario=self.usuario)
        self.assertTrue(resultado.aprobado)
        self.assertIn(f"/roadmaps/quiz/{self.quiz.id}/resultado/{resultado.id}/", resp["Location"])

    def test_resultado_y_historial_del_usuario(self):
        resultado = evaluar_quiz(
            self.usuario, self.quiz, {str(self.p1.id): 0, str(self.p2.id): "ok"}
        )
        resp_res = self.client.get(f"/roadmaps/quiz/{self.quiz.id}/resultado/{resultado.id}/")
        self.assertEqual(resp_res.status_code, 200)
        self.assertContains(resp_res, "Aprobado")

        resp_hist = self.client.get(f"/roadmaps/quiz/{self.quiz.id}/historial/")
        self.assertEqual(resp_hist.status_code, 200)
        self.assertContains(resp_hist, "Historial")
        self.assertContains(resp_hist, str(resultado.id))

    def test_quiz_borrador_no_accesible(self):
        borrador = Quiz.objects.create(
            nombre="Borrador",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.quiz.modulo,
            estado=Quiz.ESTADO_BORRADOR,
            version=2,
        )
        resp = self.client.get(f"/roadmaps/quiz/{borrador.id}/")
        self.assertEqual(resp.status_code, 404)

class ProgresionPorEvaluacionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-progreso-eval", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO progreso eval", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=1, titulo="Etapa 1")
        self.modulo = Modulo.objects.create(etapa=etapa, numero="1.1", titulo="Módulo 1")
        self.quiz = Quiz.objects.create(
            nombre="Quiz módulo",
            tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo,
            umbral_aprobacion=70,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        self.p1 = Pregunta.objects.create(
            quiz=self.quiz,
            orden=1,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Pregunta",
            datos_respuesta={"respuesta_esperada": "ok"},
        )

    def test_quiz_aprobado_marca_progreso_modulo_completado(self):
        from apps.roadmaps.models import Progreso

        resultado = evaluar_quiz(self.usuario, self.quiz, {str(self.p1.id): "ok"})
        self.assertTrue(resultado.aprobado)

        progreso = Progreso.objects.get(
            usuario=self.usuario, etapa=self.modulo.etapa, modulo=self.modulo, leccion__isnull=True
        )
        self.assertEqual(progreso.estado, "completado")
        self.assertEqual(progreso.porcentaje, 100)
        self.assertTrue(
            AuditLog.objects.filter(
                evento="progreso_modulo_completado_por_evaluacion", usuario=self.usuario
            ).exists()
        )

class ExamenEtapaHomologacionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-examen-etapa", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO examen etapa", edicion="test")
        self.etapa = Etapa.objects.create(roadmap=self.roadmap, numero=1, titulo="Etapa 1")
        self.examen = Quiz.objects.create(
            nombre="Examen etapa 1",
            tipo=Quiz.TIPO_EXAMEN,
            etapa=self.etapa,
            umbral_aprobacion=70,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        self.p1 = Pregunta.objects.create(
            quiz=self.examen,
            orden=1,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Pregunta",
            datos_respuesta={"respuesta_esperada": "ok"},
        )

    def test_examen_aprobado_homologa_etapa_y_audita(self):
        from apps.roadmaps.models import Progreso

        resultado = evaluar_quiz(self.usuario, self.examen, {str(self.p1.id): "ok"})
        self.assertTrue(resultado.aprobado)
        self.assertFalse(resultado.requiere_revision)

        progreso = Progreso.objects.get(
            usuario=self.usuario, etapa=self.etapa, modulo__isnull=True, leccion__isnull=True
        )
        self.assertEqual(progreso.estado, "completado")
        self.assertEqual(progreso.porcentaje, 100)
        self.assertTrue(
            AuditLog.objects.filter(
                evento="etapa_completada_por_criterios", usuario=self.usuario
            ).exists()
        )

    def test_examen_no_aprobado_no_homologa_etapa(self):
        from apps.roadmaps.models import Progreso

        resultado = evaluar_quiz(self.usuario, self.examen, {str(self.p1.id): "mal"})
        self.assertFalse(resultado.aprobado)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, etapa=self.etapa, modulo__isnull=True, leccion__isnull=True, estado="completado"
            ).exists()
        )

    def test_examen_con_revision_pendiente_no_homologa_etapa(self):
        from apps.roadmaps.models import Progreso

        examen = Quiz.objects.create(
            nombre="Examen revisión",
            tipo=Quiz.TIPO_EXAMEN,
            etapa=self.etapa,
            version=2,
            umbral_aprobacion=70,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        p = Pregunta.objects.create(
            quiz=examen,
            orden=1,
            formato=Pregunta.FORMATO_RESOLUCION,
            enunciado="Explica",
            datos_respuesta={"criterios": ["explicacion"]},
        )
        resultado = evaluar_quiz(self.usuario, examen, {str(p.id): "respuesta libre"})
        self.assertTrue(resultado.requiere_revision)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, etapa=self.etapa, modulo__isnull=True, leccion__isnull=True, estado="completado"
            ).exists()
        )

    def test_examen_bloqueado_por_prerrequisitos_no_homologa_etapa(self):
        from apps.roadmaps.models import Progreso
        from apps.roadmaps.models import Prerrequisito

        etapa2 = Etapa.objects.create(roadmap=self.roadmap, numero=2, titulo="Etapa 2")
        Prerrequisito.objects.create(etapa=etapa2, etapa_requerida=self.etapa)
        examen2 = Quiz.objects.create(
            nombre="Examen etapa 2",
            tipo=Quiz.TIPO_EXAMEN,
            etapa=etapa2,
            umbral_aprobacion=70,
            estado=Quiz.ESTADO_PUBLICADO,
        )
        p2 = Pregunta.objects.create(
            quiz=examen2,
            orden=1,
            formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Pregunta",
            datos_respuesta={"respuesta_esperada": "ok"},
        )
        with self.assertRaisesMessage(ValidationError, "prerrequisitos"):
            evaluar_quiz(self.usuario, examen2, {str(p2.id): "ok"})
        self.assertFalse(
            ResultadoEvaluacion.objects.filter(
                quiz=examen2, usuario=self.usuario
            ).exists()
        )
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario, etapa=etapa2, modulo__isnull=True, leccion__isnull=True, estado="completado"
            ).exists()
        )

    def test_examen_aprobado_con_criterio_proyecto_obligatorio_no_completa_etapa(self):
        from apps.roadmaps.models import CriterioFinalizacion, Progreso

        CriterioFinalizacion.objects.create(
            etapa=self.etapa,
            titulo="Proyecto de la etapa",
            tipo="proyecto",
            obligatorio=True,
            orden=1,
        )
        resultado = evaluar_quiz(self.usuario, self.examen, {str(self.p1.id): "ok"})
        self.assertTrue(resultado.aprobado)

        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario,
                etapa=self.etapa,
                modulo__isnull=True,
                leccion__isnull=True,
                estado="completado",
            ).exists()
        )
        self.assertTrue(
            AuditLog.objects.filter(
                evento="etapa_homologacion_pendiente_criterios", usuario=self.usuario
            ).exists()
        )

    def test_cumplimiento_criterio_proyecto_permite_completar_etapa_tras_examen(self):
        from apps.roadmaps.models import CriterioFinalizacion, Progreso
        from apps.roadmaps.services_evaluacion import registrar_cumplimiento_criterio

        criterio = CriterioFinalizacion.objects.create(
            etapa=self.etapa,
            titulo="Proyecto de la etapa",
            tipo="proyecto",
            obligatorio=True,
            orden=1,
        )
        resultado = evaluar_quiz(self.usuario, self.examen, {str(self.p1.id): "ok"})
        self.assertTrue(resultado.aprobado)
        self.assertFalse(
            Progreso.objects.filter(
                usuario=self.usuario,
                etapa=self.etapa,
                modulo__isnull=True,
                leccion__isnull=True,
                estado="completado",
            ).exists()
        )

        registrar_cumplimiento_criterio(
            self.usuario, criterio, evidencia="Proyecto entregado y verificado", origen="proyecto"
        )
        progreso = Progreso.objects.get(
            usuario=self.usuario, etapa=self.etapa, modulo__isnull=True, leccion__isnull=True
        )
        self.assertEqual(progreso.estado, "completado")
        self.assertTrue(
            AuditLog.objects.filter(
                evento="criterio_finalizacion_cumplido", usuario=self.usuario
            ).exists()
        )

from django.test import TestCase
from django.core.management import call_command

from apps.roadmaps.models import Etapa, Modulo, Roadmap
from apps.roadmaps.models_evaluacion import Pregunta, Quiz
from apps.roadmaps.services_carga_evaluaciones import cargar_quizzes


class CargaQuizzesTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO", edicion="3.1", activo=True)
        etapa = Etapa.objects.create(roadmap=self.roadmap, numero=0, titulo="Etapa 0")
        Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Aprender a aprender", orden=1)

    def test_carga_quizzes_ejemplo(self):
        resumen = cargar_quizzes("apps/roadmaps/data/quizzes_ejemplo.json", roadmap=self.roadmap)
        self.assertEqual(resumen["quizzes"], 1)
        self.assertEqual(resumen["preguntas"], 2)
        quiz = Quiz.objects.get(nombre__startswith="Ejemplo")
        self.assertEqual(quiz.estado, Quiz.ESTADO_BORRADOR)
        self.assertEqual(quiz.modulo.numero, "0.1")
        self.assertEqual(quiz.preguntas.count(), 2)
        p1 = quiz.preguntas.get(orden=1)
        self.assertIn("_meta_trazabilidad", p1.datos_respuesta)
        self.assertIn("objetivo", p1.datos_respuesta["_meta_trazabilidad"])

    def test_command_cargar_quizzes(self):
        call_command("cargar_quizzes", ruta="apps/roadmaps/data/quizzes_ejemplo.json")
        self.assertEqual(Quiz.objects.count(), 1)



class QuizBlockedSubmissionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-quiz-bloqueado", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO quiz bloqueado", edicion="test")
        self.prerrequisito = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Prerrequisito"
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=1, titulo="Etapa bloqueada"
        )
        Prerrequisito.objects.create(
            etapa=self.etapa, etapa_requerida=self.prerrequisito,
            justificacion="Debe completarse antes.",
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero="1.1", titulo="Módulo bloqueado"
        )
        self.quiz = Quiz.objects.create(
            nombre="Quiz bloqueado", tipo=Quiz.TIPO_QUIZ,
            modulo=self.modulo, umbral_aprobacion=70,
        )
        self.pregunta = Pregunta.objects.create(
            quiz=self.quiz, orden=1, formato=Pregunta.FORMATO_RESPUESTA,
            enunciado="Escribe la respuesta",
            datos_respuesta={"respuesta_esperada": "variable"},
        )

    def test_quiz_de_etapa_bloqueada_no_acepta_respuestas(self):
        with self.assertRaisesMessage(ValidationError, "prerrequisitos"):
            evaluar_quiz(
                self.usuario, self.quiz, {str(self.pregunta.id): "variable"}
            )
        self.assertFalse(
            ResultadoEvaluacion.objects.filter(
                quiz=self.quiz, usuario=self.usuario
            ).exists()
        )




class BlockedStageCriterionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="estudiante-criterio-bloqueado", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(
            nombre="ASCENSO criterio bloqueado", edicion="test"
        )
        prerequisito = Etapa.objects.create(
            roadmap=roadmap, numero=0, titulo="Prerrequisito"
        )
        self.etapa = Etapa.objects.create(
            roadmap=roadmap, numero=1, titulo="Etapa bloqueada"
        )
        Prerrequisito.objects.create(
            etapa=self.etapa, etapa_requerida=prerequisito,
            justificacion="Debe completarse antes.",
        )
        self.criterio = CriterioFinalizacion.objects.create(
            etapa=self.etapa, titulo="Proyecto de etapa",
            descripcion="Presentar evidencia.", tipo="proyecto",
            obligatorio=True, orden=1,
        )
        # Etapa sin prerrequisitos para validar el resto de reglas de entrada
        # sin que el bloqueo de prerrequisitos enmascare el error esperado.
        self.etapa_libre = Etapa.objects.create(
            roadmap=roadmap, numero=2, titulo="Etapa libre"
        )
        self.criterio_libre = CriterioFinalizacion.objects.create(
            etapa=self.etapa_libre, titulo="Proyecto libre",
            descripcion="Presentar evidencia.", tipo="proyecto",
            obligatorio=True, orden=1,
        )

    def test_criterio_de_etapa_bloqueada_no_acepta_evidencia(self):
        with self.assertRaisesMessage(ValidationError, "prerrequisitos"):
            registrar_cumplimiento_criterio(
                self.usuario, self.criterio,
                evidencia="Evidencia anticipada.", origen="proyecto",
            )
        self.assertFalse(
            CumplimientoCriterio.objects.filter(
                usuario=self.usuario, criterio=self.criterio
            ).exists()
        )


    def test_criterio_no_se_marca_sin_evidencia(self):
        with self.assertRaisesMessage(ValidationError, "Describe la evidencia"):
            registrar_cumplimiento_criterio(
                self.usuario, self.criterio_libre, evidencia="  ", origen="proyecto"
            )
        self.assertFalse(
            CumplimientoCriterio.objects.filter(
                usuario=self.usuario, criterio=self.criterio_libre
            ).exists()
        )


    def test_criterio_rechaza_evidencia_mayor_a_5000_caracteres(self):
        with self.assertRaisesMessage(ValidationError, "5.000 caracteres"):
            registrar_cumplimiento_criterio(
                self.usuario, self.criterio_libre, evidencia="x" * 5001,
                origen="proyecto",
            )
        self.assertFalse(
            CumplimientoCriterio.objects.filter(
                usuario=self.usuario, criterio=self.criterio_libre
            ).exists()
        )

    def test_criterio_rechaza_origen_no_permitido(self):
        with self.assertRaisesMessage(ValidationError, "origen"):
            registrar_cumplimiento_criterio(
                self.usuario, self.criterio_libre, evidencia="Evidencia válida.",
                origen="admin_inventado",
            )
        self.assertFalse(
            CumplimientoCriterio.objects.filter(
                usuario=self.usuario, criterio=self.criterio_libre
            ).exists()
        )
