#!/bin/bash
# =============================================================================
# CodeGuard Pro — Lanzador Linux del AppImage empaquetado
#
# No requiere Python, Node.js, Django ni un entorno virtual en el equipo usuario:
# el servidor Django ya está incluido en el AppImage y prepara su perfil local.
# =============================================================================
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# electron-builder puede generar nombres con arch x64 o x86_64 según configuración/versión.
shopt -s nullglob
APPIMAGES=(dist/CodeGuard-Pro-*-x64.AppImage dist/CodeGuard-Pro-*-x86_64.AppImage)
shopt -u nullglob

# Deduplicar por si algún patrón coincidiera de forma redundante
if [ "${#APPIMAGES[@]}" -gt 0 ]; then
    mapfile -t APPIMAGES < <(printf '%s\n' "${APPIMAGES[@]}" | awk '!seen[$0]++')
fi

if [ "${#APPIMAGES[@]}" -eq 0 ]; then
    echo "[CodeGuard] ERROR: No se encuentra el AppImage en dist/ (esperado: CodeGuard-Pro-*-x64.AppImage o CodeGuard-Pro-*-x86_64.AppImage)."
    echo "[CodeGuard] Genera primero el paquete con: npm run build:linux"
    exit 1
fi

if [ "${#APPIMAGES[@]}" -ne 1 ]; then
    echo "[ERROR] Se encontraron varios AppImage en dist/."
    echo "        Conserva un único artefacto o limpia dist/ antes de iniciar."
    printf '        - %s\n' "${APPIMAGES[@]}"
    exit 1
fi

APPIMAGE="${APPIMAGES[0]}"

# Fallback para sistemas con FUSE lento o restringido: extrae el AppImage a
# un directorio temporal antes de ejecutarlo. Útil en contenedores, sistemas
# con memoria ajustada o cuando el AppImage se queda bloqueado al montar.
if [ "${CODEGUARD_APPIMAGE_EXTRACT:-0}" = "1" ]; then
    export APPIMAGE_EXTRACT_AND_RUN=1
    echo "Modo extracción activado (CODEGUARD_APPIMAGE_EXTRACT=1)."
fi

# Misma ruta que app.getPath('userData') de Electron para que abrir el
# AppImage directamente o mediante ./codeguard use el mismo perfil.
CONFIG_HOME="${XDG_CONFIG_HOME:-$HOME/.config}"
DATA_DIR="${CONFIG_HOME}/CodeGuard Pro"
LEGACY_DATA_DIR="${CONFIG_HOME}/Code Guard Pro/data"
if [ -f "$LEGACY_DATA_DIR/db.sqlite3" ] && [ ! -f "$DATA_DIR/db.sqlite3" ]; then
    DATA_DIR="$LEGACY_DATA_DIR"
    echo "Perfil heredado detectado: $DATA_DIR"
fi
mkdir -p "$DATA_DIR"
export CODEGUARD_DATA_DIR="$DATA_DIR"

echo "=============================================="
echo "   CodeGuard Pro — Inicio"
echo "=============================================="
echo "AppImage: $APPIMAGE"
echo "Datos:    $CODEGUARD_DATA_DIR"
echo ""
echo "El servidor local inicializará el perfil al arrancar."
echo "Usa --ozone-platform=x11 para compatibilidad con Wayland."
echo "Si el AppImage se bloquea al montar, ejecuta: CODEGUARD_APPIMAGE_EXTRACT=1 ./run.sh"
echo ""

if [ -t 1 ]; then
  echo "[CodeGuard] Iniciando CodeGuard Pro..."
fi
exec "$APPIMAGE" --ozone-platform=x11 "$@"
