"""Vistas del módulo de identidad y acceso.

Nota: Este proyecto es una aplicación local, monousuario y offline-first.
Por ahora no se implementa sistema de inicio de sesión. Cuando el proyecto
avance y se agregue conectividad a internet, se reimplementará la
autenticación completa.

Endpoints disponibles:
- Ninguno por ahora (la aplicación abre directamente al panel).
"""

from django.shortcuts import redirect
from django.urls import reverse_lazy


def panel_redirect(request):
    """Redirige al panel principal."""
    return redirect("core:panel")