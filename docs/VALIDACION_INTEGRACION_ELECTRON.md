# Validación de integración — Electron, Django y PyInstaller

**Rama:** `test/phase-2-electron-integration`  
**Base:** `main` en `2906abc`  
**Alcance:** validación local de la aplicación empaquetada; no configura distribución remota.

## 1. Evidencia disponible

El propietario confirmó:

- 136 pruebas automatizadas OK después de corregir los imports ocultos de Django en PyInstaller y la configuración de electron-builder.
- Generación correcta de `dist-server/CodeGuardServer/CodeGuardServer`.
- Generación correcta de `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage` (Linux x86_64).
- El binario PyInstaller carga Django y alcanza `sincronizar_conocimiento`. El error por variables de sincronización ausentes es el resultado esperado cuando no se han configurado URLs, allowlist y claves.

Esta rama añade dos pruebas unitarias del modo `--sync-knowledge` y un smoke test repetible para el binario. Esas nuevas pruebas todavía deben ejecutarse localmente; por ello no se afirma que la suite tenga ya 138 pruebas aprobadas.

## 2. Actualizar la rama

```bash
cd ~/Documentos/CodeGuard

git fetch origin
git switch test/phase-2-electron-integration
git pull --ff-only origin test/phase-2-electron-integration
```

## 3. Pruebas automatizadas

Pruebas nuevas del punto de entrada empaquetado:

```bash
./.venv/bin/python manage.py test \
  apps.roadmaps.tests.test_server_entry \
  --settings=config.settings.development
```

Pruebas del cliente, instalador y despacho empaquetado:

```bash
export CODEGUARD_DATA_DIR="$PWD/data"

./.venv/bin/python manage.py test \
  apps.roadmaps.tests.test_server_entry \
  apps.roadmaps.tests.test_sync_client \
  apps.roadmaps.tests.test_installer \
  --settings=config.settings.development
```

Suite completa y controles:

```bash
./.venv/bin/python manage.py test \
  --settings=config.settings.development

./.venv/bin/python manage.py check \
  --settings=config.settings.development

./.venv/bin/python manage.py makemigrations --check --dry-run \
  --settings=config.settings.development

node --check electron/main.js
node --check electron/preload.js
bash -n scripts/smoke-test-packaged-server-linux.sh
```

La base previamente confirmada es de 136 pruebas. Las dos nuevas pruebas elevan el resultado esperado a 138 si no hay cambios adicionales en el descubrimiento de pruebas.

## 4. Smoke test del binario PyInstaller en Linux

Ejecutar desde la raíz del repositorio:

```bash
bash scripts/smoke-test-packaged-server-linux.sh \
  dist-server/CodeGuardServer/CodeGuardServer
```

Resultado esperado:

- Código de salida 0 del script.
- Mensaje `[OK] PyInstaller carga Django y ejecuta sincronizar_conocimiento.`
- Mensaje `[OK] El comando falla de forma controlada cuando faltan endpoints y claves.`
- Ningún `ModuleNotFoundError`, `ImportError` o error de módulo ausente.

El smoke test crea un directorio temporal para los datos y no usa claves reales ni realiza una descarga. La salida de configuración incompleta es deliberada.

## 5. Prueba de aceptación de la GUI empaquetada

Ejecutar en una sesión gráfica Linux. No se requiere configurar el servicio central.

1. Confirmar que existe el artefacto `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage` y que tiene permiso de ejecución.
2. Crear un directorio temporal para aislar los datos de esta prueba:
   ```bash
   TEST_DATA="$(mktemp -d)"
   CODEGUARD_DATA_DIR="$TEST_DATA" ./dist/CodeGuard-Pro-1.0.0-x86_64.AppImage
   ```
3. Confirmar que la ventana abre y carga el panel, sin depender de Python instalado en el sistema.
4. Confirmar que el servidor local escucha exclusivamente en `127.0.0.1`:
   ```bash
   ss -ltnp
   ```
   No debe existir un listener de CodeGuard en `0.0.0.0` ni en una interfaz de red externa.
5. Abrir una etapa y una lección. Verificar que el contenido local sigue disponible.
6. Cerrar la aplicación desde su menú. Esperar unos segundos y comprobar que no quedan procesos de CodeGuard huérfanos:
   ```bash
   pgrep -af 'CodeGuardServer|CodeGuard-Pro'
   ```
   La ausencia de coincidencias es el resultado esperado después del cierre.
7. Repetir el inicio con el directorio de datos habitual (sin borrar ni reemplazar la base de datos existente) y confirmar que el perfil de usuario y el progreso se conservan.
8. Mantener ausentes las variables `CODEGUARD_SYNC_MANIFEST_URL`, `CODEGUARD_SYNC_SIGNATURE_URL`, `CODEGUARD_SYNC_ALLOWED_HOSTS` y `CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS`. La aplicación debe iniciar normalmente y no intentar una conexión de actualización.

**No borrar el directorio de datos habitual.** La prueba aislada del primer arranque debe usar `TEST_DATA`; la comprobación de preservación se realiza después con el perfil real, sin operaciones destructivas.

## 6. Criterios para cerrar la integración

| Criterio | Evidencia requerida |
|---|---|
| Despacho del modo sync | Dos pruebas de `test_server_entry.py` OK |
| Suite | 138 pruebas OK o explicación documentada de cualquier variación |
| PyInstaller | Smoke test Linux OK, sin errores de importación |
| Electron empaquetado | AppImage abre la interfaz y Django local |
| Seguridad de red local | Listener únicamente en `127.0.0.1` |
| Cierre | No quedan procesos hijos huérfanos |
| Offline-first | El contenido local abre sin configuración remota |
| Datos | Perfil habitual y progreso permanecen intactos |

## 7. Fuera del alcance de esta validación

- Selección de proveedor de hosting o CDN.
- Publicación remota de manifiestos, firmas o ZIP.
- Creación o instalación de claves privadas/public keys de producción.
- Prueba de descarga real desde un endpoint externo.
- Merge a `main` o despliegue.

Esas acciones requieren decisiones y autorizaciones independientes.
