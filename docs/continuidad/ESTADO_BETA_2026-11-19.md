# Estado de avance de beta — CodeGuard Pro

**Fecha de revisión:** 2026-11-19  
**Rama de trabajo:** `fix/electron-ipc-origin-validation`  
**Base:** `main` en `59d08848726550fde442be1eb1e1be5522637f0b`  
**HEAD actual verificado:** `2e64a0ae45aef90f16ecfb5373dc9db6120631ba`  
**Commits correctivos/documentales:** `fcca40d`, `4c32fe8`, `98d354e`, `40cfdf2`, `6907ff6`, `1d025a9`, `a892b5e`, `6178df9`, `49f463c`, `2e64a0a`  
**Pull request:** https://github.com/MaverickBms/CodeGuard-Pro/pull/12 (abierto, borrador)  
**Alcance:** inspección estática remota y corrección puntual de launcher; no equivale a ejecutar el proyecto.

## 1. Trabajo incorporado en la rama

- Se centralizó la validación de origen para IPC en `electron/ipc-security.js`.
- La comprobación exige URL válida, protocolo HTTP, host loopback esperado, puerto dinámico exacto y ausencia de credenciales.
- Se aplicó la validación a todos los canales IPC expuestos por `electron/preload.js`: tema, notificaciones, estado/solicitud de sincronización, información del sistema y selector de carpetas.
- Las notificaciones limitan título (120 caracteres) y cuerpo (1000 caracteres), y utilizan el icono local de la aplicación.
- Se añadieron seis casos de regresión en `electron/ipc-security.test.js` y el comando `npm run test:electron`.
- Se añadió `.github/workflows/ci.yml` para checks Django, migraciones, suite Django y pruebas IPC. En la revisión del 19-11 se amplió el trigger `push` a todas las ramas y se añadieron verificaciones de sintaxis Python y JavaScript antes de ejecutar las suites.
- Se corrigió el script `codeguard`: ahora exporta `CODEGUARD_DATA_DIR` inmediatamente después de crear el directorio de datos y antes de ejecutar `migrate` y `cargar_ascenso`. Electron hereda la misma variable al iniciar el AppImage. No se usa `--recrear`.
- Se actualizó este documento y la descripción del PR con los hallazgos y límites de verificación.

## 2. Evidencia y límites de verificación

### Pruebas IPC

El trabajo previo reporta una ejecución aislada de `npm run test:electron` con 6/6 pruebas correctas. Esta revisión no pudo repetirla en un checkout local, por lo que se conserva como **evidencia reportada, no reproducida independientemente en esta sesión**.

Las seis pruebas cubren origen exacto, puerto diferente, host que suplanta el prefijo loopback, protocolo no permitido, credenciales en URL y eventos/argumentos inválidos. Validan la función pura; no demuestran integración real con Electron.

### GitHub Actions

Se consultaron las ejecuciones del workflow. La consulta actual mostró once ejecuciones terminadas en fallo:

| Run | Commit | Estado |
|---|---|---|
| 1 | `670d675aaaa26dbcfe2c9b1744c0ea869cb30d40` | `completed / failure` |
| 2 | `5223e4373aee76837437ebf943f952aa691b2b0f` | `completed / failure` |
| 3 | `fcca40def7c5f7703406fb78a3274579613f13a2` | `completed / failure` |
| 4 | `4c32fe83b29c67af2565efa3a64419add26a8051` | `completed / failure` |
| 5 | `98d354e4bdb4ea77a363d4e8e301a8f77a5c29f6` | `completed / failure` |
| 6 | `40cfdf23639cf8bb6384c7297e19219af87507af` | `completed / failure` (run `44444429601`) |
| 7 | `1d025a90e47e32d4580eacf31136fece5cd50160` | `completed / failure` (run `44445369572`) |
| 8 | `a892b5e024f19a97cfbb2d25907fd427ab3796d1` | `completed / failure` (run `44445451593`) |
| 9 | `6178df902159c73b4d19995e6ab245534c7ea9ef` | `completed / failure` (run `44445508444`) |
| 10 | `49f463c6a98e8dc28e6b1314eafe675d25326b87` | `completed / failure` (run `44445540907`) |
| 11 | `2e64a0ae45aef90f16ecfb5373dc9db6120631ba` | Sin ejecución asociada al consultar Actions; sin check statuses. |

La inspección directa de Actions para los runs `44444429601`, `44445369572`, `44445451593`, `44445508444` y `44445540907` confirmó `conclusion=failure`, pero `total_count=0` y `jobs=[]`, incluso al consultar los intentos disponibles. Los check-runs/statuses consultados tampoco aportan validaciones. No hay jobs, steps ni logs de job que permitan identificar un error de ejecución. Los runs se marcan como eventos `push` sobre la rama de trabajo. El workflow en la rama actual incluye `push` sin filtro de ramas y `paths-ignore` para `docs/**` y `**.md`; sin embargo, el commit de dependencias `2e64a0a` no tiene ejecución ni check status asociado al consultar la API, aunque modifica `requirements.txt`. Esto deja dos problemas: ejecuciones fallidas sin jobs y activación inconsistente del workflow. Por tanto:

- **No se conoce la causa del fallo.**
- No se puede afirmar que hayan fallado las pruebas Django, las pruebas IPC, la instalación de dependencias o la sintaxis del workflow.
- Ninguna ejecución cuenta como validación aprobada.
- Se debe inspeccionar la vista de Actions y la configuración de Actions del repositorio para determinar por qué se crean ejecuciones fallidas sin jobs. La API disponible no expone logs de workflow/job para esos runs. No hay base para modificar las pruebas o dependencias hasta resolver esta anomalía.

Enlace: https://github.com/MaverickBms/CodeGuard-Pro/actions

### Primer arranque empaquetado

El código de `server_entry.py` contiene `_initialize_database()`, que llama a `migrate` y `cargar_ascenso` antes de iniciar Waitress en el modo servidor empaquetado. Esto parece resolver el problema descrito por QA-03 en el informe del 16-11-2026, pero necesita pruebas con directorio vacío y perfil preexistente.

El endpoint `config/health.py` comprueba DB, migraciones pendientes y existencia de un roadmap activo. Electron espera HTTP 200 y los cuatro estados `ok` antes de cargar la ventana.

### Corrección del launcher `codeguard`

La versión anterior inicializaba Django sin exportar `CODEGUARD_DATA_DIR`, por lo que podía crear/usar `BASE_DIR/data` mientras el AppImage recibía otro directorio. La corrección ya está publicada en esta rama y garantiza que las operaciones previas y Electron hereden el mismo path.

**Estado de validación:** corrección inspeccionada estáticamente; aún no se ejecutó el script en Linux con un perfil temporal. Debe probarse que ambas fases usan el mismo directorio y que la carga idempotente conserva progreso existente.

## 3. Hallazgos operativos abiertos

| Prioridad | Hallazgo | Estado / acción |
|---|---|---|
| P0 | Aceptación de instalación limpia y flujo principal Electron/Django. | Pendiente de ejecución real con perfil temporal. |
| P1 | Reproducibilidad de la suite Django completa (245 reportadas). | Pendiente de ejecutar sobre el HEAD exacto y registrar salida. |
| P1 | CI sin resultado verificable. | Once runs fallidos; los cinco más recientes consultados devuelven cero jobs. El commit de dependencias más reciente no tiene run ni status asociado. |
| P1 | Persistencia tras reinicio, modo offline E2E y cierre sin procesos huérfanos. | Pendiente. |
| P1 | Backup/restauración. | Diseño documentado; implementación/aceptación pendiente. |
| P1 | Tutor Ollama. | Opcional; validar detección, modelo instalado, timeout, fallback y privacidad. |
| P2 | `run.sh` exige Python y Node aunque inicia un AppImage empaquetado. | Revisar si es un lanzador de desarrollo; no confundirlo con instalador autónomo. |
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
- Se agregaron `python -m compileall -q config apps server_entry.py manage.py` y `node --check` para los archivos principales de Electron.\n- Se retiró `PyMuPDF==2.1` de `requirements.txt`: no se encontraron importaciones del paquete en el código revisado, está etiquetado como fase futura, añade un motor PDF nativo de gran tamaño y su licencia es AGPL-3.0 o comercial. Reincorporar una biblioteca PDF cuando haya módulo activo y decisión de licencia. Fuente oficial: https://pypi.org/project/pymupdf/2.1/.
- El trigger `push` cubre todas las ramas y omite cambios exclusivamente documentales (`docs/**`, `**.md`) para evitar ejecuciones de CI innecesarias.
- Commit publicado: `1d025a90e47e32d4580eacf31136fece5cd50160`.
- Los runs `44445369572`, `44445451593`, `44445508444` y `44445540907` terminaron en `failure` con `jobs=[]`; el commit `2e64a0a` no muestra run/status. CI sigue sin ser interpretable y no se declara aprobado.\n- Se eliminó la dependencia PyMuPDF aún no utilizada de `requirements.txt`.
- La rama está 15 commits por delante de `main`, sin commits por detrás al momento de la consulta. `main` continúa en `59d08848726550fde442be1eb1e1be5522637f0b`.

## 7. Limitación de esta sesión

Se intentó clonar la rama para ejecutar pruebas localmente, pero el entorno de esta sesión no pudo resolver `github.com` por DNS. La inspección se realizó mediante la API de GitHub y lectura de archivos remotos. No se ejecutaron Python, Django, Node, Electron, PyInstaller, instaladores ni pruebas GUI en esta sesión.

Esto no significa que el proyecto no pueda ejecutarse en el equipo del propietario; significa que esta sesión no dispone de un checkout ejecutable ni de una ruta de red para obtenerlo.

## 8. Próximo bloque recomendado

1. Diagnosticar en GitHub por qué las once ejecuciones de Actions terminaron en failure sin jobs visibles y por qué el commit `2e64a0a` no generó run/status.
2. Ejecutar el launcher `codeguard` con un directorio temporal y confirmar que migrate, carga ASCENSO y AppImage comparten `CODEGUARD_DATA_DIR`.
3. Probar `server_entry.py` en un directorio vacío y otro con datos de prueba existentes, verificando idempotencia y preservación.
4. Ejecutar en el entorno del proyecto: `pip check`, `manage.py check`, `makemigrations --check --dry-run`, las siete apps de pruebas Django, `node --check` y `npm run test:electron`.
5. Ejecutar la aceptación GUI/offline/persistencia/cierre en Linux y la instalación limpia Windows si esa es la plataforma de presentación.
6. Actualizar los documentos históricos para que reflejen el código actual y distingan evidencia reportada, ejecutada y aceptada.

**Criterio de salida:** CodeGuard Pro no debe declararse beta aceptada hasta que el primer arranque, el flujo académico esencial, la persistencia, el funcionamiento offline, la integración Electron y el cierre limpio tengan evidencia reproducible. La presentación puede describirse como beta de evaluación con limitaciones explícitas si todavía quedan criterios de distribución sin aceptar.
