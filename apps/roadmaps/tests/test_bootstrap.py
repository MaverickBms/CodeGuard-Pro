"""Pruebas del arranque idempotente y la verificación de integridad curricular."""

import io
import json
import tempfile
import time
from pathlib import Path
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from apps.roadmaps.bootstrap import (
    asegurar_roadmap_instalado,
    cargar_manifiesto,
    preparar_perfil_local,
    verificar_instalacion,
)
from apps.roadmaps.models import (
    EstadoInstalacionRoadmap,
    Etapa,
    Leccion,
    Modulo,
    Progreso,
    Roadmap,
)
from apps.roadmaps.services import cargar_ascenso


def manifiesto_minimo(agregar_leccion=False):
    etapas = [
        {
            "numero": 0,
            "titulo": "Etapa 0",
            "bloque": "Fundamentos",
            "prioridad": "P1",
            "objetivo": "Objetivo 0",
            "proyecto": "Proyecto 0",
            "modulos": [
                {
                    "numero": "0.1",
                    "titulo": "Módulo 0.1",
                    "lecciones": ["Lección A", "Lección B"],
                }
            ],
        },
        {
            "numero": 1,
            "titulo": "Etapa 1",
            "prioridad": "P2",
            "prerrequisitos": [
                {"etapa_requerida": 0, "justificacion": "Dependencia de prueba"}
            ],
            "modulos": [
                {"numero": "1.1", "titulo": "Módulo 1.1", "lecciones": ["Lección C"]}
            ],
        },
    ]
    if agregar_leccion:
        etapas[0]["modulos"][0]["lecciones"].append("Lección D")
    return {
        "metadata": {"nombre": "ASCENSO de prueba", "edicion": "test"},
        "etapas": etapas,
    }


class BootstrapRoadmapTests(TestCase):
    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.ruta = Path(self.temporal.name) / "ascenso.json"
        self._escribir(manifiesto_minimo())
        self.roadmap = cargar_ascenso(self.ruta)
        self.usuario = get_user_model().objects.create_user(
            username="propietario", password="clave-de-prueba-123"
        )

    def tearDown(self):
        self.temporal.cleanup()

    def _escribir(self, datos):
        self.ruta.write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")

    def test_registra_metadatos_de_integridad_tras_la_carga(self):
        estado = EstadoInstalacionRoadmap.objects.get(roadmap=self.roadmap)
        manifiesto = cargar_manifiesto(self.ruta)

        self.assertEqual(estado.huella_manifiesto, manifiesto.sha256)
        self.assertEqual(estado.huella_contenido, manifiesto.huella_contenido)
        self.assertEqual(estado.total_etapas, 2)
        self.assertEqual(estado.total_modulos, 2)
        self.assertEqual(estado.total_lecciones, 3)
        self.assertEqual(estado.total_prerrequisitos, 1)

    def test_segundo_arranque_no_reconstruye_el_roadmap(self):
        with patch(
            "apps.roadmaps.services.cargar_ascenso",
            side_effect=AssertionError("no debe recargar"),
        ):
            with self.assertNumQueries(7):
                roadmap, cargado = asegurar_roadmap_instalado(self.ruta)

        self.assertFalse(cargado)
        self.assertEqual(roadmap.pk, self.roadmap.pk)

    def test_detecta_leccion_alterada_y_reconstruye(self):
        leccion = Leccion.objects.get(titulo="Lección A")
        leccion.titulo = "Lección alterada"
        leccion.save(update_fields=["titulo"])
        Progreso.objects.create(
            usuario=self.usuario,
            etapa=self.roadmap.etapas.get(numero=0),
            leccion=leccion,
            estado="completado",
        )

        roadmap, cargado = asegurar_roadmap_instalado(self.ruta)

        self.assertTrue(cargado)
        self.assertTrue(Leccion.objects.filter(titulo="Lección A").exists())
        # El progreso histórico no se elimina; la lección alterada queda como
        # registro sobrante y se contabiliza en los metadatos.
        self.assertTrue(Progreso.objects.filter(usuario=self.usuario).exists())
        estado = EstadoInstalacionRoadmap.objects.get(roadmap=roadmap)
        self.assertEqual(estado.registros_sobrantes, 1)
        self.assertEqual(estado.total_lecciones, 3)

    def test_detecta_manifiesto_nuevo_y_conserva_progreso(self):
        progreso = Progreso.objects.create(
            usuario=self.usuario,
            etapa=self.roadmap.etapas.get(numero=0),
            leccion=Leccion.objects.get(titulo="Lección B"),
            estado="completado",
        )
        self._escribir(manifiesto_minimo(agregar_leccion=True))

        roadmap, cargado = asegurar_roadmap_instalado(self.ruta)

        self.assertTrue(cargado)
        self.assertTrue(Leccion.objects.filter(titulo="Lección D").exists())
        self.assertTrue(Progreso.objects.filter(pk=progreso.pk).exists())
        self.assertEqual(roadmap.pk, self.roadmap.pk)

    def test_filas_sobrantes_no_provocan_reconstrucciones_repetidas(self):
        modulo = Modulo.objects.get(numero="0.1")
        Leccion.objects.create(
            modulo=modulo, titulo="Lección histórica", orden=99, tipo="concepto"
        )

        roadmap, cargado = asegurar_roadmap_instalado(self.ruta)
        self.assertFalse(cargado)
        self.assertEqual(
            EstadoInstalacionRoadmap.objects.get(roadmap=roadmap).registros_sobrantes,
            1,
        )

        with patch(
            "apps.roadmaps.services.cargar_ascenso",
            side_effect=AssertionError("no debe recargar"),
        ):
            _, cargado_de_nuevo = asegurar_roadmap_instalado(self.ruta)
        self.assertFalse(cargado_de_nuevo)

    def test_verificacion_reporta_perfil_incompleto(self):
        Leccion.objects.filter(titulo="Lección C").delete()
        verificación = verificar_instalacion(
            self.roadmap, cargar_manifiesto(self.ruta)
        )

        self.assertFalse(verificación.ok)
        self.assertTrue(verificación.claves_faltantes)
        self.assertIn("perfil local está incompleto", verificación.motivo)

    def test_manifiesto_invalido_no_se_acepta(self):
        self.ruta.write_text('{"etapas": []}', encoding="utf-8")
        with self.assertRaises(ValueError):
            cargar_manifiesto(self.ruta)

    def test_arranque_reutilizado_es_rapido(self):
        with patch(
            "apps.roadmaps.services.cargar_ascenso",
            side_effect=AssertionError("no debe recargar"),
        ):
            inicio = time.monotonic()
            _, cargado = asegurar_roadmap_instalado(self.ruta)
            transcurrido = time.monotonic() - inicio

        self.assertFalse(cargado)
        self.assertLess(
            transcurrido,
            1.0,
            f"La verificación reutilizada tardó {transcurrido:.2f}s; "
            "investiga una regresión de arranque.",
        )

    def test_comando_verificar_perfil_es_solo_lectura(self):
        salida = io.StringIO()
        call_command(
            "verificar_perfil", ruta=str(self.ruta), stdout=salida
        )
        self.assertIn("[OK]", salida.getvalue())
        self.assertIn("2 etapas", salida.getvalue())

        Leccion.objects.filter(titulo="Lección C").delete()
        with self.assertRaises(CommandError):
            call_command("verificar_perfil", ruta=str(self.ruta), stdout=io.StringIO())


class PrepararPerfilTests(TestCase):
    def test_preparar_perfil_emite_eventos_y_verifica(self):
        eventos = []
        resultado = preparar_perfil_local(emit=eventos.append)

        self.assertTrue(resultado["roadmap_cargado"])
        self.assertEqual(resultado["etapas"], 33)
        self.assertEqual(resultado["lecciones"], 1946)
        self.assertTrue(any('"phase":"ready"' in linea for linea in eventos))
        self.assertIsNotNone(resultado["propietario_local_id"])
        self.assertTrue(Roadmap.objects.filter(activo=True).exists())
        self.assertTrue(
            get_user_model().objects.filter(is_active=True).exists()
        )

        eventos.clear()
        segundo = preparar_perfil_local(emit=eventos.append)
        self.assertFalse(segundo["roadmap_cargado"])
        self.assertTrue(segundo["roadmap_reutilizado"])
        self.assertTrue(any('"reused":true' in linea for linea in eventos))

    def test_no_invoca_migrate_cuando_no_hay_migraciones_pendientes(self):
        with patch("django.core.management.call_command") as call_command_mock:
            resultado = preparar_perfil_local(emit=lambda _linea: None)
        self.assertEqual(resultado["migraciones_pendientes"], 0)
        call_command_mock.assert_not_called()
