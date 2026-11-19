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

# electron-builder genera CodeGuard-Pro-<version>-x64.AppImage
# (la arquitectura configurada en package.json es x64, no x86_64).
shopt -s nullglob
APPIMAGES=(dist/CodeGuard-Pro-*-x64.AppImage)
shopt -u nullglob

if [ "${#APPIMAGES[@]}" -eq 0 ]; then
    echo "[ERROR] No se encuentra el AppImage x64 en dist/."
    echo "        Genera primero el paquete con: npm run build:linux"
    exit 1
fi

if [ "${#APPIMAGES[@]}" -ne 1 ]; then
    echo "[ERROR] Se encontraron varios AppImage x64 en dist/."
    echo "        Conserva un único artefacto o limpia dist/ antes de iniciar."
    printf '        - %s\n' "${APPIMAGES[@]}"
    exit 1
fi

APPIMAGE="${APPIMAGES[0]}"
DATA_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/Code Guard Pro/data"
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
echo ""

exec "$APPIMAGE" --ozone-platform=x11 "$@"
