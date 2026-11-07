#!/bin/bash
# =============================================================================
# CodeGuard Pro — Script de ejecución para Linux
# Arquitectura: Electron + Django API local
#
# Electron es el único responsable de iniciar y detener el servidor Django
# (ver electron/main.js). Este script solo prepara el entorno y lanza Electron,
# evitando así dos procesos Django compitiendo por el mismo puerto.
# =============================================================================

set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

echo "============================================="
echo "   CodeGuard Pro — Iniciando aplicación"
echo "============================================="

# --- Verificar Python ---
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 no está instalado."
    exit 1
fi

# --- Verificar Node.js ---
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js no está instalado."
    exit 1
fi

# --- Activar entorno virtual si existe ---
PYTHON="python3"
if [ -d ".venv" ]; then
    echo "[INFO] Activando entorno virtual Python..."
    # shellcheck disable=SC1091
    source .venv/bin/activate
    PYTHON=".venv/bin/python"
fi

# --- Instalar dependencias Python si es necesario ---
echo "[INFO] Verificando dependencias Python..."
if ! "$PYTHON" -c "import django" 2>/dev/null; then
    echo "[INFO] Instalando dependencias Python..."
    "$PYTHON" -m pip install -r requirements.txt
fi

# --- Directorio de datos (misma base de datos que usará Electron) ---
export CODEGUARD_DATA_DIR="$PWD/data"

# --- Aplicar migraciones de Django ---
echo "[INFO] Aplicando migraciones de Django en $CODEGUARD_DATA_DIR..."
"$PYTHON" manage.py migrate --settings=config.settings.development

# --- Cargar el roadmap oficial si aún no existe ---
echo "[INFO] Verificando roadmap ASCENSO..."
"$PYTHON" manage.py cargar_ascenso --settings=config.settings.development >/dev/null 2>&1 || true

# --- Instalar dependencias Node.js si es necesario ---
echo "[INFO] Verificando dependencias Node.js..."
if [ ! -d "node_modules" ]; then
    echo "[INFO] Instalando dependencias Node.js..."
    npm install
fi

# --- Crear .env si no existe ---
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo "[INFO] Creando .env desde .env.example..."
        cp .env.example .env
    fi
fi

# --- Iniciar Electron (él inicia y detiene Django) ---
echo "[INFO] Iniciando aplicación Electron..."
npm start

echo "============================================="
echo "   CodeGuard Pro — Cerrado correctamente"
echo "============================================="
