"""Pruebas del exportador curricular de solo lectura."""
import json
import tempfile
from pathlib import Path
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from apps.roadmaps.models import (
    ContenidoLeccion,
    EjemploLeccion,
    EjercicioLeccion,
    Etapa,
    FuenteConocimiento,
    Leccion,
    Modulo,
    Roadmap,
)


class ExportarManifiestoAcademicoTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(
            nombre="PROYECTO ASCENSO — Roadmap Maestro Consolidado",
            edicion="3.1",
            activo=True,
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Preparación", objetivo="Aprender."
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa, numero="0.1", titulo="Método", orden=1
        )
        self.leccion = Leccion.objects.create(
            modulo=self.modulo, titulo="Aprendizaje activo", orden=1
        )
        self.ejemplo = EjemploLeccion.objects.create(
            leccion=self.leccion, titulo="Ejemplo", codigo="print('hola')"
        )
        self.ejercicio = EjercicioLeccion.objects.create(
            leccion=self.leccion, titulo="Práctica", enunciado="Imprime un saludo."
        )
        ContenidoLeccion.objects.create(
            leccion=self.leccion,
            objetivos_aprendizaje="Comprender el aprendizaje activo.",
            teoria_tecnica="Fundamentos.",
            explicacion_sencilla="Aprender haciendo.",
        )
        self.fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Tutorial",
            url_canonica="https://docs.python.org/3/tutorial/",
            edicion="3",
        )

    def test_exporta_uuid_y_estado_sin_modificar_datos(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "manifest.json"
            stdout = StringIO()
            before = (
                Roadmap.objects.count(),
                Leccion.objects.count(),
                EjemploLeccion.objects.count(),
                EjercicioLeccion.objects.count(),
                FuenteConocimiento.objects.count(),
            )
            call_command(
                "exportar_manifiesto_academico",
                nombre=self.roadmap.nombre,
                edicion=self.roadmap.edicion,
                salida=str(output),
                incluir_fuentes=True,
                stdout=stdout,
            )
            payload = json.loads(output.read_text(encoding="utf-8"))
            lesson = payload["etapas"][0]["modulos"][0]["lecciones"][0]
            self.assertEqual(lesson["uuid"], str(self.leccion.clave_contenido))
            self.assertEqual(lesson["ejemplos"][0]["uuid"], str(self.ejemplo.clave_contenido))
            self.assertEqual(lesson["ejercicios"][0]["uuid"], str(self.ejercicio.clave_contenido))
            self.assertTrue(lesson["contenido_legacy"]["tiene_cuerpo"])
            self.assertEqual(payload["fuentes"][0]["uuid"], str(self.fuente.clave))
            self.assertEqual(payload["resumen"]["lecciones_con_cuerpo_legacy"], 1)
            self.assertEqual(
                before,
                (
                    Roadmap.objects.count(),
                    Leccion.objects.count(),
                    EjemploLeccion.objects.count(),
                    EjercicioLeccion.objects.count(),
                    FuenteConocimiento.objects.count(),
                ),
            )

    def test_no_sobrescribe_un_archivo_existente(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "manifest.json"
            output.write_text("conservar", encoding="utf-8")
            with self.assertRaises(Exception):
                call_command(
                    "exportar_manifiesto_academico",
                    nombre=self.roadmap.nombre,
                    edicion=self.roadmap.edicion,
                    salida=str(output),
                )
            self.assertEqual(output.read_text(encoding="utf-8"), "conservar")
