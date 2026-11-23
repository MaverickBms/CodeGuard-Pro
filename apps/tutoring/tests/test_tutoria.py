"""Pruebas del tutor inteligente local (Fase 3)."""

from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from apps.roadmaps.models import (
    EjercicioLeccion,
    Etapa,
    Leccion,
    Modulo,
    Progreso,
    Roadmap,
    Prerrequisito,
)
from apps.roadmaps.attempts import registrar_intento_ejercicio
from apps.tutoring import services
from apps.tutoring.models import PistaTutoria, SesionTutoria
from apps.tutoring.services import TutorNoDisponible


def _crear_contexto_tutoria():
    """Crea el contexto mínimo de roadmap/lección/ejercicio para las pruebas."""
    usuario = get_user_model().objects.create_user(
        username="estudiante-tutoria", password="ClaveSegura123!"
    )
    roadmap = Roadmap.objects.create(nombre="ASCENSO tutoria", edicion="test")
    etapa = Etapa.objects.create(roadmap=roadmap, numero=0, titulo="Fundamentos")
    modulo = Modulo.objects.create(etapa=etapa, numero="0.1", titulo="Introducción")
    leccion = Leccion.objects.create(modulo=modulo, titulo="Variables")
    ejercicio = EjercicioLeccion.objects.create(
        leccion=leccion,
        titulo="Declara una variable",
        enunciado="Declara una variable llamada nombre.",
        lenguaje="Python",
        publicado=True,
    )
    return usuario, ejercicio


@override_settings(AUTH_DISABLED=True)
class EstadoTutoriaTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch.object(
        services,
        "estado_tutor",
        return_value={
            "disponible": True,
            "ollama": True,
            "modelo": "modelo-prueba",
            "modelo_instalado": True,
            "modo": "ollama",
        },
    )
    def test_estado_devuelve_informacion_del_tutor(self, mock_estado):
        respuesta = self.client.get(reverse("tutoring:estado"))
        self.assertEqual(respuesta.status_code, 200)
        datos = respuesta.json()
        self.assertTrue(datos["disponible"])
        self.assertEqual(datos["modo"], "ollama")
        self.assertEqual(datos["limite_pistas"], services.LIMITE_PISTAS_TUTORIA)
        mock_estado.assert_called_once()

    @patch.object(services, "_listar_modelos", return_value=["otro-modelo:latest"])
    def test_estado_detecta_modelo_no_instalado(self, mock_listar):
        services._estado_cache.update({"checked_at": 0.0, "valor": None})
        estado = services.estado_tutor(forzar=True)
        self.assertFalse(estado["disponible"])
        self.assertTrue(estado["ollama"])
        self.assertFalse(estado["modelo_instalado"])
        self.assertEqual(estado["modo"], "determinista")

    @patch.object(services, "_listar_modelos", side_effect=TutorNoDisponible)
    def test_estado_detecta_ollama_ausente(self, mock_listar):
        services._estado_cache.update({"checked_at": 0.0, "valor": None})
        estado = services.estado_tutor(forzar=True)
        self.assertFalse(estado["disponible"])
        self.assertFalse(estado["ollama"])
        self.assertEqual(estado["modo"], "determinista")


@override_settings(AUTH_DISABLED=True)
class SesionTutoriaViewTests(TestCase):
    def setUp(self):
        self.usuario, self.ejercicio = _crear_contexto_tutoria()

    def test_iniciar_crea_sesion_de_tutoria(self):
        respuesta = self.client.post(reverse("tutoring:iniciar", args=[self.ejercicio.id]))
        self.assertEqual(respuesta.status_code, 200)
        datos = respuesta.json()
        self.assertTrue(datos["exito"])
        self.assertEqual(datos["pistas_disponibles"], 3)
        sesion = SesionTutoria.objects.get(pk=datos["sesion_id"])
        self.assertEqual(sesion.usuario_id, self.usuario.id)
        self.assertEqual(sesion.ejercicio_id, self.ejercicio.id)

    def test_tutor_no_inicia_sesion_ni_da_pistas_en_etapa_bloqueada(self):
        etapa_origen = self.ejercicio.leccion.modulo.etapa
        etapa_bloqueada = Etapa.objects.create(
            roadmap=etapa_origen.roadmap,
            numero=1,
            titulo="Etapa bloqueada",
        )
        Prerrequisito.objects.create(
            etapa=etapa_bloqueada,
            etapa_requerida=etapa_origen,
            justificacion="Completa la etapa anterior.",
        )
        modulo = Modulo.objects.create(
            etapa=etapa_bloqueada, numero="1.1", titulo="Módulo bloqueado"
        )
        leccion = Leccion.objects.create(modulo=modulo, titulo="Lección bloqueada")
        ejercicio = EjercicioLeccion.objects.create(
            leccion=leccion,
            titulo="Ejercicio bloqueado",
            enunciado="No debe recibir tutoría antes de desbloquearse.",
            publicado=True,
        )

        iniciar = self.client.post(reverse("tutoring:iniciar", args=[ejercicio.id]))
        pista = self.client.post(reverse("tutoring:pista", args=[ejercicio.id]))

        self.assertEqual(iniciar.status_code, 403)
        self.assertEqual(pista.status_code, 403)
        self.assertFalse(SesionTutoria.objects.filter(ejercicio=ejercicio).exists())
        self.assertFalse(PistaTutoria.objects.filter(sesion__ejercicio=ejercicio).exists())

    def test_iniciar_con_ejercicio_inexistente(self):
        respuesta = self.client.post(reverse("tutoring:iniciar", args=[99999]))
        self.assertEqual(respuesta.status_code, 404)


@override_settings(AUTH_DISABLED=True)
class PistaTutoriaViewTests(TestCase):
    def setUp(self):
        self.usuario, self.ejercicio = _crear_contexto_tutoria()

    @patch.object(services, "_llamar_ollama", return_value="Pista generada por el tutor.")
    def test_entrega_pista_acepta_tipo_valido(self, mock_llamar):
        respuesta = self.client.post(
            reverse("tutoring:pista", args=[self.ejercicio.id]),
            {"tipo": "orientacion"},
        )
        self.assertEqual(respuesta.status_code, 200)
        datos = respuesta.json()
        self.assertTrue(datos["exito"])
        self.assertEqual(datos["numero"], 1)
        self.assertEqual(datos["restantes"], 2)
        self.assertEqual(PistaTutoria.objects.count(), 1)
        sesion = SesionTutoria.objects.get(usuario=self.usuario, ejercicio=self.ejercicio)
        self.assertEqual(sesion.pistas_utilizadas, 1)
        self.assertEqual(PistaTutoria.objects.get().numero_pista, sesion.pistas_utilizadas)

    def test_entrega_pista_rechaza_tipo_invalido(self):
        respuesta = self.client.post(
            reverse("tutoring:pista", args=[self.ejercicio.id]),
            {"tipo": "solucion"},
        )
        self.assertEqual(respuesta.status_code, 400)
        self.assertFalse(respuesta.json()["exito"])

    @patch.object(services, "_llamar_ollama", return_value="   ")
    def test_entrega_pista_vacia_cae_a_reglas_estaticas(self, mock_llamar):
        self.ejercicio.pista_1 = "Revisa primero el concepto central."
        self.ejercicio.save(update_fields=["pista_1", "actualizado_en"])

        respuesta = self.client.post(
            reverse("tutoring:pista", args=[self.ejercicio.id]),
            {"tipo": "orientacion"},
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.json()["exito"])
        self.assertEqual(
            PistaTutoria.objects.get().contenido,
            "Revisa primero el concepto central.",
        )

    @patch.object(services, "_llamar_ollama", side_effect=TutorNoDisponible)
    def test_entrega_pista_cae_a_reglas_estaticas_sin_ollama(self, mock_llamar):
        self.ejercicio.pista_1 = "Primero identifica el concepto que se evalúa."
        self.ejercicio.save(update_fields=["pista_1", "actualizado_en"])

        respuesta = self.client.post(
            reverse("tutoring:pista", args=[self.ejercicio.id]),
            {"tipo": "orientacion"},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.json()["exito"])
        pista = PistaTutoria.objects.get()
        self.assertEqual(pista.contenido, "Primero identifica el concepto que se evalúa.")


@override_settings(AUTH_DISABLED=True)
class LimitePistasTutoriaTests(TestCase):
    def setUp(self):
        self.usuario, self.ejercicio = _crear_contexto_tutoria()

    def test_limite_de_tres_pistas_por_ejercicio(self):
        from apps.tutoring.services import entregar_pista, obtener_sesion

        sesion = obtener_sesion(self.usuario, self.ejercicio)
        sesion.pistas_utilizadas = 3
        sesion.save(update_fields=["pistas_utilizadas", "ultima_pista_en", "actualizada_en"])

        resultado = entregar_pista(self.usuario, self.ejercicio, tipo_pista="orientacion")
        self.assertFalse(resultado["exito"])
        self.assertEqual(resultado["restantes"], 0)
        self.assertEqual(PistaTutoria.objects.count(), 0)


@override_settings(AUTH_DISABLED=True)
class AnalisisIntentoTutoriaTests(TestCase):
    def setUp(self):
        self.usuario, self.ejercicio = _crear_contexto_tutoria()

    def test_analizar_intento_registra_analisis_del_tutor(self):
        intento = registrar_intento_ejercicio(self.usuario, self.ejercicio, "nombre = 'Ada'")

        with patch.object(services, "_llamar_ollama", return_value="El tutor explica el error."):
            respuesta = self.client.post(
                reverse("tutoring:analizar", args=[self.ejercicio.id]),
                {"intento_ejercicio_id": intento.id},
            )

        self.assertEqual(respuesta.status_code, 200)
        datos = respuesta.json()
        self.assertTrue(datos["exito"])
        self.assertEqual(datos["resultado_evaluacion"], intento.resultado)
        self.assertEqual(datos["analisis_tutor"], "El tutor explica el error.")

    @patch.object(services, "_llamar_ollama", return_value="   ")
    def test_analizar_intento_vacio_usa_retroalimentacion_local(self, mock_llamar):
        intento = registrar_intento_ejercicio(self.usuario, self.ejercicio, "nombre = 'Ada'")

        respuesta = self.client.post(
            reverse("tutoring:analizar", args=[self.ejercicio.id]),
            {"intento_ejercicio_id": intento.id},
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertTrue(respuesta.json()["exito"])
        self.assertTrue(respuesta.json()["analisis_tutor"].strip())
        self.assertIn(
            "validador automático",
            respuesta.json()["analisis_tutor"],
        )

    def test_analizar_sin_intento_devuelve_error(self):
        respuesta = self.client.post(
            reverse("tutoring:analizar", args=[self.ejercicio.id]),
            {},
        )
        self.assertEqual(respuesta.status_code, 400)
        self.assertFalse(respuesta.json()["exito"])


class ConfiguracionOllamaSeguraTests(TestCase):
    """El tutor no debe transmitir respuestas a hosts remotos ni seguir redirects."""

    def test_acepta_solo_hosts_loopback(self):
        for url in (
            "http://localhost:11434",
            "http://127.0.0.1:11434",
            "http://[::1]:11434",
        ):
            with self.subTest(url=url), patch.object(services, "TUTOR_BASE_URL", url):
                self.assertEqual(
                    services._url_ollama_local(),
                    f"{url}/api/chat",
                )

    def test_rechaza_host_remoto_antes_de_abrir_conexion(self):
        with (
            patch.object(services, "TUTOR_BASE_URL", "https://ollama.example"),
            patch("urllib.request.build_opener") as build_opener,
        ):
            with self.assertRaises(TutorNoDisponible):
                services._llamar_ollama("sistema", "respuesta del estudiante")

        build_opener.assert_not_called()

    def test_rechaza_credenciales_y_rutas_en_la_url_base(self):
        for url in (
            "http://usuario:clave@localhost:11434",
            "http://localhost:11434/proxy",
            "http://localhost:11434/?redirect=1",
        ):
            with self.subTest(url=url), patch.object(services, "TUTOR_BASE_URL", url):
                with self.assertRaises(TutorNoDisponible):
                    services._url_ollama_local()

    def test_redirects_no_se_siguen(self):
        handler = services._NoRedirectHandler()
        self.assertIsNone(
            handler.redirect_request(
                None, None, 302, "Found", {}, "https://remote.example/collect"
            )
        )
