"""Pruebas del Mundo CodeGuard: vista, guardado y misiones."""
import json

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.gamification.models import EstadoMundo, ItemInventario
from apps.roadmaps.models import Etapa, Roadmap


class MundoCodeGuardTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="mundo-tester", password="ClaveSegura123!"
        )
        self.roadmap = Roadmap.objects.create(
            nombre="ASCENSO mundo", edicion="3.1", activo=True
        )
        Etapa.objects.create(
            roadmap=self.roadmap, numero=0, titulo="Preparación y método"
        )

    def _post(self, name, payload):
        return self.client.post(
            reverse(name),
            data=json.dumps(payload),
            content_type="application/json",
        )

    def test_vista_renderiza_canvas_y_configuracion(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self.client.get(reverse("gamification:mundo"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'id="mundoCanvas"')
        self.assertContains(respuesta, "aldea-metodo")
        self.assertContains(respuesta, "Misiones")

    def test_guardar_posicion_valida_y_persiste(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self._post(
                "gamification:guardar_mundo",
                {
                    "region": "aldea-metodo",
                    "x": 16,
                    "y": 12,
                    "direccion": "left",
                    "tiempo_jugado": 12,
                    "audio_silenciado": True,
                },
            )
        self.assertEqual(respuesta.status_code, 200)
        estado = EstadoMundo.objects.get(usuario=self.usuario)
        self.assertEqual((estado.x, estado.y, estado.direccion), (16, 12, "left"))
        self.assertTrue(estado.audio_silenciado)

    def test_guardar_posicion_fuera_del_mapa_falla(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self._post(
                "gamification:guardar_mundo",
                {"region": "aldea-metodo", "x": 999, "y": 12, "direccion": "down"},
            )
        self.assertEqual(respuesta.status_code, 400)
        self.assertIn("fuera del mapa", respuesta.json()["error"])

    def test_mision_principal_requiere_interacciones_y_es_idempotente(self):
        with override_settings(AUTH_DISABLED=True):
            temprano = self._post("gamification:completar_mision_mundo", {"mision": "metodo-principal"})
            self.assertEqual(temprano.status_code, 400)

            self.assertEqual(
                self._post("gamification:interactuar_mundo", {"objeto": "ada"}).status_code,
                200,
            )
            self.assertEqual(
                self._post(
                    "gamification:interactuar_mundo", {"objeto": "terminal"}
                ).status_code,
                200,
            )
            completada = self._post(
                "gamification:completar_mision_mundo", {"mision": "metodo-principal"}
            )
            self.assertEqual(completada.status_code, 200)
            self.assertTrue(completada.json()["creada"])
            self.assertEqual(ItemInventario.objects.filter(usuario=self.usuario).count(), 1)

            repetida = self._post(
                "gamification:completar_mision_mundo", {"mision": "metodo-principal"}
            )
            self.assertEqual(repetida.status_code, 200)
            self.assertFalse(repetida.json()["creada"])
            self.assertEqual(ItemInventario.objects.filter(usuario=self.usuario).count(), 1)

    def test_minijuego_valida_respuestas_en_servidor(self):
        with override_settings(AUTH_DISABLED=True):
            self._post("gamification:interactuar_mundo", {"objeto": "guardian"})
            incorrectas = self._post(
                "gamification:completar_mision_mundo",
                {"mision": "desafio-depuracion", "respuestas": {"q1": 0, "q2": 0, "q3": 0}},
            )
            self.assertEqual(incorrectas.status_code, 400)
            correctas = self._post(
                "gamification:completar_mision_mundo",
                {"mision": "desafio-depuracion", "respuestas": {"q1": 1, "q2": 2, "q3": 0}},
            )
        self.assertEqual(correctas.status_code, 200)
        self.assertTrue(correctas.json()["creada"])

    def test_region_biblioteca_persiste_y_minijuego_logico(self):
        with override_settings(AUTH_DISABLED=True):
            guardado = self._post(
                "gamification:guardar_mundo",
                {
                    "region": "biblioteca-aldear",
                    "x": 15,
                    "y": 17,
                    "direccion": "up",
                    "tiempo_jugado": 20,
                },
            )
            self.assertEqual(guardado.status_code, 200)
            self._post("gamification:interactuar_mundo", {"objeto": "nexo"})
            incorrectas = self._post(
                "gamification:completar_mision_mundo",
                {"mision": "logica-principal", "respuestas": {"q1": 0, "q2": 0, "q3": 0}},
            )
            self.assertEqual(incorrectas.status_code, 400)
            correctas = self._post(
                "gamification:completar_mision_mundo",
                {"mision": "logica-principal", "respuestas": {"q1": 1, "q2": 0, "q3": 2}},
            )
        self.assertEqual(correctas.status_code, 200)
        self.assertEqual(
            EstadoMundo.objects.get(usuario=self.usuario).region, "biblioteca-aldear"
        )

    def test_no_permite_interactuar_con_objetos_de_otra_region(self):
        with override_settings(AUTH_DISABLED=True):
            respuesta = self._post("gamification:interactuar_mundo", {"objeto": "byte"})
        self.assertEqual(respuesta.status_code, 400)
        self.assertIn("región", respuesta.json()["error"])

    def test_sin_propietario_local_no_permite_guardar(self):
        self.usuario.delete()
        with override_settings(AUTH_DISABLED=True):
            respuesta = self._post(
                "gamification:guardar_mundo",
                {"region": "aldea-metodo", "x": 15, "y": 12, "direccion": "down"},
            )
        self.assertEqual(respuesta.status_code, 403)
