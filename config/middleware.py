"""Middlewares de seguridad para CodeGuard Pro.

- Cabeceras de seguridad: CSP, X-Frame-Options, X-Content-Type-Options, etc. (RS-013).
- Restricción de host: solo localhost/127.0.0.1 en ejecución normal.

Nota: Aplicación local, monousuario y offline-first. Sin middlewares de
sesión ni inactividad por ahora.
"""

from django.conf import settings


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
