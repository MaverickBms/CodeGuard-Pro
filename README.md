# 🛡️ CodeGuard Pro

> **Tu formación técnica, siempre offline y siempre tuya.**

**CodeGuard Pro** es una plataforma educativa personal, local y **offline-first** que organiza tu roadmap de aprendizaje, gestiona etapas y lecciones, registra tu progreso verificado y documenta tus evidencias.

El núcleo corre en tu propio equipo: un servidor **Django** local + una aplicación de escritorio **Electron**, con **SQLite**. CodeGuard es **offline-first**: no requiere Internet para abrir la aplicación, estudiar con el contenido disponible ni consultar el progreso local. La sincronización opcional con un servicio central de conocimiento revisado está aprobada como parte de la Fase 2, pero **todavía no está implementada**. No se contempla subir progreso, intentos, código ni datos personales del estudiante.

---

## 📖 Manual de uso

### 1. Primer arranque y apertura de la aplicación

Al abrir la aplicación se inicia directamente en el **panel principal**.
No se solicita usuario ni contraseña. El sistema de autenticación está
**temporal y opcionalmente desactivado** para uso local directo (ver
`docs/MODO_SIN_AUTENTICACION.md`).

El sistema completo de autenticación (usuario, contraseña maestra, frase de
rescate, bloqueo por intentos y cierre de sesión) se **conserva íntegro** en el
código, modelos y migraciones, y puede reactivarse con autorización expresa
del propietario del proyecto.

### 2. Panel principal

Dashboard con resumen de progreso real del roadmap (etapas, módulos y
lecciones completadas), próxima actividad sugerida, actividad reciente,
módulos del MVP y estado del sistema. Todos los datos provienen de la base de
datos.

### 3. Roadmap ASCENSO

- Listado de las **33 etapas** oficiales con filtros (bloque, prioridad, búsqueda).
- Detalle de etapa: módulos, lecciones, proyecto, criterios, prerrequisitos.
- Marcado de lecciones y de etapas completas con **recalculo automático de porcentaje**.
- Bloqueo de etapas cuyos prerrequisitos no estén completados.

### 4. Temas visuales

12 temas con las 12 paletas oficiales (P01–P12): claro (P01), oscuro (P02),
alto contraste (P04), retro-pixel (P05), cyberpunk (P03), fantasía (P07),
ciencia ficción (P08), guerrero (P06), mago (P09), pícaro (P10), paladín
(P11), oscuro mago (P12).

Cada tema usa variables CSS semánticas con los HEX originales sin modificar.
El texto es blanco/negro según la luminancia para garantizar **WCAG AA
(4.5:1)** en todos los pares de interfaz (texto/fondo, texto/superficie,
botones, bordes, focus). Se respeta `prefers-reduced-motion` y no se usa
`transition: all`.

### 5. Autenticación (temporalmente desactivada)

El flujo de autenticación original queda preservado y no se ha eliminado:

- Configuración inicial de usuario y contraseña maestra.
- Inicio de sesión con contraseña maestra (Argon2).
- Cierre de sesión (POST, CSRF).
- Recuperación mediante frase de rescate (un solo uso).
- Cambio de contraseña autenticado.
- Bloqueo tras 5 intentos fallidos (15 minutos) y reinicio tras éxito.
- Auditoría de eventos de acceso.

Mientras `AUTH_DISABLED = True` en `config/settings/base.py`:

- La aplicación abre directamente el panel principal.
- No se muestran pantallas de login, registro, rescate ni cambio de contraseña.
- El botón "Cerrar sesión" no aparece en la navegación.
- Las rutas de autenticación redirigen al panel principal (HTTP 302).
- El progreso se asocia al propietario local existente de la base de datos.
- La auditoría registra actor nulo (`usuario=None`).

Para reactivar la autenticación, cambie `AUTH_DISABLED` a `False` únicamente
con autorización expresa del propietario del proyecto. No se requieren migraciones
ni cambios de esquema.

---

## ⚡ Instalación rápida

### Windows

```bat
build_windows.bat
```

Genera el servidor Django (PyInstaller) + instalador Electron (NSIS / portable).

### Linux / macOS (desde código)

```bash
git clone <repositorio>
cd CodeGuard-Pro
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_ascenso
npm install && npm start
```

O vía script: `./run.sh`.

---

## 🌐 Funcionamiento offline y actualizaciones de conocimiento

- El servidor de la aplicación escucha únicamente en `127.0.0.1`.
- El contenido instalado y los datos del estudiante se conservan localmente.
- La conexión no es requisito para estudiar con los recursos descargados.
- La Fase 2 contempla un servicio central que distribuirá paquetes académicos revisados y versionados mediante HTTPS.
- La sincronización será iniciada por el cliente, de solo descarga y no bloqueará el uso offline.
- Las actualizaciones deberán validar firma, integridad y compatibilidad antes de instalarse, con conservación de la versión anterior.
- El diseño no contempla enviar intentos, código, calificaciones, progreso ni datos personales al servidor central.
- **Estado actual:** la sincronización todavía no está implementada; estas reglas describen el alcance aprobado.

## 🔒 Privacidad

- Servidor local en `127.0.0.1` (nunca `0.0.0.0`).
- CSP estricta, cabeceras de seguridad, `DEBUG=False`.
- Contraseñas y frases con Argon2, un solo uso.
- Recursos estáticos locales, sin CDN ni telemetría.
- Cualquier futura conexión de actualización se limitará a descargar conocimiento publicado y no habilitará acceso remoto a la aplicación local.

## 🗄️ Dónde están tus datos

```
<CODEGUARD_DATA_DIR>/
├── db.sqlite3
├── logs/
├── media/
└── .secret_key
```

## 🧠 Stack técnico

Electron + Django 5.2 LTS + SQLite + Argon2 + Waitress + WhiteNoise + Bootstrap/HTMX/SweetAlert2/FontAwesome locales.

## 🧪 Verificación

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps
```

## ❓ Solución de problemas

- El panel se abre directamente sin solicitar credenciales (autenticación desactivada).
- El roadmap muestra "El roadmap todavía no está cargado" → ejecute `python manage.py cargar_ascenso`.
- Para reactivar el inicio de sesión, cambie `AUTH_DISABLED` a `False` en `config/settings/base.py` (requiere autorización expresa).

## 🤝 Contribuir · 🛡️ Seguridad · 📄 Licencia

Consulte `docs/` para arquitectura, seguridad, modelo de datos, plan de pruebas y manual extendido.

---

*CodeGuard Pro — con cimientos técnicos sólidos, funcionales, seguros, comprobables y preparados para evolucionar.*
