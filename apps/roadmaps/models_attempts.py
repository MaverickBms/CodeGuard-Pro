"""Modelos de evaluación e intentos de ejercicios.

La configuración permanece separada del enunciado para no exponer criterios
privados en la plantilla del estudiante. Ningún modelo implica ejecución de
código: los evaluadores disponibles son deterministas y estáticos.
"""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ConfiguracionEvaluacion(models.Model):
    """Contrato versionado que define cómo se evalúa un ejercicio."""

    TIPOS = [
        ("respuesta_exacta", "Respuesta de texto exacta"),
        ("codigo_contiene", "Comprobación estática de fragmentos de código"),
    ]

    ejercicio = models.OneToOneField(
        "roadmaps.EjercicioLeccion",
        on_delete=models.CASCADE,
        related_name="configuracion_evaluacion",
        verbose_name="ejercicio",
    )
    tipo = models.CharField(max_length=30, choices=TIPOS, verbose_name="tipo de evaluador")
    configuracion = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="configuración privada del evaluador",
        help_text="No se envía al navegador del estudiante.",
    )
    version = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="versión del evaluador",
    )
    activo = models.BooleanField(default=True, verbose_name="activo")
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "configuración de evaluación"
        verbose_name_plural = "configuraciones de evaluación"

    def __str__(self):
        return f"Evaluador v{self.version}: {self.ejercicio}"


class IntentoEjercicio(models.Model):
    """Entrega inmutable del estudiante y resultado reproducible."""

    RESULTADOS = [
        ("pendiente_revision", "Pendiente de revisión"),
        ("aprobado", "Aprobado"),
        ("no_aprobado", "Aún no aprobado"),
    ]

    ejercicio = models.ForeignKey(
        "roadmaps.EjercicioLeccion",
        on_delete=models.CASCADE,
        related_name="intentos",
        verbose_name="ejercicio",
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="intentos_ejercicios",
        verbose_name="usuario",
    )
    respuesta = models.TextField(verbose_name="respuesta enviada")
    resultado = models.CharField(
        max_length=24,
        choices=RESULTADOS,
        default="pendiente_revision",
        verbose_name="resultado",
    )
    puntuacion = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="puntuación",
    )
    retroalimentacion = models.TextField(blank=True, verbose_name="retroalimentación")
    detalles = models.JSONField(default=dict, blank=True, verbose_name="detalles del resultado")
    version_evaluacion = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name="versión del evaluador"
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    evaluado_en = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "intento de ejercicio"
        verbose_name_plural = "intentos de ejercicios"
        ordering = ["-creado_en", "-id"]
        indexes = [
            models.Index(
                fields=["usuario", "ejercicio", "-creado_en"],
                name="intento_user_ejercicio_idx",
            )
        ]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(puntuacion__isnull=True)
                    | models.Q(puntuacion__gte=0, puntuacion__lte=100)
                ),
                name="intento_puntuacion_0_100",
            )
        ]

    def __str__(self):
        return f"Intento {self.pk} — {self.ejercicio} ({self.resultado})"
