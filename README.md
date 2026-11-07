# 🛡️ CodeGuard Pro

> **Tu formación técnica, siempre offline y siempre tuya.**

**CodeGuard Pro** es una plataforma educativa personal, local y **offline-first** que organiza tu roadmap de aprendizaje, gestiona etapas y lecciones, registra tu progreso verificado y documenta tus evidencias.

Todo corre en tu propio equipo: un servidor **Django** local + una aplicación de escritorio **Electron**, con **SQLite** de por medio. Sin Internet obligatorio, sin servidores externos, sin nube, sin telemetría.

---

## 📖 Manual de uso

### 1. Primer arranque y configuración inicial

Al abrir la aplicación por primera vez se inicia el **asistente de configuración inicial**:

1. Creas el **usuario** y la **contraseña maestra** (mínimo 8 caracteres).
2. Se genera una **frase de rescate** de alta entropía (≥128 bits), se muestra **una sola vez** y se guarda como **hash Argon2** (nunca en texto plano). Es de un solo uso.
3. Aceptas los **términos de uso** y el **código de ética**.
4. Accedes al **panel principal**.

### 2. Inicio y cierre de sesión

- En el panel ingresas tu **usuario + contraseña maestra** (Argon2).
- La sesión expira por **inactividad** (15 minutos por defecto) y se registra en auditoría.
- El cierre de sesión se hace desde la aplicación; el acceso posterior requiere autenticación.

### 3. Panel principal

Dashboard con resumen de progreso, módulos del MVP, actividades pendientes, evaluaciones, laboratorios, documentos, evidencias y revisiones.

### 4. Roadmap ASCENSO

- Listado de las **33 etapas** oficiales con filtros (bloque, prioridad, búsqueda).
- Detalle de etapa: módulos, lecciones, proyecto, criterios, prerrequisitos.
- Marcado de lecciones y de etapas completas con **recalculo automático de porcentaje**.
- Bloqueo de etapas cuyos prerrequisitos no estén completados.

### 5. Frase de rescate

Si olvidas la contraseña: valida tu frase de rescate en `/accounts/rescate/`. Si es correcta y no se ha usado, recuperas el acceso; la frase queda **invalidada**.

### 6. Cambio de contraseña

Desde la aplicación, con la contraseña actual, actualizas la **contraseña maestra** (Argon2).

### 7. Temas visuales

12 temas (claro, oscuro, alto contraste, retro-pixel, cyberpunk, fantasía, ciencia ficción, guerrero, mago, pícaro, paladín, oscuro mago) con glassmorphism y persistencia.

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

## 🔒 Privacidad

- Servidor local en `127.0.0.1` (nunca `0.0.0.0`).
- CSP estricta, cabeceras de seguridad, `DEBUG=False`.
- Contraseñas y frases con Argon2, un solo uso.
- Sin CDN, sin telemetría, sin servicios externos.

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

- El panel redirige a `/accounts/login/?next=/` → inicie sesión.
- El roadmap muestra "El roadmap todavía no está cargado" → ejecute `python manage.py cargar_ascenso`.

## 🤝 Contribuir · 🛡️ Seguridad · 📄 Licencia

Consulte `docs/` para arquitectura, seguridad, modelo de datos, plan de pruebas y manual extendido.

---

*CodeGuard Pro — con cimientos técnicos sólidos, funcionales, seguros, comprobables y preparados para evolucionar.*
