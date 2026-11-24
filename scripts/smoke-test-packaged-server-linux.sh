#!/usr/bin/env bash
# Smoke test del servidor PyInstaller en Linux.
#
# Fase 1: primer arranque con perfil vacío, migraciones, carga ASCENSO y
#         /healthz/ en 127.0.0.1 hasta obtener los cuatro estados "ok".
# Fase 2: el modo --sync-knowledge carga Django y falla de forma controlada
#         cuando falta la configuración de distribución (sin URLs ni claves).
set -euo pipefail

SERVER_BIN="${1:-dist-server/CodeGuardServer/CodeGuardServer}"
if [[ ! -x "$SERVER_BIN" ]]; then
  echo "[ERROR] No se encuentra un ejecutable PyInstaller: $SERVER_BIN" >&2
  exit 2
fi

TEMP_ROOT="$(mktemp -d)"
SERVER_PID=""
cleanup() {
  if [[ -n "$SERVER_PID" ]] && kill -0 "$SERVER_PID" 2>/dev/null; then
    kill -TERM "$SERVER_PID" 2>/dev/null || true
    wait "$SERVER_PID" 2>/dev/null || true
  fi
  rm -rf "$TEMP_ROOT"
}
trap cleanup EXIT

export CODEGUARD_DATA_DIR="$TEMP_ROOT/data"
export DJANGO_SETTINGS_MODULE="config.settings.desktop"

# --- Fase 1: primer arranque y health check ---------------------------------
HEALTH_PORT=$((20000 + RANDOM % 20000))
export CODEGUARD_PORT="$HEALTH_PORT"
"$SERVER_BIN" >"$TEMP_ROOT/server.log" 2>&1 &
SERVER_PID=$!

HEALTH_OK=0
for _ in $(seq 1 90); do
  if curl -fsS --max-time 2 "http://127.0.0.1:${HEALTH_PORT}/healthz/" \
      >"$TEMP_ROOT/health.json" 2>/dev/null; then
    HEALTH_OK=1
    break
  fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    break
  fi
  sleep 1
done

if [[ "$HEALTH_OK" -ne 1 ]]; then
  echo "[ERROR] El servidor no alcanzó /healthz/ en 90 s." >&2
  tail -40 "$TEMP_ROOT/server.log" >&2 || true
  exit 1
fi

for clave in '"status": "ok"' '"database": "ok"' '"migrations": "ok"' '"roadmap": "ok"'; do
  if ! grep -q "$clave" "$TEMP_ROOT/health.json"; then
    echo "[ERROR] Health check incompleto: falta $clave" >&2
    cat "$TEMP_ROOT/health.json" >&2
    exit 1
  fi
done

if [[ ! -f "$TEMP_ROOT/data/db.sqlite3" ]]; then
  echo "[ERROR] El servidor no creó la base en CODEGUARD_DATA_DIR." >&2
  exit 1
fi

kill -TERM "$SERVER_PID" 2>/dev/null || true
wait "$SERVER_PID" 2>/dev/null || true
SERVER_PID=""

if curl -fsS --max-time 2 "http://127.0.0.1:${HEALTH_PORT}/healthz/" >/dev/null 2>&1; then
  echo "[ERROR] El puerto sigue abierto después de detener el servidor." >&2
  exit 1
fi

echo "[OK] Primer arranque: migraciones, ASCENSO y health check correctos."

# --- Fase 2: sincronización sin configuración --------------------------------
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
