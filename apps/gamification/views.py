"""Vistas de gamificación (Fases 5-6): perfil, logros, avatar y mundo."""

from types import SimpleNamespace

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from apps.accounts.identity import get_usuario_actual, requiere_acceso
from apps.roadmaps.models import Etapa
from apps.roadmaps.services import etapas_completadas, roadmap_activo

from .models import ItemInventario, Logro, LogroObtenido, TransaccionMoneda, ZonaMundo
from .services import obtener_avatar, obtener_perfil


@requiere_acceso
def perfil(request):
    """Perfil de gamificación, avatar y progreso en el mundo (local)."""
    usuario = get_usuario_actual(request)
    perfil_obj = obtener_perfil(usuario) if usuario is not None else None
    avatar = obtener_avatar(usuario) if usuario is not None else None

    logros_obtenidos = []
    logros_todos = []
    ids_obtenidos = set()
    transacciones = []
    inventario = []
    zonas_mundo = []
    completadas_nums = set()

    if usuario is not None:
        logros_obtenidos = list(
            LogroObtenido.objects.filter(usuario=usuario)
            .select_related("logro")
            .order_by("-obtenido_en")
        )
        ids_obtenidos = {lo.logro_id for lo in logros_obtenidos}
        logros_todos = list(Logro.objects.filter(activo=True).order_by("nombre"))
        transacciones = list(
            TransaccionMoneda.objects.filter(usuario=usuario).order_by("-creada_en")[:20]
        )
        inventario = list(
            ItemInventario.objects.filter(usuario=usuario).order_by("-obtenido_en")[:20]
        )

        roadmap = roadmap_activo()
        if roadmap is not None:
            completadas_nums = etapas_completadas(usuario, roadmap)
            zonas = list(
                ZonaMundo.objects.filter(activo=True, etapa__roadmap=roadmap)
                .select_related("etapa")
                .prefetch_related("personajes_guia")
                .order_by("orden", "etapa__numero")
            )
            if zonas:
                for zona in zonas:
                    zona.completada = zona.etapa.numero in completadas_nums
                    zona.bloqueada = zona.etapa.esta_bloqueada_para(completadas_nums)
                    zona.personajes_lista = list(zona.personajes_guia.all())
                zonas_mundo = zonas
            else:
                # Vista narrativa basada en etapas reales (sin zonas configuradas)
                etapas = list(
                    roadmap.etapas.order_by("orden", "numero").prefetch_related(
                        "prerrequisitos__etapa_requerida"
                    )
                )
                zonas_mundo = [
                    SimpleNamespace(
                        nombre=f"Zona {e.numero}: {e.titulo}",
                        etapa=e,
                        completada=e.numero in completadas_nums,
                        bloqueada=e.esta_bloqueada_para(completadas_nums),
                        personajes_lista=[],
                    )
                    for e in etapas
                ]

    for logro in logros_todos:
        logro.obtenido = logro.id in ids_obtenidos

    return render(
        request,
        "gamification/perfil.html",
        {
            "perfil_gamificacion": perfil_obj,
            "avatar": avatar,
            "logros_obtenidos": logros_obtenidos[:20],
            "logros_todos": logros_todos,
            "transacciones": transacciones,
            "inventario": inventario,
            "zonas_mundo": zonas_mundo,
        },
    )


@requiere_acceso
@require_POST
def guardar_avatar(request):
    """Actualiza datos cosméticos del avatar (sin ventajas académicas)."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        messages.error(request, "No hay un propietario local configurado.")
        return redirect("gamification:perfil")

    avatar = obtener_avatar(usuario)
    if avatar is None:
        messages.error(request, "No se pudo obtener el avatar.")
        return redirect("gamification:perfil")

    avatar.nombre_avatar = (request.POST.get("nombre_avatar") or "").strip()[:80]
    avatar.especie = (request.POST.get("especie") or "").strip()[:60]
    avatar.clase = (request.POST.get("clase") or "").strip()[:60]
    avatar.save(update_fields=["nombre_avatar", "especie", "clase", "actualizado_en"])
    messages.success(request, "Avatar actualizado.")
    return redirect("gamification:perfil")
