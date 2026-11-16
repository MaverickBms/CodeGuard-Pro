"""Modelos del tutor inteligente local (Fase 3).

El tutor acompaña al estudiante sin resolver los ejercicios por él.
Proporciona orientación gradual con un máximo de 3 pistas por ejercicio,
nunca revela la solución completa y nunca ejecuta código del estudiante.
"""

from django.conf import settings
from django.db import models
from django.utils import timezone


class SesionTutoria(models.Model):
    """Sesión de tutoría para un ejercicio de un usuario."""

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sesiones_tutoria",
        verbose_name="usuario",
    )
    ejercicio = models.ForeignKey(
        "roadmaps.EjercicioLeccion",
        on_delete=models.CASCADE,
        related_name="sesiones_tutoria",
        verbose_name="ejercicio",
    )
    pistas_utilizadas = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="pistas utilizadas",
        help_text="Número de pistas entregadas (máximo 3).",
    )
    ultima_pista_en = models.DateTimeField(
        null=True, blank=True, verbose_name="última pista entregada"
    )
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="creada en")
    actualizada_en = models.DateTimeField(auto_now=True, verbose_name="actualizada en")

    class Meta:
        verbose_name = "sesión de tutoría"
        verbose_name_plural = "sesiones de tutoría"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "ejercicio"],
                name="sesion_tutoria_unica_usuario_ejercicio",
            ),
        ]

    def __str__(self) -> str:
        return f"Tutoría {self.usuario} — {self.ejercicio} (pistas {self.pistas_utilizadas}/3)"

    @property
    def pistas_disponibles(self) -> int:
        """Devuelve cuántas pistas quedan disponibles."""
        return max(0, 3 - self.pistas_utilizadas)

    @property
    def limite_alcanzado(self) -> bool:
        """Indica si se alcanzó el límite de 3 pistas."""
        return self.pistas_utilizadas >= 3

    def puede_entregar_pista(self) -> bool:
        """Devuelve True si se puede entregar otra pista."""
        return not self.limite_alcanzado


class PistaTutoria(models.Model):
    """Pista entregada por el tutor a un estudiante."""

    TIPOS = [
        ("orientacion", "Orientación hacia el concepto"),
        ("estrategia", "Estrategia o enfoque posible"),
        ("concretizacion", "Orientación más concreta"),
    ]

    sesion = models.ForeignKey(
        SesionTutoria,
        on_delete=models.CASCADE,
        related_name="pistas",
        verbose_name="sesión de tutoría",
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        verbose_name="tipo de pista",
    )
    contenido = models.TextField(verbose_name="contenido de la pista")
    numero_pista = models.PositiveSmallIntegerField(
        verbose_name="número de pista",
        help_text="1, 2 o 3 según el orden de entrega.",
    )
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="entregada en")

    class Meta:
        verbose_name = "pista de tutoría"
        verbose_name_plural = "pistas de tutoría"
        ordering = ["numero_pista"]
        constraints = [
            models.UniqueConstraint(
                fields=["sesion", "numero_pista"],
                name="pista_unica_numero_por_sesion",
            ),
        ]

    def __str__(self) -> str:
        return f"Pista {self.numero_pista} ({self.tipo}) — {self.sesion}"


class IntentoTutoria(models.Model):
    """Registro de un intento analizado por el tutor."""

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="intentos_tutoria",
        verbose_name="usuario",
    )
    ejercicio = models.ForeignKey(
        "roadmaps.EjercicioLeccion",
        on_delete=models.CASCADE,
        related_name="intentos_tutoria",
        verbose_name="ejercicio",
    )
    intento_ejercicio = models.ForeignKey(
        "roadmaps.IntentoEjercicio",
        on_delete=models.CASCADE,
        related_name="analisis_tutoria",
        verbose_name="intento de ejercicio",
        null=True,
        blank=True,
    )
    resultado_evaluacion = models.CharField(
        max_length=30,
        verbose_name="resultado de la evaluación",
        help_text="aprobado, no_aprobado, pendiente_revision",
    )
    analisis_tutor = models.TextField(
        blank=True,
        verbose_name="análisis del tutor",
        help_text="Explicación del tutor sobre el resultado (no la solución).",
    )
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="analizado en")

    class Meta:
        verbose_name = "intento de tutoría"
        verbose_name_plural = "intentos de tutoría"
        ordering = ["-creada_en"]

    def __str__(self) -> str:
        return f"Análisis {self.ejercicio} — {self.resultado_evaluacion}"
