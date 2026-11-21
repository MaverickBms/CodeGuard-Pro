"""Pruebas del endpoint de salud que consume el proceso Electron."""

from django.test import TestCase
from django.urls import reverse

from apps.roadmaps.models import Etapa, Leccion, Modulo, Roadmap


class HealthEndpointTests(TestCase):
    def _roadmap_operativo(self):
        roadmap = Roadmap.objects.create(
            nombre="ASCENSO de prueba",
            edicion="test",
            activo=True,
        )
        etapa = Etapa.objects.create(
            roadmap=roadmap, numero=0, titulo="Etapa 0", orden=0
        )
        modulo = Modulo.objects.create(
            etapa=etapa, numero="0.1", titulo="Módulo 0.1", orden=1
        )
        Leccion.objects.create(
            modulo=modulo, titulo="Lección 0.1.1", orden=1, tipo="concepto"
        )
        return roadmap

    def test_returns_ready_only_when_database_migrations_and_roadmap_exist(self):
        self._roadmap_operativo()

        response = self.client.get(reverse("healthz"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "ok",
                "database": "ok",
                "migrations": "ok",
                "roadmap": "ok",
            },
        )

    def test_returns_service_unavailable_without_active_roadmap(self):
        response = self.client.get(reverse("healthz"))

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["roadmap"], "missing")
        self.assertEqual(response.json()["status"], "starting")

    def test_returns_service_unavailable_with_empty_roadmap(self):
        Roadmap.objects.create(
            nombre="ASCENSO vacío",
            edicion="test",
            activo=True,
        )

        response = self.client.get(reverse("healthz"))

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json()["roadmap"], "incomplete")
        self.assertEqual(response.json()["status"], "starting")
