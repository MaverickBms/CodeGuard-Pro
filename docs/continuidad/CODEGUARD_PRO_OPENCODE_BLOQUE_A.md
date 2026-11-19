# ORDEN DE TRABAJO PARA OPENCODE — CODEGUARD PRO / BLOQUE A

Lee primero el documento `CODEGUARD_PRO_CONTINUIDAD_HANDOFF_2026-11-18.md` completo. Si no está en el repositorio, el propietario debe copiarlo a la raíz o proporcionártelo como contexto.

## Objetivo

Validar y, solo si se reproducen defectos, corregir el primer arranque de CodeGuard Pro empaquetado en Linux x64. Trabaja sobre el checkout local del propietario. No reconstruyas la aplicación ni cambies su arquitectura.

## Reglas obligatorias

1. Antes de hacer nada, ejecuta y registra:
   - `pwd`
   - `git status --short --branch`
   - `git rev-parse HEAD`
   - `git branch --show-current`
   - `git log -5 --oneline --decorate`
2. No sobrescribas ni limpies cambios locales preexistentes. Si el árbol está sucio, identifica cada cambio y protégelo. No uses `git reset --hard`, `git clean`, `git checkout -- .` ni `git restore` indiscriminadamente.
3. No uses la base de datos habitual ni el perfil real. Crea un perfil de prueba nuevo y aislado en `/tmp` con un nombre único. Antes de reutilizar cualquier ruta, comprueba que no exista y no contenga datos ajenos.
4. No ejecutes `cargar_ascenso --recrear`.
5. No hagas commits, pushes, merges, tags, releases ni despliegues.
6. No cambies dependencias ni arquitectura sin demostrar necesidad.
7. No afirmes que una prueba pasó si no ejecutaste el comando y observaste el resultado.
8. Si el perfil temporal ya existe, no lo borres: selecciona otro directorio.
9. No uses el modo `--sync-knowledge` como sustituto de probar el servidor normal.
10. Si un defecto exige cambios, primero documenta la causa, archivos afectados, impacto y plan de rollback. Haz el cambio mínimo y añade una prueba de regresión.

## Paso 1 — Inspección del entorno

Comprueba disponibilidad de:
- Linux x64;
- Node.js y npm;
- Python/venv del proyecto;
- dependencias instaladas;
- artefacto AppImage disponible;
- `dist-server/CodeGuardServer` y manifiesto/hash si el flujo local los requiere.

No instales ni actualices dependencias sin justificarlo. No cambies `.env` ni configuraciones del propietario.

Ejecuta, si el entorno está preparado:

```bash
./.venv/bin/python manage.py check --settings=config.settings.development
./.venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
./.venv/bin/python -m pip check
node --check electron/main.js
node --check electron/preload.js
```

Registra cada salida y código de retorno.

## Paso 2 — Suite automatizada

Ejecuta:

```bash
./.venv/bin/python manage.py test \
  apps.core apps.accounts apps.audit apps.roadmaps \
  apps.tutoring apps.gamification apps.challenges \
  --settings=config.settings.development
```

Registra el total real de pruebas, duración, resultado final, commit y entorno. No presupongas que deben ser 245.

Si falla:
- captura el error completo;
- identifica si es defecto, dependencia ausente, configuración o problema de entorno;
- no ocultes el fallo;
- corrige únicamente si la causa está demostrada;
- repite las pruebas afectadas y la suite relevante.

## Paso 3 — Perfil temporal aislado

Crea una ruta temporal nueva, por ejemplo:

```bash
TEST_ROOT="$(mktemp -d /tmp/codeguard-beta-first-run.XXXXXX)"
printf '%s\n' "$TEST_ROOT"
mkdir -p "$TEST_ROOT/data" "$TEST_ROOT/home"
```

Conserva la ruta y no borres el perfil al finalizar. No uses el HOME real como destino de datos. Revisa `run.sh`, `electron/main.js` y `server_entry.py` para confirmar cómo se propaga `CODEGUARD_DATA_DIR` al AppImage. No inicialices el perfil real.

## Paso 4 — Build solo si hace falta y si el entorno está preparado

Si no existe artefacto reciente o el servidor empaquetado no contiene el HEAD local, usa el pipeline verificado:

```bash
npm run build:linux
```

No ejecutes `electron-builder` aislado. Si falta una dependencia, detente y documenta el bloqueo antes de instalar.

Registra artefacto exacto, tamaño, fecha y hash SHA-256.

## Paso 5 — Aceptación funcional del primer arranque

Ejecuta la aplicación empaquetada con el perfil temporal, nunca con el perfil real.

Verifica:
- proceso `CodeGuardServer` inicia;
- Waitress escucha únicamente en `127.0.0.1`;
- `/healthz/` devuelve HTTP 200 y los indicadores `database`, `migrations`, `roadmap` en `ok`;
- Electron muestra el dashboard;
- se puede navegar a ASCENSO y abrir una lección con contenido disponible;
- se puede completar una operación educativa disponible y observar persistencia;
- al cerrar desde el menú, se terminan los procesos hijos y se libera el puerto;
- al volver a abrir con el mismo perfil, el progreso permanece;
- con conectividad desactivada, los flujos locales esenciales siguen funcionando.

No inventes datos ni alteres el perfil de usuario real. Si el contenido no permite completar un flujo, registra la limitación.

## Paso 6 — Informe de salida

Entrega un informe en texto con:
1. SHA y rama local.
2. Estado inicial de Git.
3. Entorno detectado.
4. Comandos ejecutados y resultados exactos.
5. Pruebas unitarias y total real.
6. Artefacto y SHA-256.
7. Perfil temporal utilizado.
8. Resultado de cada criterio de aceptación.
9. Errores y causa raíz.
10. Archivos modificados y diff resumido (si hubo cambios).
11. Riesgos y limitaciones pendientes.
12. Siguiente acción recomendada.

No declares Bloque A aceptado si no se verificaron la GUI, el health check, el cierre normal y la persistencia tras reinicio.

## Paso 7 — Documentación

Actualiza el informe de continuidad y los documentos rectores de la rama documental de forma selectiva. La rama `documentation` estaba 125 commits detrás de `main` en la revisión del 18-11-2026: no hagas merge completo ni copies archivos sin comparar. No publiques commits ni pushes. Deja los cambios documentales locales listos para revisión del propietario.

**Resultado esperado:** evidencia reproducible del arranque empaquetado o un informe preciso de por qué no pudo completarse. No es aceptable sustituir la prueba real por una revisión estática.