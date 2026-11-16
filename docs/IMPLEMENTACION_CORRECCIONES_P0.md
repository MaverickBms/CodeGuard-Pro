# Correcciones P0 — inicialización del primer arranque

**Rama:** `fix/p0-first-run-initialization`  
**Alcance:** inicialización de datos y comprobación de disponibilidad del servidor local.

## Comportamiento nuevo

1. Electron inicia el ejecutable Django con `CODEGUARD_DATA_DIR` apuntando al perfil de usuario.
2. Antes de abrir Waitress, `server_entry.py` ejecuta `migrate` y después `cargar_ascenso`.
3. La carga del roadmap utiliza el modo idempotente predeterminado. No se invoca `--recrear`; el progreso del usuario no se elimina.
4. El modo aislado `--sync-knowledge` conserva su comportamiento y no ejecuta migraciones ni carga el roadmap.
5. El build de Windows deja de crear una base de datos de desarrollo. La base real se inicializa en el primer arranque de cada usuario.
6. Electron espera `GET /healthz/` y solo considera listo el servidor cuando la base de datos responde, no hay migraciones pendientes y existe un roadmap activo.

## Verificación local pendiente

La modificación remota no equivale a una ejecución de pruebas. En Linux, actualizar la rama y ejecutar:

```bash
cd ~/Documentos/CodeGuard
git fetch origin
git switch fix/p0-first-run-initialization
git pull --ff-only origin fix/p0-first-run-initialization

./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
CODEGUARD_DATA_DIR="$(mktemp -d)" ./.venv/bin/python manage.py test apps.roadmaps.tests.test_server_entry apps.core.tests.test_health --settings=config.settings.development
node --check electron/main.js
```

Para probar la inicialización empaquetada, generar el servidor y arrancar Electron con un directorio de datos temporal vacío. Confirmar que aparecen `db.sqlite3`, `.secret_key`, `logs/` y el roadmap de 33 etapas; cerrar y abrir de nuevo y verificar que el progreso permanece intacto.

En Windows, construir NSIS/portable y probar ambos con un perfil de usuario nuevo. El build ya no debe ejecutar migraciones ni sembrar datos en la máquina de construcción.

## Límites

- No se habilita ejecución arbitraria de código.
- No se configura hosting, sincronización remota ni claves de distribución.
- No se considera aceptada la distribución hasta completar pruebas reales en Linux y Windows.
