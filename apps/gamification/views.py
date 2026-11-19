"""Vistas de gamificación (Fases 5-6): perfil, logros, avatar y mundo."""

from types import SimpleNamespace

import json

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.accounts.identity import get_usuario_actual, requiere_acceso
from apps.roadmaps.models import Etapa
from apps.roadmaps.services import etapas_completadas, roadmap_activo

from .models import (
    EstadoMundo,
    ItemInventario,
    Logro,
    LogroObtenido,
    Mision,
    MisionProgreso,
    TransaccionMoneda,
    ZonaMundo,
)
from .mundo import (
    completar_mision,
    contexto_academico,
    guardar_posicion,
    interactuar,
    obtener_estado,
    serializar_estado,
)
from .services import asegurar_misiones_defecto, obtener_avatar, obtener_perfil


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
    misiones = []

    if usuario is not None:
        asegurar_misiones_defecto()
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
        misiones = list(Mision.objects.filter(activo=True).order_by("tipo", "nombre"))
        progresos_m = {
            mp.mision_id: mp
            for mp in MisionProgreso.objects.filter(usuario=usuario, mision__in=misiones)
        }
        for m in misiones:
            m.progreso_usuario = progresos_m.get(m.id)

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
            "misiones": misiones,
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


# --- Mundo CodeGuard -------------------------------------------------------

def _json_body(request, max_bytes: int = 32_768) -> dict:
    """Lee un cuerpo JSON pequeño y devuelve un error de validación uniforme."""
    if len(request.body) > max_bytes:
        raise ValidationError("La solicitud es demasiado grande.")
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError("La solicitud no contiene JSON válido.") from exc
    if not isinstance(payload, dict):
        raise ValidationError("La solicitud debe ser un objeto JSON.")
    return payload


def _error_json(exc: ValidationError, status: int = 400) -> JsonResponse:
    mensaje = exc.messages[0] if getattr(exc, "messages", None) else str(exc)
    return JsonResponse({"error": mensaje}, status=status)


@requiere_acceso
def mundo(request):
    """Vista del Mundo CodeGuard con la región piloto integrada."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        estado = EstadoMundo()
        puede_guardar = False
    else:
        estado = obtener_estado(usuario)
        puede_guardar = True
    configuracion = serializar_estado(estado)
    configuracion["academico"] = contexto_academico(usuario)
    configuracion["endpoints"] = {
        "guardar": reverse("gamification:guardar_mundo"),
        "interactuar": reverse("gamification:interactuar_mundo"),
        "mision": reverse("gamification:completar_mision_mundo"),
    }
    return render(
        request,
        "gamification/mundo.html",
        {
            "mundo_config": configuracion,
            "puede_guardar": puede_guardar,
            "usuario_nombre": usuario.get_username() if usuario else "Visitante local",
        },
    )


@requiere_acceso
@require_POST
def guardar_mundo(request):
    """Persiste posición y preferencias; nunca misiones ni inventario."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return JsonResponse({"error": "No hay propietario local configurado."}, status=403)
    try:
        payload = _json_body(request)
        estado = obtener_estado(usuario)
        estado = guardar_posicion(
            estado,
            region=payload.get("region", estado.region),
            x=payload.get("x"),
            y=payload.get("y"),
            direccion=payload.get("direccion"),
            tiempo_jugado=payload.get("tiempo_jugado", estado.tiempo_jugado),
            audio_silenciado=payload.get("audio_silenciado", estado.audio_silenciado),
        )
    except ValidationError as exc:
        return _error_json(exc)
    return JsonResponse({"ok": True, "estado": serializar_estado(estado)})


@requiere_acceso
@require_POST
def interactuar_mundo(request):
    """Registra una interacción conocida del mapa."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return JsonResponse({"error": "No hay propietario local configurado."}, status=403)
    try:
        payload = _json_body(request)
        objeto = payload.get("objeto")
        if not isinstance(objeto, str):
            raise ValidationError("El objeto interactivo no es válido.")
        estado = obtener_estado(usuario)
        resultado = interactuar(estado, objeto)
    except ValidationError as exc:
        return _error_json(exc)
    return JsonResponse(
        {"ok": True, "interaccion": resultado, "estado": serializar_estado(estado)}
    )


@requiere_acceso
@require_POST
def completar_mision_mundo(request):
    """Valida y completa una misión del mundo con recompensa idempotente."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return JsonResponse({"error": "No hay propietario local configurado."}, status=403)
    try:
        payload = _json_body(request)
        mision_id = payload.get("mision")
        if not isinstance(mision_id, str):
            raise ValidationError("La misión no es válida.")
        estado = obtener_estado(usuario)
        estado, creada, resultado = completar_mision(
            estado, mision_id, payload.get("respuestas")
        )
    except ValidationError as exc:
        return _error_json(exc)
    return JsonResponse(
        {
            "ok": True,
            "creada": creada,
            "resultado": resultado,
            "estado": serializar_estado(estado),
        }
    )
