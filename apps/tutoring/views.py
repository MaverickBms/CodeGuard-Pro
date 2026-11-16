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

from . import services
from .models import SesionTutoria


def _sin_propietario() -> JsonResponse:
    """Respuesta genérica cuando no hay propietario local ni usuario autenticado."""
    return JsonResponse(
        {
            "exito": False,
            "error": "No hay un propietario local configurado. No se puede guardar el tutoría.",
        },
        status=403,
    )


@requiere_acceso
def tutoria_estado(request):
    """Devuelve el estado operativo del tutor IA."""
    return JsonResponse(
        {
            "disponible": services.esta_disponible(),
            "modelo": services.TUTOR_MODEL,
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

    ejercicio = get_object_or_404(EjercicioLeccion, pk=ejercicio_id, publicado=True)
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

    ejercicio = get_object_or_404(EjercicioLeccion, pk=ejercicio_id, publicado=True)
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

    ejercicio = get_object_or_404(EjercicioLeccion, pk=ejercicio_id, publicado=True)
    intento_id = request.POST.get("intento_ejercicio_id")
    if not intento_id:
        return JsonResponse(
            {"exito": False, "error": "Debe indicar el identificador del intento."},
            status=400,
        )

    intento = get_object_or_404(
        IntentoEjercicio, pk=intento_id, ejercicio=ejercicio
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
