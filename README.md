# CodeGuard Pro

Plataforma educativa personal, monousuario, local y **offline-first** para organizar la formación técnica, gestionar el roadmap **ASCENSO 3.1**, documentar el aprendizaje y demostrar competencias con evidencias verificables.

CodeGuard Pro se ejecuta como una **aplicación de escritorio independiente** (no abre un navegador externo): un cliente **Electron** inicia y controla un servidor **Django** que escucha exclusivamente en `127.0.0.1`. No usa CDN, no envía telemetría y no expone la aplicación a la red local ni a Internet.

---

## Estado actual

| Incremento | Contenido | Estado |
|---|---|---|
| 1 | Identidad y acceso: configuración inicial, Argon2, frase de rescate, timeout por inactividad, auditoría, panel protegido | ✅ Implementado |
| 2 | Gestión académica: roadmap ASCENSO 3.1 con 33 etapas, 212 módulos, 1 946 lecciones, 33 proyectos, prerrequisitos y progreso | ✅ Implementado |
| 3 | Biblioteca documental, base de conocimiento, competencias, evaluaciones, evidencias y laboratorios | ⏳ Pendiente |

El contenido del roadmap se extrae del documento oficial **PROYECTO ASCENSO — Roadmap Maestro Consolidado 3.1 (2026)**. No se inventan etapas, módulos, lecciones ni dependencias. El JSON generado conserva el SHA-256 de la fuente documental.

---

## Arquitectura

```
┌──────────────────────────────────────────────────────────────┐
│ Electron (proceso principal)                                 │
│  • Ventana nativa, menú, temas, notificaciones               │
│  • Elige un puerto libre y lanza el servidor Django          │
│  • Espera a que 127.0.0.1:<puerto> responda                  │
│  • Detiene el árbol de procesos al cerrar                    │
└───────────────┬──────────────────────────────────────────────┘
                │ HTTP loopback (127.0.0.1)
┌───────────────▼──────────────────────────────────────────────┐
│ Django 5.2 LTS (API y renderizado local)                     │
│  • apps.accounts  → identidad, sesión, frase de rescate      │
│  • apps.audit     → registro de eventos de seguridad         │
│  • apps.core      → panel y configuración del sistema        │
│  • apps.roadmaps  → ASCENSO, módulos, lecciones, progreso    │
│  • SQLite + Argon2 + plantillas Django                       │
└───────────────┬──────────────────────────────────────────────┘
                │
┌───────────────▼──────────────────────────────────────────────┐
│ Datos del usuario (escribibles)                              │
│  Linux:   ~/.config/CodeGuard Pro/  (o data/ en desarrollo)  │
│  Windows: %APPDATA%\CodeGuard Pro\                           │
│  • db.sqlite3 · logs/ · media/ · .secret_key                 │
└──────────────────────────────────────────────────────────────┘
```

### Componentes principales

- **Electron** (`electron/main.js`, `electron/preload.js`): ventana, menú nativo, selector de 12 temas, notificaciones, selección de carpetas y aislamiento del renderer (`contextIsolation`, `sandbox`, `nodeIntegration: false`).
- **Django** (`config/`, `apps/`): lógica de negocio, autenticación, auditoría, roadmap y plantillas semánticas.
- **SQLite**: base de datos local monousuario. La aplicación empaquetada escribe en `CODEGUARD_DATA_DIR`, nunca dentro del directorio de instalación.
- **Recursos locales**: Bootstrap, HTMX, SweetAlert2, Font Awesome y tipografías Caladea/Liberation Sans se sirven desde `static/`.

---

## Requisitos

### Desarrollo en Linux

- Python 3.12 o superior (probado con 3.14)
- Node.js 20 o superior y npm
- SQLite con soporte FTS5 (incluido en la mayoría de distribuciones)
- 2 GB de RAM libre y ~1 GB de disco

### Construcción del `.exe` de Windows

- Windows 10/11 de 64 bits
- Python 3.12+ y Node.js 20+
- Ejecutar `build_windows.bat` **en Windows**. Electron no puede compilar un `.exe` nativo de Windows desde Fedora/Linux.

---

## Instalación y ejecución (Linux)

```bash
git clone https://github.com/MaverickBms/CodeGuard-Pro.git
cd CodeGuard-Pro

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate --settings=config.settings.development
python manage.py cargar_ascenso --settings=config.settings.development

npm install
npm start
```

También puedes usar el script incluido, que prepara el entorno, aplica migraciones y lanza Electron:

```bash
chmod +x run.sh
./run.sh
```

> Electron es el único proceso que inicia y detiene Django. `run.sh` ya no lanza un segundo servidor en segundo plano.

### Ejecución manual sin Electron (solo desarrollo)

```bash
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000 --settings=config.settings.development
```

Abre `http://127.0.0.1:8000` en un navegador local. Esta modalidad es solo para depuración; la aplicación distribuible es la de Electron.

---

## Primer uso

1. Al abrir la aplicación por primera vez, se muestra el **asistente de configuración inicial**.
2. Crea el usuario administrador y la contraseña maestra. La contraseña se almacena con **Argon2**.
3. Guarda la **frase de rescate** generada. Se muestra una sola vez y no se almacena en texto plano.
4. El panel principal queda protegido por sesión. La sesión expira por inactividad (15 minutos por defecto).
5. Abre **Roadmap ASCENSO** en la barra lateral para explorar las 33 etapas.

No se incluyen credenciales por defecto ni datos personales en el repositorio.

---

## Roadmap ASCENSO 3.1

El comando `cargar_ascenso` importa el contenido oficial de forma idempotente:

```bash
python manage.py cargar_ascenso
```

Resultado esperado:

- **33 etapas** (0–32), organizadas en 7 partes/bloques.
- **212 módulos** y **1 946 lecciones**.
- **33 proyectos** de etapa.
- **7 prerrequisitos explícitos** documentados: `10→9`, `15→13` y `31→{3,4,7,8,21}`.
- Todas las etapas quedan visibles. Las no desarrolladas en el MVP se marcan como **«No desarrollada en MVP»**.

La decisión **P-002** (qué etapas se desarrollan en el MVP) sigue pendiente. La propuesta registrada en la documentación es desarrollar las etapas **0, 1, 2, 3, 8, 17 y 21**, sin eliminar las demás del roadmap. Ninguna etapa se oculta ni se borra.

### Funcionalidad del módulo

- Listado de etapas con filtros por bloque, prioridad y búsqueda en títulos, módulos y lecciones.
- Detalle de etapa con objetivo, módulos, lecciones, proyecto, criterios y notas del documento.
- Marcado de lecciones y de etapa completa; recálculo automático del porcentaje.
- Bloqueo de etapas con prerrequisitos sin completar.
- Registro de progreso por etapa y por lección en SQLite.
- Auditoría de las acciones de progreso (`roadmap_*`).

---

## Temas visuales

La aplicación incluye **12 temas** con variantes de contraste y estética de videojuego, implementados con variables CSS y superficies glassmorphism:

1. Claro Diurno
2. Oscuro Nocturno
3. Alto Contraste
4. Retro Pixel
5. Cyberpunk
6. Reino Fantasía
7. Ciencia Ficción
8. Guerrero
9. Mago
10. Pícaro
11. Paladín
12. Oscuro Mago

El tema se cambia desde el icono de paleta del encabezado o desde **Ver → Tema** en el menú de Electron. La preferencia se guarda en `localStorage` y se sincroniza con el proceso principal.

La interfaz usa estructura semántica: `<aside>` para la navegación, `<header>` para la cabecera, `<main>` para el contenido y `<footer>` para el pie.

---

## Seguridad y privacidad

- El servidor escucha **solo en `127.0.0.1`**; nunca en `0.0.0.0`.
- Contraseñas con **Argon2**; frase de rescate de un solo uso.
- Sesión con expiración por inactividad y cookies `HttpOnly`/`SameSite=Lax`.
- Cabeceras CSP, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer` y `Permissions-Policy` restrictiva.
- Sin CDN, sin telemetría, sin comprobaciones de red externas.
- La clave secreta de Django se genera y persiste localmente en `CODEGUARD_DATA_DIR/.secret_key` (nunca se versiona).
- El renderer de Electron tiene `contextIsolation`, `sandbox` y `nodeIntegration: false`; solo se expone una API mínima por `preload.js`.
- Los enlaces externos y las ventanas nuevas se bloquean por defecto.

### Decisiones de seguridad pendientes

- **Cifrado de backups**: pendiente de decisión. Actualmente no se afirma que los backups estén cifrados.
- **RF-006 / RS-017**: el valor de `N` (número de intentos o parámetro asociado) sigue pendiente de definición.

---

## Pruebas

```bash
source .venv/bin/activate
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps
```

Cobertura actual: **26 pruebas** de identidad, auditoría, panel, carga del roadmap, prerrequisitos, progreso y vistas.

---

## Construcción del paquete Windows

El flujo tiene dos etapas:

1. **PyInstaller** genera un servidor Django autónomo en `dist-server/CodeGuardServer/`.
2. **electron-builder** empaqueta Electron + el servidor en un instalador NSIS y una versión portable.

En Windows:

```bat
build_windows.bat
```

Salidas esperadas:

```
dist-server\CodeGuardServer\CodeGuardServer.exe
dist\CodeGuard-Pro-1.0.0-x64.exe
dist\CodeGuard-Pro-1.0.0-portable.exe
```

El servidor empaquetado se copia a `resources/server` dentro de la aplicación. Al arrancar, Electron le pasa un puerto libre y `CODEGUARD_DATA_DIR` apunta a `%APPDATA%\CodeGuard Pro`.

> **Importante:** no es posible generar un `.exe` nativo de Windows desde Fedora sin toolchain cruzado. El build debe ejecutarse en Windows. Consulta `README_WINDOWS.md` para el detalle.

---

## Estructura del repositorio

```
CodeGuard/
├── apps/
│   ├── accounts/       # Identidad, sesión y frase de rescate
│   ├── audit/          # Auditoría de eventos
│   ├── core/           # Panel y configuración del sistema
│   └── roadmaps/       # ASCENSO: modelos, servicios, vistas y datos
│       └── data/ascenso_3_1.json
├── config/
│   ├── settings/       # base, development y desktop
│   ├── middleware.py   # Inactividad, cabeceras y setup inicial
│   ├── urls.py
│   └── wsgi.py
├── electron/
│   ├── main.js         # Proceso principal: ventana, servidor, menú
│   └── preload.js      # Puente IPC seguro
├── templates/          # Plantillas semánticas Django
├── static/             # CSS, JS, fuentes e iconos locales
├── docs/               # Arquitectura, seguridad, modelo de datos, etc.
├── scripts/            # Extracción del DOCX oficial a JSON
├── desktop/            # Implementación PySide6 legada (referencia)
├── server_entry.py     # Entrada del servidor empaquetado
├── CodeGuardServer.spec
├── build_windows.bat
├── run.sh
├── manage.py
├── requirements.txt
├── package.json
├── README.md
├── README_WINDOWS.md
├── IEEE830.md
└── IEEE830 (1).pdf     # Documento original, sin modificar
```

`desktop/` y `CodeGuard.spec` se conservan como referencia histórica de la etapa PySide6/Qt. La ruta soportada y empaquetada es **Electron + Django**.

---

## Documentación

- [`IEEE830.md`](IEEE830.md) — Especificación de requisitos (SRS), actualizada a la arquitectura Electron + Django.
- [`README_WINDOWS.md`](README_WINDOWS.md) — Guía de construcción y distribución para Windows.
- [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md) — Arquitectura y decisiones técnicas.
- [`docs/MODELO_DATOS.md`](docs/MODELO_DATOS.md) — Modelo de datos.
- [`docs/MATRIZ_TRAZABILIDAD.md`](docs/MATRIZ_TRAZABILIDAD.md) — Trazabilidad requisitos → implementación.
- [`docs/PLAN_DESARROLLO.md`](docs/PLAN_DESARROLLO.md) — Plan por incrementos.
- [`docs/SEGURIDAD.md`](docs/SEGURIDAD.md) — Requisitos y medidas de seguridad.
- [`docs/INSTALACION.md`](docs/INSTALACION.md) — Instalación y operación.
- [`docs/MANUAL_USUARIO.md`](docs/MANUAL_USUARIO.md) — Manual de usuario.

El PDF original `IEEE830 (1).pdf` se conserva intacto como evidencia documental.

---

## Licencia

MIT. Consulta el archivo de licencia del repositorio.
