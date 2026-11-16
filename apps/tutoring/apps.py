"""Configuración de la aplicación de tutoría inteligente local."""

from django.apps import AppConfig


class TutoringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tutoring"
    verbose_name = "Tutoría inteligente local"

    def ready(self):
        import apps.tutoring.signals  # noqa: F401