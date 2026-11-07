# CodeGuard Pro — Modelo de datos

**Producto:** CodeGuard Pro  
**Versión:** 1.1 (Incrementos 1–2)
**SRS de referencia:** `IEEE830.md` v2.2 — Sección 3.4 (RD-001 a RD-022)

---

## 1. Entidades del primer incremento

Las entidades modeladas en el incremento 1 (núcleo funcional) son:

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

## 3. Entidades planificadas (incrementos futuros)

Según RD-004 a RD-022 del SRS, se modelarán en los siguientes incrementos:

- **Académico:** Roadmap, Etapa, Modulo, Leccion, Actividad, Prerrequisito, CriterioFinalizacion, Progreso.
- **Competencias:** Competencia, NivelDominio, CriterioEvaluacion, RequisitoEvidencia, ReglaFinalizacion, LogroCompetencia.
- **Evaluacion:** Evaluacion, Pregunta, Opcion, Intento, Resultado, Retroalimentacion, Rubrica.
- **Documental:** Documento, Metadato, FragmentoDocumental, IndiceFTS5, ErrorImportacion.
- **Conocimiento:** Concepto, RelacionConcepto, VínculoConceptoFragmento, VínculoConceptoActividad.
- **Evidencias:** Evidencia, ArchivoEvidencia, HashSHA256.
- **Laboratorios:** Laboratorio, Paso, Comando, Resultado, Captura.
- **Vigencia:** Revision, DecisionRevision.
- **Backups:** BackupOperacion, HashBackup.
- **Configuracion:** ParametroSistema.

Ver `docs/MATRIZ_TRAZABILIDAD.md` para el mapeo requisito → entidad.

---

## 4. Índices y claves únicas (incremento 1)

| Tabla | Índice / Único | Propósito |
|---|---|---|
| audit_log | (evento, creado_en) | Consultas de auditoría por evento y fecha |
| audit_log | (usuario, creado_en) | Historial de eventos por usuario |
| frase_rescate | (usuario, creada_en desc) | Última frase por usuario |
| configuracion_sistema | pk=1 | Singleton |

---

## 5. Integridad referencial

Todas las claves foráneas usan `on_delete` apropiado (`CASCADE` o `SET_NULL`) para evitar
huérfanos. Se utilizan migraciones de Django y se verifica que aplican desde una base de datos
vacía (RNF-008: integridad transaccional en SQLite).

---

## 6. Crecimiento futuro

El modelo está diseñado para agregar nuevas aplicaciones sin modificar las existentes.
Cada nueva entidad vivirá en su propia app Django con su propia migración, evitando modelos
monolíticos y dependencias circulares.
