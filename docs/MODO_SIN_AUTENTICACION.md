# Modo sin autenticación de CodeGuard Pro

## Estado

El sistema de autenticación de CodeGuard Pro está **temporalmente desactivado**.

- `AUTH_DISABLED = True` en `config/settings/base.py`.
- La aplicación abre directamente el panel principal.
- No se solicita usuario ni contraseña.
- No se crean sesiones ni se autentica mediante `request.user`.

## ¿Qué se desactivó?

| Componente | Estado | Observación |
|---|---|---|
| Pantalla de inicio de sesión | Redirige al panel (302) | Ruta conservada, no accesible |
| Configuración inicial de usuario | Redirige al panel (302) | Ruta conservada, no accesible |
| Cierre de sesión | Redirige al panel (302) | Botón eliminado de la navegación |
| Recuperación por frase de rescate | Redirige al panel (302) | Ruta conservada, no accesible |
| Restablecimiento de contraseña | Redirige al panel (302) | Ruta conservada, no accesible |
| Cambio de contraseña autenticado | Redirige al panel (302) | Ruta conservada, no accesible |
| Bloqueo por 5 intentos fallidos | No aplica | Sin sesiones, sin intentos |
| Restricción por inactividad | No aplica | Middleware no-op |
| Formularios y pantallas de auth | Eliminados de la navegación | Plantillas conservadas |

## ¿Qué se conservó (no se eliminó)?

- Modelo `Usuario` (con `intentos_fallidos`, `bloqueado_hasta`, etc.).
- Modelo `FraseRescate`.
- Servicios de autenticación (`apps/account/services.py`).
- Formularios de autenticación (`apps/account/forms.py`).
- Vistas de autenticación (`apps/account/views.py`).
- Plantillas de autenticación (`templates/accounts/*.html`).
- Archivo de migración `0002_usuario_bloqueado_hasta_usuario_intentos_fallidos.py`.
- Campos `intentos_fallidos` y `bloqueado_hasta`.
- Historial de migraciones.
- Datos existentes en `data/db.sqlite3`.
- Pruebas automatizadas de autenticación (verificables con `override_settings(AUTH_DISABLED=False)`).

## ¿Cómo funciona el progreso sin autenticación?

El progreso de los roadmaps (etapas, lecciones completadas) se asocia al **propietario local existente** de la base de datos (el usuario `usuario` creado previamente), resuelto a través de `request.usuario_local`:

- No se crea ninguna cuenta ficticia.
- No se inicia sesión.
- `request.user` permanece como `AnonymousUser`.
- Si no existiera ningún usuario activo en la BD, la lectura funcionaría pero las operaciones de escritura se bloquearían con un mensaje claro.

## ¿Cómo se registra la auditoría?

Cuando la autenticación está desactivada, los eventos de auditoría se registran con actor nulo (`usuario=None`), compatible con el modelo `AuditLog` que permite `usuario` nulo (`on_delete=SET_NULL, null=True, blank=True`).

## ¿Cómo reactivar la autenticación?

**Requiere autorización expresa del propietario del proyecto.**

1. Cambie `AUTH_DISABLED = True` a `AUTH_DISABLED = False` en `config/settings/base.py`.
2. No se requieren migraciones ni cambios de esquema.
3. El sistema de autenticación original recupera su funcionamiento completo.

No se debe reactivar sin autorización expresa.

## Archivos implicados

- `config/settings/base.py` — constante `AUTH_DISABLED`.
- `config/middleware.py` — `AccesoLocalMiddleware` y `SesionInactividadMiddleware` no-op.
- `config/settings/desktop.py` — middleware añadido.
- `apps/accounts/identity.py` — helpers y decoradores de acceso local (nuevo).
- `apps/accounts/views.py` — guardas en rutas de autenticación.
- `apps/core/views.py` — panel sin login y contexto adaptado.
- `apps/roadmaps/views.py` — roadmaps sin login y guardas de escritura.
- `apps/roadmaps/services.py` — actor de auditoría opcional.
- `templates/base.html` — formulario de cierre de sesión eliminado.
- `templates/core/panel.html` — referencias a `user` adaptadas.
- `apps/accounts/tests/test_modo_sin_auth.py` — pruebas del modo sin auth (nuevo).
- Pruebas existentes — envueltas con `override_settings(AUTH_DISABLED=False)`.
