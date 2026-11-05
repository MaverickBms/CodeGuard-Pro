"""Modelos del módulo de auditoría.

Registra eventos de seguridad y acceso del usuario: inicios de sesión, cierres,
fallos de autenticación y cambios de estado de sesión.
"""

from django.conf import settings
from django.db import models


class AuditLog(models.Model):
    """Entrada única de auditoría."""

    EVENTO_CHOICES = [
        ("login_exitoso", "Inicio de sesión exitoso"),
        ("login_fallido", "Inicio de sesión fallido"),
        ("logout", "Cierre de sesión"),
        ("logout_inactividad", "Cierre de sesión por inactividad"),
        ("setup_inicial", "Configuración inicial completada"),
        ("cambio_contraseña", "Cambio de contraseña"),
        ("uso_frase_rescate", "Uso de frase de rescate"),
        ("acceso_denegado", "Acceso denegado a vista protegida"),
        ("backup_creado", "Backup creado"),
        ("backup_restaurado", "Backup restaurado"),
        ("error_importacion", "Error de importación de documento"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="eventos_auditoria",
        verbose_name="usuario",
    )
    evento = models.CharField(max_length=40, choices=EVENTO_CHOICES, verbose_name="evento")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP")
    user_agent = models.CharField(max_length=512, blank=True, verbose_name="user agent")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")

    class Meta:
        verbose_name = "registro de auditoría"
        verbose_name_plural = "registros de auditoría"
        ordering = ["-creado_en"]
        indexes = [
            models.Index(fields=["evento", "creado_en"]),
            models.Index(fields=["usuario", "creado_en"]),
        ]

    def __str__(self) -> str:
        return f"{self.creado_en} — {self.get_evento_display()} — {self.usuario}"
