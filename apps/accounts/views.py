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
from django.utils import timezone
from django.views.decorators.http import require_POST
from datetime import timedelta

from apps.accounts.forms import CambiarContraseñaForm, LoginForm, NuevoPasswordForm, SetupInicialForm
from apps.accounts.models import Usuario
from apps.accounts.services import (
    cambiar_contrasena_por_frase,
    crear_usuario_inicial,
    verificar_frase_rescate,
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
        # Se conserva la instancia con errores para no perder los datos ni los
        # mensajes de validación (CG-004).
        form = SetupInicialForm(request.POST)
        if form.is_valid():
            usuario, frase_rescate = crear_usuario_inicial(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
                ip=request.META.get("REMOTE_ADDR") or None,
                user_agent=request.META.get("HTTP_USER_AGENT", "")[:512],
            )
            return render(request, "accounts/setup_exito.html", {"frase_rescate": frase_rescate})
    else:
        form = SetupInicialForm()

    return render(request, "accounts/setup_inicial.html", {"form": form})


class LoginView(auth_views.LoginView):
    """Inicio de sesión con la contraseña maestra (Argon2).

    Incluye la política RS-017:
    - 5 intentos fallidos consecutivos bloquean la cuenta durante 15 minutos.
    - El contador se reinicia tras un inicio de sesión exitoso.
    - Los bloqueos y los intentos fallidos se registran en auditoría.
    """

    form_class = LoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    INTENTOS_MAXIMOS = 5
    BLOQUEO_MINUTOS = 15

    def get_success_url(self):
        """Redirige al panel principal tras un inicio de sesión exitoso."""
        return reverse("core:panel")

    def dispatch(self, request, *args, **kwargs):
        """Verifica bloqueo antes de mostrar el form o procesar el POST."""
        username = request.POST.get("username", "") if request.method == "POST" else ""
        if username:
            usuario = Usuario.objects.filter(username=username).first()
            if usuario and usuario.bloqueado_hasta and usuario.bloqueado_hasta > timezone.now():
                mensajes = {
                    "error": (
                        "La cuenta está temporalmente bloqueada por intentos fallidos. "
                        f"Inténtelo de nuevo dentro de {self.BLOQUEO_MINUTOS} minutos."
                    )
                }
                messages.error(request, mensajes["error"])
                registrar_evento(
                    "acceso_denegado",
                    usuario=usuario,
                    descripcion="Intento de login con cuenta bloqueada por intentos fallidos.",
                    ip=request.META.get("REMOTE_ADDR") or None,
                    user_agent=request.META.get("HTTP_USER_AGENT", "")[:512],
                )
                return self.render_to_response(self.get_context_data(form=self.get_form()))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Inicio exitoso: reinicia contador de intentos y bloqueo."""
        usuario = form.get_user()
        usuario.intentos_fallidos = 0
        usuario.bloqueado_hasta = None
        usuario.save(update_fields=["intentos_fallidos", "bloqueado_hasta"])
        login(self.request, usuario)
        registrar_evento(
            "login_exitoso",
            usuario=usuario,
            descripcion="Inicio de sesión exitoso.",
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """Inicio fallido: incrementa contador y bloquea tras el umbral."""
        username = form.cleaned_data.get("username", "") if form.cleaned_data else ""
        usuario = Usuario.objects.filter(username=username).first()

        if usuario:
            usuario.intentos_fallidos += 1
            if usuario.intentos_fallidos >= self.INTENTOS_MAXIMOS:
                usuario.bloqueado_hasta = timezone.now() + timedelta(
                    minutes=self.BLOQUEO_MINUTOS
                )
                usuario.save(update_fields=["intentos_fallidos", "bloqueado_hasta"])
                registrar_evento(
                    "acceso_denegado",
                    usuario=usuario,
                    descripcion=(
                        f"Cuenta bloqueada tras {usuario.intentos_fallidos} "
                        "intentos fallidos consecutivos."
                    ),
                    ip=self.request.META.get("REMOTE_ADDR") or None,
                    user_agent=self.request.META.get("HTTP_USER_AGENT", "")[:512],
                )
            else:
                usuario.save(update_fields=["intentos_fallidos"])
                registrar_evento(
                    "login_fallido",
                    usuario=usuario,
                    descripcion=(
                        f"Intento de inicio de sesión fallido "
                        f"({usuario.intentos_fallidos}/{self.INTENTOS_MAXIMOS})."
                    ),
                    ip=self.request.META.get("REMOTE_ADDR") or None,
                    user_agent=self.request.META.get("HTTP_USER_AGENT", "")[:512],
                )
        else:
            # Usuario inexistente: mensaje genérico, no revelar existencia.
            registrar_evento(
                "login_fallido",
                usuario=None,
                descripcion=f"Intento de inicio de sesión fallido para usuario inexistente.",
                ip=self.request.META.get("REMOTE_ADDR") or None,
                user_agent=self.request.META.get("HTTP_USER_AGENT", "")[:512],
            )

        # Mensaje genérico que no revela si el usuario existe o está bloqueado.
        messages.error(
            self.request,
            "Usuario o contraseña incorrectos.",
        )
        return super().form_invalid(form)


@require_POST
def cerrar_sesion(request):
    """Cierre de sesión manual (exige POST y mantiene CSRF)."""
    usuario = request.user if request.user.is_authenticated else None
    logout(request)
    registrar_evento(
        "logout",
        usuario=usuario,
        descripcion="Cierre de sesión manual.",
        ip=request.META.get("REMOTE_ADDR") or None,
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:512],
    )
    return redirect("core:panel")


def rescate(request):
    """Valida la frase de rescate para recuperar el acceso (un solo uso)."""
    error = False
    usuario = get_user_model().objects.first()
    if request.method == "POST":
        frase = (request.POST.get("frase_rescate") or "").strip()
        if usuario is not None and verificar_frase_rescate(usuario, frase):
            # La frase no se consume aquí: se invalidará al establecer la nueva
            # contraseña con éxito (flujo atómico, CG-003).
            return redirect("accounts:resetear_contrasena")
        error = True
    return render(request, "accounts/rescue.html", {"error": error})


def rescate_exito(request):
    """Página posterior a una frase de rescate válida."""
    return redirect("accounts:login")


def resetear_contrasena(request):
    """Establece la nueva contraseña maestra tras validar la frase de rescate.

    Paso posterior al alta de la frase: recibe la frase y la nueva contraseña
    (con confirmación). Si la frase es válida y la contraseña supera los
    validadores, se establece de forma segura y atómica y se invalida la frase.
    Si algo falla, la frase no se consume y no se cambia la contraseña.
    """
    Usuario = get_user_model()
    usuario = Usuario.objects.first()
    if usuario is None:
        return redirect("accounts:login")

    if request.method == "POST":
        form = NuevoPasswordForm(usuario, request.POST)
        if form.is_valid():
            if cambiar_contrasena_por_frase(
                usuario,
                form.cleaned_data["frase_rescate"],
                form.cleaned_data["password1"],
            ):
                return redirect("accounts:login")
            form.add_error("frase_rescate", "Frase de rescate incorrecta o ya utilizada.")
        return render(request, "accounts/resetear_contrasena.html", {"form": form})

    form = NuevoPasswordForm(usuario)
    return render(request, "accounts/resetear_contrasena.html", {"form": form})


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
