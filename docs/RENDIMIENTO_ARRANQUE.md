# Rendimiento del arranque

**Fecha:** 2026-11-21
**Objetivo:** arranque normal ≤10 s y primer arranque con perfil vacío ≤30 s,
sin bloqueos silenciosos de dos minutos.

## 1. Diagnóstico inicial

Se midieron por separado las fases del servidor con un perfil temporal:

| Fase | Tiempo medido |
|---|---|
| Importar Django | ~0,01 s |
| `django.setup()` | ~0,49 s |
| `migrate` con 46 migraciones | ~4,0 s |
| `cargar_ascenso` (1ª vez) | ~3,5 s |
| `migrate` sin cambios | ~0,13 s |
| **`cargar_ascenso` en cada arranque** | **~3,4 s** |

`cargar_ascenso` ejecutaba `update_or_create` para 33 etapas, 212 módulos,
1.946 lecciones, criterios y prerrequisitos. En discos lentos, antivirus o
equipos con poca memoria, esas ~4.000 consultas podían explicar esperas de
decenas de segundos. Electron además esperaba hasta 120 s sin mostrar el estado
real.

## 2. Cambios aplicados

### 2.1 Verificación idempotente (`apps/roadmaps/bootstrap.py`)

- Lee y valida el manifiesto distribuido.
- Calcula una huella SHA-256 del JSON y una huella canónica del contenido.
- Consulta etapas, módulos, lecciones, criterios y prerrequisitos en bloque.
- Compara la huella real de SQLite con la esperada.
- Solo llama a `cargar_ascenso` si falta contenido, cambió el manifiesto o la
  huella no coincide.
- Persiste `EstadoInstalacionRoadmap` con hashes, recuentos y filas sobrantes.
- Conserva filas históricas y progreso; no borra intentos, evidencias ni
  preferencias.

La verificación normal usa **7 consultas** y no modifica la base si todo
coincide.

### 2.2 Migraciones

Se inspecciona el plan de migraciones con `MigrationExecutor`. Si no hay
pendientes, no se invoca `migrate`; si las hay, se aplican antes de verificar el
roadmap. Esto evita el coste de arranque de una operación innecesaria sin
saltarse actualizaciones reales.

### 2.3 Perfil limpio

El arranque crea un propietario local sin credenciales cuando `AUTH_DISABLED`
está activo y no existe ningún usuario. Así el perfil limpio puede guardar
progreso sin reactivar el login.

### 2.4 Electron

- El splash muestra las fases reales (`database`, `profile`, `roadmap`,
  `ready`) emitidas por el servidor.
- La espera de salud tiene un límite configurable
  (`CODEGUARD_STARTUP_TIMEOUT_MS`, 90 s por defecto) y muestra el estado del
  health check.
- Si el proceso hijo termina, se detecta de inmediato y se muestra el último
  error del servidor.
- `npm start` usa `server_entry.py`, el mismo punto de entrada que el paquete,
  por lo que un perfil limpio también funciona en desarrollo.

## 3. Resultados reproducibles

### Medición de la auditoría final (commit `24d04b6`)

```
primer_arranque: interno 8.706 ms · pared 9.650 ms · 54 migraciones · roadmap cargado
segundo_arranque: interno 144 ms · pared 901 ms · 1.946 lecciones reutilizadas
perfil_con_historial: interno 129 ms · pared 813 ms
```

La mejora respecto de la medición anterior se explica por el estado del host y
por no reconstruir el roadmap. Es una medición local; no se extrapola a otros
equipos.

### Medición previa de la base

```bash
.venv/bin/python scripts/benchmark-startup.py
```

Salida en la máquina de referencia (Linux x64, 7,4 GB RAM, carga alta):

```
primer_arranque: interno 13.125 ms · pared 15.157 ms · 52 migraciones · roadmap cargado · 8 contenidos sembrados
segundo_arranque: interno 145 ms · pared 983 ms · roadmap reutilizado · 1.946 lecciones
perfil_con_historial: interno 152 ms · pared 920 ms · roadmap reutilizado
```

Servidor PyInstaller empaquetado:

```
RUN 1 (perfil vacío, con siembra académica): ~15.2 s hasta /healthz/ OK
RUN 2 (perfil existente): ~1.0 s hasta /healthz/ OK
```

AppImage con datos existentes (extraído; el montaje FUSE de este host se
bloqueó, ver limitaciones):

```
[Startup] Servidor Django listo en ~2.1 s
[Startup] Aplicación lista en ~3.1 s
```

## 4. Antes y después

| Métrica | Antes | Después |
|---|---|---|
| Reconstrucción del roadmap en arranque normal | Sí, ~3,4 s | No |
| Consultas en arranque normal | ~4.000+ | 7 |
| Verificación de integridad | No existía | Sí, 0,08–0,30 s |
| Servidor empaquetado, segundo arranque | ~4,0 s | ~1,0–1,2 s |
| Electron, segundo arranque | No medido | ~2,8–3,1 s |
| Espera máxima silenciosa | 120 s | 90 s con estado visible |

## 5. Pruebas de regresión

- `apps.roadmaps.tests.test_bootstrap`:
  - segundo arranque no llama a `cargar_ascenso`;
  - límite de 7 consultas;
  - tiempo de verificación <1 s para el manifiesto de prueba;
  - detección de lección alterada, manifiesto nuevo y perfil incompleto;
  - conservación de progreso;
  - no invoca `migrate` si no hay pendientes.
- `electron/startup-status.test.js`: parser de eventos, mensajes, timeout
  acotado y descripción del health check.
- `scripts/benchmark-startup.py`: falla si se superan los objetivos.
- CI ejecuta el benchmark y la suite completa.

## 6. Limitaciones

- El primer arranque sigue pagando migraciones y siembra inicial; es inevitable
  en un perfil vacío.
- El montaje FUSE del AppImage se bloqueó en el host de pruebas con el artefacto
  nuevo y con el anterior. Se verificó con extracción y se documentó
  `CODEGUARD_APPIMAGE_EXTRACT=1 ./run.sh`. En un equipo normal debería usarse el
  montaje directo.
- Los objetivos se midieron en la máquina indicada; hardware más lento debe
  compararse con el mismo benchmark, no con una impresión subjetiva.
