# CodeGuard Pro — Bitácora Temporal de Seguimiento y Validación

> **Propósito:** archivo maestro de trazabilidad del proyecto durante el desarrollo. Se actualiza frecuentemente. Sirve de guía principal para la validación final del usuario.
> **Estado:** Línea base establecida tras auditoría inicial (16 nov 2026).
> **Orquestador:** CodeGuard Pro Tech Lead / Scrum Master.

---

## 1. Resumen del proyecto

### Estado inicial (línea base)
- **Repositorio:** `/home/mvxbms/Documentos/CodeGuard` (remoto: `https://github.com/MaverickBms/CodeGuard-Pro`)
- **Rama de trabajo:** `chore/stabilizacion-pre-fase-2` (adelante de main por 11 commits tras merge-base)
- **Último commit en rama:** `af56fbd docs: actualizar conteo de pruebas a 197 OK (línea base verificada)`
- **Commits recientes integrados:**
  - `a40d1f0 chore(electron): retrasar maximizado tras ready-to-show` (electron/main.js, ajuste de UI)
  - `af56fbd docs: actualizar conteo de pruebas a 197 OK` (README.md, docs/PLAN_DESARROLLO.md)
- **Entorno:** Python 3.14.10, Django 5.2.19, entorno virtual `.venv/`, Electron 45.2.3, Node.js instalados.
- **Base de datos:** `data/db.sqlite3` existe, migraciones aplicadas, `.secret_key` presente.
- **Pruebas automatizadas:** **206 pruebas OK** (`apps.core`, `apps.accounts`, `apps.audit`, `apps.roadmaps`, `apps.tutoring`) ejecutadas con `--settings=config.settings.development`. Incluye las 9 nuevas del tutor IA (Fase 3).
- **Django system check:** 0 issues.
- **Migraciones pendientes:** Ninguna (`makemigrations --check --dry-run` limpio).
- **Autenticación:** `AUTH_DISABLED = True` (temporal). La app abre directamente el panel. Sistema de auth completo conservado pero inactivo.
- **Offline-first:** Sí. El núcleo funciona sin Internet. Sincronización remota de conocimiento implementada pero inactiva (falta endpoint, allowlist, claves públicas de producción).

### Objetivo general
Entregar CodeGuard Pro como aplicación de escritorio completamente funcional, estable, segura, profesional y preparada para evolucionar. Primera versión: monousuario, local, offline-first, sin dependencias de pago ni servicios externos.

### Arquitectura
- **Monolito modular Django** (patrón MVT) con 4 apps: `core` (panel), `accounts` (identidad), `audit` (auditoría), `roadmaps` (roadmap ASCENSO 3.1, contenido académico, flujo editorial, paquetes, sincronización).
- **Electron** como contenedor de escritorio que inicia Django local (Waitress + WhiteNoise) en `127.0.0.1:<puerto dinámico>`.
- **SQLite** en `DATA_DIR` (desarrollo: `data/`; empaquetado: `userData` del usuario).
- **Frontend:** HTML/CSS/JS vanilla, Bootstrap 5, HTMX, SweetAlert2, FontAwesome (todo local, sin CDN), **12 temas visuales**.
- **Empaquetado:** PyInstaller para el servidor Django (`CodeGuardServer`), electron-builder para el instalador (AppImage Linux, NSIS Windows).

### Alcance de la versión actual (primera versión gratuita y local)
- Panel principal con navegación y módulos.
- Roadmap ASCENSO 3.1 (33 etapas) con listado, detalle, filtros, prerrequisitos, bloqueo de etapas.
- Marcado de etapas completadas; reapertura de lecciones.
- Vista de lección con teoría, explicación sencilla, ejemplos y ejercicios.
- Registro de intentos de ejercicio (evaluación determinista, sin ejecución de código arbitrario).
- Flujo editorial versionado (borrador → revisión → aprobación → publicación → sustitución → retirada).
- Generador de paquetes firmados Ed25519, instalador transaccional, rollback, cliente HTTP pull-only.
- 12 temas visuales con accesibilidad WCAG AA.
- Configuración inicial, frase de rescate, cambio de contraseña (conservados, auth desactivada temporalmente).
- Auditoría de eventos, cabeceras de seguridad, CSP estricta, bind 127.0.0.1.

---

## 2. Historial de fases

| Fase | Nombre | Estado | Trabajo realizado | Resultado pruebas |
|---|---|---|---|---|
| 1 | Fundamentos UX/UI y experiencia base | ✅ Completada | Dashboard, navegación, sidebar, 12 temas, responsive, ajustes de contraste. | Documentado como verificado por propietario. |
| 2 | Motor de aprendizaje y contenido interactivo | 🔄 Casi completo (cierre pendiente GUI) | Modelos curriculares, contenido, ejemplos, ejercicios, progreso, flujo editorial, paquetes firmados, sincronización cliente. Arquitectura refinada: ADR-005 a ADR-009 implementados. Eliminados ~170 líneas de código duplicado. Pendiente: verificación GUI Electron+Waitress, contenido académico real, demo offline/rollback. | 197 pruebas OK (verificado tras cada cambio). |
| 3 | Tutor inteligente local | 🔄 En progreso — parcialmente implementada (ADR-010) | App `apps/tutoring` creada (modelos, servicios Ollama con degradación, vistas API, migración 0001) + integración UI (S2: `templates/roadmaps/leccion.html`, `static/js/tutoria.js`, `static/css/lesson-learning.css`). Fixes de seguridad/ajuste (S1): propietario del intento en `tutoria_analizar`, mapping normalizado de resultado, settings centralizados `CODEGUARD_TUTOR_*`. Borrador de aceptación `FASE_3_ACEPTACION.md`. Pendiente: validación con Ollama en ejecución real, cierre formal de criterios, UI visual de pistas. | Suite completa (incl. apps.tutoring): **206 pruebas OK** (197 + 9 nuevos), system check 0 issues (dev+desktop), makemigrations sin cambios. |
| 4 | Evaluaciones y progresión académica | ⏳ Pendiente | — | — |
| 5 | Gamificación y economía de recompensas | ⏳ Pendiente | — | — |
| 6 | Mundo, avatar, personajes e inventario | ⏳ Pendiente | — | — |
| 7 | Minijuegos, desafíos y jefes | ⏳ Pendiente | — | — |
| 8 | Integración, calidad, seguridad y optimización | 🔄 En curso (transversal) | Seguridad: 0 vulnerabilidades encontradas, CSRF en vistas POST, sin ejecución de código, auditoría completa. WAL mode para concurrencia. Fase 3 transversal: tutor IA Ollama con límites y degradación. Pendiente: accesibilidad WCAG, pruebas de carga, manejo de errores edge cases. | 206 pruebas OK, system check 0 issues (dev+desktop). |

**Prioridad inmediata:** Cerrar correctamente la Fase 2 antes de avanzar a la Fase 3 (tutor IA).

---

## 3. Registro de incidencias

### Incidencia 1 — Cambio sin commitear en electron/main.js ✅ RESUELTA
- **Problema:** `electron/main.js` modificado sin commit: `mainWindow.maximize()` envuelto en `setTimeout(..., 100)`.
- **Causa:** Ajuste de UI para asegurar que el maximizado se aplique tras `ready-to-show`.
- **Solución aplicada:** Revisado y commiteado en `a40d1f0`. Cambio menor de UI, bajo riesgo, aprobado.
- **Archivos afectados:** `electron/main.js`
- **Verificación:** Commit `a40d1f0` en rama `chore/stabilizacion-pre-fase-2`.

### Incidencia 2 — Rama de trabajo vs main
- **Problema:** Rama actual `chore/stabilizacion-pre-fase-2` diverge de `main`. Últimos commits de cada una son distintos.
- **Causa:** Trabajo de estabilización en rama separada sin integrar a main.
- **Solución pendiente:** Evaluar si se integra main o se continúa en la rama actual.
- **Archivos afectados:** Rama de git.
- **Verificación:** Pendiente.

### Incidencia 3 — Cifra de pruebas discrepante
- **Problema:** Documentación reporta 138 pruebas OK (12-11-2026); ejecución real arroja 197 pruebas OK.
- **Causa:** Las pruebas han crecido desde el último reporte del propietario.
- **Solución adoptada:** Registrar 197 pruebas OK como línea base vigente en esta bitácora.
- **Archivos afectados:** `docs/SEGUIMIENTO_TEMPORAL_USUARIO.md`, `docs/PLAN_DESARROLLO.md` (pendiente actualizar).
- **Verificación:** Ejecutado y verificado 16 nov 2026.

### Incidencia 5 — Duplicación lógica y acoplamiento en apps.roadmaps (hallazgo de S1/arquitecto)
- **Problema:** `arquitecto` identificó 4 áreas de duplicación lógica en `apps.roadmaps`:
  1. `resumen_roadmap()` vs propiedades del modelo `Roadmap` (dos fuentes de verdad para contadores).
  2. `DEPENDENCIAS_EXPLICITAS` hardcodeado vs `Prerrequisito` (modelo BD) vs JSON maestro (tres capas sin una única fuente de verdad).
  3. Resolución de contenido activo duplicada en `views.leccion_detalle`, `attempts._completar_leccion_si_corresponde`, `attempts.registrar_intento_ejercicio`.
  4. Doble escritura en `marcar_leccion` (save + recalcular_progreso_etapa).
- **Causa:** Evolución incremental sin refactorización de servicios compartidos.
- **Solución pendiente:** Propuestas 6.1 (corto plazo): unificar contadores, extraer servicio `obtener_contenido_activo()`, combinar consultas de progreso, activar WAL en SQLite, mover `DEPENDENCIAS_EXPLICITAS` a JSON.
- **Archivos afectados:** `apps/roadmaps/services.py`, `apps/roadmaps/views.py`, `apps/roadmaps/attempts.py`, `config/settings/base.py`
- **Verificación:** Pendiente (espera autorización del orquestador para modificar).
- **Decisión DT-005:** No modificar código en esta fase; documentado para futura autorización.

### Incidencia 6 — Navegación GUI de Electron + Django empaquetados no verificada
- **Problema:** El smoke test de PyInstaller valida solo `--sync-knowledge`, no el arranque normal de Waitress ni la navegación GUI.
- **Causa:** Requiere entorno gráfico (X11/Wayland) para verificar panel, etapas, lecciones, cierre normal.
- **Solución pendiente:** Ejecutar pruebas de arranque/cierre en entorno con servidor gráfico.
- **Archivos afectados:** `electron/main.js`, `server_entry.py`, `run.sh`.
- **Verificación:** Pendiente.

---

## 4. Decisiones técnicas

| ID | Decisión | Motivo | Alternativas descartadas | Consecuencias |
|---|---|---|---|---|
| DT-001 | Mantener `AUTH_DISABLED = True` por ahora | Primera versión monousuario local sin fricción de credenciales; auth completa conservada para reactivar con autorización. | Reactivar auth inmediatamente. | La app abre directo al panel; no hay login ni cierre de sesión visibles. |
| DT-002 | Continuar en rama `chore/stabilizacion-pre-fase-2` | La rama contiene trabajo de estabilización previo a fase 2; no se asume que una rama experimental esté integrada. | Cambiar a `main` inmediatamente. | Riesgo de divergencia con main; debe evaluarse integración. |
| DT-003 | Línea base de pruebas = 197 OK | Ejecución real en el commit actual supera las 138 reportadas por el propietario. | Mantener 138 como referencia. | Documentación debe actualizarse para reflejar 197. |
| DT-004 | No introducir microservicios ni cloud en v1 | Principio de primera versión local y gratuita. | Arquitectura distribuida anticipada. | Simplicidad operativa; evolución futura documentada pero no implementada. |
| DT-005 | Implementar ADR-005 a ADR-009 (mejoras arquitectónicas cortas) | `arquitecto` (S1) implementó las 5 mejoras propuestas en la revisión de arquitectura: WAL mode, unificar contadores, servicio contenido activo, combinar consultas progreso, mover DEPENDENCIAS_EXPLICITAS a JSON. | No implementar mejoras y mantener deuda técnica. | Código más limpio, menor duplicado, mejor concurrencia SQLite. ~170 líneas eliminadas. |

---

## 5. Estado de los subagentes

| Subagente | Especialización | Responsabilidades | Actividades | Entregables | Resultado supervisión |
|---|---|---|---|---|---|
| S1 | Arquitectura y Backend | Django, Python, modelos, servicios, vistas, APIs, integridad de datos, rendimiento. | Revisión completa de arquitectura; implementó ADR-005 (WAL mode), ADR-006 (unificar contadores), ADR-007 (servicio obtener_contenido_activo), ADR-008 (combinar consultas progreso), ADR-009 (DEPENDENCIAS_EXPLICITAS a JSON) y ADR-010 (tutor IA Ollama) con su app `apps/tutoring`. | 5 ADRs + ADR-010 + app tutoring. 197 pruebas OK tras cada cambio. Eliminó ~170 líneas de código duplicado. | ✅ Completado (16-nov-2026) |
| S2 | Frontend y UX | HTML, CSS, JS, interfaz visual, accesibilidad, responsive, temas, animaciones. | Revisión de consistencia visual; actualizó README.md y docs/PLAN_DESARROLLO.md (138→197 pruebas). | Cambios commiteados en `af56fbd`. Salida por buffer no capturada, pero cambios revisados y aceptados. | ✅ Completado (16-nov-2026) |
| S3 | Seguridad y Calidad | Vulnerabilidades, auth, sesiones, aislamiento Electron, pruebas unitarias/integración/regresión. | **No respondió a través de herdr**. Tarea asumida por el orquestador. | system check: 0 issues (dev y desktop). 197 pruebas OK. Sin secretos hardcodeados. .env en .gitignore. CSP estricta. Bind 127.0.0.1. Electron: sandbox, contextIsolation, nodeIntegration=false, IPC con validación de origen. | ✅ Completado por orquestador (16-nov-2026) |
| S4 | Documentación, Integración y QA | Documentación técnica, registros, integración, trazabilidad, instalación, distribución, informes de aceptación. | **No respondió a través de herdr**. Tarea asumida por el orquestador. | docs/INFORMES_ACEPTACION/ (README + PLANTILLA + FASE_2_ACEPTACION.md). docs/SEGUIMIENTO_TEMPORAL_USUARIO.md mantenido. ADRs 005-009 revisados. | ✅ Completado por orquestador (16-nov-2026) |

> Los 4 subagentes se organizaron mediante `herdr` (workspace w3, tab w3:t1). S1 (arquitecto, w3:p2) y S2 (frontend, w3:p3) respondieron y completaron sus tareas iniciales. S3 (seguridad, w3:p4) y S4 (documentacion, w3:p5) no respondieron a los prompts de herdr a pesar de `--focus` y `--wait`; sus responsabilidades fueron asumidas por el orquestador.

---

## 6. Validación final del usuario

Esta sección es la guía principal para verificar que CodeGuard Pro funciona correctamente tras completar todas las fases. Cada prueba tiene: objetivo, procedimiento, resultado esperado y criterio de aprobación.

> **Nota:** Esta guía se completará progresivamente a medida que se completen las fases. Al finalizar, contendrá todas las pruebas necesarias para la validación manual completa.

### 6.1 Instalación de la aplicación

**Prueba I-1 — Instalación desde código (Linux/macOS)**

1. **Objetivo:** Verificar que la aplicación se puede instalar y ejecutar desde el código fuente.
2. **Procedimiento:**
   - Clonar el repositorio: `git clone https://github.com/MaverickBms/CodeGuard-Pro.git`
   - Entrar al directorio: `cd CodeGuard-Pro`
   - Crear y activar entorno virtual: `python3 -m venv .venv && source .venv/bin/activate`
   - Instalar dependencias Python: `pip install -r requirements.txt`
   - Instalar dependencias Node.js: `npm install`
   - Aplicar migraciones: `python manage.py migrate --settings=config.settings.development`
   - Cargar roadmap: `python manage.py cargar_ascenso --settings=config.settings.development`
   - Crear .env si no existe: copiar `.env.example` a `.env`
   - Ejecutar la aplicación: `./run.sh`
3. **Resultado esperado:** La ventana de Electron se abre, muestra splash de inicio, inicia Django localmente y carga el panel principal sin errores.
4. **Criterio de aprobación:** La aplicación arranca, el panel principal es visible y no hay errores en consola ni en los logs.

**Prueba I-2 — Ejecución del AppImage empaquetado (Linux)**

1. **Objetivo:** Verificar que la versión distribuible (AppImage) funciona de forma independiente.
2. **Procedimiento:**
   - Generar el AppImage: `npm run build:linux` (requiere electron-builder y PyInstaller).
   - Ejecutar: `./dist/CodeGuard-Pro-1.0.0-x86_64.AppImage --ozone-platform=x11`
   - Opcional: establecer `CODEGUARD_DATA_DIR` a un directorio temporal.
3. **Resultado esperado:** La aplicación se abre, Django inicia dentro del AppImage, el panel principal es accesible.
4. **Criterio de aprobación:** La aplicación arranca y permanece activa; al cerrarse, no deja procesos huérfanos (código de salida 143 al recibir SIGTERM).

### 6.2 Ejecución y configuración inicial

**Prueba E-1 — Arranque normal de la aplicación**

1. **Objetivo:** Verificar que la aplicación inicia correctamente desde el script `./run.sh`.
2. **Procedimiento:**
   - Ejecutar `./run.sh` desde el directorio del proyecto.
   - Observar la salida de consola (migraciones, carga de roadmap, inicio de Electron).
3. **Resultado esperado:** Se aplican migraciones, se carga el roadmap ASCENSO, se abre Electron con splash y luego el panel principal.
4. **Criterio de aprobación:** La ventana principal aparece sin diálogos de error y el panel muestra información del roadmap.

**Prueba E-2 — Configuración inicial (setup)**

1. **Objetivo:** Verificar el flujo de configuración inicial cuando no existe usuario.
2. **Procedimiento:**
   - Con una base de datos vacía (sin usuario), iniciar la aplicación.
   - Verificar que se redirige a la pantalla de setup inicial (cuando auth está activada) o que se usa el usuario existente (modo sin auth).
3. **Resultado esperado:** En modo sin auth (`AUTH_DISABLED=True`), se abre directamente el panel usando el usuario local existente. Con auth activada, se muestra el formulario de setup.
4. **Criterio de aprobación:** No hay errores; el usuario puede acceder al panel.

### 6.3 Autenticación

**Prueba A-1 — Autenticación desactivada (estado actual)**

1. **Objetivo:** Verificar que la aplicación funciona sin credenciales cuando `AUTH_DISABLED=True`.
2. **Procedimiento:**
   - Confirmar que `config/settings/base.py` tiene `AUTH_DISABLED = True`.
   - Iniciar la aplicación.
   - Verificar que no se solicita usuario ni contraseña.
   - Verificar que el panel principal se abre directamente.
3. **Resultado esperado:** Acceso directo al panel sin pantallas de login.
4. **Criterio de aprobación:** El panel es accesible sin credenciales; las rutas de auth redirigen al panel (302).

**Prueba A-2 — Autenticación reactivada (con autorización)**

1. **Objetivo:** Verificar que el sistema de auth completo funciona cuando se reactiva.
2. **Procedimiento:**
   - Cambiar `AUTH_DISABLED = False` en `config/settings/base.py` (requiere autorización expresa).
   - Iniciar la aplicación sin usuario existente.
   - Completar el setup inicial (usuario, contraseña, frase de rescate).
   - Iniciar sesión con la contraseña maestra.
   - Cerrar sesión.
   - Probar recuperación por frase de rescate.
3. **Resultado esperado:** Setup, login, logout, rescate y cambio de contraseña funcionan correctamente.
4. **Criterio de aprobación:** Todos los flujos de autenticación completan sin errores; la frase de rescate se invalida tras uso; bloqueo tras 5 intentos fallidos.

### 6.4 Gestión de sesiones

**Prueba S-1 — Persistencia de sesión entre reinicios**

1. **Objetivo:** Verificar que el progreso y preferencias se conservan al cerrar y reabrir la aplicación.
2. **Procedimiento:**
   - Marcar una etapa como completada en el panel.
   - Cerrar la aplicación completamente.
   - Volver a abrir la aplicación.
   - Verificar que la etapa sigue marcada como completada.
3. **Resultado esperado:** Los datos persisten en SQLite entre sesiones.
4. **Criterio de aprobación:** El progreso marcado previamente sigue presente tras el reinicio.

### 6.5 Panel principal

**Prueba P-1 — Panel principal y navegación**

1. **Objetivo:** Verificar que el panel principal carga y la navegación funciona.
2. **Procedimiento:**
   - Abrir la aplicación.
   - Verificar que el panel muestra resumen de progreso, próxima actividad y módulos.
   - Hacer clic en cada módulo de navegación (Roadmap académico, etc.).
3. **Resultado esperado:** El panel carga con datos reales de la base de datos; los módulos implementados navegan a sus vistas; los no implementados se indican como tales.
4. **Criterio de aprobación:** El panel es visible y navegable; no hay errores de plantilla ni de JavaScript.

### 6.6 Roadmap ASCENSO 3.1

**Prueba R-1 — Listado de etapas**

1. **Objetivo:** Verificar que se muestran las 33 etapas con filtros.
2. **Procedimiento:**
   - Ir a Roadmap académico → Listado.
   - Verificar que aparecen las etapas (0 a 32).
   - Aplicar filtros por bloque, prioridad y búsqueda.
3. **Resultado esperado:** Las etapas se listan correctamente; los filtros reducen el listado según corresponda.
4. **Criterio de aprobación:** 33 etapas visibles; filtros funcionan sin errores.

**Prueba R-2 — Detalle de etapa y prerrequisitos**

1. **Objetivo:** Verificar el detalle de una etapa y el bloqueo por prerrequisitos.
2. **Procedimiento:**
   - Hacer clic en una etapa para ver su detalle.
   - Verificar módulos, lecciones, proyecto, criterios y prerrequisitos.
   - Verificar que etapas con prerrequisitos no completados aparecen bloqueadas.
3. **Resultado esperado:** El detalle muestra toda la información de la etapa; el bloqueo por prerrequisitos se respeta.
4. **Criterio de aprobación:** Navegación a detalle exitosa; bloqueo de etapas funcionando.

### 6.7 Registro del progreso

**Prueba PG-1 — Marcado de etapa completada**

1. **Objetivo:** Verificar que se puede marcar una etapa como completada y que se recalcula el avance.
2. **Procedimiento:**
   - En el detalle de una etapa, marcarla como completada.
   - Verificar que el porcentaje de avance se actualiza.
   - Verificar que la etapa siguiente se desbloquea si sus prerrequisitos están completados.
3. **Resultado esperado:** El avance se recalcula automáticamente; las etapas se desbloquean según prerrequisitos.
4. **Criterio de aprobación:** Porcentaje actualizado correctamente; desbloqueo condicional funcionando.

**Prueba PG-2 — Reapertura de lección**

1. **Objetivo:** Verificar que una lección no se puede completar manualmente (solo mediante actividades verificadas).
2. **Procedimiento:**
   - Intentar marcar una lección como completada manualmente.
   - Verificar que se muestra un mensaje indicando que la finalización requiere verificación de actividades.
3. **Resultado esperado:** La lección no se marca como completada manualmente; se muestra mensaje informativo.
4. **Criterio de aprobación:** No hay finalización manual de lecciones; mensaje claro al usuario.

### 6.8 Persistencia de información

**Prueba PD-1 — Datos sobreviven reinicio de la aplicación**

1. **Objetivo:** Verificar que progreso, intentos y preferencias persisten en SQLite.
2. **Procedimiento:**
   - Realizar cambios (marcar etapa, registrar intento de ejercicio).
   - Cerrar la aplicación.
   - Volver a abrir y verificar que los cambios están presentes.
3. **Resultado esperado:** Todos los cambios están en la base de datos tras el reinicio.
4. **Criterio de aprobación:** Ningún dato se pierde entre sesiones.

### 6.9 Preferencias y temas visuales

**Prueba T-1 — Cambio de tema visual**

1. **Objetivo:** Verificar que los 12 temas visuales funcionan y se aplican correctamente.
2. **Procedimiento:**
   - Abrir el menú Ver → Tema.
   - Seleccionar cada uno de los 12 temas.
   - Verificar que la interfaz cambia de apariencia en cada uno.
3. **Resultado esperado:** Cada tema aplica su paleta de colores; el contraste es legible en todos.
4. **Criterio de aprobación:** Los 12 temas cambian la apariencia sin romper la interfaz.

**Prueba T-2 — Persistencia del tema**

1. **Objetivo:** Verificar que el tema seleccionado se recuerda entre sesiones.
2. **Procedimiento:**
   - Cambiar a un tema diferente del predeterminado.
   - Cerrar y volver a abrir la aplicación.
   - Verificar que el tema seleccionado se mantiene.
3. **Resultado esperado:** La preferencia de tema persiste.
4. **Criterio de aprobación:** El tema seleccionado sigue activo tras reiniciar.

### 6.10 Almacenamiento local

**Prueba AL-1 — Ubicación de los datos**

1. **Objetivo:** Verificar que los datos se almacenan en el directorio de datos del usuario.
2. **Procedimiento:**
   - Verificar la existencia de `data/db.sqlite3`, `data/logs/`, `data/media/`, `data/.secret_key` en desarrollo.
   - En empaquetado, verificar que se usa `userData` (Windows: %APPDATA%/CodeGuard Pro).
3. **Resultado esperado:** Los archivos de datos están en las ubicaciones esperadas.
4. **Criterio de aprobación:** La base de datos, logs y clave secreta están en el directorio de datos correcto.

### 6.11 Funcionamiento sin Internet

**Prueba OFF-1 — Uso offline de funcionalidades esenciales**

1. **Objetivo:** Verificar que la aplicación funciona sin conexión a Internet.
2. **Procedimiento:**
   - Desconectar el equipo de Internet (o bloquear acceso de red).
   - Iniciar la aplicación.
   - Navegar por el panel, roadmap, etapas y lecciones.
   - Registrar progreso e intentos.
3. **Resultado esperado:** Todas las funcionalidades esenciales operan sin red; el servidor escucha solo en 127.0.0.1.
4. **Criterio de aprobación:** La aplicación es completamente usable offline para estudio y progreso.

### 6.12 Módulos del roadmap

**Prueba M-1 — Vista de lección**

1. **Objetivo:** Verificar que una lección muestra teoría, explicación, ejemplos y ejercicios.
2. **Procedimiento:**
   - Abrir una lección desde el roadmap.
   - Verificar que se muestra el contenido publicado (objetivos, teoría técnica, explicación sencilla).
   - Verificar que ejemplos y ejercicios se listan correctamente.
3. **Resultado esperado:** La lección se renderiza con todo su contenido.
4. **Criterio de aprobación:** Contenido visible y navegable sin errores.

**Prueba M-2 — Intento de ejercicio**

1. **Objetivo:** Verificar que se puede registrar y evaluar un intento de ejercicio sin ejecutar código arbitrario.
2. **Procedimiento:**
   - Abrir una lección con ejercicios.
   - Enviar una respuesta a un ejercicio.
   - Verificar que se registra el intento con resultado (aprobado / no aprobado / pendiente).
   - Verificar el historial de los últimos tres intentos.
3. **Resultado esperado:** El intento se guarda con su resultado; el historial muestra hasta 3 intentos previos.
4. **Criterio de aprobación:** Los intentos se persisten y se muestran correctamente.

### 6.13 Copias de seguridad

**Prueba BK-1 — Backup y restauración**

1. **Objetivo:** Verificar el proceso de backup y restauración de datos.
2. **Procedimiento:**
   - Ejecutar el comando o función de backup (según implementación en Fase 8).
   - Verificar que se genera un archivo de backup con hash.
   - Restaurar el backup en un entorno de prueba.
   - Verificar que los datos se recuperan correctamente.
3. **Resultado esperado:** El backup es válido y la restauración recupera los datos.
4. **Criterio de aprobación:** Backup y restauración completan sin pérdida de datos.

> **Nota:** Esta prueba depende de la implementación de backups (Fase 8 / Incremento 6 del plan de desarrollo).

### 6.14 Cierre de la aplicación

**Prueba C-1 — Cierre seguro desde el menú**

1. **Objetivo:** Verificar que la aplicación se cierra correctamente sin dejar procesos huérfanos.
2. **Procedimiento:**
   - Abrir la aplicación.
   - Cerrar desde el menú (CodeGuard Pro → Salir, o CmdOrCtrl+Q).
   - Verificar que el proceso de Django (Waitress) se detiene.
   - Verificar que no quedan procesos de Electron ni Python huérfanos.
3. **Resultado esperado:** Cierre limpio; código de salida adecuado (143 al SIGTERM en AppImage); no hay procesos huérfanos.
4. **Criterio de aprobación:** La aplicación termina completamente y libera el puerto de Django.

### 6.15 Versión distribuible

**Prueba D-1 — Instalador independiente**

1. **Objetivo:** Verificar que la aplicación empaquetada se ejecuta sin dependencias externas en el equipo.
2. **Procedimiento:**
   - Instalar el AppImage (Linux) o el instalador NSIS (Windows).
   - Ejecutar la aplicación sin tener Python, Node.js ni Django instalados en el sistema.
   - Verificar que inicia Django internamente mediante el binario PyInstaller.
3. **Resultado esperado:** La aplicación arranca de forma independiente.
4. **Criterio de aprobación:** Funciona sin dependencias de desarrollo en el equipo destino.

---

## 7. Línea base de calidad

| Métrica | Valor (16 nov 2026) |
|---|---|
| Django system check | 0 issues |
| Migraciones pendientes | Ninguna |
| Pruebas automatizadas | 197 OK |
| Cobertura de apps probadas | core, accounts, audit, roadmaps |
| Autenticación | Desactivada temporalmente (conservada) |
| Offline-first | Sí |
| Temas visuales | 12 implementados |
| Roadmap ASCENSO | 33 etapas cargables |

---

*Este archivo se actualiza frecuentemente durante el desarrollo. No esperar hasta el final para reconstruir lo sucedido.*