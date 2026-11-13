#!/bin/bash
# =============================================================================
# CodeGuard Pro — Script de ejecución para Linux
# Arquitectura: Electron + Django API local (empaquetado con PyInstaller)
#
# Electron inicia el servidor Django empaquetado (CodeGuardServer) dentro
# del AppImage. Este script prepara el entorno (migraciones + roadmap) y
# lanza el AppImage con --ozone-platform=x11 para evitar problemas de Wayland.
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

# --- Directorio de datos del AppImage (empaquetado) ---
# El AppImage empaquetado usa ~/.config/Code Guard Pro/data
DATA_DIR="$HOME/.config/Code Guard Pro/data"
mkdir -p "$DATA_DIR"
export CODEGUARD_DATA_DIR="$DATA_DIR"

echo "[INFO] Directorio de datos: $DATA_DIR"

# --- Aplicar migraciones de Django ---
echo "[INFO] Aplicando migraciones de Django en $DATA_DIR..."
"$PYTHON" manage.py migrate --settings=config.settings.development 2>&1 | tail -5

# --- Cargar el roadmap oficial si aún no existe ---
echo "[INFO] Cargando roadmap ASCENSO..."
"$PYTHON" manage.py cargar_ascenso --settings=config.settings.development 2>&1 | tail -3

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

# --- Verificar que el AppImage existe ---
if [ ! -f "dist/CodeGuard-Pro-1.0.0-x86_64.AppImage" ]; then
    echo "[ERROR] No se encuentra el AppImage en dist/"
    echo "   Ejecuta primero: npm run build:linux"
    exit 1
fi

# --- Lanzar Electron (AppImage con --ozone-platform=x11 para Wayland) ---
echo ""
echo "[INFO] Iniciando aplicación Electron (AppImage)..."
echo "   Usando --ozone-platform=x11 para evitar problemas de Wayland/Vulkan"
echo ""

CODEGUARD_DATA_DIR="$DATA_DIR" \
./dist/CodeGuard-Pro-1.0.0-x86_64.AppImage --ozone-platform=x11

echo ""
echo "============================================="
echo "   CodeGuard Pro — Cerrado correctamente"
echo "============================================="