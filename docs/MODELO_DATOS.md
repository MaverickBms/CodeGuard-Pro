# CodeGuard Pro — Modelo de datos

**Producto:** CodeGuard Pro  
**Versión:** 2.0 (Incremento 1 + Fase 2 parcialmente implementada)  
**SRS de referencia:** `IEEE830(1).md` v2.2 — Sección 3.4 (RD-001 a RD-022)  
**Línea base:** `main`; correcciones aisladas en `fix/phase-2-integrity-learning`

---

## 1. Entidades del incremento 1 (núcleo funcional)

Las entidades modeladas en el incremento 1 están implementadas y verificadas:

### Usuario (`apps.accounts.Usuario`)
Extiende `AbstractUser` de Django. Usuario único del sistema (monousuario local).

| Campo | Tipo | Descripción |
|---|---|---|
| username | CharField(150) | Identificador de inicio de sesión |
| password | CharField(128) | Hash Argon2 de la contraseña maestra |
| email | EmailField | Correo opcional |
| email_verificado | BooleanField | Email verificado |
| fecha_configuracion_inicial | DateTimeField | Fecha en que se completó el setup |
| sesion_timeout_minutos | PositiveIntegerField | Tiempo de inactividad antes de expirar (defecto 15) |
| intentos_fallidos | PositiveIntegerField | Intentos fallidos consecutivos |
| bloqueado_hasta | DateTimeField (nulo) | Bloqueado hasta |

Restricciones: `swappable = "AUTH_USER_MODEL"`; solo una instancia esperada (monousuario).

### FraseRescate (`apps.accounts.FraseRescate`)
Frase de rescate de alta entropía (≥128 bits), mostrada una sola vez, hash Argon2, un solo uso.

| Campo | Tipo | Descripción |
|---|---|---|
| usuario | FK → Usuario | Usuario propietario |
| hash_argon2 | TextField | Hash Argon2 de la frase de rescate (nunca texto plano) |
| usada | BooleanField | Indica si ya se utilizó (invalida tras uso) |
| fecha_uso | DateTimeField (nulo) | Fecha en que se usó |
| creada_en | DateTimeField | Fecha de creación |

Cardinalidad: 1 usuario → N frases (histórico), pero solo una no usada activa.

### ConfiguracionSistema (`apps.core.ConfiguracionSistema`)
Configuración global (singleton lógico, pk=1 forzado).

| Campo | Tipo | Descripción |
|---|---|---|
| configuracion_inicial_completada | BooleanField | Indica si se hizo el setup inicial |
| fecha_ultimo_backup | DateTimeField (nulo) | Fecha del último backup realizado |
| version_bd | CharField(16) | Versión del esquema de datos |

### AuditLog (`apps.audit.AuditLog`)
Registro de eventos de seguridad y acceso (RF-005, RS-014).

| Campo | Tipo | Descripción |
|---|---|---|
| usuario | FK → Usuario (nulo) | Usuario relacionado (SET_NULL al borrar) |
| evento | CharField(40) + choices | Tipo de evento (login, logout, setup, cambio_contraseña, uso_frase_rescate, ...) |
| descripcion | TextField | Detalle legible del evento |
| ip | GenericIPAddressField (nulo) | IP de origen |
| user_agent | CharField(512) | User agent del navegador |
| creado_en | DateTimeField | Fecha y hora del evento |

Índices: `(evento, creado_en)`, `(usuario, creado_en)`.

---

## 2. Cardinalidades y restricciones (incremento 1)

| Relación | Cardinalidad | Restricción |
|---|---|---|
| Usuario → FraseRescate | 1:N | `on_delete=CASCADE` |
| Usuario → AuditLog | 1:N | `on_delete=SET_NULL`, nullable |
| ConfiguracionSistema | 1 fila (singleton) | `save()` fuerza pk=1; `delete()` no-op |

---

## 3. Entidades académicas implementadas (Fase 2, rama de trabajo)

Las siguientes entidades ya existen en `apps.roadmaps` y sus migraciones (0001 a 0013):

### Estructura curricular
- **Roadmap:** contenedor raíz de una ruta formativa (ASCENSO 3.1 u otra futura).
- **Etapa:** etapa numerada del roadmap (0 a 32 en ASCENSO 3.1).
- **Modulo:** módulo dentro de una etapa.
- **Leccion:** lección dentro de un módulo, con clave UUID estable (`clave_contenido`).
- **Prerrequisito:** dependencias entre etapas.

### Contenido académico editable
- **ContenidoLeccion:** objetivos de aprendizaje, teoría técnica, explicación sencilla, notas, estado de publicación.
- **EjemploLeccion:** ejemplos guiados con código, lenguaje, salida esperada.
- **EjercicioLeccion:** ejercicios con enunciado, instrucciones, nivel, código inicial, pistas, obligatoriedad.
- **Progreso:** registro de progreso del estudiante por lección.

### Evaluación inicial
- **ConfiguracionEvaluacion:** configuración por ejercicio, versiones históricas, una sola activa.
- **IntentoEjercicio:** persistencia de respuesta, resultado, puntuación, retroalimentación, versión de evaluación.

Estas entidades representan la estructura y el primer flujo de contenido/evaluación, pero todavía no implementan fuentes trazables, snapshots inmutables de contenido, paquetes instalados ni sincronización (esas entidades están en la sección 4).

---

## 4. Entidades de conocimiento versionado y sincronización (Fase 2, implementadas en rama)

Las siguientes entidades ya están implementadas en `main` (migraciones 0004 a 0013), con extensión en la rama `fix/phase-2-integrity-learning` (migración 0014):

### FuenteConocimiento
Identificar publicador, URL canónica, licencia y atribución.

| Campo | Tipo | Descripción |
|---|---|---|
| clave | UUID | Identidad estable |
| publicador | CharField | Organización o autor responsable |
| titulo | CharField | Título de la documentación o estándar |
| url_canonica | URLField | URL canónica HTTPS |
| edicion | CharField | Edición o versión |
| identificador_licencia | CharField | Identificador de licencia (SPDX u otro) |
| url_licencia | URLField | URL de condiciones de licencia |
| consultada_en | DateTimeField (nulo) | Fecha de consulta |
| activa | BooleanField | Fuente activa |
| notas | TextField | Notas editoriales |

Restricción única: (`url_canonica`, `edicion`).

### VersionContenidoLeccion
Snapshot inmutable de teoría, ejemplos, ejercicios y evaluadores declarativos.

| Campo | Tipo | Descripción |
|---|---|---|
| clave | UUID | Identidad estable de la versión |
| leccion | FK → Leccion | Lección curricular |
| numero_version | PositiveIntegerField | Número de versión |
| esquema_version | PositiveSmallIntegerField | Versión del esquema |
| estado | CharField | borrador, revisión, aprobada, publicada, sustituida, retirada |
| snapshot | JSONField | Snapshot académico |
| sha256 | CharField(64) | SHA-256 del snapshot |
| resumen_cambios | TextField (nulo) | Resumen de cambios |
| motivo_retiro | TextField (nulo) | Motivo de retiro |
| revisada_en / publicada_en | DateTimeField (nulo) | Fechas de revisión/publicación |
| creada_en | DateTimeField | Fecha de creación |
| enviada_por / revisada_por / publicada_por | FK → Usuario | Responsables de cada transición |

Restricciones: único por (`leccion`, `numero_version`); una sola publicada por lección (restricción parcial condicional).

### ReferenciaFuenteContenido
Registrar qué versión/fragmento de fuente respalda un contenido. N:M entre fuente y versión de contenido.

| Campo | Tipo | Descripción |
|---|---|---|
| version | FK → VersionContenidoLeccion | Versión de contenido |
| fuente | FK → FuenteConocimiento | Fuente registrada |
| rol | CharField | principal, complementaria, normativa |
| localizador | CharField (nulo) | Sección o localizador |
| nota_atribucion | TextField (nulo) | Nota de atribución |

Restricción única: (`version`, `fuente`).

### PaqueteConocimientoInstalado
Registro local de identidad inmutable y transiciones controladas de paquetes.

| Campo | Tipo | Descripción |
|---|---|---|
| package_id | UUID | UUID del paquete |
| package_version | CharField(40) | Versión del paquete |
| channel | CharField(16) | Canal (stable, beta) |
| sequence | PositiveBigIntegerField | Secuencia monotónica |
| content_schema_version | PositiveSmallIntegerField | Versión del esquema |
| sha256 | CharField(64) | SHA-256 del ZIP |
| manifest_sha256 | CharField(64) | SHA-256 del manifiesto |
| signature_key_id | CharField(80) | Identificador de clave de firma |
| published_at | DateTimeField | Publicado el |
| installed_at | DateTimeField (nulo) | Instalado el |
| estado | CharField(16) | descargado, verificado, activo, rechazado, sustituido |
| error_code | CharField(80, nulo) | Código de error |
| creado_en | DateTimeField | Creado el |

Restricciones: único por (`channel`, `sequence`); un solo activo por canal (restricción parcial `estado="activo"`). Transiciones controladas: `descargado → {verificado, rechazado}`, `verificado → {activo, rechazado}`, `activo → {sustituido}`. Identidad inmutable; no se elimina físicamente.

### EstadoSincronizacion
Estado local por canal de sincronización.

| Campo | Tipo | Descripción |
|---|---|---|
| channel | CharField(16, único) | Canal |
| last_check_at | DateTimeField (nulo) | Última comprobación |
| last_success_at | DateTimeField (nulo) | Último éxito |
| manifest_etag | CharField (nulo) | ETag del manifiesto |
| active_package | FK → PaqueteConocimientoInstalado (nulo) | Paquete activo |
| last_error_code | CharField (nulo) | Último error |
| next_check_after | DateTimeField (nulo) | Siguiente comprobación |



### 4.4 Snapshots instalados por paquete (migración 0016)

El contenido distribuido se conserva separado del flujo editorial local.

| Entidad | Campos principales | Invariante |
|---|---|---|
| `ContenidoLeccionPaquete` | paquete, lección, documento JSON, SHA-256 | Un snapshot por paquete/lección; documento y hash inmutables; FK protegidas |
| `FuentePaqueteConocimiento` | paquete, UUID de fuente, metadatos JSON | Catálogo firmado inmutable y aislado de `FuenteConocimiento` |
| `PaqueteConocimientoInstalado.artifact_storage_key` | clave relativa del ZIP en almacén local | Inmutable; no guarda rutas suministradas por el paquete |
| `IntentoEjercicio.paquete_contenido` | FK protegida al paquete presentado | Mutuamente excluyente con `version_contenido`; snapshot de ejercicio exacto |

El instalador resuelve UUID de lección, ejemplo y ejercicio contra el roadmap ASCENSO ya instalado. Los paquetes v2 conservan su catálogo de fuentes dentro de `FuentePaqueteConocimiento`; los paquetes v1 requieren que las fuentes ya estén registradas localmente. Ninguna variante sobrescribe el registro editorial de fuentes.

`EstadoSincronizacion.active_package` es el único selector del paquete distribuido activo por canal. No debe confundirse con `ContenidoLeccionActivo`, que sigue siendo el selector de publicación editorial local. La activación y el rollback cambian el estado de los paquetes y el puntero de sincronización dentro de una transacción SQLite; no eliminan intentos, progreso ni snapshots anteriores.

---

## 5. Entidades previstas para incrementos posteriores

Según RD-004 a RD-022 del SRS y el plan maestro, quedan previstas:

- **Competencias:** Competencia, NivelDominio, CriterioEvaluacion, RequisitoEvidencia, ReglaFinalizacion, LogroCompetencia.
- **Evaluaciones académicas:** Evaluacion, Pregunta, Opcion, Intento, Resultado, Retroalimentacion, Rubrica.
- **Documental:** Documento, Metadato, FragmentoDocumental, IndiceFTS5, ErrorImportacion.
- **Conocimiento semántico:** Concepto, RelacionConcepto, VínculoConceptoFragmento, VínculoConceptoActividad.
- **Evidencias:** Evidencia, ArchivoEvidencia, HashSHA256.
- **Laboratorios:** Laboratorio, Paso, Comando, Resultado, Captura.
- **Vigencia:** Revision, DecisionRevision.
- **Backups:** BackupOperacion, HashBackup.
- **Configuración:** ParametroSistema.

Ver `docs/MATRIZ_TRAZABILIDAD.md` para el mapeo requisito → entidad.

---

## 6. Índices y claves únicas

| Tabla | Índice / Único | Propósito |
|---|---|---|
| audit_log | (evento, creado_en) | Consultas de auditoría por evento y fecha |
| audit_log | (usuario, creado_en) | Historial de eventos por usuario |
| frase_rescate | (usuario, creada_en desc) | Última frase por usuario |
| configuracion_sistema | pk=1 | Singleton |
| fuente_conocimiento | (url_canonica, edicion) | Fuente única por URL y edición |
| version_contenido_leccion | (leccion, numero_version) | Versión única por lección |
| version_contenido_leccion | (leccion) WHERE estado='publicada' | Una sola publicada por lección |
| referencia_fuente_contenido | (version, fuente) | Referencia única versión-fuente |
| paquete_conocimiento_instalado | (channel, sequence) | Secuencia única por canal |
| paquete_conocimiento_instalado | (channel) WHERE estado='activo' | Un solo activo por canal |
| paquete_conocimiento_instalado | (channel, -sequence) | Índice de consulta por canal |
| contenido_leccion_paquete | (paquete, leccion) | Snapshot único por paquete/lección |
| fuente_paquete_conocimiento | (paquete, source_uuid) | Fuente única por paquete |

---

## 7. Integridad referencial

Todas las claves foráneas usan `on_delete` apropiado (`CASCADE`, `PROTECT` o `SET_NULL`) para evitar huérfanos y preservar evidencias históricas. Se utilizan migraciones de Django y se verifica que aplican desde una base de datos vacía (RNF-008: integridad transaccional en SQLite).

Las versiones publicadas y sus referencias se protegen contra borrado (`PROTECT`). Los intentos conservan la versión de contenido y evaluación que los originó.

---

## 8. Crecimiento futuro

El modelo está diseñado para agregar nuevas aplicaciones sin modificar las existentes. Cada nueva entidad vivirá en su propia app Django con su propia migración, evitando modelos monolíticos y dependencias circulares.

---

## 9. Contrato y documentación técnica

El payload, manifiesto, firma Ed25519, hash SHA-256, validación, instalación atómica, rollback y estrategia de migración se especifican en `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md`.

---

## Anexo — Contenido activo y evidencia de intentos (migración 0014)

- `ContenidoLeccionActivo`: relación 1:1 entre una lección y su `VersionContenidoLeccion` actualmente publicada. No copia ni modifica el snapshot; únicamente selecciona cuál debe leer la vista de estudio.
- La publicación editorial actualiza el puntero dentro de la misma transacción que publica la versión. La retirada elimina el puntero después de retirar la versión, sin borrar snapshots ni intentos.
- `IntentoEjercicio.version_contenido`: FK protegida y nullable para conservar compatibilidad con intentos históricos que no pueden asociarse retroactivamente a una versión exacta.
- `IntentoEjercicio.snapshot_ejercicio`: JSON protegido por el modelo que conserva el enunciado, instrucciones, lenguaje, nivel, código inicial, obligatoriedad y clave estable del ejercicio presentado.
- La evidencia original del intento (`ejercicio`, `usuario`, `version_contenido`, `snapshot_ejercicio`, `respuesta`, configuración y versión del evaluador, fecha de creación) no se puede sobrescribir mediante el modelo ni operaciones masivas ORM.
- La migración 0014 rellena snapshots para intentos anteriores con el contenido disponible durante la migración y crea punteros para versiones que ya estaban publicadas. No inventa una FK histórica cuando no hay evidencia suficiente para determinar qué versión vio el estudiante.
- Los modelos validan el puntero y los servicios editoriales controlan su ciclo de vida. Estas protecciones ORM no equivalen a restricciones completas frente a SQL directo.
