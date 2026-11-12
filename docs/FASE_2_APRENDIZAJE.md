# Fase 2 — Sistema de aprendizaje interactivo

**Producto:** CodeGuard Pro  
**Estado:** Motor de aprendizaje y control editorial en desarrollo (rama `docs/phase-2-hybrid-knowledge-sync`, fusionada a `main`)  
**Línea base:** rama `main`  
**Documentos de referencia:** `docs/PLAN_DESARROLLO.md`, `docs/ARQUITECTURA.md`, `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md`, `docs/MODELO_DATOS.md`

---

## 1. Objetivo

Convertir cada lección del Roadmap ASCENSO en una unidad de estudio navegable y estructurada, sin confundir la existencia de una ficha académica con el dominio demostrado del contenido.

---

## 2. Alcance implementado (Fase 2, en `main`)

La rama `docs/phase-2-hybrid-knowledge-sync` fue fusionada a `main`. Incluye:

- **Roadmap ASCENSO 3.1:** 33 etapas (0 a 32) con bloques, secciones, prioridades, objetivos, proyectos y prerrequisitos. Cargable con `python manage.py cargar_ascenso`.
- **Estructura curricular relacional:** `Roadmap`, `Etapa`, `Modulo`, `Leccion`, `Prerrequisito`.
- **Contenido académico editable:** `ContenidoLeccion`, `EjemploLeccion`, `EjercicioLeccion` con teoría, ejemplos, ejercicios, estado de publicación y evaluadores.
- **Claves UUID estables:** `clave_contenido` en `Leccion`, `EjemploLeccion`, `EjercicioLeccion` (migración 0004).
- **Catálogo de fuentes documentales:** `FuenteConocimiento` (migración 0005).
- **Snapshots inmutables de versión de lección:** `VersionContenidoLeccion` con flujo editorial (`borrador → revisión → aprobada → publicada → sustituida → retirada`), snapshot JSON, SHA-256, metadatos de auditoría (migración 0005).
- **Referencias de fuente por versión:** `ReferenciaFuenteContenido` (migración 0005).
- **Auditoría editorial:** envío a revisión, aprobación, publicación, sustitución y retirada (migraciones 0006–0008).
- **Revisión de licencias de fuentes:** estados `compatible`, `solo_referencia`, `requiere_permiso`, `no_reutilizable` (migraciones 0009–0010).
- **Autoría de versiones:** `VersionContenidoLeccion.autoria` (migración 0011).
- **Registro local de paquetes de conocimiento:** `PaqueteConocimientoInstalado` con transiciones controladas, identidad inmutable, un solo activo por canal, secuencia única por canal (migración 0012).
- **Un solo paquete activo por canal:** restricción parcial y migración de datos (migración 0013).
- **Estado de sincronización por canal:** `EstadoSincronizacion` (migración 0012).
- **Verificador de distribución firmada:** `validate_package_archive`, `verify_signed_manifest` (Ed25519, manifiesto, ZIP).
- **Contenido activo por snapshot:** `ContenidoLeccionActivo` apunta a la versión editorial publicada que debe mostrarse; la publicación y retirada actualizan el puntero dentro de la transacción editorial (migración 0014).
- **Evidencia histórica de ejercicios:** cada nuevo `IntentoEjercicio` conserva `snapshot_ejercicio` y referencia `version_contenido` cuando existe una versión activa. La migración 0014 conserva el enunciado visible de intentos anteriores. La evidencia original queda protegida frente a cambios y borrados ORM.
- **Interfaz de entregas:** el estudiante ya puede enviar respuestas mediante POST con CSRF, límite de 20.000 caracteres e historial de los tres últimos intentos. No se ejecuta código arbitrario.
- **Registro local endurecido:** escrituras masivas de paquetes y estado de sincronización validan invariantes o quedan bloqueadas para evitar saltarse el flujo controlado.
- **Comandos de gestión:** `cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`, `publicar_paquete_conocimiento` y el nuevo `sincronizar_conocimiento` (cliente HTTP, en rama aislada), con scheduler Electron y backoff implementados y pruebas unitarias locales satisfactorias; build PyInstaller e integración Electron pendientes.
- **Validación de la línea base:** el propietario confirmó 119 pruebas OK, `manage.py check` sin errores y `makemigrations --check --dry-run` sin cambios pendientes en `main` `2c5d441`. La validación local cubre el instalador transaccional y rollback.

---

## 3. Modelo de datos

Ver `docs/MODELO_DATOS.md` (sección 3: entidades académicas de la Fase 2; sección 4: entidades de conocimiento versionado y sincronización).

---

## 4. Flujo editorial

Ver `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` (secciones 8: publicador central; 21: flujo editorial controlado; 22: comandos de gestión; 23: registro de fuentes).

---

## 5. Sincronización híbrida de conocimiento

Ver `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` (secciones 1–7: diseño de sincronización y contrato del paquete; 9: flujo editorial y de sincronización; 10: infraestructura de distribución central; 11: estrategia de migración; 12: invariantes obligatorias).

---

## 6. Publicador central local y catálogo firmado (validados localmente)

Se añadió el módulo apps/roadmaps/publisher.py, el comando publicar_paquete_conocimiento y el registro inmutable de publicaciones (migración 0015_publicador_central_conocimiento). El generador toma únicamente versiones editoriales publicadas señaladas por ContenidoLeccionActivo, verifica hash e identidad curricular, y bloquea fuentes inactivas, licencias no autorizadas o decisiones de licencia modificadas después de la revisión.

Genera ZIP reproducible por secuencia, índice interno, manifiesto externo y firma Ed25519. La clave privada PEM se carga desde una ruta externa al repositorio, exige permisos POSIX restrictivos y no se guarda en SQLite ni en Git. La secuencia se mantiene por canal (stable/beta) y el registro de publicaciones es inmutable. El comando escribe artefactos localmente; no sube archivos ni crea endpoints.

El contrato de paquete v2 incluye un catálogo normalizado de fuentes con datos bibliográficos, decisión y evidencia de licencia, alcance y fecha de revisión. El verificador conserva compatibilidad con índice v1. No se exporta la identidad personal del revisor.

## 7. Pendiente (no implementado)

| Elemento | Estado | Documento |
|---|---|---|
| Cliente de sincronización de red | Cliente HTTP validado localmente por el propietario dentro de 132 pruebas; scheduler Electron y backoff implementados; pruebas unitarias locales satisfactorias. Build PyInstaller e integración Electron pendientes. Endpoint y claves de producción no configurados | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Generador local y catálogo firmado v2 | Implementado; migración 0015 y pruebas confirmadas por el propietario. Hosting y publicación remota pendientes | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Instalación transaccional local y rollback | Validada por el propietario en `main` `2c5d441` (119 pruebas OK; migración 0016 incluida) | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Competencias y evaluaciones | Pendiente (Incremento 3) | `docs/PLAN_DESARROLLO.md` |
| Biblioteca documental | Pendiente (Incremento 4) | `docs/PLAN_DESARROLLO.md` |
| Evidencias y laboratorios | Pendiente (Incremento 5) | `docs/PLAN_DESARROLLO.md` |
| Backups y administración | Pendiente (Incremento 6) | `docs/PLAN_DESARROLLO.md` |

---


### 7.1 Cliente HTTP pull-only (implementación inicial en rama aislada)

El módulo `apps/roadmaps/sync_client.py` realiza GET HTTPS al manifiesto, firma y ZIP. Verifica el manifiesto Ed25519 y su compatibilidad antes de descargar el paquete; el ZIP se entrega al instalador ya validado en `main`. Se aplican allowlist de hosts, TLS validado, rechazo de redirecciones, timeout y límites de bytes, ETag y verificación del tamaño/hash. No se envían datos del estudiante.

El comando manual es `python manage.py sincronizar_conocimiento --channel stable`. Requiere URLs, allowlist y claves públicas confiables mediante variables de entorno. El scheduler Electron consulta localmente cada cinco minutos, pero el cliente solo realiza red cuando vence `next_check_after`; la primera comprobación se difiere 30 segundos y los fallos aplican backoff de 15 minutos hasta 24 horas. La ejecución empaquetada utiliza `CodeGuardServer --sync-knowledge`, sin iniciar Waitress ni migraciones. Las pruebas unitarias posteriores de backoff y bloqueo fueron confirmadas como satisfactorias por el propietario; todavía falta compilar PyInstaller y ejecutar la integración empaquetada con Electron. No se ha elegido proveedor ni publicado un endpoint real.

## 8. Reglas de operación

- El núcleo de CodeGuard sigue ejecutándose localmente mediante Electron + Django + SQLite.
- La sincronización es pull-only: el cliente descarga conocimiento y no transmite datos académicos del estudiante.
- El servidor local escucha únicamente en `127.0.0.1`.
- Django Admin permanece deshabilitado; el flujo editorial se opera mediante comandos de gestión.
- `cargar_ascenso --recrear` nunca debe usarse para actualizar contenido pedagógico (elimina progreso por cascada).

---

## 9. Validación

El propietario confirmó 119 pruebas OK, `manage.py check` sin errores y `makemigrations --check --dry-run` sin cambios pendientes en `main` `2c5d441`; esa validación incluye el catálogo v2 y el instalador transaccional.

Desde la carpeta local del proyecto:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps
```

Luego iniciar CodeGuard Pro con `./run.sh`, abrir una etapa y entrar en una lección.

### Catálogo de fuentes de distribución (índice v2)

El índice del paquete firmado incorpora un catálogo normalizado de fuentes con UUID, datos bibliográficos, decisión/evidencia/alcance de licencia y fecha de revisión. Se excluye la identidad personal del revisor. El verificador admite índices v1 anteriores y valida estrictamente v2, incluida la correspondencia exacta entre fuentes declaradas y referencias de las lecciones. El instalador conserva el catálogo firmado en `FuentePaqueteConocimiento`, asociado al paquete. No modifica ni sobrescribe `FuenteConocimiento`, por lo que cada versión instalada mantiene su propio expediente de fuentes.

Las pruebas SRC-001 a SRC-008, PUB-001 a PUB-012 y las pruebas del instalador quedaron incluidas en las 119 pruebas confirmadas en `main`. El propietario confirmó después 132 pruebas OK en la rama del cliente HTTP, que incluyen las pruebas de transporte e integración iniciales. Las pruebas unitarias de backoff y bloqueo entre procesos fueron confirmadas como satisfactorias por el propietario. La ejecución real del binario PyInstaller y la integración con Electron siguen pendientes.

## 10. Instalador transaccional de paquetes (validado en main)

El servicio `apps/roadmaps/installer.py` recibe bytes de manifiesto, firma y ZIP; no realiza descargas HTTP. Verifica Ed25519, canal, versión mínima, secuencia anti-replay, hash y estructura del ZIP antes de persistir datos.

La migración 0016 añade snapshots de lección y catálogo de fuentes asociados al paquete. Estos registros son inmutables y quedan separados de `VersionContenidoLeccion`, `ContenidoLeccionActivo` y `FuenteConocimiento`: instalar una publicación central no crea borradores editoriales ni sobrescribe fuentes locales. La instalación valida que las identidades estables de lecciones, ejemplos y ejercicios correspondan al ASCENSO local.

El artefacto ZIP se conserva bajo `CODEGUARD_DATA_DIR/knowledge-packages/`. La activación se realiza al final de la transacción: el paquete anterior pasa a sustituido, el nuevo queda activo y `EstadoSincronizacion.active_package` cambia en la misma transacción. El rollback reactiva un paquete sustituido conservando artefactos, snapshots, intentos y progreso. El servicio también resuelve la vista de lección y la entrega de ejercicios contra el snapshot del paquete activo.

**Límites actuales:** el cliente HTTP inicial fue validado por el propietario dentro de 132 pruebas. El scheduler Electron, el backoff y el bloqueo de concurrencia ya superaron las pruebas unitarias locales confirmadas por el propietario; el modo PyInstaller requiere compilación real y prueba integrada. No hay endpoint, hosting ni claves públicas de producción; por ello la sincronización automática permanece inactiva hasta configurar una distribución confiable. El guardado del artefacto en disco y la transacción SQLite no son una transacción distribuida; un cierre abrupto puede dejar un archivo huérfano no anunciado.
