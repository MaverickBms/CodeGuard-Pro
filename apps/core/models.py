"""Modelo de configuración global del sistema (singleton lógico)."""

from django.db import models


class ConfiguracionSistema(models.Model):
    """Configuración global de CodeGuard Pro. Solo debe existir una fila."""

    configuracion_inicial_completada = models.BooleanField(
        default=False, verbose_name="configuración inicial completada"
    )
    fecha_ultimo_backup = models.DateTimeField(
        null=True, blank=True, verbose_name="fecha del último backup"
    )
    version_bd = models.CharField(
        max_length=16, default="1.0", verbose_name="versión del esquema de datos"
    )

    class Meta:
        verbose_name = "configuración del sistema"
        verbose_name_plural = "configuración del sistema"

    def save(self, *args, **kwargs):
        # Forzar singleton: siempre una sola fila (pk=1).
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Evitar borrado accidental de la única fila de configuración.
        pass

    @classmethod
    def cargar(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self) -> str:
        return "Configuración del sistema"
