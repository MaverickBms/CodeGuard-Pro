"""Pruebas del contenido académico ampliado, videos y flujo editorial."""

from pathlib import Path

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from apps.accounts.bootstrap import asegurar_propietario_local
from apps.roadmaps.coverage import calcular_cobertura
from apps.roadmaps.knowledge import (
    aprobar_version_contenido,
    crear_version_contenido_leccion,
    enviar_version_a_revision,
    publicar_version_contenido,
)
from apps.roadmaps.models import (
    ContenidoLeccion,
    ContenidoLeccionActivo,
    EjemploLeccion,
    EjercicioLeccion,
    FuenteConocimiento,
    Leccion,
    RecursoAudiovisual,
    VersionContenidoLeccion,
)
from apps.roadmaps.services import cargar_ascenso, obtener_contenido_activo, roadmap_activo
from apps.roadmaps.management.commands.cargar_contenido_academico import (
    ContenidoAcademicoError,
    _propietario_editorial,
)
from apps.roadmaps.templatetags.academic import academico

RUTA_SEED = Path(__file__).resolve().parents[1] / "data" / "contenido_academico_0_1.json"


@override_settings(AUTH_DISABLED=True)
class CargaContenidoAcademicoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.roadmap = cargar_ascenso()
        asegurar_propietario_local()
        call_command("cargar_contenido_academico", ruta=str(RUTA_SEED), verbosity=0)
        cls.leccion = Leccion.objects.get(titulo="Aprendizaje activo.")

    def test_carga_ocho_lecciones_completas_sin_publicar(self):
        self.assertEqual(ContenidoLeccion.objects.count(), 8)
        self.assertEqual(VersionContenidoLeccion.objects.count(), 8)
        self.assertEqual(RecursoAudiovisual.objects.count(), 8)
        self.assertEqual(EjemploLeccion.objects.count(), 8)
        self.assertEqual(EjercicioLeccion.objects.count(), 16)
        self.assertEqual(ContenidoLeccionActivo.objects.count(), 0)
        self.assertFalse(ContenidoLeccion.objects.filter(publicado=True).exists())
        for contenido in ContenidoLeccion.objects.all():
            self.assertTrue(contenido.calidad_academica_completa)
        for version in VersionContenidoLeccion.objects.all():
            self.assertEqual(version.esquema_version, 2)
            self.assertEqual(version.estado, "borrador")

    def test_carga_es_idempotente(self):
        salida = call_command(
            "cargar_contenido_academico", ruta=str(RUTA_SEED), verbosity=0
        )
        self.assertEqual(VersionContenidoLeccion.objects.count(), 8)
        self.assertEqual(EjemploLeccion.objects.count(), 8)
        self.assertEqual(EjercicioLeccion.objects.count(), 16)

    def test_videos_estan_aprobados_y_relacionados(self):
        for video in RecursoAudiovisual.objects.select_related("leccion"):
            self.assertEqual(video.estado_revision, "aprobado")
            self.assertTrue(video.disponible)
            self.assertEqual(video.idioma, "es")
            self.assertIsNotNone(video.verificado_en)
            self.assertEqual(video.video_id, RecursoAudiovisual.extraer_video_id(video.url))

    def test_leccion_borrador_se_puede_estudiar_con_aviso(self):
        respuesta = self.client.get(
            reverse("roadmaps:leccion_detalle", args=[self.leccion.id])
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Contenido en borrador")
        self.assertContains(respuesta, "Conocimientos previos")
        self.assertContains(respuesta, "Explicación teórica")
        self.assertContains(respuesta, "Videos recomendados")
        self.assertContains(respuesta, "Fuentes y lectura complementaria")
        self.assertContains(respuesta, "Sprouts Español")

    def test_contenido_activo_marca_borrador_y_video(self):
        resultado = obtener_contenido_activo(self.leccion, permitir_borrador=True)
        self.assertEqual(resultado["origen"], "borrador")
        self.assertTrue(resultado["es_borrador"])
        self.assertEqual(resultado["estado_editorial"], "borrador")
        self.assertEqual(len(resultado["videos"]), 1)
        self.assertTrue(resultado["contenido"].conceptos_fundamentales)

    def test_publicar_una_version_valida_la_activa(self):
        version = VersionContenidoLeccion.objects.get(leccion=self.leccion)
        actor = get_user_model().objects.get(is_staff=True)
        enviar_version_a_revision(version.id, actor=actor)
        aprobar_version_contenido(version.id, actor=actor)
        publicar_version_contenido(version.id, actor=actor)

        version.refresh_from_db()
        self.assertEqual(version.estado, "publicada")
        self.assertTrue(ContenidoLeccionActivo.objects.filter(leccion=self.leccion).exists())
        resultado = obtener_contenido_activo(self.leccion)
        self.assertEqual(resultado["origen"], "editorial")
        self.assertFalse(resultado["es_borrador"])
        self.assertEqual(resultado["estado_editorial"], "publicada")
        cobertura = calcular_cobertura(roadmap_activo())
        self.assertEqual(cobertura.publicada, 1)
        self.assertEqual(cobertura.borrador, 7)

    def test_cobertura_distingue_estados(self):
        cobertura = calcular_cobertura(roadmap_activo())
        self.assertEqual(cobertura.total, 1946)
        self.assertEqual(cobertura.desarrolladas, 8)
        self.assertEqual(cobertura.borrador, 8)
        self.assertEqual(cobertura.publicada, 0)
        self.assertEqual(cobertura.pendiente, 1938)
        self.assertEqual(cobertura.con_video, 8)


class FiltroAcademicoTests(TestCase):
    def test_escapa_html_y_convierte_estructura(self):
        html = academico("- **Uno:** texto\n- **Dos:** más\n\n<script>alert(1)</script>")
        self.assertIn("<ul><li><strong>Uno:</strong> texto</li>", html)
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)


@override_settings(AUTH_DISABLED=False)
class ModoConAutenticacionTests(TestCase):
    def test_no_eleva_a_staff_ni_siembra_automaticamente(self):
        usuario = get_user_model().objects.create_user(
            username="sin-permisos", password="ClaveSegura123!"
        )
        self.assertFalse(usuario.is_staff)
        with self.assertRaises(ContenidoAcademicoError):
            _propietario_editorial()
        usuario.refresh_from_db()
        self.assertFalse(usuario.is_staff)
        from apps.roadmaps.bootstrap import _sembrar_contenido_inicial

        self.assertEqual(_sembrar_contenido_inicial(), 0)
        from apps.roadmaps.models import ContenidoLeccion

        self.assertFalse(ContenidoLeccion.objects.exists())


class RecursoAudiovisualTests(TestCase):
    def setUp(self):
        roadmap = cargar_ascenso()
        self.leccion = Leccion.objects.filter(
            modulo__etapa__roadmap=roadmap
        ).first()

    def _recurso(self, **cambios):
        datos = {
            "leccion": self.leccion,
            "titulo": "Video de prueba",
            "canal": "Canal educativo",
            "url": "https://www.youtube.com/watch?v=oMPQNOD-2fo",
            "idioma": "es",
            "objetivo_aprendizaje": "Comprender el concepto.",
            "estado_revision": "pendiente",
        }
        datos.update(cambios)
        return RecursoAudiovisual(**datos)

    def test_normaliza_url_de_youtube(self):
        recurso = self._recurso()
        recurso.save()
        self.assertEqual(recurso.video_id, "oMPQNOD-2fo")
        self.assertEqual(recurso.url, "https://www.youtube.com/watch?v=oMPQNOD-2fo")

    def test_rechaza_hosts_que_no_son_youtube(self):
        with self.assertRaises(ValidationError):
            self._recurso(url="https://example.com/video").save()

    def test_rechaza_audio_no_espanol(self):
        with self.assertRaises(ValidationError):
            self._recurso(idioma="en").save()

    def test_aprobado_exige_verificacion(self):
        with self.assertRaises(ValidationError):
            self._recurso(estado_revision="aprobado").save()
        recurso = self._recurso(
            estado_revision="aprobado",
            verificado_en=timezone.now(),
        )
        recurso.save()
        self.assertTrue(recurso.publicado)


@override_settings(AUTH_DISABLED=True)
class EditorialViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cargar_ascenso()
        asegurar_propietario_local()
        call_command("cargar_contenido_academico", ruta=str(RUTA_SEED), verbosity=0)
        cls.leccion = Leccion.objects.get(titulo="Aprendizaje activo.")

    def test_editorial_lista_y_filtra(self):
        respuesta = self.client.get(reverse("roadmaps:editorial"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Taller de contenido")
        self.assertContains(respuesta, "Aprendizaje activo.")

        respuesta = self.client.get(reverse("roadmaps:editorial"), {"estado": "borrador"})
        self.assertContains(respuesta, "Aprendizaje activo.")

    def test_editorial_leccion_muestra_formulario_y_videos(self):
        respuesta = self.client.get(
            reverse("roadmaps:editorial_leccion", args=[self.leccion.id])
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Contenido editable")
        self.assertContains(respuesta, "Crear snapshot versionado")
        self.assertContains(respuesta, "Recursos audiovisuales")

    def test_video_se_agrega_en_revision_y_se_aprueba(self):
        url = reverse("roadmaps:editorial_leccion", args=[self.leccion.id])
        respuesta = self.client.post(
            url,
            {
                "accion": "crear_video",
                "titulo": "Video de prueba editorial",
                "canal": "Canal de prueba",
                "url": "https://www.youtube.com/watch?v=inZe9kW5djI",
                "subtitulos": "manual",
                "duracion_segundos": "125",
                "objetivo_aprendizaje": "Probar el flujo de video.",
                "descripcion": "",
                "orden": "9",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        video = RecursoAudiovisual.objects.get(titulo="Video de prueba editorial")
        self.assertEqual(video.estado_revision, "en_revision")
        respuesta = self.client.post(
            url,
            {
                "accion": "revisar_video",
                "video_id": video.id,
                "decision": "aprobado",
                "notas_verificacion": "Título, URL, duración y audio español verificados.",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        video.refresh_from_db()
        self.assertEqual(video.estado_revision, "aprobado")
        self.assertIsNotNone(video.verificado_en)
        self.assertTrue(video.publicado)

    def test_cobertura_y_conocimiento_incluyen_estado(self):
        for nombre in ("roadmaps:cobertura", "roadmaps:conocimiento"):
            respuesta = self.client.get(reverse(nombre))
            self.assertEqual(respuesta.status_code, 200)
            self.assertContains(respuesta, "8")

    def test_fuentes_permite_registrar_y_revisar(self):
        respuesta = self.client.get(reverse("roadmaps:editorial_fuentes"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Registrar una fuente")

        respuesta = self.client.post(
            reverse("roadmaps:editorial_fuentes"),
            {
                "accion": "crear_fuente",
                "publicador": "Organismo de prueba",
                "titulo": "Documento de prueba",
                "url_canonica": "https://example.org/doc",
                "edicion": "1",
                "identificador_licencia": "CC-BY-4.0",
                "url_licencia": "https://example.org/licencia",
                "notas": "Fuente de prueba.",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        fuente = FuenteConocimiento.objects.get(titulo="Documento de prueba")
        self.assertEqual(fuente.estado_revision_licencia, "pendiente")

        respuesta = self.client.post(
            reverse("roadmaps:editorial_fuentes"),
            {
                "accion": "revisar_fuente",
                "fuente_id": fuente.id,
                "estado": "compatible",
                "evidencia": "https://example.org/evidencia",
                "alcance": "Uso referencial con atribución.",
                "nota": "Revisión de prueba con evidencia HTTPS.",
            },
        )
        self.assertEqual(respuesta.status_code, 302)
        fuente.refresh_from_db()
        self.assertEqual(fuente.estado_revision_licencia, "compatible")
        self.assertIsNotNone(fuente.revisada_en)
