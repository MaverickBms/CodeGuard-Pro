# Changelog — CodeGuard Pro

Todos los cambios notables del proyecto se documentan aquí.

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
