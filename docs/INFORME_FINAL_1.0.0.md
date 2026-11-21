# CodeGuard Pro 1.0.0 — informe de finalización

**Fecha:** 2026-11-21
**Rama:** `release/1.0.0-final` (base: `release/1.0.0`)
**Alcance:** plataforma educativa local (Electron + Django + SQLite).
**Fuera de alcance:** Mundo CodeGuard, PR #15 y PR #16. No se ha desarrollado contenido de videojuego.

> Este informe describe únicamente lo verificado en esta iteración. Las
> dependencias externas pendientes se indican de forma expresa y no se
> presentan como completadas.

## 1. Resultado ejecutivo

La aplicación arranca en un perfil limpio, crea el propietario local, aplica
migraciones, instala ASCENSO 3.1 y abre la interfaz. Los módulos operativos
quedan conectados a SQLite: panel, roadmap, lecciones, evaluaciones,
evidencias, gamificación, tutor local, biblioteca documental, base de
conocimiento (solo lectura) y backups.

Se corrigieron tres bloqueos reales:

1. **Sin propietario local en un perfil limpio.** Todas las escrituras
   (progreso, intentos, evidencias, gamificación) se rechazaban. Ahora el
   arranque crea una sola vez un propietario local sin credenciales, solo con
   `AUTH_DISABLED=True`.
2. **CSRF roto por `Referrer-Policy: no-referrer`.** Chromium enviaba
   `Origin: null` en los POST de formularios y Django los rechazaba con 403.
   Se cambió a `same-origin`; los formularios reales (importación de PDF,
   archivar, evaluaciones, evidencias) funcionan dentro de Electron.
3. **Arranque lento por reconstruir el roadmap en cada inicio.** Se añadió
   verificación de integridad con huella de manifiesto y contenido. El segundo
   arranque verifica 1.946 lecciones en ~0,1–0,3 s en lugar de reconstruirlas.

## 2. Funcionalidades verificadas

| Área | Resultado | Evidencia |
|---|---|---|
| Backend Django | Operativo | `manage.py check` sin incidencias; 349 pruebas OK |
| Migraciones | Al día | `makemigrations --check --dry-run` sin cambios |
| Frontend | Operativo | 7 rutas principales HTTP 200; 12 temas; sin desbordamiento a 1024/768 px |
| Electron | Operativo | IPC, tema persistente, cierre sin huérfanos, formularios CSRF |
| Base de datos | Operativa | SQLite WAL; migraciones y datos en `CODEGUARD_DATA_DIR` |
| Roadmap ASCENSO | Completo | 33 etapas, 212 módulos, 1.946 títulos, 7 prerrequisitos |
| Lecciones | Contenido inicial | 8 lecciones estructuradas en borrador; 1.938 títulos pendientes; 0 publicadas |
| Tutor IA | Operativo con y sin Ollama | Detección de Ollama/modelo, pistas y fallback determinista |
| Evaluaciones | Operativo | Quiz publicado de prueba, envío y calificación en servidor |
| Evidencias | Operativo | Registro de criterio y cierre de etapa por criterios |
| Biblioteca | Operativa | Importación PDF, búsqueda, archivo, visor y rangos HTTP |
| Base de conocimiento | Consulta y edición | Fuentes, versiones, paquetes y espacio editorial con transiciones auditadas |
| Gamificación | Operativa | XP/monedas/logros/misiones idempotentes; no altera notas |
| Backups | Operativo | Crear, verificar, restaurar y rollback con perfil temporal |
| Seguridad | Sin hallazgos críticos | CSP, loopback, CSRF, uploads validados, Ed25519, backups |
| Rendimiento | Objetivos cumplidos | Primer arranque 13–16 s; normal ~2,8 s con Electron |
| Instalación Linux | Verificada | Servidor PyInstaller + AppImage extraído, E2E completo |
| Instalación Windows | CI únicamente | Run `44944410767` verde: NSIS, 7 rutas, 12 temas, tema/progreso persistente, desinstalación y portable; falta hardware físico |
| Offline | Verificado por diseño y E2E | Sin CDN, sin telemetría, sync falla cerrado |

## 2.1 Contenido académico y espacio editorial

Se desarrolló el módulo 0.1 «Aprender a aprender» con **8 lecciones completas**
(objetivos, conocimientos previos, introducción, teoría, explicación sencilla,
conceptos, aplicaciones, errores frecuentes, ejemplo, dos ejercicios
deterministas, autoevaluación, fuentes y video). El contenido es original y
usa referencias verificables; no se rellenaron lecciones con texto genérico.

La cobertura real es: **8 desarrolladas, 0 aprobadas y 0 publicadas**; las otras
1.938 permanecen pendientes. El contenido se siembra una sola vez como
**borrador editorial** y se puede estudiar con un aviso visible. La aprobación
y publicación requieren una acción explícita del propietario en el nuevo
**Espacio editorial**, que permite editar, versionar, enviar a revisión,
aprobar, publicar, retirar, registrar fuentes y revisar licencias. La pantalla
**Cobertura** separa producción editorial de progreso del estudiante.

Los **8 videos** fueron verificados por metadatos públicos (título, canal, URL,
duración y pista de audio/captions en español). Se abren en el navegador del
sistema mediante un IPC restringido a HTTPS; la lección funciona sin conexión.
La revisión pedagógica completa de cada video queda declarada como pendiente.

Detalle: [`CONTENIDO_ACADEMICO.md`](CONTENIDO_ACADEMICO.md).

## 3. Datos y persistencia

- El propietario local se crea solo una vez y no tiene contraseña utilizable.
- El progreso, intentos, resultados, evidencias, monedas y misiones se guardan
  en SQLite y sobreviven al reinicio.
- La restauración de una copia conserva `media/` y la tabla de estado del
  roadmap; el arranque posterior reutiliza el contenido sin reconstruirlo.
- Los registros ajenos al manifiesto se conservan y se contabilizan para no
  borrar progreso histórico.

## 4. Rendimiento medido

Máquina de referencia: Linux x86_64, 7,4 GB RAM, carga media alta durante las
pruebas. Medición reproducible con `scripts/benchmark-startup.py`.

| Escenario | Antes (medido) | Después (medido) |
|---|---|---|
| `cargar_ascenso` en cada arranque | ~3,4 s (4.000+ consultas) | 0 s en arranque normal |
| Verificación de 1.946 lecciones | No existía | 0,08–0,30 s |
| Servidor empaquetado, primer arranque | ~12,6 s (sin cambios de datos) | ~13–16 s según carga del equipo |
| Servidor empaquetado, segundo arranque | ~4,0 s | **~1,2 s** |
| Electron completo, segundo arranque | No medido | **~2,8 s** |
| Benchmark interno, segundo arranque | ~3,4 s | **~0,15 s** |

Objetivos: normal ≤10 s y primer arranque ≤30 s. Ambos se cumplen en la
máquina de referencia. El detalle metodológico está en
[`RENDIMIENTO_ARRANQUE.md`](RENDIMIENTO_ARRANQUE.md).

## 5. Pruebas ejecutadas

```bash
CODEGUARD_DATA_DIR=/tmp/cg-base .venv/bin/python manage.py check
CODEGUARD_DATA_DIR=/tmp/cg-base .venv/bin/python manage.py makemigrations --check --dry-run
CODEGUARD_DATA_DIR=/tmp/cg-base .venv/bin/python manage.py test --parallel 1
npm run test:electron
.venv/bin/python scripts/benchmark-startup.py
.venv/bin/python -m pip_audit -r requirements.txt
npm audit --omit=dev
```

Resultados:

- Django: **349 pruebas OK** (178 s).
- Electron: **26 pruebas OK**.
- `pip-audit`: sin vulnerabilidades conocidas.
- `npm audit --omit=dev`: 0 vulnerabilidades de producción.
- `npm audit` completo: 6 moderadas en la cadena de build de
  `electron-builder`; no hay corrección compatible sin degradación.
- Benchmark: primer arranque 13,6 s; segundo 1,0 s de pared; historial 1,5 s.
- Servidor PyInstaller: primer arranque ~15,2 s; segundo ~1,0 s.
- AppImage extraído: interfaz lista en ~2,8 s; E2E de 7 rutas, 12 temas,
  formulario PDF y cierre sin procesos huérfanos.
- Responsive: 11 pantallas sin desbordamiento horizontal a 1024×720 y 768×900
  (`scripts/cdp-responsive.js`).
- Backup/restore de integración: base y `media/` restauradas; marcador posterior
  eliminado; estado curricular reutilizado tras restaurar.
- Windows (CI, no hardware físico): run `44944410767` verde en 4/4 jobs.
  Instalación NSIS, primer arranque, 7 rutas 200, 12 temas, tema `fantasy`
  persistente, `PROGRESS=1`, desinstalación, portable y sin procesos huérfanos.
  Artefacto `codeguard-windows-x64` (275.075.760 bytes, SHA-256 del ZIP
  `906ed6993c8b29efff86452a8e5805fac5c7d861d676ba13a101b6448e5306a5`).

## 6. Seguridad

- Servidor Waitress en `127.0.0.1`; `ALLOWED_HOSTS` local.
- CSP sin CDN, `script-src 'self'`, `frame-src 'self'`; PDF incrustado solo del
  mismo origen.
- CSRF activo. La política de referrer se ajustó a `same-origin` para que
  Chromium envíe un `Origin` válido en los POST.
- Subida de PDF: extensión, tamaño máximo 50 MB, firma `%PDF-`, SHA-256,
  rechazo de duplicados, nombre saneado y descarga con `nosniff`.
- El tutor solo acepta URLs loopback de Ollama, no sigue redirecciones y no
  envía datos a hosts remotos.
- Los backups validan ZIP, rutas, CRC, hashes, SQLite y compatibilidad de
  esquema antes de restaurar; conservan copia de reversión.
- La ejecución arbitraria de código sigue deshabilitada. No se añadió sandbox
  ni se habilitaron laboratorios de ejecución.
- No se reactivó la autenticación ni se expuso Django a la red.

## 7. Limitaciones y pendientes externos

1. **Contenido académico:** 8 lecciones del módulo 0.1 están desarrolladas
   como borradores; 1.938 siguen pendientes. No se publicaron cuerpos genéricos
   ni se atribuyó aprobación humana. El contenido de PR #14 se usó como
   orientación editorial, no como publicación automática. La etapa 25 sigue sin
   objetivo formal en el documento maestro.
2. **Windows físico:** la instalación NSIS/portable está validada en CI, no en
   hardware Windows real. No se declara aceptación física.
3. **Sincronización remota de producción:** no hay endpoint, allowlist ni
   claves públicas. El cliente falla cerrado y la aplicación funciona offline.
4. **macOS y ARM64:** no configurados ni validados.
5. **Biblioteca:** no se añadió parsing/OCR de PDF; se usa el visor de Chromium.
   Esto evita dependencias y superficie de ataque adicionales.
6. **Laboratorios, competencias, vigencia y ética:** siguen fuera del alcance
   operativo de esta entrega y aparecen como no disponibles en la navegación;
   no se simulan acciones.
7. **AppImage en este host:** el montaje FUSE se bloqueó tanto en el artefacto
   nuevo como en el anterior. Se verificó con extracción
   (`APPIMAGE_EXTRACT_AND_RUN=1`) y se documentó el fallback en `run.sh`.

## 8. Matriz de trazabilidad resumida

| Funcionalidad | Requisito | Backend | Frontend | Persistencia | Prueba | Estado |
|---|---|---|---|---|---|---|
| Perfil local | Identidad monousuario | `accounts.bootstrap` | Navegación sin login | `accounts_usuario` | `test_bootstrap_local` | Completo |
| Panel | RF-016 | `core.views.panel` | `core/panel.html` | SQLite | `test_panel` | Completo |
| Roadmap | RF-010/011 | `roadmaps.services` | `lista/detalle` | SQLite | `test_roadmaps` | Completo |
| Lecciones | Fase 2 | `leccion_detalle` | `leccion.html` | SQLite | `test_learning_content` | Estructura; contenido editorial pendiente |
| Evaluaciones | Fase 4 | `services_evaluacion` | `quiz_*` | SQLite | `test_evaluacion` | Completo con contenido publicado |
| Evidencias | Fase 5 | `registrar_cumplimiento_criterio` | `evidencias` | SQLite | `test_evaluacion` | Completo |
| Tutor | Fase 3 | `tutoring.services` | `tutoria.js` | SQLite | `test_tutoria` | Completo con fallback |
| Biblioteca | Fase 4 | `apps.library` | `library/*` | SQLite + media | `test_library` | Completo |
| Conocimiento | RF-050–059 | modelos y comandos | `conocimiento.html` | SQLite | `test_publisher` | Backend completo; UI solo lectura |
| Gamificación | Fase 5 | `gamification.services` | `perfil.html` | SQLite | `test_gamification` | Completo; no altera notas |
| Backups | Fase 8 | `core.backup/restore` | `backups.html` + IPC | ZIP + SQLite | `test_backups` | Completo |
| Arranque | RNF rendimiento | `roadmaps.bootstrap` | splash Electron | metadatos SQLite | `test_bootstrap`, benchmark | Completo |

## 9. Archivos principales modificados o añadidos

- `apps/roadmaps/bootstrap.py`, `apps/roadmaps/migrations/0020_*`,
  `apps/roadmaps/management/commands/verificar_perfil.py`.
- `apps/accounts/bootstrap.py`, migración de auditoría de propietario local.
- `apps/roadmaps/data/contenido_academico_0_1.json`,
  `cargar_contenido_academico`, `coverage.py`, `editorial_views.py`,
  `forms.py`, `templates/roadmaps/editorial*.html` y `cobertura.html`.
- `apps/roadmaps/models.py` y migración 0021: contenido ampliado y videos.
- `apps/library/*` y `templates/library/*` (módulo nuevo).
- `templates/roadmaps/conocimiento.html` y vista de solo lectura.
- `config/health.py`, `config/middleware.py`, `config/settings/development.py`,
  `config/urls.py`.
- `electron/main.js`, `electron/startup-status.js` y pruebas.
- `scripts/benchmark-startup.py`, `scripts/cdp-form-smoke.js`,
  `scripts/cdp-smoke.js`.
- `run.sh`, `.github/workflows/ci.yml`, README y documentación.

## 10. Artefactos verificados

- Servidor PyInstaller Linux x64:
  `4fceaa9acc0e209c1446a7f5e8b423e136344759351c35af57fdf1f93af1fd39`
  (`dist-server/CodeGuardServer/CodeGuardServer`).
- AppImage Linux x64:
  `aba8922cf79524942a7ae8a80c5d70e7ec25d33ab919634930ccdccdcdd65493`
  (`dist/CodeGuard-Pro-1.0.0-x86_64.AppImage`).
- El AppImage se verificó extrayéndolo (`--appimage-extract`) por el bloqueo
  FUSE del host de pruebas; el binario extraído ejecutó el mismo E2E.

## 11. Entrega

- Rama: `release/1.0.0-final` (publicada en `origin`).
- Pull request de finalización: https://github.com/MaverickBms/CodeGuard-Pro/pull/17
  (contra `release/1.0.0`; **no fusionado**).
- Commits principales:
  - `5a1862e` fix(arranque): perfil local idempotente y propietario sin credenciales.
  - `abf5b97` feat(biblioteca): PDFs locales, conocimiento de solo lectura y navegación.
  - `13c00f1` fix(seguridad,electron): CSRF same-origin y arranque observable.
  - `ec07181` feat(tutor): detección de modelo, timeout acotado y fallback claro.
  - `17ec90a` docs: informe final 1.0.0, rendimiento y criterios de aceptación.
  - `bb457e0` fix(linux): conserva el perfil heredado al lanzar con run.sh.
  - `937684b` test(ui): smoke responsive de las pantallas principales.
- No se ha creado tag ni release; no se ha fusionado ningún PR.
- PR #15 y #16 permanecen fuera de alcance y sin modificar.

## 12. Conclusión

CodeGuard Pro 1.0.0 queda operativo como plataforma educativa local para un
perfil limpio: abre, siembra 8 lecciones iniciales en borrador, guarda progreso
real, permite estudiar contenido con fuentes y videos, resolver ejercicios,
registrar evidencias y evaluaciones, consultar PDFs, usar el tutor con fallback
y crear/restaurar copias. El espacio editorial permite aprobar y publicar
contenido cuando el propietario lo decida. Lo que falta es ampliar el contenido
académico, la revisión humana independiente, la aceptación física Windows y la
infraestructura remota opcional; nada de ello se declara terminado.
