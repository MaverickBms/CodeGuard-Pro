"""Vistas de gamificación (Fase 5): perfil, logros e historial."""

from django.shortcuts import render

from apps.accounts.identity import get_usuario_actual, requiere_acceso

from .models import ItemInventario, LogroObtenido, TransaccionMoneda
from .services import obtener_perfil


@requiere_acceso
def perfil(request):
    """Perfil de gamificación del usuario local."""
    usuario = get_usuario_actual(request)
    perfil_obj = obtener_perfil(usuario) if usuario is not None else None
    logros = []
    transacciones = []
    inventario = []
    if usuario is not None:
        logros = list(
            LogroObtenido.objects.filter(usuario=usuario)
            .select_related("logro")
            .order_by("-obtenido_en")[:20]
        )
        transacciones = list(
            TransaccionMoneda.objects.filter(usuario=usuario).order_by("-creada_en")[:20]
        )
        inventario = list(
            ItemInventario.objects.filter(usuario=usuario).order_by("-obtenido_en")[:20]
        )

    return render(
        request,
        "gamification/perfil.html",
        {
            "perfil_gamificacion": perfil_obj,
            "logros_obtenidos": logros,
            "transacciones": transacciones,
            "inventario": inventario,
        },
    )
