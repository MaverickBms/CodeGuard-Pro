"""App configuration for the audit module (registro de eventos de seguridad)."""

from django.apps import AppConfig


class AuditConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.audit"
    verbose_name = "Audit — Auditoría de eventos"
