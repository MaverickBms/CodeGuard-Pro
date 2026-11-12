# CodeGuard Pro — Control oficial del proyecto

**Documento:** `PROJECT_CONTROL.md`  
**Versión:** 2.4 — instalador transaccional de paquetes  
**Fecha de actualización:** 2026-11-12  
**Propietario:** propietario de CodeGuard Pro  
**Mantenedor:** orquestador  
**Estado:** vigente, sujeto a autorización expresa para cada acción  
**Ubicación:** raíz del repositorio  
**Rama de correcciones autorizada:** `fix/phase-2-integrity-learning` (derivada de `main`; contiene el instalador en desarrollo)  
**Línea base:** `main` en `cd7e18e`; los commits posteriores permanecen en la rama autorizada

---

## 0. Resumen ejecutivo

- **Fase 1 (núcleo funcional):** completada, verificada y aprobada documentalmente. Autenticación local, panel, roadmap, auditoría y seguridad operativos.
- **Fase 2 (motor de aprendizaje y conocimiento versionado):** en curso; `main` contiene el verificador, publicador y catálogo firmado v2. El instalador transaccional y su integración académica están en desarrollo en `fix/phase-2-integrity-learning`.
  - Roadmap ASCENSO 3.1 (33 etapas, módulos, lecciones, prerrequisitos) implementado y cargable con `cargar_ascenso`.
  - Contenido académico editable (`ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion`) implementado.
  - Flujo editorial de versiones (`VersionContenidoLeccion`, `ReferenciaFuenteContenido`, `FuenteConocimiento`) implementado con comandos de gestión.
  - Registro local de paquetes de conocimiento (`PaqueteConocimientoInstalado`, `EstadoSincronizacion`) implementado con transiciones controladas e identidad inmutable.
  - Verificador de distribución firmada (Ed25519, manifiesto, ZIP) implementado (`validate_package_archive`, `verify_signed_manifest`).
  - Puntero editorial `ContenidoLeccionActivo` para seleccionar snapshots publicados y mantener el borrador editable separado.
  - Intentos nuevos vinculados a la versión activa y con snapshot del ejercicio presentado.
  - Interfaz de entrega POST con CSRF, límite de 20.000 caracteres e historial de intentos.
  - Protecciones adicionales para escrituras masivas del registro local de paquetes y sincronización.
  - El propietario confirmó **108 pruebas OK**, `manage.py check` sin errores y `makemigrations --check --dry-run` sin cambios pendientes para el estado de `main` en `cd7e18e`. La migración 0016 y las pruebas del instalador añadidas después están pendientes de validación local.
- **Sincronización de red:** publicador local e instalador transaccional inicial en la rama correctiva; cliente HTTP, hosting, endpoint y activación desde Electron pendientes.
- **Validación del instalador:** pendiente de ejecución local de la migración 0016 y de las nuevas pruebas específicas; no afecta a la validación ya confirmada de `main`.
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
| Línea base | `main` en `cd7e18e` (incluye la corrección del catálogo v2) |
| Rama de correcciones | `fix/phase-2-integrity-learning` |
| HEAD de correcciones | Consultar `fix/phase-2-integrity-learning`; contiene commits posteriores a `main`, no fusionados |
| Remoto | `origin/fix/phase-2-integrity-learning` |
| Apps instaladas | `accounts`, `audit`, `core`, `roadmaps` |
| Migraciones roadmaps | 0014 y 0015 validadas localmente por el propietario; 0016 añadida en la rama correctiva y pendiente de ejecución local |
| Comandos de gestión | 9 (`cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`) |
| Pruebas automatizadas | 108 OK confirmadas en `main` antes del instalador; pruebas de `test_installer` pendientes de ejecución local |
| Autenticación | `AUTH_DISABLED = True` (temporal, conservada íntegra) |
| Base de datos | SQLite, `data/db.sqlite3` |
| Servidor local | Waitress + WhiteNoise en `127.0.0.1` |

### 3.2 Evidencia principal de verificación

| Artefacto | Valor |
|---|---|
| `manage.py check` | Sin errores |
| `makemigrations --check --dry-run` | Sin cambios pendientes |
| Suite de pruebas | 108 OK confirmadas para `main` en `cd7e18e`; nuevas pruebas de instalación y rollback pendientes |
| Migraciones desde base vacía | Verificado |
| Bind exclusivo | `127.0.0.1` (no `0.0.0.0`) |
| Dependencias fijadas | `requirements.txt` con versiones exactas |

---

## 4. Fases y estado

| Fase | Estado | Observación |
|---|---|---|
| **Fase 1 — Núcleo funcional** | ✅ Completada y verificada | Autenticación, panel, auditoría, seguridad, 12 temas, servidor local |
| **Fase 2 — Motor de aprendizaje y conocimiento versionado** | 🔄 En curso | Roadmap, flujo editorial, verificador, publicador y catálogo v2 en `main`; instalador transaccional en rama correctiva; cliente HTTP y hosting pendientes |
| **Sincronización de red / servicio central / cliente de sync** | ⏳ Parcial | Publicador local implementado y validadado en `main`; instalador offline inicial en rama correctiva, pendiente de validación local; transporte HTTP, endpoint, hosting y Electron pendientes |
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

### 5.3 Autorización específica vigente — correcciones de Fase 2

El propietario autorizó ejecutar las correcciones de consistencia identificadas en la auditoría, en una rama nueva derivada de `main`, incluyendo cambios de código, migraciones, pruebas y documentación.

- Rama autorizada: `fix/phase-2-integrity-learning`.
- Alcance: interfaz de entregas, snapshots de intentos, puntero editorial activo, protecciones del registro local, publicador central, catálogo v2, instalador transaccional, snapshots de paquete, intentos vinculados al paquete, activación, rollback, pruebas y documentación relacionada.
- Se permiten commits exclusivamente en esa rama como mecanismo de escritura del repositorio.
- No se autoriza merge, PR de integración, despliegue, publicación remota de paquetes, cambios en `main`, instalaciones ni migraciones sobre la base de datos local. La migración 0016 debe validarse primero en el entorno local del propietario.
- El propietario confirmó 108 pruebas OK, `manage.py check` limpio y `makemigrations --check --dry-run` sin cambios pendientes en `main` `cd7e18e`. La migración 0016, el servicio instalador y las pruebas INS-001 a INS-012 están añadidos en la rama correctiva y pendientes de validación local.

## 6. Pendientes de decisión o autorización del propietario

| Elemento | Estado |
|---|---|
| **Hosting/endpoint público de distribución** | Pendiente de selección de proveedor y autorización |
| **Generador central y catálogo firmado v2** | Generador, migración 0015 y catálogo v2 validados localmente por el propietario (108 pruebas OK) |
| **Instalador transaccional (migración 0016)** | Implementado inicialmente en rama correctiva; pendiente de migración y pruebas locales |\n| **Cliente de sincronización HTTP / hosting** | Pendiente de selección técnica y autorización específica |
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
| 2.3 | 2026-11-12 | Catálogo normalizado de fuentes y metadatos de licencia en índice de paquete v2; verificación estricta y compatibilidad de lectura v1 | Continuación autorizada en rama aislada; validación local confirmada por el propietario (108 pruebas OK) |\n| 2.4 | 2026-11-12 | Instalador transaccional, snapshots por paquete, catálogo aislado, activación, rollback, integración de lecciones e intentos, migración 0016 y pruebas | Continuación autorizada en rama aislada; validación local pendiente |

### Reglas de actualización

1. Actualizar solo tras una acción autorizada o un cambio de estado verificado.
2. Añadir una fila al historial de cambios; no reescribir el historial anterior.
3. Si una corrección afecta a una decisión o autorización, identificarla como corrección y conservar el texto anterior.
4. Verificar que no se introducen secretos.
5. No preparar ni commitear el documento sin autorización expresa.
6. Si hay conflicto entre este documento y el estado real, prevalece el estado real y se corrige el documento.

---

**El alcance autorizado continúa únicamente en `fix/phase-2-integrity-learning`; `main` permanece intacta. Detenerse antes de merge, despliegue, publicación remota o ampliación de alcance.**