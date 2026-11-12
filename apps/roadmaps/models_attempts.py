"""Modelos de evaluación e intentos de ejercicios.

La configuración permanece separada del enunciado para no exponer criterios
privados en la plantilla del estudiante. Ningún modelo implica ejecución de
código: los evaluadores disponibles son deterministas y estáticos.
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ConfiguracionEvaluacion(models.Model):
    """Contrato versionado que define cómo se evalúa un ejercicio."""

    TIPOS = [
        ("respuesta_exacta", "Respuesta de texto exacta"),
        ("codigo_contiene", "Comprobación estática de fragmentos de código"),
    ]

    ejercicio = models.ForeignKey(
        "roadmaps.EjercicioLeccion",
        on_delete=models.PROTECT,
        related_name="configuraciones_evaluacion",
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
    permite_completar_leccion = models.BooleanField(
        default=False,
        verbose_name="puede aportar a la finalización de la lección",
        help_text="Debe habilitarse expresamente; los chequeos estáticos simples no deben aprobar por sí solos una lección.",
    )
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "configuración de evaluación"
        verbose_name_plural = "configuraciones de evaluación"
        ordering = ["ejercicio", "-version"]
        constraints = [
            models.UniqueConstraint(fields=["ejercicio", "version"], name="evaluacion_version_unica"),
            models.UniqueConstraint(
                fields=["ejercicio"],
                condition=models.Q(activo=True),
                name="evaluacion_unica_activa",
            ),
        ]

    def __str__(self):
        return f"Evaluador v{self.version}: {self.ejercicio}"


class IntentoEjercicioQuerySet(models.QuerySet):
    """Conserva la evidencia académica y bloquea mutaciones masivas."""

    def update(self, **kwargs):
        raise ValidationError("Los intentos son evidencia histórica y no admiten update() masivo.")

    def bulk_update(self, objs, fields, batch_size=None):
        raise ValidationError("Los intentos son evidencia histórica y no admiten bulk_update().")

    def delete(self):
        raise ValidationError("Los intentos académicos no se eliminan mediante operaciones masivas.")


class IntentoEjercicio(models.Model):
    """Entrega persistida del estudiante y resultado reproducible."""

    objects = IntentoEjercicioQuerySet.as_manager()

    RESULTADOS = [
        ("pendiente_revision", "Pendiente de revisión"),
        ("aprobado", "Aprobado"),
        ("criterios_cumplidos", "Criterios estáticos cumplidos"),
        ("no_aprobado", "Aún no aprobado"),
    ]

    ejercicio = models.ForeignKey(
        "roadmaps.EjercicioLeccion",
        on_delete=models.PROTECT,
        related_name="intentos",
        verbose_name="ejercicio",
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="intentos_ejercicios",
        verbose_name="usuario",
    )
    version_contenido = models.ForeignKey(
        "roadmaps.VersionContenidoLeccion",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="intentos",
        verbose_name="versión académica presentada",
    )
    snapshot_ejercicio = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="snapshot del ejercicio presentado",
        help_text="Conserva el enunciado exacto aunque el contenido editable cambie.",
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
    configuracion_evaluacion = models.ForeignKey(
        ConfiguracionEvaluacion,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="intentos",
        verbose_name="configuración aplicada",
    )
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

    def clean(self):
        super().clean()
        if self.version_contenido_id:
            if self.version_contenido.leccion_id != self.ejercicio.leccion_id:
                raise ValidationError({
                    "version_contenido": "La versión académica debe pertenecer a la lección del ejercicio."
                })
            if (
                not isinstance(self.snapshot_ejercicio, dict)
                or self.snapshot_ejercicio.get("clave") != str(self.ejercicio.clave_contenido)
            ):
                raise ValidationError({
                    "snapshot_ejercicio": "El snapshot debe identificar el ejercicio presentado."
                })

    def save(self, *args, **kwargs):
        if self.pk:
            anterior = type(self).objects.get(pk=self.pk)
            campos_inmutables = (
                "ejercicio_id", "usuario_id", "version_contenido_id",
                "snapshot_ejercicio", "respuesta", "configuracion_evaluacion_id",
                "version_evaluacion", "creado_en",
            )
            if any(
                getattr(anterior, campo) != getattr(self, campo)
                for campo in campos_inmutables
            ):
                raise ValidationError("La evidencia original de un intento es inmutable.")
        self.full_clean(validate_unique=False, validate_constraints=False)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError("Los intentos académicos no se eliminan físicamente.")

    def __str__(self):
        return f"Intento {self.pk} — {self.ejercicio} ({self.resultado})"
