# Estado de avance de beta — CodeGuard Pro

**Fecha de revisión:** 2026-11-18 (hora local del propietario)  
**Rama de trabajo:** `fix/electron-ipc-origin-validation`  
**Base:** `main` en `59d08848726550fde442be1eb1e1be5522637f0b`  
**HEAD revisado:** `5223e4373aee76837437ebf943f952aa691b2b0f`  
**Pull request:** https://github.com/MaverickBms/CodeGuard-Pro/pull/12 (abierto, borrador)  
**Alcance de esta revisión:** inspección estática remota; no equivale a ejecutar el proyecto.

## 1. Trabajo incorporado en la rama

- Se centralizó la validación de origen para IPC en `electron/ipc-security.js`.
- La comprobación exige URL válida, protocolo HTTP, host loopback esperado, puerto dinámico exacto y ausencia de credenciales.
- Se aplicó la validación a todos los canales IPC expuestos por `electron/preload.js`: tema, notificaciones, estado/solicitud de sincronización, información del sistema y selector de carpetas.
- Las notificaciones limitan título (120 caracteres) y cuerpo (1000 caracteres), y utilizan el icono local de la aplicación.
- Se añadieron seis casos de regresión en `electron/ipc-security.test.js` y el comando `npm run test:electron`.
- Se añadió `.github/workflows/ci.yml` para checks Django, migraciones, suite Django y pruebas IPC.

## 2. Evidencia y límites de verificación

### Pruebas IPC

El registro de trabajo anterior reporta una ejecución aislada de `npm run test:electron` con 6/6 pruebas correctas. Esta revisión no pudo repetirla en un checkout local, por lo que se conserva como **evidencia reportada, no reproducida independientemente en esta sesión**.

Las seis pruebas cubren origen exacto, puerto diferente, host que suplanta el prefijo loopback, protocolo no permitido, credenciales en URL y eventos/argumentos inválidos. Validan la función pura; no demuestran integración real con Electron.

### GitHub Actions

La consulta del repositorio encontró dos ejecuciones asociadas al workflow:

| Ejecución | Commit | Estado remoto |
|---|---|---|
| #1 | `670d675aaaa26dbcfe2c9b1744c0ea869cb30d40` | `completed / failure` |
| #2 | `5223e4373aee76837437ebf943f952aa691b2b0f` | `completed / failure` |

En esta consulta, el endpoint de jobs devolvió una lista vacía para ambas ejecuciones y no se obtuvieron check-runs ni logs de jobs. Por tanto:

- **No se conoce la causa del fallo.**
- No se puede afirmar que hayan fallado las pruebas Django, las pruebas IPC, la instalación de dependencias o la sintaxis del workflow.
- Tampoco se puede contar ninguna de esas ejecuciones como validación aprobada.
- La siguiente acción es inspeccionar los detalles visibles de Actions en GitHub y determinar si se trata de un error de inicialización del workflow, permisos/configuración del repositorio o un job real.

Enlace: https://github.com/MaverickBms/CodeGuard-Pro/actions

### Inspección estática de primer arranque

El código actual de `server_entry.py` contiene `_initialize_database()`, que llama a `migrate` y `cargar_ascenso` antes de iniciar Waitress en el modo servidor empaquetado. Esto **parece corregir** el hallazgo QA-03 del informe del 16-11-2026, que describía una inicialización externa.

La corrección todavía requiere pruebas en un directorio de datos vacío y en uno preexistente. Debe comprobarse que:
- la base, migraciones y roadmap quedan en el mismo `CODEGUARD_DATA_DIR` utilizado por Electron;
- la carga es idempotente;
- no se utiliza `--recrear`;
- el progreso existente no se elimina ni se reinicia;
- el endpoint `/healthz/` llega a estado `ok` solo cuando DB, migraciones y roadmap están disponibles.

El endpoint `config/health.py` comprueba DB, migraciones pendientes y existencia de un roadmap activo. Electron espera HTTP 200 y los cuatro estados `ok` antes de cargar la ventana.

## 3. Hallazgos documentales y operativos abiertos

| Prioridad | Hallazgo | Estado / acción |
|---|---|---|
| P0 | El script raíz `codeguard` define `DATA_DIR`, pero no exporta `CODEGUARD_DATA_DIR` antes de ejecutar migraciones y cargar ASCENSO. | Puede inicializar otra base distinta de la usada por AppImage. Corregir y probar con directorio temporal si se mantiene como lanzador soportado. |
| P0 | Aceptación de instalación limpia y flujo principal Electron/Django. | Pendiente de ejecución real con perfil temporal. |
| P1 | Reproducibilidad de la suite Django completa (245 reportadas). | Pendiente de ejecutar sobre el HEAD exacto y registrar salida. |
| P1 | CI sin resultado verificable. | Dos ejecuciones reportadas como failure, sin jobs/logs accesibles en esta revisión. |
| P1 | Persistencia tras reinicio, modo offline E2E y cierre sin procesos huérfanos. | Pendiente. |
| P1 | Backup/restauración. | Diseño documentado; implementación/aceptación pendiente. |
| P1 | Tutor Ollama. | Opcional; validar detección, modelo instalado, timeout, fallback y privacidad. |
| P2 | `run.sh` exige Python y Node aunque inicia un AppImage que ya contiene Electron y el servidor empaquetado. | Revisar si es solo lanzador de desarrollo; no confundirlo con instalador autónomo. |
| P2 | Documentos históricos no totalmente sincronizados. | Revisar especialmente `docs/VALIDACION_INTEGRACION_ELECTRON.md`, QA-03, estados de fases y cifras históricas de pruebas. |

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

## 6. Limitación de esta sesión

Se intentó clonar la rama para ejecutar pruebas localmente, pero el entorno de esta sesión no pudo resolver `github.com` por DNS. La inspección se realizó mediante la API de GitHub y lectura de archivos remotos. No se ejecutaron Python, Django, Node, Electron, PyInstaller, instaladores ni pruebas GUI en esta sesión.

Esto no significa que el proyecto no pueda ejecutarse en el equipo del propietario; significa que esta sesión no dispone de un checkout ejecutable ni de una ruta de red para obtenerlo.

## 7. Próximo bloque recomendado

1. Diagnosticar en GitHub por qué las dos ejecuciones de Actions terminaron en failure sin jobs visibles.
2. Corregir el script `codeguard` para exportar `CODEGUARD_DATA_DIR` antes de cualquier comando Django, si se mantiene como punto de entrada soportado; añadir una prueba de regresión aislada.
3. Probar `server_entry.py` en un directorio vacío y otro con datos de prueba existentes, verificando idempotencia y preservación.
4. Ejecutar en el entorno del proyecto: `pip check`, `manage.py check`, `makemigrations --check --dry-run`, las siete apps de pruebas Django, `node --check` y `npm run test:electron`.
5. Ejecutar la aceptación GUI/offline/persistencia/cierre en Linux y la instalación limpia Windows si esa es la plataforma de presentación.
6. Actualizar los documentos históricos para que reflejen el código actual y distinguir claramente evidencia reportada, ejecutada y aceptada.

**Criterio de salida:** CodeGuard Pro no debe declararse beta aceptada hasta que el primer arranque, el flujo académico esencial, la persistencia, el funcionamiento offline, la integración Electron y el cierre limpio tengan evidencia reproducible. La presentación puede describirse como beta de evaluación con limitaciones explícitas si todavía quedan criterios de distribución sin aceptar.
