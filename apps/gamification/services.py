"""Servicios de gamificación y economía de recompensas (Fase 5).

Operaciones atómicas, consistentes y no duplicables. Las recompensas no
alteran resultados académicos ni aprobaciones.
"""

from __future__ import annotations

from django.db import transaction
from django.db.models import F

from .models import Logro, LogroObtenido, PerfilGamificacion, TransaccionMoneda


def obtener_perfil(usuario) -> PerfilGamificacion:
    perfil, _ = PerfilGamificacion.objects.get_or_create(usuario=usuario)
    return perfil


@transaction.atomic
def acreditar_monedas(usuario, monto: int, concepto: str, referencia: str = "") -> TransaccionMoneda:
    """Acredita monedas al usuario de forma atómica y registra la transacción."""
    if monto <= 0:
        raise ValueError("El monto a acreditar debe ser mayor que cero.")

    if referencia:
        existente = TransaccionMoneda.objects.select_for_update().filter(
            usuario=usuario, referencia=referencia, tipo="credito"
        ).first()
        if existente:
            return existente

    perfil = PerfilGamificacion.objects.select_for_update().get_or_create(usuario=usuario)[0]
    perfil.saldo_monedas = F("saldo_monedas") + int(monto)
    perfil.save(update_fields=["saldo_monedas", "actualizado_en"])
    perfil.refresh_from_db(fields=["saldo_monedas"])

    return TransaccionMoneda.objects.create(
        usuario=usuario,
        tipo="credito",
        monto=int(monto),
        saldo_resultante=perfil.saldo_monedas,
        concepto=concepto[:160],
        referencia=referencia[:120],
    )


@transaction.atomic
def otorgar_logro(usuario, logro: Logro, origen: str = "") -> tuple[LogroObtenido, bool]:
    """Otorga un logro al usuario si no lo tiene. Devuelve (instancia, creado).

    Si el logro tiene recompensa en monedas, se acredita una sola vez usando
    una referencia idempotente basada en el logro y el usuario.
    """
    obtenido, creado = LogroObtenido.objects.get_or_create(
        usuario=usuario,
        logro=logro,
        defaults={"origen": origen[:120]},
    )
    if creado and logro.recompensa_monedas > 0:
        acreditar_monedas(
            usuario,
            logro.recompensa_monedas,
            concepto=f"Recompensa por logro: {logro.nombre}",
            referencia=f"logro:{logro.id}:usuario:{usuario.id}",
        )
    return obtenido, creado


@transaction.atomic
def recompensar_evento_academico(usuario, evento: str, objeto_id: int, concepto: str, monto: int = 10) -> TransaccionMoneda | None:
    """Otorga monedas por un evento académico de forma idempotente.

    No altera resultados académicos ni aprobaciones.
    """
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        return None
    referencia = f"evento:{evento}:{objeto_id}:usuario:{usuario.id}"
    return acreditar_monedas(usuario, int(monto), concepto, referencia=referencia)


LOGROS_ACADEMICOS_DEFECTO = [
    {"clave": "primer-modulo", "nombre": "Primer módulo completado", "descripcion": "Completaste tu primer módulo por evaluación.", "condicion": "modulos_completados>=1", "recompensa_monedas": 10},
    {"clave": "cinco-modulos", "nombre": "Cinco módulos completados", "descripcion": "Alcanzaste 5 módulos completados.", "condicion": "modulos_completados>=5", "recompensa_monedas": 25},
    {"clave": "primera-etapa", "nombre": "Primera etapa completada", "descripcion": "Completaste tu primera etapa por criterios verificables.", "condicion": "etapas_completadas>=1", "recompensa_monedas": 20},
    {"clave": "tres-etapas", "nombre": "Tres etapas completadas", "descripcion": "Alcanzaste 3 etapas completadas.", "condicion": "etapas_completadas>=3", "recompensa_monedas": 40},
]


def asegurar_logros_academicos_defecto() -> None:
    """Crea logros académicos base si no existen (configurables)."""
    for datos in LOGROS_ACADEMICOS_DEFECTO:
        Logro.objects.get_or_create(clave=datos["clave"], defaults=datos)


def evaluar_logros_academicos(usuario, *, modulos_completados: int | None = None, etapas_completadas: int | None = None) -> list[LogroObtenido]:
    """Evalúa y otorga logros académicos de forma idempotente."""
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        return []

    asegurar_logros_academicos_defecto()

    if modulos_completados is None:
        try:
            from apps.roadmaps.models import Progreso
            modulos_completados = Progreso.objects.filter(
                usuario=usuario, modulo__isnull=False, leccion__isnull=True, actividad__isnull=True, estado="completado"
            ).values("modulo_id").distinct().count()
        except Exception:
            modulos_completados = 0
    if etapas_completadas is None:
        try:
            from apps.roadmaps.models import Progreso
            etapas_completadas = Progreso.objects.filter(
                usuario=usuario, modulo__isnull=True, leccion__isnull=True, actividad__isnull=True, estado="completado"
            ).values("etapa_id").distinct().count()
        except Exception:
            etapas_completadas = 0

    otorgados = []
    reglas = [
        ("primer-modulo", modulos_completados >= 1),
        ("cinco-modulos", modulos_completados >= 5),
        ("primera-etapa", etapas_completadas >= 1),
        ("tres-etapas", etapas_completadas >= 3),
    ]
    for clave, cumple in reglas:
        if not cumple:
            continue
        logro = Logro.objects.filter(clave=clave, activo=True).first()
        if not logro:
            continue
        obtenido, _ = otorgar_logro(usuario, logro, origen="evento_academico")
        otorgados.append(obtenido)
    return otorgados
