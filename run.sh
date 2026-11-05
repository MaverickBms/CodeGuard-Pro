#!/bin/bash
# =============================================================================
# CodeGuard Pro — Script de ejecución para Linux
# Arquitectura: Electron + Django API local
# =============================================================================

set -e

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
if [ -d ".venv" ]; then
    echo "[INFO] Activando entorno virtual Python..."
    source .venv/bin/activate
fi

# --- Instalar dependencias Python si es necesario ---
echo "[INFO] Verificando dependencias Python..."
if ! python3 -c "import django" 2>/dev/null; then
    echo "[INFO] Instalando dependencias Python..."
    pip install -r requirements.txt
fi

# --- Aplicar migraciones de Django ---
echo "[INFO] Aplicando migraciones de Django..."
python3 manage.py migrate --settings=config.settings.development

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

# --- Iniciar Django en segundo plano ---
echo "[INFO] Iniciando servidor Django API local (127.0.0.1:8000)..."
DJANGO_SETTINGS_MODULE=config.settings.development nohup python3 manage.py runserver 127.0.0.1:8000 > logs/django.log 2>&1 &
DJANGO_PID=$!
echo "    Django PID: $DJANGO_PID"

# Esperar a que Django esté listo
echo "[INFO] Esperando a que Django esté disponible..."
for i in $(seq 1 30); do
    if curl -s http://127.0.0.1:8000/ > /dev/null 2>&1; then
        echo "[INFO] Django está listo."
        break
    fi
    sleep 1
done

# --- Iniciar Electron ---
echo "[INFO] Iniciando aplicación Electron..."
npm start

# --- Detener Django al salir ---
echo "[INFO] Deteniendo servidor Django..."
kill $DJANGO_PID 2>/dev/null || true

echo "============================================="
echo "   CodeGuard Pro — Cerrado correctamente"
echo "============================================="
