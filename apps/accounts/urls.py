"""URLs del módulo de identidad y acceso.

Endpoints:
- ``accounts/setup/``: configuración inicial (primer uso).
- ``accounts/login/``: inicio de sesión con contraseña maestra.
- ``accounts/logout/``: cierre de sesión.
- ``accounts/rescate/``: recuperación mediante frase de rescate.
- ``accounts/rescate/exito/``: resultado de la validación de frase.
- ``accounts/cambiar-contraseña/``: cambio autenticado de contraseña.
- ``accounts/panel/``: redirección al panel (protegido).
"""

from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("panel/", views.panel_redirect, name="panel"),
    path("setup/", views.setup_inicial, name="setup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path("rescate/", views.rescate, name="rescate"),
    path("rescate/exito/", views.rescate_exito, name="rescate_exito"),
    path("cambiar-contraseña/", views.cambiar_contraseña, name="cambiar_contraseña"),
]
