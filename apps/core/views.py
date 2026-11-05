"""Vistas del módulo core (panel principal y navegación)."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.audit.services import registrar_evento
from apps.core.models import ConfiguracionSistema


@login_required
def panel(request):
    """Panel principal protegido (dashboard).

    Muestra el progreso general, etapas, competencias, actividades pendientes,
    evaluaciones, laboratorios, documentos, evidencias y revisiones pendientes.
    En este primer incremento es un esqueleto funcional que enumera los módulos
    disponibles del MVP.
    """
    configuracion = ConfiguracionSistema.cargar()

    modulos = [
        {
            "titulo": "Roadmap académico",
            "descripcion": "33 etapas ASCENSO, módulos, lecciones y actividades.",
            "url": "roadmaps:lista",
            "icono": "🗺️",
            "implementado": False,
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
    ]

    registrar_evento(
        "acceso_panel",
        usuario=request.user,
        descripcion="Acceso al panel principal.",
    )

    return render(
        request,
        "core/panel.html",
        {
            "configuracion": configuracion,
            "modulos": modulos,
        },
    )
