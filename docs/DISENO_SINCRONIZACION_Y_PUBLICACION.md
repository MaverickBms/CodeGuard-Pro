# Diseño técnico — Sincronización híbrida y publicador central de conocimiento

**Producto:** CodeGuard Pro  
**Fase:** 2 — Motor de aprendizaje y contenido interactivo  
**Estado:** Diseño aprobado (ADR-004); núcleo de verificación criptográfica y registro local implementado en rama de trabajo. Cliente HTTP, publicación central e instalación atómica siguen pendientes.  
**Fecha:** 12 de noviembre de 2026  
**ADR relacionada:** `docs/ADR/ADR-004-sincronizacion-hibrida-conocimiento.md`  
**Unifica:** `docs/DISENO_DATOS_SINCRONIZACION.md` + `docs/DISENO_PUBLICADOR_CENTRAL.md`

---

## 1. Objetivo y límites

Definir cómo CodeGuard Pro podrá distribuir contenido académico revisado, mantenerlo versionado y actualizarlo de forma opcional cuando exista conexión, sin depender de Internet para estudiar.

Este documento no afirma que el sincronizador exista. Describe el diseño recomendado antes de modificar modelos, migraciones, vistas o Electron.

Incluye:
- Auditoría del modelo actual de contenido y evidencias.
- Separación entre estructura curricular, contenido versionado y datos del estudiante.
- Entidades locales y metadatos editoriales.
- Contrato del paquete y del manifiesto.
- Flujo de publicación, descarga, validación, activación y rollback.
- Estrategia de migración compatible con los registros existentes.
- Requisitos de seguridad, privacidad y pruebas.
- Diseño del publicador central de conocimiento.

No incluye sincronización de progreso entre dispositivos, cuentas en la nube, actualización del ejecutable ni ejecución remota/local de código descargado.

---

## 2. Decisión de producto aprobada

**Resuelta por el propietario (11-11-2026): modelo híbrido.** Un servidor central distribuye contenido revisado y versionado; el cliente sincroniza automáticamente cuando hay conexión y conserva el contenido local. Forma parte de la Fase 2.

- Sincronización pull-only por HTTPS; el cliente valida firma, hash, esquema y compatibilidad; instalación atómica y rollback.
- No se suben progreso, intentos, código, calificaciones ni datos personales.
- La detección de cambios en fuentes no publica contenido sin revisión editorial.

---

## 3. Auditoría del estado actual

La revisión de la rama de trabajo encontró:

| Archivo / componente | Estado comprobado | Limitación para versionado |
|---|---|---|
| `apps/roadmaps/models.py` — `Roadmap`, `Etapa`, `Modulo`, `Leccion` | Estructura curricular relacional | No se encontró una clave pública/estable de contenido para resolver recursos de paquetes entre instalaciones. |
| `ContenidoLeccion` | Relación `OneToOneField` con `Leccion`; teoría, explicación y `publicado` | Solo existe un registro editable por lección; no conserva versiones históricas ni referencias a fuentes. |
| `EjemploLeccion` | FK a `Leccion`; campos editables; `publicado=True` por defecto | No tiene clave externa estable ni versión editorial. |
| `EjercicioLeccion` | FK a `Leccion`; campos editables; `publicado=True` por defecto | Enunciado y pistas pueden cambiar sin snapshot histórico. |
| `ConfiguracionEvaluacion` | Versionado numérico por ejercicio y una sola configuración activa | La configuración histórica permanece como fila, pero no está vinculada a una versión del contenido. |
| `IntentoEjercicio` | Guarda respuesta, resultado, puntuación, detalles y versión numérica del evaluador | No identifica la versión exacta del enunciado/teoría que vio el estudiante. |
| `views.leccion_detalle` | Lee directamente los modelos editables publicados | No resuelve una versión inmutable activa. |
| `electron/main.js` / `preload.js` | Arranque del servidor local y API IPC de temas/funciones de escritorio | No se encontró flujo de consulta/descarga de paquetes. |
| `config/settings/base.py` | Aplicaciones instaladas: accounts, audit, core y roadmaps | No se encontró una app de conocimiento/sincronización instalada. |
| `apps/roadmaps/migrations` | Migraciones `0001_initial`, `0002_contenido_leccion`, `0003_intentos_y_evaluacion` | No hay todavía tablas para fuentes, versiones de contenido o paquetes instalados. |

### 2.1 Riesgos que deben resolverse

1. **Borrado en cascada de evidencias:** `IntentoEjercicio.ejercicio` usa `on_delete=CASCADE`. Eliminar un ejercicio elimina también sus intentos.
2. **Pérdida de vínculo histórico:** `IntentoEjercicio.configuracion_evaluacion` usa `SET_NULL`. Si se elimina una configuración, queda el número de versión, pero no la configuración aplicada.
3. **Contenido mutable:** las vistas leen directamente `ContenidoLeccion`, `EjemploLeccion` y `EjercicioLeccion`; una edición puede cambiar lo que se muestra sin conservar la versión anterior.
4. **Publicación inconsistente:** `ContenidoLeccion.publicado` inicia en falso, pero ejemplos y ejercicios inician publicados. El futuro flujo editorial debe validar la publicación de la lección como una unidad coherente.
5. **Identidad de contenido:** los IDs numéricos de SQLite no deben ser identificadores del paquete, porque no son una identidad portátil garantizada entre instalaciones.
6. **Configuración de evaluación en cliente:** los evaluadores necesarios para operar localmente no deben tratarse como secretos inviolables. Un propietario con acceso al equipo puede inspeccionar sus datos locales; no almacenar secretos ni credenciales dentro de esas configuraciones.

---

## 4. Principio de diseño: tres dominios separados

La arquitectura de datos debe separar:

### A. Estructura curricular

Contiene la ruta, etapas, módulos y lecciones: qué debe aprender el estudiante y en qué orden.

- Identidad estable de cada elemento curricular.
- Prerrequisitos y orden.
- No se reemplaza al actualizar una explicación o un ejercicio.
- Los cambios estructurales del roadmap requieren una publicación curricular explícita y una política de compatibilidad propia.

### B. Conocimiento académico versionado

Contiene el material que se puede actualizar:

- Teoría técnica y explicación pedagógica.
- Objetivos de aprendizaje.
- Ejemplos, código, salidas esperadas y explicaciones.
- Enunciados, instrucciones, pistas y criterios/evaluadores asociados.
- Fuentes, licencias, versiones consultadas y fechas de revisión.
- Estado editorial y versión publicada.

Cada publicación es inmutable. Una corrección produce una nueva versión; no sobrescribe la versión anterior.

### C. Evidencias y datos locales del estudiante

Contiene progreso, intentos, respuestas, resultados, preferencias y configuración local.

- No se distribuye dentro de paquetes de conocimiento.
- No se sobrescribe al instalar contenido.
- Los intentos conservan la versión del contenido y del evaluador que los originó.
- El historial académico se conserva aunque una lección sea sustituida o retirada.

---

## 5. Modelo de datos local recomendado

Los siguientes modelos son una propuesta conceptual. Los nombres pueden ajustarse al estilo del código antes de crear migraciones.

### 5.1 Identificadores estables

Agregar una clave estable UUID a los elementos que deben resolverse desde paquetes externos:

- `Leccion.clave_contenido`: UUID único e inmutable.
- `EjemploLeccion.clave_contenido`: UUID único e inmutable.
- `EjercicioLeccion.clave_contenido`: UUID único e inmutable.

Los paquetes referencian estas claves, no los PK autoincrementales de SQLite. La clave no cambia si se modifica el título, la redacción o el orden.

La fuente maestra del roadmap debe incluir esas claves para que una instalación nueva pueda resolver los mismos recursos. Para registros existentes, una migración de datos asignará UUID una sola vez y un export controlado los incorporará al catálogo curricular canónico. No generar claves nuevas en cada arranque ni al importar un paquete.

### 5.2 `FuenteConocimiento`

Representa una fuente técnica externa.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `id` | UUID | Identidad estable |
| `nombre` | texto | Nombre del publicador/documentación |
| `editor` | texto | Organización responsable |
| `url_canonica` | URL | Página/documentación principal |
| `identificador_licencia` | texto | SPDX u otra identificación, si aplica |
| `url_licencia` | URL | Condiciones de reutilización |
| `atribucion_requerida` | texto | Atribución que debe mostrarse |
| `tipo_fuente` | choice | Documentación oficial, estándar, especificación, etc. |
| `activa` | boolean | Si se sigue consultando |

Una fuente no se considera reutilizable solo por ser pública. La licencia y las condiciones deben revisarse.

### 5.3 `VersionContenidoLeccion`

Snapshot inmutable de una lección publicada.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `id` | UUID | Identidad de la versión |
| `leccion` | FK protegida | Lección curricular estable |
| `version` | entero | Secuencia por lección |
| `schema_version` | texto | Versión del esquema de payload |
| `payload` | JSON validado | Snapshot completo de teoría, ejemplos y ejercicios |
| `sha256` | texto de 64 caracteres | Integridad del payload canónico |
| `estado_editorial` | choice | borrador, revisión, aprobado, publicado, sustituido, retirado |
| `creado_en` | fecha/hora | Creación del snapshot |
| `revisado_en` | fecha/hora nullable | Última revisión técnica/pedagógica |
| `publicado_en` | fecha/hora nullable | Publicación |
| `responsable_revision` | texto/identidad editorial | Trazabilidad |
| `motivo_cambio` | texto | Por qué se creó esta versión |

Restricciones:
- Único por (`leccion`, `version`).
- Una versión publicada nunca se edita; se crea otra.
- El payload se valida contra un esquema conocido.
- Las referencias a fuentes se registran mediante una relación explícita, no solo en texto libre.

### 5.4 `ReferenciaFuenteContenido`

Relación entre una versión de lección y una fuente consultada.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `version_contenido` | FK protegida | Snapshot académico respaldado |
| `fuente` | FK protegida | Fuente registrada |
| `version_fuente` | texto | Versión/edición/tag/fecha de la fuente consultada |
| `url_seccion` | URL | Sección exacta usada como referencia |
| `consultada_en` | fecha/hora | Momento de consulta |
| `nota` | texto | Qué afirmación o parte respalda |

La relación permite que una lección cite varias fuentes y que una fuente respalde varias lecciones.

### 5.5 `ContenidoLeccionActivo`

Puntero a la versión que debe presentar la aplicación.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `leccion` | OneToOne/FK única | Lección curricular |
| `version_contenido` | FK protegida | Versión publicada activa |
| `activado_en` | fecha/hora | Momento de activación |

Separar el puntero de activación del snapshot permite cambiar muchas lecciones dentro de una transacción al instalar un paquete. Si falla la activación, se revierte la transacción y permanece el conjunto anterior.

### 5.6 `PaqueteConocimientoInstalado`

Registro local de paquetes recibidos y validados.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `package_id` | UUID | Identidad del paquete |
| `package_version` | texto/semver | Versión publicada |
| `channel` | texto | stable/beta u otro canal explícito |
| `content_schema_version` | texto | Esquema requerido |
| `sha256` | texto | Hash verificado |
| `signature_key_id` | texto | Clave pública usada para verificar |
| `published_at` | fecha/hora | Publicación central |
| `installed_at` | fecha/hora nullable | Instalación local |
| `status` | choice | descargado, verificado, activo, rechazado, sustituido |
| `error_code` | texto nullable | Diagnóstico técnico sin datos privados |

La tabla conserva historial de paquetes y permite diagnosticar instalaciones.

### 5.7 `EstadoSincronizacion`

Estado local de la comprobación, idealmente una fila por canal.

| Campo propuesto | Tipo conceptual | Uso |
|---|---|---|
| `channel` | texto único | Canal consultado |
| `last_check_at` | fecha/hora nullable | Última comprobación |
| `last_success_at` | fecha/hora nullable | Última sincronización exitosa |
| `manifest_etag` | texto nullable | Cache condicional HTTP |
| `active_package` | FK nullable | Paquete local activo |
| `last_error_code` | texto nullable | Último error |
| `next_check_after` | fecha/hora nullable | Evitar consultas repetitivas |

No almacenar tokens personales ni progreso del estudiante en este registro.

---

## 6. Snapshot de contenido: forma del payload

El payload de una versión de lección debe ser autocontenido y validable. Ejemplo ilustrativo (no es contenido académico real):

```json
{
  "schema_version": "1.0",
  "lesson_key": "uuid-estable-de-leccion",
  "version": 3,
  "locale": "es-CO",
  "title": "Variables",
  "objectives": ["Declarar y asignar variables"],
  "technical_theory": "Contenido técnico revisado...",
  "simple_explanation": "Explicación pedagógica original...",
  "notes": [],
  "examples": [
    {
      "key": "uuid-estable-de-ejemplo",
      "title": "Asignación",
      "language": "python",
      "code": "nombre = 'Ada'",
      "expected_output": "",
      "explanation": "..."
    }
  ],
  "exercises": [
    {
      "key": "uuid-estable-de-ejercicio",
      "title": "Declara una variable",
      "prompt": "Enunciado revisado...",
      "instructions": [],
      "language": "python",
      "level": "basico",
      "starter_code": "",
      "hints": [],
      "required": true,
      "evaluator": {
        "type": "respuesta_exacta",
        "version": 2,
        "config": {}
      }
    }
  ],
  "references": ["source-uuid-1"]
}
```

Reglas del payload:
- No incluir HTML arbitrario, JavaScript ejecutable, SQL, comandos de sistema ni migraciones.
- El contenido enriquecido debe usar un formato permitido y sanitizable (por ejemplo Markdown con un subconjunto documentado).
- Validar longitudes, número de ejemplos/ejercicios, tipos, URLs, UUIDs y campos permitidos.
- Los identificadores de ejercicio deben ser estables entre versiones si representan el mismo ejercicio.
- Si un ejercicio cambia sustancialmente de objetivo o criterio, crear una nueva identidad de ejercicio y no reciclar su clave.
- Las configuraciones de evaluación deben ser declarativas y validadas por tipo. No se acepta código Python/JS arbitrario como evaluador.
- Las configuraciones que el cliente necesita para evaluar localmente no son secretos frente al propietario del dispositivo. No colocar claves ni datos sensibles en ellas.

---

## 7. Contrato del paquete de distribución

### 7.1 Topología de distribución

El manifiesto firmado y el paquete son dos artefactos distintos. El manifiesto se publica fuera del ZIP para evitar una referencia circular: un manifiesto que contuviera el SHA-256 del ZIP no puede estar incluido dentro de ese mismo ZIP.

Estructura remota recomendada:

```text
/stable/
  manifest.json
  manifest.ed25519
  /packages/
    codeguard-knowledge-stable-<sequence>-<version>.zip
```

El cliente descarga primero el manifiesto y su firma; solo si la firma es válida descarga el paquete indicado. El paquete es inmutable y su URL debe pertenecer a un host permitido por la aplicación.

### 7.2 Contenido del paquete

El ZIP contiene únicamente datos editoriales y un índice interno de archivos:

```text
package/
  package-index.json
  payload/
    lessons/
      <lesson-uuid>.json
```

`package-index.json` declara `package_id`, `package_version`, `content_schema_version` y el listado de archivos con ruta relativa, tamaño y SHA-256. No incluye la firma externa ni intenta contener el hash del ZIP completo. No se aceptan ejecutables, scripts, migraciones, enlaces simbólicos ni archivos fuera del esquema permitido.

El paquete no incluye base de datos del estudiante, intentos, respuestas, progreso, preferencias, secretos ni ejecutables.

### 7.3 Manifiesto externo firmado

Ejemplo conceptual:

```json
{
  "manifest_version": "1",
  "channel": "stable",
  "sequence": 104,
  "published_at": "2026-11-11T18:00:00Z",
  "minimum_app_version": "1.0.0",
  "content_schema_version": "1.0",
  "package": {
    "package_id": "uuid-del-paquete",
    "package_version": "2026.11.1",
    "url": "/stable/packages/codeguard-knowledge-stable-104-2026.11.1.zip",
    "size_bytes": 123456,
    "sha256": "64-caracteres-hexadecimales"
  },
  "key_id": "codeguard-release-2026"
}
```

Los valores son ilustrativos. La firma Ed25519 se entrega como archivo separado (`manifest.ed25519`) y cubre exactamente los bytes de `manifest.json`. El manifiesto firmado contiene el hash y tamaño del ZIP, por lo que el cliente puede verificar el artefacto sin circularidad.

Reglas:
- `sequence` es un contador monotónico por canal y evita aceptar downgrades o manifiestos antiguos reproducidos. SemVer por sí solo no basta para este control.
- `published_at` sirve para trazabilidad; no sustituye `sequence`.
- La URL final se resuelve contra un origen HTTPS permitido. Se rechazan esquemas distintos de HTTPS, redirecciones a hosts no permitidos y URLs con credenciales.
- El cliente valida firma, canal, secuencia, versión mínima de aplicación, esquema, tamaño y hash antes de procesar el ZIP.
- La clave privada solo existe en el entorno de publicación. El cliente incorpora únicamente claves públicas de confianza identificadas por `key_id`.
- La rotación de claves requiere un procedimiento explícito y una versión de aplicación que reconozca la nueva clave.
- El hash detecta corrupción; la firma autentica el manifiesto. TLS protege el transporte, pero no sustituye la firma.

---

## 8. Publicador central de conocimiento

### 8.1 Objetivo

Construir el componente editorial que convierte versiones de lecciones aprobadas y publicadas en paquetes académicos inmutables, compatibles con el verificador local de distribución. El publicador no modifica el roadmap, no toca progreso ni intentos y no se ejecuta en el cliente del estudiante.

### 8.2 Entrada autorizada

El publicador solo seleccionará registros `VersionContenidoLeccion` cuyo estado sea `publicada`. No leerá el contenido editable actual de `ContenidoLeccion`, ni ejemplos/ejercicios mutables: el origen será exclusivamente el snapshot congelado de cada versión.

Antes de empaquetar cada lección debe comprobar:

- Hash SHA-256 del snapshot recalculado con JSON canónico (UTF-8, claves ordenadas y separadores compactos).
- Esquema académico soportado y UUID estable de lección, ejemplos y ejercicios.
- Referencias de fuente completas y congeladas al entrar en revisión.
- Evidencia de revisión de licencia y estado permitido: `compatible` o `solo_referencia`.
- Si la fuente está en `solo_referencia`, el uso declarado debe ser exclusivamente `original`.
- Para `compatible`, debe existir evidencia HTTPS, responsable/fecha de revisión y alcance de reutilización documentado.
- Ninguna fuente puede estar inactiva o tener una decisión de licencia incompatible con la publicación.

La salida por lección seguirá exactamente el contrato JSON v1 que consume `content_import._validate_document`: `schema_version`, `resumen_cambios`, `snapshot` y `fuentes`. Las referencias incluirán UUID de fuente, rol, localizador, nota de atribución y uso declarado.

### 8.3 Artefactos de distribución

Cada publicación producirá tres artefactos externos:

- `package.zip`: ZIP determinista con `package-index.json` y un JSON por lección bajo `payload/lessons/<uuid>.json`.
- `manifest.json`: manifiesto v1 con canal, secuencia, fecha UTC, versión mínima de aplicación, esquema, UUID/versión del paquete, URL HTTPS, tamaño, SHA-256 y `key_id`.
- `manifest.ed25519`: firma Ed25519 detached en Base64 sobre los bytes exactos de `manifest.json`.

El ZIP será reproducible para la misma entrada e identidad de paquete: orden estable de archivos, JSON canónico, timestamps ZIP fijos, permisos regulares normalizados y compresión definida. No se incluirán binarios, scripts, archivos ejecutables, datos de usuarios, progreso, intentos, credenciales ni configuraciones privadas.

### 8.4 Secuencia e historial de publicaciones

La secuencia es monotónica por canal y no puede depender únicamente de un argumento CLI ni de inspeccionar una carpeta arbitraria. Antes del publicador operativo se incorporará un registro central de releases con:

- Canal y secuencia únicos.
- UUID y SemVer del paquete.
- Hash del ZIP y hash del manifiesto.
- `key_id`, fecha de publicación y editor responsable.
- Identificador/ruta inmutable de los artefactos.

La reserva de secuencia se realizará bajo transacción y restricción única por canal. Un release ya registrado no se sobrescribe ni se vuelve a firmar con el mismo número. Los artefactos se prepararán en staging y se promoverán atómicamente; si falla la promoción, el release no se marcará como publicado. La política de recuperación de fallos entre almacenamiento y base de datos debe quedar explícita y probada.

### 8.5 Custodia de claves

- La clave privada Ed25519 se suministra fuera del repositorio mediante archivo PEM protegido o gestor de secretos.
- El publicador comprobará tipo de clave, permisos restrictivos del archivo y correspondencia con el `key_id` configurado.
- La clave privada nunca se registra, imprime, copia al ZIP ni almacena en SQLite.
- No se generarán claves de producción automáticamente durante una ejecución.
- La rotación de claves requerirá registrar previamente la clave pública correspondiente en los clientes y mantener un periodo de compatibilidad controlado.
- Las claves de prueba serán efímeras y solo existirán en fixtures de tests.

### 8.6 Separación de responsabilidades

El primer incremento implementará generación/validación local de artefactos y un comando editorial explícito. No realizará upload, despliegue CDN, cambios DNS ni configuración de proveedor. La URL pública declarada en el manifiesto deberá corresponder a una ubicación HTTPS autorizada y aprobada antes de una publicación real.

El cliente local seguirá siendo pull-only. La implementación del publicador no inicia conexiones desde el equipo del estudiante ni transmite información personal.

### 8.7 Pruebas de aceptación

- Solo versiones publicadas pueden empaquetarse.
- Rechazo de snapshot/hash alterado o esquema incompatible.
- Rechazo de fuente sin evidencia, licencia pendiente, permiso requerido, no reutilizable o inactiva.
- Rechazo de uso no permitido bajo `solo_referencia`.
- Validación de UUID y ausencia de colisiones entre recursos del paquete.
- ZIP determinista para la misma entrada.
- Round-trip: los artefactos generados pasan `verify_signed_manifest` y `validate_package_archive`.
- Rechazo de clave privada ausente, PEM inválido, tipo de clave incorrecto o permisos inseguros.
- Secuencia duplicada/descendente rechazada bajo concurrencia.
- Release y artefactos existentes nunca se sobrescriben.
- Fallo de escritura/promoción no deja un release marcado como publicado.
- Los paquetes no contienen información del estudiante ni código ejecutable.
- La generación no altera versiones editoriales, roadmap, progreso ni intentos.

---

## 9. Flujo editorial y de sincronización

### 9.1 Publicación central

1. Registrar la fuente, licencia, atribución y versión consultada.
2. Detectar cambios en fuentes técnicas y crear una alerta/propuesta de revisión.
3. Redactar o corregir contenido propio de CodeGuard.
4. Validar exactitud técnica, claridad pedagógica, ejemplos, ejercicios y evaluadores.
5. Aprobar la revisión mediante el flujo editorial.
6. Generar snapshots inmutables por lección.
7. Construir el paquete y el manifiesto.
8. Firmar el manifiesto con la clave privada de publicación.
9. Publicar archivos inmutables en el canal correspondiente.
10. Registrar la versión publicada y su historial.

### 9.2 Cliente local

1. La aplicación arranca normalmente desde el almacenamiento local.
2. Un comprobador en segundo plano consulta el manifiesto si hay conexión y si la política local permite comprobar.
3. Usa timeout, límites de tamaño, caché HTTP/ETag y backoff.
4. Compara las versiones instaladas con el manifiesto.
5. Descarga solo paquetes compatibles a una zona temporal.
6. Verifica firma del manifiesto, hash del paquete, esquema, claves y límites.
7. Valida todo el contenido antes de modificar las tablas activas.
8. Importa snapshots en una transacción.
9. Actualiza los punteros de contenido activo en una transacción.
10. Registra el paquete y conserva la versión anterior para rollback.
11. Si cualquier paso falla, conserva el contenido previo y muestra un estado recuperable.

### 9.3 Política de ejecución

Recomendación para la primera implementación:
- Comprobar al iniciar, pero después de que la ventana principal esté disponible.
- No hacer llamadas de red desde `AppConfig.ready()`, migraciones ni durante el arranque crítico de Django.
- Ejecutar la comprobación como tarea independiente/no bloqueante.
- Permitir comprobación manual y opción para desactivar/posponer la automática.
- Usar intervalo configurable y backoff; no crear un temporizador agresivo.
- No mantener WebSocket ni conexión permanente.
- La ausencia del servicio, timeout o falta de red nunca debe impedir estudiar.

---

## 10. Distribución central: recomendación de infraestructura

Para el primer incremento se recomienda que el endpoint central sea de distribución estática por HTTPS (almacenamiento de objetos o publicación estática con control de versiones), en lugar de crear de inmediato una API dinámica y una base de datos central.

Motivos:
- CodeGuard es una aplicación local monousuario.
- El cliente solo necesita leer un manifiesto y descargar paquetes.
- No se requieren cuentas cloud ni sincronización de progreso.
- Los paquetes son inmutables y se pueden almacenar en caché.
- Reduce infraestructura, superficie de ataque y mantenimiento.

El proceso editorial puede publicar artefactos mediante un flujo controlado. El endpoint estático sigue siendo el servicio central de distribución aprobado por la ADR-004. La selección del proveedor y dominio se hará antes de implementar la publicación, no se presupone un proveedor concreto.

---

## 11. Estrategia de compatibilidad y migración

No reemplazar las tablas existentes de forma abrupta.

### Incremento A — Identidad y protección de evidencia

1. Añadir claves estables UUID a lecciones, ejemplos y ejercicios.
2. Crear una migración de datos para asignar claves a filas existentes una sola vez.
3. Exportar y versionar las claves en el catálogo curricular canónico.
4. Añadir referencia a versión de contenido en los intentos futuros.
5. Añadir snapshot mínimo del ejercicio presentado (clave, enunciado y versión) para preservar evidencia.
6. Revisar las reglas `on_delete` de ejercicio y configuración de evaluación para que no se destruyan evidencias; usar protección y/o snapshots según el caso.

### Incremento B — Fuentes y snapshots

1. Crear `FuenteConocimiento` y relaciones de referencia.
2. Crear `VersionContenidoLeccion` con payload validado e inmutable.
3. Crear `ContenidoLeccionActivo` como puntero independiente.
4. Crear importador desde los modelos actuales a una primera versión, sin borrar ni alterar IDs.
5. Añadir pruebas de equivalencia entre contenido anterior y snapshot importado.

### Incremento C — Registro de paquetes y sincronizador

1. Crear `PaqueteConocimientoInstalado` y `EstadoSincronizacion`.
2. Implementar cliente HTTP con allowlist de host, TLS validado, timeout, tamaño máximo y ETag.
3. Implementar verificación Ed25519 y SHA-256.
4. Implementar importación transaccional y activación atómica.
5. Implementar rollback y estados visibles.

### Incremento D — Cambio de lectura

1. Adaptar `leccion_detalle` para leer la versión activa.
2. Mantener compatibilidad de URLs y progreso por IDs curriculares.
3. Adaptar envío de intentos para registrar la versión de contenido presentada.
4. Mantener las versiones previas accesibles para el historial.
5. Retirar gradualmente la lectura directa de los campos editables solo después de verificar equivalencia.

No borrar los modelos actuales ni ejecutar migraciones destructivas durante la primera integración.

---

## 12. Invariantes obligatorias

1. La estructura curricular no cambia al instalar una actualización de contenido.
2. Una versión publicada es inmutable.
3. Cada versión de lección identifica sus fuentes, revisión, estado y esquema.
4. La activación del paquete es atómica.
5. Una instalación fallida nunca sustituye la versión local válida.
6. El progreso, intentos, respuestas, preferencias y datos personales nunca se sobrescriben por sincronización.
7. Cada intento conserva la versión de contenido y el evaluador aplicados.
8. Las evidencias históricas sobreviven a la retirada de un ejercicio o una lección.
9. El contenido no ejecuta código ni comandos.
10. Ningún cambio detectado en una fuente externa se publica sin revisión.
11. La última versión válida permanece disponible offline.
12. La sincronización de esta fase es pull-only: el cliente descarga conocimiento y no transmite datos académicos del estudiante.

---

## 13. Pruebas técnicas derivadas

Además de SYNC-001 a SYNC-020 en `docs/PLAN_PRUEBAS.md`, añadir:

| ID | Prueba | Resultado esperado |
|---|---|---|
| DATA-001 | Asignación UUID a registros existentes | Cada recurso recibe una clave estable y única, sin alterar PK ni relaciones. |
| DATA-002 | Repetir migración/backfill | No cambia UUID previamente asignados. |
| DATA-003 | Snapshot inicial | El payload conserva teoría, ejemplos, ejercicios y orden de la versión original. |
| DATA-004 | Inmutabilidad | Una versión publicada no se modifica; se crea otra versión. |
| DATA-005 | Referencias | Cada fuente mantiene licencia, URL, versión y fecha consultada. |
| DATA-006 | Puntero activo | Una transacción activa el conjunto nuevo o mantiene íntegro el anterior. |
| DATA-007 | Historial de intento | Un intento antiguo conserva snapshot del enunciado y versión del contenido/evaluador. |
| DATA-008 | Eliminación de ejercicio | No se borran intentos históricos asociados. |
| DATA-009 | Retirada | Un recurso retirado se oculta de nuevas asignaciones sin borrar evidencias. |
| DATA-010 | Instalación limpia | Una base nueva resuelve las claves estables incluidas en el catálogo curricular. |

Pruebas del publicador (del diseño original):
- Solo versiones publicadas pueden empaquetarse.
- Rechazo de snapshot/hash alterado o esquema incompatible.
- Rechazo de fuente sin evidencia, licencia pendiente, permiso requerido, no reutilizable o inactiva.
- Rechazo de uso no permitido bajo `solo_referencia`.
- Validación de UUID y ausencia de colisiones entre recursos del paquete.
- ZIP determinista para la misma entrada.
- Round-trip: los artefactos generados pasan `verify_signed_manifest` y `validate_package_archive`.
- Rechazo de clave privada ausente, PEM inválido, tipo de clave incorrecto o permisos inseguros.
- Secuencia duplicada/descendente rechazada bajo concurrencia.
- Release y artefactos existentes nunca se sobrescriben.
- Fallo de escritura/promoción no deja un release marcado como publicado.
- Los paquetes no contienen información del estudiante ni código ejecutable.
- La generación no altera versiones editoriales, roadmap, progreso ni intentos.

---

## 14. Decisiones pendientes antes de implementar

Estas decisiones no invalidan la arquitectura híbrida ya aprobada; concretan detalles operativos que deben cerrarse antes de escribir código:

1. **Proveedor de distribución:** dominio/almacenamiento estático HTTPS. No seleccionar proveedor sin revisar coste, disponibilidad y facilidad de operación.
2. **Canales:** comenzar con `stable`; `beta` solo si se necesita probar publicaciones antes de producción.
3. **Frecuencia:** valor inicial recomendado de comprobación diaria, con comprobación manual y backoff. Debe poder cambiarse desde configuración.
4. **Tamaño máximo:** definir límite de paquete y de recurso antes de implementar el descargador.
5. **Política de versiones retiradas:** decidir cuánto tiempo conservar versiones antiguas localmente y cómo informar retiros críticos.
6. **Catálogo curricular canónico:** definir el archivo/flujo que transporta las claves UUID de las lecciones entre instalaciones.
7. **Editorial:** determinar dónde se redacta y revisa el contenido (repositorio controlado, herramienta interna o flujo editorial propio). No habilitar Django Admin por defecto como sustituto de este diseño.

---

## 15. Criterio de cierre del diseño

El diseño estará listo para implementación cuando:

- Los nombres y relaciones de los modelos hayan sido aprobados.
- El esquema del payload y manifiesto tenga validación automatizada.
- La estrategia de claves estables esté definida.
- La política de preservación de intentos/evaluadores esté definida.
- Se haya seleccionado el endpoint de distribución.
- La migración desde los registros actuales tenga pruebas de ida/compatibilidad y no sea destructiva.

**Estado al 12-11-2026:** auditoría y propuesta documentadas; no se han modificado modelos, migraciones, vistas, Electron ni datos de estudiantes.

---

## 16. Hallazgos de auditoría y precisiones obligatorias

Esta sección concreta el diseño tras contrastarlo con los modelos y migraciones existentes. Prevalece sobre cualquier ejemplo anterior que resulte ambiguo.

### 16.1 Preservación de evidencias

- Los FK desde `IntentoEjercicio` hacia `EjercicioLeccion` y `ConfiguracionEvaluacion` no deben permitir borrado en cascada de evidencias. Para nuevos cambios se debe preferir `PROTECT` y retiro lógico/editorial, no eliminación física.
- Los intentos nuevos deben conservar la clave estable del ejercicio, la versión de contenido presentada y un snapshot mínimo del enunciado/instrucciones. Los intentos anteriores se migran como históricos con versión de contenido desconocida explícitamente; no se inventa una versión retroactiva.
- La configuración de evaluación aplicada debe permanecer consultable e inmutable una vez utilizada. El intento conserva su referencia y versión; la referencia histórica no se elimina.
- La eliminación de una lección o ejercicio con evidencias no forma parte del flujo editorial normal. Se retira o sustituye.

### 16.2 Identidad curricular

Los UUID se asignan una sola vez mediante migración de datos y se exportan al catálogo curricular canónico. La importación de ASCENSO debe resolver por esa identidad estable, no por título, orden ni PK local. Cambiar título u orden no cambia identidad. Un cambio de objetivo curricular que represente otra lección requiere nueva identidad y una regla explícita de migración del progreso.

### 16.3 Separación entre borrador, publicación y vigencia

El contenido editorial mutable existente puede seguir siendo fuente de trabajo durante la transición. Al publicar se genera un snapshot inmutable. No se debe editar un snapshot publicado ni mezclar en un único estado el ciclo editorial (borrador/revisión/aprobado) con la vigencia (vigente/revisión pendiente/sustituido/retirado). La vigencia puede cambiar mediante eventos/metadata sin alterar el payload histórico.

Cada contenido debe registrar al menos: `reviewed_at`, `review_due_at` cuando aplique, versión tecnológica objetivo, idioma, fuentes, licencia/atribución y estado de vigencia. Una revisión vencida genera advertencia editorial, no una afirmación automática de que el contenido es incorrecto.

### 16.4 Evaluadores y límite de confianza local

Las configuraciones de evaluación incluidas en un paquete son datos declarativos, nunca código ejecutable. Como CodeGuard funciona localmente, el propietario del equipo puede inspeccionar o modificar la base de datos y el contenido instalado; por tanto, una configuración "no expuesta en la plantilla" no es un secreto criptográfico ni hace inviolable la evaluación. No incluir credenciales, claves ni secretos en evaluadores. Las aprobaciones locales sirven para la experiencia académica del usuario, no como certificación remota resistente a manipulación.

### 16.5 Transición sin ruptura

La migración se ejecutará por pasos aditivos: asignar UUID; crear snapshots iniciales desde los modelos actuales; comparar salida de la vista anterior y nueva; enlazar intentos nuevos a snapshots; cambiar lectura a la versión activa; y solo después retirar gradualmente la lectura mutable. Se conservan PK, URLs y progreso existentes. No se modifica ni se borra contenido real durante la auditoría.

### 16.6 Límites de archivos comprimidos

Antes de extraer, validar número de entradas, tamaño comprimido y descomprimido total, tamaño individual, relación de compresión, rutas normalizadas, nombres duplicados y tipo de archivo. Rechazar rutas absolutas, `..`, enlaces simbólicos, archivos anidados no previstos y entradas que escapen del directorio temporal. La extracción ocurre en una carpeta temporal nueva y no confiable; nunca directamente sobre el contenido activo.

---

## 17. Integración con el ciclo de vida Electron/Django

La revisión del empaquetado confirma que Electron inicia un servidor Django local como proceso hijo. En desarrollo se ejecuta `manage.py`; en la aplicación empaquetada se inicia el binario PyInstaller `CodeGuardServer`, construido desde `server_entry.py`. Por tanto, el sincronizador debe integrarse en este ciclo y no asumir que existe un intérprete Python externo en los equipos instalados.

Diseño recomendado para la implementación:

1. Crear una app de dominio `apps.knowledge` e instalarla en `INSTALLED_APPS`.
2. Implementar la lógica de sincronización como servicios Python y un comando Django de una sola ejecución (por ejemplo, `sync_knowledge`). El comando comparte `CODEGUARD_DATA_DIR` y la misma configuración de base de datos que el servidor local.
3. Extender `server_entry.py` para reconocer un modo de comando de sincronización y salir al terminar, además del modo actual de servidor WSGI. En desarrollo, Electron puede invocar el comando mediante el Python del entorno virtual; en producción, invoca el mismo binario PyInstaller con el argumento correspondiente.
4. Electron inicia la comprobación después de que la ventana principal esté disponible. El proceso de descarga no forma parte del camino crítico de arranque y no bloquea el uso local. El renderer solo recibirá estado mediante IPC limitado y tipado: última comprobación, última sincronización exitosa, versión disponible, estado y error genérico. No se exponen rutas arbitrarias, comandos ni argumentos libres al renderer.
5. Permitir comprobación manual, desactivar/posponer la comprobación automática y configurar una frecuencia inicial diaria. Si la aplicación está cerrada no se ejecuta una tarea residente ni se requiere servicio del sistema operativo.
6. Usar un bloqueo local para impedir dos sincronizaciones simultáneas. Descargar y validar fuera de la transacción; mantener la transacción SQLite de importación/activación breve. Manejar `database is locked` con reintentos limitados y nunca borrar el contenido activo por un error de concurrencia.

No se debe realizar tráfico de red desde `AppConfig.ready()`, durante migraciones, en el constructor de Django ni antes de que la ventana esté disponible. La sincronización no se debe iniciar desde el renderer mediante llamadas HTTP arbitrarias.

### 17.1 Compatibilidad del empaquetado

La implementación debe revisar y actualizar de forma coordinada `server_entry.py`, `CodeGuardServer.spec`, `electron/main.js`, `electron/preload.js`, `package.json` si se requiere una señal de estado y `requirements.txt` si se incorpora criptografía. La app nueva debe quedar incluida en el descubrimiento de PyInstaller y en `INSTALLED_APPS`. La clave privada de firma no se incluye en `CodeGuardServer`, en Electron ni en el repositorio de distribución.

### 17.2 Riesgo del cargador curricular actual

El comando `cargar_ascenso` no es un instalador de paquetes de conocimiento:

- El JSON `apps/roadmaps/data/ascenso_3_1.json` identifica lecciones por títulos y no contiene las claves UUID estables propuestas.
- El servicio `cargar_ascenso` usa `update_or_create` por título para módulos/lecciones; no implementa un protocolo de migración de identidad curricular.
- La opción `--recrear` elimina el roadmap y, por cascada, puede eliminar progreso y contenido asociado.
- La reconstrucción de prerrequisitos forma parte de la carga del roadmap, no de la actualización de contenido pedagógico.

**Regla obligatoria:** el sincronizador nunca invoca `cargar_ascenso --recrear` ni modifica la estructura curricular al instalar contenido de lecciones. La incorporación de UUID al catálogo ASCENSO requiere una migración/exportación controlada, preservando PK y progreso. Las actualizaciones de contenido usan exclusivamente el importador versionado descrito en este documento.

---

## 18. Primer incremento implementado

Se incorpora una migración aditiva para asignar UUID permanentes a lecciones, ejemplos y ejercicios existentes. La migración primero agrega columnas anulables, asigna un UUID distinto por fila y después impone unicidad y obligatoriedad.

Las relaciones desde intentos hacia ejercicios, desde evaluadores hacia ejercicios y desde intentos hacia la configuración aplicada pasan a protección contra borrado (PROTECT). El historial se conserva; la retirada de contenido deberá realizarse mediante estados editoriales y no mediante eliminación física.

Este incremento no crea todavía snapshots ni sincronización de red. Las claves UUID deberán exportarse posteriormente al catálogo curricular canónico y nunca regenerarse al cargar ASCENSO o instalar paquetes.

---

## 19. Catálogo de fuentes y snapshots versionados

Se añade la primera estructura persistente para registrar la procedencia y las versiones del conocimiento académico:

- `FuenteConocimiento`: publicador, título, URL canónica, edición, licencia, fecha de consulta y notas editoriales.
- `VersionContenidoLeccion`: snapshot JSON, UUID, número de versión, versión del esquema, SHA-256, estado editorial, resumen de cambios y fechas de revisión/publicación.
- `ReferenciaFuenteContenido`: relación explícita entre una versión y sus fuentes, con rol, localizador y atribución.

Restricciones:
- Una sola versión publicada por lección.
- Número de versión único por lección.
- Una fuente no se duplica por URL canónica y edición.
- La versión y la fuente referenciadas se protegen contra borrado.
- El hash debe validarse como hexadecimal SHA-256 en la validación del modelo.

**Límite de este incremento:** los snapshots se almacenan, pero aún no se generan automáticamente desde `ContenidoLeccion`, ejemplos y ejercicios; tampoco se ha implementado el flujo editorial, la firma de paquetes ni el cliente de sincronización. La inmutabilidad completa deberá centralizarse en servicios de publicación y reforzarse en el siguiente incremento; no se debe editar una versión publicada desde interfaces ordinarias.

---

## 20. Servicio de generación de snapshots

El servicio `apps/roadmaps/knowledge.py` genera snapshots deterministas desde el borrador editorial actual:

- Incluye los datos estables de la lección, teoría, explicación, objetivos y notas.
- Incluye únicamente ejemplos y ejercicios publicados.
- Ordena los recursos por orden editorial e ID local como desempate.
- Serializa JSON con claves ordenadas, UTF-8 y separadores estables; calcula SHA-256 sobre esa representación canónica.
- Asigna el siguiente número de versión dentro de una transacción y bloquea la fila de lección durante la operación.
- Asocia fuentes y datos de atribución.
- Crea siempre una versión en estado `borrador`; no publica ni modifica el contenido editorial activo.
- Rechaza lecciones sin contenido, sin teoría técnica o sin explicación sencilla, así como fuentes inactivas.

La prueba verifica que el snapshot no cambia cuando el borrador editorial se modifica después y que el siguiente snapshot recibe la versión siguiente.

**Límite:** el servicio crea snapshots, pero todavía no aplica una política completa de aprobación/publicación, no congela por sí mismo las filas de versiones frente a escrituras directas y no produce paquetes firmados.

---

## 21. Flujo editorial controlado

Se implementan servicios explícitos para las transiciones de estado:

- `enviar_version_a_revision`: solo admite borradores con hash íntegro, estructura mínima válida, identidad de lección coincidente y al menos una fuente activa.
- `aprobar_version_contenido`: solo admite versiones en revisión y registra fecha y usuario revisor.
- `publicar_version_contenido`: solo admite versiones aprobadas; sustituye la publicación anterior y activa la nueva dentro de una única transacción.
- `retirar_version_publicada`: exige motivo documentado y conserva el snapshot histórico.

Las operaciones exigen un usuario autenticado, activo y con `is_staff=True`. Las versiones enviadas a revisión bloquean cambios en su identidad, snapshot, hash y resumen de cambios; solo los borradores pueden eliminarse mediante el método de instancia del modelo.

**Importante:** Django Admin continúa deshabilitado. Estos servicios son la capa de dominio para una futura interfaz editorial segura o un comando de gestión; no se habilita un panel administrativo ni se expone publicación desde vistas de estudiante.

### 20.1 Auditoría de retirada

La retirada registra campos independientes `retirada_por` y `retirada_en`. No reutiliza los metadatos de revisión/aprobación, para preservar quién aprobó originalmente el contenido y quién ordenó su retirada. La causa queda en `motivo_retiro`.

### 20.2 Protección frente a escrituras masivas

El modelo de versiones usa un QuerySet especializado que rechaza `update()`, `bulk_update()` y eliminaciones masivas, además de impedir la creación masiva en estados distintos de borrador. La modificación de estados debe pasar por los servicios editoriales; la eliminación individual se limita a borradores. Esto reduce las vías accidentales para saltarse las validaciones del ciclo de vida. Como toda protección a nivel ORM, no sustituye controles de acceso a la base de datos ni impide SQL directo ejecutado por código privilegiado.

El envío a revisión también conserva `enviada_por` y `enviada_en`, separados de los datos de aprobación, publicación y retirada. Así queda identificada cada responsabilidad del ciclo editorial.

---

## 22. Operación editorial local mediante comandos de gestión

Como Django Admin no está habilitado, se incorporan comandos internos para operar el flujo sin exponerlo a estudiantes:

```bash
python manage.py crear_version_leccion --leccion 123 --fuente-id 4 --resumen "Primera revisión"
python manage.py gestionar_version_leccion enviar-revision --version-id 17 --usuario editor
python manage.py gestionar_version_leccion aprobar --version-id 17 --usuario revisor
python manage.py gestionar_version_leccion publicar --version-id 17 --usuario publicador
python manage.py gestionar_version_leccion retirar --version-id 17 --usuario revisor --motivo "La referencia quedó obsoleta"
```

Los IDs numéricos son locales y solo se usan para operación; los UUID son las identidades estables para distribución. Los comandos no crean usuarios ni conceden privilegios: el usuario debe existir, estar activo y tener `is_staff=True`.

El propio modelo también valida la secuencia de estados y exige los metadatos correspondientes para cada transición. No permite saltar de borrador directamente a publicación ni sobrescribir una vez asignados los responsables/fechas de envío, revisión, publicación o retirada.

---

## 23. Registro controlado del catálogo de fuentes

El comando `registrar_fuente_conocimiento` permite crear registros desde una operación explícita del equipo editorial. Acepta publicador, título, URL canónica HTTPS, edición, identificador y URL de licencia y notas. La fecha de consulta se registra al crear el registro; la combinación URL + edición debe ser única.

El comando rechaza URLs que no sean HTTPS absolutas o que incluyan credenciales, valida el modelo y no sobrescribe registros existentes. Su resultado es un registro **pendiente de verificación editorial**: no comprueba automáticamente la autoridad del dominio, la vigencia de la documentación ni los derechos de reutilización. La revisión humana debe comprobar esos aspectos antes de asociar la fuente a un snapshot que avance al estado de revisión.

Ejemplo:

```bash
python manage.py registrar_fuente_conocimiento \
  --publicador "Python Software Foundation" \
  --titulo "Python Language Reference" \
  --url "https://docs.python.org/3/reference/" \
  --edicion "Python 3" \
  --licencia-id "PSF-2.0" \
  --licencia-url "https://docs.python.org/3/license.html"
```

El registro no realiza solicitudes HTTP, no importa páginas, no ejecuta recursos remotos y no cambia el estado editorial de ninguna lección. La administración del contenido y su publicación continúan separadas.

---

## 24. Verificación de manifiestos y paquetes

**Estado:** núcleo de verificación y registro local implementado en `main`. El usuario confirmó 93 pruebas (`OK`) antes del incremento de correcciones 0014; la migración y pruebas nuevas de la rama correctiva están pendientes de validación local.

### 24.1 Verificación del manifiesto

Módulo: `apps/roadmaps/distribution.py`.

- Analiza JSON UTF-8 estricto y rechaza claves duplicadas, constantes no estándar, tipos incorrectos y propiedades no declaradas.
- Acepta únicamente `manifest_version=1`, canales `stable`/`beta` y `content_schema_version=1`.
- Comprueba UUID canónico, SemVer, fecha ISO-8601 con zona horaria, tamaño máximo y SHA-256.
- Exige URL HTTPS absoluta, sin credenciales ni fragmento, puerto estándar y hostname incluido en la allowlist entregada por el llamador.
- Verifica firma Ed25519 sobre los bytes exactos de `manifest.json`; el archivo de firma separado contiene Base64 de los 64 bytes de firma.
- Resuelve `key_id` únicamente contra claves públicas de confianza entregadas por configuración; no incorpora claves privadas ni claves públicas ficticias al repositorio.
- Rechaza secuencias inferiores y manifiestos distintos que reutilicen la secuencia ya instalada. La misma secuencia y el mismo hash se reconocen como no-op.
- Comprueba la versión mínima de la aplicación mediante comparación SemVer.

La allowlist y el almacén de claves públicas todavía deben integrarse con la configuración empaquetada. El verificador recibe ambos explícitamente; no se ha habilitado ningún host ni clave de producción.

### 24.2 Verificación del ZIP

`validate_package_archive()` verifica el paquete en memoria y no extrae rutas suministradas por terceros.

Límites actuales:

| Control | Límite |
|---|---|
| Manifiesto JSON | 64 KiB |
| Firma Base64 | 256 bytes |
| Paquete ZIP | 100 MiB |
| Entradas totales | 501 (índice + 500 lecciones) |
| Índice JSON | 1 MiB |
| Documento de lección | 2 MiB |
| Contenido descomprimido total | 100 MiB |
| Ratio de compresión por entrada | 100:1 |

Solo se aceptan `package-index.json` y documentos `payload/lessons/<uuid>.json`. Se rechazan rutas absolutas, traversal, barras invertidas, directorios explícitos, enlaces simbólicos, tipos especiales, métodos de compresión no admitidos, nombres duplicados, archivos no declarados, hashes/tamaños incorrectos y UUID repetidos o reasignados entre lecciones, ejemplos y ejercicios. Cada documento se valida con el contrato académico JSON v1 existente; el UUID del nombre del archivo debe coincidir con el UUID curricular interno.

El validador no ejecuta contenido, no escribe archivos y no modifica SQLite.

### 24.3 Registro local

Migraciones `0012_registro_paquetes_sincronizacion` y `0013_un_paquete_activo_por_canal` incorporan:

- `PaqueteConocimientoInstalado`: identidad, versión, canal, secuencia, esquema, hashes, clave de firma, fecha de publicación, instalación, estado y código de error.
- `EstadoSincronizacion`: última comprobación/actualización, ETag, paquete activo, siguiente comprobación y último error.

Se exige una secuencia única por canal y como máximo un paquete con estado `activo` por canal. El modelo restringe transiciones (`descargado → verificado/rechazado → activo → sustituido`), bloquea cambios de identidad/hash y borrado físico; el FK al paquete activo usa `PROTECT` y valida que el canal coincida. No se almacenan datos de progreso, respuestas, código del estudiante, secretos ni credenciales.

### 24.4 Dependencia criptográfica

Se fija `cryptography==46.0.3` en `requirements.txt` para Ed25519. Debe instalarse en el entorno virtual y estar incluida en la construcción PyInstaller antes de distribuir el cliente.

### 24.5 Límites explícitos del incremento

Este avance **no** implementa todavía:

- cliente HTTP, descarga, ETag, reintentos o backoff;
- endpoint o proveedor de distribución central;
- almacén definitivo de claves públicas y allowlist de producción;
- comando de empaquetado/firma editorial;
- instalación de paquetes descargados, punteros de paquete activo y rollback transaccional;
- programación automática desde Electron.

El puntero editorial local `ContenidoLeccionActivo` ya existe para publicaciones gestionadas dentro de la aplicación; todavía no es un instalador de paquetes remotos ni debe confundirse con la activación transaccional de un paquete de distribución.

No se debe interpretar la validación criptográfica de artefactos como una sincronización ya operativa. El siguiente incremento debe conectar el verificador con un flujo de publicación controlado y un instalador transaccional, sin tocar progreso ni intentos.