"""Vistas del módulo académico (roadmap ASCENSO).

Nota: Aplicación local, monousuario y offline-first. La identidad del usuario
actual proviene del flujo de autenticación; no se crea identidad implícita.
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Etapa, Leccion
from .services import (
    etapas_completadas,
    mapa_progreso_etapas,
    mapa_progreso_lecciones,
    marcar_etapa,
    marcar_leccion,
    progreso_general,
    resumen_roadmap,
    roadmap_activo,
)


def get_usuario_actual(request):
    """Devuelve el usuario autenticado de la petición.

    No existe creación implícita de usuarios: la identidad proviene del flujo
    de autenticación (configuración inicial / inicio de sesión). Ver CG-003.
    """
    return request.user


@login_required
def lista(request):
    """Listado de las 33 etapas con filtros, avance y estado de bloqueo."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)

    etapas = list(
        roadmap.etapas.prefetch_related(
            "prerrequisitos__etapa_requerida", "modulos__lecciones"
        )
    )

    bloque = request.GET.get("bloque", "").strip()
    prioridad = request.GET.get("prioridad", "").strip()
    busqueda = request.GET.get("q", "").strip()

    if bloque:
        etapas = [etapa for etapa in etapas if etapa.bloque == bloque]
    if prioridad:
        etapas = [etapa for etapa in etapas if etapa.prioridad == prioridad]
    if busqueda:
        termino = busqueda.lower()
        etapas = [
            etapa
            for etapa in etapas
            if termino in etapa.titulo.lower()
            or termino in etapa.objetivo.lower()
            or any(
                termino in modulo.titulo.lower()
                or any(termino in leccion.titulo.lower() for leccion in modulo.lecciones.all())
                for modulo in etapa.modulos.all()
            )
        ]

    completadas = etapas_completadas(usuario, roadmap)
    progresos = mapa_progreso_etapas(usuario, roadmap)

    for etapa in etapas:
        etapa.progreso_actual = progresos.get(etapa.id)
        etapa.completada = etapa.numero in completadas
        etapa.bloqueada = etapa.esta_bloqueada_para(completadas)
        etapa.total_lecciones_cache = sum(
            len(modulo.lecciones.all()) for modulo in etapa.modulos.all()
        )

    resumen = resumen_roadmap(roadmap)
    avance = progreso_general(usuario, roadmap)
    bloques = list(
        roadmap.etapas.values_list("bloque", flat=True).distinct().order_by("bloque")
    )

    return render(
        request,
        "roadmaps/lista.html",
        {
            "roadmap": roadmap,
            "etapas": etapas,
            "resumen": resumen,
            "avance": avance,
            "bloques": bloques,
            "bloque_seleccionado": bloque,
            "prioridad_seleccionada": prioridad,
            "busqueda": busqueda,
        },
    )


@login_required
def detalle(request, numero):
    """Detalle de una etapa: módulos, lecciones, proyecto y prerrequisitos."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return render(request, "roadmaps/sin_datos.html")

    usuario = get_usuario_actual(request)

    etapa = get_object_or_404(Etapa, roadmap=roadmap, numero=numero)
    modulos = list(etapa.modulos.prefetch_related("lecciones"))

    completadas = etapas_completadas(usuario, roadmap)
    progreso = mapa_progreso_etapas(usuario, roadmap).get(etapa.id)
    progresos_lecciones = mapa_progreso_lecciones(usuario, etapa)

    for modulo in modulos:
        modulo.lecciones_lista = list(modulo.lecciones.all())
        for leccion in modulo.lecciones_lista:
            leccion.progreso_actual = progresos_lecciones.get(leccion.id)
            leccion.completada = bool(
                leccion.progreso_actual
                and leccion.progreso_actual.estado == "completado"
            )

    return render(
        request,
        "roadmaps/detalle.html",
        {
            "roadmap": roadmap,
            "etapa": etapa,
            "modulos": modulos,
            "progreso": progreso,
            "completada": etapa.numero in completadas,
            "completadas": completadas,
            "bloqueada": etapa.esta_bloqueada_para(completadas),
            "prerrequisitos": etapa.prerrequisitos.select_related("etapa_requerida"),
            "desbloquea": etapa.desbloquea.select_related("etapa"),
            "criterios": etapa.criterios.all(),
        },
    )


@login_required
@require_POST
def marcar_etapa_view(request, numero):
    """Marca o reabre una etapa completa (POST)."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return redirect("roadmaps:lista")

    usuario = get_usuario_actual(request)

    etapa = get_object_or_404(Etapa, roadmap=roadmap, numero=numero)
    completada = request.POST.get("completada") == "1"

    try:
        marcar_etapa(usuario, etapa, completada=completada)
    except ValueError as exc:
        messages.error(request, str(exc))
    else:
        if completada:
            messages.success(request, f"Etapa {etapa.numero} marcada como completada.")
        else:
            messages.info(request, f"Etapa {etapa.numero} reabierta.")

    return redirect("roadmaps:detalle", numero=etapa.numero)


@login_required
@require_POST
def marcar_leccion_view(request, leccion_id):
    """Marca o desmarca una lección (POST)."""
    usuario = get_usuario_actual(request)

    leccion = get_object_or_404(
        Leccion.objects.select_related("modulo__etapa"), pk=leccion_id
    )
    completada = request.POST.get("completada") == "1"
    marcar_leccion(usuario, leccion, completada=completada)

    if completada:
        messages.success(request, f"Lección completada: {leccion.titulo}")
    else:
        messages.info(request, f"Lección reabierta: {leccion.titulo}")

    return redirect("roadmaps:detalle", numero=leccion.modulo.etapa.numero)