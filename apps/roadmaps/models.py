"""Modelos del módulo académico: Roadmap ASCENSO.

La jerarquía reproduce los requisitos RD-004 (roadmap, etapa, módulo, lección,
actividad), RD-005 (prerrequisitos) y RD-006 (criterios de finalización).
El contenido de las 33 etapas se carga desde el documento maestro oficial
ASCENSO 3.1; este módulo no inventa etapas ni dependencias.
"""

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
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

    clave_contenido = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="clave estable de contenido")

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



class FuenteConocimiento(models.Model):
    """Fuente técnica consultada para elaborar o revisar contenido académico."""

    ESTADOS_LICENCIA = [
        ("pendiente", "Pendiente de revisión"),
        ("compatible", "Reutilización compatible"),
        ("solo_referencia", "Solo consulta; contenido original"),
        ("requiere_permiso", "Requiere permiso"),
        ("no_reutilizable", "No reutilizable"),
    ]

    clave = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    publicador = models.CharField(max_length=180, verbose_name="publicador")
    titulo = models.CharField(max_length=240, verbose_name="título de la fuente")
    url_canonica = models.URLField(max_length=1000, verbose_name="URL canónica")
    edicion = models.CharField(max_length=100, blank=True, verbose_name="edición o versión")
    identificador_licencia = models.CharField(
        max_length=120, blank=True, verbose_name="identificador de licencia"
    )
    url_licencia = models.URLField(max_length=1000, blank=True, verbose_name="URL de licencia")
    estado_revision_licencia = models.CharField(
        max_length=20, choices=ESTADOS_LICENCIA, default="pendiente",
        verbose_name="estado de revisión de licencia",
    )
    evidencia_licencia = models.URLField(
        max_length=1000, blank=True, verbose_name="evidencia de revisión de licencia"
    )
    alcance_licencia = models.TextField(blank=True, verbose_name="alcance autorizado")
    nota_revision_licencia = models.TextField(blank=True, verbose_name="decisión editorial de licencia")
    revisada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True,
        related_name="fuentes_licencia_revisadas", verbose_name="licencia revisada por",
    )
    revisada_en = models.DateTimeField(null=True, blank=True, verbose_name="licencia revisada el")
    consultada_en = models.DateTimeField(null=True, blank=True, verbose_name="consultada el")
    activa = models.BooleanField(default=True, verbose_name="fuente activa")
    notas = models.TextField(blank=True, verbose_name="notas editoriales")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "fuente de conocimiento"
        verbose_name_plural = "fuentes de conocimiento"
        ordering = ["publicador", "titulo"]
        constraints = [
            models.UniqueConstraint(
                fields=["url_canonica", "edicion"],
                name="fuente_unica_url_edicion",
            )
        ]

    def __str__(self):
        return f"{self.publicador}: {self.titulo}"


class VersionContenidoLeccionQuerySet(models.QuerySet):
    """Impide mutaciones masivas que omitan el flujo editorial."""

    def update(self, **kwargs):
        raise ValidationError(
            "Las versiones de contenido solo pueden cambiar mediante servicios editoriales."
        )

    def bulk_update(self, objs, fields, batch_size=None):
        raise ValidationError(
            "Las versiones de contenido solo pueden cambiar mediante servicios editoriales."
        )

    def bulk_create(self, objs, **kwargs):
        objs = list(objs)
        if any(obj.estado != "borrador" for obj in objs):
            raise ValidationError("Las versiones deben crearse inicialmente como borrador.")
        return super().bulk_create(objs, **kwargs)

    def delete(self):
        raise ValidationError(
            "No se permite eliminar versiones mediante operaciones masivas."
        )


class VersionContenidoLeccion(models.Model):
    """Snapshot versionado del contenido de una lección; no reemplaza el borrador editable."""

    ESTADOS = [
        ("borrador", "Borrador"),
        ("revision", "En revisión"),
        ("aprobada", "Aprobada"),
        ("publicada", "Publicada"),
        ("sustituida", "Sustituida"),
        ("retirada", "Retirada"),
    ]

    objects = VersionContenidoLeccionQuerySet.as_manager()

    clave = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.PROTECT,
        related_name="versiones_contenido",
        verbose_name="lección",
    )
    numero_version = models.PositiveIntegerField(verbose_name="número de versión")
    esquema_version = models.PositiveSmallIntegerField(default=1, verbose_name="versión del esquema")
    estado = models.CharField(max_length=12, choices=ESTADOS, default="borrador")
    snapshot = models.JSONField(verbose_name="snapshot académico")
    sha256 = models.CharField(
        max_length=64,
        validators=[RegexValidator(r"^[0-9a-f]{64}$", "Debe ser un SHA-256 hexadecimal en minúsculas.")],
        verbose_name="SHA-256 del snapshot",
    )
    resumen_cambios = models.TextField(blank=True, verbose_name="resumen de cambios")
    motivo_retiro = models.TextField(blank=True, verbose_name="motivo de retiro")
    revisada_en = models.DateTimeField(null=True, blank=True, verbose_name="revisada el")
    publicada_en = models.DateTimeField(null=True, blank=True, verbose_name="publicada el")
    fuentes = models.ManyToManyField(
        FuenteConocimiento,
        through="ReferenciaFuenteContenido",
        related_name="versiones",
        blank=True,
    )
    enviada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="versiones_contenido_enviadas",
        verbose_name="enviada por",
    )
    enviada_en = models.DateTimeField(null=True, blank=True, verbose_name="enviada a revisión el")
    revisada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="versiones_contenido_revisadas",
        verbose_name="revisada por",
    )
    publicada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="versiones_contenido_publicadas",
        verbose_name="publicada por",
    )
    retirada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="versiones_contenido_retiradas",
        verbose_name="retirada por",
    )
    retirada_en = models.DateTimeField(null=True, blank=True, verbose_name="retirada el")
    creada_en = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk and self.estado != "borrador":
            raise ValidationError("Una versión debe crearse inicialmente como borrador.")
        if self.pk:
            anterior = type(self).objects.only(
                "estado", "leccion_id", "numero_version", "esquema_version",
                "snapshot", "sha256", "resumen_cambios",
                "enviada_por_id", "enviada_en", "revisada_por_id", "revisada_en",
                "publicada_por_id", "publicada_en", "retirada_por_id", "retirada_en",
                "motivo_retiro",
            ).get(pk=self.pk)
            estados_bloqueados = {"revision", "aprobada", "publicada", "sustituida", "retirada"}
            campos_inmutables = (
                "leccion_id", "numero_version", "esquema_version",
                "snapshot", "sha256", "resumen_cambios",
            )
            if anterior.estado in estados_bloqueados:
                modificados = [
                    campo for campo in campos_inmutables
                    if getattr(anterior, campo) != getattr(self, campo)
                ]
                if modificados:
                    raise ValidationError(
                        "Una versión enviada a revisión no puede modificar su snapshot, "
                        "hash, identidad ni resumen de cambios."
                    )

            transiciones = {
                "borrador": {"revision"},
                "revision": {"aprobada"},
                "aprobada": {"publicada"},
                "publicada": {"sustituida", "retirada"},
            }
            if anterior.estado != self.estado:
                if self.estado not in transiciones.get(anterior.estado, set()):
                    raise ValidationError(
                        f"Transición editorial no permitida: {anterior.estado} → {self.estado}."
                    )
                requisitos = {
                    "revision": (self.enviada_por_id, self.enviada_en),
                    "aprobada": (self.revisada_por_id, self.revisada_en),
                    "publicada": (self.publicada_por_id, self.publicada_en),
                    "retirada": (
                        self.retirada_por_id,
                        self.retirada_en,
                        self.motivo_retiro.strip(),
                    ),
                }
                if self.estado in requisitos and not all(requisitos[self.estado]):
                    raise ValidationError(
                        "La transición editorial requiere sus metadatos de auditoría."
                    )

            auditoria = (
                "enviada_por_id", "enviada_en", "revisada_por_id", "revisada_en",
                "publicada_por_id", "publicada_en", "retirada_por_id", "retirada_en",
            )
            for campo in auditoria:
                valor_anterior = getattr(anterior, campo)
                if valor_anterior is not None and getattr(self, campo) != valor_anterior:
                    raise ValidationError(
                        "Los metadatos de auditoría editorial no se pueden sobrescribir."
                    )
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.estado != "borrador":
            raise ValidationError("Solo se pueden eliminar versiones que sigan en borrador.")
        return super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "versión de contenido de lección"
        verbose_name_plural = "versiones de contenido de lección"
        ordering = ["leccion_id", "-numero_version"]
        constraints = [
            models.UniqueConstraint(
                fields=["leccion", "numero_version"],
                name="contenido_version_unica_leccion",
            ),
            models.UniqueConstraint(
                fields=["leccion"],
                condition=models.Q(estado="publicada"),
                name="contenido_una_publicada_por_leccion",
            ),
        ]
        indexes = [
            models.Index(fields=["estado", "publicada_en"], name="contenido_estado_pub_idx")
        ]

    def clean(self):
        super().clean()
        if len(self.sha256) != 64 or any(c not in "0123456789abcdef" for c in self.sha256):
            raise ValidationError({"sha256": "Debe ser un SHA-256 hexadecimal de 64 caracteres."})

    def __str__(self):
        return f"{self.leccion} — v{self.numero_version} ({self.estado})"


class ReferenciaFuenteContenido(models.Model):
    """Atribución explícita de una fuente dentro de una versión académica."""

    ROLES = [
        ("principal", "Fuente principal"),
        ("complementaria", "Fuente complementaria"),
        ("normativa", "Especificación o norma"),
    ]

    version = models.ForeignKey(
        VersionContenidoLeccion,
        on_delete=models.PROTECT,
        related_name="referencias",
    )
    fuente = models.ForeignKey(
        FuenteConocimiento,
        on_delete=models.PROTECT,
        related_name="referencias_contenido",
    )
    USOS_DECLARADOS = [
        ("original", "Contenido original de CodeGuard"),
        ("cita_breve", "Cita breve atribuida"),
        ("adaptacion", "Adaptación de la fuente"),
        ("reproduccion", "Reproducción de material"),
    ]

    rol = models.CharField(max_length=16, choices=ROLES, default="principal")
    uso_declarado = models.CharField(
        max_length=16, choices=USOS_DECLARADOS, default="original",
        verbose_name="uso declarado de la fuente",
    )
    localizador = models.CharField(max_length=500, blank=True, verbose_name="sección o localizador")
    nota_atribucion = models.TextField(blank=True, verbose_name="nota de atribución")

    class Meta:
        verbose_name = "referencia de fuente de contenido"
        verbose_name_plural = "referencias de fuentes de contenido"
        constraints = [
            models.UniqueConstraint(
                fields=["version", "fuente"],
                name="referencia_fuente_unica_version",
            )
        ]

    def __str__(self):
        return f"{self.fuente} → {self.version}"


class EjemploLeccion(models.Model):
    """Ejemplo explicado que acompaña la teoría de una lección."""

    clave_contenido = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="clave estable de contenido")

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

    clave_contenido = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, verbose_name="clave estable de contenido")

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
