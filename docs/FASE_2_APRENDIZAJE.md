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
- **Comandos de gestión editoriales:** `cargar_ascenso`, `crear_version_leccion`, `gestionar_version_leccion`, `importar_paquete_contenido`, `registrar_fuente_conocimiento`, `revisar_licencia_fuente`, `validar_paquete_contenido`.
- **Pruebas base:** 93 pruebas automatizadas confirmadas por el usuario antes de este incremento. Las pruebas nuevas de la migración 0014 siguen pendientes de ejecución local.

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

## 6. Pendiente (no implementado)

| Elemento | Estado | Documento |
|---|---|---|
| Cliente de sincronización de red | Pendiente | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Servicio central de publicación | Pendiente | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Paquetes firmados y publicación real | Pendiente | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Instalación atómica de paquetes y rollback | Pendiente | `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md` |
| Competencias y evaluaciones | Pendiente (Incremento 3) | `docs/PLAN_DESARROLLO.md` |
| Biblioteca documental | Pendiente (Incremento 4) | `docs/PLAN_DESARROLLO.md` |
| Evidencias y laboratorios | Pendiente (Incremento 5) | `docs/PLAN_DESARROLLO.md` |
| Backups y administración | Pendiente (Incremento 6) | `docs/PLAN_DESARROLLO.md` |

---

## 7. Reglas de operación

- El núcleo de CodeGuard sigue ejecutándose localmente mediante Electron + Django + SQLite.
- La sincronización es pull-only: el cliente descarga conocimiento y no transmite datos académicos del estudiante.
- El servidor local escucha únicamente en `127.0.0.1`.
- Django Admin permanece deshabilitado; el flujo editorial se opera mediante comandos de gestión.
- `cargar_ascenso --recrear` nunca debe usarse para actualizar contenido pedagógico (elimina progreso por cascada).

---

## 8. Validación

La migración 0014 y los cambios de esta rama están pendientes de validación local. Las 93 pruebas confirmadas anteriormente corresponden al estado anterior a este incremento; no deben atribuirse a los cambios nuevos. Se añadieron pruebas para snapshots de intentos, activación de versiones y protecciones de escritura masiva.

Desde la carpeta local del proyecto:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py migrate
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps
```

Luego iniciar CodeGuard Pro con `./run.sh`, abrir una etapa y entrar en una lección.