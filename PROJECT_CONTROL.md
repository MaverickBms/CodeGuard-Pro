# CodeGuard Pro — Control oficial del proyecto

**Documento:** `PROJECT_CONTROL.md`  
**Versión:** 2.9 — 138 pruebas y smoke test PyInstaller confirmados; aceptación GUI pendiente  
**Fecha de actualización:** 2026-11-12  
**Propietario:** propietario de CodeGuard Pro  
**Mantenedor:** orquestador  
**Estado:** vigente, sujeto a autorización expresa para cada acción  
**Ubicación:** raíz del repositorio  
**Rama de trabajo autorizada:** `test/phase-2-electron-integration` (derivada de `main` `2906abc`; pruebas de integración empaquetada y documentación)  
**Línea base:** `main` en `2906abc`; incluye correcciones PyInstaller/Django y electron-builder/Linux

---

## 0. Resumen ejecutivo

- **Fase 1 (núcleo funcional):** completada, verificada y aprobada documentalmente. Autenticación local, panel, roadmap, auditoría y seguridad operativos.
- **Fase 2 (motor de aprendizaje y conocimiento versionado):** en curso; `main` contiene el verificador, publicador, catálogo firmado v2, instalador transaccional, cliente HTTP y scheduler; el propietario confirmó 136 pruebas OK en la versión actualizada `2906abc` (la línea base previa del instalador fue de 119 pruebas en `2c5d441`). El cliente HTTP y las pruebas unitarias de backoff/bloqueo del scheduler fueron validados localmente por el propietario en `feat/phase-2-http-sync-client`. El propietario confirmó la generación del ejecutable PyInstaller y del AppImage Linux. El binario ya carga Django y alcanza `sincronizar_conocimiento`; la ejecución GUI completa con Electron y el ciclo de vida de procesos siguen pendientes de una prueba de aceptación.
  - Roadmap ASCENSO 3.1 (33 etapas, módulos, lecciones, prerrequisitos) implementado y cargable con `cargar_ascenso`.
  - Contenido académico editable (`ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion`) implementado.
  - Flujo editorial de versiones (`VersionContenidoLeccion`, `ReferenciaFuenteContenido`, `FuenteConocimiento`) implementado con comandos de gestión.
  - Registro local de paquetes de conocimiento (`PaqueteConocimientoInstalado`, `EstadoSincronizacion`) implementado con transiciones controladas e identidad inmutable.
  - Verificador de distribución firmada (Ed25519, manifiesto, ZIP) implementado (`validate_package_archive`, `verify_signed_manifest`).
  - Puntero editorial `ContenidoLeccionActivo` para seleccionar snapshots publicados y mantener el borrador editable separado.
  - Intentos nuevos vinculados a la versión activa y con snapshot del ejercicio presentado.
  - Interfaz de entrega POST con CSRF, límite de 20.000 caracteres e historial de intentos.
  - Protecciones adicionales para escrituras masivas del registro local de paquetes y sincronización.
  - El propietario confirmó **136 pruebas OK** después de corregir PyInstaller y electron-builder. En esta rama se agregaron dos pruebas del despacho `--sync-knowledge` (la nueva suite debe confirmar 138 pruebas); también se añadió un smoke test reproducible del binario Linux. La generación de PyInstaller y AppImage fue confirmada por el propietario; falta ejecutar las nuevas pruebas y validar el ciclo de vida de la aplicación Electron empaquetada.
- **Sincronización de red:** cliente HTTP, backoff y bloqueo entre procesos implementados; PyInstaller y AppImage Linux generados; el binario alcanza el comando de sincronización y devuelve el error de configuración esperado cuando faltan variables. La integración GUI completa y las pruebas añadidas están pendientes de ejecución local. Hosting, endpoint y claves de producción siguen pendientes.
- **Validación de pruebas:** el propietario reportó 136 pruebas OK. Las dos pruebas nuevas de `server_entry` y el smoke test del binario deben ejecutarse en el entorno local para cerrar esta intervención.
- **Autenticación:** temporalmente desactivada (`AUTH_DISABLED = True`); el sistema original se conserva íntegro y puede reactivarse con autorización expresa.

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
| Línea base | `main` en `2906abc` (incluye catálogo v2, instalador, correcciones PyInstaller y electron-builder) |
| Rama de trabajo | `test/phase-2-electron-integration` |
| HEAD de trabajo | Rama de pruebas derivada de `main`; no fusionada |
| Diferencia respecto a `main` | Rama de trabajo con commits no fusionados; `main` sin modificar |
| Remoto | `origin/test/phase-2-electron-integration` |
| Apps instaladas | `accounts`, `audit`, `core`, `roadmaps` |
| Migraciones roadmaps | 0014, 0015 y 0016 validadas por el propietario; esta intervención no añade migraciones |
| Comandos de gestión | 9; incluye `publicar_paquete_conocimiento` y `sincronizar_conocimiento` (este último en rama de trabajo) |
| Pruebas automatizadas | 138 OK confirmadas por el propietario; `manage.py check`, `makemigrations --check --dry-run` y `node --check` correctos. Smoke test Linux y reconstrucción PyInstaller confirmados. Integración GUI Electron pendiente |
| Autenticación | `AUTH_DISABLED = True` (temporal, conservada íntegra) |
| Base de datos | SQLite, `data/db.sqlite3` |
| Servidor local | Waitress + WhiteNoise en `127.0.0.1` |

### 3.2 Evidencia principal de verificación

| Artefacto | Valor |
|---|---|
| `manage.py check` | Sin errores |
| `makemigrations --check --dry-run` | Sin cambios pendientes |
| Suite de pruebas | 119 OK en baseline histórica; 132 OK en validación HTTP anterior; 138 OK confirmadas por el propietario en la rama de integración |
| Migraciones desde base vacía | Verificado |
| Bind exclusivo | `127.0.0.1` (no `0.0.0.0`) |
| Dependencias fijadas | `requirements.txt` con versiones exactas |

---

## 4. Fases y estado

| Fase | Estado | Observación |
|---|---|---|
| **Fase 1 — Núcleo funcional** | ✅ Completada y verificada | Autenticación, panel, auditoría, seguridad, 12 temas, servidor local |
| **Fase 2 — Motor de aprendizaje y conocimiento versionado** | 🔄 En curso | Motor, cliente HTTP, scheduler y empaquetado implementados; 138 pruebas y smoke test PyInstaller confirmados; aceptación GUI pendiente; hosting y claves de producción pendientes |
| **Sincronización de red / servicio central / cliente de sync** | ⏳ Parcial | Cliente HTTP, scheduler y backoff implementados; ejecución PyInstaller y smoke test confirmados; aceptación GUI, endpoint, hosting y claves de producción pendientes |
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
| **Cliente de sincronización HTTP** | Validado por el propietario; 136 pruebas de la base confirmadas. PyInstaller/AppImage generados; el binario alcanza el comando de sync con error de configuración esperado. Nuevas pruebas `server_entry` pendientes de ejecutar |
| **Competencias y evaluaciones (Incremento 3)** | Pendiente de decisión |
| **Biblioteca documental (Incremento 4)** | Pendiente de decisión |
| **Evidencias y laboratorios (Incremento 5)** | Pendiente de decisión |
| **Backups y administración (Incremento 6)** | Pendiente de decisión |
| **Reactivación de autenticación** | Pendiente de autorización expresa del propietario |
| **Commit / tag / baseline** | Pendiente de autorización expresa |
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
| 2.8 | 2026-11-12 | Corrección PyInstaller (Django hidden imports) y electron-builder; propietario confirma 136 pruebas, build PyInstaller y AppImage; nueva rama con pruebas de despacho y smoke test Linux | Autorización expresa para validación de integración en rama aislada |
| 2.9 | 2026-11-12 | Propietario confirma 138 pruebas OK, checks Django/migraciones/Node correctos, reconstrucción PyInstaller y smoke test Linux satisfactorios; queda aceptación GUI del AppImage | Confirmación del propietario |

### Reglas de actualización

1. Actualizar solo tras una acción autorizada o un cambio de estado verificado.
2. Añadir una fila al historial de cambios; no reescribir el historial anterior.
3. Si una corrección afecta a una decisión o autorización, identificarla como corrección y conservar el texto anterior.
4. Verificar que no se introducen secretos.
5. No preparar ni commitear el documento sin autorización expresa.
6. Si hay conflicto entre este documento y el estado real, prevalece el estado real y se corrige el documento.

---

**El alcance autorizado de esta intervención se limita a `test/phase-2-electron-integration`, derivada de `main` `2906abc`. `main` no debe modificarse. Detenerse antes de merge, despliegue, publicación remota o configuración de claves/hosting.**
### 5.4 Autorización específica vigente — scheduler Electron y sincronización automática

El propietario autorizó expresamente la implementación completa de la integración Electron, scheduler, reintentos progresivos y compatibilidad con PyInstaller, manteniendo `main` intacta.

- Rama autorizada en la intervención anterior: `feat/phase-2-http-sync-client` (no usar para nuevos cambios de esta intervención).
- Alcance: temporizador Electron no bloqueante, comprobación inicial diferida, sondeo local, backoff persistente, bloqueo por canal entre procesos, comando de una sola tarea en PyInstaller, IPC limitado, pruebas y documentación.
- Se permiten commits exclusivamente en la rama autorizada como mecanismo de escritura.
- No se autoriza merge, PR de integración, despliegue, publicación remota, selección de hosting ni incorporación de URLs/claves públicas de producción.
- La sincronización debe permanecer inactiva si no hay configuración de distribución completa y confiable.
- El propietario confirmó 136 pruebas OK, generación PyInstaller y AppImage Linux, y que el binario alcanza el comando `sincronizar_conocimiento` con el error esperado por variables ausentes. La ejecución GUI completa con Electron aún debe validarse.
- `main` permanece intacta.

### 5.5 Autorización vigente — validación de integración empaquetada

El propietario autorizó crear una rama desde el `main` actualizado y completar las pruebas de integración de Electron, corregir incidencias dentro del alcance y actualizar la documentación de Fase 2.

- Rama: `test/phase-2-electron-integration`.
- Base: `main` en `2906abc922044670c029d7ff73345fdb5657dd2b`.
- Alcance: pruebas del modo `CodeGuardServer --sync-knowledge`, smoke test Linux, validación del arranque y cierre de Electron empaquetado, correcciones necesarias y documentación.
- Se permiten commits en esta rama.
- No se autoriza modificar `main`, fusionar, desplegar, publicar paquetes, elegir hosting ni configurar claves públicas/privadas de producción.
- La sincronización remota permanece desactivada mientras no exista configuración confiable.


### 5.6 Evidencia de validación — 138 pruebas y PyInstaller

El 12 de noviembre de 2026, el propietario confirmó en `test/phase-2-electron-integration`:

- 138 pruebas Django ejecutadas y aprobadas.
- `manage.py check`: sin problemas.
- `makemigrations --check --dry-run`: sin cambios.
- `node --check electron/main.js` y `node --check electron/preload.js`: correctos.
- Reconstrucción de PyInstaller y smoke test Linux: funcionamiento satisfactorio.

**Pendiente:** reconstruir el AppImage para incorporar el ejecutable PyInstaller actualizado y completar la aceptación GUI descrita en `docs/VALIDACION_INTEGRACION_ELECTRON.md`. No se autoriza merge ni despliegue.
