"""Development settings for CodeGuard Pro.

Modo de desarrollo local. Nunca utilizar DEBUG=True en ejecución de producción.
"""

from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

INSTALLED_APPS = INSTALLED_APPS + [  # noqa: F405
    "django.contrib.admin",
]

# En desarrollo las cabeceras de seguridad se relajan para facilitar pruebas locales.
# En producción se activan estrictamente (ver docs/SEGURIDAD.md).
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Evitar que Django intente servir por interfaces externas en dev.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
