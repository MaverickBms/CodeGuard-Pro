"""Vistas del módulo core (panel principal y navegación)."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.audit.services import registrar_evento
from apps.core.models import ConfiguracionSistema
from apps.roadmaps.models import Etapa, Progreso, Roadmap
from apps.roadmaps.services import (
    etapas_completadas,
    progreso_general,
    roadmap_activo,
)


def get_usuario_actual(request):
    """Devuelve el usuario autenticado de la petición.

    No existe creación implícita de usuarios: la identidad proviene del flujo
    de autenticación (configuración inicial / inicio de sesión). Ver CG-003.
    """
    return request.user


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


@login_required
def panel(request):
    """Panel principal (dashboard).

    Muestra el progreso general, etapas completadas, lecciones completadas,
    próxima etapa disponible y actividad reciente. Todos los datos provienen
    de la base de datos; no se inventan porcentajes ni estadísticas.
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
        usuario=usuario,
        descripcion="Acceso al panel principal.",
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
