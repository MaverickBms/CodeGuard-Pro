# CodeGuard Pro — Control oficial del proyecto

**Documento:** `PROJECT_CONTROL.md`  
**Versión:** 2.0 — revisado tras avance de la Fase 2 (motor de aprendizaje y conocimiento versionado)  
**Fecha de actualización:** 2026-11-11  
**Propietario:** propietario de CodeGuard Pro  
**Mantenedor:** orquestador  
**Estado:** vigente, sujeto a autorización expresa para cada acción  
**Ubicación:** raíz del repositorio  
**Rama actual:** `docs/phase-2-hybrid-knowledge-sync`  
**HEAD:** `6a16f93` (sincronizado con `origin/docs/phase-2-hybrid-knowledge-sync`)

---

## 0. Resumen ejecutivo

- **Fase 1 (núcleo funcional):** completada, verificada y aprobada documentalmente. Autenticación local, panel, roadmap, auditoría y seguridad operativos.
- **Fase 2 (motor de aprendizaje y conocimiento versionado):** en curso / parcialmente implementada en la rama `docs/phase-2-hybrid-knowledge-sync`.
  - Roadmap ASCENSO 3.1 (33 etapas, módulos, lecciones, prerrequisitos) implementado y cargable con `cargar_ascenso`.
  - Contenido académico editable (`ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion`) implementado.
  - Flujo editorial de versiones (`VersionContenidoLeccion`, `ReferenciaFuenteContenido`, `FuenteConocimiento`) implementado con comandos de gestión.
  - Registro local de paquetes de conocimiento (`PaqueteConocimientoInstalado`, `EstadoSincronizacion`) implementado con transiciones controladas e identidad inmutable.
  - Verificador de distribución firmada (Ed25519, manifiesto, ZIP) implementado (`validate_package_archive`, `verify_signed_manifest`).
  - Suite de pruebas: **93 pruebas pasando** (`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`).
- **Sincronización de red, servicio central y cliente de sincronización:** pendientes (Fase 2, no implementados en la rama principal).
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
| Rama | `docs/phase-2-hybrid-knowledge-sync` |
| HEAD | `6a16f93` |
| Remoto | `origin/docs/phase-2-hybrid-knowledge-sync` |
| Apps instaladas | `accounts`, `audit`, `core`, `roadmaps` |
| Migraciones roadmaps | 0001 a 0013 (todas aplicadas) |
| Comandos de gestión | 9 (`cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`) |
| Pruebas automatizadas | 93 OK (`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`) |
| Autenticación | `AUTH_DISABLED = True` (temporal, conservada íntegra) |
| Base de datos | SQLite, `data/db.sqlite3` |
| Servidor local | Waitress + WhiteNoise en `127.0.0.1` |

### 3.2 Evidencia principal de verificación

| Artefacto | Valor |
|---|---|
| `manage.py check` | Sin errores |
| `makemigrations --check --dry-run` | Sin cambios pendientes |
| Suite de pruebas | 93 pruebas OK |
| Migraciones desde base vacía | Verificado |
| Bind exclusivo | `127.0.0.1` (no `0.0.0.0`) |
| Dependencias fijadas | `requirements.txt` con versiones exactas |

---

## 4. Fases y estado

| Fase | Estado | Observación |
|---|---|---|
| **Fase 1 — Núcleo funcional** | ✅ Completada y verificada | Autenticación, panel, auditoría, seguridad, 12 temas, servidor local |
| **Fase 2 — Motor de aprendizaje y conocimiento versionado** | 🔄 En curso (rama de trabajo) | Roadmap ASCENSO, contenido académico, flujo editorial, registro de paquetes, verificador de distribución |
| **Sincronización de red / servicio central / cliente de sync** | ⏳ Pendiente | Fase 2, no implementados en rama principal |
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

## 6. Pendientes de decisión o autorización del propietario

| Elemento | Estado |
|---|---|
| **Sincronización de red** | Pendiente de decisión y autorización |
| **Servicio central de publicación** | Pendiente de decisión y autorización |
| **Cliente de sincronización** | Pendiente de decisión y autorización |
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

### Reglas de actualización

1. Actualizar solo tras una acción autorizada o un cambio de estado verificado.
2. Añadir una fila al historial de cambios; no reescribir el historial anterior.
3. Si una corrección afecta a una decisión o autorización, identificarla como corrección y conservar el texto anterior.
4. Verificar que no se introducen secretos.
5. No preparar ni commitear el documento sin autorización expresa.
6. Si hay conflicto entre este documento y el estado real, prevalece el estado real y se corrige el documento.

---

**El trabajo se detiene aquí a la espera de nuevas instrucciones.**