"""Pruebas del contrato JSON, importación y revisión de licencias."""

import json
import tempfile
import uuid
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.roadmaps.content_import import (
    importar_documentos_validados,
    validar_directorio_contenido,
)
from apps.roadmaps.knowledge import (
    enviar_version_a_revision,
    revisar_licencia_fuente,
)
from apps.roadmaps.models import (
    EjemploLeccion,
    EjercicioLeccion,
    Etapa,
    FuenteConocimiento,
    Leccion,
    Modulo,
    Roadmap,
    VersionContenidoLeccion,
)


class ImportacionContenidoTests(TestCase):
    def setUp(self):
        self.editor = get_user_model().objects.create_user(
            username="editor_import", password="ClaveSegura123!", is_staff=True, is_active=True
        )
        self.roadmap = Roadmap.objects.create(nombre="ASCENSO import", edicion="test")
        self.etapa = Etapa.objects.create(roadmap=self.roadmap, numero=0, titulo="Fundamentos")
        self.modulo = Modulo.objects.create(etapa=self.etapa, numero="0.1", titulo="Inicio")
        self.leccion = Leccion.objects.create(
            modulo=self.modulo, titulo="Variables", descripcion="Introducción", tipo="concepto"
        )
        self.ejemplo = EjemploLeccion.objects.create(
            leccion=self.leccion, titulo="Asignación", codigo="nombre = 'Ada'"
        )
        self.ejercicio = EjercicioLeccion.objects.create(
            leccion=self.leccion, titulo="Declara una variable",
            enunciado="Declara nombre.", lenguaje="Python", nivel="basico"
        )
        self.fuente = FuenteConocimiento.objects.create(
            publicador="Python Software Foundation",
            titulo="Python Language Reference",
            url_canonica="https://docs.python.org/3/reference/",
            edicion="3",
        )
        self.document = {
            "schema_version": 1,
            "resumen_cambios": "Primera versión editorial.",
            "snapshot": {
                "esquema_version": 1,
                "leccion": {
                    "clave": str(self.leccion.clave_contenido),
                    "titulo": self.leccion.titulo,
                    "descripcion": self.leccion.descripcion,
                    "tipo": self.leccion.tipo,
                },
                "contenido": {
                    "objetivos_aprendizaje": "Comprender variables.",
                    "teoria_tecnica": "Una variable enlaza un nombre con un objeto.",
                    "explicacion_sencilla": "Un nombre permite referirse a un valor.",
                    "notas": "",
                },
                "ejemplos": [{
                    "clave": str(self.ejemplo.clave_contenido),
                    "titulo": "Asignación",
                    "contexto": "Crear una variable.",
                    "lenguaje": "Python",
                    "codigo": "nombre = 'Ada'",
                    "salida_esperada": "",
                    "explicacion": "Asigna un valor.",
                    "orden": 1,
                }],
                "ejercicios": [{
                    "clave": str(self.ejercicio.clave_contenido),
                    "titulo": "Declara una variable",
                    "enunciado": "Declara nombre.",
                    "instrucciones": "Usa una asignación.",
                    "lenguaje": "Python",
                    "nivel": "basico",
                    "codigo_inicial": "",
                    "obligatorio": True,
                    "orden": 1,
                }],
            },
            "fuentes": [{
                "clave": str(self.fuente.clave),
                "rol": "principal",
                "localizador": "Assignment statements",
                "nota_atribucion": "Referencia conceptual.",
                "uso_declarado": "original",
            }],
        }
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.write_document()

    def write_document(self):
        (self.directory / "variables.json").write_text(
            json.dumps(self.document, ensure_ascii=False), encoding="utf-8"
        )

    def approve_license(self, state="compatible", use="original"):
        self.document["fuentes"][0]["uso_declarado"] = use
        self.write_document()
        return revisar_licencia_fuente(
            self.fuente.pk,
            actor=self.editor,
            estado=state,
            evidencia="https://docs.python.org/3/license.html",
            alcance="Permite redistribución con atribución." if state == "compatible" else "",
            nota="Revisión manual documentada.",
        )

    def test_validacion_no_escribe_en_base_de_datos(self):
        report = validar_directorio_contenido(self.directory)
        self.assertEqual(report["documents"], 1)
        self.assertEqual(report["valid"], 1)
        self.assertFalse(report["errors"])
        self.assertEqual(VersionContenidoLeccion.objects.count(), 0)
        self.assertTrue(report["warnings"])

    def test_importacion_crea_solo_borrador_y_referencias(self):
        report = validar_directorio_contenido(self.directory)
        result = importar_documentos_validados(report, actor=self.editor)
        version = result["created"][0]
        self.assertEqual(version.estado, "borrador")
        self.assertEqual(version.snapshot["leccion"]["clave"], str(self.leccion.clave_contenido))
        self.assertEqual(version.referencias.count(), 1)
        self.assertEqual(version.referencias.get().uso_declarado, "original")
        self.assertFalse(result["duplicates"])

    def test_reimportacion_del_mismo_hash_es_idempotente(self):
        report = validar_directorio_contenido(self.directory)
        first = importar_documentos_validados(report, actor=self.editor)
        second_report = validar_directorio_contenido(self.directory)
        second = importar_documentos_validados(second_report, actor=self.editor)
        self.assertEqual(len(first["created"]), 1)
        self.assertEqual(len(second["created"]), 0)
        self.assertEqual(len(second["duplicates"]), 1)
        self.assertEqual(VersionContenidoLeccion.objects.count(), 1)

    def test_campo_desconocido_rechaza_lote_sin_escritura(self):
        self.document["snapshot"]["contenido"]["campo_inventado"] = "no permitido"
        self.write_document()
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(report["errors"])
        self.assertEqual(report["items"], [])
        self.assertEqual(VersionContenidoLeccion.objects.count(), 0)

    def test_uuid_de_ejemplo_de_otra_leccion_se_rechaza(self):
        otra = Leccion.objects.create(modulo=self.modulo, titulo="Otra lección")
        ejemplo = EjemploLeccion.objects.create(leccion=otra, titulo="Ajeno")
        self.document["snapshot"]["ejemplos"][0]["clave"] = str(ejemplo.clave_contenido)
        self.write_document()
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(report["errors"])

    def test_fuente_pendiente_bloquea_envio_a_revision(self):
        report = validar_directorio_contenido(self.directory)
        version = importar_documentos_validados(report, actor=self.editor)["created"][0]
        with self.assertRaisesMessage(ValidationError, "estado de licencia 'pendiente'"):
            enviar_version_a_revision(version.pk, actor=self.editor)

    def test_revision_compatible_habilita_revision_editorial(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        version = importar_documentos_validados(report, actor=self.editor)["created"][0]
        version = enviar_version_a_revision(version.pk, actor=self.editor)
        self.assertEqual(version.estado, "revision")
        self.assertEqual(self.fuente.revisada_por, self.editor)

    def test_solo_referencia_no_permite_adaptacion(self):
        self.approve_license(state="solo_referencia", use="adaptacion")
        report = validar_directorio_contenido(self.directory)
        version = importar_documentos_validados(report, actor=self.editor)["created"][0]
        with self.assertRaisesMessage(ValidationError, "solo permite contenido original"):
            enviar_version_a_revision(version.pk, actor=self.editor)

    def test_usuario_sin_privilegios_no_puede_importar(self):
        report = validar_directorio_contenido(self.directory)
        with self.assertRaisesMessage(ValidationError, "editor activo"):
            importar_documentos_validados(report, actor=get_user_model().objects.create_user(
                username="no_editor", password="ClaveSegura123!"
            ))
