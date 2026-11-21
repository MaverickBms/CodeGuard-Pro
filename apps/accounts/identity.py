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
    propietario = Usuario.objects.filter(
        is_active=True, es_propietario_local=True
    ).order_by("id").first()
    if propietario is not None:
        return propietario

    heredado = Usuario.objects.filter(
        is_active=True, username="propietario-local"
    ).first()
    if heredado is not None:
        return heredado

    # Compatibilidad con perfiles anteriores a la marca explícita. Solo se
    # resuelve una cuenta cuando no hay ambigüedad; con varias cuentas activas
    # y sin propietario marcado no se elige ninguna al azar.
    activos = list(
        Usuario.objects.filter(is_active=True).order_by("id").values_list("id", flat=True)[:2]
    )
    if len(activos) == 1:
        return Usuario.objects.get(pk=activos[0])
    return None


def get_usuario_actual(request):
    """Devuelve el usuario activo para operaciones de progreso.

    En modo sin autenticación devuelve el propietario local existente
    (``request.usuario_local``). Cuando la autenticación está activa devuelve
    el usuario autenticado de la petición.

    Si no existe propietario local ni usuario autenticado, devuelve None.
    Las vistas deben manejar este caso: lectura permitida, escritura bloqueada
    con mensaje comprensible. No se crea ningún usuario implícito.
    """
    usuario_local = getattr(request, "usuario_local", None)
    if usuario_local is not None:
        return usuario_local
    if request.user.is_authenticated:
        return request.user
    return None


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
