# CodeGuard Pro — instalación y entorno de desarrollo

**Estado:** guía de desarrollo. La instalación limpia de los paquetes de escritorio todavía no está aceptada; consulta el [informe QA](INFORME_QA_INTEGRAL_2026-11-16.md). No utilizar estas instrucciones como declaración de que existe una release estable.

## 1. Plataformas

| Plataforma | Estado |
|---|---|
| Linux x64 | AppImage configurado; aceptación de primer arranque/GUI/offline pendiente |
| Windows x64 | Script de build e instalador configurados; instalación limpia pendiente |
| macOS | No configurado ni validado |
| ARM64 | No configurado ni validado |

El artefacto de cada sistema debe construirse en un entorno compatible con su plataforma. No se debe asumir que un paquete x64 funciona en ARM64.

## 2. Requisitos para desarrollar

- Git.
- Python compatible con las versiones fijadas en `requirements.txt`.
- Node.js/npm compatibles con `package-lock.json`.
- Herramientas nativas de construcción requeridas por Electron Builder/PyInstaller para el sistema destino.

El usuario final de un instalador aceptado no debería necesitar Python, Node.js, Django ni el entorno virtual del desarrollador.

## 3. Clonar y preparar dependencias

Linux:

```bash
git clone https://github.com/MaverickBms/CodeGuard-Pro.git
cd CodeGuard-Pro

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

npm ci
```

Windows PowerShell:

```powershell
git clone https://github.com/MaverickBms/CodeGuard-Pro.git
Set-Location CodeGuard-Pro

py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

npm ci
```

## 4. Base de datos de desarrollo aislada

No ejecutar migraciones ni cargas sobre la base personal del usuario durante pruebas. Mantener los datos locales fuera del repositorio.

Linux:

```bash
export CODEGUARD_DATA_DIR="$PWD/.local-data"
mkdir -p "$CODEGUARD_DATA_DIR"

./.venv/bin/python manage.py migrate \
  --settings=config.settings.development

./.venv/bin/python manage.py cargar_ascenso \
  --settings=config.settings.development
```

Windows PowerShell:

```powershell
$env:CODEGUARD_DATA_DIR = Join-Path $PWD ".local-data"
New-Item -ItemType Directory -Force $env:CODEGUARD_DATA_DIR | Out-Null

.\.venv\Scripts\python.exe manage.py migrate --settings=config.settings.development
.\.venv\Scripts\python.exe manage.py cargar_ascenso --settings=config.settings.development
```

La carga de ASCENSO debe ser idempotente y reportar los conteos esperados (33 etapas, 212 módulos y 1.946 lecciones). No usar `--recrear` sobre datos existentes.

## 5. Ejecutar en desarrollo

Con dependencias instaladas, base aislada inicializada y `CODEGUARD_DATA_DIR` establecido en la misma terminal:

```bash
npm start
```

El modo de desarrollo de Electron y el servidor local deben utilizar el mismo directorio de datos. Si el servidor no inicia, conservar la salida completa y los logs antes de cambiar configuración.

El lanzador `run.sh` existente es un flujo específico de AppImage y está sujeto a los hallazgos de inicialización descritos en el informe QA. No utilizarlo como prueba de instalación limpia hasta corregir y aceptar ese flujo.

## 6. Comprobaciones

```bash
./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
./.venv/bin/python -m pip check
./.venv/bin/python manage.py test \
  apps.core apps.accounts apps.audit apps.roadmaps \
  apps.tutoring apps.gamification apps.challenges \
  --settings=config.settings.development
```

La cifra de 245 pruebas OK está reportada en el README al 16-11-2026, pero debe reproducirse en el HEAD actual antes de usarla como línea base de release. Estas pruebas no sustituyen la aceptación de Electron, GUI, cierre limpio, offline y persistencia.

## 7. Construcción de paquetes

- Windows x64: `build_windows.bat`.
- Linux x64: `npm run build:linux` después de generar el servidor con PyInstaller según el flujo vigente.

Los comandos anteriores generan artefactos; no demuestran que el instalador pueda inicializar una base vacía. No distribuir paquetes hasta completar los criterios de aceptación del informe QA.

## 8. Datos y privacidad

El directorio runtime contiene SQLite, claves locales, logs y archivos del estudiante. Debe estar fuera del repositorio y no sincronizarse con Git.

- No compartir `.local-data/`, `.env`, bases SQLite ni logs.
- No configurar servicios remotos como requisito del modo offline.
- El tutor Ollama es opcional; la aplicación debe seguir operativa sin el modelo.
- No habilitar ejecución arbitraria de código sin sandbox auditado.
