"""Modelos base para minijuegos, desafíos y jefes (Fase 7).

Cada actividad declara la competencia que practica y registra resultados
verificables. No sustituye exámenes formales de etapa.
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Desafio(models.Model):
    """Definición de minijuego, desafío o jefe integrador."""

    TIPOS = [
        ("minijuego", "Minijuego"),
        ("desafio", "Desafío"),
        ("jefe", "Jefe / reto integrador"),
    ]
    DIFICULTADES = [
        ("basica", "Básica"),
        ("intermedia", "Intermedia"),
        ("avanzada", "Avanzada"),
        ("adaptativa", "Adaptativa"),
    ]

    nombre = models.CharField(max_length=160, verbose_name="nombre")
    tipo = models.CharField(max_length=20, choices=TIPOS, default="minijuego", verbose_name="tipo")
    competencia = models.CharField(
        max_length=200,
        verbose_name="competencia que practica",
        help_text="Competencia declarada explícitamente (p. ej. lógica, depuración).",
    )
    etapa = models.ForeignKey(
        "roadmaps.Etapa",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="desafios",
        verbose_name="etapa",
    )
    modulo = models.ForeignKey(
        "roadmaps.Modulo",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="desafios",
        verbose_name="módulo",
    )
    dificultad = models.CharField(max_length=20, choices=DIFICULTADES, default="basica", verbose_name="dificultad")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    reglas = models.JSONField(default=dict, blank=True, verbose_name="reglas/objetivos")
    activo = models.BooleanField(default=True, verbose_name="activo")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "desafío"
        verbose_name_plural = "desafíos"
        ordering = ["tipo", "nombre"]

    def clean(self) -> None:
        super().clean()
        if not self.competencia or not self.competencia.strip():
            raise ValidationError({"competencia": "Cada desafío debe declarar la competencia que practica."})

    def __str__(self) -> str:
        return f"{self.nombre} ({self.get_tipo_display()})"


class ResultadoDesafio(models.Model):
    """Evidencia de intento/resultado en un desafío (no sustituye examen formal)."""

    desafio = models.ForeignKey(
        Desafio,
        on_delete=models.CASCADE,
        related_name="resultados",
        verbose_name="desafío",
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resultados_desafio",
        verbose_name="usuario",
    )
    puntuacion = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="puntuación",
    )
    completado = models.BooleanField(default=False, verbose_name="completado")
    tiempo_segundos = models.PositiveIntegerField(null=True, blank=True, verbose_name="tiempo (s)")
    datos_rendimiento = models.JSONField(default=dict, blank=True, verbose_name="datos de rendimiento")
    conceptos_practicados = models.JSONField(default=list, blank=True, verbose_name="conceptos practicados")
    retroalimentacion = models.TextField(blank=True, verbose_name="retroalimentación")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")

    CAMPOS_INMUTABLES = (
        "desafio_id", "usuario_id", "puntuacion", "completado",
        "tiempo_segundos", "datos_rendimiento", "conceptos_practicados", "retroalimentacion",
    )

    class Meta:
        verbose_name = "resultado de desafío"
        verbose_name_plural = "resultados de desafío"
        ordering = ["-creado_en"]

    def clean(self) -> None:
        super().clean()
        if self.puntuacion is not None and not 0 <= self.puntuacion <= 100:
            raise ValidationError({"puntuacion": "La puntuación debe estar entre 0 y 100."})

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            anterior = type(self).objects.get(pk=self.pk)
            if any(getattr(anterior, c) != getattr(self, c) for c in self.CAMPOS_INMUTABLES):
                raise ValidationError("La evidencia de desafío no admite modificaciones.")
        self.full_clean(validate_unique=False, validate_constraints=False)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError("La evidencia de desafío no se elimina.")

    def __str__(self) -> str:
        return f"Resultado {self.pk} — {self.desafio} ({'completado' if self.completado else 'intento'})"
