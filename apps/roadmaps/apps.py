"""App configuration for the roadmaps module (gestión académica ASCENSO)."""

from django.apps import AppConfig


class RoadmapsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.roadmaps"
    verbose_name = "Roadmaps — Gestión académica"
