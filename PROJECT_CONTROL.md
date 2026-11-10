# CodeGuard Pro — Control oficial del proyecto

**Documento:** `PROJECT_CONTROL.md`  
**Versión:** 1.0 — base revisada v0.4  
**Fecha de creación:** 2026-11-07  
**Propietario:** propietario de CodeGuard Pro  
**Mantenedor:** orquestador  
**Estado:** vigente, sujeto a autorización expresa para cada acción  
**Ubicación:** raíz del repositorio `/home/mvxbms/Documentos/Estrada/CodeGuard`

---

## 0. Resumen ejecutivo

- **F0-A está completada, verificada y aprobada documentalmente.** El respaldo, la restauración aislada y las comprobaciones de integridad constan en la evidencia indicada en el anexo B.
- **Los 24 archivos pendientes fueron verificados:** 24/24 hashes coinciden tanto en el repositorio original como en la restauración aislada.
- **Los 24 archivos fueron examinados con un escaneo heurístico de secretos y revisión manual**, incluidos los 3 archivos no rastreados. No se confirmó ninguna credencial real. El escaneo heurístico no garantiza por sí solo la ausencia de secretos.
- **En esta sesión se creó únicamente `PROJECT_CONTROL.md`.** No se ejecutaron commits, tags, cambios de rama, worktrees, agentes, F1-A, F1-B, modificaciones de código o configuración, migraciones ni instalaciones.
- **El diario privado de operaciones y el paquete de relevo se describen como propuestas de diseño.** No se han creado ni generado.
- **El siguiente paso operativo no está autorizado todavía.** F0-C sigue pendiente de decisión y F1-A, la baseline, el commit/tag, los worktrees y F1-B requieren autorización expresa e independiente.

---

## 1. Propósito y autoridad

Este documento es el **estado oficial y actualizado del proyecto**. Su finalidad es que el propietario, el orquestador, los subagentes y cualquier orquestador de relevo puedan conocer:

- qué está completado y con qué evidencia;
- qué está en curso;
- qué decisiones están aprobadas, cuáles son solo criterios aceptados y cuáles siguen siendo propuestas;
- qué restricciones y autorizaciones están vigentes;
- qué riesgos, bloqueos y pendientes existen;
- cuál es el siguiente paso autorizado.

Este documento **no es una autorización**. La autorización solo la concede el propietario de forma expresa, para una acción concreta y dentro de un alcance delimitado. La lectura de este documento, del diario o de un paquete de relevo **no hereda ni amplía autorizaciones**.

---

## 2. Reglas de interpretación

### 2.1 Niveles de decisión

| Nivel | Quién lo concede | Efecto | No implica |
|---|---|---|---|
| **Autorización expresa** | Propietario | Permite únicamente la acción y el alcance indicados | Permiso para acciones relacionadas, futuras o implícitas |
| **Restricción expresa** | Propietario | Prohíbe la acción indicada | Excepción por conveniencia técnica |
| **Criterio aceptado** | Propietario, como base de planificación | Orienta el diseño y la planificación | Autorización de ejecución |
| **Propuesta del orquestador** | Orquestador | Solo se somete a consideración | Aprobación, decisión tomada o autorización |
| **Evidencia verificada** | Comprobación reproducible | Acredita un hecho del estado del proyecto | Autorización para repetir o ampliar la acción |

### 2.2 Reglas obligatorias

1. **No atribuir al propietario decisiones que no ha aprobado.** Una propuesta no se convierte en decisión por aparecer en un informe, en el diario o en este documento.
2. **El silencio no es aprobación.** La ausencia de respuesta no autoriza continuar.
3. **Las autorizaciones son específicas, separadas e independientes.** Autorizar un documento no autoriza una estrategia; autorizar una estrategia no autoriza F1-A; autorizar F1-A no autoriza la baseline, el commit/tag, los worktrees ni F1-B.
4. **Ante conflicto, prevalece la interpretación más restrictiva** y se solicita aclaración al propietario.
5. **El estado real prevalece sobre la documentación.** Git, los archivos, los hashes, la base de datos y las pruebas deben verificarse antes de actuar.
6. **No se registran credenciales, tokens, cookies, claves privadas ni información sensible.** Las evidencias sensibles se referencian y se redactan.
7. **Las correcciones se identifican como tales.** No se sobrescriben entradas anteriores de forma silenciosa.

---

## 3. Estado oficial del proyecto

### 3.1 Instantánea al crear este documento

| Elemento | Estado |
|---|---|
| Repositorio | `/home/mvxbms/Documentos/Estrada/CodeGuard` |
| Rama | `main` |
| HEAD | `e9f2981` (`fix: corregir FOUC de temas y anadir prueba T-027 de expiracion RS-017`) |
| Remoto | `origin/main` en el mismo commit |
| Archivos rastreados | 130 |
| Archivos modificados | 21 |
| Archivos no rastreados antes de esta sesión | 3 |
| Archivos no rastreados después de esta sesión | 4 (los 3 anteriores más `PROJECT_CONTROL.md`) |
| Archivos preparados en el índice Git | 0 |
| Archivos pendientes antes de esta sesión | 24 (21 modificados + 3 no rastreados) |
| Archivos pendientes después de esta sesión | 25 (los 24 anteriores más este documento) |
| Base de datos original | `data/db.sqlite3` — no modificada en esta sesión |
| Validación visual | No realizada; no hay herramientas visuales instaladas |
| Commits, tags, ramas o worktrees creados en esta sesión | Ninguno |

### 3.2 Los 3 archivos no rastreados preexistentes

| Archivo | Función |
|---|---|
| `apps/accounts/identity.py` | Helpers y decoradores de identidad local para el modo sin autenticación |
| `apps/accounts/tests/test_modo_sin_auth.py` | Pruebas del modo sin autenticación |
| `docs/MODO_SIN_AUTENTICACION.md` | Guía del modo sin autenticación |

`PROJECT_CONTROL.md` es un cuarto archivo no rastreado. **No debe prepararse ni commitearse sin autorización expresa.**

### 3.3 Evidencia principal de F0-A

| Artefacto | Ubicación / valor |
|---|---|
| Directorio de respaldo | `/home/mvxbms/Backups/CodeGuard/F0A_20261108T015221Z` |
| Informe verificado | `F0A_REPORT.md` |
| Manifiesto final | `SHA256SUMS` — 58/58 artefactos OK |
| Manifiesto de archivos | `metadata/SHA256SUMS.files` — 513 archivos |
| Comprobación de inclusión | `metadata/included-check.txt` — 24 archivos, 3 no rastreados incluidos |
| Instantánea SQLite | `db_snapshot.sqlite3` — integridad `ok` |
| Respaldo del repositorio | `repo_snapshot.tar.zst` — SHA-256 `d0307dab8e1d393da745fb9c8c5a0bc0428b34177994e9f1c500f8dafc50ef4a` |
| Respaldo del árbol completo | `full_tree_snapshot.tar.zst` — SHA-256 `b0553acaeeca285d699abd0e780a2d3bf21dce739879b764ea641933fa71fadf` |
| Instantánea de base de datos | `db_snapshot.sqlite3` — SHA-256 `bad256edd334c26a89ba41686cd45a1d859fd9f535a63f1ec89ab219ee83c531` |
| Pruebas | 82 pruebas OK |
| Restauración aislada | `restore_test/CodeGuard` — 513/513 archivos OK |

---

## 4. Fases y estado

| Fase | Estado | Observación |
|---|---|---|
| **F0-A** | Completada, verificada y aprobada documentalmente | Respaldo, restauración aislada, hashes, pruebas e integridad SQLite verificados |
| **F0-B** | Planificación entregada; base v0.4 aceptada como base de planificación | Versiones v0.1 a v0.4; no autoriza ejecución |
| **F0-C** | **Pendiente de decisión del propietario** | Elección entre Alternativa A y Alternativa B; no se ha elegido ninguna |
| **F1-A** | **No autorizada** | Requiere autorización expresa e independiente |
| **F1-B** | **No autorizada** | Requiere autorización expresa e independiente |
| **Baseline** | **No autorizada** | Requiere autorización expresa e independiente |
| **Commit / tag** | **No autorizados** | Requiere autorización expresa e independiente |
| **Worktrees** | **No autorizados** | Requiere autorización expresa e independiente |
| **F2** | **No autorizada** | Depende de las decisiones y autorizaciones anteriores |

### 4.1 Distribución operativa de responsabilidades

| Rol | Responsabilidad | Límite |
|---|---|---|
| **Orquestador** | Planificación, coordinación, solicitud de autorizaciones, verificación de estado, registro documental | No ejecuta código ni cambios de configuración sin autorización |
| **E1** | Análisis técnico y arquitectura | Solo dentro de la tarea autorizada |
| **E2** | Implementación backend y datos | Solo dentro de la tarea autorizada; no migra ni modifica datos sin autorización |
| **E3** | Implementación frontend, UI y temas | Solo dentro de la tarea autorizada; no altera los 12 temas |
| **E4** | Verificación, pruebas, regresión y evidencias | Solo dentro de la tarea autorizada |

**Regla de ejecutores:** máximo **cuatro** ejecutores (E1, E2, E3 y E4). Las líneas **E4-T**, **E4-R** y **E4-E** son líneas internas de E4, no agentes adicionales.

La asignación concreta de cada tarea se define en la orden de trabajo correspondiente. La existencia de un rol no autoriza su activación.

---

## 5. Decisiones, restricciones y autorizaciones

### 5.1 Autorización expresa registrada

| ID | Fecha | Autorización | Alcance | Límite |
|---|---|---|---|---|
| **D-001** | 2026-11-07 | Aprobación de la base v0.4 y del orden de trabajo recomendado; autorización para crear `PROJECT_CONTROL.md` | Crear este documento en la raíz del repositorio, incorporando las salvaguardas acordadas | **Solo** la creación de este documento. No autoriza diario, paquete de relevo, estrategia, F1-A, F1-B, baseline, commit/tag, worktrees, agentes ni cambios de código/configuración |

La aprobación documental de F0-A es previa y se registra como evidencia en el anexo B. **No se reutiliza como autorización para nuevas acciones.**

### 5.2 Restricciones expresas

| ID | Restricción | Estado |
|---|---|---|
| **D-003** | Mantener CSRF activo; no desactivarlo | Vigente |
| **D-004** | No añadir el origen `null` a `CSRF_TRUSTED_ORIGINS` | Vigente |
| **D-005** | No restaurar la autenticación sin autorización expresa | Vigente |

Además, son restricciones vigentes de esta sesión:

- No ejecutar commits, tags ni cambios de rama.
- No crear ni modificar worktrees.
- No iniciar agentes ni subagentes.
- No ejecutar F1-A ni F1-B.
- No modificar código, configuración, plantillas, migraciones ni dependencias.
- No ejecutar migraciones ni instalaciones.
- No alterar los 12 temas visuales.
- No modificar `data/db.sqlite3` ni datos reales.
- No preparar archivos en el índice Git ni commitear este documento.
- No copiar ni exponer `.env`, `data/.secret_key` ni credenciales.
- No ejecutar acciones fuera del alcance autorizado.

### 5.3 Criterios aceptados como base de planificación

| ID | Criterio aceptado |
|---|---|
| **D-006** | Máximo cuatro ejecutores (E1, E2, E3, E4) |
| **D-007** | E4-T, E4-R y E4-E son líneas internas de E4, no agentes adicionales |
| **D-008** | Baseline reproducible y uso de datos aislados para pruebas y reproducciones |
| **D-009** | Pruebas y evidencias verificables antes de declarar completada una tarea |
| **D-010** | Integridad de los 12 temas visuales; no alterarlos sin autorización |
| **D-018** | Manejo prudente de secretos; el escaneo heurístico sin hallazgos no garantiza ausencia de secretos |
| **D-019** | Evidencias fuera del repositorio y redacción de información sensible |
| **D-020** | Comprobar que el índice Git esté limpio antes de cualquier operación de staging |
| **D-021** | El informe se acepta como base de planificación; no elige Alternativa A/B ni autoriza ejecución |
| **D-022** | Las autorizaciones son separadas e independientes |
| **D-023** | El relevo no hereda autorizaciones por leer el historial; debe verificar el estado real y solicitarlas |

Estos criterios **no autorizan ejecución**. Son reglas de diseño y planificación.

### 5.4 Propuestas del orquestador

| ID | Propuesta | Estado |
|---|---|---|
| **D-012** | F1 secuencial; F2 con worktrees | **Propuesta del orquestador.** No aprobada, no autorizada |
| — | Diario privado de operaciones (sección 8.2) | **Propuesta.** No creado |
| — | Paquete de continuidad y relevo (sección 8.3) | **Propuesta.** No generado |
| — | Alternativa A / Alternativa B para F0-C | **Sin elección.** El propietario debe decidir |

### 5.5 Pendientes de decisión o autorización del propietario

| Elemento | Estado |
|---|---|
| **F0-C** — elección de estrategia A/B | Pendiente de decisión |
| **P-001** — valor de N para bloqueo tras intentos fallidos | Pendiente de decisión del propietario |
| **P-002** — selección de etapas ASCENSO para el MVP | Pendiente de decisión del propietario |
| **P-003** — cifrado de backup | Pendiente de decisión del propietario |
| **F1-A** | Pendiente de autorización expresa |
| **Baseline** | Pendiente de autorización expresa |
| **Commit / tag** | Pendiente de autorización expresa |
| **Worktrees** | Pendientes de autorización expresa |
| **F1-B** | Pendiente de autorización expresa |
| **Creación del diario privado** | Pendiente de aprobación expresa |
| **Generación del paquete de relevo** | Pendiente de autorización expresa |

### 5.6 Identificadores sin contenido aprobado

Los identificadores de decisión no listados en este documento **no tienen contenido aprobado en esta base** y no deben interpretarse como autorización, criterio aceptado ni propuesta vigente. Si se necesitan, deben recuperarse del registro aprobado y añadirse mediante una revisión documentada.

---

## 6. Salvaguardas operativas

### 6.1 Seguridad

- **CSRF activo.** No se desactiva ni se relaja.
- **Sin origen `null`.** No se añade `null` a `CSRF_TRUSTED_ORIGINS`.
- **Autenticación conservada.** El modo sin autenticación es temporal; no se restaura ni se elimina sin autorización expresa.
- **12 temas intactos.** Cualquier cambio visual requiere autorización y verificación de contraste.
- **Secretos.** No se registran credenciales, tokens, cookies, claves privadas ni valores de `.env` o `data/.secret_key`.
- **Redacción.** Las evidencias con información sensible se referencian, no se copian; los valores se sustituyen por `[REDACTADO]`.

### 6.2 Git

- Comprobar `git status --porcelain=v1` y `git diff --cached` antes de cualquier operación.
- El índice debe estar limpio antes de un staging autorizado.
- No hacer staging, commit, tag, cambio de rama ni worktree sin autorización expresa.
- No usar `git add -A` ni `git add .` sin revisar previamente la lista exacta.
- No reescribir historia ni forzar push.

### 6.3 Datos y pruebas

- No modificar `data/db.sqlite3`.
- Usar la instantánea `db_snapshot.sqlite3` o copias aisladas para reproducciones.
- No ejecutar migraciones sin autorización.
- No instalar dependencias ni herramientas sin autorización.
- Registrar comandos, resultados y evidencias; no volcar salidas completas con información sensible.

### 6.4 Verificación

- Verificar hashes contra el manifiesto antes y después de una restauración.
- Ejecutar pruebas en entorno aislado cuando sea posible.
- No declarar una tarea completada sin evidencia reproducible.
- No confundir “sin hallazgos” con “sin secretos”.

---

## 7. Verificación de los 24 archivos pendientes

### 7.1 Método

Se filtró `metadata/SHA256SUMS.files` para los 24 archivos de `metadata/included-check.txt` y se ejecutó `sha256sum -c` desde:

1. la raíz del repositorio original;
2. la raíz de la restauración aislada `restore_test/CodeGuard`.

### 7.2 Resultado

| Comprobación | Resultado |
|---|---|
| Archivos verificados en el repositorio original | **24/24 OK** |
| Archivos verificados en la restauración aislada | **24/24 OK** |
| Discrepancias | **0** |
| Archivos no rastreados incluidos | **3/3** (`identity.py`, `test_modo_sin_auth.py`, `MODO_SIN_AUTENTICACION.md`) |

### 7.3 Hashes verificados

| Archivo | SHA-256 |
|---|---|
| `README.md` | `0daed1b121657d4fba831bacd339ff08c2812bc6bd3f18515ae356487e333a16` |
| `apps/accounts/tests/test_auth.py` | `a7bc73a4f6b677623818755add6b8f1cf9adbd95c3371b1d524fd3f8f0a0f7f7` |
| `apps/accounts/views.py` | `157f7baef6e37249486ce44d9d406856136b48d2c6bb6472e853b63d811a5d90` |
| `apps/audit/tests/test_audit.py` | `28e5b7530a8f52dc230893a2a442690130c129469e1e20778152aabd0bb62aa4` |
| `apps/core/tests/test_panel.py` | `e46f24dfc15752558a1cca206b3b17156e511566a9f377f7e946af6214d77bf6` |
| `apps/core/views.py` | `57ef9ac563e36da2d61cdf7c9f1f61db2817496a15a3eacbdcf2e71e81226f0b` |
| `apps/roadmaps/services.py` | `5f876398cc0bed05de34460f8398910c6508c239e0bdbc7d0cae47174e2d4e5c` |
| `apps/roadmaps/tests/test_roadmaps.py` | `0699e5d0b7ef36770298a2b162e483c806551e7077dadc1b24c2cd3de6f3f85b` |
| `apps/roadmaps/views.py` | `9378e3717901755a7baa8d41b5bc92e1014faf6c206982fd0c94a73da66d1c7a` |
| `config/middleware.py` | `d02beab84cc8faaa4826e2665e1ed4d5c35df7bcae296244f390e9460d4367b7` |
| `config/settings/base.py` | `24b5cf1c9f7051fbc9ac6981a0a595b1e916e1517ff0145512ddc9987304c6f6` |
| `config/settings/desktop.py` | `549d79df324b162200ed232b40772890993b4de3e8ad0febf5c0f44b98323125` |
| `docs/ARQUITECTURA.md` | `71475e8748e7f9748ba54c4b09e6f25c84a881528dde71dd0ff480ad6243447b` |
| `docs/CHANGELOG.md` | `2d07ec309053241ae64954dd00e787051bc48890671b3706c62efb29aeb778bd` |
| `docs/MANUAL_USUARIO.md` | `c99e258fff8ed7ad37e3b77b9025fabafbfe45f560b5f0b500e2e60866b24585` |
| `docs/PLAN_DESARROLLO.md` | `2ceeaad8af95507dbb245ee3cd902c045d7c3e2a0cff29b83d8fc8f5f214455f` |
| `docs/PLAN_PRUEBAS.md` | `2fb8aa793503e0be7e55028173cfa57307931f85cf0364a956ed119d15b7072e` |
| `docs/REVISION_SRS.md` | `66ff789795518f0dfb4cb1371d51188d898b9620eeb473ae66a11f3c21a82e5d` |
| `docs/SEGURIDAD.md` | `775a20c17a4737deed046f5919b537fce8d1fd8851f64750daef799136220da9` |
| `templates/base.html` | `8283ab37451e3d3421f72356d733cdccced37e46e73499fa937f3e5a5d6150fb` |
| `templates/core/panel.html` | `eb33729c353487306022f41fd95eb15c59dc95f60787fe508c7035fbdee661be` |
| `apps/accounts/identity.py` | `f5074b85303ab52f48c159dabc7ac031d97d333b57545fed92d2dc78e0199f89` |
| `apps/accounts/tests/test_modo_sin_auth.py` | `2ebdbed73d4e2b2ce2efe08af7f9145873d756cfd071845b29d848b36f8fa9a1` |
| `docs/MODO_SIN_AUTENTICACION.md` | `9525fc6106e25cb4fb41fdc53f460c28bfa0b516467c0a4aff8b535e3a475cd6` |

### 7.4 Escaneo heurístico de secretos

Se aplicaron reglas heurísticas sobre los 24 archivos completos: claves AWS, bloques de clave privada, asignaciones literales de secretos/contraseñas/tokens, variables de entorno, tokens Bearer, cadenas de conexión con contraseña, cadenas hexadecimales de 64 caracteres, JWT y prefijos de proveedores conocidos.

| Resultado | Detalle |
|---|---|
| Archivos escaneados | 24/24 |
| Hallazgos brutos | 18 |
| Hallazgos revisados manualmente | 18/18 |
| Credenciales reales confirmadas | **0** |
| Archivos no rastreados revisados manualmente | 3/3 |

**Revisión manual:**

- La mayoría de los hallazgos son contraseñas literales de **fixtures de prueba** en archivos `test_*.py`. No son credenciales reales ni acceden a servicios externos.
- `apps/accounts/views.py` contiene una **referencia** a `form.cleaned_data[...]`, no un secreto embebido.
- `config/settings/base.py` obtiene `SECRET_KEY` de `DJANGO_SECRET_KEY` o de `data/.secret_key`; no hay una clave literal versionada en el archivo.
- Los 3 archivos no rastreados no contienen secretos: `identity.py` solo define helpers y decoradores; la prueba usa una contraseña de fixture; la guía no incluye credenciales.
- **No se reproducen los valores sensibles en este documento.**

**Limitación:** el escaneo es heurístico. Cero hallazgos no garantiza ausencia de secretos. La revisión manual y la revisión de credenciales reales siguen siendo necesarias antes de cualquier publicación.

---

## 8. Sistema de continuidad operativa

### 8.1 Artefactos y autoridad

| Artefacto | Función | Autoridad | Estado |
|---|---|---|---|
| `PROJECT_CONTROL.md` | Estado oficial y actualizado del proyecto | Documento de referencia; no autoriza | Creado en esta sesión |
| Diario privado de operaciones | Registro cronológico, persistente y auditable | Evidencia factual; no autoriza | **Propuesto, no creado** |
| Paquete de relevo | Instantánea para sustituir al orquestador o cambiar de cuenta | Material de traspaso; no autoriza | **Propuesto, no generado** |

**Precedencia:** el estado real (Git, archivos, hashes, base de datos y pruebas) prevalece sobre los tres artefactos. La autorización expresa del propietario prevalece sobre cualquier documento.

### 8.2 Propuesta de diario privado de operaciones

> **Estado: propuesta. No crear hasta recibir aprobación expresa.**

#### Ubicación propuesta

```
/home/mvxbms/Backups/CodeGuard/operaciones/
├── diario/
│   ├── diario-2026-11.jsonl
│   ├── diario-2026-12.jsonl
│   └── SHA256SUMS
├── indices/
│   └── INDICE.md
└── respaldos/
    └── diario-2026-11.tar.zst
```

- Fuera del repositorio.
- Directorio propietario: `0700`.
- Archivos: `0600`.
- `umask 077` durante la escritura.
- Sin acceso de grupo ni de otros usuarios.

#### Formato

- **JSON Lines (`.jsonl`)**: una entrada JSON por línea, append-only.
- Rotación mensual por nombre ordenable.
- Cada entrada incluye `prev_hash` y `entry_hash` para cadena de integridad.
- `INDICE.md` es una vista generada; no es la fuente de verdad.
- Las correcciones son entradas nuevas con `correccion_de: "<entry_id>"`; nunca se edita ni se borra una entrada anterior.

#### Campos mínimos de cada entrada

| Campo | Contenido |
|---|---|
| `entry_id` | Identificador único (UUIDv7 o ULID) |
| `timestamp_utc` | Fecha y hora ISO 8601 en UTC |
| `tarea_id` | Identificador de la tarea |
| `fase` | F0-A, F0-B, F0-C, F1-A, etc. |
| `agente` | Orquestador, E1, E2, E3 o E4; línea E4-T/E4-R/E4-E si aplica |
| `objetivo` | Objetivo de la actuación |
| `alcance_autorizado` | Autorización concreta y sus límites |
| `archivos_examinados` | Rutas relativas |
| `archivos_modificados` | Rutas relativas; vacío si no hubo cambios |
| `acciones` | Acciones ejecutadas, sin volcar terminal completa |
| `pruebas` | Comandos, resultados y estado |
| `evidencias` | Rutas y hashes de evidencias conservadas |
| `decisiones` | Decisiones tomadas y justificación |
| `incidencias` | Incidencias y riesgos |
| `bloqueos` | Bloqueos activos |
| `estado_final` | Estado al cerrar la entrada |
| `pendientes` | Tareas pendientes |
| `autorizaciones` | Autorizaciones recibidas y su alcance |
| `limites` | Restricciones vigentes |
| `prev_hash` | Hash de la entrada anterior del mismo archivo |
| `entry_hash` | Hash de la entrada actual |
| `correccion_de` | `entry_id` corregido, si aplica |
| `redaccion` | `true` si se eliminó información sensible |

#### Procedimiento de actualización

1. El orquestador abre el archivo del mes con `O_APPEND` y un bloqueo `flock`.
2. Calcula `prev_hash` leyendo la última línea.
3. Construye la entrada con los campos mínimos.
4. Sustituye cualquier valor sensible por `[REDACTADO]`.
5. Escribe **una sola línea** y fuerza la sincronización.
6. Calcula y actualiza `SHA256SUMS` del mes.
7. Verifica la cadena de hashes.
8. Cierra el bloqueo.

**Quién escribe:** solo el orquestador. Los subagentes entregan su informe estructurado al orquestador; no escriben directamente en el diario para evitar carreras y entradas inconsistentes.

#### Qué no registrar

- Credenciales, tokens, cookies, claves privadas ni valores de `.env`.
- Volcados completos de terminal.
- Datos personales innecesarios.
- Rutas o contenidos sensibles sin redactar.

#### Respaldo

- Copia del mes cerrado a un segundo medio.
- Archivo `diario-AAAA-MM.tar.zst` + `SHA256SUMS`.
- Verificación de hash tras cada copia.
- Cifrado opcional con `age` o `gpg` **solo si ya está disponible**; no instalar herramientas sin autorización.
- Retención indefinida; no borrar entradas.

#### Aprobación requerida

La creación del diario, su ubicación definitiva, el formato y el procedimiento de respaldo requieren **aprobación expresa del propietario**. Hasta entonces, esta sección es solo una propuesta.

### 8.3 Diseño del paquete de continuidad y relevo

> **Estado: propuesta. No generar hasta recibir autorización expresa.**

#### Cuándo se genera

- Sustitución del orquestador.
- Cambio de cuenta o de entorno.
- Pausa prolongada.
- Incidente que afecte a la continuidad.
- Cierre de una fase relevante.

#### Ubicación propuesta

```
/home/mvxbms/Backups/CodeGuard/relevo/<AAAA-MM-DDTHHMMSSZ>/
```

Fuera del repositorio, con permisos `0700` para el directorio y `0600` para los archivos.

#### Contenido mínimo

| Archivo | Contenido |
|---|---|
| `00_LEEME.md` | Propósito, fecha, alcance y advertencia de que no hereda autorizaciones |
| `01_ESTADO.md` | Rama, HEAD, índice, archivos modificados/no rastreados, estado de fases |
| `02_COMPLETADO.md` | Fases y tareas completadas, con evidencia y hashes |
| `03_EN_CURSO.md` | Trabajo en curso, responsable y estado exacto |
| `04_DECISIONES.md` | Autorizaciones expresas, restricciones, criterios aceptados y propuestas, con IDs y fechas |
| `05_RESPONSABILIDADES.md` | Orquestador, E1-E4 y límites; máximo cuatro ejecutores |
| `06_RIESGOS_BLOQUEOS.md` | Riesgos, bloqueos, incidencias y dependencias |
| `07_SIGUIENTE_PASO.md` | Único siguiente paso autorizado; si no hay autorización, indicarlo |
| `08_ENTORNO.md` | Rutas, versiones, herramientas disponibles y limitaciones |
| `09_EVIDENCIAS.md` | Rutas de evidencias, hashes y criterios de redacción |
| `10_VERIFICACION.md` | Comandos reproducibles para verificar el estado real |
| `MANIFEST.sha256` | Hashes de todos los archivos del paquete |

#### Procedimiento de generación

1. Leer `PROJECT_CONTROL.md` y el diario.
2. Verificar el estado real de Git, archivos, hashes y base de datos.
3. Reunir evidencia de lo completado y de lo que está en curso.
4. Separar claramente autorizaciones, restricciones, criterios y propuestas.
5. Redactar información sensible.
6. Escribir el paquete fuera del repositorio.
7. Calcular `MANIFEST.sha256`.
8. Verificar el manifiesto.
9. Registrar la generación en el diario (cuando exista).
10. Entregar al propietario la ruta y el hash del manifiesto.

#### Protocolo del nuevo orquestador

1. Leer `00_LEEME.md` y `PROJECT_CONTROL.md`.
2. **No asumir autorizaciones por leer el historial.**
3. Verificar el estado real: rama, HEAD, índice, archivos pendientes, hashes y base de datos.
4. Comparar el estado real con el paquete; registrar discrepancias.
5. Revisar riesgos, bloqueos y pendientes.
6. Identificar el siguiente paso autorizado; si no existe, solicitarlo.
7. Confirmar con el propietario el alcance antes de actuar.
8. Registrar la recepción y las verificaciones en el diario.
9. No ejecutar F1-A, F1-B, baseline, commit/tag, worktrees, agentes ni cambios de código/configuración sin autorización expresa.
10. Si hay conflicto entre el paquete y el estado real, prevalece el estado real y se detiene la ejecución.

### 8.4 Relación entre los artefactos

- `PROJECT_CONTROL.md` responde a **“¿cuál es el estado oficial?”**
- El diario responde a **“¿qué ocurrió, cuándo, quién y con qué autorización?”**
- El paquete de relevo responde a **“¿qué necesita saber un nuevo orquestador para continuar sin heredar autorizaciones?”**

Ninguno de los tres sustituye la verificación del estado real ni la autorización expresa del propietario.

---

## 9. Control de cambios de este documento

| Versión | Fecha | Cambio | Autorización |
|---|---|---|---|
| 1.0 | 2026-11-07 | Creación inicial a partir de la base revisada v0.4, con estado real, verificaciones, salvaguardas y diseño de continuidad | D-001 |

### Reglas de actualización

1. Actualizar solo tras una acción autorizada o un cambio de estado verificado.
2. Añadir una fila al historial de cambios; no reescribir el historial anterior.
3. Si una corrección afecta a una decisión o autorización, identificarla como corrección y conservar el texto anterior.
4. Verificar que no se introducen secretos.
5. No preparar ni commitear el documento sin autorización expresa.
6. Si hay conflicto entre este documento y el estado real, prevalece el estado real y se corrige el documento.

---

## 10. Declaración de alcance de esta sesión

- **Archivo creado:** `PROJECT_CONTROL.md` en la raíz del repositorio.
- **Archivos modificados:** ninguno.
- **Archivos preparados en el índice Git:** ninguno.
- **Commits, tags, ramas o worktrees:** ninguno.
- **Agentes o subagentes iniciados:** ninguno.
- **F1-A, F1-B, baseline, commit/tag, worktrees o F2:** no ejecutados.
- **Cambios de código, configuración, plantillas, migraciones o dependencias:** ninguno.
- **Instalaciones:** ninguna.
- **Base de datos original:** no modificada.
- **Diario privado:** no creado.
- **Paquete de relevo:** no generado.
- **Validación visual:** no realizada.
- **Estado de Git antes:** 21 modificados, 3 no rastreados, índice vacío, HEAD `e9f2981`.
- **Estado de Git después:** 21 modificados, 4 no rastreados (los 3 anteriores más `PROJECT_CONTROL.md`), índice vacío, HEAD `e9f2981`.

**El trabajo se detiene aquí a la espera de nuevas instrucciones.**

---

## Anexo A — Los 24 archivos pendientes y sus hashes

Los hashes de la tabla 7.3 son la referencia verificada. La comprobación se realizó contra `metadata/SHA256SUMS.files` desde la raíz del proyecto y desde `restore_test/CodeGuard`: **24/24 OK en ambas ubicaciones**.

## Anexo B — Evidencia de F0-A

- Directorio: `/home/mvxbms/Backups/CodeGuard/F0A_20261108T015221Z`
- Informe: `F0A_REPORT.md`
- Manifiesto final: `SHA256SUMS` — 58/58 artefactos OK
- Manifiesto de archivos: `metadata/SHA256SUMS.files` — 513 archivos
- Inclusión de los 24 archivos: `metadata/included-check.txt`
- Restauración aislada: `restore_test/CodeGuard`
- Integridad SQLite: `ok`
- Pruebas: 82 OK

## Anexo C — Evidencias de esta sesión

Las comprobaciones de esta sesión se conservan fuera del repositorio, en `/tmp/opencode/`:

| Archivo | Contenido |
|---|---|
| `cg24.sha256` | Manifiesto filtrado de los 24 archivos |
| `cg24-root-check.txt` | Resultado de `sha256sum -c` en el repositorio original |
| `cg24-restore-check.txt` | Resultado de `sha256sum -c` en la restauración aislada |
| `scan_secrets.py` | Reglas heurísticas aplicadas |
| `show_redacted.py` | Revisión de hallazgos con valores redactados |

Estas evidencias son temporales. Si se requiere conservación permanente, deben copiarse a un directorio privado fuera del repositorio con permisos restrictivos y un manifiesto de hashes, previa autorización.
