"""Vistas del módulo de identidad y acceso.

Flujo local y monousuario:

- Configuración inicial (primer uso): crea usuario y frase de rescate.
- Inicio / cierre de sesión con la contraseña maestra.
- Recuperación de acceso mediante frase de rescate (un solo uso).
- Cambio de contraseña maestra autenticado.

Sin OAuth, proveedores externos o autenticación remota.
"""

from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from apps.accounts.forms import CambiarContraseñaForm, LoginForm, SetupInicialForm
from apps.accounts.services import (
    crear_usuario_inicial,
    validar_frase_rescate,
)
from apps.audit.services import registrar_evento


def panel_redirect(request):
    """Redirige al panel principal (protegido por autenticación)."""
    return redirect("core:panel")


def setup_inicial(request):
    """Configuración inicial (primer uso): crea usuario y frase de rescate.

    Solo debe ejecutarse cuando todavía no existe ningún usuario en la base de
    datos. La contraseña se hashea con Argon2 y la frase de rescate se genera con
    alta entropía (≥128 bits) y se almacena como hash de un solo uso.
    """
    Usuario = get_user_model()

    if Usuario.objects.exists():
        return redirect("accounts:login")

    if request.method == "POST":
        form = SetupInicialForm(request.POST)
        if form.is_valid():
            usuario, frase_rescate = crear_usuario_inicial(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
                ip=request.META.get("REMOTE_ADDR") or None,
                user_agent=request.META.get("HTTP_USER_AGENT", "")[:512],
            )
            return render(request, "accounts/setup_exito.html", {"frase_rescate": frase_rescate})

    form = SetupInicialForm()
    return render(request, "accounts/setup_inicial.html", {"form": form})


class LoginView(auth_views.LoginView):
    """Inicio de sesión con la contraseña maestra (Argon2)."""

    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        """Redirige al panel principal tras un inicio de sesión exitoso."""
        return reverse("core:panel")

    def form_valid(self, form):
        usuario = form.get_user()
        login(self.request, usuario)
        registrar_evento(
            "login_exitoso",
            usuario=usuario,
            descripcion="Inicio de sesión exitoso.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        username = form.cleaned_data.get("username") if form.cleaned_data else ""
        registrar_evento(
            "login_fallido",
            usuario=None,
            descripcion=f"Intento de inicio de sesión fallido para '{username}'.",
        )
        return super().form_invalid(form)


def cerrar_sesion(request):
    """Cierre de sesión manual."""
    usuario = request.user if request.user.is_authenticated else None
    logout(request)
    registrar_evento(
        "logout",
        usuario=usuario,
        descripcion="Cierre de sesión manual.",
    )
    return redirect("core:panel")


def rescate(request):
    """Valida la frase de rescate para recuperar el acceso (un solo uso)."""
    error = False
    usuario = get_user_model().objects.first()
    if request.method == "POST":
        frase = (request.POST.get("frase_rescate") or "").strip()
        if usuario is not None and validar_frase_rescate(usuario, frase):
            return redirect("accounts:rescate_exito")
        error = True
    return render(request, "accounts/rescue.html", {"error": error})


def rescate_exito(request):
    """Página posterior a una frase de rescate válida."""
    return redirect("accounts:login")


@login_required
def cambiar_contraseña(request):
    """Cambio de la contraseña maestra autenticado."""
    if request.method == "POST":
        form = CambiarContraseñaForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            registrar_evento(
                "cambio_contraseña",
                usuario=request.user,
                descripcion="Contraseña maestra cambiada.",
            )
            messages.success(request, "Contraseña maestra actualizada correctamente.")
            return redirect("core:panel")
    else:
        form = CambiarContraseñaForm(request.user)
    return render(request, "accounts/cambiar_contraseña.html", {"form": form})
