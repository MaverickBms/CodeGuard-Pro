import json
import tempfile
from pathlib import Path

from django.core.management import call_command
from django.test import TestCase

from apps.roadmaps.models import (
    EjemploLeccion,
    EjercicioLeccion,
    Etapa,
    Leccion,
    Modulo,
    Roadmap,
)


class ExportarManifiestoAcademicoTests(TestCase):
    def setUp(self):
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO — Roadmap Maestro Consolidado",
            edicion="3.1",
            fuente="roadmap-test.json",
            sha256_fuente="a" * 64,
        )
        self.etapa = Etapa.objects.create(
            roadmap=self.roadmap,
            numero=0,
            titulo="Preparación y método de aprendizaje",
        )
        self.modulo = Modulo.objects.create(
            etapa=self.etapa,
            numero="0.1",
            titulo="Aprender a aprender",
        )
        self.leccion = Leccion.objects.create(
            modulo=self.modulo,
            titulo="Aprendizaje activo.",
            descripcion="Descripción de prueba.",
            tipo="concepto",
        )
        self.ejemplo = EjemploLeccion.objects.create(
            leccion=self.leccion,
            titulo="Ejemplo de prueba",
        )
        self.ejercicio = EjercicioLeccion.objects.create(
            leccion=self.leccion,
            titulo="Ejercicio de prueba",
            enunciado="Resolver un caso sintético.",
        )

    def _arguments(self, **extra):
        return {
            "nombre": self.roadmap.nombre,
            "edicion": self.roadmap.edicion,
            **extra,
        }

    def test_stdout_incluye_uuid_curriculares_y_recursos(self):
        from io import StringIO

        output = StringIO()
        call_command(
            "exportar_manifiesto_academico",
            stdout=output,
            **self._arguments(),
        )
        manifest = json.loads(output.getvalue())
        lesson = manifest["etapas"][0]["modulos"][0]["lecciones"][0]

        self.assertEqual(manifest["schema"], "codeguard-academic-manifest-v1")
        self.assertEqual(lesson["uuid"], str(self.leccion.clave_contenido))
        self.assertEqual(lesson["ejemplos"][0]["uuid"], str(self.ejemplo.clave_contenido))
        self.assertEqual(lesson["ejercicios"][0]["uuid"], str(self.ejercicio.clave_contenido))
        self.assertEqual(manifest["resumen"]["lecciones"], 1)
        self.assertEqual(manifest["resumen"]["ejemplos"], 1)
        self.assertEqual(manifest["resumen"]["ejercicios"], 1)

    def test_salida_no_sobrescribe_archivo_existente(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "manifest.json"
            destination.write_text("preservar", encoding="utf-8")
            from django.core.management.base import CommandError

            with self.assertRaises(CommandError):
                call_command(
                    "exportar_manifiesto_academico",
                    **self._arguments(salida=str(destination)),
                )
            self.assertEqual(destination.read_text(encoding="utf-8"), "preservar")

    def test_roadmap_inexistente_falla_sin_crear_datos(self):
        from django.core.management.base import CommandError

        before = Roadmap.objects.count()
        with self.assertRaises(CommandError):
            call_command(
                "exportar_manifiesto_academico",
                nombre="No existe",
                edicion="0",
            )
        self.assertEqual(Roadmap.objects.count(), before)
