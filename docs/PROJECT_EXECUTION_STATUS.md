# Estado de ejecución del proyecto

**Última actualización:** 2026-11-21
**Fase:** finalización 1.0.0 — perfil limpio, rendimiento, biblioteca y entrega
**Rama:** `release/1.0.0-final` (base `release/1.0.0`; sin fusionar)
**PR de finalización:** se publicará al subir la rama; no se fusiona ni se crea tag/release sin autorización.
**Base:** `main` intacta; PR #15 y #16 fuera de alcance.

> Este documento conserva el historial de ejecución. No sustituye los informes
> anteriores de la rama `documentation` ni el informe final
> [`INFORME_FINAL_1.0.0.md`](INFORME_FINAL_1.0.0.md).

## 0. Iteración de finalización (21-11-2026)

### Cambios principales

| Área | Cambio |
|---|---|
| Perfil limpio | Propietario local creado una sola vez sin credenciales; las escrituras dejan de fallar |
| Arranque | Verificación idempotente con huella de manifiesto/contenido; 7 consultas frente a ~4.000 |
| Electron | Splash con fases reales, timeout configurable, detección temprana de errores y `server_entry.py` también en desarrollo |
| CSRF | `Referrer-Policy` pasa de `no-referrer` a `same-origin`; los POST de Electron ya no envían `Origin: null` |
| Biblioteca | Módulo nuevo: importación PDF validada, búsqueda, archivo, visor con rangos HTTP y metadatos |
| Conocimiento | Panel de solo lectura con fuentes, versiones, paquetes y sincronización |
| Navegación | Biblioteca y Base de conocimiento activas; un solo acceso activo por página |
| Dev | Waitress + WhiteNoise en desarrollo; recursos estáticos ya no devuelven 404 |
| Pruebas | 331 Django + 24 Electron + benchmark de arranque en CI |

### Artefactos Linux

- AppImage: `f137bfc900466966f47dffefd319d8f232cbff2fd716080d2db5aff940f9b5c8`.
- Servidor PyInstaller: `7ad9366963b4f69428827b59c71f29c74b76675b4c2d1f11af4ff151c399262d`.

### Evidencia

- Suite Django: **331 pruebas OK**.
- Electron: **24/24 OK**.
- `pip-audit`: sin vulnerabilidades conocidas.
- `npm audit --omit=dev`: 0 vulnerabilidades de producción.
- Primer arranque empaquetado: **12,6 s**; segundo: **1,2 s** de servidor y
  **~2,5 s** con Electron.
- AppImage: 7 rutas 200, 12 temas, formulario PDF real, visor, cierre limpio.
- Backup/restore: base y `media/` restauradas; estado curricular reutilizado.

### Pendientes que no se declaran terminados

- Contenido académico de las 1.946 lecciones (solo títulos estructurales).
- Aceptación física Windows.
- Sincronización remota de producción (sin endpoint/claves).
- macOS/ARM64.
- Laboratorios con sandbox, competencias, vigencia y ética.


## 1. Cambios de esta iteración

| Área | Cambio | Archivos |
|---|---|---|
| Persistencia de tema | El tema se guarda en `ui-preferences.json` dentro del perfil, no solo en `localStorage` (ligado al puerto aleatorio) | `electron/theme-preference.js`, `electron/main.js`, `electron/preload.js`, `static/js/codeguard.js`, `static/js/settings.js` |
| Pruebas de tema | 5 pruebas de lectura/escritura atómica y validación de temas | `electron/theme-preference.test.js` |
| Windows | Aceptación automatizada: instalación NSIS, arranque, health, rutas, tema, progreso, cierre, desinstalación y portable | `scripts/windows-acceptance.ps1`, `scripts/cdp-smoke.js`, `scripts/windows-profile-check.py`, `.github/workflows/ci.yml`, `package.json` |
| Responsive | Verificación CDP sin desbordamiento horizontal a 1024 y 768 px | `scripts/cdp-smoke.js` |
| Roadmap | Corregido el proyecto de la etapa 10 (4.739 → 136 caracteres) y el extractor que absorbía la ampliación | `apps/roadmaps/data/ascenso_3_1.json`, `scripts/extraer_ascenso.py` |
| Roadmap | Regresión para evitar que una ampliación vuelva a contaminar un proyecto | `apps/roadmaps/tests/test_roadmaps.py` |
| Documentación | Inventario de las 33 etapas, fuente DOCX/hash y hallazgos editoriales | `docs/ROADMAP_ASCENSO_INVENTARIO.md` |

## 2. Fuente académica

- DOCX localizado en `/home/mvxbms/Descargas/PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx`.
- SHA-256 `15a9ef38c7284de79eedd1ba10ef33cc50b324c9706836740205778eea4704d3`; coincide con `metadata.sha256_fuente` del JSON.
- No se copió el DOCX al repositorio por contener material del propietario. No se modificó el contenido académico; solo se corrigió la extracción del proyecto de la etapa 10 para que coincida con la frase oficial.
- La etapa 25 no tiene objetivo formal en el DOCX. Se documenta una propuesta sujeta a aprobación; no se publicó.

## 3. Pruebas ejecutadas

| Prueba | Resultado |
|---|---|
| Suite Django (7 apps) | **292 pruebas OK** |
| Pruebas Node/Electron | **20/20 OK** |
| `manage.py check` | 0 incidencias |
| `makemigrations --check --dry-run` | Sin cambios |
| `pip-audit -r requirements.txt` | Sin vulnerabilidades conocidas |
| `npm audit --omit=dev` | 0 vulnerabilidades de producción |
| `npm audit` completo | 6 moderadas, solo cadena de build de electron-builder |
| Smoke PyInstaller Linux | Primer arranque, ASCENSO, health, cierre de puerto y sync OK |
| Persistencia de tema (AppImage, dos arranques) | `fantasy` persiste tras reiniciar el paquete |
| E2E AppImage Linux | 5 rutas HTTP 200, 12 temas, responsive, cierre sin huérfanos |
| Windows CI run `44574923603` y `44576601446` | **7/7 fases OK**: instalación, primer arranque, health, 5 rutas, tema, progreso, desinstalación, portable y ausencia de huérfanos |

### Artefactos Linux

- AppImage: `f137bfc900466966f47dffefd319d8f232cbff2fd716080d2db5aff940f9b5c8`.
- Servidor PyInstaller: `7ad9366963b4f69428827b59c71f29c74b76675b4c2d1f11af4ff151c399262d`.

### Evidencia Windows (CI, no hardware físico)

```
[1/7] Instalación silenciosa: CodeGuard Pro Setup 1.0.0.exe
[2/7] Primer arranque, health check y rutas principales
TITLE=Dashboard V14 — CodeGuard Pro
STATUSES={"/":200,"/roadmaps/":200,"/roadmaps/evaluaciones/":200,"/roadmaps/evidencias/":200,"/backups/":200}
THEMES=12
THEME=fantasy
[3/7] Progreso local y reinicio
SEED_OK
THEME=fantasy
PROGRESS=1
[4/7] Desinstalación silenciosa
[5/7] Ejecutable portable: arranque y health check
[6/7] Comprobación de procesos huérfanos
[7/7] Aceptación Windows completada
```

No se ha probado en un equipo Windows físico ni con hardware real. El runner
`windows-latest` valida el ciclo del instalador y del portable, pero no sustituye
la aceptación manual en un equipo limpio.

## 4. Problemas detectados y corregidos

1. **Tema no persistía entre reinicios:** `localStorage` está separado por origen
   `http://127.0.0.1:<puerto>` y el puerto cambia en cada arranque. Corregido con
   preferencia en el perfil y sincronización IPC.
2. **Proyecto de etapa 10 contaminado:** el extractor no cerraba el marcador de
   proyecto al entrar en `Ampliación de profundidad`. Corregido; el JSON conserva
   prerrequisitos y el resto de campos.
3. **Fallo de siembra en Windows CI:** `python scripts/windows-profile-check.py`
   no encontraba `config`; se añadió la raíz del proyecto a `sys.path`.
4. **Instalador NSIS lanzaba la app automáticamente:** se configuró
   `runAfterFinish: false` para una aceptación determinista.

## 5. Riesgos residuales

- `npm audit` reporta 6 avisos moderados en `electron-builder`/`minimatch`
  (herramientas de build, no runtime). `electron-builder` 26.18.0 es la última
  versión y `npm audit fix --force` propone una degradación, no una corrección.
  No se fuerza un override no verificado.
- Etapa 25 sin objetivo formal en la fuente. Requiere decisión editorial.
- 1.946 lecciones son títulos estructurales; no hay cuerpos de lección,
  ejercicios ni quizzes publicados en un perfil limpio.
- Windows validado en CI, no en hardware físico.

## 6. Pendientes

1. Revisar y aprobar el inventario académico; decidir etapa 25 y alcance cursable.
2. Aceptación manual en un equipo Windows limpio (hardware real).
3. Sincronización remota de producción, macOS/ARM64 y contenido académico completo:
   fuera del alcance de este RC.

## 7. Artefactos finales

- Servidor PyInstaller: `c21ff228b40fab302a8081532e227feb3efe54a16194d19b7bbf667f7e84ea53`.
- AppImage: `3e14314636be75a44665846a0f1a25972352cb847dadbe407d84a9fd11a7f05d`.
- CI push `e4599aa`: run `44576601446`, **4/4 jobs verdes**.

## 8. Próximos pasos

- Actualizar PR #13 y `documentation` con esta evidencia.
- No fusionar ni crear release/tag sin autorización.
