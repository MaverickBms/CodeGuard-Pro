"""Identidad local para el modo sin autenticación de CodeGuard Pro.

Cuando ``AUTH_DISABLED`` es True, la aplicación no solicita credenciales ni
crea sesiones. El progreso de los roadmaps se asocia al propietario local
existente (``request.usuario_local``) y la auditoría registra actor nulo
(``usuario=None``).

Cuando ``AUTH_DISABLED`` es False, se recupera el flujo de autenticación
original conservado íntegramente.

Este módulo no crea cuentas ficticias ni modifica el esquema de datos.
"""

from functools import wraps

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect


def obtener_usuario_local(request):
    """Devuelve el propietario local existente cuando la autenticación está desactivada.

    Si no existe ningún usuario activo en la base de datos, devuelve None.
    En ese caso la lectura funciona y las operaciones de escritura deben
    bloquearse con un mensaje comprensible.

    No crea usuarios ni inicia sesiones.
    """
    if not getattr(settings, "AUTH_DISABLED", False):
        return None

    Usuario = get_user_model()
    return Usuario.objects.filter(is_active=True).first()


def obtener_actor_auditoria(request):
    """Devuelve el actor para los registros de auditoría.

    En modo sin autenticación devuelve None (actor nulo, compatible con el
    modelo AuditLog que permite usuario nulo).
    En modo con autenticación devuelve el usuario autenticado.
    """
    if getattr(settings, "AUTH_DISABLED", False):
        return None
    return request.user if request.user.is_authenticated else None


def requiere_acceso(view_func):
    """Decorator que permite el acceso siempre que AUTH_DISABLED sea True.

    Cuando la autenticación está activa, se comporta exactamente como
    @login_required (redirige al login si no hay sesión).

    Se aplica sobre vistas que necesitan acceso al panel/roadmaps sin exigir
    credenciales mientras el sistema de autenticación está desactivado.
    """

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if getattr(settings, "AUTH_DISABLED", False):
            return view_func(request, *args, **kwargs)
        from django.contrib.auth.decorators import login_required

        return login_required(view_func)(request, *args, **kwargs)

    return _wrapped


def solo_con_autenticacion_activa(view_func):
    """Decorator para rutas de autenticación (login, logout, rescate, etc.).

    Cuando AUTH_DISABLED es True redirige al panel principal (HTTP 302)
    para que el usuario no pueda iniciar un flujo de autenticación desactivado.
    Cuando AUTH_DISABLED es False ejecuta la vista original.
    """

    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if getattr(settings, "AUTH_DISABLED", False):
            return redirect("core:panel")
        return view_func(request, *args, **kwargs)

    return _wrapped


def vista_sin_autenticacion(view_class):
    """Decorator de clase para vistas basadas en clase de autenticación.

    Cuando AUTH_DISABLED es True, el dispatch redirige al panel principal.
    Cuando AUTH_DISABLED es False se comporta como la vista original.
    """

    original_dispatch = view_class.dispatch

    @wraps(original_dispatch)
    def _dispatch(self, request, *args, **kwargs):
        if getattr(settings, "AUTH_DISABLED", False):
            return redirect("core:panel")
        return original_dispatch(self, request, *args, **kwargs)

    view_class.dispatch = _dispatch
    return view_class
