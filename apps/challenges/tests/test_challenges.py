from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.challenges.models import Desafio, ResultadoDesafio
from apps.challenges.services import registrar_resultado_desafio
from apps.roadmaps.models import Etapa, Roadmap


class ChallengesBaseTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="jugador-desafio", password="ClaveSegura123!"
        )
        roadmap = Roadmap.objects.create(nombre="ASCENSO desafios", edicion="test")
        self.etapa = Etapa.objects.create(roadmap=roadmap, numero=1, titulo="Etapa 1")

    def test_desafio_requiere_competencia(self):
        desafio = Desafio(nombre="Lógica básica", tipo="minijuego", competencia="")
        with self.assertRaises(ValidationError):
            desafio.full_clean()

    def test_registrar_resultado_desafio_inmutable(self):
        desafio = Desafio.objects.create(
            nombre="Debug rápido",
            tipo="desafio",
            competencia="Depuración",
            etapa=self.etapa,
            dificultad="basica",
        )
        resultado = registrar_resultado_desafio(
            self.usuario,
            desafio,
            puntuacion=80,
            completado=True,
            conceptos_practicados=["breakpoints", "logs"],
            retroalimentacion="Buen trabajo",
        )
        self.assertEqual(ResultadoDesafio.objects.filter(desafio=desafio).count(), 1)
        resultado.puntuacion = 90
        with self.assertRaises(ValidationError):
            resultado.save()

    def test_no_sustituye_examen_formal_por_regla_de_dominio(self):
        # El modelo base no crea aprobaciones de etapa; solo evidencia de desafío.
        desafio = Desafio.objects.create(
            nombre="Jefe de etapa",
            tipo="jefe",
            competencia="Integración",
            etapa=self.etapa,
        )
        resultado = registrar_resultado_desafio(self.usuario, desafio, puntuacion=100, completado=True)
        self.assertTrue(resultado.completado)
        self.assertFalse(hasattr(resultado, "aprobado_academicamente"))
