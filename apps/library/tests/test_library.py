"""Pruebas de importación, búsqueda y servicio de PDFs de la biblioteca."""

import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.audit.models import AuditLog
from apps.library.models import DocumentoBiblioteca

PDF_MINIMO = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF\n"


class BibliotecaBaseTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.media_temporal = tempfile.mkdtemp(prefix="cg-media-")
        cls.override = override_settings(MEDIA_ROOT=cls.media_temporal, AUTH_DISABLED=True)
        cls.override.enable()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.override.disable()
        shutil.rmtree(cls.media_temporal, ignore_errors=True)

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(username="biblioteca")

    def _subir(self, nombre="manual.pdf", contenido=PDF_MINIMO, titulo="Manual de prueba"):
        return self.client.post(
            reverse("library:importar"),
            {
                "titulo": titulo,
                "autor": "Autora de prueba",
                "categoria": "manual",
                "descripcion": "Documento de prueba local.",
                "etiquetas": "pruebas, local",
                "archivo": SimpleUploadedFile(nombre, contenido, content_type="application/pdf"),
            },
        )


class ImportacionBibliotecaTests(BibliotecaBaseTests):
    def test_importa_pdf_valido_y_registra_metadatos(self):
        respuesta = self._subir()

        self.assertEqual(respuesta.status_code, 302)
        documento = DocumentoBiblioteca.objects.get()
        self.assertEqual(documento.titulo, "Manual de prueba")
        self.assertEqual(documento.autor, "Autora de prueba")
        self.assertEqual(documento.categoria, "manual")
        self.assertEqual(documento.tamano_bytes, len(PDF_MINIMO))
        self.assertEqual(len(documento.sha256), 64)
        self.assertEqual(documento.estado, "activo")
        self.assertEqual(documento.subido_por, self.usuario)
        self.assertTrue(documento.archivo_existe())
        self.assertTrue(AuditLog.objects.filter(evento="documento_biblioteca_importado").exists())

    def test_rechaza_archivo_que_no_es_pdf(self):
        respuesta = self._subir(nombre="notas.txt", contenido=b"texto plano")

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "extensión .pdf")
        self.assertFalse(DocumentoBiblioteca.objects.exists())

    def test_rechaza_pdf_con_firma_incorrecta(self):
        respuesta = self._subir(nombre="falso.pdf", contenido=b"no es un pdf")

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "firma %PDF-")
        self.assertFalse(DocumentoBiblioteca.objects.exists())

    def test_rechaza_pdf_demasiado_grande(self):
        with patch("apps.library.forms.MAX_PDF_BYTES", 10):
            respuesta = self._subir(contenido=PDF_MINIMO)

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "supera el límite")
        self.assertFalse(DocumentoBiblioteca.objects.exists())

    def test_rechaza_duplicados_por_sha256(self):
        self._subir()
        respuesta = self._subir(titulo="Copia duplicada")

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "mismo contenido")
        self.assertEqual(DocumentoBiblioteca.objects.count(), 1)

    def test_rechaza_titulo_vacio(self):
        respuesta = self._subir(titulo="   ")
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "necesita un título")
        self.assertFalse(DocumentoBiblioteca.objects.exists())


class ConsultaBibliotecaTests(BibliotecaBaseTests):
    def setUp(self):
        super().setUp()
        self._subir(titulo="Redes y protocolos", contenido=PDF_MINIMO + b"redes")
        self._subir(titulo="Bases de datos", contenido=PDF_MINIMO + b"sql")
        self.documento = DocumentoBiblioteca.objects.get(titulo="Redes y protocolos")

    def test_lista_muestra_documentos_y_metadatos(self):
        respuesta = self.client.get(reverse("library:lista"))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Redes y protocolos")
        self.assertContains(respuesta, "Bases de datos")
        self.assertContains(respuesta, "2 documentos")

    def test_busqueda_por_titulo_y_etiquetas(self):
        respuesta = self.client.get(reverse("library:lista"), {"q": "protocolos"})
        self.assertEqual([d.titulo for d in respuesta.context["documentos"]], ["Redes y protocolos"])

        DocumentoBiblioteca.objects.filter(titulo="Bases de datos").update(
            etiquetas="sql, consultas"
        )
        respuesta = self.client.get(reverse("library:lista"), {"q": "consultas"})
        self.assertEqual([d.titulo for d in respuesta.context["documentos"]], ["Bases de datos"])

    def test_filtro_por_categoria(self):
        DocumentoBiblioteca.objects.filter(titulo="Bases de datos").update(categoria="libro")
        respuesta = self.client.get(reverse("library:lista"), {"categoria": "libro"})
        self.assertEqual([d.titulo for d in respuesta.context["documentos"]], ["Bases de datos"])

    def test_detalle_muestra_visor_y_metadatos(self):
        respuesta = self.client.get(reverse("library:detalle", args=[self.documento.pk]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Visor")
        self.assertContains(respuesta, self.documento.sha256)
        self.assertContains(respuesta, "application/pdf")

    def test_archivar_y_restaurar(self):
        respuesta = self.client.post(
            reverse("library:cambiar_estado", args=[self.documento.pk]),
            {"accion": "archivar"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.documento.refresh_from_db()
        self.assertEqual(self.documento.estado, "archivado")
        activos = self.client.get(reverse("library:lista"))
        self.assertEqual([d.titulo for d in activos.context["documentos"]], ["Bases de datos"])
        archivados = self.client.get(reverse("library:lista"), {"estado": "archivado"})
        self.assertEqual([d.titulo for d in archivados.context["documentos"]], ["Redes y protocolos"])

        self.client.post(
            reverse("library:cambiar_estado", args=[self.documento.pk]),
            {"accion": "restaurar"},
        )
        self.documento.refresh_from_db()
        self.assertEqual(self.documento.estado, "activo")

    def test_accion_desconocida_no_cambia_estado(self):
        respuesta = self.client.post(
            reverse("library:cambiar_estado", args=[self.documento.pk]),
            {"accion": "borrar_todo"},
        )
        self.documento.refresh_from_db()
        self.assertEqual(self.documento.estado, "activo")
        self.assertEqual(respuesta.status_code, 302)


class ServicioArchivoTests(BibliotecaBaseTests):
    def setUp(self):
        super().setUp()
        self._subir()
        self.documento = DocumentoBiblioteca.objects.get()
        self.url = reverse("library:archivo", args=[self.documento.pk])

    def test_sirve_pdf_completo(self):
        respuesta = self.client.get(self.url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta["Content-Type"], "application/pdf")
        self.assertEqual(respuesta["Accept-Ranges"], "bytes")
        self.assertEqual(respuesta["X-Content-Type-Options"], "nosniff")
        self.assertEqual(respuesta["X-Frame-Options"], "SAMEORIGIN")
        self.assertIn("frame-ancestors 'self'", respuesta["Content-Security-Policy"])
        self.assertEqual(b"".join(respuesta.streaming_content), PDF_MINIMO)

    def test_sirve_rango_parcial(self):
        respuesta = self.client.get(self.url, HTTP_RANGE="bytes=0-3")

        self.assertEqual(respuesta.status_code, 206)
        self.assertEqual(respuesta["Content-Range"], f"bytes 0-3/{len(PDF_MINIMO)}")
        self.assertEqual(b"".join(respuesta.streaming_content), b"%PDF")

    def test_rango_invalido_devuelve_416(self):
        respuesta = self.client.get(self.url, HTTP_RANGE="bytes=99999-")
        self.assertEqual(respuesta.status_code, 416)
        self.assertEqual(respuesta["Content-Range"], f"bytes */{len(PDF_MINIMO)}")

    def test_archivo_ausente_devuelve_404(self):
        Path(self.documento.archivo.path).unlink()
        respuesta = self.client.get(self.url)
        self.assertEqual(respuesta.status_code, 404)

    def test_pagina_normal_conserva_frame_denegado(self):
        respuesta = self.client.get(reverse("library:lista"))
        self.assertEqual(respuesta["X-Frame-Options"], "DENY")
        self.assertIn("frame-ancestors 'none'", respuesta["Content-Security-Policy"])


class IntegridadConcurrenteBibliotecaTests(BibliotecaBaseTests):
    def test_base_de_datos_impide_hashes_duplicados_incluso_si_se_omite_la_vista(self):
        self._subir(titulo="Original")
        original = DocumentoBiblioteca.objects.get()
        from django.db import IntegrityError

        with self.assertRaises(IntegrityError):
            DocumentoBiblioteca.objects.create(
                titulo="Duplicado concurrente",
                archivo=original.archivo.name,
                nombre_original="duplicado.pdf",
                sha256=original.sha256,
                tamano_bytes=original.tamano_bytes,
            )

        self.assertEqual(
            DocumentoBiblioteca.objects.filter(sha256=original.sha256).count(), 1
        )

    def test_documentos_legacy_sin_hash_no_colisionan(self):
        DocumentoBiblioteca.objects.create(titulo="Sin hash A", sha256="")
        DocumentoBiblioteca.objects.create(titulo="Sin hash B", sha256="")
        self.assertEqual(DocumentoBiblioteca.objects.filter(sha256="").count(), 2)
