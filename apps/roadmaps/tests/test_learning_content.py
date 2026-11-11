from django.test import TestCase, override_settings
from django.urls import reverse

from .models import (
    ContenidoLeccion,
    EjemploLeccion,
    EjercicioLeccion,
    Etapa,
    Leccion,
    Modulo,
    Roadmap,
)


class ContenidoLeccionModelTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO test", edicion="test")
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Fundamentos"
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero="0.1", titulo="Introducción"
        )
        self.leccion = Leccion.objects.create(
            modulo=self.modulo, titulo="Variables"
        )

    def test_contenido_se_asocia_unicamente_a_una_leccion(self):
        contenido = ContenidoLeccion.objects.create(
            leccion=self.leccion,
            teoria_tecnica="Una variable referencia un valor.",
            explicacion_sencilla="Es un nombre para guardar y reutilizar un dato.",
        )
        self.assertEqual(self.leccion.contenido, contenido)
        self.assertTrue(contenido.esta_completo)

    def test_ejemplos_y_ejercicios_pertenecen_a_la_leccion(self):
        ejemplo = EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Declarar una variable",
            lenguaje="Python",
            codigo="nombre = 'Ada'",
        )
        ejercicio = EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Crea una variable",
            enunciado="Declara una variable llamada ciudad.",
            pista_1="Piensa en el operador de asignación.",
            pista_2="El nombre va a la izquierda del signo igual.",
            pista_3="Asigna un texto entre comillas.",
        )
        self.assertEqual(list(self.leccion.ejemplos.all()), [ejemplo])
        self.assertEqual(list(self.leccion.ejercicios.all()), [ejercicio])
        self.assertEqual(ejercicio.total_pistas_disponibles, 3)


@override_settings(AUTH_DISABLED=True)
class LeccionDetalleViewTests(TestCase):
    def setUp(self):
        roadmap = Roadmap.objects.create(nombre="ASCENSO test", edicion="test")
        etapa = Etapa.objects.create(roadmap=roadmap, numero=0, titulo="Fundamentos")
        modulo = Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Introducción")
        self.leccion = Leccion.objects.create(modulo=modulo, titulo="Variables")
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            teoria_tecnica="Fundamento técnico de una variable.",
            explicacion_sencilla="Una variable permite nombrar un dato.",
            publicado=True,
        )
        EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Primer ejemplo",
            codigo="valor = 10",
            publicado=True,
        )
        EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Practica",
            enunciado="Declara una variable.",
            publicado=True,
        )

    def test_vista_muestra_contenido_ejemplos_y_ejercicios(self):
        response = self.client.get(
            reverse("roadmaps:leccion_detalle", args=[self.leccion.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teoría técnica")
        self.assertContains(response, "Explicación sencilla")
        self.assertContains(response, "Primer ejemplo")
        self.assertContains(response, "Practica")

    def test_leccion_sin_contenido_muestra_estado_en_preparacion(self):
        self.leccion.contenido.delete()
        response = self.client.get(
            reverse("roadmaps:leccion_detalle", args=[self.leccion.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contenido en preparación")
