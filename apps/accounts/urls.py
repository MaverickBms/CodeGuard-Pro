"""URLs del módulo de identidad y acceso.

Nota: Aplicación local, monousuario y offline-first. Sin rutas de
autenticación por ahora.
"""

from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("panel/", views.panel_redirect, name="panel"),
]