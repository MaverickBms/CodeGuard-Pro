"""Middlewares de seguridad, sesión y acceso local para CodeGuard Pro.

- Cabeceras de seguridad: CSP, X-Frame-Options, X-Content-Type-Options, etc. (RS-013).
- Restricción de host: ALLOWED_HOSTS limita el encabezado Host y el servidor
  empaquetado se enlaza exclusivamente a 127.0.0.1.
- Cierre de sesión por inactividad (RF-002 / CG-005).
- Identidad local (AccesoLocalMiddleware): resuelve el propietario explícito cuando
  la autenticación está desactivada (AUTH_DISABLED=True), sin crear sesiones ni
  usar request.user como respaldo.

Nota: La aplicación es local, monousuario y offline-first. Sin autenticación
remota ni multiusuario.
"""

from datetime import timedelta

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone

from apps.accounts.identity import obtener_usuario_local
from apps.audit.services import registrar_evento


class AccesoLocalMiddleware:
    """Resuelve el propietario local existente para el modo sin autenticación.

    Cuando ``AUTH_DISABLED`` es True:
      - Establece ``request.usuario_local`` con el propietario explícito resuelto.
      - No crea cuentas ni inicia sesión. Una sesión Django heredada puede seguir
        presente, pero get_usuario_actual() no la usa como identidad local.
      - Si el perfil es ambiguo, deja ``request.usuario_local`` en None.
    Cuando es False, no hace nada y el flujo de autenticación original sigue intacto.

    Debe colocarse después de AuthenticationMiddleware en settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, "AUTH_DISABLED", False):
            request.usuario_local = obtener_usuario_local(request)
        else:
            request.usuario_local = None

        return self.get_response(request)


class CabecerasSeguridadMiddleware:
    """Añade cabeceras de seguridad a todas las respuestas (RS-013)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Evitar clickjacking. El visor de la biblioteca necesita incrustar
        # únicamente su propio PDF del mismo origen; el resto queda denegado.
        allow_same_origin_frame = bool(
            getattr(response, "_cg_allow_same_origin_frame", False)
        )
        response["X-Frame-Options"] = (
            "SAMEORIGIN" if allow_same_origin_frame else "DENY"
        )
        # Evitar MIME-sniffing.
        response["X-Content-Type-Options"] = "nosniff"
        # Control del referrer.
        response["Referrer-Policy"] = "same-origin"
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
            "object-src 'none'; "
            "frame-src 'self'; "
            "frame-ancestors '%s'; "
            "form-action 'self'; "
            "base-uri 'self';"
            % ("self" if allow_same_origin_frame else "none")
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

    La comprobación se realiza **antes** de delegar en la vista (``get_response``)
    para garantizar que una sesión vencida nunca ejecute operaciones protegidas.
    Los recursos locales (estáticos y medios) no renuevan la sesión.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def _es_recurso_local(request) -> bool:
        """Indica si la petición solicita un recurso local (estático/medio)."""
        return request.path.startswith("/static/") or request.path.startswith("/media/")

    def __call__(self, request):
        if getattr(settings, "AUTH_DISABLED", False):
            # La autenticación está desactivada: no hay sesiones que cerrar ni
            # redirecciones al login. Delega directamente en la vista.
            return self.get_response(request)

        user = getattr(request, "user", None)
        if user is not None and user.is_authenticated and user.is_active:
            if not self._es_recurso_local(request):
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
                elif ahora - int(ultima) > int(timeout.total_seconds()):
                    # Sesión inactiva por encima del umbral: cerrar y redirigir
                    # ANTES de ejecutar la vista.
                    logout(request)
                    registrar_evento(
                        "logout_inactividad",
                        usuario=user,
                        descripcion="Sesión cerrada por inactividad.",
                        ip=request.META.get("REMOTE_ADDR") or None,
                        user_agent=request.META.get("HTTP_USER_AGENT", "")[:512],
                    )
                    return redirect("accounts:login")

                request.session["ultima_actividad"] = ahora

        return self.get_response(request)
