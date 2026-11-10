"""Vistas del módulo core (panel principal y navegación)."""

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.accounts.identity import obtener_actor_auditoria, obtener_usuario_local, requiere_acceso
from apps.audit.services import registrar_evento
from apps.core.models import ConfiguracionSistema
from apps.roadmaps.models import Etapa, Progreso, Roadmap
from apps.roadmaps.services import (
    etapas_completadas,
    progreso_general,
    roadmap_activo,
)


def get_usuario_actual(request):
    """Devuelve el usuario activo para operaciones de progreso.

    En modo sin autenticación devuelve el propietario local existente
    (``request.usuario_local``). Cuando la autenticación está activa devuelve
    el usuario autenticado de la petición.

    Si no existe propietario local ni usuario autenticado, devuelve None.
    Las vistas deben manejar este caso: lectura permitida, escritura bloqueada
    con mensaje comprensible. No se crea ningún usuario implícitamente.
    """
    usuario_local = getattr(request, "usuario_local", None)
    if usuario_local is not None:
        return usuario_local
    if request.user.is_authenticated:
        return request.user
    return None


def _progreso_reciente(usuario, limite=5):
    """Devuelve los progresos más recientes del usuario (actividad reciente)."""
    return (
        Progreso.objects.filter(usuario=usuario)
        .select_related("etapa", "leccion", "modulo")
        .order_by("-fecha_actualizacion")[:limite]
    )


def _etapa_siguiente(usuario, roadmap):
    """Devuelve la primera etapa no bloqueada y no completada, o None."""
    completadas = etapas_completadas(usuario, roadmap)
    etapas = (
        roadmap.etapas.all()
        .order_by("orden", "numero")
        .prefetch_related("prerrequisitos__etapa_requerida")
    )
    for etapa in etapas:
        if etapa.numero in completadas:
            continue
        if not etapa.esta_bloqueada_para(completadas):
            return etapa
    return None


@requiere_acceso
def panel(request):
    """Panel principal (dashboard).

    Muestra el progreso general, etapas completadas, lecciones completadas,
    próxima etapa disponible y actividad reciente. Todos los datos provienen
    de la base de datos; no se inventan porcentajes ni estadísticas.

    En modo sin autenticación no se solicitan credenciales y se usa el
    propietario local existente para asociar el progreso. La auditoría
    registra actor nulo (usuario=None).
    """
    usuario = get_usuario_actual(request)
    configuracion = ConfiguracionSistema.cargar()
    roadmap = roadmap_activo()

    avance = None
    etapas_completadas_set = set()
    lecciones_completadas = 0
    modulos_completados = 0
    proxima_etapa = None
    actividad_reciente = []
    roadmap_existe = roadmap is not None

    if roadmap_existe:
        avance = progreso_general(usuario, roadmap)
        etapas_completadas_set = etapas_completadas(usuario, roadmap)

        # Lecciones y módulos completados (filtrados por el roadmap activo).
        progresos = Progreso.objects.filter(usuario=usuario, etapa__roadmap=roadmap)
        lecciones_completadas = progresos.filter(
            leccion__isnull=False, estado="completado"
        ).count()
        modulos_completados = progresos.filter(
            modulo__isnull=False, leccion__isnull=True, estado="completado"
        ).count()

        proxima_etapa = _etapa_siguiente(usuario, roadmap)

        # Próxima actividad: primera etapa no completada del roadmap.
        proxima_actividad = (
            Progreso.objects.filter(
                usuario=usuario,
                etapa__roadmap=roadmap,
                estado__in=["no_iniciado", "en_progreso"],
            )
            .select_related("etapa", "leccion", "modulo")
            .order_by("etapa__numero", "fecha_inicio")
            .first()
        )
    else:
        proxima_actividad = None

    actividad_reciente = _progreso_reciente(usuario)

    registrar_evento(
        "acceso_panel",
        usuario=obtener_actor_auditoria(request),
        descripcion="Acceso al panel principal.",
    )

    # Tiempo de sesión por inactividad (solo informativo en modo sin autenticación).
    sesion_timeout_minutos = (
        getattr(usuario, "sesion_timeout_minutos", None)
        or getattr(settings, "SESSION_TIMEOUT_MINUTES", 15)
    )

    return render(
        request,
        "core/panel.html",
        {
            "configuracion": configuracion,
            "modulos": [
                {
                    "titulo": "Roadmap académico",
                    "descripcion": "33 etapas ASCENSO, módulos, lecciones y actividades.",
                    "url": "roadmaps:lista",
                    "icono": "🗺️",
                    "implementado": True,
                },
                {
                    "titulo": "Competencias",
                    "descripcion": "Registro de competencias, niveles y criterios.",
                    "url": "competencies:lista",
                    "icono": "🏅",
                    "implementado": False,
                },
                {
                    "titulo": "Biblioteca documental",
                    "descripcion": "Importación y gestión de PDFs.",
                    "url": "library:lista",
                    "icono": "📚",
                    "implementado": False,
                },
                {
                    "titulo": "Base de conocimiento",
                    "descripcion": "Conceptos, relaciones y trazabilidad documental.",
                    "url": "knowledge:lista",
                    "icono": "🧠",
                    "implementado": False,
                },
                {
                    "titulo": "Evaluaciones",
                    "descripcion": "Preguntas, rúbricas, intentos y resultados.",
                    "url": "assessments:lista",
                    "icono": "📝",
                    "implementado": False,
                },
                {
                    "titulo": "Evidencias",
                    "descripcion": "Portafolio por etapa y competencia.",
                    "url": "evidence:lista",
                    "icono": "📎",
                    "implementado": False,
                },
                {
                    "titulo": "Laboratorios",
                    "descripcion": "Guías, pasos y registro de resultados.",
                    "url": "labs:lista",
                    "icono": "🧪",
                    "implementado": False,
                },
                {
                    "titulo": "Administración y backups",
                    "descripcion": "Backup, restauración y auditoría.",
                    "url": "backups:lista",
                    "icono": "💾",
                    "implementado": False,
                },
                {
                    "titulo": "Vigencia y revisión",
                    "descripcion": "Estado de vigencia y revisión manual de contenidos.",
                    "url": "vigencia:lista",
                    "icono": "📅",
                    "implementado": False,
                },
                {
                    "titulo": "Ética y seguridad del aprendizaje",
                    "descripcion": "Advertencias, aceptación explícita y guías de uso ético.",
                    "url": "ethics:lista",
                    "icono": "⚖️",
                    "implementado": False,
                },
            ],
            "user": usuario,
            "usuario_nombre": usuario.get_username() if usuario else "Local",
            "sesion_timeout_minutos": sesion_timeout_minutos,
            "auth_disabled": getattr(settings, "AUTH_DISABLED", False),
            "avance": avance,
            "etapas_completadas": len(etapas_completadas_set),
            "lecciones_completadas": lecciones_completadas,
            "modulos_completados": modulos_completados,
            "proxima_etapa": proxima_etapa,
            "proxima_actividad": proxima_actividad,
            "actividad_reciente": actividad_reciente,
            "roadmap_existe": roadmap_existe,
        },
    )
