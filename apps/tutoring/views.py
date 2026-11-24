"""Vistas del tutor inteligente local (Fase 3).

Expone un API JSON local para:
- Consultar disponibilidad del tutor IA (Ollama local).
- Iniciar una sesión de tutoría para un ejercicio.
- Entregar una pista respetando el límite de 3 por ejercicio.
- Analizar un intento con el tutor (sin decidir la aprobación académica).

Todas las vistas requieren acceso (``requiere_acceso``) y las de escritura
usan ``@require_POST``. No se ejecuta código del estudiante; solo se analiza
texto y se consulta el validador determinista existente.
"""

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from apps.accounts.identity import get_usuario_actual, requiere_acceso
from apps.roadmaps.models import EjercicioLeccion, IntentoEjercicio
from apps.roadmaps.services import etapas_completadas, roadmap_activo

from . import services
from .models import SesionTutoria


def _sin_propietario() -> JsonResponse:
    """Respuesta genérica cuando no hay propietario local ni usuario autenticado."""
    return JsonResponse(
        {
            "exito": False,
            "error": "No hay un propietario local configurado. No se puede guardar la tutoría.",
        },
        status=403,
    )


def _obtener_ejercicio_desbloqueado(usuario, ejercicio_id):
    """Limita el tutor al roadmap activo y a etapas con prerrequisitos satisfechos."""
    roadmap = roadmap_activo()
    if roadmap is None:
        return None, JsonResponse(
            {"exito": False, "error": "No hay un roadmap activo disponible."},
            status=503,
        )
    ejercicio = get_object_or_404(
        EjercicioLeccion.objects.select_related("leccion__modulo__etapa__roadmap"),
        pk=ejercicio_id,
        publicado=True,
        leccion__modulo__etapa__roadmap=roadmap,
    )
    etapa = ejercicio.leccion.modulo.etapa
    if etapa.esta_bloqueada_para(etapas_completadas(usuario, roadmap)):
        return None, JsonResponse(
            {
                "exito": False,
                "error": "El ejercicio está bloqueado hasta completar los prerrequisitos de la etapa.",
            },
            status=403,
        )
    return ejercicio, None



@requiere_acceso
def tutoria_estado(request):
    """Devuelve el estado operativo del tutor IA."""
    estado = services.estado_tutor()
    return JsonResponse(
        {
            **estado,
            "limite_pistas": services.LIMITE_PISTAS_TUTORIA,
        }
    )


@requiere_acceso
@require_POST
def tutoria_iniciar(request, ejercicio_id):
    """Crea (o recupera) la sesión de tutoría para el ejercicio indicado."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return _sin_propietario()

    ejercicio, error = _obtener_ejercicio_desbloqueado(usuario, ejercicio_id)
    if error is not None:
        return error
    sesion = SesionTutoria.objects.get_or_create(usuario=usuario, ejercicio=ejercicio)[0]

    return JsonResponse(
        {
            "exito": True,
            "sesion_id": sesion.pk,
            "pistas_disponibles": sesion.pistas_disponibles,
            "limite_pistas": services.LIMITE_PISTAS_TUTORIA,
        }
    )


@requiere_acceso
@require_POST
def tutoria_pista(request, ejercicio_id):
    """Entrega una pista al estudiante para un ejercicio."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return _sin_propietario()

    ejercicio, error = _obtener_ejercicio_desbloqueado(usuario, ejercicio_id)
    if error is not None:
        return error
    tipo_pista = request.POST.get("tipo") or "orientacion"
    if tipo_pista not in services.TIPOS_PISTA:
        return JsonResponse(
            {"exito": False, "error": f"Tipo de pista no válido. Opciones: {list(services.TIPOS_PISTA)}."},
            status=400,
        )

    resultado = services.entregar_pista(usuario, ejercicio, tipo_pista=tipo_pista)
    status_code = 200 if resultado.get("exito") else 409
    return JsonResponse(resultado, status=status_code)


@requiere_acceso
@require_POST
def tutoria_analizar(request, ejercicio_id):
    """Analiza un intento de ejercicio con el tutor IA."""
    usuario = get_usuario_actual(request)
    if usuario is None:
        return _sin_propietario()

    ejercicio, error = _obtener_ejercicio_desbloqueado(usuario, ejercicio_id)
    if error is not None:
        return error
    intento_id = request.POST.get("intento_ejercicio_id")
    if not intento_id:
        return JsonResponse(
            {"exito": False, "error": "Debe indicar el identificador del intento."},
            status=400,
        )

    intento = get_object_or_404(
        IntentoEjercicio, pk=intento_id, ejercicio=ejercicio, usuario=usuario
    )
    analisis = services.analizar_intento(usuario, ejercicio, intento)

    return JsonResponse(
        {
            "exito": True,
            "intento_tutoria_id": analisis.pk,
            "resultado_evaluacion": analisis.resultado_evaluacion,
            "analisis_tutor": analisis.analisis_tutor,
        }
    )
