# Correcciones P0 — inicialización del primer arranque

**Rama:** `fix/p0-first-run-initialization`  
**Alcance:** inicialización de datos y comprobación de disponibilidad del servidor local.

## Comportamiento nuevo

1. Electron inicia el ejecutable Django con `CODEGUARD_DATA_DIR` apuntando al perfil de usuario.
2. Antes de abrir Waitress, `server_entry.py` ejecuta `migrate` y después `cargar_ascenso`.
3. La carga del roadmap utiliza el modo idempotente predeterminado. No se invoca `--recrear`; el progreso del usuario no se elimina.
4. El modo aislado `--sync-knowledge` conserva su comportamiento y no ejecuta migraciones ni carga el roadmap.
5. El build de Windows deja de crear una base de datos de desarrollo. La base real se inicializa en el primer arranque de cada usuario.
6. `run.sh` deja de ejecutar migraciones y sembrar ASCENSO por separado; el servidor empaquetado es el único responsable de inicializar el perfil.
7. Electron espera `GET /healthz/` y solo considera listo el servidor cuando la base de datos responde, no hay migraciones pendientes y existe un roadmap activo.
8. El tutor solo admite Ollama en loopback, ignora proxies del entorno y rechaza redirecciones para evitar que el código del estudiante se envíe a un host remoto.
9. La reserva del número de pista usa una actualización condicional atómica dentro de una transacción; el límite de tres se vuelve a comprobar en la base de datos y se conserva la unicidad `(sesion, numero_pista)`.

## Verificación local pendiente

La modificación remota no equivale a una ejecución de pruebas. En Linux, actualizar la rama y ejecutar:

```bash
cd ~/Documentos/CodeGuard
git fetch origin
git switch fix/p0-first-run-initialization
git pull --ff-only origin fix/p0-first-run-initialization

./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
CODEGUARD_DATA_DIR="$(mktemp -d)" ./.venv/bin/python manage.py test apps.roadmaps.tests.test_server_entry apps.core.tests.test_health apps.tutoring.tests.test_tutoria --settings=config.settings.development
node --check electron/main.js
```

Para probar la inicialización empaquetada, generar el servidor y arrancar Electron con un directorio de datos temporal vacío. Confirmar que aparecen `db.sqlite3`, `.secret_key`, `logs/` y el roadmap de 33 etapas; cerrar y abrir de nuevo y verificar que el progreso permanece intacto.

En Windows, construir NSIS/portable y probar ambos con un perfil de usuario nuevo. El build ya no debe ejecutar migraciones ni sembrar datos en la máquina de construcción.

## Flujo de empaquetado protegido

Los comandos de distribución pasan obligatoriamente por el mismo flujo:

```bash
npm run build:server
npm run verify:server
npm run build:linux  # o build:win; ambos reconstruyen y verifican antes de empaquetar
```

`npm run build:server` elimina el ejecutable anterior y su manifiesto, ejecuta PyInstaller con `--distpath dist-server` y genera un manifiesto SHA-256 fuera de la carpeta que electron-builder copia a `resources/server`. Si PyInstaller falla, no se crea un manifiesto válido. `npm run verify:server` exige ejecutable, manifiesto, plataforma/nombre esperados y coincidencia SHA-256. Los scripts `build`, `build:linux` y `build:win` encadenan generación, verificación y electron-builder mediante `&&`; cualquier fallo detiene el empaquetado. `build_windows.bat` delega en `npm run build:win` y no mantiene una segunda invocación independiente de PyInstaller.

No ejecutar `electron-builder` directamente para crear artefactos distribuibles, porque ese comando aislado no ejecuta la protección anterior.

## Límites

- No se habilita ejecución arbitraria de código.
- No se configura hosting, sincronización remota ni claves de distribución.
- No se considera aceptada la distribución hasta completar pruebas reales en Linux y Windows.
- Las pruebas de concurrencia con múltiples procesos SQLite y la comprobación de redirecciones HTTP deben ejecutarse también en el entorno objetivo.
