"""Pruebas del contrato JSON, importación y revisión de licencias."""

import json
import tempfile
from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.roadmaps.content_import import (
    importar_documentos_validados,
    validar_directorio_contenido,
)
from apps.roadmaps.knowledge import (
    aprobar_version_contenido,
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

    def write_document(self, name="variables.json"):
        (self.directory / name).write_text(
            json.dumps(self.document, ensure_ascii=False), encoding="utf-8"
        )

    def approve_license(self, state="compatible", use="original", alcance=None, evidencia=None):
        self.document["fuentes"][0]["uso_declarado"] = use
        self.write_document()
        if alcance is None:
            alcance = "Permite redistribución con atribución." if state == "compatible" else "Consulta técnica para elaborar contenido original."
        if evidencia is None:
            evidencia = "https://docs.python.org/3/license.html"
        return revisar_licencia_fuente(
            self.fuente.pk,
            actor=self.editor,
            estado=state,
            evidencia=evidencia,
            alcance=alcance,
            nota="Revisión manual documentada.",
        )

    def test_validacion_no_escribe_en_base_de_datos(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        self.assertEqual(report["documents"], 1)
        self.assertEqual(report["valid"], 1)
        self.assertFalse(report["errors"])
        self.assertEqual(VersionContenidoLeccion.objects.count(), 0)
        self.assertFalse(report["warnings"])

    def test_importacion_crea_solo_borrador_y_referencias(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        result = importar_documentos_validados(report, actor=self.editor)
        version = result["created"][0]
        self.assertEqual(version.estado, "borrador")
        self.assertEqual(version.creada_por, self.editor)
        self.assertEqual(version.snapshot["leccion"]["clave"], str(self.leccion.clave_contenido))
        self.assertEqual(version.referencias.count(), 1)
        self.assertEqual(version.referencias.get().uso_declarado, "original")
        self.assertFalse(result["duplicates"])
        otro_editor = get_user_model().objects.create_user(
            username="editor_otro", password="ClaveSegura123!", is_staff=True
        )
        version.creada_por = otro_editor
        with self.assertRaisesMessage(ValidationError, "no puede modificarse"):
            version.save()

    def test_reimportacion_del_mismo_hash_es_idempotente(self):
        self.approve_license()
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

    def test_fuente_pendiente_bloquea_validacion(self):
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(report["errors"])
        self.assertTrue(any("pendiente" in e for e in report["errors"]))
        self.assertEqual(VersionContenidoLeccion.objects.count(), 0)

    def test_revision_compatible_habilita_revision_editorial(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        version = importar_documentos_validados(report, actor=self.editor)["created"][0]
        version = enviar_version_a_revision(version.pk, actor=self.editor)
        self.assertEqual(version.estado, "revision")
        referencia = version.referencias.get()
        self.assertEqual(referencia.estado_licencia_snapshot, "compatible")
        self.assertEqual(referencia.evidencia_licencia_snapshot, "https://docs.python.org/3/license.html")
        self.assertEqual(referencia.licencia_revisada_por_snapshot, self.editor)
        self.fuente.refresh_from_db()
        self.assertEqual(self.fuente.revisada_por, self.editor)

    def test_solo_referencia_no_permite_adaptacion(self):
        self.approve_license(state="solo_referencia", use="adaptacion")
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(report["errors"])
        self.assertTrue(any("solo referencia" in e.lower() or "original" in e.lower() for e in report["errors"]))

    def test_cambio_posterior_de_licencia_bloquea_aprobacion_y_snapshot_es_inmutable(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        version = importar_documentos_validados(report, actor=self.editor)["created"][0]
        enviar_version_a_revision(version.pk, actor=self.editor)
        referencia = version.referencias.get()
        referencia.uso_declarado = "adaptacion"
        with self.assertRaisesMessage(ValidationError, "procedencia de una versión en revisión es inmutable"):
            referencia.save()

        revisar_licencia_fuente(
            self.fuente.pk,
            actor=self.editor,
            estado="solo_referencia",
            evidencia="https://docs.python.org/3/license.html",
            alcance="Consulta para contenido original.",
            nota="Se actualizó la interpretación de los términos.",
        )
        with self.assertRaisesMessage(ValidationError, "cambió después del envío a revisión"):
            aprobar_version_contenido(version.pk, actor=self.editor)

    def test_evidencia_http_no_puede_aprobar_licencia(self):
        with self.assertRaisesMessage(ValidationError, "URL HTTPS absoluta"):
            revisar_licencia_fuente(
                self.fuente.pk,
                actor=self.editor,
                estado="compatible",
                evidencia="http://example.org/license",
                alcance="Redistribución.",
                nota="Prueba de rechazo de HTTP.",
            )

    def test_usuario_sin_privilegios_no_puede_importar(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        with self.assertRaisesMessage(ValidationError, "editor activo"):
            importar_documentos_validados(report, actor=get_user_model().objects.create_user(
                username="no_editor", password="ClaveSegura123!"
            ))

    def test_licencia_requiere_permiso_bloquea_validacion(self):
        self.approve_license(state="requiere_permiso")
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(any("requiere_permiso" in e for e in report["errors"]))

    def test_licencia_no_reutilizable_bloquea_validacion(self):
        self.approve_license(state="no_reutilizable")
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(any("no_reutilizable" in e for e in report["errors"]))

    def test_compatible_sin_alcance_bloquea_validacion(self):
        revisar_licencia_fuente(
            self.fuente.pk, actor=self.editor, estado="compatible",
            evidencia="https://docs.python.org/3/license.html",
            alcance="Alcance temporal.", nota="ok"
        )
        # Simular ausencia de alcance en BD sin pasar por servicio: no permitido por servicio,
        # así que probamos a través del servicio directamente.
        with self.assertRaisesMessage(ValidationError, "alcance"):
            revisar_licencia_fuente(
                self.fuente.pk, actor=self.editor, estado="compatible",
                evidencia="https://docs.python.org/3/license.html",
                alcance="", nota="sin alcance"
            )

    def test_solo_referencia_sin_alcance_bloquea_revision_licencia(self):
        with self.assertRaisesMessage(ValidationError, "alcance de consulta"):
            revisar_licencia_fuente(
                self.fuente.pk, actor=self.editor, estado="solo_referencia",
                evidencia="https://docs.python.org/3/license.html",
                alcance="", nota="sin alcance"
            )

    def test_fuente_inactiva_rechazada(self):
        self.approve_license()
        self.fuente.activa = False
        self.fuente.save(update_fields=["activa"])
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(any("inactiva" in e.lower() for e in report["errors"]))

    def test_fuente_inexistente_rechazada(self):
        self.approve_license()
        self.document["fuentes"][0]["clave"] = "00000000-0000-0000-0000-000000000099"
        self.write_document()
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(any("no están registradas" in e or "registrada" in e.lower() for e in report["errors"]))

    def test_fuente_sin_evidencia_o_auditoria_rechazada(self):
        # Fuente con estado compatible pero sin auditoría: forzar estado directamente en BD no es posible por servicio;
        # creamos fuente y la dejamos sin revisar.
        fuente2 = FuenteConocimiento.objects.create(
            publicador="W3C", titulo="HTML Spec",
            url_canonica="https://html.spec.whatwg.org/", edicion="living",
            estado_revision_licencia="compatible", activa=True,
        )
        self.document["fuentes"][0]["clave"] = str(fuente2.clave)
        self.write_document()
        report = validar_directorio_contenido(self.directory)
        self.assertTrue(any("auditoría" in e.lower() or "evidencia" in e.lower() for e in report["errors"]))

    def test_cambio_posterior_a_validacion_bloquea_importacion(self):
        self.approve_license()
        report = validar_directorio_contenido(self.directory)
        self.assertFalse(report["errors"])
        # Cambiar licencia después de validar pero antes de importar
        revisar_licencia_fuente(
            self.fuente.pk, actor=self.editor, estado="no_reutilizable",
            evidencia="https://docs.python.org/3/license.html",
            alcance="", nota="Cambio posterior."
        )
        with self.assertRaises(ValidationError):
            importar_documentos_validados(report, actor=self.editor)
        self.assertEqual(VersionContenidoLeccion.objects.count(), 0)

    def test_solo_referencia_con_alcance_y_uso_original_pasa(self):
        self.approve_license(state="solo_referencia", use="original")
        report = validar_directorio_contenido(self.directory)
        self.assertFalse(report["errors"])
        self.assertEqual(report["valid"], 1)
