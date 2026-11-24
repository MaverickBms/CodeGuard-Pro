# Estado funcional de CodeGuard Pro 1.0.0

**Fecha:** 2026-11-21
**Criterio:** una función solo figura como **Completa** si tiene implementación
real, persistencia y una prueba reproducible. Una pantalla vacía no se considera
funcionalidad terminada.

## 1. Matriz general

| Área | Estado | Qué funciona realmente | Límite declarado |
|---|---|---|---|
| Arranque | Completa | Migraciones, propietario, roadmap y siembra inicial | Primer arranque tarda más por migraciones/siembra |
| Panel | Completa | Progreso real, próxima etapa, actividad y cobertura | No hay métricas inventadas |
| Roadmap | Completa | 33 etapas, 212 módulos, 1.946 títulos, filtros y prerrequisitos | La mayoría de títulos no tienen cuerpo |
| Etapas | Completa | Navegación, bloqueo, criterios y evidencias; la lectura de lecciones bloqueadas es de solo consulta y las entregas/quizzes/tutoría respetan prerrequisitos | Reabrir una etapa es explícito |
| Lecciones | Parcial | 8 lecciones completas del módulo 0.1 | 1.938 títulos sin contenido |
| Ejercicios | Completa (alcance actual) | Evaluadores deterministas, intentos e historial | No ejecuta código; sin sandbox |
| Evaluaciones | Parcial | Quiz publicables, corrección backend y resultados inmutables | 0 quizzes publicados en perfil limpio; abiertas pendientes de revisión |
| Progreso | Completa | Lecciones por evidencia, módulos por evaluación y etapas por criterios; unicidad de registros protegida por nivel en la base de datos | No se puede completar manualmente |
| Tutor | Completa con fallback | Ollama local, detección de modelo, pistas e informe; verifica roadmap activo y prerrequisitos en endpoints directos | Sin Ollama o respuesta vacía usa reglas locales |
| Biblioteca | Completa | Importación PDF, SHA-256, búsqueda, archivo, visor y rangos | Sin OCR ni parsing |
| Conocimiento | Completa local | Fuentes, versiones, paquetes y estados reales | Sincronización remota no configurada |
| Editorial | Completa | Editar, versionar, fuentes, revisión, aprobación, publicación y retirada | El contenido inicial queda en borrador |
| Gamificación | Completa | Monedas, logros, misiones, racha, avatar e historial | No sustituye criterios académicos |
| Perfil | Parcial | Avatar, nombre, especie y clase | No hay edición de nombre de usuario |
| Temas | Completa | 12 paletas, persistencia en perfil y contraste WCAG | Sin editor de temas personalizados |
| Backups | Completa | Crear, verificar, restaurar y rollback | Restauración desde menú/CLI, no desde la web con servidor activo |
| Instalación Linux | Completa (host de auditoría) | AppImage, servidor PyInstaller y cierre limpio | FUSE bloqueado en este host; se usó extracción |
| Instalación Windows | Parcial | CI de NSIS/portable, instalación y persistencia | Falta hardware Windows físico |
| macOS / ARM64 | No disponible | — | Fuera de alcance; no se declara soporte |
| Laboratorios | No disponible | Elemento deshabilitado con aviso | No hay sandbox |
| Competencias | No disponible | Elemento deshabilitado con aviso | Fuera del alcance 1.0.0 |
| Vigencia | No disponible | Elemento deshabilitado con aviso | Fuera del alcance 1.0.0 |
| Ética | No disponible | Elemento deshabilitado con aviso | Fuera del alcance 1.0.0 |

## 2. Recorrido inicial real

El recorrido disponible en un perfil limpio es:

1. Abrir el panel y el roadmap ASCENSO.
2. Entrar en la etapa 0 y en el módulo 0.1 «Aprender a aprender».
3. Estudiar una de las 8 lecciones con contenido.
4. Leer objetivos, teoría, explicación, conceptos, aplicaciones, errores, ejemplo
   y fuentes.
5. Resolver el ejercicio determinista obligatorio.
6. Recibir retroalimentación del backend.
7. Completar la lección cuando se aprueba el ejercicio exigido.
8. Consultar el progreso en la lección, la etapa y el panel.
9. Cerrar y volver a abrir: el progreso, el intento y el tema persisten.
10. Usar el tutor local (o su fallback) y consultar los videos.

La lección se muestra con el aviso de **borrador editorial**. No se presenta
como publicada. El recorrido es corto y real; no se rellenaron las 1.938
lecciones restantes con texto genérico.

## 3. Evaluaciones: estado exacto

- El modelo, la corrección y la inmutabilidad están implementados.
- Un quiz solo se muestra si está publicado.
- La puntuación se calcula en servidor; el cliente no puede cambiarla.
- Las respuestas correctas no se envían antes del envío.
- Un resultado por debajo del umbral no aprueba.
- Las respuestas abiertas quedan en `requiere_revision` y no se aprueban solas.
- En un perfil limpio no hay quizzes publicados: la pantalla muestra un estado
  vacío honesto. Existe un comando de carga de ejemplo en estado borrador.
- **Pendiente:** interfaz de revisión docente para resolver respuestas abiertas.

## 4. Contenido y videos

| Indicador | Valor real |
|---|---:|
| Títulos curriculares | 1.946 |
| Lecciones con cuerpo | 8 |
| Versiones borrador | 8 |
| Aprobadas | 0 |
| Publicadas | 0 |
| Pendientes | 1.938 |
| Ejemplos | 8 |
| Ejercicios | 16 |
| Videos con enlace/metadatos verificados | 8 |
| Videos con revisión pedagógica aprobada | 0 |
| Fuentes únicas | 13 |
| Referencias de fuente | 16 |

Los videos están disponibles como recurso complementario, pero la interfaz
declara que su revisión pedagógica está pendiente. Los enlaces se verificaron
técnicamente con metadatos públicos; no se atribuye una validación didáctica que
no se realizó.

## 5. Persistencia comprobada

Se verificó con un perfil temporal y reinicios reales de Electron:

- Tema `fantasy` aplicado y recuperado tras reiniciar.
- Lección «Aprendizaje activo» completada al 100 %.
- Intento con 100 % y estado «Aprobado».
- Etapa 0 con 3 % de avance por 1 de 30 lecciones.
- Documento PDF importado, visible, archivado y persistente.
- Backup creado, verificado y restaurado en un perfil aislado; progreso, intento
  y documento archivado recuperados.
- Cierre sin procesos `CodeGuardServer` ni Electron huérfanos.

## 6. Sistema editorial

Flujo real:

`borrador → revisión → aprobada → publicada → retirada/sustituida`

- Cada transición es una acción POST explícita y auditada.
- Una versión publicada no se edita silenciosamente; se crea otra versión.
- La publicación exige versión aprobada, fuentes autorizadas y puerta de calidad.
- El estudiante solo ve publicado cuando existe `ContenidoLeccionActivo`.
- El contenido sin publicar se muestra como borrador con aviso.
- Los permisos se limitan al propietario local explícito.
- Los formularios inválidos conservan el texto y muestran errores.

## 7. Conclusión

La versión 1.0.0 es una plataforma educativa local funcional y honesta sobre su
cobertura. Su mayor limitación no es técnica sino de contenido: 8 lecciones con
cuerpo frente a 1.946 títulos curriculares. La aplicación no oculta esa brecha.

## 8. Actualización de auditoría autónoma (2026-11-23)

### Estado verificado en esta sesión
- Suite Django: 379 pruebas OK en entorno local (apps.core, accounts, audit, roadmaps, tutoring, gamification, challenges, library).
- Electron: 26 pruebas OK.
- `manage.py check` y `makemigrations --check --dry-run` sin incidencias.
- Smoke HTTP de rutas principales: 200 en páginas clave; POST-only endpoints devuelven 405 ante GET.
- CI del HEAD base `66468a5`: 4/4 verde (dos runs).

### Correcciones aplicadas en esta sesión
- Criterio manual/proyecto ya no completa etapa sin evaluación aprobada (se mantiene registro de evidencia).
- `codigo_contiene` puede completar lección cuando `permite_completar_leccion=True`.
- Publisher/distribución/content_import aceptan esquemas de contenido 1 y 2 (validación de compatibilidad; pendiente validación E2E de publicación esquema 2).
- Manejo de errores robusto en `cargar_contenido_academico` y `importar_documentos_validados` ante datos malformados/carreras.
- Vista detalle de etapa expone `etapa.completada`.

### Limitaciones funcionales observadas (no resueltas)
- Cobertura académica: 8 lecciones en borrador, 0 aprobadas/publicadas, 1.938 títulos pendientes. Etapa 25 sin objetivo formal aprobado.
- Gamificación sin campos de experiencia/nivel en `PerfilGamificacion` (hay monedas, rachas, logros, misiones, avatar).
- No hay UI de borrado de documentos de biblioteca (solo archivar/restaurar).
- No hay revisión docente de respuestas abiertas.
- Sin validación visual automatizada por navegador en esta sesión.
- Aceptación Windows física, firma de código, sincronización remota de producción, macOS/ARM64 fuera de alcance.

## Arranque / rendimiento (2026-11-23)

| Área | Estado | Nota |
|---|---|---|
| Instrumentación arranque server/bootstrap/Electron | OK | `startup-perf.json`, `startup-perf-electron.json`, eventos BOOT/PERF |
| `/healthz/` caché migraciones | OK | Solo cachea migraciones; sigue verificando roadmap |
| Cobertura panel con caché | OK | TTL 60s, invalidación en mutaciones editoriales/conocimiento |
| Waitress hilos arranque local | OK | 8 hilos por defecto, configurable `CODEGUARD_WAITRESS_THREADS` |
| Servidor empaquetado warm | OK medido | ~1.28s a /healthz en temp profile |
| Servidor empaquetado fresh | OK medido | ~12.45s a /healthz en temp profile |
| AppImage UI utilizable validado | PENDIENTE VALIDACIÓN EXTERNA | Rebuild OK; ejecución GUI no concluyente en este entorno |


## Pantalla de carga dinámica (2026-11-23)

| Área | Estado | Nota |
|---|---|---|
| Splash local autocontenido | OK | `electron/splash.html`, sin deps externas |
| Progreso real por fases | OK | IPC `startup-progress`, pesos, cap 99% hasta interactivo |
| Frases motivacionales locales | OK | colección local en español, sin red |
| Terminal progress (TTY) | PARCIAL | línea de progreso desde Electron stdout; run.sh header TTY |
| Validación AppImage UI | PENDIENTE VALIDACIÓN EXTERNA | rebuild OK, entorno GUI no concluyente |


## Endurecimiento splash/señal interactiva (2026-11-23 sesión 4)

| Área | Estado | Nota |
|---|---|---|
| IPC app-interactive-signal | OK | corregida validación `isTrustedIpcEvent` |
| Marcas splash diferenciadas | OK | shown/dom_ready/document_loaded/first_paint |
| Buffer progreso splash | OK | snapshot enviado al cargar |
| Señal interactiva explícita | OK | frontend + fallbacks controlados |
| Recuperación fallo splash | PARCIAL | reintento/timeout/fallback; requiere validación GUI real |
| Validación AppImage GUI | PENDIENTE VALIDACIÓN EXTERNA | sin entorno gráfico |


## Auditoría de cierre sesión 5 (2026-11-23)

| Área | Estado | Nota |
|---|---|---|
| Señal interactiva verificada | OK | solo `frontend-explicit` desde main window confiable |
| Fallback sin usable/100% | OK | recuperación controlada, `verified:false` |
| Métricas splash/main frame | OK | `splash_renderer_frame_ready`, no first_paint en catch |
| Recuperación loadURL principal | PARCIAL | retry + diagnóstico; validación real pendiente |
| CI Windows acceptance (8b4063c) | FALLA CORREGIDA | causa probable pages[0] splash; fix en f22fddb |
| Validación gráfica AppImage | PENDIENTE | entorno sin GUI |
