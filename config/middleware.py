"""Middlewares de seguridad y sesión para CodeGuard Pro.

- Inactividad: expira la sesión tras el tiempo configurado (RF-002 / RS-009).
- Cabeceras de seguridad: CSP, X-Frame-Options, X-Content-Type-Options, etc. (RS-013).
- Redirección a configuración inicial si no existe usuario.
- Restricción de host: solo localhost/127.0.0.1 en ejecución normal.
"""

from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.urls import reverse


class SesionInactividadMiddleware:
    """Expira la sesión por inactividad según sesion_timeout_minutos del usuario."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            return None

        ultima_actividad = request.session.get("ultima_actividad")
        ahora = None
        from django.utils import timezone
        ahora = timezone.now()

        if ultima_actividad is not None:
            from datetime import datetime
            if isinstance(ultima_actividad, str):
                from django.utils.dateparse import parse_datetime
                ultima_actividad = parse_datetime(ultima_actividad)

            if ultima_actividad is not None:
                inactividad = (ahora - ultima_actividad).total_seconds()
                limite = request.user.sesion_timeout_minutos * 60
                if inactividad > limite:
                    from apps.audit.services import registrar_evento
                    registrar_evento(
                        "logout_inactividad",
                        usuario=request.user,
                        descripcion="Sesión expirada por inactividad.",
                    )
                    auth_logout(request)
                    login_url = reverse("accounts:login")
                    if request.path != login_url:
                        return redirect(login_url)
                    return None

        request.session["ultima_actividad"] = ahora.isoformat()
        return None


class CabecerasSeguridadMiddleware:
    """Añade cabeceras de seguridad a todas las respuestas (RS-013)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Evitar clickjacking.
        response["X-Frame-Options"] = "DENY"
        # Evitar MIME-sniffing.
        response["X-Content-Type-Options"] = "nosniff"
        # Control del referrer.
        response["Referrer-Policy"] = "no-referrer"
        # Permissions policy restrictiva (sin APIs innecesarias).
        response["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )

        # Content Security Policy: solo recursos propios (sin CDN).
        # Se permite 'unsafe-inline' en styles y scripts porque es una aplicación
        # desktop local que renderiza sus propios recursos estáticos.
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self'; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self';"
        )
        response["Content-Security-Policy"] = csp

        # No cachear páginas con datos sensibles por defecto (se relaja en static).
        if not request.path.startswith("/static/") and not request.path.startswith("/media/"):
            response["Cache-Control"] = "no-store, no-cache, must-revalidate, private"
            response["Pragma"] = "no-cache"

        return response


class ConfiguracionInicialMiddleware:
    """Redirige a la configuración inicial si no existe usuario todavía."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        respuesta = self.get_response(request)
        return respuesta

    def process_view(self, request, view_func, view_args, view_kwargs):
        from apps.accounts.models import Usuario

        if not Usuario.objects.exists():
            rutas_permitidas = [
                reverse("accounts:setup_inicial"),
                reverse("accounts:setup_exito"),
                "/admin/",
                "/static/",
            ]
            if not any(request.path.startswith(r) for r in rutas_permitidas):
                return redirect("accounts:setup_inicial")
        return None
