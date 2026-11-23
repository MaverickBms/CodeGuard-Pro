# Auditoría final de CodeGuard Pro 1.0.0

**Fecha:** 2026-11-21
**Rama auditada:** `release/1.0.0-final`
**Base del PR:** `release/1.0.0`
**Commit inicial de referencia:** `e17721f`
**PR:** [#17](https://github.com/MaverickBms/CodeGuard-Pro/pull/17) (abierto, sin fusionar)

> Esta auditoría se ejecutó sobre el árbol real del repositorio. Los resultados
> de pruebas, rutas y artefactos se separan de las comprobaciones que dependen de
> hardware o servicios externos. Nada se declara verificado por inferencia.

## 1. Estado inicial

El punto de partida era un release candidate funcional:

- Aplicación Electron + Django + SQLite con servidor en `127.0.0.1`.
- 349 pruebas Django y 26 pruebas Node/Electron en verde.
- Migraciones al día.
- Roadmap ASCENSO 3.1 con 33 etapas, 212 módulos y 1.946 títulos.
- 8 lecciones redactadas del módulo 0.1 en estado borrador.
- 0 lecciones aprobadas o publicadas.
- Espacio editorial, biblioteca PDF, tutor local, gamificación, backups y
  paneles de cobertura implementados.
- Windows validado únicamente en CI; macOS/ARM64 y sincronización remota fuera
  de alcance.

La revisión no encontró una vulnerabilidad crítica que justificara bloquear la
entrega, pero sí dos defectos de integridad relevantes y varias inconsistencias
de menor severidad.

## 2. Componentes revisados

| Área | Elementos |
|---|---|
| Aplicación | `server_entry.py`, `run.sh`, `codeguard`, `CodeGuardServer.spec` |
| Configuración | `config/settings/{base,development,desktop}.py`, `config/urls.py`, middleware, health |
| Backend | 8 apps, 50 modelos, 39 migraciones, vistas, formularios, servicios y comandos |
| Identidad | propietario local, bootstrap, permisos editoriales, autenticación conservada |
| Roadmap | instalación idempotente, manifiesto, huellas, prerrequisitos y progreso |
| Contenido | 8 lecciones, 8 ejemplos, 16 ejercicios, 8 videos, 13 fuentes |
| Editorial | versiones, snapshots, licencias, revisión, publicación y retirada |
| Evaluaciones | quizzes/exámenes, respuestas, resultados inmutables y homologación |
| Tutor | Ollama local, timeout, fallback, límite de 3 pistas y contexto |
| Biblioteca | importación PDF, SHA-256, duplicados, rangos HTTP y archivo |
| Gamificación | monedas, logros, misiones, racha, avatar e inventario |
| Electron | IPC, preload, context isolation, sandbox, CSP, navegación y cierre |
| Frontend | 27 plantillas HTML, JavaScript propio, 12 temas, accesibilidad y responsive |
| Backups | creación, verificación, restauración transaccional y rollback |
| CI/CD | workflows, empaquetado, pruebas Windows y auditorías de dependencias |
| Documentación | README, informes, inventario, rendimiento y limitaciones |

## 3. Hallazgos y correcciones

### A-01 — Identidad local: elevación implícita de la primera cuenta (Alta, corregida)

**Problema.** `asegurar_propietario_local()` tomaba la primera cuenta activa y
`_asegurar_permiso_editorial()` la convertía en `is_staff`. En un perfil con
varias cuentas, o restaurado desde otro equipo, podía elevar una cuenta que no
era el propietario previsto. La marca de propietario no era explícita.

**Corrección.**

- Nueva columna `Usuario.es_propietario_local` y migración
  `accounts.0003_usuario_es_propietario_local`.
- El propietario marcado tiene prioridad.
- Se acepta el nombre reservado heredado `propietario-local` como identificación
  explícita de compatibilidad.
- Si hay varias cuentas activas y ninguna es inequívoca, el arranque no elige ni
  eleva ninguna; el perfil queda en modo lectura y se registra una advertencia.
- El comando de siembra ya no eleva cuentas: exige que el arranque haya
  habilitado al propietario explícito.
- Se añadieron pruebas de cuenta ordinaria, perfil ambiguo y nombre heredado.

**Riesgo residual.** El propietario sigue siendo una identidad local sin
credenciales mientras `AUTH_DISABLED=True`. Esto es una decisión de producto
documentada, no una autenticación remota. El servidor solo escucha en loopback.

### A-02 — Progreso: una lección podía revocar una etapa ya aprobada (Alta, corregida)

**Problema.** `recalcular_progreso_etapa()` reescribía el estado de la etapa a
`en_progreso` y borraba `fecha_completado` cada vez que se recalculaba el avance
de lecciones. Completar o reabrir una lección después de aprobar la etapa podía
perder la aprobación persistida.

**Corrección.** Si la etapa ya está `completado`, el recálculo de lecciones es
informativo y no altera estado, porcentaje ni fecha. Se añadió una regresión en
`test_roadmaps`.

### A-03 — Editorial: pérdida de datos en formularios inválidos (Media, corregida)

**Problema.** Al fallar la validación del contenido o de un video, la vista
reconstruía un formulario vacío y descartaba el texto enviado. El usuario podía
perder una edición larga.

**Corrección.** La vista conserva los formularios ligados y sus errores; el
formulario de licencia también conserva los datos inválidos. Se añadió una
prueba que verifica que el texto enviado sigue visible tras un error.

### A-04 — Videos: verificación técnica confundida con aprobación pedagógica (Media, corregida)

**Problema.** Los videos sembrados tenían `estado_revision="aprobado"` tras
verificar solo enlace, título, canal, duración e idioma. La interfaz no separaba
esa verificación técnica de una revisión pedagógica real.

**Corrección.**

- Nuevos campos `estado_pedagogico`, `notas_pedagogicas`,
  `revisado_pedagogicamente_en` y `revisado_pedagogicamente_por`.
- Los 8 videos existentes quedan con revisión pedagógica **pendiente**.
- La aprobación pedagógica exige enlace previamente verificado, fecha, actor y
  notas de correspondencia didáctica.
- La vista del estudiante muestra explícitamente «Revisión pedagógica
  pendiente» cuando corresponde.
- Se prohíben enlaces `http://` en recursos audiovisuales.

### A-05 — CI: el PR de release no ejecutaba los workflows (Media, corregida)

**Problema.** El workflow solo se activaba en `pull_request` contra `main`; el
PR #17 tiene como base `release/1.0.0`, por lo que no se ejecutaba en el evento
de PR. La evidencia Windows existente provenía de `workflow_dispatch`.

**Corrección.** Se añadieron `release/1.0.0` y `release/**` como ramas de PR.
El empaquetado Windows también se ejecuta en pushes a `release/1.0.0-final`.
Se añadieron auditorías `pip-audit` y `npm audit --omit=dev` al CI.

### A-06 — Contraseña inicial sin validadores completos (Media, corregida)

**Problema.** El formulario de configuración inicial solo comprobaba longitud
mínima; no aplicaba los validadores de Django.

**Corrección.** Se aplica `validate_password()` además de la comprobación de
longitud y confirmación. El flujo de autenticación sigue desactivado por diseño.

### A-07 — Documentación con cifras y rutas contradictorias (Media, corregida)

**Problema.** README e informes mencionaban 7 rutas HTTP y 349 pruebas, mientras
el smoke vigente comprobaba 9 rutas y la suite ya tenía más pruebas. El run de
Windows no estaba vinculado a su commit exacto.

**Corrección.** Se actualizaron los documentos a:

- 356 pruebas Django en esta iteración.
- 26 pruebas Node/Electron.
- 9 rutas HTTP del smoke actual.
- Run Windows `44945721326` sobre el commit `5747ec6` (4/4 jobs), no sobre
  `e17721f`.
- Artefactos antiguos identificados como tales; los nuevos se documentan con su
  hash y commit de origen.

### A-08 — Detalles de accesibilidad y estabilidad (Baja, corregidos)

- Se sustituyó `transition: all` por propiedades concretas.
- Las opciones futuras de la barra lateral llevan etiqueta y título que indican
  «No disponible en CodeGuard Pro 1.0.0».
- Se bloquean envíos duplicados de formularios deshabilitando el botón tras el
  evento `submit`, con restauración en `pageshow`.

### A-09 — Duplicados PDF bajo concurrencia (Media, corregido en esta revisión)

**Problema.** La vista comprobaba el SHA-256 antes de guardar, pero dos procesos
podían superar esa consulta simultáneamente y crear dos registros con el mismo
contenido. El conflicto de base de datos tampoco limpiaba necesariamente el
archivo que el campo FileField hubiera escrito antes del INSERT.

**Corrección.**

- Restricción única condicional sobre SHA-256 no vacío, aplicada en SQLite.
- La consulta previa se conserva para ofrecer un mensaje claro; la restricción
  de base de datos es la autoridad ante carreras concurrentes.
- La vista traduce únicamente el conflicto cuando ya existe el hash ganador,
  elimina el archivo huérfano y no oculta otros errores de integridad.
- Migración library.0002_unique_document_sha256: comprueba duplicados
  históricos y aborta sin borrar ni modificar documentos si encuentra alguno.
- Se añadieron dos pruebas para la unicidad a nivel de base de datos y la
  compatibilidad de registros históricos sin hash. La ejecución de estas
  pruebas queda pendiente de la CI del commit actual.

### A-10 — Recomendación de videos rechazados (Media, corregido en esta revisión)

**Problema.** La consulta de recursos para el estudiante filtraba enlaces
técnicamente aprobados y disponibles, pero no excluía un video que el editor
hubiera rechazado en la revisión pedagógica. Un recurso considerado
didácticamente inadecuado podía seguir apareciendo como recomendación.

**Corrección.** El catálogo del estudiante ahora admite videos con revisión
pedagógica pendiente (identificados explícitamente como no validados) o aprobada,
y excluye los rechazados. Se añadió una prueba de regresión sobre el contenido
sembrado. La ejecución de esta prueba queda pendiente de la CI del HEAD actual.

## 4. Funcionalidades verificadas

| Área | Verificación |
|---|---|
| Arranque limpio | Migraciones, propietario, roadmap y 8 lecciones sembradas |
| Persistencia | Lección completada, intento, tema e ítem de biblioteca sobreviven al reinicio |
| Roadmap | 33/212/1.946/7 comprobados contra el manifiesto |
| Lecciones | Contenido, fuentes, videos y ejercicios renderizados |
| Ejercicio | Respuesta correcta aprobada en backend y lección completada |
| Editorial | Flujo probado por pruebas; formularios inválidos conservan datos |
| Biblioteca | Importación PDF real, visor, archivo y restauración |
| Tutor | Estado con/sin Ollama y fallback determinista probados con mocks |
| Backups | Crear, verificar, restaurar en perfil aislado y comprobar datos |
| Frontend | 9 rutas 200, 12 temas, 13 pantallas responsive, formulario real |
| Electron | IPC/seguridad y cierre sin procesos huérfanos |
| Seguridad | CSRF, CSP, loopback, uploads, backups y dependencias auditadas |

## 5. Funcionalidades incompletas o fuera de alcance

- Revisión humana independiente del contenido académico.
- 1.938 lecciones sin cuerpo desarrollado.
- Revisión pedagógica de los 8 videos (queda pendiente y visible).
- Publicación editorial: es una decisión explícita, no automática; no se publicó
  contenido durante la auditoría.
- Sandbox de ejecución de código.
- Sincronización remota de producción (sin endpoint ni claves públicas).
- Laboratorios, competencias, vigencia y ética.
- macOS, ARM64 y aceptación en hardware Windows físico.
- Revisión manual de respuestas abiertas: el sistema las deja pendientes y no las
  aprueba; no existe todavía una pantalla de revisión docente.

## 6. Riesgos residuales

| Riesgo | Severidad | Estado |
|---|---|---|
| Propietario local sin credenciales mientras `AUTH_DISABLED=True` | Aceptado por diseño | Servidor solo loopback; escrituras asociadas al propietario marcado |
| Perfil con varias cuentas ambiguas | Bajo | Falla cerrado: no elige ni eleva; requiere resolución manual |
| Respuestas abiertas pendientes para siempre | Medio funcional | Documentado; no se autoaprueban |
| Windows no probado en hardware físico | Medio de distribución | CI 4/4; aceptación física pendiente |
| Sincronización remota no operativa | Bajo (offline-first) | Falla cerrada; no hay conexiones |
| Duplicado de PDF en concurrencia | Bajo | La comprobación secuencial existe; no hay restricción única en SQLite |
| AppImage actual no probado con montaje FUSE directo | Bajo de plataforma | Se ejecutó con extracción; se documenta el fallback |

## 7. Plan de ejecución aplicado

1. Auditar repositorio, rama, PR y estado de CI.
2. Ejecutar línea base de pruebas y análisis de dependencias.
3. Corregir identidad y permisos.
4. Corregir integridad de progreso.
5. Corregir formularios editoriales y distinguir video técnico/pedagógico.
6. Endurecer CI y validaciones.
7. Ejecutar suite completa, smoke Electron, E2E de aprendizaje, backup/restore.
8. Reconstruir artefactos y calcular hashes.
9. Actualizar documentación y PR.
10. No fusionar, no crear tag ni release definitiva.

## 8. Conclusión

No se identificaron bloqueos críticos después de las correcciones. La versión
queda **lista con limitaciones documentadas**: el producto funciona dentro de su
alcance local, pero la aceptación Windows física, la revisión pedagógica de
videos, la ampliación del contenido y la infraestructura remota siguen fuera de
lo demostrado en esta iteración. El veredicto completo y la evidencia están en
[`INFORME_FINAL_1.0.0.md`](INFORME_FINAL_1.0.0.md).
