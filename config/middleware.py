"""Middlewares de seguridad y sesión para CodeGuard Pro.

- Cabeceras de seguridad: CSP, X-Frame-Options, X-Content-Type-Options, etc. (RS-013).
- Restricción de host: solo localhost/127.0.0.1 en ejecución normal.
- Cierre de sesión por inactividad (RF-002 / CG-005).

Nota: La aplicación es local, monousuario y offline-first. Sin autenticación
remota ni multiusuario.
"""

from datetime import timedelta

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone

from apps.audit.services import registrar_evento


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
        # Se permite 'unsafe-inline' en styles porque la interfaz usa estilos
        # inline; los scripts se sirven desde /static/ y no usan inline scripts.
        csp = (
            "default-src 'self'; "
            "script-src 'self'; "
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


class SesionInactividadMiddleware:
    """Cierra la sesión del usuario tras un periodo de inactividad (RF-002).

    Consulta el tiempo transcurrido desde la última actividad registrada en la
    sesión del usuario autenticado. Si supera ``usuario.sesion_timeout_minutos``
    (por defecto ``SESSION_TIMEOUT_MINUTES`` = 15), cierra la sesión, registra el
    evento en auditoría y redirige al inicio de sesión.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = getattr(request, "user", None)
        if user is None or not user.is_authenticated or not user.is_active:
            return response

        timeout_min = getattr(user, "sesion_timeout_minutos", None) or getattr(
            settings, "SESSION_TIMEOUT_MINUTES", 15
        )
        try:
            timeout = timedelta(minutes=int(timeout_min))
        except (TypeError, ValueError):
            timeout = timedelta(minutes=15)

        ahora = int(timezone.now().timestamp())
        ultima = request.session.get("ultima_actividad")
        if ultima is None:
            # Primera actividad registrada de la sesión actual.
            request.session["ultima_actividad"] = ahora
            return response

        if ahora - int(ultima) > int(timeout.total_seconds()):
            # Sesión inactiva por encima del umbral: cerrar y redirigir.
            logout(request)
            registrar_evento(
                "logout_inactividad",
                usuario=user,
                descripcion="Sesión cerrada por inactividad.",
            )
            return redirect("accounts:login")

        request.session["ultima_actividad"] = ahora
        return response
