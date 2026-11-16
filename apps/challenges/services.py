"""Servicios base para desafíos/minijuegos (Fase 7)."""

from __future__ import annotations

from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Desafio, ResultadoDesafio


@transaction.atomic
def registrar_resultado_desafio(
    usuario,
    desafio: Desafio,
    *,
    puntuacion: int | None = None,
    completado: bool = False,
    tiempo_segundos: int | None = None,
    datos_rendimiento: dict | None = None,
    conceptos_practicados: list | None = None,
    retroalimentacion: str = "",
) -> ResultadoDesafio:
    """Registra evidencia de un intento/resultado de desafío.

    No sustituye exámenes formales; recompensas deben gestionarse de forma
    idempotente por evento si se integran.
    """
    if usuario is None or not getattr(usuario, "is_authenticated", False):
        raise ValidationError("Se requiere un usuario autenticado.")
    if datos_rendimiento is None:
        datos_rendimiento = {}
    if conceptos_practicados is None:
        conceptos_practicados = []

    resultado = ResultadoDesafio.objects.create(
        desafio=desafio,
        usuario=usuario,
        puntuacion=puntuacion,
        completado=bool(completado),
        tiempo_segundos=tiempo_segundos,
        datos_rendimiento=datos_rendimiento,
        conceptos_practicados=conceptos_practicados,
        retroalimentacion=retroalimentacion or "",
    )
    return resultado
