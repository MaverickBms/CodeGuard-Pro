#!/usr/bin/env bash
# Smoke test del servidor PyInstaller en Linux.
# Comprueba que el binario carga Django y alcanza el comando de sincronización
# sin requerir URLs ni claves reales. La salida de configuración incompleta
# es intencional; ModuleNotFoundError u otro fallo de importación no lo es.
set -euo pipefail

SERVER_BIN="${1:-dist-server/CodeGuardServer/CodeGuardServer}"
if [[ ! -x "$SERVER_BIN" ]]; then
  echo "[ERROR] No se encuentra un ejecutable PyInstaller: $SERVER_BIN" >&2
  exit 2
fi

TEMP_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEMP_ROOT"' EXIT

export CODEGUARD_DATA_DIR="$TEMP_ROOT/data"
export DJANGO_SETTINGS_MODULE="config.settings.desktop"
unset CODEGUARD_SYNC_MANIFEST_URL CODEGUARD_SYNC_SIGNATURE_URL
unset CODEGUARD_SYNC_ALLOWED_HOSTS CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS
unset CODEGUARD_SYNC_TIMEOUT CODEGUARD_APP_VERSION
export CODEGUARD_SYNC_CHANNEL="stable"
export CODEGUARD_SYNC_FORCE="0"

set +e
OUTPUT="$("$SERVER_BIN" --sync-knowledge 2>&1)"
STATUS=$?
set -e

if [[ "$STATUS" -eq 0 ]]; then
  echo "[ERROR] El binario aceptó una configuración de sincronización incompleta." >&2
  echo "$OUTPUT" >&2
  exit 1
fi

if grep -Eqi "ModuleNotFoundError|ImportError|No module named" <<<"$OUTPUT"; then
  echo "[ERROR] Falló la carga de módulos dentro del binario." >&2
  echo "$OUTPUT" >&2
  exit 1
fi

if ! grep -q "CODEGUARD_SYNC_MANIFEST_URL" <<<"$OUTPUT"; then
  echo "[ERROR] El binario no alcanzó la validación de configuración del comando." >&2
  echo "$OUTPUT" >&2
  exit 1
fi

echo "[OK] PyInstaller carga Django y ejecuta sincronizar_conocimiento."
echo "[OK] El comando falla de forma controlada cuando faltan endpoints y claves."
