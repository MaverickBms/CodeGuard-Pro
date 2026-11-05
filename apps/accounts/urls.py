"""URLs del módulo de identidad y acceso."""

from django.urls import path

from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path("setup/", views.setup_inicial, name="setup_inicial"),
    path("setup/exito/", views.setup_exito, name="setup_exito"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("panel/", views.panel_redirect, name="panel"),
    path("password/", views.CambiarContraseñaView.as_view(), name="cambiar_contraseña"),
    path("rescate/", views.validar_frase_rescate_view, name="rescate"),
]
