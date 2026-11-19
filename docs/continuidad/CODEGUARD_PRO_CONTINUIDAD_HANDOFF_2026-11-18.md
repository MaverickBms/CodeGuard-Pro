# CODEGUARD PRO — REGISTRO DE CONTINUIDAD Y HANDOFF

**Fecha de revisión:** 18 de noviembre de 2026 (hora local de Colombia)  
**Repositorio:** https://github.com/MaverickBms/CodeGuard-Pro  
**Rama principal:** `main`  
**Commit remoto observado:** `59d08848726550fde442be1eb1e1be5522637f0b`  
**Estado de esta revisión:** auditoría remota/documental; no se modificó el repositorio ni se ejecutaron pruebas locales.

> Este documento está diseñado para que otro desarrollador o agente de IA pueda continuar el proyecto sin depender del historial de conversaciones. Antes de actuar, debe comprobar que el commit y las ramas siguen siendo los mismos.

---

## 1. Instrucción prioritaria para el siguiente agente

Continúa CodeGuard Pro como una tarea de finalización de producto. No reconstruyas el proyecto, no cambies su propósito y no sustituyas componentes funcionales por versiones simplificadas.

**Primera tarea:** inspeccionar el estado local real del repositorio y validar la integración de escritorio en un perfil de datos temporal aislado. Después, ejecutar las pruebas automatizadas del HEAD local y validar el flujo educativo principal.

No declares la beta terminada sin evidencia reproducible de:
- arranque normal de la aplicación empaquetada;
- inicialización limpia y segura del perfil;
- navegación y operación del flujo educativo;
- persistencia tras reinicio;
- funcionamiento sin Internet en los flujos esenciales;
- cierre normal sin procesos huérfanos;
- documentación y limitaciones actualizadas.

### Restricciones permanentes

- No ejecutar `git reset --hard`, `git clean -fd`, `git checkout -- .` ni `git restore` indiscriminadamente.
- No borrar, sustituir ni migrar la base de datos real del usuario durante pruebas.
- Usar perfiles temporales aislados para pruebas de instalación limpia.
- No ejecutar `cargar_ascenso --recrear` en el perfil real.
- No ejecutar código arbitrario del estudiante en el proceso Django.
- No desactivar pruebas, validaciones o controles para conseguir un resultado verde.
- No introducir dependencias sin justificación.
- No reactivar autenticación sin evaluar y documentar el impacto; la desactivación actual es una decisión temporal conocida.
- No configurar hosting, endpoints de producción, claves públicas de distribución ni publicación remota sin autorización específica.
- No realizar commits, pushes, merges, tags, releases ni despliegues sin autorización expresa.
- Antes de cambiar archivos, revisar `git status`, rama, HEAD y diff. Proteger cualquier trabajo local preexistente.

El usuario ha autorizado continuar autónomamente y tomar decisiones técnicas ordinarias con prudencia. Esa autorización no revoca las restricciones anteriores sobre Git, datos, seguridad ni despliegues.

---

## 2. Identidad y propósito del producto

CodeGuard Pro es una plataforma educativa personal, monousuario, local y offline-first para organizar el aprendizaje técnico mediante rutas formativas, documentación trazable, evaluaciones, laboratorios y evidencias.

No es solamente un catálogo de cursos. El flujo de valor esperado es:
1. organizar el aprendizaje mediante el roadmap ASCENSO;
2. consultar lecciones y material técnico;
3. resolver ejercicios y talleres;
4. realizar evaluaciones;
5. registrar intentos, evidencias y progreso;
6. recibir tutoría local opcional;
7. usar gamificación como incentivo, sin sustituir la evidencia académica.

La aplicación debe seguir siendo utilizable sin Internet para estudiar con el contenido local disponible y consultar el progreso almacenado.

---

## 3. Arquitectura vigente observada en el código

La arquitectura activa es:

- **Escritorio:** Electron.
- **Backend local:** Django 5.2, servido mediante Waitress.
- **Persistencia:** SQLite.
- **Servidor empaquetado:** PyInstaller (`CodeGuardServer`).
- **Frontend:** templates HTML, CSS, JavaScript y recursos locales; Bootstrap/HTMX/SweetAlert2/FontAwesome según README.
- **Servidor estático:** WhiteNoise.
- **Tutor IA:** Ollama local opcional con fallback determinista/estático.
- **Integridad de paquetes:** SHA-256 y firmas Ed25519.
- **Distribución:** cliente HTTPS pull-only y paquetes de conocimiento versionados; distribución remota de producción aún no configurada.

Electron inicia Django localmente, espera el endpoint `/healthz/` y abre la interfaz cuando el servicio está listo. El servidor debe escuchar exclusivamente en `127.0.0.1`.

**No reconstruir con PySide6, React, Vue ni microservicios.** La descripción pública del repositorio todavía menciona PySide6 en sus metadatos, pero la arquitectura del código activo es Electron + Django. La documentación Windows actual indica expresamente que PySide6/`desktop/main.py` pertenece a una arquitectura anterior.

### Módulos Django observados

| Aplicación | Función |
|---|---|
| `apps.core` | Panel, vistas base y health check |
| `apps.accounts` | Identidad, autenticación y modo temporal sin autenticación |
| `apps.audit` | Auditoría y trazabilidad |
| `apps.roadmaps` | ASCENSO, contenido, lecciones, ejercicios, intentos, evaluaciones, importación y sincronización |
| `apps.tutoring` | Sesiones, análisis y pistas del tutor |
| `apps.gamification` | Monedas, transacciones, logros, misiones, rachas y mundo/avatar |
| `apps.challenges` | Desafíos y evidencias |

---

## 4. Estado remoto comprobado en esta revisión

### Ramas

La API pública de GitHub devolvió estas ramas:

| Rama | SHA observado | Interpretación |
|---|---|---|
| `main` | `59d08848726550fde442be1eb1e1be5522637f0b` | Línea principal actual |
| `documentation` | `11cefff675d502aca24fb4d93668ce77f8c6fd79` | Línea documental histórica, atrasada |
| `test/phase-2-electron-integration` | `98fb56f68de9557445baebc26b14355092e8362a` | Evidencia histórica de integración |

`main` contiene dos commits recientes relevantes:
- `c05b321feddb17fe0be8f1a53daa25f820f033c0`: integra el trabajo de `fix/p0-first-run-initialization`, reorganiza documentación y ajusta empaquetado/permisos.
- `59d08848726550fde442be1eb1e1be5522637f0b`: restaura README, README_WINDOWS y CONTRIBUTING en `main`, con enlaces a la documentación extendida en la rama `documentation`.

La rama `documentation` está **125 commits por detrás** de `main` según la comparación consultada. No hacer merge completo de esa rama hacia `main` sin analizar el historial y los diffs: puede reintroducir código anterior. Mantener `main` como línea de desarrollo. Recuperar o sincronizar documentos de forma selectiva, preservando decisiones y evidencias.

### Estado de CI

La consulta a GitHub Actions devolvió cero ejecuciones/workflows en la colección consultada. No hay evidencia de CI activa que certifique el HEAD actual. No asumir que GitHub Actions ha ejecutado la suite.

### Archivos de referencia inspeccionados

En `main`:
- `README.md`
- `README_WINDOWS.md`
- `package.json`
- `requirements.txt`
- `server_entry.py`
- `config/health.py`
- `electron/main.js`
- `run.sh`
- `build_windows.bat`
- `apps/roadmaps/management/commands/cargar_ascenso.py`
- `apps/roadmaps/tests/test_server_entry.py`
- `apps/core/tests/test_health.py`

En `documentation`:
- `PROJECT_CONTROL.md`
- `docs/README.md`
- `docs/PLAN_MAESTRO_CODEGUARD.md`
- `docs/INFORME_QA_INTEGRAL_2026-11-16.md`
- `docs/IMPLEMENTACION_CORRECCIONES_P0.md`
- `docs/VALIDACION_INTEGRACION_ELECTRON.md`

---

## 5. Fases y estado funcional

Estado documental que debe confirmarse contra código y ejecución:

| Fase | Estado | Qué falta |
|---|---|---|
| 1. UX/UI base | Completada según línea base | Regresión visual final de temas, tamaños y GUI empaquetada |
| 2. Motor de aprendizaje | Parcial/en progreso | Contenido académico completo y revisado, validación de todos los tipos de lección, práctica segura y E2E |
| 3. Tutor IA local | Parcial | Ollama real, latencia, detección de modelo, privacidad y fallback |
| 4. Evaluaciones | Parcial | Flujo de corrección, homologación/progresión y UI completa |
| 5. Gamificación | Base integrada | Reglas, recompensas y coherencia con logros académicos |
| 6. Mundo/avatar | Base integrada | Personalización y experiencia completa |
| 7. Desafíos | Base técnica | Catálogo e interacción completa |
| 8. Calidad e integración | En progreso | Instalación limpia, GUI, offline E2E, backup/restore y aceptación de plataforma |

No asumir que todas las lecciones del roadmap tienen contenido sustantivo. La cantidad de registros curriculares no demuestra que cada lección esté redactada, revisada y pedagógicamente completa.

### Decisión de MVP

Para la beta, priorizar:
1. arranque y persistencia;
2. dashboard;
3. roadmap ASCENSO;
4. apertura de lección y contenido local;
5. ejercicio y envío;
6. evaluación determinista disponible;
7. registro de resultado y progreso;
8. reinicio y persistencia;
9. tutor opcional/fallback si no compromete el núcleo;
10. interfaz estable y recorrido de demostración.

No intentar terminar todas las características futuras de fases 3–7 antes de cerrar el flujo educativo central.

---

## 6. Hallazgos técnicos y riesgos

### P0 — Primer arranque del perfil empaquetado

La inspección del `main` actual muestra que `server_entry.py`:
- establece `config.settings.desktop`;
- ejecuta `django.setup()`;
- para el modo servidor, ejecuta `migrate`;
- ejecuta `cargar_ascenso` sin `--recrear`;
- después carga WSGI y Waitress;
- para `--sync-knowledge`, despacha el comando de sincronización sin iniciar Waitress ni migraciones.

`electron/main.js`:
- selecciona `app.getPath('userData')` para la aplicación empaquetada;
- inicia `CodeGuardServer`;
- espera `/healthz/`;
- comprueba HTTP 200 y estado saludable de DB, migraciones y roadmap.

Hay pruebas unitarias de despacho del modo sync, inicialización idempotente y health check. **Esto acredita el diseño y las rutas unitarias, no la aceptación real del AppImage/GUI.**

Prueba obligatoria: perfil temporal nuevo, arranque real del artefacto, verificación de base, migraciones y ASCENSO; cierre; segundo arranque; comprobar que no se pierde progreso.

### P1 — Aceptación de escritorio

No hay evidencia suficiente de aceptación E2E de:
- Waitress en modo servidor normal;
- GUI Electron cargada;
- navegación a ASCENSO y lecciones;
- puerto dinámico ligado solo a loopback;
- cierre normal desde el menú;
- liberación de procesos hijos;
- persistencia tras reinicio.

Un smoke test de `--sync-knowledge` no demuestra el funcionamiento normal de la aplicación.

### P1 — Suite de pruebas sin línea base reproducible

README documenta 245 pruebas OK en siete aplicaciones el 16-11-2026. El subconjunto de cuatro apps aparece con 197 pruebas y una línea histórica de 138. Estos resultados son históricos/reportados, no una ejecución independiente sobre el HEAD `59d0884`.

Ejecutar de nuevo el conjunto completo en el checkout local, registrar comando, entorno, salida final, fecha y SHA. No escribir “245 OK” si no se reprodujo.

### P1 — Tutor y privacidad

Ollama no se distribuye necesariamente con la aplicación ni con los pesos del modelo. La tutoría generativa requiere instalación y descarga del modelo. El núcleo educativo debe funcionar sin Ollama.

Verificar que la URL del tutor esté limitada a loopback en modo privado, que no se sigan redirecciones a hosts remotos y que no se filtren datos del estudiante. No enviar código/consultas a servicios remotos por configuración accidental.

### P0 — Ejecución arbitraria de código

Permanece prohibida hasta que exista sandbox independiente y auditado con límites de CPU, memoria, tiempo, filesystem, procesos y red, y pruebas de escape. Mantener evaluadores deterministas como fuente de verdad.

### P1 — Backup y restauración

La estrategia de backup/restore sigue sin aceptación. Debe cubrir una copia consistente de SQLite (incluyendo WAL según corresponda), clave secreta, media y metadatos de paquetes/versiones. Probar restauración en perfil aislado. No implementar una copia improvisada que pueda producir una base inconsistente.

### P2 — Documentación heredada y metadatos

- La descripción del repositorio GitHub menciona PySide6; el código activo utiliza Electron.
- La documentación extensa está en `documentation`, pero esa rama está atrasada 125 commits.
- La documentación QA contiene hallazgos originales que luego se corrigieron; se deben marcar como corregidos en main, sin borrar el historial del hallazgo.
- `README_WINDOWS.md` actual indica Electron y señala que PySide6/`desktop/main.py` es legado.
- Mantener el estado “reportado”, “probado”, “verificado manualmente” y “aceptado” separado.

### P2 — Plataformas

Configuración observada:
- Linux x64: AppImage.
- Windows x64: NSIS y portable mediante `build_windows.bat`.
- macOS y ARM64 no deben anunciarse como soportados sin build y aceptación nativos.

---

## 7. Comandos de validación

Ejecutar desde la raíz del repositorio y con el entorno virtual del proyecto. Antes, revisar `git status` y no tocar la base de datos real.

### Inspección inicial

```bash
git status --short --branch
git rev-parse HEAD
git branch --show-current
git log -5 --oneline --decorate
git diff --check
```

### Validación Django y dependencias

```bash
./.venv/bin/python manage.py check \
  --settings=config.settings.development

./.venv/bin/python manage.py makemigrations --check --dry-run \
  --settings=config.settings.development

./.venv/bin/python -m pip check
```

### Suite completa conocida

```bash
./.venv/bin/python manage.py test \
  apps.core apps.accounts apps.audit apps.roadmaps \
  apps.tutoring apps.gamification apps.challenges \
  --settings=config.settings.development
```

Registrar el total real, no asumir 245.

### Validación JavaScript

```bash
node --check electron/main.js
node --check electron/preload.js
```

### Build Linux

Seguir el pipeline documentado:
```bash
npm run build:linux
```

Este comando debe generar el servidor PyInstaller, verificar manifiesto/hash y solo entonces ejecutar electron-builder. No invocar `electron-builder` directamente para producir artefactos distribuibles.

### Prueba de primer arranque

Preparar un directorio temporal aislado, exportar `CODEGUARD_DATA_DIR` a ese directorio y ejecutar el artefacto empaquetado. No apuntar a `~/.../data` real.

Comprobar:
- DB y migraciones;
- roadmap activo y 33 etapas;
- `/healthz/` saludable;
- GUI visible;
- navegación y flujo educativo;
- reinicio y conservación de progreso;
- ausencia de Internet en flujo local;
- cierre normal y procesos/puertos liberados.

No usar ni eliminar el perfil temporal anterior sin comprobar primero su ruta y contenido.

---

## 8. Documentación que debe quedar sincronizada

La documentación técnica extensa vive en la rama `documentation` y contiene:
- `PROJECT_CONTROL.md`
- `docs/PLAN_MAESTRO_CODEGUARD.md`
- `docs/PLAN_PRUEBAS.md`
- `docs/ARQUITECTURA.md`
- `docs/INFORME_QA_INTEGRAL_2026-11-16.md`
- `docs/IMPLEMENTACION_CORRECCIONES_P0.md`
- `docs/VALIDACION_INTEGRACION_ELECTRON.md`
- `docs/INSTALACION.md`
- `docs/MANUAL_USUARIO.md`
- `docs/SEGURIDAD.md`
- `docs/BACKUPS_Y_RESTAURACION.md`
- `docs/MATRIZ_TRAZABILIDAD.md`
- `docs/FASE_2_APRENDIZAJE.md`
- `docs/DECISIONES_PENDIENTES.md`
- `docs/CHANGELOG.md`
- `docs/INFORMES_ACEPTACION/`

### Estrategia documental segura

No fusionar `documentation` completa sobre `main`. Primero:
1. actualizar el checkout local de `main` y verificar su HEAD;
2. preservar un respaldo local de la documentación histórica;
3. comparar archivos documentales individualmente;
4. identificar qué cambios de `main` deben reflejarse en la documentación;
5. actualizar documentos de forma selectiva en una rama de trabajo local;
6. revisar los diffs y referencias cruzadas;
7. no commit/push/merge sin autorización.

### Documento de liberación beta que falta

Crear `docs/RELEASE_BETA_1.0.0.md` cuando existan evidencias reales. Debe incluir:
- alcance exacto de la beta;
- módulos incluidos;
- requisitos e instalación;
- matriz de pruebas;
- plataformas probadas;
- limitaciones conocidas;
- recorrido de demostración;
- funcionalidades planificadas;
- commit y artefacto exactos aceptados.

No fechar ni declarar aceptación antes de ejecutar las pruebas.

---

## 9. Orden de trabajo recomendado

### Bloque A — Instalación y arranque
1. inspección del entorno local;
2. perfil temporal nuevo;
3. ejecutar artefacto real;
4. revisar health check y procesos;
5. probar segundo arranque;
6. corregir defectos reproducibles.

### Bloque B — Flujo educativo
1. dashboard;
2. ASCENSO;
3. lección;
4. ejercicio;
5. evaluación;
6. persistencia del resultado;
7. progreso actualizado.

### Bloque C — Tutor, gamificación y desafíos
Validar lo que ya está integrado; no construir módulos secundarios desde cero para la presentación.

### Bloque D — Calidad
Suite completa, checks, regresiones, offline, privacidad, cierre y recuperación.

### Bloque E — Documentación y demo
Actualizar control del proyecto, plan maestro, QA, instalación, manual, pruebas y acta beta. Preparar un recorrido reproducible.

---

## 10. Recorrido de demostración sugerido

La demo debe usar datos reales del perfil de prueba y operaciones reales:
1. explicar propósito y problema que resuelve;
2. abrir el dashboard;
3. mostrar ASCENSO y una etapa;
4. abrir una lección con contenido local;
5. resolver un ejercicio;
6. mostrar la evaluación/resultado real;
7. mostrar progreso persistido;
8. reiniciar la aplicación y confirmar persistencia;
9. explicar tutor opcional y fallback;
10. explicar qué queda planificado para futuras versiones.

No mostrar pantallas vacías ni datos inventados. Si una funcionalidad no está verificada, no incluirla como demostración funcional.

---

## 11. Estado de esta intervención

- Revisión remota de ramas, commits, árbol de archivos y documentación: realizada.
- Inspección estática de `server_entry.py`, health check, Electron, scripts de build y pruebas específicas: realizada.
- Cambios en repositorio: ninguno.
- Pruebas locales ejecutadas: ninguna.
- Build ejecutado: ninguno.
- Instalación GUI aceptada: no.
- Commit/push/merge/tag/release/deploy: ninguno.
- Riesgo documental prioritario: rama `documentation` atrasada 125 commits respecto a `main`.

### Próxima acción obligatoria

Continuar en el entorno local del propietario con el Bloque A. Si el agente no tiene acceso al filesystem/terminal local, debe indicarlo claramente y solicitar al propietario ejecutar los comandos de inspección/validación o delegarlos al agente local (openCode). No debe afirmar que ejecutó pruebas o modificó el proyecto si no tuvo acceso real.

---

## 12. Instrucción de continuidad para una nueva IA

Lee este documento completo y después consulta el repositorio oficial. Comprueba la rama y el SHA actuales; este handoff es una fotografía del 18-11-2026, no una garantía de que GitHub siga igual.

Lee primero `PROJECT_CONTROL.md`, `docs/PLAN_MAESTRO_CODEGUARD.md`, `docs/ARQUITECTURA.md`, `docs/PLAN_PRUEBAS.md` y los informes QA/aceptación disponibles en la rama documental. Compara esos documentos con el código actual de `main`, especialmente el commit `59d0884`.

No empieces rediseñando ni reconstruyendo. Ejecuta primero la inspección local y el Bloque A en un perfil temporal. Registra cada decisión, archivo modificado, prueba ejecutada y resultado. Actualiza este handoff y los documentos rectores después de cada bloque. Mantén las restricciones de protección del proyecto y no realices operaciones Git de publicación sin autorización.

**Objetivo:** una beta pequeña pero real, estable, reproducible, offline-first y demostrable. La prioridad es el flujo educativo esencial, no completar todas las funciones futuras.