"""Modelos de evaluaciones académicas y resultados (Fase 4, ADR-011).

Los quizzes y preguntas se construyen sobre los contenidos del roadmap y los
evaluadores deterministas ya existentes (``apps.roadmaps.attempts``). Un
resultado de evaluación registra la evidencia de un intento sobre un quiz,
la puntuación frente al umbral de aprobación y los temas que requieren repaso.

El tutor IA (``apps.tutoring``) puede explicar o recomendar repaso, pero nunca
decide la aprobación académica: el umbral versionable y la evidencia son del
dominio académico.
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Quiz(models.Model):
    """Quiz o examen versionable asociado a un módulo del roadmap."""

    TIPO_QUIZ = "quiz"
    TIPO_EXAMEN = "examen"
    ESTADO_BORRADOR = "borrador"
    ESTADO_PUBLICADO = "publicado"

    TIPOS = [
        (TIPO_QUIZ, "Quiz"),
        (TIPO_EXAMEN, "Examen"),
    ]
    ESTADOS = [
        (ESTADO_BORRADOR, "Borrador"),
        (ESTADO_PUBLICADO, "Publicado"),
    ]

    nombre = models.CharField(max_length=200, verbose_name="nombre")
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        default=TIPO_QUIZ,
        verbose_name="tipo",
    )
    modulo = models.ForeignKey(
        "roadmaps.Modulo",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="quizzes",
        verbose_name="módulo",
    )
    etapa = models.ForeignKey(
        "roadmaps.Etapa",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="quizzes",
        verbose_name="etapa",
    )
    umbral_aprobacion = models.PositiveSmallIntegerField(
        default=70,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="umbral de aprobación",
    )
    version = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="versión",
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_BORRADOR,
        verbose_name="estado",
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "quiz"
        verbose_name_plural = "quizzes"
        ordering = ["-creado_en"]
        constraints = [
            models.UniqueConstraint(
                fields=["modulo", "version"],
                condition=models.Q(modulo__isnull=False),
                name="quiz_unico_modulo_version",
            ),
            models.UniqueConstraint(
                fields=["etapa", "version"],
                condition=models.Q(etapa__isnull=False),
                name="quiz_unico_etapa_version",
            ),
        ]

    def clean(self) -> None:
        super().clean()
        if self.tipo == self.TIPO_QUIZ and not self.modulo_id:
            raise ValidationError({"modulo": "Un quiz debe estar asociado a un módulo."})
        if self.tipo == self.TIPO_EXAMEN and not self.etapa_id and not self.modulo_id:
            raise ValidationError({"etapa": "Un examen debe estar asociado a una etapa o a un módulo."})
        if self.etapa_id and self.modulo_id and self.modulo.etapa_id != self.etapa_id:
            raise ValidationError({"etapa": "La etapa del examen debe coincidir con la etapa del módulo."})
        if self.umbral_aprobacion is None or not 0 <= self.umbral_aprobacion <= 100:
            raise ValidationError({"umbral_aprobacion": "El umbral de aprobación debe estar entre 0 y 100."})

    def __str__(self) -> str:
        return f"Quiz {self.nombre} ({self.tipo} v{self.version})"


class Pregunta(models.Model):
    """Pregunta de quiz/examen con formato objetivo o de revisión controlada."""

    FORMATO_SELECCION = "seleccion"
    FORMATO_RESPUESTA = "respuesta"
    FORMATO_INTERPRETACION = "interpretacion_codigo"
    FORMATO_RESOLUCION = "resolucion_problemas"

    FORMATOS = [
        (FORMATO_SELECCION, "Selección"),
        (FORMATO_RESPUESTA, "Respuesta"),
        (FORMATO_INTERPRETACION, "Interpretación de código"),
        (FORMATO_RESOLUCION, "Resolución de problemas"),
    ]

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="preguntas",
        verbose_name="quiz",
    )
    orden = models.PositiveSmallIntegerField(verbose_name="orden")
    formato = models.CharField(
        max_length=30,
        choices=FORMATOS,
        verbose_name="formato",
    )
    enunciado = models.TextField(verbose_name="enunciado")
    datos_respuesta = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="datos de respuesta",
    )
    leccion = models.ForeignKey(
        "roadmaps.Leccion",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="preguntas_evaluacion",
        verbose_name="lección",
    )

    class Meta:
        verbose_name = "pregunta"
        verbose_name_plural = "preguntas"
        ordering = ["quiz", "orden"]
        constraints = [
            models.UniqueConstraint(
                fields=["quiz", "orden"],
                name="pregunta_unica_orden_por_quiz",
            ),
            models.CheckConstraint(
                condition=models.Q(
                    formato__in=[
                        "seleccion",
                        "respuesta",
                        "interpretacion_codigo",
                        "resolucion_problemas",
                    ]
                ),
                name="pregunta_formato_valido",
            ),
        ]

    def clean(self) -> None:
        super().clean()
        if not self.enunciado or not self.enunciado.strip():
            raise ValidationError({"enunciado": "La pregunta requiere un enunciado."})
        if self.orden is None or self.orden < 1:
            raise ValidationError({"orden": "La pregunta debe tener un orden mayor o igual a 1."})
        formatos_validos = {formato for formato, _ in self.FORMATOS}
        if self.formato not in formatos_validos:
            raise ValidationError({"formato": "El formato de pregunta no es válido."})
        datos = self.datos_respuesta if isinstance(self.datos_respuesta, dict) else {}
        if self.formato == self.FORMATO_SELECCION:
            opciones = datos.get("opciones")
            if not isinstance(opciones, list) or not opciones:
                raise ValidationError({"datos_respuesta": "El formato selección requiere opciones."})
            if not any(
                isinstance(opcion, dict) and opcion.get("correcta")
                for opcion in opciones
            ):
                raise ValidationError({"datos_respuesta": "El formato selección requiere una opción correcta."})
        elif self.formato == self.FORMATO_RESPUESTA:
            respuesta_esperada = datos.get("respuesta_esperada")
            if not isinstance(respuesta_esperada, str) or not respuesta_esperada.strip():
                raise ValidationError({"datos_respuesta": "El formato respuesta requiere una respuesta esperada."})
        elif self.formato in (self.FORMATO_INTERPRETACION, self.FORMATO_RESOLUCION):
            criterios = datos.get("criterios")
            if not isinstance(criterios, list) or not criterios:
                raise ValidationError({"datos_respuesta": "El formato abierto requiere criterios de evaluación."})

    def __str__(self) -> str:
        return f"Pregunta {self.orden} ({self.get_formato_display()}) — Quiz {self.quiz_id}"


class ResultadoEvaluacion(models.Model):
    """Evidencia de un intento de evaluación sobre un quiz.

    Al igual que ``IntentoEjercicio``, la evidencia no admite modificaciones
    una vez registrada; los reintentos crean nuevos resultados.
    """

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="resultados",
        verbose_name="quiz",
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resultados_evaluacion",
        verbose_name="usuario",
    )
    respuestas = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="respuestas",
    )
    puntuacion = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="puntuación",
    )
    aprobado = models.BooleanField(default=False, verbose_name="aprobado")
    umbral_aprobacion = models.PositiveSmallIntegerField(
        default=70,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="umbral de aprobación",
    )
    retroalimentacion = models.TextField(blank=True, verbose_name="retroalimentación")
    temas_repaso = models.JSONField(
        default=list,
        blank=True,
        verbose_name="temas de repaso",
    )
    requiere_revision = models.BooleanField(
        default=False,
        verbose_name="requiere revisión",
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")

    # Campos que componen la evidencia y no admiten cambios posteriores.
    CAMPOS_INMUTABLES = (
        "quiz_id",
        "usuario_id",
        "respuestas",
        "puntuacion",
        "aprobado",
        "umbral_aprobacion",
        "retroalimentacion",
        "temas_repaso",
        "requiere_revision",
    )

    class Meta:
        verbose_name = "resultado de evaluación"
        verbose_name_plural = "resultados de evaluación"
        ordering = ["-creado_en"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(puntuacion__isnull=True)
                    | models.Q(puntuacion__gte=0, puntuacion__lte=100)
                ),
                name="resultado_evaluacion_puntuacion_0_100",
            ),
        ]

    def clean(self) -> None:
        super().clean()
        if self.puntuacion is not None and not 0 <= self.puntuacion <= 100:
            raise ValidationError({"puntuacion": "La puntuación debe estar entre 0 y 100."})
        if self.umbral_aprobacion is None or not 0 <= self.umbral_aprobacion <= 100:
            raise ValidationError({"umbral_aprobacion": "El umbral de aprobación debe estar entre 0 y 100."})
        if self.aprobado and (self.puntuacion is None or self.puntuacion < self.umbral_aprobacion):
            raise ValidationError({"aprobado": "El resultado solo puede marcarse como aprobado si alcanza el umbral."})

    @property
    def esta_aprobado(self) -> bool:
        """Indica si la evidencia alcanzó el umbral de aprobación vigente."""
        return self.puntuacion is not None and self.puntuacion >= self.umbral_aprobacion

    def save(self, *args, **kwargs) -> None:
        if self.pk:
            anterior = type(self).objects.get(pk=self.pk)
            if any(
                getattr(anterior, campo) != getattr(self, campo)
                for campo in self.CAMPOS_INMUTABLES
            ):
                raise ValidationError("La evidencia de evaluación no admite modificaciones.")
        self.full_clean(validate_unique=False, validate_constraints=False)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError("La evidencia de evaluación académica no se elimina.")

    def __str__(self) -> str:
        return f"Resultado {self.pk} — Quiz {self.quiz_id} ({self.get_resultado_estado()})"

    def get_resultado_estado(self) -> str:
        if self.requiere_revision:
            return "pendiente_revision"
        return "aprobado" if self.aprobado else "no_aprobado"


class ResultadoPregunta(models.Model):
    """Resultado de una pregunta concreta dentro de un resultado de evaluación."""

    resultado = models.ForeignKey(
        ResultadoEvaluacion,
        on_delete=models.CASCADE,
        related_name="preguntas_resultados",
        verbose_name="resultado de evaluación",
    )
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name="evaluacion_resultados",
        verbose_name="pregunta",
    )
    correcta = models.BooleanField(default=False, verbose_name="correcta")
    puntuacion = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="puntuación",
    )
    respuesta = models.JSONField(
        default=dict,
        blank=True,
        verbose_name="respuesta",
    )
    retroalimentacion = models.TextField(blank=True, verbose_name="retroalimentación")
    requiere_revision = models.BooleanField(
        default=False,
        verbose_name="requiere revisión",
    )
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="registrada en")

    class Meta:
        verbose_name = "resultado de pregunta"
        verbose_name_plural = "resultados de pregunta"
        ordering = ["id"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(puntuacion__isnull=True)
                    | models.Q(puntuacion__gte=0, puntuacion__lte=100)
                ),
                name="resultado_pregunta_puntuacion_0_100",
            ),
            models.UniqueConstraint(
                fields=["resultado", "pregunta"],
                name="resultado_pregunta_unica",
            ),
        ]

    def clean(self) -> None:
        super().clean()
        if self.puntuacion is not None and not 0 <= self.puntuacion <= 100:
            raise ValidationError({"puntuacion": "La puntuación debe estar entre 0 y 100."})

    def __str__(self) -> str:
        return f"ResultadoPregunta {self.pk} — Pregunta {self.pregunta_id} (correcta: {self.correcta})"
