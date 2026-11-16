"""Pruebas del endpoint de salud que consume el proceso Electron."""

from django.test import TestCase
from django.urls import reverse

from apps.roadmaps.models import Roadmap


class HealthEndpointTests(TestCase):
    def test_returns_ready_only_when_database_migrations_and_roadmap_exist(self):
        Roadmap.objects.create(
            nombre="ASCENSO de prueba",
            edicion="test",
            activo=True,
        )

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
        self.assertEqual(response.json()["status"], "starting")
