"""Development settings for CodeGuard Pro.

Modo de desarrollo local. Nunca utilizar DEBUG=True en ejecución de producción.
"""

from .base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# En desarrollo las cabeceras de seguridad se relajan para facilitar pruebas locales.
# En producción se activan estrictamente (ver docs/SEGURIDAD.md).
# Nota: Sin sistema de autenticación, no se incluye django.contrib.admin.
