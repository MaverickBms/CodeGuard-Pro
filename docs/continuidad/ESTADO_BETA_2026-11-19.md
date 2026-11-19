# Estado de avance de beta — CodeGuard Pro

**Fecha de revisión:** 2026-11-19  
**Rama de trabajo:** `fix/electron-ipc-origin-validation`  
**Base:** `main` en `59d08848726550fde442be1eb1e1be5522637f0b`  
**HEAD auditado antes de esta actualización:** `4e784bbf59cc6a9c461470cf2ae2eafd40a87621`  
**Commits correctivos/documentales:** `fcca40d`, `4c32fe8`, `98d354e`, `40cfdf2`, `6907ff6`, `1d025a9`, `a892b5e`, `6178df9`, `49f463c`, `2e64a0a`, `cf963b8`, `80f703a`, `7f3cedd`  
**Pull request:** https://github.com/MaverickBms/CodeGuard-Pro/pull/12 (abierto, borrador)  
**Alcance:** inspección estática remota y corrección puntual de launcher; no equivale a ejecutar el proyecto.

## 1. Trabajo incorporado en la rama

- Se centralizó la validación de origen para IPC en `electron/ipc-security.js`.
- La comprobación exige URL válida, protocolo HTTP, host loopback esperado, puerto dinámico exacto y ausencia de credenciales.
- Se aplicó la validación a todos los canales IPC expuestos por `electron/preload.js`: tema, notificaciones, estado/solicitud de sincronización, información del sistema y selector de carpetas.
- Las notificaciones limitan título (120 caracteres) y cuerpo (1000 caracteres), y utilizan el icono local de la aplicación.
- Se añadieron seis casos de regresión en `electron/ipc-security.test.js` y el comando `npm run test:electron`.
- Se añadió `.github/workflows/ci.yml` para checks Django, migraciones, suite Django y pruebas IPC. En la revisión del 19-11 se amplió el trigger `push` a todas las ramas y se añadieron verificaciones de sintaxis Python y JavaScript antes de ejecutar las suites.
- Los lanzadores Linux `codeguard` y `run.sh` se ajustaron posteriormente para detectar el AppImage x64 y delegar la inicialización del perfil en el servidor empaquetado; ya no ejecutan migraciones con un Python externo.
- Se actualizó este documento y la descripción del PR con los hallazgos y límites de verificación.

## 2. Evidencia y límites de verificación

### Pruebas IPC

El trabajo previo reporta una ejecución aislada de `npm run test:electron` con 6/6 pruebas correctas. Esta revisión no pudo repetirla en un checkout local, por lo que se conserva como **evidencia reportada, no reproducida independientemente en esta sesión**.

Las seis pruebas cubren origen exacto, puerto diferente, host que suplanta el prefijo loopback, protocolo no permitido, credenciales en URL y eventos/argumentos inválidos. Validan la función pura; no demuestran integración real con Electron.

### GitHub Actions

Se consultaron las ejecuciones del workflow. La consulta actual mostró quince ejecuciones terminadas en fallo:

| Run | Commit | Estado |
|---|---|---|
| 1 | `670d675aaaa26dbcfe2c9b1744c0ea869cb30d40` | `completed / failure` (run `44443084187`) |
| 2 | `5223e4373aee76837437ebf943f952aa691b2b0f` | `completed / failure` (run `44443103887`) |
| 3 | `fcca40def7c5f7703406fb78a3274579613f13a2` | `completed / failure` (run `44444331213`) |
| 4 | `4c32fe83b29c67af2565efa3a64419add26a8051` | `completed / failure` (run `44444347512`) |
| 5 | `98d354e4bdb4ea77a363d4e8e301a8f77a5c29f6` | `completed / failure` (run `44444371255`) |
| 6 | `40cfdf23639cf8bb6384c7297e19219af87507af` | `completed / failure` (run `44444429601`) |
| 7 | `6907ff66f0d7a03bf68bbd00ab6f7f039678dfe7` | `completed / failure` (run `44445039210`) |
| 8 | `1d025a90e47e32d4580eacf31136fece5cd50160` | `completed / failure` (run `44445369572`) |
| 9 | `a892b5e024f19a97cfbb2d25907fd427ab3796d1` | `completed / failure` (run `44445451593`) |
| 10 | `6178df902159c73b4d19995e6ab245534c7ea9ef` | `completed / failure` (run `44445508444`) |
| 11 | `49f463c6a98e8dc28e6b1314eafe675d25326b87` | `completed / failure` (run `44445540907`) |
| 12 | `2e64a0ae45aef90f16ecfb5373dc9db6120631ba` | `completed / failure` (run `44445764770`) |
| 13 | `cf963b8ac72163003c750793b8c1811eb060f4e6` | `completed / failure` (run `44445807473`) |
| 14 | `80f703a409897ef59eb2a2b72986a990c99e6e10` | `completed / failure` (run `44445836794`) |
| 15 | `7f3ceddd3835b92d622a84859518b89b2537ba41` | `completed / failure` (run `44445883166`) |

La inspección directa de Actions para los runs `44444429601`, `44445369572`, `44445451593`, `44445508444` y `44445540907` confirmó `conclusion=failure`, pero `total_count=0` y `jobs=[]`, incluso al consultar los intentos disponibles. Los check-runs/statuses consultados tampoco aportan validaciones. Los seis runs más recientes (`44445369572`, `44445451593`, `44445508444`, `44445540907`, `44445764770` y `44445807473`) devuelven `jobs=[]`; el run `44445836794` del último commit documental también devuelve `jobs=[]`. No hay jobs, steps ni logs de job que permitan identificar un error de ejecución. Los runs se marcan como eventos `push` sobre la rama de trabajo. El workflow en la rama actual incluye `push` sin filtro de ramas y `paths-ignore` para `docs/**` y `**.md`; sin embargo, tanto el cambio de dependencias (`2e64a0a`) como los cambios exclusivamente documentales (`cf963b8`) generaron ejecuciones. Por tanto, el filtro `paths-ignore` no parece estar evitando los runs como se esperaba. Esto deja dos problemas: ejecuciones fallidas sin jobs y comportamiento inconsistente de filtros/activación.

- **No se conoce la causa del fallo.**
- No se puede afirmar que hayan fallado las pruebas Django, las pruebas IPC, la instalación de dependencias o la sintaxis del workflow.
- Ninguna ejecución cuenta como validación aprobada.
- Se debe inspeccionar la vista de Actions y la configuración de Actions del repositorio para determinar por qué se crean ejecuciones fallidas sin jobs. La API disponible no expone logs de workflow/job para esos runs. No hay base para modificar las pruebas o dependencias hasta resolver esta anomalía.

Enlace: https://github.com/MaverickBms/CodeGuard-Pro/actions

### Primer arranque empaquetado

El código de `server_entry.py` contiene `_initialize_database()`, que llama a `migrate` y `cargar_ascenso` antes de iniciar Waitress en el modo servidor empaquetado. Esto parece resolver el problema descrito por QA-03 en el informe del 16-11-2026, pero necesita pruebas con directorio vacío y perfil preexistente.

El endpoint `config/health.py` comprueba DB, migraciones pendientes y existencia de un roadmap activo. Electron espera HTTP 200 y los cuatro estados `ok` antes de cargar la ventana.

### Corrección del launcher `codeguard`

El launcher ya no inicializa Django por separado con el entorno de desarrollo. `run.sh` exporta `CODEGUARD_DATA_DIR` y el AppImage hereda esa variable; `server_entry.py` ejecuta `migrate` y `cargar_ascenso` en el proceso empaquetado antes de iniciar Waitress. Así se evita exigir Python/Node externos y se mantiene un solo punto de inicialización.

**Estado de validación:** corrección inspeccionada estáticamente; aún no se ejecutó el AppImage en Linux con un perfil temporal. Debe probarse que el servidor empaquetado escribe en el directorio esperado y que la carga idempotente conserva progreso existente.

## 3. Hallazgos operativos abiertos

| Prioridad | Hallazgo | Estado / acción |
|---|---|---|
| P0 | Aceptación de instalación limpia y flujo principal Electron/Django. | Pendiente de ejecución real con perfil temporal. |
| P1 | Reproducibilidad de la suite Django completa (245 reportadas). | Pendiente de ejecutar sobre el HEAD exacto y registrar salida. |
| P1 | CI sin resultado verificable. | Catorce runs fallidos; los seis más recientes inspeccionados devuelven cero jobs. Los cambios de dependencias y documentación generan runs pese a `paths-ignore`. |
| P1 | Persistencia tras reinicio, modo offline E2E y cierre sin procesos huérfanos. | Pendiente. |
| P1 | Backup/restauración. | Diseño documentado; implementación/aceptación pendiente. |
| P1 | Tutor Ollama. | Opcional; validar detección, modelo instalado, timeout, fallback y privacidad. |
| P2 | Build Windows x64 y artefactos de distribución. | Objetivos NSIS y portable declarados; build/instalación reales aún pendientes. |
| P2 | Ciclo de vida en macOS. | `window-all-closed` detiene Django pero no cierra la app en macOS; `activate` crea una ventana sin reiniciar ni recargar el servidor. macOS no está configurado/validado y queda fuera de la beta actual. |
| P2 | Documentos históricos no totalmente sincronizados. | Revisar especialmente `docs/VALIDACION_INTEGRACION_ELECTRON.md`, estados de fases y cifras históricas. |

## 4. Estado funcional del producto

La visión y arquitectura deben mantenerse: plataforma educativa personal, monousuario, local y offline-first, con Electron, Django 5.2, Waitress, SQLite y frontend HTML/CSS/JavaScript local.

- Núcleo, dashboard, estructura ASCENSO y navegación: implementados; aceptación de escritorio actual pendiente.
- Contenido versionado, fuentes, flujo editorial, paquetes firmados y sincronización pull-only: bases técnicas implementadas; contenido pedagógico completo y distribución remota de producción pendientes.
- Tutoría local: parcial y dependiente opcionalmente de Ollama; fallback estático.
- Evaluaciones: modelos y servicios parciales; UI y progresión completa pendientes.
- Gamificación, mundo/avatar y desafíos: bases integradas, experiencia completa y reglas funcionales por validar.
- Autenticación: código conservado, `AUTH_DISABLED = True`; no reactivarla sin autorización expresa.
- Ejecución arbitraria de código: no habilitar sin sandbox independiente auditado.
- Backup/restauración: no aceptar como disponible.
- Hosting, endpoint, allowlist y claves de producción para sincronización: no configurados; no son requisito para estudiar offline.

No confundir modelos, rutas o controles visibles con un flujo de usuario terminado. La implementación debe probarse de extremo a extremo.

## 5. Restricciones de protección

- Mantener `main` intacta; el trabajo de esta iteración permanece en la rama del PR #12.
- No fusionar el PR ni crear releases/tags.
- No modificar bases de datos reales, perfiles, `.env`, claves, credenciales o datos personales.
- No ejecutar `cargar_ascenso --recrear` sobre datos existentes.
- No cambiar `AUTH_DISABLED` sin autorización expresa.
- No añadir hosting, claves privadas ni configuración de producción.
- No desactivar CSRF, CSP, validaciones ni pruebas para conseguir un CI verde.
- No declarar pruebas exitosas si no se ejecutaron realmente.

## 6. Última actualización de la rama

- Workflow CI actualizado para ejecutarse en `push` de cualquier rama.
- Se agregaron `python -m compileall -q config apps server_entry.py manage.py` y `node --check` para los archivos principales de Electron.
- Se retiró `PyMuPDF==2.1` de `requirements.txt`: no se encontraron importaciones del paquete en el código revisado, está etiquetado como fase futura, añade un motor PDF nativo de gran tamaño y su licencia es AGPL-3.0 o comercial. Reincorporar una biblioteca PDF cuando haya módulo activo y decisión de licencia. Fuente oficial: https://pypi.org/project/pymupdf/2.1/.
- El trigger `push` cubre todas las ramas y omite cambios exclusivamente documentales (`docs/**`, `**.md`) para evitar ejecuciones de CI innecesarias.
- Commit del ajuste del workflow: `1d025a90e47e32d4580eacf31136fece5cd50160`.
- Los runs `44445369572`, `44445451593`, `44445508444`, `44445540907`, `44445764770`, `44445807473` y `44445836794` terminaron en `failure` con `jobs=[]`. CI sigue sin ser interpretable y no se declara aprobado.
- Se eliminó la dependencia PyMuPDF aún no utilizada de `requirements.txt`.
- La rama está 22 commits por delante de `main`, sin commits por detrás al momento de la consulta. `main` continúa en `59d08848726550fde442be1eb1e1be5522637f0b`.

## 7. Limitación de esta sesión

Se intentó clonar la rama para ejecutar pruebas localmente, pero el entorno de esta sesión no pudo resolver `github.com` por DNS. La inspección se realizó mediante la API de GitHub y lectura de archivos remotos. No se ejecutaron Python, Django, Node, Electron, PyInstaller, instaladores ni pruebas GUI en esta sesión.

Esto no significa que el proyecto no pueda ejecutarse en el equipo del propietario; significa que esta sesión no dispone de un checkout ejecutable ni de una ruta de red para obtenerlo.

## 8. Próximo bloque recomendado

1. Diagnosticar en GitHub por qué las quince ejecuciones de Actions terminaron en failure sin jobs visibles y por qué `paths-ignore` no evita las ejecuciones documentales.
2. Generar y ejecutar el AppImage Linux en un perfil temporal; confirmar que el servidor empaquetado ejecuta migraciones/carga ASCENSO dentro del `CODEGUARD_DATA_DIR` exportado por `run.sh`.
3. Probar `server_entry.py` en un directorio vacío y otro con datos de prueba existentes, verificando idempotencia y preservación.
4. Ejecutar en el entorno del proyecto: `pip check`, `manage.py check`, `makemigrations --check --dry-run`, las siete apps de pruebas Django, `node --check` y `npm run test:electron`.
5. Ejecutar la aceptación GUI/offline/persistencia/cierre en Linux y la instalación limpia Windows si esa es la plataforma de presentación.
6. Actualizar los documentos históricos para que reflejen el código actual y distingan evidencia reportada, ejecutada y aceptada.

**Nota de corte:** este informe registra los runs visibles hasta el commit `7f3cedd`; el propio commit de esta actualización documental puede generar otra ejecución push.\n\n**Criterio de salida:** CodeGuard Pro no debe declararse beta aceptada hasta que el primer arranque, el flujo académico esencial, la persistencia, el funcionamiento offline, la integración Electron y el cierre limpio tengan evidencia reproducible. La presentación puede describirse como beta de evaluación con limitaciones explícitas si todavía quedan criterios de distribución sin aceptar.

## 9. Corrección posterior al corte: lanzadores Linux

La revisión posterior detectó una discrepancia entre el artefacto configurado y los nombres que buscaban los lanzadores:

- `package.json` configura electron-builder con arquitectura Linux `x64` y patrón `CodeGuard-Pro-${version}-${arch}.AppImage`.
- Los scripts anteriores `run.sh` y `codeguard` buscaban el sufijo `x86_64.AppImage`, por lo que podían rechazar el AppImage generado por el build configurado.
- `run.sh` también exigía Python y Node.js e intentaba instalar dependencias Python/Node aunque el servidor Django está empaquetado dentro del AppImage. El servidor empaquetado ya ejecuta migraciones y carga idempotente de ASCENSO en el perfil local.

**Corrección publicada en la rama del PR #12:**

- `run.sh` ahora localiza exactamente un artefacto `dist/CodeGuard-Pro-*-x64.AppImage`, configura `CODEGUARD_DATA_DIR` respetando `XDG_CONFIG_HOME` y ejecuta el AppImage sin instalar ni requerir Python/Node en el equipo usuario.
- `codeguard` delega en `run.sh` para evitar mantener dos implementaciones distintas del arranque.
- Ambos lanzadores pasan argumentos adicionales al AppImage y usan `exec` para conservar correctamente el proceso y sus señales.

**Límite de validación:** comprobación estática contra `package.json` y `server_entry.py`; no se generó ni ejecutó un AppImage en esta sesión. La aceptación del nombre final del artefacto y del arranque real sigue pendiente de build Linux y prueba en equipo limpio.


## 10. Actualización posterior: empaquetado Windows x64 (19-11-2026)

La revisión del empaquetado detectó que `README_WINDOWS.md` y `build_windows.bat` anunciaban instalador NSIS y ejecutable portable, pero `package.json` no declaraba objetivos Windows. Se corrigió en la rama del PR #12:

- `package.json` declara explícitamente los objetivos `nsis` y `portable`, ambos para arquitectura `x64`, y utiliza el icono Windows `static/icons/icon.ico`.
- Se evita forzar un `artifactName` compartido que podría producir colisión entre dos ejecutables .exe; electron-builder conserva sus nombres por objetivo.
- `build_windows.bat` usa `npm ci` para instalar exactamente lo fijado en `package-lock.json`, en lugar de saltarse la instalación cuando existe un `node_modules` potencialmente desactualizado.
- El script comprueba que el Python seleccionado sea 3.12 o superior y Node.js sea 20 o superior antes de continuar con la compilación.
- `README_WINDOWS.md` distingue la configuración de objetivos de la aceptación real: el build, instalación limpia, primer arranque y persistencia siguen pendientes.

**Evidencia:** inspección estática de `package.json`, `build_windows.bat`, `scripts/build-server.js`, `scripts/verify-server-build.js`, `CodeGuardServer.spec`, `server_entry.py` y `config/settings/desktop.py`. No se ejecutó Windows, PyInstaller ni electron-builder; no se generaron artefactos.

**Estado Git verificado tras estos cambios:** PR #12 sigue abierto y en borrador, sin fusionar. La rama está 33 commits por delante y 0 por detrás de `main`; la base de `main` sigue en `59d08848726550fde442be1eb1e1be5522637f0b`. El árbol Git confirma que `run.sh` conserva modo ejecutable `100755` y `codeguard` también `100755`.

**CI:** para el HEAD `5aeb614016386eca64f2495d9c2c07d796002088`, las consultas de runs de PR y estados combinados no devolvieron ejecuciones ni checks. Esto no equivale a aprobación; el problema histórico de Actions sin jobs sigue sin diagnóstico.

**Siguiente paso de empaquetado:** ejecutar `build_windows.bat` en Windows x64 limpio y verificar que aparezcan ambos artefactos; instalar el NSIS y ejecutar el portable, ambos sin Python/Node, con perfil de datos nuevo y con perfil ya existente. No distribuir hasta completar esa matriz.


**Ajuste final de requisitos Windows:** `build_windows.bat` también comprueba Node.js 20+; `README_WINDOWS.md` actualiza la fecha de revisión al 19-11-2026. Estas validaciones siguen siendo estáticas hasta ejecutar el script en Windows.


## 11. Verificación adicional de GitHub Actions

Se consultó directamente la colección de ejecuciones del repositorio, además del wrapper de runs de PR. Para el HEAD `252168148609e7ff8f041df41741e1a036abd9a4`, GitHub registra el run `44446813398` como `completed / failure`, evento `push`, pero la consulta directa de `/actions/runs/44446813398/jobs` devuelve `total_count=0` y `jobs=[]`. El run fue creado y actualizado en el mismo segundo, sin inicio visible de jobs. Se repitió la consulta para `44446640625` y `44445950472`, con el mismo resultado. No hay evidencia que permita atribuir el fallo a código, instalación de dependencias o tests; no cambiar tests ni desactivar protecciones para ocultar esta anomalía.

La última actualización documental generó el run `44446871347` para el commit `4e784bbf59cc6a9c461470cf2ae2eafd40a87621`; volvió a terminar en `failure` con `jobs=[]` y `total_count=0`. La causa sigue sin estar expuesta por la API consultada.


## 12. Reconciliación con hallazgos QA históricos (19-11-2026)

Se contrastaron los hallazgos QA-04, QA-12 y QA-13 del informe histórico en la rama `documentation` contra el código actual de esta rama:

- **QA-04 — health check:** el código actual incluye `/healthz/` en `config/health.py`, que devuelve 200 solo cuando la base responde, no hay migraciones pendientes y existe un roadmap activo. Electron exige HTTP 200 y los cuatro estados `ok` antes de cargar la interfaz. Hallazgo corregido en código; aceptación empaquetada sigue pendiente.
- **QA-12 — concurrencia del límite de pistas:** `apps/tutoring/services.py` reserva el contador mediante `QuerySet.update(pistas_utilizadas=F(...)+1)` condicionado a `pistas_utilizadas__lt=3`, dentro de transacción; `PistaTutoria` tiene restricción única por sesión/número. El límite no depende de un contador leído previamente. La prueba de concurrencia real no se ha ejecutado en esta sesión.
- **QA-13 — privacidad de Ollama:** `_url_ollama_local()` limita el destino a HTTP con hostname `localhost`, `127.0.0.1` o `::1`, sin credenciales, rutas adicionales, query ni fragmento. `_NoRedirectHandler` impide seguir redirecciones. `apps/tutoring/tests/test_tutoria.py` incluye pruebas para hosts remotos, rutas/credenciales y redirecciones. El código de protección y las pruebas están presentes; no se han ejecutado localmente en este entorno.

Estos tres hallazgos no deben seguir describiéndose como defectos abiertos de código; su aceptación runtime/automatizada sigue condicionada a ejecutar las pruebas. El QA-14 (modo sin autenticación) continúa siendo una decisión consciente de producto para equipo personal monousuario y no se modifica sin autorización.

**Pendientes de beta priorizados tras esta reconciliación:** reproducir la suite, instalar/probar AppImage y paquetes Windows en equipos limpios, validar GUI + offline + persistencia + cierre, e implementar/aceptar backup y restauración. El tutor IA local permanece opcional y no debe bloquear el núcleo educativo.



## 13. Corrección de consistencia del registro de auditoría (19-11-2026)

La vista del panel principal ya registraba el evento `acceso_panel`, pero el valor no figuraba en `AuditLog.EVENTO_CHOICES`. Esto podía hacer que el evento se guardara con una etiqueta de presentación vacía/no reconocida en la auditoría.

Cambios incorporados en la rama:
- Se añadió `acceso_panel` a las opciones del modelo `AuditLog`.
- Se creó la migración `0003_add_acceso_panel_event.py` para mantener sincronizado el estado de migraciones y las opciones persistidas en el estado del proyecto.
- Se reforzó `AuditoriaSinAutenticacionTests` para comprobar también la etiqueta de presentación del evento.

**Estado de validación:** corrección de código y migración revisadas estáticamente. No se ejecutó `manage.py test`, `makemigrations --check` ni la migración sobre SQLite en esta sesión. No se afirma que el test esté pasando.

## 14. Corte de Git y CI tras la corrección de auditoría

- HEAD de la rama en este corte: `2043ef3a8b4f02832bab75f93d7e0edb9b2ac964`.
- PR #12: abierto, borrador, sin fusionar.
- Comparación contra `main`: 43 commits por delante, 0 por detrás; merge-base/base SHA `59d08848726550fde442be1eb1e1be5522637f0b`.
- La consulta de workflow runs para el nuevo HEAD no devolvió ejecuciones asociadas y el estado combinado no contiene checks. El run previo `44447430636`, correspondiente al HEAD anterior `9290216`, acabó en `failure` con `jobs=[]` y timestamps de creación/inicio/actualización en el mismo segundo. Esto no permite determinar si Actions está deshabilitado, si el workflow fue rechazado antes de crear jobs o cuál es la causa concreta. No atribuirlo a las pruebas.
- Se intentó clonar el repositorio para reproducir tests, pero el entorno no pudo resolver `github.com` por DNS. Tampoco hay un proyecto Vercel asociado al repositorio en la cuenta consultada para provisionar un sandbox de ejecución sin crear recursos nuevos. Por tanto, no se ejecutaron suites ni builds.

**Criterio pendiente:** reproducir en un checkout ejecutable los tests de auditoría, el conjunto Django, las pruebas IPC y las comprobaciones de migraciones; después realizar aceptación GUI, offline, persistencia, instalación limpia y cierre limpio. El diseño de backup/restauración continúa pendiente de implementación: no se ha añadido un módulo incompleto ni se presenta como funcional.

## 15. Corte posterior: verificación del HEAD publicado y diagnóstico de Actions

Consulta realizada después de incorporar la corrección de auditoría:

- HEAD publicado: `b82c17ced02a1117e41af9384781ee50fbe45cb8`.
- PR #12 continúa abierto, en borrador y sin fusionar.
- Comparación remota: 44 commits por delante de `main`, 0 por detrás. La base de `main` permanece en `59d08848726550fde442be1eb1e1be5522637f0b`.
- La rama contiene la migración `apps/audit/migrations/0003_add_acceso_panel_event.py`, el cambio de `AuditLog.EVENTO_CHOICES` y la aserción de presentación del evento.
- La ejecución más reciente visible al momento de esta consulta es el run `44448214712`, asociado al HEAD anterior al nuevo corte documental/código. GitHub lo registra como `completed / failure`, pero su endpoint de jobs devuelve `total_count=0` y `jobs=[]`. No hay steps ni logs con los que atribuir la conclusión a un fallo de sintaxis, dependencias o pruebas.
- La definición del workflow aparece registrada por GitHub como `.github/workflows/ci.yml` (workflow id `423323839`), por lo que el evento sí generó un registro de ejecución. Eso no explica por qué no se crearon jobs; la configuración de Actions del repositorio o la evaluación previa a los jobs sigue siendo una incógnita y no puede corregirse desde esta sesión con las herramientas disponibles.

**Validación:** se verificó el contenido publicado y los metadatos remotos. No se ejecutaron pruebas Django/Electron ni builds en un runner. No declarar CI aprobado ni beta aceptada. El siguiente paso técnico sigue siendo obtener un entorno reproducible con Python/Node y acceso al checkout, o resolver desde la configuración de GitHub del propietario por qué Actions finaliza sin jobs.

## 16. Verificación adicional de GitHub Actions (run 38)

Se consultó el objeto completo del run `44448412917` y los endpoints de check-runs/status para el commit `f50663c09b800dc7c0f7292fcc3c182fd6f49ead`:

- Evento: `push`; workflow registrado: `.github/workflows/ci.yml`; workflow id `423323839`.
- Resultado: `completed / failure`, con hora de inicio y finalización idénticas (`2026-11-19T03:01:00Z`).
- Endpoint de jobs: `total_count=0`, `jobs=[]`.
- Endpoint de check-runs del commit: `total_count=0`, `check_runs=[]`.
- Commit status: `pending`, `total_count=0`, sin estados individuales.

Esto confirma que no existe evidencia de que los jobs Django o Electron hayan comenzado. No permite concluir si la causa es configuración/política de Actions, evaluación del workflow u otro fallo previo a la creación de jobs. No cambiar el workflow ni sus protecciones sin identificar primero la causa. Las pruebas y los builds siguen sin ejecutarse desde un entorno reproducible.

## 17. Especificación de backup/restauración publicada

Se añadió `docs/BACKUPS_Y_RESTAURACION.md` como contrato técnico para la futura función. La revisión de `config/settings/base.py` confirma que el perfil incluye `db.sqlite3`, `media/`, `.secret_key` y `logs/`; SQLite usa WAL.

La especificación exige snapshot SQLite mediante API de backup (no copiar la base activa), validación de integridad y hashes, rechazo de ZIP path traversal/symlinks/ZIP bombs, restauración desde staging, rollback ante fallo y tratamiento cifrado de la clave local si se decide incluirla. También define pruebas de concurrencia, corrupción, interrupción, compatibilidad y recuperación.

**Importante:** se publicó únicamente la especificación; no existe todavía código ejecutable de backup/restauración ni UI para ello. No anunciar esta función como disponible. No se ejecutaron pruebas ni builds en este corte.

## 18. Revisión de seguridad IPC y diagnóstico CI (19-11-2026)

Se revisaron de nuevo `electron/ipc-security.js`, sus seis pruebas, los handlers IPC de `electron/main.js`, el preload y el endpoint `/healthz/`.

- La validación IPC compara protocolo HTTP, hostname y puerto exactos, rechaza credenciales y falla de forma cerrada ante eventos/puertos inválidos. Los handlers privilegiados revisados aplican esa validación.
- Electron mantiene `contextIsolation`, `nodeIntegration: false`, sandbox y bloqueo de ventanas nuevas. La revisión fue estática; no sustituye pruebas con Electron real.
- El health check comprueba conexión SQLite, ausencia de migraciones pendientes y existencia de un roadmap activo antes de que Electron muestre la aplicación.

### CI: evidencia más reciente

El run `44448810877` corresponde al push del commit `1e556b1`, workflow `.github/workflows/ci.yml`, evento `push`. GitHub devuelve `completed/failure`, pero la consulta de jobs devuelve `total_count=0`, `jobs=[]`; la consulta de check-runs del commit también devuelve cero. No hay logs de job que permitan identificar una excepción o un paso fallido.

El commit que disparó el run modifica documentación únicamente, aunque el workflow declara `paths-ignore` para `docs/**` y Markdown. Esto es una anomalía adicional que debe investigarse desde la configuración/ejecución de Actions; con la evidencia disponible no se puede atribuir a una prueba, a un error de YAML ni a permisos concretos. El conector disponible permite leer runs/jobs, pero no inspeccionar la configuración administrativa de Actions ni despachar un nuevo workflow manualmente.

**Acción pendiente externa al código:** verificar en GitHub, en Settings → Actions → General, que Actions está habilitado para el repositorio y que las políticas permiten los workflows y acciones usados; después ejecutar manualmente `CodeGuard Pro CI` con `workflow_dispatch`. Si sigue fallando antes de crear jobs, obtener el detalle de diagnóstico desde la interfaz de Actions o soporte de GitHub.

**Validación:** revisión estática únicamente. No se ejecutaron suites Django/Electron, compilación PyInstaller, electron-builder ni instaladores. No se declara CI aprobado ni beta aceptada.


## 19. Servicio interno de backup inicial (19-11-2026)

Se incorporó `apps/core/backup.py` con creación y verificación de archivos ZIP de backup:
- Snapshot consistente de SQLite mediante `Connection.backup()`, con `PRAGMA integrity_check`.
- Inclusión de `media/`, manifiesto versionado, tamaños y SHA-256; validación CRC y de hashes al reabrir el archivo.
- Rechazo de destinos dentro del perfil, destinos ya existentes, rutas ZIP absolutas/traversal, entradas duplicadas, symlinks y límites de tamaño.
- Exclusión deliberada de `.secret_key`, logs y archivos WAL/SHM independientes.
- Pruebas añadidas para creación, exclusión de secretos/logs, destino dentro del perfil, no sobrescritura, traversal y ZIP truncado.

**Límite importante:** esto solo implementa el servicio de creación/verificación. No hay restauración, interfaz, cifrado de secretos, ejecución de pruebas ni validación en Windows/Linux. No usarlo aún como una función de usuario final ni marcar backup/restore como terminado. La restauración debe ejecutarse con Django/Electron detenidos y con rollback probado.

**Validación de este commit:** cambios publicados en la rama del PR; el entorno de trabajo no tiene checkout local funcional, así que no se ejecutaron las pruebas Django ni el análisis estático con intérprete. CI sigue pendiente de diagnóstico.


## 20. Comandos de backup internos (19-11-2026)

Se añadieron dos comandos Django:
- `python manage.py crear_backup --output RUTA.zip`: crea un ZIP verificado desde `settings.DATA_DIR`.
- `python manage.py verificar_backup RUTA.zip`: comprueba formato, CRC, manifiesto, hashes SHA-256 e integridad SQLite sin extraer al perfil.

Se añadieron pruebas de integración de los comandos en `apps/core/tests/test_backup_commands.py` y se documentó su uso. Son herramientas internas de mantenimiento; todavía no están conectadas a una pantalla de la aplicación.

**Pendiente:** restauración offline con rollback, interfaz, ejecución real de pruebas, CI con jobs/logs, builds Windows/Linux y validación de instalación limpia. No se debe anunciar backup/restore como función completa.


## 21. Endurecimiento del formato de backup y corte de beta (19-11-2026)

Se endureció el validador de apps/core/backup.py:
- El ZIP solo admite database.sqlite3 y archivos dentro de media/; rechaza payloads adicionales (por ejemplo, logs o rutas arbitrarias), incluso si están declarados en el manifiesto.
- La detección de symlink en media/ ocurre antes de comprobar su existencia, por lo que también rechaza enlaces simbólicos rotos.
- La carpeta raíz del perfil se comprueba antes de resolver la ruta para no aceptar una raíz configurada como symlink.
- Se añadieron pruebas para payload inesperado y directorio media simbólico.

**Estado de ejecución:** cambios publicados en esta rama, pero no ejecutados en un intérprete Python ni en CI. Las pruebas nuevas son cobertura añadida, no evidencia de que pasen.

### Alcance beta y elementos que se omiten temporalmente

Para evitar bloquear el cierre por trabajo no esencial:
- **Omitido de la beta inicial:** sincronización remota de producción (no hay endpoint, allowlist ni claves públicas productivas); macOS y ARM64; tutor IA local como dependencia del flujo principal; restauración automática/UI de backups. Se mantienen documentados y no se anuncian como disponibles.
- **No omitible antes de distribución:** reproducir suite Django y pruebas Electron; compilar al menos un artefacto por plataforma objetivo; instalación limpia y primer arranque; flujo principal de panel/roadmap/lección/evaluación; funcionamiento offline; persistencia tras reinicio; cierre sin procesos/puertos huérfanos.
- **Bloqueo externo:** GitHub Actions sigue generando runs failure sin jobs ni check-runs. No se atribuye a los tests o al código sin logs. La corrección de Settings → Actions y el workflow_dispatch requieren intervención en la interfaz del propietario del repositorio.
- **Backup actual:** creación/verificación interna disponible mediante comandos Django, pero sin restauración y sin UI. No equivale a una solución completa de recuperación de datos.

### Estado Git de este corte

Rama de trabajo: fix/electron-ipc-origin-validation. HEAD verificado en este corte: 607c27af1dce48829ea43b7b16f6939a57db2ca8. PR #12 sigue abierto y en borrador; comparación con main: 78 commits por delante y 0 por detrás. No se fusiona ni se modifica main.


## 22. Diagnóstico temprano del servidor Electron (19-11-2026)

`electron/main.js` ahora entrega el proceso hijo a `waitForServer`. Durante el sondeo de `/healthz/`, el arranque se interrumpe inmediatamente si el proceso emite un error de spawn o termina antes de estar listo; ya no espera innecesariamente el timeout completo de 120 segundos en ese escenario. El error incluye código de salida o señal y orienta a revisar los logs.

**Validación pendiente:** el cambio está publicado, pero no se ejecutaron `node --check`, pruebas Electron ni una aplicación empaquetada en este entorno. La consulta de ejecuciones para este commit no devolvió runs; no se interpreta como CI aprobado.


## 23. Pruebas unitarias de arranque Electron (19-11-2026)

Se aisló `getChildStartupFailure` en `electron/process-health.js` y se añadieron pruebas Node para proceso activo, error de spawn, salida con código, salida por señal y proceso ausente. `electron/main.js` utiliza ahora este helper durante la espera de `/healthz/`.

Las pruebas están añadidas a `npm run test:electron` por el patrón `electron/*.test.js`. No se afirma que estén aprobadas: falta ejecutar Node y obtener un resultado CI válido.


## 24. Auditoría ampliada de frontend y roadmap (18-11-2026)

### Hallazgos estructurales del contenido

Se inspeccionó apps/roadmaps/data/ascenso_3_1.json mediante parseo y validaciones estructurales:
- 33 etapas consecutivas (0–32), 212 módulos y 1.946 títulos de lección.
- Distribución de prioridades: 24 P1, 6 P2 y 3 P3.
- Siete relaciones de prerrequisito; todas apuntan a etapas existentes.
- No se detectaron números de módulo duplicados dentro de una misma etapa, títulos de lección vacíos ni espacios periféricos en los títulos.
- **Defecto editorial confirmado:** la etapa 25 (Seguridad de aplicaciones web y APIs) no tiene objetivo.
- **Defecto de estructura/contenido confirmado:** el campo proyecto de la etapa 10 contiene aproximadamente 4.739 caracteres de material curricular y secuencias de tecnologías, no una descripción breve de proyecto. No se reescribe ni recorta sin cotejar la fuente oficial.
- La metadata declara como fuente PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx y guarda un SHA-256, pero ese DOCX no está versionado en el repositorio ni apareció en la búsqueda de archivos disponibles. Por tanto, esta auditoría comprueba estructura y consistencia interna, no fidelidad semántica contra el documento maestro.

### Cobertura académica real en la beta

- El JSON contiene la estructura curricular (etapas, módulos, títulos de lección, objetivos/proyectos por etapa y algunas dependencias), pero no incorpora teoría, explicación sencilla, ejemplos, ejercicios ni rúbricas por lección.
- cargar_ascenso crea los registros estructurales; no genera material didáctico completo ni publica evaluaciones.
- quizzes_ejemplo.json se identifica explícitamente como borrador de estructura, con dos preguntas de ejemplo que deben reemplazarse y fuente académica pendiente. No representa una evaluación lista para estudiantes.
- La plantilla de lección contempla estados vacíos de forma explícita (Contenido en preparación, ejemplos/ejercicios pendientes). En consecuencia, la navegación por las 1.946 lecciones no significa que existan 1.946 lecciones desarrolladas.
- La finalización académica depende de ejercicios/evaluaciones y criterios verificables. Sin contenido y evaluadores publicados para cada unidad, no debe prometerse que el recorrido completo pueda cursarse de principio a fin.

### Navegación y opciones del frontend

- Los filtros de bloque, prioridad y búsqueda de etapa/módulo/lección están conectados a la vista del roadmap.
- Los módulos Competencias, Biblioteca, Base de conocimiento, Evaluaciones, Evidencias, Laboratorios, Backups, Vigencia y Ética aparecen deshabilitados en la navegación porque sus vistas integradas no están implementadas. Se mantienen así deliberadamente: habilitarlos ahora llevaría a destinos inexistentes o a controles sin acción.
- Las herramientas de backup actuales son comandos de gestión; todavía no existe una pantalla integrada de backup/restauración.
- Los temas y ajustes visuales tienen controladores frontend; su funcionamiento visual final requiere prueba manual en la aplicación empaquetada y distintos tamaños de ventana.
- En tutoría frontend se detectó que el análisis automático posterior al envío registraba un listener de DOMContentLoaded desde otro listener de ese mismo evento, por lo que podía no ejecutarse. Se cambió a invocación directa después de inicializar la vista. También se añadieron manejadores de fallo de red para que pedir una pista no deje el botón bloqueado y para informar cuando no se pueda recuperar el análisis.

### Corrección de progresión aplicada

La inspección encontró que el estado Bloqueada se calculaba y mostraba, pero los servicios de envío de ejercicios y evaluaciones no comprobaban los prerrequisitos antes de aceptar una entrega. Se corrigió en esta rama:
- registrar_intento_ejercicio rechaza entregas de etapas con prerrequisitos pendientes.
- evaluar_quiz rechaza envíos de quizzes de etapas bloqueadas antes de crear resultados.
- registrar_cumplimiento_criterio rechaza evidencia anticipada en etapas bloqueadas y no acepta evidencia vacía; la plantilla oculta ese formulario antes de cumplir prerrequisitos y exige texto de evidencia.
- La pantalla de detalle aclara que se puede consultar el contenido bloqueado, pero no enviar entregas/evaluaciones ni registrar criterios hasta cumplir los prerrequisitos.
- Se añadieron pruebas de regresión para ejercicios, quizzes, criterios bloqueados y rechazo de criterios sin evidencia.

**Validación pendiente:** las pruebas nuevas y las suites Django/Electron no se han ejecutado en un checkout de esta sesión; CI sigue sin ofrecer jobs/logs verificables. No se declara aprobada esta corrección hasta ejecutar las pruebas.

### Dictamen provisional de frontend/roadmap

La estructura de navegación y consulta del roadmap está implementada, pero el contenido académico no está completo para una beta educativa integral. Antes de aceptar el roadmap como correcto:
1. Recuperar y cotejar el DOCX maestro exacto para corregir la etapa 25 y normalizar el campo proyecto de la etapa 10 sin inventar contenido.
2. Definir explícitamente qué etapas y lecciones forman el alcance cursable de la beta.
3. Publicar material revisado, ejemplos, ejercicios, evaluadores y evaluaciones reales para ese alcance.
4. Ejecutar pruebas de navegación, filtros, entregas, evaluaciones, progresión, persistencia y presentación en Windows/Linux.
5. Mantener deshabilitados los módulos que todavía no tienen una implementación real.


## 25. Revisión adicional de dashboard y evidencias (18-11-2026)

### Dashboard: actividad reciente aislada por roadmap
Se detectó que el panel consultaba los cinco registros más recientes del usuario sin filtrar por roadmap. Al cambiar de ruta, podía mezclar actividad de una ruta anterior con las métricas del roadmap activo. Ahora la consulta se limita al roadmap activo y devuelve una lista vacía si no existe uno. Se añadieron dos pruebas para ambos escenarios.

### Criterios de finalización: transparencia y validación de entradas
La revisión confirmó que los criterios de proyecto/manual son autodeclaraciones locales, no una revisión docente independiente. Se aclaró esto en la interfaz y se cambió el estado visual a «Evidencia registrada» para no presentar la declaración como verificación externa. El formulario ahora habla de registrar evidencia y no de conceder aprobación por sí solo.
- El backend exige evidencia no vacía y limita su longitud a 5.000 caracteres.
- El origen debe pertenecer a los valores permitidos por el modelo.
- La referencia se limita a 120 caracteres.
- Se añadieron pruebas para evidencia demasiado larga y origen inválido.

**Validación pendiente:** los tests del dashboard y de criterios están versionados, pero no se han ejecutado. No se declara correcto el comportamiento runtime hasta tener salida reproducible de la suite.

### Estado del frontend
El panel, roadmap, gamificación y ajustes visuales tienen rutas y acciones identificables. Las secciones que aún no tienen vistas reales continúan deshabilitadas intencionalmente. Las doce opciones de tema están presentes en el diálogo de ajustes; las pruebas de plantilla comprueban su presencia, pero falta validación visual en ejecución para cada tema, contraste, responsive y persistencia real entre reinicios.

### Bloqueos de contenido y alcance
Sigue sin existir cotejo semántico con el DOCX maestro ASCENSO 3.1. Se mantienen los defectos editoriales detectados en la etapa 25 (objetivo vacío) y etapa 10 (campo proyecto con contenido anormalmente extenso). La plataforma sigue mostrando la estructura curricular completa, no 1.946 lecciones desarrolladas. Los contenidos, ejercicios y quizzes deben completarse para el conjunto de etapas que se defina como alcance cursable de la beta.


### CI: resultado observado tras la última publicación
La consulta directa de GitHub Actions para el HEAD e13a3897fc8c0e1203e53819b686635c32e587f4 encontró el run 44452070470 (evento push), concluido como failure con total_count=0 y jobs=[]. No se ejecutó ningún job; por tanto no es un fallo demostrado de las pruebas ni una aprobación. La consulta resumida de runs por commit no incluye este evento push, por lo que para auditoría se debe consultar la lista de Actions runs directamente. La causa del run sin jobs sigue sin estar expuesta en la respuesta disponible.

- Se confirmó que los commits de código 7889e4d, 754d19b y 395c687 generan runs push 44451957786, 44452032907 y 44452044606 respectivamente; los tres terminan en failure con cero jobs. No hay logs ni jobs para determinar la causa. El run 44452070470 del commit documental posterior también fue failure sin jobs. No debe interpretarse como que los tests de código hayan fallado: no llegaron a ejecutarse.


## 26. Cierre de brechas P0/P1 y verificación empaquetada (19-11-2026)

Esta sección registra trabajo ejecutado en un checkout local, no solo inspección
estática. Rama de trabajo: `release/1.0.0`, creada desde `main` (`f762166`).

### Suite de pruebas

- Se corrigieron cinco pruebas defectuosas sin debilitar validaciones:
  fixture de etapa bloqueada en criterios, `assertRaises` en examen bloqueado y
  argumento posicional de `verificar_backup`.
- Se añadieron pruebas de restauración, índices de evaluaciones/evidencias,
  pantalla de backups, cabeceras CSP y contraste WCAG de los 12 temas.
- **Resultado ejecutado:** 291 pruebas Django OK; 15 pruebas Node/Electron OK.
- `manage.py check`: 0 incidencias. `makemigrations --check --dry-run`: sin cambios.

### Recuperación de datos

- `apps/core/restore.py` implementa restauración con staging, validación de
  esquema, copia de reversión y rollback.
- Comando `restaurar_backup RUTA.zip --confirm` y pantalla `/backups/`.
- Modo `--restore-backup` del servidor empaquetado y menú de Electron
  **Restaurar copia de seguridad…** con parada de Django y reinicio.
- Verificación manual: backup real → restauración en perfil vacío → arranque
  del servidor PyInstaller → `/healthz/` con `database`, `migrations` y
  `roadmap` en `ok`.

### Frontend y accesibilidad

- Nuevas vistas `/roadmaps/evaluaciones/`, `/roadmaps/evidencias/` y `/backups/`.
- Navegación y tarjetas del panel actualizadas; los módulos sin implementación
  (competencias, biblioteca, base de conocimiento, laboratorios, vigencia,
  ética y desafíos) siguen deshabilitados y rotulados como no disponibles.
- CSP endurecida con `object-src`/`frame-src` cerrados y `form-action 'self'`.
- Bordes derivados de ocho temas corregidos para alcanzar 3:1; los HEX
  oficiales se conservan y una prueba automática lo verifica.

### Artefactos y E2E

- Servidor PyInstaller reconstruido con SHA-256
  `a2d0daf32ae0211db00fb02b7d8925e01d52b5ea9488d6e501b4572776f7568d`.
- AppImage Linux reconstruido (`CodeGuard-Pro-1.0.0-x86_64.AppImage`,
  SHA-256 `5af43286c2e5acab95c34d8f7ac6c176284c2392f57d74904ec744b31d424636`).
- E2E ejecutado sobre el AppImage con perfil temporal:
  - `/healthz/` → `{"status":"ok","database":"ok","migrations":"ok","roadmap":"ok"}`.
  - `/`, `/roadmaps/`, `/roadmaps/evaluaciones/`, `/roadmaps/evidencias/` y
    `/backups/` → HTTP 200.
  - 12 controles de tema presentes; `localStorage` + recarga aplican el tema.
  - Cierre de ventana → Django y Electron terminan; sin procesos huérfanos ni
    puerto abierto.

### Commits de la rama

`11f957a`, `e684442`, `5afee37`, `58dad2f`, `274a271`, `bf96116`, `880fbff`, `02f9583`, `fb32d3f`, `48afb1e`.

### Pendientes y bloqueos

- **Windows:** build, instalación y aceptación E2E no ejecutados en este equipo
  Linux. No declarar aceptación Windows.
- **GitHub Actions:** el entorno no resuelve `github.com` (fallo DNS) y `gh` no
  tiene sesión. No se pueden publicar commits, abrir PR ni diagnosticar los
  runs con `jobs=[]`. La configuración de Actions requiere intervención del
  propietario.
- **macOS/ARM64:** fuera de alcance de 1.0.0.
- **Sincronización remota de producción:** sin endpoint, allowlist ni claves;
  el cliente falla cerrado.
- **Contenido académico:** el JSON conserva 33/212/1946 y los defectos
  editoriales conocidos (etapa 25 sin objetivo; etapa 10 con proyecto
  anormalmente extenso). No se modificó contenido sin la fuente maestra.


### Dependencias y CI (actualización final)

- `pip-audit -r requirements.txt`: **sin vulnerabilidades conocidas** tras subir
  `cryptography` 46.0.3 → 50.0.2 y `waitress` 3.0.0 → 3.0.2.
- `npm audit`: 6 avisos moderados en la cadena de build de `electron-builder`
  (`minimatch`/`@electron/universal`), no incluidos en el runtime empaquetado.
  No se fuerza una actualización rota; se documenta como riesgo de herramienta
  de compilación.
- CI incorpora un job `packaging` que compila el servidor PyInstaller y ejecuta
  un smoke test de primer arranque, health check y modo de sincronización.
- La suite Django (291) y las pruebas Electron (15) se repitieron tras la
  actualización de dependencias y el rebuild de artefactos.
