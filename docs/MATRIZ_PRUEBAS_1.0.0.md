# Matriz de pruebas de CodeGuard Pro 1.0.0

**Fecha:** 2026-11-21
**Rama:** `release/1.0.0-final`
**Commit de código auditado:** `24d04b6`
**PR:** [#17](https://github.com/MaverickBms/CodeGuard-Pro/pull/17)

> Las pruebas de esta tabla se ejecutaron localmente sobre el commit indicado.
> La evidencia de CI se identifica por separado. No se atribuyen resultados de un
> commit a otro.

### Revisión funcional incremental (HEAD de esta rama)

Se añadieron doce pruebas de regresión desde el commit base de esta revisión:
dos de biblioteca PDF, una de curación de videos, dos de identidad local, tres
de bloqueo de acceso directo (lección, quiz y tutoría), dos de fallback de
respuestas vacías del tutor, una de formato del contexto de pistas y una de
unicidad de progreso por nivel. La ejecución
correspondiente se identifica por su run de CI en el PR #17; no se atribuye el
resultado del commit anterior a estas pruebas.

### Validación funcional incremental — 2026-11-23

CI del PR #17, run [45198026989](https://github.com/MaverickBms/CodeGuard-Pro/actions/runs/45198026989):

- Django: **368 pruebas OK** (75,889 s).
- `manage.py check`: correcto.
- `makemigrations --check --dry-run`: `No changes detected`.
- Rendimiento de arranque: correcto.
- Electron IPC: pruebas unitarias correctas.
- PyInstaller: construcción y smoke test correctos.
- El trabajo de Windows x64 permanece fuera del criterio de aceptación funcional de esta fase; no se usa para declarar terminada la validación del núcleo.

Esta ejecución incluye las doce pruebas de regresión añadidas en esta revisión.

## 1. Backend Django

| Prueba | Comando / procedimiento | Resultado | Evidencia |
|---|---|---|---|
| Comprobación del sistema | `python manage.py check --settings=config.settings.development` | 0 incidencias | Salida local |
| Migraciones al día | `python manage.py makemigrations --check --dry-run` | `No changes detected` | Salida local |
| Suite completa | `python manage.py test --settings=config.settings.development --parallel 1` | **356 pruebas OK** | `/tmp/cg-test-final2.log`, 131 s |
| Modelos y servicios | Incluida en la suite | OK | `apps/*/tests` |
| Vistas y permisos | Incluida en la suite | OK | `test_auth`, `test_modo_sin_auth`, `test_navigation_views` |
| Persistencia | Incluida y E2E manual | OK | Progreso, intento, PDF y tema tras reiniciar |
| Migraciones nuevas | `accounts.0003`, `roadmaps.0022` | Aplicadas | Perfil temporal |
| Backup/restore | CLI + prueba aislada | OK | ZIP verificado, restaurado, datos comprobados |

## 2. Electron / Node

| Prueba | Comando | Resultado | Evidencia |
|---|---|---|---|
| Unitarias Electron | `npm run test:electron` | **26/26 OK** | Salida local |
| Sintaxis JS | `node --check` sobre main, preload, IPC y scripts | OK | Salida local |
| Arranque dev | `electron .` con perfil temporal | OK | UI en ~11 s con primer arranque |
| Arranque AppImage | `APPIMAGE_EXTRACT_AND_RUN=1 ...AppImage` | OK | UI en ~10,2 s; 9 rutas 200 |
| Cierre | Cerrar ventana y comprobar procesos | OK | Sin `CodeGuardServer` ni Electron |
| Tema | `cdp-smoke set/expect fantasy` | OK | Persiste tras reiniciar |
| Responsive | `cdp-responsive.js` | OK | 13 pantallas a 1024×720 y 768×900, `BAD=[]` |
| Formulario PDF | `cdp-form-smoke.js` | OK | Importación real, visor, archivo |

## 3. Recorridos funcionales

| Recorrido | Procedimiento | Resultado |
|---|---|---|
| A. Primer arranque | Perfil vacío, migraciones, propietario, roadmap y siembra | OK |
| B. Aprendizaje | Lección 1, respuesta correcta, feedback, cierre y reapertura | OK: lección 100 %, intento 100 %, persiste |
| C. Evaluación | Suite de corrección y bloqueo por prerrequisitos | OK; sin quizzes publicados en perfil limpio |
| D. Tutor | Estado y pistas con Ollama simulado/ausente | OK; fallback determinista |
| E. Biblioteca | PDF válido, búsqueda, visor, archivo, reinicio | OK; estado archivado persiste |
| F. Editorial | Edición, versión, fuentes, revisión, publicación | OK en pruebas; formulario inválido no pierde datos |
| G. Backup | Crear, verificar, restaurar en perfil aislado | OK; progreso, intento y PDF recuperados |
| H. Gamificación | Monedas/logros/misiones idempotentes | OK; no altera notas |

### Evidencia del recorrido B

Salida del smoke de aprendizaje:

```json
{"before":true,"url":"/roadmaps/leccion/1/","ok":true,"done":true,"attempts":1}
```

Comprobación posterior al reinicio:

```json
{"completed":true,"attempt":true,"score":true}
```

### Evidencia del recorrido E/G

- PDF `Documento E2E ...` importado y archivado.
- Backup: 2 archivos, 1.511.679 bytes, SHA-256
  `e592c07ce392da8c635d2885341c8c7755485ebfc917ddc0980817746d6f2753`.
- Restauración en `/tmp/cg-restore-e2e`: progreso de lección 100 %, intento 100 %
  y documento archivado recuperados.

## 4. Roadmap y contenido

| Comprobación | Resultado |
|---|---|
| Etapas | 33 |
| Módulos | 212 |
| Títulos de lección | 1.946 |
| Prerrequisitos | 7 |
| Lecciones con cuerpo | 8 |
| Versiones borrador | 8 |
| Lecciones aprobadas | 0 |
| Lecciones publicadas | 0 |
| Lecciones pendientes | 1.938 |
| Ejemplos | 8 |
| Ejercicios | 16 |
| Fuentes únicas | 13 |
| Referencias de fuente | 16 |
| Videos con enlace verificado | 8 |
| Videos con revisión pedagógica aprobada | 0 |

Verificado con consultas SQLite sobre un perfil temporal y con la suite
`test_academic_content`, `test_roadmaps` y `test_bootstrap`.

### Revisión posterior — unicidad de PDF

Se añadieron cinco pruebas nuevas: dos para la restricción de SHA-256 y los
registros sin hash; una para excluir videos rechazados pedagógicamente; y dos
para impedir que sesiones heredadas sustituyan al propietario local. Están
incorporadas a apps.library, apps.roadmaps y apps.accounts, que ejecuta CI; el
resultado del HEAD actual debe confirmarse en el nuevo run y no se hereda del
run anterior.

## 5. Seguridad y dependencias

| Prueba | Resultado |
|---|---|
| `pip-audit -r requirements.txt` | Sin vulnerabilidades conocidas |
| `npm audit --omit=dev --audit-level=high` | 0 vulnerabilidades de producción |
| `npm audit` completo | 6 moderadas de build; 0 altas/críticas |
| `pip check` | Sin conflictos |
| Cabeceras CSP/CSRF/clickjacking | OK en suite |
| Upload PDF inválido/duplicado/grande | OK en suite |
| Rutas PDF y rangos | OK en suite |
| Permisos editoriales | OK: cuenta ordinaria no se eleva; perfil ambiguo falla cerrado |
| IPC Electron | OK en 26 pruebas |
| Enlaces externos | OK: HTTPS sin credenciales; rechaza esquemas peligrosos |
| Backups maliciosos | OK: rutas, symlinks, hashes, CRC y SQLite |

## 6. Rendimiento

Comando: `python scripts/benchmark-startup.py`

| Escenario | Resultado local |
|---|---|
| Primer arranque | 8,7 s interno / 9,6 s pared, 54 migraciones, roadmap cargado |
| Segundo arranque | 144 ms interno / 901 ms pared |
| Perfil con historial | 129 ms interno / 813 ms pared |
| Objetivos | ≤10 s normal y ≤30 s primer arranque: **cumplidos** |

## 7. CI remoto

| Run | Commit | Resultado | Nota |
|---|---|---|---|
| `44945721326` | `5747ec6` | 4/4 jobs verdes | Evidencia Windows anterior a esta auditoría |
| `44952905523` (push) | `29b836f` | **4/4 jobs verdes** | Django, PyInstaller, Electron y Windows |
| `44952910842` (PR #17) | `29b836f` | **OK** | Workflow corregido para PR contra `release/1.0.0` |

El commit `29b836f` solo añade documentación sobre `24d04b6`; el código validado
por CI es el mismo.

El workflow se corrigió para ejecutarse también en PR contra `release/1.0.0` y
ramas `release/**`, y en pushes a `release/1.0.0-final`.

## 8. Artefactos de esta auditoría

| Artefacto | Plataforma | Tamaño | SHA-256 | Commit de origen |
|---|---|---:|---|---|
| `CodeGuard-Pro-1.0.0-x86_64.AppImage` | Linux x64 | 129.372.879 B | `7ca64d4e46787aee17cd839d162c965ba549f4f280809a8ca7d4eac915c28202` | `24d04b6` |
| `CodeGuardServer` | Linux x64 | 7.798.232 B | `6080dc8ca8ed731ecdfe38c84e0906eadfce6dd2b6838036911577479ec3d4a5` | `24d04b6` |
| `codeguard-windows-x64.zip` (artefacto CI) | Windows x64 | 275.098.534 B | `da2fda5aa7878f51fb142a74d1076ea1416991ae3ddb0c23ee7bb78cbe02463a` | `29b836f` (código `24d04b6`) |
| `CodeGuard Pro Setup 1.0.0.exe` | Windows x64 | 146.505.176 B | `1c814266baa25028a579ed5f7296b9e91ca709867d86d360520679f94a78117b` | `29b836f` |
| `CodeGuard Pro 1.0.0.exe` (portable) | Windows x64 | 129.364.031 B | `52b1d3d8dd0548edd82bbf2feb67397c84619283a1a6aef837223b8a70497be9` | `29b836f` |

El AppImage se ejecutó con extracción porque el montaje FUSE de este host queda
bloqueado. El servidor PyInstaller pasó su smoke de primer arranque y
sincronización cerrada.

## 9. Limitaciones de la matriz

- No hay hardware Windows físico; el ciclo Windows se valida en CI.
- Los artefactos Windows/Linux no tienen firma de código de producción.
- No se probó macOS ni ARM64.
- No se hizo revisión pedagógica humana de los videos.
- No se probó concurrencia real de importación de PDF.
- La restauración se probó en un perfil aislado, no sobre el perfil real.


### Validación incremental — integridad de recompensas (2026-11-23)

Se incorporó una restricción única condicional sobre `TransaccionMoneda(usuario, tipo, referencia)` para referencias no vacías, además de una migración conservadora que aborta si detecta duplicados históricos y una prueba de inserción duplicada directa. Esta prueba se suma a la suite previa; el total y el resultado solo se actualizarán cuando CI del HEAD `59ff81a` termine. La validación anterior de 368 pruebas corresponde al commit anterior y no incluye esta prueba nueva.


### Validación incremental — restauraciones consecutivas (2026-11-23)

Se corrigió la colisión de nombres de las copias de reversión al restaurar dos veces dentro del mismo segundo. Cada operación reserva un directorio único y la prueba de regresión verifica que no se sobrescribe la copia anterior. Esta prueba aún no tiene resultado CI asociado.

## 10. Validación incremental autónoma (2026-11-23)

| Área | Prueba | Resultado | Evidencia |
|---|---|---|---|
| Sistema | `manage.py check --settings=config.settings.development` | OK | Ejecución local, 0 issues |
| Migraciones | `manage.py makemigrations --check --dry-run --settings=config.settings.development` | OK | No changes detected |
| Django suite | `manage.py test apps.core apps.accounts apps.audit apps.roadmaps apps.tutoring apps.gamification apps.challenges apps.library --settings=config.settings.development` | OK | **379 tests**, 173.956s |
| Electron | `npm run test:electron` | OK | 26/26 pass |
| Smoke HTTP | Rutas principales con servidor dev + datos sembrados | OK | 200 en /, roadmaps, etapas 0/1/25, lección, evaluaciones, evidencias, conocimiento, cobertura, editorial, fuentes, biblioteca, importar, gamificación/perfil, tutoría estado, healthz, backups, login; 405 en POST-only por GET |
| Regresión | Criterio manual no completa etapa sin evaluación aprobada | OK | `test_criterio_manual_no_completa_etapa_sin_evaluacion_aprobada` |
| Regresión | `codigo_contiene` con `permite_completar_leccion` completa lección | OK | `test_codigo_contiene_completa_leccion_si_permite_completar` |
| CI HEAD base | Runs 45205752117, 45205738457 para `66468a5` | OK | 4/4 jobs success en ambos runs (Django, Electron, PyInstaller, Windows x64) |

**Limitaciones de esta validación:** no se ejecutó navegador automatizado (sin Playwright/Selenium; CDP scripts orientados a Electron empaquetado). No se probó aceptación Windows física. No se ejecutó smoke E2E empaquetado en esta sesión. No se validó flujo de publicación de esquema 2 extremo a extremo con firma.

## Rendimiento de arranque (2026-11-23)

| Caso | Tipo | Resultado | Evidencia |
|---|---|---|---|
| `manage.py check` | automatizada | OK | salida local |
| `makemigrations --check --dry-run` | automatizada | OK | No changes detected |
| Django suite completa | automatizada | OK (379) | `manage.py test -v 0` |
| Electron tests | automatizada | OK (26) | `npm run test:electron` |
| Benchmark Django fuente | automatizada | OK | `scripts/benchmark-startup.py --json` |
| Benchmark servidor empaquetado fresh | automatizada | OK | 12,446 ms /healthz, 277 ms `/` |
| Benchmark servidor empaquetado warm | automatizada | OK | 1,279 ms /healthz, 347 ms `/` |
| Benchmark servidor empaquetado historial | automatizada | OK | 1,302 ms /healthz, 389 ms `/` |
| Rebuild PyInstaller server | build | OK | `npm run build:server` |
| Rebuild AppImage Linux | build | OK | `npm run build:linux` |
| AppImage UI utilizable en este entorno | manual/best-effort | NO CONCLUYENTE | no se obtuvo `startup-perf-electron.json` usable; limitación de entorno |


## Pantalla de carga dinámica (2026-11-23)

| Caso | Tipo | Resultado | Evidencia |
|---|---|---|---|
| Progreso por fases reales / no retroceso | unit (node) | OK | `startup-progress.test.js` |
| No 100% antes de interactiva | unit (node) | OK | `startup-progress.test.js` |
| Eventos fuera de orden/duplicados | unit (node) | OK | `startup-progress.test.js` |
| Error de arranque visible | unit (node) | OK | `startup-progress.test.js` |
| Frases sin repetición inmediata / intervalo | unit (node) | OK | `startup-progress.test.js` |
| Electron suite | automatizada | OK (31) | `npm run test:electron` |
| AppImage rebuild | build | OK | `npm run build:linux` |
| AppImage UI utilizable en este entorno | manual | NO CONCLUYENTE | limitación de entorno |
