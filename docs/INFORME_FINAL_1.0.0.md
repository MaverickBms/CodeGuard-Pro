# CodeGuard Pro 1.0.0 — informe de finalización

**Fecha:** 2026-11-21
**Rama:** `release/1.0.0-final` (base: `release/1.0.0`)
**Commit de código auditado:** `24d04b6`
**PR:** [#17](https://github.com/MaverickBms/CodeGuard-Pro/pull/17) — abierto, sin fusionar
**Alcance:** plataforma educativa local (Electron + Django + SQLite).
**Fuera de alcance:** Mundo CodeGuard, PR #15 y PR #16.

> Los documentos de esta carpeta describen el estado real de esta rama. Las
> comprobaciones no ejecutadas se indican como pendientes. No se copian cifras
> de iteraciones anteriores sin verificarlas.

## 1. Resultado ejecutivo

CodeGuard Pro 1.0.0 es una plataforma educativa local, offline-first y
monousuario que arranca en un perfil limpio, aplica migraciones, crea un
propietario local explícito, instala ASCENSO 3.1 y permite estudiar 8 lecciones
reales con ejercicios deterministas, progreso persistente, biblioteca PDF,
tutor local con fallback, gamificación, espacio editorial y backups verificados.

La auditoría final corrigió dos defectos de integridad relevantes:

1. **Identidad local:** ya no se eleva la primera cuenta activa. El propietario
   se marca explícitamente y un perfil ambiguo falla cerrado.
2. **Progreso:** una etapa aprobada ya no se revierte al recalcular lecciones.

También se separó la verificación técnica de videos de su revisión pedagógica,
se conservaron los formularios editoriales inválidos y se corrigió el CI para
que el PR de release ejecute los workflows.

## 2. Estado verificado

| Área | Resultado |
|---|---|
| Backend Django | 356 pruebas OK; `check` sin incidencias; migraciones al día |
| Electron | 26/26 pruebas OK; IPC, cierre y tema persistentes |
| Frontend | 9 rutas HTTP 200; 12 temas; 13 pantallas responsive |
| Roadmap | 33 etapas, 212 módulos, 1.946 títulos, 7 prerrequisitos |
| Contenido | 8 lecciones, 8 ejemplos, 16 ejercicios, 13 fuentes, 8 videos |
| Cobertura | 8 desarrolladas en borrador; 0 aprobadas; 0 publicadas; 1.938 pendientes |
| Aprendizaje | Lección completada por ejercicio; persiste tras reiniciar |
| Biblioteca | PDF importado, visor, archivo y persistencia |
| Backups | Crear, verificar y restaurar en perfil aislado con datos comprobados |
| Tutor | Ollama local y fallback determinista; límite de 3 pistas |
| Seguridad | Sin vulnerabilidades críticas/altas conocidas en el alcance local |
| Linux | AppImage y servidor PyInstaller actuales verificados |
| Windows | CI 4/4 sobre `29b836f` (`24d04b6`); hardware físico pendiente |
| macOS/ARM64 | No soportados ni validados |

## 3. Cambios de esta auditoría

### 3.1 Identidad y permisos

- Nueva marca persistente `Usuario.es_propietario_local`.
- Migración `accounts.0003_usuario_es_propietario_local`.
- El nombre reservado heredado `propietario-local` se reconoce explícitamente.
- Varias cuentas sin propietario inequívoco: no se elige ni se eleva ninguna.
- La siembra de contenido ya no convierte cuentas en staff.
- Pruebas de cuenta ordinaria, perfil ambiguo y nombre heredado.

### 3.2 Progreso

- `recalcular_progreso_etapa` no revoca una etapa completada.
- Regresión añadida en `test_roadmaps`.

### 3.3 Editorial y contenido

- Formularios inválidos conservan texto y errores.
- Videos separan `estado_revision` (enlace/metadatos) de `estado_pedagogico`.
- La aprobación pedagógica exige enlace verificado, fecha, actor y notas.
- Los 8 videos quedan con revisión pedagógica **pendiente**.
- Se rechazan URLs `http://` en videos.
- Migración `roadmaps.0022_recursoaudiovisual_revision_pedagogica`.

### 3.4 Seguridad y CI

- Validación completa de contraseña en el setup conservado.
- CI se ejecuta en PR contra `release/1.0.0` y `release/**`.
- Windows se ejecuta también en push a `release/1.0.0-final`.
- `pip-audit` y `npm audit --omit=dev` añadidos al CI.
- Opciones futuras de navegación etiquetadas como no disponibles.
- `transition: all` sustituido por propiedades concretas.
- Prevención de envíos duplicados en formularios.

## 4. Pruebas

La matriz detallada está en [`MATRIZ_PRUEBAS_1.0.0.md`](MATRIZ_PRUEBAS_1.0.0.md).

### Backend

```bash
CODEGUARD_DATA_DIR=/tmp/cg-audit .venv/bin/python manage.py check --settings=config.settings.development
CODEGUARD_DATA_DIR=/tmp/cg-audit .venv/bin/python manage.py makemigrations --check --dry-run --settings=config.settings.development
CODEGUARD_DATA_DIR=/tmp/cg-audit .venv/bin/python manage.py test --settings=config.settings.development --parallel 1
```

Resultado: **356 pruebas OK** en 131 s; migraciones sin cambios.

### Electron y UI

```bash
npm run test:electron                 # 26/26 OK
node scripts/cdp-smoke.js "$WS" basic # 9 rutas 200, 12 temas
node scripts/cdp-form-smoke.js "$WS"  # PDF real, visor, archivo
node scripts/cdp-responsive.js "$WS"  # BAD=[]
```

### Aprendizaje y persistencia

- Lección 1 respondida correctamente: `{"ok":true,"done":true,"attempts":1}`.
- Tras reiniciar: `{"completed":true,"attempt":true,"score":true}`.
- Tema `fantasy` persiste en `ui-preferences.json` tras reiniciar.

### Backup y restauración

- Backup de 2 archivos y 1.511.679 bytes.
- SHA-256 del ZIP de prueba:
  `e592c07ce392da8c635d2885341c8c7755485ebfc917ddc0980817746d6f2753`.
- Restaurado en perfil aislado; progreso, intento y documento archivado
  recuperados.

### Dependencias

```text
pip-audit: sin vulnerabilidades conocidas
npm audit --omit=dev: 0 vulnerabilidades
npm audit completo: 6 moderadas (build de electron-builder), 0 altas/críticas
```

## 5. Rendimiento

`python scripts/benchmark-startup.py`:

| Escenario | Medición local |
|---|---|
| Primer arranque | 8,7 s interno / 9,6 s pared |
| Segundo arranque | 144 ms interno / 901 ms pared |
| Perfil con historial | 129 ms interno / 813 ms pared |

Los objetivos (≤10 s normal, ≤30 s primer arranque) se cumplen en este host. No
se extrapolan a hardware más lento sin repetir el benchmark.

## 6. Contenido académico

| Indicador | Valor |
|---|---:|
| Etapas | 33 |
| Módulos | 212 |
| Títulos | 1.946 |
| Lecciones con cuerpo | 8 |
| Versiones borrador | 8 |
| Aprobadas | 0 |
| Publicadas | 0 |
| Pendientes | 1.938 |
| Ejemplos | 8 |
| Ejercicios | 16 |
| Fuentes únicas | 13 |
| Referencias | 16 |
| Videos con enlace verificado | 8 |
| Videos con revisión pedagógica aprobada | 0 |

El detalle está en [`CONTENIDO_ACADEMICO.md`](CONTENIDO_ACADEMICO.md). Los títulos
no se presentan como lecciones terminadas.

## 7. Artefactos

| Artefacto | Plataforma | Tamaño | SHA-256 | Commit |
|---|---|---:|---|---|
| `CodeGuard-Pro-1.0.0-x86_64.AppImage` | Linux x64 | 129.372.879 B | `7ca64d4e46787aee17cd839d162c965ba549f4f280809a8ca7d4eac915c28202` | `24d04b6` |
| `CodeGuardServer` | Linux x64 | 7.798.232 B | `6080dc8ca8ed731ecdfe38c84e0906eadfce6dd2b6838036911577479ec3d4a5` | `24d04b6` |
| `codeguard-windows-x64.zip` (artefacto CI) | Windows x64 | 275.098.534 B | `da2fda5aa7878f51fb142a74d1076ea1416991ae3ddb0c23ee7bb78cbe02463a` | `29b836f` |
| Instalador NSIS | Windows x64 | 146.505.176 B | `1c814266baa25028a579ed5f7296b9e91ca709867d86d360520679f94a78117b` | `29b836f` |
| Portable | Windows x64 | 129.364.031 B | `52b1d3d8dd0548edd82bbf2feb67397c84619283a1a6aef837223b8a70497be9` | `29b836f` |

El AppImage actual se ejecutó con `APPIMAGE_EXTRACT_AND_RUN=1` porque el montaje
FUSE de este host permanece bloqueado. No se reutilizan hashes antiguos.

Windows: el CI construyó y verificó los artefactos; los hashes se calcularon
descargando el artefacto del run `44952905523`. **No están firmados
digitalmente** (el log de CI indica que no hay certificado de firma), por lo que
Windows SmartScreen puede advertir. No hay aceptación física en hardware
Windows.

## 8. Seguridad

Resumen: [`SEGURIDAD_1.0.0.md`](SEGURIDAD_1.0.0.md).

- Servidor solo en `127.0.0.1`.
- CSRF, CSP, cabeceras y cookies endurecidas.
- Propietario local explícito y permisos editoriales limitados.
- Uploads PDF validados por extensión, firma, tamaño y SHA-256.
- Visor restringido a `MEDIA_ROOT` y rangos HTTP.
- Electron con context isolation, sandbox, IPC por origen exacto y navegación
  restringida.
- Backups con hashes, validación de rutas, SQLite y rollback.
- Tutor solo loopback y sin redirecciones.
- Sync remota falla cerrada sin configuración.

## 9. Limitaciones

Detalle: [`LIMITACIONES_1.0.0.md`](LIMITACIONES_1.0.0.md).

1. 1.938 lecciones sin cuerpo.
2. 8 lecciones en borrador; 0 publicadas.
3. 0 videos con revisión pedagógica aprobada.
4. Sin sandbox de ejecución de código.
5. Sin interfaz docente para resolver respuestas abiertas.
6. Windows físico pendiente.
7. macOS y ARM64 no soportados.
8. Sincronización remota de producción no configurada.
9. AppImage no probado con montaje FUSE directo en este host.
10. Artefactos sin firma de código de producción (Windows/Linux).
11. No se fusionó el PR ni se creó tag/release.

## 10. Estado del PR y veredicto

- Rama: `release/1.0.0-final`, publicada en `origin`.
- PR #17: abierto, contra `release/1.0.0`, sin fusionar.
- PR #15 y #16: intactos y fuera de alcance.
- CI: run `44952905523` (push) y `44952910842` (PR) verdes sobre `29b836f/24d04b6`, 4/4 jobs.
- No se creó etiqueta ni release definitiva.

**Veredicto: LISTO CON LIMITACIONES DOCUMENTADAS.**

La aplicación funciona dentro del alcance local definido y no tiene bloqueos
críticos conocidos. No se declara aceptación física de Windows ni cobertura
académica completa. La entrega es honesta sobre lo que falta y deja el PR
preparado para revisión, sin fusionarlo.
