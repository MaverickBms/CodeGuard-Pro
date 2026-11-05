"""Vistas del módulo de identidad y acceso.

Endpoints:
- GET/POST /accounts/setup/   -> Configuración inicial (solo si no hay usuario)
- GET/POST /accounts/login/   -> Inicio de sesión
- POST /accounts/logout/      -> Cierre de sesión
- GET  /accounts/rescue/      -> Validación de frase de rescate
- GET  /accounts/password/    -> Cambio de contraseña
"""

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_POST

from apps.accounts.forms import CambiarContraseñaForm, LoginForm, SetupInicialForm
from apps.accounts.services import (
    crear_usuario_inicial,
    validar_frase_rescate,
)
from apps.audit.services import registrar_evento


def _cliente_ip(request) -> str | None:
    xff = request.META.get("HTTP_X_FORWARDED_FOR")
    if xff:
        return xff.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def _registrar_login(request, usuario, exitoso: bool, descripcion: str = "") -> None:
    registrar_evento(
        "login_exitoso" if exitoso else "login_fallido",
        usuario=usuario,
        descripcion=descripcion,
        ip=_cliente_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
    )


def setup_inicial(request):
    """Configuración inicial guiada (CU-001).

    Solo accesible cuando no existe usuario configurado. Crea el usuario, su
    frase de rescate (mostrada una sola vez) y registra la aceptación de
    términos.
    """
    from apps.accounts.models import Usuario

    if Usuario.objects.exists():
        return redirect("accounts:login")

    if request.method == "POST":
        form = SetupInicialForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            try:
                usuario, frase_texto = crear_usuario_inicial(
                    username,
                    password,
                    ip=_cliente_ip(request),
                    user_agent=request.META.get("HTTP_USER_AGENT", ""),
                )
            except RuntimeError:
                return redirect("accounts:login")
            # Guardar la frase en la sesión para mostrarla UNA sola vez.
            request.session["frase_rescate_mostrar"] = frase_texto
            request.session["frase_rescate_usuario_id"] = usuario.pk
            return redirect("accounts:setup_exito")
    else:
        form = SetupInicialForm()

    return render(request, "accounts/setup_inicial.html", {"form": form})


def setup_exito(request):
    """Muestra la frase de rescate una sola vez y limpia la sesión."""
    frase = request.session.pop("frase_rescate_mostrar", None)
    if frase is None:
        return redirect("accounts:login")
    return render(request, "accounts/setup_exito.html", {"frase_rescate": frase})


def login_view(request):
    """Inicio de sesión local con contraseña maestra."""
    if request.user.is_authenticated:
        return redirect("core:panel")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            from django.contrib.auth import login as auth_login

            auth_login(request, usuario)
            request.session.set_expiry(
                usuario.sesion_timeout_minutos * 60
            )
            _registrar_login(request, usuario, True)
            return redirect("core:panel")
        _registrar_login(request, None, False, "Credenciales inválidas")
    else:
        form = LoginForm(request)

    return render(request, "accounts/login.html", {"form": form})


@require_POST
def logout_view(request):
    """Cierre de sesión."""
    if request.user.is_authenticated:
        registrar_evento(
            "logout",
            usuario=request.user,
            ip=_cliente_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", ""),
        )
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def panel_redirect(request):
    """Redirige al panel principal."""
    return redirect("core:panel")


class CambiarContraseñaView(PasswordChangeView):
    """Cambio de contraseña maestra con registro de auditoría."""

    form_class = CambiarContraseñaForm
    template_name = "accounts/cambiar_contraseña.html"
    success_url = reverse_lazy("core:panel")

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            "cambio_contraseña",
            usuario=self.request.user,
            descripcion="Contraseña maestra cambiada.",
            ip=_cliente_ip(self.request),
            user_agent=self.request.META.get("HTTP_USER_AGENT", ""),
        )
        return response


@login_required
@require_http_methods(["GET", "POST"])
def validar_frase_rescate_view(request):
    """Validación de frase de rescate (recuperación de acceso)."""
    if request.method == "POST":
        frase = request.POST.get("frase_rescate", "")
        ok = validar_frase_rescate(request.user, frase)
        if ok:
            registrar_evento(
                "uso_frase_rescate",
                usuario=request.user,
                descripcion="Frase de rescate validada (recuperación).",
                ip=_cliente_ip(request),
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
            )
            return render(request, "accounts/rescue_exito.html")
        return render(request, "accounts/rescue.html", {"error": True})
    return render(request, "accounts/rescue.html")
