# Changelog — CodeGuard Pro

Todos los cambios notables del proyecto se documentan aquí.

## [1.0.3] — 2026-11-11 — Fase 2: roadmap ASCENSO, flujo editorial y registro de paquetes

### Añadido
- Roadmap ASCENSO 3.1 completo: `Roadmap`, `Etapa`, `Modulo`, `Leccion`, `Prerrequisito` (33 etapas, 0 a 32).
- Contenido académico editable: `ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion` con objetivos, teoría, ejemplos, ejercicios y evaluadores.
- Claves UUID estables (`clave_contenido`) para `Leccion`, `EjemploLeccion`, `EjercicioLeccion` (migración 0004).
- Catálogo de fuentes documentales: `FuenteConocimiento` con publicador, título, URL canónica, edición, licencia y fecha de consulta (migración 0005).
- Snapshots inmutables de versión de lección: `VersionContenidoLeccion` con flujo editorial (`borrador → revisión → aprobada → publicada → sustituida → retirada`) y metadatos de auditoría (migración 0005).
- Referencias de fuente por versión: `ReferenciaFuenteContenido` con rol, localizador y nota de atribución (migración 0005).
- Autoría y metadatos de versión de contenido (migración 0011).
- Auditoría editorial: envío a revisión, aprobación, publicación, sustitución y retirada (migraciones 0006–0008).
- Revisión de licencias de fuentes y correspondencia UUID/paquete (migraciones 0009–0010).
- Registro local de paquetes de conocimiento: `PaqueteConocimientoInstalado` con transiciones controladas (`descargado → verificado → activo → rechazado → sustituido`), identidad inmutable, un solo activo por canal y secuencia única por canal (migración 0012).
- Un solo paquete activo por canal: restricción parcial y migración de datos (migración 0013).
- Estado de sincronización por canal: `EstadoSincronizacion` (migración 0012).
- Comandos de gestión: `cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`.
- Pruebas del flujo editorial, registro de paquetes, distribución firmada (Ed25519) y modo sin autenticación.

### Verificado
- `manage.py check`: sin errores.
- `makemigrations --check --dry-run`: sin cambios pendientes.
- Suite de pruebas: **93 pruebas OK** (`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`).

## [1.0.2] — 2026-11-07 — Desactivación temporal de autenticación

### Cambiado
- `AUTH_DISABLED = True` en `config/settings/base.py`: la aplicación abre directamente
  el panel principal sin solicitar credenciales.
- Las rutas de autenticación (login, setup, logout, rescate, resetear, cambio de
  contraseña) redirigen al panel principal (HTTP 302) mientras `AUTH_DISABLED` es True.
- Eliminado el botón "Cerrar sesión" de la navegación (`templates/base.html`).
- `SesionInactividadMiddleware` no opera cuando la autenticación está desactivada.
- `request.user` permanece como `AnonymousUser`; el progreso usa `request.usuario_local`
  (propietario local existente).
- La auditoría registra actor nulo (`usuario=None`) en modo sin autenticación.

### Añadido
- `config/middleware.py`: `AccesoLocalMiddleware` (resuelve el propietario local).
- `apps/accounts/identity.py`: helpers y decoradores de acceso local (nuevo).
- `apps/accounts/tests/test_modo_sin_auth.py`: pruebas del modo sin autenticación.
- `docs/MODO_SIN_AUTENTICACION.md`: guía canónica y procedimiento de reactivación.
- Pruebas existentes envueltas con `override_settings(AUTH_DISABLED=False)`.

### Conservado (no se eliminó)
- Modelos `Usuario` y `FraseRescate`; servicios, formularios, vistas y plantillas de
  autenticación; migración `0002`; campos `intentos_fallidos` y `bloqueado_hasta`;
  datos existentes en `data/db.sqlite3`.

### Verificado
- `manage.py check`: sin errores.
- `makemigrations --check --dry-run`: sin cambios pendientes.
- Suite de pruebas: OK (`apps.core apps.accounts apps.audit apps.roadmaps`).

## [1.0.1] — 2026-11-07 — Intervención de auditoría y consolidación técnica

### Corregido
- `DEBUG` ahora es `False` por defecto en settings base (antes `True`); desarrollo usa
  `DEBUG=True` explícito (`config/settings/development.py`).
- CSP endurecida: `script-src 'self'` (scripts locales sin `unsafe-inline`); el script inline de
  temas/utilidades se movió a `static/js/codeguard.js`; `style-src 'self' 'unsafe-inline'`.
- Eliminado ocultamiento de errores en `run.sh` (`cargar_ascenso` ya no se ejecuta con `|| true`).
- Sustituido `runserver --insecure` por servidor WSGI local **Waitress + WhiteNoise** en
  `server_entry.py`, settings de escritorio y `requirements.txt`; spec PyInstaller actualizado.
- Eliminada la creación implícita de usuario con contraseña vacía en panel y roadmap; la
  identidad pasa a ser la del usuario autenticado.

### Añadido
- Middlewares de sesión y autenticación (`SessionMiddleware`, `AuthenticationMiddleware`) y
  `SesionInactividadMiddleware` (timeout por inactividad, RF-002/RS-009, default 15 min).
- Vistas de autenticación completas: setup inicial, login, logout, rescate y cambio de contraseña.
- Rutas protegidas con `@login_required` (panel, roadmap lista, detalle, marcar etapa/lección).

### Verificado
- `manage.py check` (development + desktop): sin errores.
- `makemigrations --check`: sin cambios pendientes.
- Suite de pruebas: 31 pruebas OK (`apps.core apps.accounts apps.audit apps.roadmaps`).
- Smoke test del servidor WSGI: `GET / → 302` (login), `GET /static/js/codeguard.js → 200`.

## [1.0.0] — 2026-11-05 — Incremento 1: Núcleo funcional

### Añadido
- Proyecto Django base (config, manage.py, requirements.txt, .env.example, .gitignore).
- Apps: `core` (panel, navegación, configuración sistema), `accounts` (identidad, acceso),
  `audit` (registro de eventos).
- Modelo de usuario personalizado `accounts.Usuario` (extiende AbstractUser).
- Modelo `FraseRescate` (hash Argon2, un solo uso, alta entropía ≥128 bits).
- Modelo `ConfiguracionSistema` (singleton lógico).
- Modelo `AuditLog` (registro de eventos de seguridad y acceso).
- Servicios: `crear_usuario_inicial`, `generar_frase_rescate`, `validar_frase_rescate`,
  `autenticar_usuario`, `registrar_evento`.
- Vistas y formularios: setup inicial, login, logout, cambio de contraseña, frase de rescate.
- Middlewares: sesión por inactividad (timeout), cabeceras de seguridad (CSP, X-Frame, etc.),
  redirección a setup inicial si no hay usuario.
- Plantillas con Bootstrap 5.3.3 y HTMX 2.0.4 locales (sin CDN).
- CSS propio (`static/css/codeguard.css`).
- Documentación: arquitectura, modelo de datos, seguridad, instalación, revisión del SRS,
  decisiones pendientes, trazabilidad, plan de desarrollo, plan de pruebas, backups,
  manual de usuario, ADR 001-003, changelog.
- Migraciones iniciales aplicadas y verificadas desde base de datos vacía.
- Usuario inicial creado y verificado.
- Servidor verificado en `127.0.0.1:8000` (sin exposición a red).

### Verificado
- Aplicación arranca.
- Base de datos se crea y migraciones aplican.
- Usuario inicial se crea.
- Login funciona (302 → panel 200).
- Rutas protegidas requieren autenticación.
- Logout funciona (302 → login).
- Servidor escucha solo en 127.0.0.1.
- No hay referencias a CDN.
- Cabeceras de seguridad presentes (CSP, X-Frame-Options, X-Content-Type-Options, etc.).

### Pendiente
- Pruebas unitarias automatizadas (se añadirán en `tests/`).
- Roadmap ASCENSO (incremento 2).
- Competencias y evaluaciones (incremento 3).
- Biblioteca documental y base de conocimiento (incremento 4).
- Evidencias y laboratorios (incremento 5).
- Backups, restauración y vigencia (incremento 6).
