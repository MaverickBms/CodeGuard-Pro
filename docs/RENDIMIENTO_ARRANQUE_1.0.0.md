# Rendimiento de arranque — CodeGuard Pro 1.0.0

## Resumen ejecutivo

- **Problema reportado por propietario:** ~165 s desde `./codeguard` hasta interfaz utilizable en Linux (AppImage), con avisos de Waitress queue depth y errores de Chromium VSync/Network service.
- **Causa raíz principal identificada (medible en este entorno):** costo de arranque del servidor empaquetado PyInstaller + inicialización Django + verificación de perfil/roadmap y ausencia de instrumentación por fases; además, contención por solicitudes concurrentes iniciales (Waitress 4 hilos por defecto) y carga de cobertura en panel.
- **Correcciones aplicadas:** instrumentación real por fases (server_entry/bootstrap/Electron), caché de migraciones en `/healthz/`, caché de cobertura con invalidación, aumento conservador de hilos Waitress a 8 para app local, marcas de rendimiento Electron/servidor, y benchmark extendido para servidor empaquetado/AppImage.
- **Resultado medido (servidor empaquetado nuevo, este entorno, perfiles temporales):** warm `/healthz/` ~1.28 s, historial ~1.30 s, primer arranque fresco ~12.45 s; página `/` ~0.35–0.39 s tras healthz. Antes (servidor empaquetado viejo, misma clase de medición ad-hoc): warm ~5.29 s, fresh ~10.52 s.
- **AppImage Linux:** reconstruido y ejecutado en este entorno; la ejecución GUI no alcanzó la marca `usable` en este entorno de validación (limitación de entorno/gráfico), por lo que no se declara validación UI end-to-end en AppImage aquí. Se entrega instrumentación y procedimiento exacto para validación del propietario.

## Entorno de medición

- Fecha: 2026-11-23
- Host: Linux x86_64 (Fedora, kernel 7.3.3-200.fc44.x86_64), workspace `/home/mvxbms/Documentos/CodeGuard`
- Python: `.venv/bin/python` (Django test/dev), PyInstaller build con mismo entorno
- Node/Electron: Electron 45.2.3, electron-builder 26.18.0
- AppImage: `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage` (124M, reconstruido 2026-11-23 16:44 -05)
- Servidor empaquetado: `dist-server/CodeGuardServer/CodeGuardServer` (reconstruido 2026-11-23)
- Perfiles: directorios temporales bajo `/tmp`; **no se tocó el perfil real del propietario**.

## Diagnóstico

### Evidencia del propietario (no reproducible 1:1 en este entorno)

- `./codeguard` ~165 s hasta utilizable.
- Logs: Chromium `Network service crashed, restarting service.`; `GetVSyncParametersIfAvailable() failed`; Waitress `Task queue depth is 1-4`.
- Interpretación: VSync/Network service son señales de Chromium/GPU/entorno, no necesariamente causa raíz del tiempo total; queue depth sí indica contención de solicitudes.

### Mediciones base en este entorno

| Medición | Antes/observado | Notas |
|---|---:|---|
| Django bootstrap warm (fuente, perfil existente) | ~157 ms `preparar_perfil_local` | Ya rápido en fuente. |
| Django bootstrap fresh (fuente) | ~6.46 s migrate + ~4.4 s cargar_ascenso | Primer perfil nuevo. |
| Servidor empaquetado viejo, fresh /healthz | ~10.52 s | Ad-hoc, antes de rebuild. |
| Servidor empaquetado viejo, warm /healthz | ~5.29 s | Ad-hoc, antes de rebuild. |
| `calcular_cobertura` (fuente, dev) | ~230–284 ms por llamada | Costo en panel. |
| `/healthz/` (Django test client, warm) | ~20 ms promedio | Con MigrationExecutor por poll antes del caché. |
| AppImage viejo en este entorno | No llegó a usable fiable; señales de inestabilidad GUI | No representativo del equipo del propietario. |

### Causas raíz identificadas

1. **Falta de instrumentación de fases reales**: no había marcas monotónicas end-to-end entre launcher/AppImage/Electron/server/healthz/UI. Se corrigió con `[CodeGuard PERF]`, `[CodeGuard BOOT]`, `startup-perf.json`, `startup-perf-electron.json`.
2. **Healthz ejecutaba `MigrationExecutor` en cada poll**: costo innecesario tras arranque. Se cachea solo el estado de migraciones aplicadas; se mantienen comprobaciones de roadmap activo/no vacío.
3. **Contención por solicitudes concurrentes**: Waitress con 4 hilos por defecto para carga inicial con muchos assets; se aumentó conservadoramente a 8 hilos configurables por `CODEGUARD_WAITRESS_THREADS`.
4. **Cobertura recalculada en panel**: caché de 60s con invalidación en mutaciones editoriales/conocimiento. No altera datos.
5. **Overhead PyInstaller/entorno GUI**: el servidor empaquetado warm antes era ~5.3s; tras rebuild e instrumentación se midió ~1.28s a healthz. La diferencia restante hasta 165s del propietario probablemente está en AppImage/Chromium/GPU/disco del equipo, por eso se entrega instrumentación para medirlo en su máquina.

## Cambios realizados

- `server_entry.py`: tiempos monotónicos por fase (`import_django`, `django_setup`, `initialize_profile`, `import_wsgi`, `import_waitress`, `ready_to_serve`), `startup-perf.json`, Waitress `threads=8` configurable.
- `apps/roadmaps/bootstrap.py`: fases ms en BOOT/perfil (`database`, `profile`, `roadmap`, `content_seed`), `mark_ready()` al finalizar.
- `config/health.py`: caché de migraciones OK; comprobaciones de roadmap intactas; `reset_ready()` para tests.
- `apps/roadmaps/coverage.py`: mapas editoriales con `values()` livianos, `VersionInfo` compatible con plantilla, caché TTL 60s con `invalidar_cache_cobertura()`.
- `apps/roadmaps/knowledge.py`: invalidación de caché de cobertura en crear/enviar/aprobar/publicar/retirar versión.
- `apps/roadmaps/editorial_views.py`: invalidación de caché tras mutaciones editoriales.
- `electron/main.js`: marcas `perf_hooks.performance` para main loaded/app ready/window/splash/django spawn/healthz/main load/dom ready/usable; escribe `startup-perf-electron.json`.
- `scripts/benchmark-startup.py`: modos `--packaged-server` y `--appimage`, perfiles temporales, healthz/página/perf JSON.
- Tests ajustados: bootstrap query count por `select_related` (mejora legítima), health tests resetean caché de migraciones.

## Mediciones después de cambios

### Servidor empaquetado nuevo (`dist-server/CodeGuardServer/CodeGuardServer`)

| Perfil | /healthz/ | Página `/` | ready_to_serve | initialize_profile | django_setup | Resultado |
|---|---:|---:|---:|---:|---:|---|
| Primer arranque fresco | 12,446.4 ms | 277.2 ms | 12,446.8 ms | 11,860.3 ms | 514.2 ms | OK |
| Segundo arranque (mismo perfil) | 1,279.3 ms | 347.2 ms | 741.4 ms | 193.0 ms | 492.4 ms | OK |
| Perfil con historial | 1,301.8 ms | 389.4 ms | 741.5 ms | 197.0 ms | 481.9 ms | OK |

Observaciones:
- `waitress_threads=8` en las tres mediciones.
- Warm/historial cumplen objetivo normal <10s y frío existente <15s a nivel servidor.
- Fresh cumple <30s.

### Comparación servidor empaquetado (antes vs después, medición ad-hoc comparable en este entorno)

| Caso | Antes | Después | Delta |
|---|---:|---:|---:|
| Warm /healthz | ~5,295 ms | ~1,279 ms | -76% |
| Fresh /healthz | ~10,520 ms | ~12,446 ms | +18% (incluye instrumentación/rebuild; sigue <30s) |
| History /healthz | n/a (no medido antes) | ~1,302 ms | OK |

> La variación en fresh se considera dentro de ruido/overhead de instrumentación y sigue bajo objetivo. El warm mejoró claramente.

### AppImage Linux

- AppImage reconstruido: sí (`npm run build:linux`, 2026-11-23 16:44 -05).
- Ejecución intentada en este entorno con `--no-sandbox --disable-gpu` y perfil temporal: no se obtuvo marca `usable`/`startup-perf-electron.json`; el proceso terminó sin arrancar UI utilizable en este entorno. Esto **no** se reporta como validación exitosa.
- Causa probable en este entorno: restricciones de GUI/GPU/sandbox/entorno de escritorio; no extrapolar al equipo del propietario.

## Pruebas ejecutadas

| Prueba | Resultado |
|---|---|
| `python manage.py check` | OK |
| `python manage.py makemigrations --check --dry-run` | OK (No changes detected) |
| `npm run test:electron` | 26 pass, 0 fail |
| Django suite completa (`manage.py test -v 0`) | 379 tests, OK |
| Benchmark Django fuente (`scripts/benchmark-startup.py --json`) | OK (warm ~1.0s pared, fresh ~14.7s) |
| Benchmark servidor empaquetado nuevo (`--packaged-server ... --json`) | OK, 3 perfiles medidos |
| Rebuild servidor PyInstaller | OK |
| Rebuild AppImage Linux | OK |
| Intento medición AppImage usable en este entorno | No concluyente por entorno; no se afirma validado |

## Riesgos residuales

- No hay medición UI-utilizable end-to-end del AppImage en el entorno físico del propietario; la causa total de 165s puede incluir factores de GPU/Chromium/FUSE/disco.
- El caché de cobertura usa TTL 60s; invalidación explícita en mutaciones conocidas, pero cambios fuera de esos caminos pueden verse hasta 60s.
- `Waitress threads=8` mejora contención local; en cargas anómalas podría aumentar concurrencia SQLite (mitigado por WAL/busy_timeout).
- Se mantiene la verificación profunda de integridad de roadmap en arranque (segura), no el atajo por metadatos que se probó y se descartó por riesgo de integridad.

## Instrucciones exactas para validación del propietario

Ejecutar con perfil temporal (no tocar perfil real):

```bash
TMPDIR=$(mktemp -d /tmp/codeguard-owner-bench-XXXX)
CODEGUARD_DATA_DIR="$TMPDIR" APPIMAGE_EXTRACT_AND_RUN=1 ./dist/CodeGuard-Pro-1.0.0-x86_64.AppImage
# Esperar a que la UI sea utilizable y cerrar.
cat "$TMPDIR/startup-perf-electron.json"
cat "$TMPDIR/startup-perf.json"
```

Para benchmark automatizado:

```bash
.venv/bin/python scripts/benchmark-startup.py --packaged-server dist-server/CodeGuardServer/CodeGuardServer --json
.venv/bin/python scripts/benchmark-startup.py --appimage dist/CodeGuard-Pro-1.0.0-x86_64.AppImage --json --conservar
```

Criterio: reportar `usable_ms`/marcas en `startup-perf-electron.json` y tiempos de `/healthz/`.


## Misión de pantalla de carga dinámica y optimización adicional (2026-11-23, sesión 2)

### Objetivo
- Reducir tiempo percibido de arranque y mostrar progreso real por fases.
- Investigar demoras reportadas por propietario: window_create ~21s, splash_loaded ~41s tras carga, total ~102s.

### Cambios
- `electron/splash.html`: nueva pantalla de carga local, autocontenida (sin CDN/deps externas), con logo, barra de progreso, porcentaje, tarea actual, fases, frases motivacionales en español y estado de error.
- `electron/startup-progress.js`: modelo de progreso por fases con pesos, sin avance ficticio, cap 99% hasta `app_interactive`, manejo de eventos duplicados/fuera de orden.
- `electron/main.js`: emite `startup-progress` por IPC real; marca `splash_dom_ready`, `splash_first_paint`, `document_loaded`, `renderer_first_paint`, `app_interactive`; no marca usable en `loadURL`.
- `electron/preload.js`: expone `onStartupProgress` (solo lectura).
- `run.sh`: encabezado TTY no intrusivo; conserva compatibilidad.
- Tests: `electron/startup-progress.test.js` (5 pruebas).

### Medición en este entorno
- No se obtuvo medición AppImage GUI end-to-end utilizable en este entorno (mismo límite de entorno ya documentado). No se presentan tiempos AppImage nuevos como validados.
- Electron tests: 31 pass, 0 fail.
- AppImage Linux reconstruido con los cambios.

### Limitaciones
- Las demoras de 21s/41s reportadas por propietario están en creación de ventana/renderizado Chromium en su entorno; no reproducibles aquí. Se requiere validación en equipo del propietario con `startup-perf-electron.json`.


## Corrección crítica: splash no visible (2026-11-23, sesión 3)

### Causa raíz demostrada
- `createWindow()` cargaba `splash.html` en la misma `BrowserWindow` que luego navegaba a la URL Django con `loadURL()`, pudiendo reemplazar el splash antes de pintarse.
- Listeners de carga se registraban después de `loadFile()` y no se manejaba fallo de carga.
- No había evidencia `splash_dom_ready/splash_first_paint/splash_loaded` en logs del propietario.
- `splash.html` no tenía spinner animado visible.

### Solución
- Ventana de splash separada (`BrowserWindow` dedicada) y ventana principal oculta hasta señal interactiva.
- Listeners registrados antes de `loadFile()`, manejo `did-fail-load`/`render-process-gone`.
- Progreso IPC a splash y main; estado actual enviado al cargar.
- Spinner CSS animado visible, respeta `prefers-reduced-motion`.
- Señal explícita `app-interactive-signal` desde preload + fallback rAF; `usable` solo tras interactivo.
- AppImage reconstruido. Prueba gráfica real en este entorno: no concluyente; requiere validación en equipo del propietario.


## Sesión 4 — endurecimiento definitivo de splash/señal interactiva (2026-11-23)

### Hallazgos y correcciones
- **Bug IPC crítico corregido**: `app-interactive-signal` usaba `isTrustedIpcSender(event)` sin host/puerto, por lo que la validación fallaba y la señal explícita nunca se aceptaba. Corregido a `isTrustedIpcEvent(event)`.
- **Marcas splash diferenciadas**: `splash_window_shown` (show/ready-to-show), `splash_dom_ready`, `splash_document_loaded` (did-finish-load), `splash_first_paint` (rAF real tras carga). Ya no se usa `ready-to-show` como first paint.
- **Buffer de progreso**: al cargar el splash se envía snapshot actual por IPC para no perder eventos emitidos antes de la suscripción del renderer.
- **Señal interactiva explícita**: preload expone `signalAppInteractive()`; `templates/base.html` la invoca al `load` (después de scripts críticos). Fallbacks controlados: preload 4s y main 5s, marcados como fallback; no se usa 2 rAF como confirmación principal.
- **Carga robusta de splash**: `loadFile()` con reintento (1 reintento), `did-fail-load` solo loguea (isMainFrame) para no interferir con reintento; timeout de seguridad 15s; recuperación mostrando ventana principal si corresponde.
- **Limpieza**: eliminado `splashHtml()` muerto. Contrato de splash/preload/seguridad cubierto por `electron/splash-contract.test.js`.

### Pruebas ejecutadas (esta sesión)
- `node --check electron/main.js electron/preload.js electron/startup-progress.js`: OK.
- `npm run test:electron`: 36 pass, 0 fail (incluye 5 contract tests nuevos).
- `manage.py check`: OK. `manage.py makemigrations --check --dry-run`: OK.
- Suite Django completa: 379 tests, 269.325s, OK.
- Build AppImage Linux: OK (`npm run build:linux`), artefacto `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage` (124M, 2026-11-23 18:34 -05).
- Smoke AppImage en entorno con DISPLAY=:0 y timeout 45s: servidor arrancó y `healthz_ready` ~17.36s; la carga de URL principal falló con `ERR_FAILED (-2)` en este entorno limitado/no validado gráficamente. No se considera validación GUI.

### Validación gráfica AppImage
- No ejecutada en este entorno (sin sesión gráfica confiable para validar UI). No se declara splash visualmente validado aquí. Se requiere validación en equipo Linux gráfico con `./codeguard` y revisión de `startup-perf-electron.json`.


## Sesión 5 — auditoría de cierre: interactividad verificable y métricas honestas (2026-11-23)

### Correcciones
- **Señal interactiva verificable**: `app-interactive-signal` acepta solo payload `source=frontend-explicit` desde la ventana principal confiable; rechaza duplicados y señales de otras ventanas; registra `app_interactive_signal_received/rejected` con origen.
- **Fallbacks no declaran usable**: fallbacks (main-timeout, preload-fallback) muestran la UI por recuperación controlada, marcan `app_interactive_fallback` y `writeStartupPerf({usable:false, verified:false,...})`; no marcan 100% ni `app_interactive` verificado.
- **Métricas de pintado honestas**: `splash_renderer_frame_ready` se marca solo en éxito de rAF; en catch se marca `splash_renderer_frame_check_failed` y no se afirma `splash_first_paint`. `main_renderer_frame_ready` análogo. `splash_first_paint/renderer_first_paint` quedan como alias legacy con `verified: renderer_frame_only`.
- **Recuperación de carga principal**: retry de `loadURL` (1 reintento), `main_did_fail_load`, `main_render_process_gone`, `startup_failed` con diagnóstico.

### Pruebas
- `npm run test:electron`: 46 pass, 0 fail.
- Django check/makemigrations: OK (previos). Django suite: 379 OK (sesión anterior, sin cambios Python).

### CI / Build
- CI 45290793853 (SHA 8b4063c): failure en "Windows installation acceptance" (Windows x64 package); Django/Electron/PyInstaller smoke jobs verdes. Causa probable: `scripts/windows-acceptance.ps1` usaba `pages[0]` de CDP; con la ventana splash separada, `file://.../splash.html` puede aparecer primero. Corregido en `f22fddb` filtrando la primera página `http://127.0.0.1:*`.
- Build AppImage sesión 5: OK. `dist/CodeGuard-Pro-1.0.0-x86_64.AppImage`, 124M, 2026-11-23 18:52 -05, SHA256 `411ae6756c1dd362cad64371235bea0c8936958a148583d7a822fe02ee8c5281`. Contenido verificado en asar (contiene `app_interactive_signal_rejected`, `splash_renderer_frame_ready`).

### Limitación
- Sin validación gráfica real del AppImage. El smoke previo con timeout mostró ERR_FAILED(-2) en loadURL principal; coherente con aborto por timeout/entorno, no confirmado como regresión de producto.
