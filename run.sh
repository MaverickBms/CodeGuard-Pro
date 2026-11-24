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

APPIMAGE="$PROJECT_DIR/${APPIMAGES[0]}"

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

# Rendimiento: extraer AppImage a caché evita latencia de FUSE (PyInstaller/Electron
# hacen muchas lecturas aleatorias). Se reutiliza la extracción mientras el AppImage
# no cambie. Opt-out: CODEGUARD_APPIMAGE_NO_EXTRACT=1 ./codeguard
USE_FUSE="${CODEGUARD_APPIMAGE_NO_EXTRACT:-0}"
CACHE_HOME="${XDG_CACHE_HOME:-$HOME/.cache}"
APPIMAGE_BASENAME="$(basename "$APPIMAGE")"
APPIMAGE_ID="$(stat -c '%s-%Y' "$APPIMAGE" 2>/dev/null || stat -f '%z-%m' "$APPIMAGE" 2>/dev/null || echo unknown)"
EXTRACT_DIR="$CACHE_HOME/codeguard-pro/extracted/${APPIMAGE_BASENAME}.${APPIMAGE_ID}"

resolve_extracted_app() {
  local dir="$1"
  if [ -x "$dir/AppRun" ]; then echo "$dir/AppRun"; return 0; fi
  if [ -x "$dir/codeguard-pro" ]; then echo "$dir/codeguard-pro"; return 0; fi
  local found
  found="$(find "$dir" -maxdepth 2 -type f \( -name 'AppRun' -o -name 'codeguard-pro' \) -perm -u+x 2>/dev/null | head -1 || true)"
  if [ -n "$found" ]; then echo "$found"; return 0; fi
  return 1
}

LAUNCH_CMD=("$APPIMAGE")
if [ "$USE_FUSE" != "1" ]; then
  mkdir -p "$CACHE_HOME/codeguard-pro/extracted"
  CACHED_APP="$(resolve_extracted_app "$EXTRACT_DIR" 2>/dev/null || true)"
  if [ -z "$CACHED_APP" ]; then
    echo "[CodeGuard] Extrayendo AppImage a caché para mejor rendimiento..."
    rm -rf "$EXTRACT_DIR"
    mkdir -p "$EXTRACT_DIR"
    if (cd "$EXTRACT_DIR" && "$APPIMAGE" --appimage-extract >/dev/null 2>&1); then
      # --appimage-extract crea squashfs-root dentro del cwd
      if [ -d "$EXTRACT_DIR/squashfs-root" ]; then
        mv "$EXTRACT_DIR/squashfs-root" "$EXTRACT_DIR/root"
      fi
      CACHED_APP="$(resolve_extracted_app "$EXTRACT_DIR/root" 2>/dev/null || resolve_extracted_app "$EXTRACT_DIR" 2>/dev/null || true)"
    else
      echo "[CodeGuard] Extracción falló; usando FUSE/montaje."
      rm -rf "$EXTRACT_DIR"
      CACHED_APP=""
    fi
    # Limpiar cachés viejas del mismo nombre base
    find "$CACHE_HOME/codeguard-pro/extracted" -mindepth 1 -maxdepth 1 -type d -name "${APPIMAGE_BASENAME}.*" ! -path "$EXTRACT_DIR" -exec rm -rf {} + 2>/dev/null || true
  fi
  if [ -n "$CACHED_APP" ]; then
    LAUNCH_CMD=("$CACHED_APP")
    echo "[CodeGuard] Usando AppImage extraído en caché."
  fi
else
  echo "Modo FUSE/montaje activado (CODEGUARD_APPIMAGE_NO_EXTRACT=1)."
fi

echo "=============================================="
echo "   CodeGuard Pro — Inicio"
echo "=============================================="
echo "AppImage: $APPIMAGE"
echo "Datos:    $CODEGUARD_DATA_DIR"
if [ "$USE_FUSE" != "1" ] && [ "${LAUNCH_CMD[0]}" != "$APPIMAGE" ]; then
  echo "Caché:    $EXTRACT_DIR"
fi
echo ""
echo "El servidor local inicializará el perfil al arrancar."
echo "Usa --ozone-platform=x11 para compatibilidad con Wayland."
echo ""

if [ -t 1 ]; then
  echo "[CodeGuard] Iniciando CodeGuard Pro..."
fi
exec "${LAUNCH_CMD[@]}" --ozone-platform=x11 "$@"
