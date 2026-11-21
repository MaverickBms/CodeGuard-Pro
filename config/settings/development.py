"""Development settings for CodeGuard Pro.

Modo de desarrollo local. Nunca utilizar DEBUG=True en ejecución de producción.
"""

from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# En desarrollo las cabeceras de seguridad se relajan para facilitar pruebas locales.
# En producción se activan estrictamente (ver docs/SEGURIDAD.md).
# Nota: Sin sistema de autenticación, no se incluye django.contrib.admin.

# Servidor local de desarrollo sin runserver: Waitress sirve WSGI y WhiteNoise
# entrega los recursos estáticos desde los finders de Django. Así `npm start`
# usa el mismo punto de entrada que el paquete y un perfil limpio funciona.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *[middleware for middleware in MIDDLEWARE if middleware != "django.middleware.security.SecurityMiddleware"],
]
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
