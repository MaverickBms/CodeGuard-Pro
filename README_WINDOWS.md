# CodeGuard Pro — Versión para Windows (.exe)

Este paquete contiene todo lo necesario para construir y ejecutar CodeGuard Pro
como una aplicación desktop independiente en Windows.

## Contenido

| Archivo | Descripción |
|---|---|
| `build_windows.bat` | Script de construcción automática para Windows |
| `CodeGuard.spec` | Especificación de PyInstaller para empaquetado |
| `requirements.txt` | Dependencias de Python (versiones exactas) |
| `manage.py` | Punto de entrada de Django |
| `config/` | Configuración de Django (settings, URLs, middleware) |
| `apps/` | Aplicaciones Django (core, accounts, audit) |
| `desktop/` | Lanzador de aplicación desktop (PySide6) |
| `templates/` | Plantillas HTML de la interfaz |
| `static/` | Recursos estáticos (CSS, JS, fuentes, Bootstrap, HTMX) |
| `docs/` | Documentación del proyecto |
| `IEEE830.md` | Especificación de requisitos (SRS v2.0) |

## Requisitos del sistema (Windows)

- Windows 10 o Windows 11 (64 bits)
- Python 3.12 o superior
- Al menos 2 GB de RAM libre
- Al menos 1 GB de espacio en disco

## Instalación y ejecución

### Opción A: Construcción automática (recomendada)

1. Descomprima este archivo en una carpeta de su elección.
2. Haga doble clic en `build_windows.bat`.
3. El script instalará Python, las dependencias, aplicará las migraciones y
   generará el ejecutable `Code Guard Pro.exe` en la carpeta `dist/`.
4. Ejecute `Code Guard Pro.exe` para iniciar la aplicación.

### Opción B: Ejecución desde código fuente

1. Instale Python 3.12+ desde https://www.python.org
2. Abra una terminal en la carpeta del proyecto.
3. Ejecute: `python -m pip install -r requirements.txt`
4. Ejecute: `python manage.py migrate`
5. Ejecute: `python desktop/main.py`

## Características

- ✅ Aplicación desktop independiente (no requiere navegador web)
- ✅ Servidor Django embebido en 127.0.0.1 (sin exposición a red)
- ✅ Autenticación local con contraseña maestra (Argon2)
- ✅ Frase de rescate de alta entropía (un solo uso)
- ✅ Sesión con timeout por inactividad
- ✅ Panel principal con navegación de módulos
- ✅ Todos los recursos estáticos locales (sin CDN, offline-first)
- ✅ Diseño profesional con tipografía elegante (Caladea + Liberation Sans)
- ✅ Cabeceras de seguridad (CSP, X-Frame-Options, CSRF, etc.)

## Seguridad

- La aplicación escucha exclusivamente en 127.0.0.1 (localhost)
- Nunca se expone a la red local ni a Internet
- Las contraseñas y la frase de rescate se hashean con Argon2
- No hay telemetría ni llamadas externas
- CSP estricta para prevenir XSS

## Documentación

Consulte la carpeta `docs/` para documentación completa:
- `ARQUITECTURA.md` — Arquitectura del sistema
- `SEGURIDAD.md` — Requisitos y medidas de seguridad
- `INSTALACION.md` — Guía de instalación
- `MANUAL_USUARIO.md` — Manual de usuario
- `IEEE830.md` — Especificación de requisitos (SRS v2.0)
