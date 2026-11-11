"""Modelos del módulo académico: Roadmap ASCENSO.

La jerarquía reproduce los requisitos RD-004 (roadmap, etapa, módulo, lección,
actividad), RD-005 (prerrequisitos) y RD-006 (criterios de finalización).
El contenido de las 33 etapas se carga desde el documento maestro oficial
ASCENSO 3.1; este módulo no inventa etapas ni dependencias.
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Roadmap(models.Model):
    """Contenedor raíz de una ruta formativa (ASCENSO 3.1 u otra futura)."""

    nombre = models.CharField(max_length=200, verbose_name="nombre")
    edicion = models.CharField(max_length=20, verbose_name="edición")
    fecha_consolidacion = models.DateField(
        null=True, blank=True, verbose_name="fecha de consolidación"
    )
    fuente = models.CharField(max_length=255, blank=True, verbose_name="fuente documental")
    sha256_fuente = models.CharField(
        max_length=64, blank=True, verbose_name="SHA-256 de la fuente"
    )
    activo = models.BooleanField(default=True, verbose_name="activo")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "roadmap"
        verbose_name_plural = "roadmaps"
        ordering = ["-activo", "-actualizado_en"]
        constraints = [
            models.UniqueConstraint(
                fields=["nombre", "edicion"], name="roadmap_unico_nombre_edicion"
            )
        ]

    def __str__(self) -> str:
        return f"{self.nombre} ({self.edicion})"

    @property
    def total_etapas(self) -> int:
        return self.etapas.count()

    @property
    def total_modulos(self) -> int:
        return Modulo.objects.filter(etapa__roadmap=self).count()

    @property
    def total_lecciones(self) -> int:
        return Leccion.objects.filter(modulo__etapa__roadmap=self).count()

    @property
    def total_proyectos(self) -> int:
        return self.etapas.exclude(proyecto="").count()


class Etapa(models.Model):
    """Etapa numerada del roadmap (0 a 32 en ASCENSO 3.1)."""

    PRIORIDADES = [
        ("P1", "P1 — Obligatoria"),
        ("P2", "P2 — Complementaria"),
        ("P3", "P3 — Especialización avanzada"),
    ]

    roadmap = models.ForeignKey(
        Roadmap, on_delete=models.CASCADE, related_name="etapas", verbose_name="roadmap"
    )
    numero = models.PositiveSmallIntegerField(verbose_name="número")
    titulo = models.CharField(max_length=200, verbose_name="título")
    bloque = models.CharField(max_length=140, blank=True, verbose_name="bloque")
    seccion = models.CharField(max_length=180, blank=True, verbose_name="sección")
    prioridad = models.CharField(
        max_length=2, choices=PRIORIDADES, default="P1", verbose_name="prioridad"
    )
    prioridad_detalle = models.CharField(
        max_length=160, blank=True, verbose_name="detalle de prioridad"
    )
    objetivo = models.TextField(blank=True, verbose_name="objetivo")
    proyecto = models.TextField(blank=True, verbose_name="proyecto de la etapa")
    proyecto_titulo = models.CharField(
        max_length=60, blank=True, verbose_name="título del proyecto"
    )
    notas = models.TextField(
        blank=True,
        verbose_name="notas del documento",
        help_text="Ampliaciones o trayectos complementarios documentados para la etapa.",
    )
    nota_mvp = models.TextField(
        blank=True,
        verbose_name="nota sobre el MVP",
        help_text="Aclaración sobre el estado de desarrollo en el MVP (P-002).",
    )
    desarrollada_en_mvp = models.BooleanField(
        default=False, verbose_name="desarrollada en el MVP"
    )
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"
        ordering = ["orden", "numero"]
        constraints = [
            models.UniqueConstraint(
                fields=["roadmap", "numero"], name="etapa_unica_por_roadmap"
            )
        ]

    def __str__(self) -> str:
        return f"Etapa {self.numero} — {self.titulo}"

    @property
    def total_modulos(self) -> int:
        return self.modulos.count()

    @property
    def total_lecciones(self) -> int:
        return Leccion.objects.filter(modulo__etapa=self).count()

    @property
    def total_actividades(self) -> int:
        return Actividad.objects.filter(leccion__modulo__etapa=self).count()

    def esta_bloqueada_para(self, etapas_completadas: set[int]) -> bool:
        """Devuelve True si algún prerrequisito no está completado."""
        requeridas = self.prerrequisitos.values_list("etapa_requerida__numero", flat=True)
        return any(numero not in etapas_completadas for numero in requeridas)


class Modulo(models.Model):
    """Módulo temático dentro de una etapa (por ejemplo, 0.1)."""

    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, related_name="modulos", verbose_name="etapa"
    )
    numero = models.CharField(max_length=20, verbose_name="número")
    titulo = models.CharField(max_length=200, verbose_name="título")
    objetivo = models.TextField(blank=True, verbose_name="objetivo")
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "módulo"
        verbose_name_plural = "módulos"
        ordering = ["orden", "numero"]
        constraints = [
            models.UniqueConstraint(
                fields=["etapa", "numero"], name="modulo_unico_por_etapa"
            )
        ]

    def __str__(self) -> str:
        return f"{self.numero} {self.titulo}"

    @property
    def total_lecciones(self) -> int:
        return self.lecciones.count()


class Leccion(models.Model):
    """Unidad de aprendizaje extraída del documento maestro."""

    TIPOS = [
        ("concepto", "Concepto"),
        ("practica", "Práctica"),
        ("laboratorio", "Laboratorio"),
        ("proyecto", "Proyecto"),
        ("evaluacion", "Evaluación"),
    ]

    modulo = models.ForeignKey(
        Modulo, on_delete=models.CASCADE, related_name="lecciones", verbose_name="módulo"
    )
    titulo = models.CharField(max_length=220, verbose_name="título")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    tipo = models.CharField(
        max_length=20, choices=TIPOS, default="concepto", verbose_name="tipo"
    )
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    duracion_estimada_minutos = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="duración estimada (minutos)"
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "lección"
        verbose_name_plural = "lecciones"
        ordering = ["orden", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["modulo", "titulo"], name="leccion_unica_por_modulo"
            )
        ]

    def __str__(self) -> str:
        return self.titulo


class Actividad(models.Model):
    """Actividad concreta asociada a una lección."""

    TIPOS = [
        ("lectura", "Lectura"),
        ("ejercicio", "Ejercicio"),
        ("laboratorio", "Laboratorio"),
        ("proyecto", "Proyecto"),
        ("evaluacion", "Evaluación"),
    ]

    leccion = models.ForeignKey(
        Leccion, on_delete=models.CASCADE, related_name="actividades", verbose_name="lección"
    )
    titulo = models.CharField(max_length=220, verbose_name="título")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    tipo = models.CharField(
        max_length=20, choices=TIPOS, default="lectura", verbose_name="tipo"
    )
    obligatoria = models.BooleanField(default=True, verbose_name="obligatoria")
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        ordering = ["orden", "id"]
        constraints = [
            models.UniqueConstraint(
                fields=["leccion", "titulo"], name="actividad_unica_por_leccion"
            )
        ]

    def __str__(self) -> str:
        return self.titulo


class Prerrequisito(models.Model):
    """Dependencia explícita entre etapas (RD-005)."""

    etapa = models.ForeignKey(
        Etapa,
        on_delete=models.CASCADE,
        related_name="prerrequisitos",
        verbose_name="etapa dependiente",
    )
    etapa_requerida = models.ForeignKey(
        Etapa,
        on_delete=models.CASCADE,
        related_name="desbloquea",
        verbose_name="etapa requerida",
    )
    justificacion = models.TextField(blank=True, verbose_name="justificación documental")
    documentado = models.BooleanField(
        default=True, verbose_name="documentado en la fuente"
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "prerrequisito"
        verbose_name_plural = "prerrequisitos"
        ordering = ["etapa__numero", "etapa_requerida__numero"]
        constraints = [
            models.UniqueConstraint(
                fields=["etapa", "etapa_requerida"],
                name="prerrequisito_unico_por_etapa",
            ),
            models.CheckConstraint(
                condition=~models.Q(etapa=models.F("etapa_requerida")),
                name="prerrequisito_no_autoreferente",
            ),
        ]

    def clean(self) -> None:
        if self.etapa_id and self.etapa_id == self.etapa_requerida_id:
            raise ValidationError("Una etapa no puede ser prerrequisito de sí misma.")

    def __str__(self) -> str:
        return f"Etapa {self.etapa.numero} requiere etapa {self.etapa_requerida.numero}"


class CriterioFinalizacion(models.Model):
    """Criterio verificable para dar una etapa por completada (RD-006)."""

    TIPOS = [
        ("proyecto", "Proyecto"),
        ("evaluacion", "Evaluación"),
        ("evidencia", "Evidencia"),
        ("manual", "Verificación manual"),
    ]

    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, related_name="criterios", verbose_name="etapa"
    )
    titulo = models.CharField(max_length=160, verbose_name="título")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    tipo = models.CharField(
        max_length=20, choices=TIPOS, default="proyecto", verbose_name="tipo"
    )
    obligatorio = models.BooleanField(default=True, verbose_name="obligatorio")
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")

    class Meta:
        verbose_name = "criterio de finalización"
        verbose_name_plural = "criterios de finalización"
        ordering = ["orden", "id"]

    def __str__(self) -> str:
        return f"{self.etapa.numero}: {self.titulo}"


class Progreso(models.Model):
    """Registro de avance por etapa, módulo, lección o actividad (RF-016)."""

    ESTADOS = [
        ("no_iniciado", "No iniciado"),
        ("en_progreso", "En progreso"),
        ("completado", "Completado"),
        ("bloqueado", "Bloqueado"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="progresos_roadmap",
        verbose_name="usuario",
    )
    etapa = models.ForeignKey(
        Etapa, on_delete=models.CASCADE, related_name="progresos", verbose_name="etapa"
    )
    modulo = models.ForeignKey(
        Modulo,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="progresos",
        verbose_name="módulo",
    )
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="progresos",
        verbose_name="lección",
    )
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="progresos",
        verbose_name="actividad",
    )
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default="no_iniciado", verbose_name="estado"
    )
    porcentaje = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="porcentaje",
    )
    tiempo_dedicado_minutos = models.PositiveIntegerField(
        default=0, verbose_name="tiempo dedicado (minutos)"
    )
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name="fecha de inicio")
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="última actualización"
    )
    fecha_completado = models.DateTimeField(
        null=True, blank=True, verbose_name="fecha de finalización"
    )

    class Meta:
        verbose_name = "progreso"
        verbose_name_plural = "progresos"
        ordering = ["-fecha_actualizacion"]
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "etapa", "modulo", "leccion", "actividad"],
                name="progreso_unico_por_objetivo",
            )
        ]

    def __str__(self) -> str:
        objetivo = "etapa"
        if self.actividad_id:
            objetivo = f"actividad {self.actividad_id}"
        elif self.leccion_id:
            objetivo = f"lección {self.leccion_id}"
        elif self.modulo_id:
            objetivo = f"módulo {self.modulo_id}"
        return f"{self.usuario} — {objetivo} ({self.estado})"

    def save(self, *args, **kwargs):
        if self.estado == "completado":
            self.porcentaje = 100
            if self.fecha_completado is None:
                self.fecha_completado = timezone.now()
        elif self.estado == "no_iniciado":
            self.porcentaje = 0
            self.fecha_completado = None
        super().save(*args, **kwargs)


class ContenidoLeccion(models.Model):
    """Contenido didáctico estructurado para una lección del roadmap."""

    leccion = models.OneToOneField(
        Leccion,
        on_delete=models.CASCADE,
        related_name="contenido",
        verbose_name="lección",
    )
    objetivos_aprendizaje = models.TextField(
        blank=True, verbose_name="objetivos de aprendizaje"
    )
    teoria_tecnica = models.TextField(
        blank=True,
        verbose_name="teoría técnica",
        help_text="Explicación rigurosa del concepto, terminología y fundamentos.",
    )
    explicacion_sencilla = models.TextField(
        blank=True,
        verbose_name="explicación sencilla",
        help_text="Explicación clara, gradual y sin asumir conocimientos no presentados.",
    )
    notas = models.TextField(blank=True, verbose_name="notas complementarias")
    publicado = models.BooleanField(default=False, verbose_name="publicado")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "contenido de lección"
        verbose_name_plural = "contenidos de lecciones"

    def __str__(self) -> str:
        return f"Contenido: {self.leccion.titulo}"

    @property
    def esta_completo(self) -> bool:
        return bool(self.teoria_tecnica.strip() and self.explicacion_sencilla.strip())


class EjemploLeccion(models.Model):
    """Ejemplo explicado que acompaña la teoría de una lección."""

    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        related_name="ejemplos",
        verbose_name="lección",
    )
    titulo = models.CharField(max_length=180, verbose_name="título")
    contexto = models.TextField(blank=True, verbose_name="contexto")
    lenguaje = models.CharField(max_length=40, blank=True, verbose_name="lenguaje")
    codigo = models.TextField(blank=True, verbose_name="código")
    salida_esperada = models.TextField(blank=True, verbose_name="salida esperada")
    explicacion = models.TextField(blank=True, verbose_name="explicación paso a paso")
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    publicado = models.BooleanField(default=True, verbose_name="publicado")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ejemplo de lección"
        verbose_name_plural = "ejemplos de lección"
        ordering = ["orden", "id"]

    def __str__(self) -> str:
        return f"{self.leccion.titulo}: {self.titulo}"


class EjercicioLeccion(models.Model):
    """Enunciado de práctica; evaluación en fase 2 y tutoría en fase 3."""

    NIVELES = [
        ("basico", "Básico"),
        ("intermedio", "Intermedio"),
        ("avanzado", "Avanzado"),
    ]

    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        related_name="ejercicios",
        verbose_name="lección",
    )
    titulo = models.CharField(max_length=180, verbose_name="título")
    enunciado = models.TextField(verbose_name="enunciado")
    instrucciones = models.TextField(blank=True, verbose_name="instrucciones")
    lenguaje = models.CharField(max_length=40, blank=True, verbose_name="lenguaje")
    nivel = models.CharField(
        max_length=16, choices=NIVELES, default="basico", verbose_name="nivel"
    )
    codigo_inicial = models.TextField(blank=True, verbose_name="código inicial")
    pista_1 = models.TextField(blank=True, verbose_name="pista 1")
    pista_2 = models.TextField(blank=True, verbose_name="pista 2")
    pista_3 = models.TextField(blank=True, verbose_name="pista 3")
    obligatorio = models.BooleanField(default=True, verbose_name="obligatorio")
    orden = models.PositiveSmallIntegerField(default=0, verbose_name="orden")
    publicado = models.BooleanField(default=True, verbose_name="publicado")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ejercicio de lección"
        verbose_name_plural = "ejercicios de lección"
        ordering = ["orden", "id"]

    def __str__(self) -> str:
        return f"{self.leccion.titulo}: {self.titulo}"

    @property
    def total_pistas_disponibles(self) -> int:
        return sum(bool(pista.strip()) for pista in (self.pista_1, self.pista_2, self.pista_3))

# Registrar los modelos auxiliares del flujo de intentos y evaluación.
from .models_attempts import ConfiguracionEvaluacion, IntentoEjercicio  # noqa: E402,F401
