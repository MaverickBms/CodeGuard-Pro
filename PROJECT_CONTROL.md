# CodeGuard Pro — Control oficial del proyecto

**Documento:** `PROJECT_CONTROL.md`  
**Versión:** 3.0 — auditoría integral, fases 2–7 integradas y estabilización de portabilidad pendiente  
**Fecha de actualización:** 2026-11-16  
**Propietario:** propietario de CodeGuard Pro  
**Mantenedor:** orquestador  
**Estado:** vigente, sujeto a autorización expresa para cada acción  
**Ubicación:** raíz del repositorio  
**Rama de trabajo:** `main`  
**Línea base de código auditada:** `main` en `26085c66ae4afd01b174b461b76d3de19d211b50`

---

## 0. Resumen ejecutivo

- **Fase 1 — UX/UI base:** completada según la línea base del proyecto; regresión visual completa de los últimos cambios sigue pendiente.
- **Fase 2 — Motor de aprendizaje:** en progreso. ASCENSO, contenido versionado, flujo editorial, paquetes firmados, instalación transaccional, rollback y cliente de sincronización están implementados parcialmente. Faltan contenido editorial completo, experiencia de práctica segura y aceptación E2E.
- **Fase 3 — Tutor IA local:** app `apps/tutoring` integrada; Ollama es opcional y existe fallback estático. Validación real de modelo, rendimiento y privacidad pendiente.
- **Fase 4 — Evaluaciones:** modelos, preguntas, resultados y criterios incorporados; corrección/progresión y UI completa pendientes.
- **Fase 5 — Gamificación:** base de perfiles, monedas, transacciones, logros, misiones y rachas integrada; balance y validación funcional pendientes.
- **Fase 6 — Mundo/avatar:** modelos y UI inicial integrados; personalización y narrativa avanzadas pendientes.
- **Fase 7 — Desafíos:** base técnica integrada; catálogo y experiencia interactiva pendientes.
- **Fase 8 — Calidad e integración:** en progreso. La instalación limpia, GUI empaquetada, offline E2E, backup/restore, matriz multiplataforma y aceptación de cierre siguen abiertas.
- **Pruebas:** README informa 245 pruebas en siete apps (16-11-2026); el subconjunto de cuatro apps aparece con 197. Reproducir el comando completo en el HEAD actual antes de release.
- **Escritorio:** Electron + Django/Waitress + SQLite + PyInstaller. El modo servidor empaquetado presupone base inicializada; se ha identificado una discrepancia en el lanzador `codeguard` y en el proceso de primer arranque Windows.
- **Distribución remota:** cliente pull-only implementado parcialmente, pero hosting, endpoint, allowlist y claves de producción no configurados. No es requisito para estudiar offline.
- **Autenticación:** `AUTH_DISABLED = True` temporalmente; el sistema original se conserva. No reactivarlo sin autorización expresa.
- **Dictamen QA:** no declarar el producto listo para distribución hasta cerrar instalación limpia, aceptación GUI, offline, persistencia, recuperación y plataformas soportadas.

Informe detallado: `docs/INFORME_QA_INTEGRAL_2026-11-16.md`.
---

## 1. Propósito y autoridad

Este documento es el **estado oficial y actualizado del proyecto**. Su finalidad es que el propietario, el orquestador, los subagentes y cualquier orquestador de relevo puedan conocer:

- qué está completado y con qué evidencia;
- qué está en curso;
- qué decisiones están aprobadas, cuáles son solo criterios aceptados y cuáles siguen siendo propuestas;
- qué restricciones y autorizaciones están vigentes;
- qué riesgos, bloqueos y pendientes existen;
- cuál es el siguiente paso autorizado.

Este documento **no es una autorización**. La autorización solo la concede el propietario de forma expresa, para una acción concreta y dentro de un alcance delimitado.

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
3. **Las autorizaciones son específicas, separadas e independientes.**
4. **Ante conflicto, prevalece la interpretación más restrictiva** y se solicita aclaración al propietario.
5. **El estado real prevalece sobre la documentación.** Git, los archivos, los hashes, la base de datos y las pruebas deben verificarse antes de actuar.
6. **No se registran credenciales, tokens, cookies, claves privadas ni información sensible.**
7. **Las correcciones se identifican como tales.** No se sobrescriben entradas anteriores de forma silenciosa.

---

## 3. Estado oficial del proyecto

### 3.1 Instantánea actual

| Elemento | Estado |
|---|---|
| Repositorio | `/home/mvxbms/Documentos/CodeGuard` |
| Línea base | `main` en `b82a249` (incluye catálogo v2, instalador, cliente HTTP, scheduler y corrección PyInstaller) |
| Rama de trabajo | `main` |
| HEAD de código auditado | `26085c66ae4afd01b174b461b76d3de19d211b50` |
| Diferencia respecto a `main` | Ninguna: documentación sincronizada directamente sobre `main` con autorización expresa |
| Remoto | `origin/main` |
| Apps instaladas | `accounts`, `audit`, `core`, `roadmaps`, `tutoring`, `gamification`, `challenges` |
| Migraciones | Roadmaps hasta 0019; tutoring 0001; gamification 0003; challenges 0001 (revalidar desde base vacía) |
| Comandos de gestión | 9; incluye `publicar_paquete_conocimiento` y `sincronizar_conocimiento` (este último en rama de trabajo) |
| Pruebas automatizadas | 245 reportadas en README para siete apps; 197 reportadas para el subconjunto de cuatro apps. Reproducibilidad en HEAD actual pendiente |
| Autenticación | `AUTH_DISABLED = True` (temporal, conservada íntegra) |
| Base de datos | SQLite, `data/db.sqlite3` |
| Servidor local | Waitress + WhiteNoise en `127.0.0.1` |

### 3.2 Evidencia principal de verificación

| Artefacto | Valor |
|---|---|
| `manage.py check` | Sin errores |
| `makemigrations --check --dry-run` | Sin cambios pendientes |
| Suite de pruebas | 245 reportadas en siete apps el 16-11-2026; ejecutar nuevamente y registrar salida íntegra |
| Migraciones desde base vacía | Verificado |
| Bind exclusivo | `127.0.0.1` (no `0.0.0.0`) |
| Dependencias fijadas | `requirements.txt` con versiones exactas |

---

## 4. Fases y estado

| Fase | Estado | Observación |
|---|---|---|
| **Fase 1 — Núcleo funcional** | ✅ Completada y verificada | Autenticación, panel, auditoría, seguridad, 12 temas, servidor local |
| **Fase 2 — Motor de aprendizaje y conocimiento versionado** | 🔄 En curso | 138 pruebas OK; PyInstaller, smoke test sync y AppImage confirmados. Aceptación GUI/Waitress y navegación curricular pendientes; hosting y claves de producción pendientes |
| **Sincronización de red / servicio central / cliente de sync** | ⏳ Parcial | Cliente HTTP/scheduler integrados; modo sync empaquetado probado; endpoint, hosting y claves de producción pendientes |
| **Competencias y evaluaciones** | ⏳ Pendiente | Incremento 3 |
| **Biblioteca documental y base de conocimiento** | ⏳ Pendiente | Incremento 4 |
| **Evidencias y laboratorios** | ⏳ Pendiente | Incremento 5 |
| **Administración y vigencia (backups)** | ⏳ Pendiente | Incremento 6 |

---

## 5. Decisiones, restricciones y autorizaciones

### 5.1 Restricciones expresas vigentes

| ID | Restricción | Estado |
|---|---|---|
| **D-003** | Mantener CSRF activo; no desactivarlo | Vigente |
| **D-004** | No añadir el origen `null` a `CSRF_TRUSTED_ORIGINS` | Vigente |
| **D-005** | No restaurar la autenticación sin autorización expresa | Vigente |
| **RS-019** | Versiones exactas fijadas en `requirements.txt` para reproducibilidad y seguridad | Vigente |

### 5.2 Reglas de sesión operativa

- No ejecutar commits, tags ni cambios de rama sin autorización expresa.
- No crear ni modificar worktrees sin autorización expresa.
- No iniciar agentes ni subagentes sin autorización expresa.
- No modificar código, configuración, plantillas, migraciones ni dependencias sin autorización expresa.
- No ejecutar migraciones ni instalaciones sin autorización expresa.
- No alterar los 12 temas visuales sin autorización y verificación de contraste.
- No modificar `data/db.sqlite3` ni datos reales.
- No copiar ni exponer `.env`, `data/.secret_key` ni credenciales.
- Comprobar `git status --porcelain=v1` y `git diff --cached` antes de cualquier operación de staging.

---

### 5.3 Autorización específica vigente — cliente HTTP de Fase 2

El propietario confirmó la validación del instalador en `main` y autorizó continuar con el siguiente componente de Fase 2: cliente de sincronización HTTP pull-only, en una rama aislada derivada de `main`.

- Rama de trabajo anterior: `feat/phase-2-http-sync-client` (histórica; ya no es la rama activa).
- Alcance: transporte HTTPS GET, allowlist, TLS validado, rechazo de redirecciones, timeout y límites de tamaño, ETag, verificación del manifiesto antes de descargar el ZIP, integración con el instalador ya validado, comando manual, pruebas y documentación relacionada.
- Se permiten commits exclusivamente en esta rama como mecanismo de escritura. No se autoriza merge, PR de integración, despliegue, publicación remota de paquetes ni cambios en `main`.
- El propietario confirmó 119 pruebas OK, `manage.py check` limpio y `makemigrations --check --dry-run` sin cambios pendientes en `main` `2c5d441`; esto incluye la migración 0016, instalador y rollback.
- Restricción original de este incremento: no elegir proveedor/hosting, publicar paquetes reales ni incorporar claves públicas de producción. La restricción sobre sincronización automática Electron fue sustituida por la autorización específica registrada en §5.4; hosting, publicación y claves de producción siguen sin autorizarse.

## 6. Pendientes de decisión o autorización del propietario

| Elemento | Estado |
|---|---|
| **Hosting/endpoint público de distribución** | Pendiente de seleccionar proveedor y autorizar publicación; no se configura en esta rama |
| **Generador central y catálogo firmado v2** | Generador, migración 0015 y catálogo v2 validados localmente por el propietario (119 pruebas OK) |
| **Instalador transaccional (migración 0016)** | Validado en `main` `2c5d441` (119 pruebas OK) |
| **Cliente de sincronización HTTP** | Integrado; 138 pruebas OK y smoke test del modo sync confirmados. No confundir con aceptación del servidor Waitress normal |
| **Competencias y evaluaciones (Incremento 3)** | Pendiente de decisión |
| **Biblioteca documental (Incremento 4)** | Pendiente de decisión |
| **Evidencias y laboratorios (Incremento 5)** | Pendiente de decisión |
| **Backups y administración (Incremento 6)** | Pendiente de decisión |
| **Reactivación de autenticación** | Pendiente de autorización expresa del propietario |
| **Commit / tag / baseline** | Actualización documental autorizada y registrada en el commit actual; tags y releases requieren autorización independiente |
| **Worktrees** | Pendiente de autorización expresa |

---

## 7. Control de cambios de este documento

| Versión | Fecha | Cambio | Autorización |
|---|---|---|---|
| 1.0 | 2026-11-07 | Creación inicial a partir de la base revisada v0.4 | D-001 |
| 2.0 | 2026-11-11 | Revisión completa tras avance de Fase 2: estado real de rama, HEAD, migraciones, comandos, pruebas y pendientes | Revisión de estado verificado |
| 2.1 | 2026-11-12 | Corrección de línea base tras fusión a main; puntero de contenido activo, snapshots de intentos, interfaz de entregas y hardening de registros | Autorización expresa del propietario; validación local confirmada por el propietario |
| 2.2 | 2026-11-12 | Generador reproducible de ZIP, manifiesto Ed25519, secuencias monotónicas, registro inmutable y comando editorial | Continuación autorizada en rama aislada; validación local confirmada por el propietario |
| 2.3 | 2026-11-12 | Catálogo normalizado de fuentes y metadatos de licencia en índice de paquete v2; verificación estricta y compatibilidad de lectura v1 | Continuación autorizada en rama aislada; validación local confirmada por el propietario (108 pruebas OK) |
| 2.4 | 2026-11-12 | Instalador transaccional, snapshots por paquete, catálogo aislado, activación, rollback, integración de lecciones e intentos, migración 0016 y pruebas | Validación local confirmada por el propietario: 119 pruebas OK en `main` `2c5d441` |
| 2.5 | 2026-11-12 | Cliente HTTP pull-only inicial, comando manual, allowlist HTTPS, TLS, ETag, límites de descarga, rechazo de redirecciones, pruebas y documentación | Continuación autorizada en rama aislada; posteriormente validado localmente (132 pruebas OK) |
| 2.6 | 2026-11-12 | Scheduler Electron, backoff exponencial, bloqueo entre procesos, proceso PyInstaller de una sola tarea, IPC limitado, pruebas y documentación | Autorización expresa del propietario |
| 2.7 | 2026-11-12 | Validación local satisfactoria de las pruebas de backoff/bloqueo y chequeos sintácticos | Confirmación del propietario |
| 2.8 | 2026-11-12 | Corrección PyInstaller (Django hidden imports) y electron-builder; propietario confirma 136 pruebas, build PyInstaller y AppImage | Autorización expresa para validación de integración |
| 2.9 | 2026-11-12 | Línea base histórica de 138 pruebas, build PyInstaller, smoke test sync y AppImage | Confirmación del propietario |\n| 3.0 | 2026-11-16 | Integración fast-forward de 75 commits a `main`; fases 3–7 incorporadas; auditoría QA integral, riesgos de primer arranque y portabilidad documentados | Solicitud del propietario de auditar, consolidar `main` y actualizar documentación |

### Reglas de actualización

1. Actualizar solo tras una acción autorizada o un cambio de estado verificado.
2. Añadir una fila al historial de cambios; no reescribir el historial anterior.
3. Si una corrección afecta a una decisión o autorización, identificarla como corrección y conservar el texto anterior.
4. Verificar que no se introducen secretos.
5. No preparar ni commitear el documento sin autorización expresa.
6. Si hay conflicto entre este documento y el estado real, prevalece el estado real y se corrige el documento.

---

**Nota de vigencia:** las autorizaciones históricas de ramas aisladas descritas en §5.3–§5.5 documentan intervenciones anteriores y no describen el estado actual de Git. Para esta actualización documental, el propietario autorizó expresamente modificar únicamente los cinco documentos enumerados y crear un commit en `main`. No se autoriza con ello modificar código, desplegar, publicar paquetes, elegir hosting ni configurar claves de producción.
### 5.4 Registro histórico — autorización del scheduler Electron y sincronización automática

**Vigencia:** autorización histórica de implementación; sus restricciones de rama y estado de `main` fueron superadas por la integración posterior. La evidencia actual se registra en §3 y §5.6.

El propietario autorizó expresamente la implementación completa de la integración Electron, scheduler, reintentos progresivos y compatibilidad con PyInstaller, manteniendo `main` intacta.

- Rama autorizada en la intervención anterior: `feat/phase-2-http-sync-client` (no usar para nuevos cambios de esta intervención).
- Alcance: temporizador Electron no bloqueante, comprobación inicial diferida, sondeo local, backoff persistente, bloqueo por canal entre procesos, comando de una sola tarea en PyInstaller, IPC limitado, pruebas y documentación.
- Se permiten commits exclusivamente en la rama autorizada como mecanismo de escritura.
- No se autoriza merge, PR de integración, despliegue, publicación remota, selección de hosting ni incorporación de URLs/claves públicas de producción.
- La sincronización debe permanecer inactiva si no hay configuración de distribución completa y confiable.
- En esa intervención se confirmó una línea base de 136 pruebas, generación PyInstaller y AppImage, y despacho del comando `sincronizar_conocimiento`. La validación posterior elevó la suite confirmada a 138 pruebas; la GUI completa sigue pendiente.
- `main` permanece intacta.

### 5.5 Registro histórico — autorización de validación de integración empaquetada

**Vigencia:** autorización de la intervención de pruebas en rama aislada. La autorización documental posterior para `main` está registrada en §5.6; el estado de Git actual se describe en §3.

El propietario autorizó crear una rama desde el `main` actualizado y completar las pruebas de integración de Electron, corregir incidencias dentro del alcance y actualizar la documentación de Fase 2.

- Rama: `test/phase-2-electron-integration`.
- Base: `main` en `2906abc922044670c029d7ff73345fdb5657dd2b`.
- Alcance: pruebas del modo `CodeGuardServer --sync-knowledge`, smoke test Linux, validación del arranque y cierre de Electron empaquetado, correcciones necesarias y documentación.
- Se permiten commits en esta rama.
- No se autoriza modificar `main`, fusionar, desplegar, publicar paquetes, elegir hosting ni configurar claves públicas/privadas de producción.
- La sincronización remota permanece desactivada mientras no exista configuración confiable.


### 5.6 Autorización específica vigente — actualización documental de integración

El propietario autorizó actualizar en `main` los siguientes cinco documentos y crear un commit único: `docs/PLAN_DESARROLLO.md`, `docs/FASE_2_APRENDIZAJE.md`, `docs/ARQUITECTURA.md`, `PROJECT_CONTROL.md` y `docs/VALIDACION_INTEGRACION_ELECTRON.md`.

El registro debe reflejar únicamente la evidencia confirmada: 138 pruebas OK; build PyInstaller; smoke test del modo `--sync-knowledge`; generación y lanzamiento del AppImage Linux. No debe declarar probados el arranque normal de Waitress, el acceso HTTP a la interfaz, la navegación por ASCENSO, el cierre normal desde el menú ni la ausencia de procesos huérfanos. El fin mediante SIGTERM con código 143 no se considera prueba de cierre limpio.

Esta autorización no incluye cambios de código, configuración de producción, hosting, endpoints, claves, publicación remota, merge adicional ni despliegue.
