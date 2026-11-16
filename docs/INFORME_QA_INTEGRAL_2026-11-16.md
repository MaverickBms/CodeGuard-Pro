# Informe QA integral — CodeGuard Pro

**Fecha de auditoría:** 16-11-2026  
**Repositorio:** `MaverickBms/CodeGuard-Pro`  
**Rama auditada:** `main`  
**HEAD auditado:** `26085c66ae4afd01b174b461b76d3de19d211b50`  
**Método:** inspección estática del repositorio, comparación de ramas, revisión de configuración, scripts de empaquetado, arquitectura, documentación, servicios y pruebas declaradas.  
**Limitación:** no se ejecutaron Django, pytest, Electron, PyInstaller ni la GUI en esta auditoría. Los resultados de pruebas y compilación se identifican como reportados por el propietario/documentados, no como ejecuciones independientes de esta revisión.

---

## 1. Dictamen ejecutivo

CodeGuard Pro ha evolucionado de un núcleo de escritorio con roadmap a una plataforma educativa local con siete aplicaciones Django, sistema de contenido versionado, tutoría local, evaluaciones, gamificación y componentes de desafíos.

La dirección del producto es coherente con el objetivo **offline-first, monousuario y sin infraestructura externa obligatoria**. SQLite conserva el estado académico local; Electron aloja la interfaz; Django/Waitress sirve la aplicación en loopback; Ollama puede proporcionar tutoría local y existe una degradación a pistas estáticas cuando no está disponible.

**Estado global: IMPLEMENTADO PARCIALMENTE — NO LISTO PARA DISTRIBUCIÓN GENERAL.**

Los bloqueos más importantes antes de considerar una versión instalable fiable son:
1. Corregir y probar la inicialización de la base de datos y del roadmap en una instalación limpia, especialmente Windows y el lanzador `codeguard`.
2. Reproducir la suite completa y fijar una única línea base de pruebas.
3. Validar la aplicación empaquetada en GUI, el funcionamiento sin Internet, persistencia, cierre normal y ausencia de procesos huérfanos.
4. Completar el plan de distribución por sistema operativo y arquitectura de CPU.
5. Cerrar los criterios funcionales de Fases 2–8; varias fases tienen bases técnicas, no productos terminados.

## 2. Estado del repositorio y ramas

### 2.1 Integración en main

Antes de esta auditoría, `main` estaba en `e4172789b00319ada35916e13ea390868e08c88d`. La rama `chore/stabilizacion-pre-fase-2` estaba **75 commits por delante y 0 por detrás**. Se realizó un avance directo de `main` a:

`26085c66ae4afd01b174b461b76d3de19d211b50`

No se reescribió historial. La rama de estabilización y `main` quedan en la misma línea de desarrollo.

### 2.2 Ramas restantes observadas

| Rama | Situación respecto a main | Recomendación |
|---|---:|---|
| `chore/stabilizacion-pre-fase-2` | Integrada; misma línea de commits | Conservar temporalmente como referencia y eliminar solo después de confirmar clones y respaldos |
| `docs/phase-2-hybrid-knowledge-sync` | 246 commits detrás, sin commits exclusivos | Rama histórica; no fusionar |
| `feat/phase-2-http-sync-client` | 31 commits detrás, sin commits exclusivos | Rama histórica; no fusionar |
| `fix/phase-2-integrity-learning` | 96 commits detrás, sin commits exclusivos | Rama histórica; no fusionar |
| `test/phase-2-electron-integration` | Divergida: 4 commits exclusivos y 10 detrás | Revisar sus cuatro commits antes de decidir cherry-pick o archivo |

**Política recomendada:** `main` como única línea integrada y estable. Para trabajo futuro, usar ramas cortas solo si se necesita aislamiento, integrarlas mediante PR o fast-forward después de pruebas y no mantener ramas permanentes por fase. No borrar ramas divergidas sin inspeccionar los commits exclusivos.

## 3. Inventario funcional

### 3.1 Núcleo y escritorio

- Django 5.2.x con arquitectura MVT y separación por aplicaciones.
- Electron como contenedor de escritorio.
- Servidor local Waitress y WhiteNoise.
- SQLite como almacenamiento local; configuración WAL presente.
- Recursos estáticos locales; Bootstrap, HTMX y bibliotecas frontend empaquetadas.
- Configuración separada para desarrollo y escritorio.
- PyInstaller para empaquetar el servidor Django.
- Directorio de datos externo al paquete: base SQLite, logs, media y clave secreta.
- Servidor previsto para escuchar exclusivamente en `127.0.0.1`.

### 3.2 Aplicaciones Django

| Aplicación | Responsabilidad | Estado observado |
|---|---|---|
| `apps.core` | Panel, navegación y configuración del sistema | Base funcional |
| `apps.accounts` | Identidad local y autenticación conservada | El modo sin autenticación está activo temporalmente |
| `apps.audit` | Registro de eventos y trazabilidad | Implementado |
| `apps.roadmaps` | ASCENSO, lecciones, ejercicios, intentos, contenido versionado, distribución y evaluaciones | Módulo más desarrollado; Fase 2 sigue abierta |
| `apps.tutoring` | Tutor local Ollama, sesiones, pistas y análisis | Implementación inicial; validación real de Ollama pendiente |
| `apps.gamification` | Perfil, moneda, transacciones, logros, misiones, rachas y elementos de mundo/avatar | Base implementada; expansión pendiente |
| `apps.challenges` | Desafíos, minijuegos y evidencia de resultados | Base técnica; catálogo y experiencia interactiva pendientes |

### 3.3 Roadmap y aprendizaje

- ASCENSO 3.1: 33 etapas.
- La documentación histórica del proyecto informa 212 módulos y 1.946 lecciones; los conteos deben volver a verificarse desde una base limpia tras aplicar migraciones y cargar el JSON vigente.
- Contenido de lecciones, ejemplos, ejercicios, prerrequisitos y registro de intentos.
- UUID estables para recursos académicos.
- Snapshots de contenido, fuentes, atribución, licencia y flujo editorial.
- Registro de paquetes de conocimiento, manifiestos, hash SHA-256 y firmas Ed25519.
- Instalación transaccional y rollback de paquetes.
- Cliente HTTP pull-only, ETag, backoff y scheduler Electron implementados; distribución remota de producción no configurada.
- Evaluaciones con modelos de quiz, pregunta, resultados y criterios de cumplimiento.

**Pendiente:** comprobar que el contenido académico publicado es sustantivo, vigente, trazable y pedagógicamente suficiente. Tener 1.946 registros curriculares no demuestra que las 1.946 lecciones estén redactadas, revisadas y completas.

## 4. Estado por fases

| Fase | Estado QA | Falta para cerrar |
|---|---|---|
| 1. UX/UI y experiencia base | Base declarada completada | Regresión visual real en resoluciones, accesibilidad y 12 temas tras los últimos cambios |
| 2. Motor de aprendizaje | En progreso | Contenido editorial real, editor/experiencia de práctica, evaluación segura, navegación completa, importación manual integral y aceptación offline |
| 3. Tutor IA local | Implementación parcial | Probar Ollama real, modelos instalados, recursos, timeouts, fallback, privacidad y rendimiento en hardware modesto |
| 4. Evaluaciones y progresión | Implementación parcial | Corrección, reglas de homologación/progresión, UI completa, autoría y trazabilidad del evaluador |
| 5. Gamificación | Base implementada | Validar reglas, idempotencia, consistencia del saldo, recompensas y que nunca otorgue aprobación académica |
| 6. Mundo/avatar/personajes | Base implementada | Completar experiencia visual, personalización, desbloqueos y persistencia |
| 7. Minijuegos/desafíos | Base técnica implementada | Catálogo, interfaz interactiva, dificultad adaptativa y conexión con competencias |
| 8. Integración, calidad y optimización | En progreso | Instalación limpia, matriz de plataformas, offline E2E, backup/restore, GUI, rendimiento y seguridad integral |

## 5. Hallazgos QA priorizados

### QA-01 — Inicialización inconsistente del directorio de datos
**Prioridad: P0 / bloqueante para instalación limpia.**

El lanzador `codeguard` calcula `DATA_DIR="$HOME/.config/Code Guard Pro/data"`, pero no exporta `CODEGUARD_DATA_DIR` antes de ejecutar `manage.py migrate` y `manage.py cargar_ascenso`. La variable solo se pasa al proceso AppImage posterior. La configuración Django usa `CODEGUARD_DATA_DIR` o, si falta, `BASE_DIR/data`. Por tanto, el lanzador puede inicializar una base distinta de la que utilizará la aplicación empaquetada.

**Corrección recomendada:** exportar la variable antes de cualquier comando Django y comprobar explícitamente que la base, migraciones y roadmap quedan en el mismo directorio que usa Electron. Añadir una prueba automatizada del script con directorio temporal.

### QA-02 — El lanzador codeguard depende de un entorno de desarrollo
**Prioridad: P1.**

El script invoca `./.venv/bin/python` sin comprobar que exista y requiere que el repositorio y el AppImage estén en la ruta calculada desde el script. Esto no es apropiado como lanzador de usuario final en un equipo que solo recibe el paquete.

**Corrección recomendada:** separar claramente el lanzador de desarrollo del acceso al paquete instalado. La aplicación distribuida no debe requerir Python, Node.js, `.venv` ni el repositorio fuente.

### QA-03 — El servidor empaquetado no inicializa una instalación nueva
**Prioridad: P0 / bloqueante para primer arranque.**

`server_entry.py` declara que las migraciones y la carga de ASCENSO se ejecutan externamente antes de iniciar Electron. Sin embargo, Electron inicia directamente el binario empaquetado. En Windows, `build_windows.bat` aplica migraciones y carga ASCENSO durante la construcción usando la configuración de desarrollo; el runtime empaquetado usa el directorio `userData` de Electron. La base creada durante el build no es la base limpia del usuario final.

**Corrección recomendada:** implementar un inicializador de primer arranque seguro e idempotente para el directorio de datos del usuario. Debe aplicar migraciones y cargar el roadmap solo cuando corresponda, validar el resultado y no sobrescribir progreso ni datos existentes. No incluir una base SQLite del desarrollador como sustituto de inicialización.

### QA-04 — Comprobación de disponibilidad HTTP demasiado permisiva
**Prioridad: P2.**

`waitForServer` acepta cualquier estado HTTP inferior a 500. Un 404 o 403 podría considerarse señal de servidor listo aunque la ruta principal o el sistema no esté correctamente inicializado.

**Mejora recomendada:** endpoint local de salud dedicado que confirme aplicación, base inicializada y migraciones; comprobar el estado esperado y reportar errores diagnósticos concretos.

### QA-05 — Matriz de plataformas incompleta
**Prioridad: P1 para distribución multiplataforma.**

La configuración de electron-builder declara Linux AppImage para `x64`. Existe un script de build Windows para instalador NSIS y portable. No se observa configuración de macOS ni de Linux ARM64/Windows ARM64.

**Recomendación:** definir oficialmente los sistemas y arquitecturas soportados. Construir cada artefacto en runner/host nativo, probar instalación limpia y mantener una matriz de compatibilidad. No afirmar que funciona en “cualquier equipo” hasta cubrir esa matriz.

### QA-06 — Tutor local no equivale a IA disponible en cualquier equipo
**Prioridad: P1 para experiencia del tutor.**

El tutor usa Ollama local, con modelo por defecto `qwen2.5-coder:1.5b` y fallback de reglas estáticas. El ejecutable de Ollama y sus pesos no forman parte del paquete Electron observado. La tutoría generativa depende de instalar Ollama y descargar el modelo al menos una vez; memoria, CPU y GPU afectan latencia y viabilidad.

**Recomendación:** hacer Ollama opcional, detectar su disponibilidad y modelo instalado, ofrecer guía de instalación/descarga separada y garantizar que el núcleo educativo siga funcionando sin modelo. Medir rendimiento en el hardware mínimo. Verificar que la URL configurable del tutor se limite a loopback en la modalidad privada para impedir enviar código/consultas a un host remoto por configuración accidental.

### QA-07 — Ejecución segura de código aún pendiente
**Prioridad: P0 antes de habilitar ejecución arbitraria.**

La documentación correctamente prohíbe ejecutar código del estudiante en el proceso Django sin sandbox. No se debe añadir ejecución real hasta tener aislamiento independiente con límites de CPU, memoria, tiempo, archivos, procesos y red, y pruebas de escape. Los evaluadores deterministas actuales deben seguir siendo la fuente de verdad.

### QA-08 — Línea base de pruebas no está reconciliada
**Prioridad: P1 de calidad documental.**

El README informa 245 pruebas OK en siete aplicaciones el 16-11-2026. El plan maestro informa 245 como total; el plan de pruebas registra 197 en cuatro aplicaciones; otros documentos todavía citan 138. Estos resultados pueden representar subconjuntos y líneas base históricas, pero la documentación no proporciona una única orden reproducible para el total de 245.

**Acción:** ejecutar en el commit actual el conjunto explícito de las siete apps, registrar comando completo, entorno, salida final y fecha. Mantener 197 como resultado histórico/subconjunto solo si se confirma qué módulos incluye.

### QA-09 — Backups y restauración no están aceptados
**Prioridad: P1 antes de distribuir.**

SQLite WAL y los datos locales requieren una estrategia coherente de backup/restauración que contemple base, WAL, clave secreta, media y metadatos de versiones. El plan de pruebas todavía marca backup/restauración como pendiente.

**Recomendación:** usar la API de backup de SQLite o una copia consistente, verificar hash, probar restauración en directorio aislado y documentar exportación/importación entre equipos.

### QA-10 — Aceptación de escritorio y offline E2E pendiente
**Prioridad: P0 antes de distribución.**

Los documentos previos acreditan build PyInstaller, smoke test del modo `--sync-knowledge` y generación del AppImage, pero no equivalen a validar el arranque normal de Waitress, navegación GUI, uso offline real, cierre normal y ausencia de procesos huérfanos.

**Acción:** ejecutar una matriz manual en instalación limpia, sin Internet y con datos temporales; validar panel, ASCENSO, lección, ejercicio, persistencia, reinicio, cierre y puertos.

### QA-11 — Documentación de Windows heredada
**Prioridad: P2.**

`README_WINDOWS.md` conserva referencias a PySide6, `desktop/main.py`, `CodeGuard.spec` y autenticación activa, mientras la arquitectura actual es Electron + Django empaquetado con `CodeGuardServer.spec` y autenticación desactivada temporalmente.

**Acción:** reemplazar las instrucciones heredadas y mantener una guía de build separada de la guía de instalación del usuario final.

## 6. Recomendaciones de arquitectura para un producto personal offline

1. Mantener SQLite como fuente de verdad del estudiante y separar estrictamente datos de usuario de paquetes académicos.
2. Permitir exportar/importar el perfil local con progreso, intentos, preferencias y evidencias, cifrando datos sensibles cuando corresponda.
3. Diseñar actualizaciones de aplicación y de contenido como procesos distintos: la actualización del contenido no debe exigir Internet para estudiar ni tocar el progreso.
4. Mantener el tutor IA como capacidad opcional; fallback determinista siempre disponible.
5. No incluir servicios remotos, telemetría, APIs de pago ni sincronización de datos personales por defecto.
6. Introducir un instalador/primer arranque idempotente, con migraciones, carga curricular, verificación de integridad y recuperación.
7. Añadir health check, logs rotativos, diagnóstico exportable sin secretos y reporte de errores local.
8. Medir RAM, CPU, espacio en disco, tiempos de inicio y tamaño de modelos en el equipo mínimo objetivo.
9. Definir política de soporte por SO/arquitectura; no prometer compatibilidad universal.
10. Mantener los 12 temas, accesibilidad de teclado, contraste y reduced-motion como regresiones obligatorias.

## 7. Plan de trabajo recomendado

### Bloque A — Estabilización de instalación
- Corregir QA-01 y QA-03.
- Validar primer arranque con directorio vacío y con datos ya existentes.
- Repetir Linux AppImage y Windows NSIS/portable en equipos limpios.

### Bloque B — Calidad y seguridad
- Reproducir 245 pruebas y unificar la línea base.
- Ejecutar check, makemigrations check, pip check, pruebas de seguridad y análisis de dependencias.
- Auditar privacidad del tutor, IPC Electron, CSP, CSRF, almacenamiento de secretos y permisos de archivos.
- Mantener bloqueada la ejecución arbitraria hasta aprobar sandbox.

### Bloque C — Aceptación funcional
- Probar las 33 etapas, módulos y lecciones con contenido real.
- Probar ejercicios, evaluaciones, progresión y trazabilidad de resultados.
- Probar tutor con Ollama y fallback sin Ollama.
- Probar recompensas, misiones, rachas, mundo/avatar y desafíos.
- Probar los 12 temas y tamaños de ventana.

### Bloque D — Portabilidad y recuperación
- Añadir backup/restore y migración de datos entre equipos.
- Validar funcionamiento sin red desde arranque en frío.
- Definir artefactos soportados por sistema operativo y arquitectura.
- Documentar requisitos mínimos y espacio de almacenamiento, especialmente para modelos locales.

## 8. Criterio de liberación

No declarar CodeGuard Pro listo para distribución hasta que:
- Una instalación limpia inicialice su propia base y roadmap sin Python/Node en el equipo destino.
- La suite de pruebas esté reproducible y documentada.
- La aplicación funcione sin Internet en los flujos esenciales.
- Los datos sobrevivan reinicios, actualizaciones y restauración.
- Se valide GUI, cierre y procesos en cada plataforma declarada.
- No existan rutas de ejecución arbitraria sin sandbox aprobado.
- Los requisitos del tutor local se comuniquen con claridad.
- La documentación de instalación corresponda exactamente al paquete entregado.

---

**Conclusión:** la base del proyecto es sustancial y la arquitectura elegida encaja con una aplicación educativa personal offline-first. La prioridad ya no debe ser añadir más módulos; debe ser cerrar la instalación limpia, la persistencia, la portabilidad, el contenido académico real y la aceptación funcional de extremo a extremo.

### QA-12 — Límite de pistas no protegido frente a concurrencia
**Prioridad: P2.**

En `apps/tutoring/services.py`, `entregar_pista` lee `pistas_utilizadas`, genera la pista y después actualiza el contador. El flujo no está envuelto en una transacción ni bloquea la fila de sesión. Dos solicitudes simultáneas pueden leer el mismo contador y registrar pistas con el mismo número o superar el límite efectivo.

**Mejora recomendada:** serializar la reserva del número de pista con transacción y estrategia compatible con SQLite (actualización condicional/contador atómico), imponer unicidad de `(sesion, numero_pista)` y añadir prueba concurrente.

### QA-13 — URL del tutor configurable sin restricción de loopback
**Prioridad: P1 de privacidad.**

El tutor construye la URL de Ollama desde `CODEGUARD_TUTOR_BASE_URL`. El valor por defecto es localhost, pero la configuración acepta una URL alternativa sin validar que sea loopback. El análisis del intento incluye la respuesta/código del estudiante en el contexto enviado al modelo.

**Mejora recomendada:** en el modo privado/offline, aceptar únicamente `localhost`, `127.0.0.1` o `::1`; rechazar hosts remotos y redirecciones. Si en el futuro se permite un proveedor remoto, debe ser una opción explícita, con consentimiento y aviso claro de qué datos salen del equipo.

### QA-14 — Modo sin autenticación en equipo compartido
**Prioridad: P1 condicionada al entorno de uso.**

`AUTH_DISABLED = True` y las vistas con `requiere_acceso` permiten acceso sin credenciales. El servidor se limita a loopback, pero loopback no separa usuarios del sistema operativo: otros procesos o cuentas locales del mismo equipo pueden intentar acceder a la interfaz.

**Recomendación:** para equipos personales de un solo usuario puede aceptarse como decisión temporal; para laboratorios, computadores compartidos o perfiles de Windows/Linux multiusuario, reactivar autenticación o añadir una barrera local ligada a la sesión del usuario antes de distribuir.
