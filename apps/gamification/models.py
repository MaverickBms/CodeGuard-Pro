"""Modelos de gamificación y economía de recompensas (Fase 5).

Las recompensas motivan sin sustituir ni alterar el aprendizaje o las
aprobaciones académicas. Todas las transacciones deben ser consistentes,
auditables y no duplicables.
"""

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone


class PerfilGamificacion(models.Model):
    """Perfil de gamificación por usuario (saldo, racha, contadores)."""

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_gamificacion",
        verbose_name="usuario",
    )
    saldo_monedas = models.PositiveIntegerField(default=0, verbose_name="saldo de monedas")
    racha_dias = models.PositiveIntegerField(default=0, verbose_name="racha (días)")
    mejor_racha_dias = models.PositiveIntegerField(default=0, verbose_name="mejor racha (días)")
    ultima_actividad_fecha = models.DateField(
        null=True, blank=True, verbose_name="última actividad (fecha)"
    )
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "perfil de gamificación"
        verbose_name_plural = "perfiles de gamificación"

    def __str__(self) -> str:
        return f"Perfil gamificación — {self.usuario} ({self.saldo_monedas} monedas)"


class Logro(models.Model):
    """Definición de un logro verificable."""

    clave = models.SlugField(max_length=80, unique=True, verbose_name="clave")
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    condicion = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="condición verificable",
        help_text="Identificador de la condición/evento que otorga el logro.",
    )
    recompensa_monedas = models.PositiveIntegerField(
        default=0, verbose_name="recompensa en monedas"
    )
    activo = models.BooleanField(default=True, verbose_name="activo")

    class Meta:
        verbose_name = "logro"
        verbose_name_plural = "logros"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return self.nombre


class LogroObtenido(models.Model):
    """Registro de un logro otorgado a un usuario (no duplicable)."""

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="logros_obtenidos",
        verbose_name="usuario",
    )
    logro = models.ForeignKey(
        Logro,
        on_delete=models.CASCADE,
        related_name="otorgados",
        verbose_name="logro",
    )
    obtenido_en = models.DateTimeField(default=timezone.now, verbose_name="obtenido en")
    origen = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="origen",
        help_text="Evento o referencia que justificó el otorgamiento.",
    )

    class Meta:
        verbose_name = "logro obtenido"
        verbose_name_plural = "logros obtenidos"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "logro"], name="logro_unico_por_usuario"
            )
        ]
        ordering = ["-obtenido_en"]

    def __str__(self) -> str:
        return f"{self.usuario} — {self.logro}"


class TransaccionMoneda(models.Model):
    """Historial auditable de transacciones de moneda virtual."""

    TIPOS = [
        ("credito", "Crédito"),
        ("debito", "Débito"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transacciones_moneda",
        verbose_name="usuario",
    )
    tipo = models.CharField(max_length=10, choices=TIPOS, verbose_name="tipo")
    monto = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], verbose_name="monto"
    )
    saldo_resultante = models.PositiveIntegerField(
        default=0, verbose_name="saldo resultante"
    )
    concepto = models.CharField(max_length=160, verbose_name="concepto")
    referencia = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="referencia",
        help_text="Clave idempotente/origen (p.ej. logro:<id>:usuario:<id>).",
    )
    creada_en = models.DateTimeField(auto_now_add=True, verbose_name="creada en")

    class Meta:
        verbose_name = "transacción de moneda"
        verbose_name_plural = "transacciones de moneda"
        ordering = ["-creada_en"]
        indexes = [
            models.Index(fields=["usuario", "creada_en"], name="gamif_tx_usuario_fecha_idx"),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "tipo", "referencia"],
                condition=~Q(referencia=""),
                name="gamif_tx_ref_unica",
            )
        ]

    def __str__(self) -> str:
        return f"{self.get_tipo_display()} {self.monto} — {self.usuario}"


class Mision(models.Model):
    """Misión/motivación periódica (Fase 5)."""

    TIPOS = [
        ("diaria", "Diaria"),
        ("semanal", "Semanal"),
        ("hito", "Hito"),
    ]

    clave = models.SlugField(max_length=80, unique=True, verbose_name="clave")
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    tipo = models.CharField(max_length=20, choices=TIPOS, default="hito", verbose_name="tipo")
    objetivo = models.PositiveIntegerField(default=1, verbose_name="objetivo (contador)")
    condicion = models.CharField(max_length=120, blank=True, verbose_name="condición/evento")
    recompensa_monedas = models.PositiveIntegerField(default=0, verbose_name="recompensa en monedas")
    activo = models.BooleanField(default=True, verbose_name="activo")

    class Meta:
        verbose_name = "misión"
        verbose_name_plural = "misiones"
        ordering = ["tipo", "nombre"]

    def __str__(self) -> str:
        return self.nombre


class MisionProgreso(models.Model):
    """Progreso de una misión por usuario (idempotente al completar)."""

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="misiones_progreso",
        verbose_name="usuario",
    )
    mision = models.ForeignKey(
        Mision,
        on_delete=models.CASCADE,
        related_name="progresos",
        verbose_name="misión",
    )
    progreso = models.PositiveIntegerField(default=0, verbose_name="progreso")
    completada = models.BooleanField(default=False, verbose_name="completada")
    completada_en = models.DateTimeField(null=True, blank=True, verbose_name="completada en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "progreso de misión"
        verbose_name_plural = "progresos de misión"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "mision"],
                name="mision_unica_por_usuario",
            )
        ]

    def __str__(self) -> str:
        return f"{self.mision} — {self.usuario} ({self.progreso}/{self.mision.objetivo})"


class ItemInventario(models.Model):
    """Objeto de inventario otorgado al usuario."""

    RAREZAS = [
        ("cobre", "Cobre"),
        ("plata", "Plata"),
        ("oro", "Oro"),
        ("diamante", "Diamante"),
        ("legendario", "Legendario"),
        ("arcano", "Arcano"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventario_items",
        verbose_name="usuario",
    )
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    rareza = models.CharField(max_length=20, choices=RAREZAS, verbose_name="rareza")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    origen = models.CharField(
        max_length=120, blank=True, verbose_name="origen del otorgamiento"
    )
    cantidad = models.PositiveIntegerField(default=1, verbose_name="cantidad")
    obtenido_en = models.DateTimeField(default=timezone.now, verbose_name="obtenido en")

    class Meta:
        verbose_name = "ítem de inventario"
        verbose_name_plural = "ítems de inventario"
        ordering = ["-obtenido_en"]

    def __str__(self) -> str:
        return f"{self.nombre} ({self.get_rareza_display()}) — {self.usuario}"
# append to apps/gamification/models.py

class ZonaMundo(models.Model):
    """Zona/mundo narrativo asociado a una etapa académica (Fase 6)."""

    etapa = models.OneToOneField(
        "roadmaps.Etapa",
        on_delete=models.CASCADE,
        related_name="zona_mundo",
        verbose_name="etapa",
    )
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    orden = models.PositiveIntegerField(default=0, verbose_name="orden")
    activo = models.BooleanField(default=True, verbose_name="activo")

    class Meta:
        verbose_name = "zona del mundo"
        verbose_name_plural = "zonas del mundo"
        ordering = ["orden", "etapa__numero"]

    def __str__(self) -> str:
        return f"{self.nombre} (Etapa {self.etapa.numero})"


class PersonajeGuia(models.Model):
    """Personaje guía asociado a una zona/etapa (Fase 6)."""

    zona = models.ForeignKey(
        ZonaMundo,
        on_delete=models.CASCADE,
        related_name="personajes_guia",
        verbose_name="zona",
    )
    nombre = models.CharField(max_length=120, verbose_name="nombre")
    rol = models.CharField(max_length=120, blank=True, verbose_name="rol")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    activo = models.BooleanField(default=True, verbose_name="activo")

    class Meta:
        verbose_name = "personaje guía"
        verbose_name_plural = "personajes guía"
        ordering = ["zona__orden", "nombre"]

    def __str__(self) -> str:
        return f"{self.nombre} — {self.zona}"


class AvatarPerfil(models.Model):
    """Avatar personalizable del usuario (cosmético/narrativo, Fase 6)."""

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="avatar_perfil",
        verbose_name="usuario",
    )
    nombre_avatar = models.CharField(max_length=80, blank=True, verbose_name="nombre del avatar")
    especie = models.CharField(max_length=60, blank=True, verbose_name="especie")
    clase = models.CharField(max_length=60, blank=True, verbose_name="clase")
    apariencia = models.JSONField(default=dict, blank=True, verbose_name="apariencia (cosmética)")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="creado en")
    actualizado_en = models.DateTimeField(auto_now=True, verbose_name="actualizado en")

    class Meta:
        verbose_name = "avatar del usuario"
        verbose_name_plural = "avatares de usuario"

    def __str__(self) -> str:
        return f"Avatar — {self.usuario}"


class DecisionEvolutiva(models.Model):
    """Registro de decisión evolutiva cosmética/narrativa (Fase 6)."""

    avatar = models.ForeignKey(
        AvatarPerfil,
        on_delete=models.CASCADE,
        related_name="decisiones_evolutivas",
        verbose_name="avatar",
    )
    clave = models.CharField(max_length=80, verbose_name="clave de decisión")
    valor = models.CharField(max_length=120, verbose_name="valor elegido")
    descripcion = models.TextField(blank=True, verbose_name="descripción")
    registrada_en = models.DateTimeField(auto_now_add=True, verbose_name="registrada en")

    class Meta:
        verbose_name = "decisión evolutiva"
        verbose_name_plural = "decisiones evolutivas"
        ordering = ["-registrada_en"]

    def __str__(self) -> str:
        return f"{self.avatar} — {self.clave}: {self.valor}"
