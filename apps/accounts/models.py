"""Modelos del módulo de identidad y acceso.

Se extiende el modelo de usuario de Django con información específica de la
configuración inicial y la frase de rescate de alta entropía.
"""

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuario único del sistema CodeGuard Pro (monousuario local).

    La contraseña se hashea con Argon2 gracias a la configuración de
    AUTH_PASSWORD_HASHERS.
    """

    email_verificado = models.BooleanField(default=False, verbose_name="email verificado")
    fecha_configuracion_inicial = models.DateTimeField(
        null=True, blank=True, verbose_name="fecha de configuración inicial"
    )
    sesion_timeout_minutos = models.PositiveIntegerField(
        default=15, verbose_name="tiempo de sesión por inactividad (minutos)"
    )

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        swappable = "AUTH_USER_MODEL"

    def __str__(self) -> str:
        return self.username


class FraseRescate(models.Model):
    """Frase de rescate de alta entropía, mostrada una sola vez y almacenada como hash.

    Nunca se almacena en texto plano. Tras usarse una vez se marca como usada e
    invalida.
    """

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="frases_rescate",
        verbose_name="usuario",
    )
    hash_argon2 = models.TextField(verbose_name="hash Argon2 de la frase de rescate")
    usada = models.BooleanField(default=False, verbose_name="usada")
    fecha_uso = models.DateTimeField(null=True, blank=True, verbose_name="fecha de uso")
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="creada en")

    class Meta:
        verbose_name = "frase de rescate"
        verbose_name_plural = "frases de rescate"
        ordering = ["-creada_en"]

    def __str__(self) -> str:
        return f"Frase rescate {self.usuario} — usada={self.usada}"
