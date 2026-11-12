# Contrato de importación de contenido académico

**Producto:** CodeGuard Pro  
**Fase:** 2 — Motor de aprendizaje y contenido interactivo  
**Estado:** Contrato implementado en la rama de trabajo; pendiente de validación local completa.  
**Fecha:** 11 de noviembre de 2026  
**Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md`, `docs/FASE_2_APRENDIZAJE.md`, `docs/DISENO_DATOS_SINCRONIZACION.md`, `docs/ADR/ADR-004-sincronizacion-hibrida-conocimiento.md`.

---

## 1. Propósito

Definir un contrato estricto para recibir contenido académico estructurado, validarlo y convertir cada lección en un snapshot editorial en estado `borrador`.

El importador será una herramienta editorial interna. No será una ruta pública, no estará disponible para estudiantes y no publicará contenido automáticamente.

Este incremento debe poder ejecutarse antes de construir el distribuidor central y el cliente de sincronización. El mismo contrato se reutilizará después dentro de los paquetes firmados.

## 2. Hallazgos de la revisión del repositorio

La rama `docs/phase-2-hybrid-knowledge-sync` ya contiene:

- UUID estables en `Leccion`, `EjemploLeccion` y `EjercicioLeccion`.
- `FuenteConocimiento`, con UUID, publicador, título, URL canónica HTTPS, edición, campos de licencia, fecha de consulta y estado activo.
- `VersionContenidoLeccion`, que conserva un snapshot JSON, hash SHA-256, número incremental y estado editorial.
- `ReferenciaFuenteContenido`, que asocia fuentes a snapshots mediante rol, localizador y nota de atribución.
- `crear_version_contenido_leccion()`, que genera snapshots deterministas desde los modelos actuales.
- Servicios editoriales para enviar a revisión, aprobar, publicar y retirar versiones.
- Comandos para registrar fuentes, crear snapshots y ejecutar transiciones editoriales.

El contrato de importación debe integrarse con esas entidades y servicios. No debe crear tablas paralelas de versiones ni inventar un segundo ciclo editorial.

### 2.1 Diferencia entre el registro actual y el importador

El comando `registrar_fuente_conocimiento` registra metadatos declarados por quien lo ejecuta. No verifica automáticamente que el publicador sea oficial, que la edición esté vigente ni que la licencia permita reutilización.

Por tanto, el registro de una fuente y la autorización editorial de su uso son decisiones distintas. La importación podrá detectar referencias faltantes o fuentes sin revisión, pero no debe convertir esos registros en fuentes verificadas.

## 3. Unidad de importación y formato

La unidad lógica de importación será una colección de documentos JSON UTF-8, uno por lección. El paquete físico posterior podrá agrupar muchos documentos, pero la validación inicial trabajará con el mismo contrato lógico.

Estructura de un documento:

```json
{
  "schema_version": 1,
  "resumen_cambios": "Primera redacción revisada de la lección.",
  "snapshot": {
    "esquema_version": 1,
    "leccion": {
      "clave": "UUID-ESTABLE-DE-LECCION",
      "titulo": "Variables",
      "descripcion": "Introducción a variables.",
      "tipo": "concepto"
    },
    "contenido": {
      "objetivos_aprendizaje": "Declarar y asignar variables.",
      "teoria_tecnica": "Explicación técnica original y revisada.",
      "explicacion_sencilla": "Explicación pedagógica clara.",
      "notas": ""
    },
    "ejemplos": [
      {
        "clave": "UUID-ESTABLE-DE-EJEMPLO",
        "titulo": "Asignación",
        "contexto": "Asignar un valor a una variable.",
        "lenguaje": "Python",
        "codigo": "nombre = 'Ada'",
        "salida_esperada": "",
        "explicacion": "La variable nombre referencia el valor.",
        "orden": 1
      }
    ],
    "ejercicios": [
      {
        "clave": "UUID-ESTABLE-DE-EJERCICIO",
        "titulo": "Declara una variable",
        "enunciado": "Declara una variable llamada nombre.",
        "instrucciones": "Usa una asignación.",
        "lenguaje": "Python",
        "nivel": "basico",
        "codigo_inicial": "",
        "obligatorio": true,
        "orden": 1
      }
    ]
  },
  "fuentes": [
    {
      "clave": "UUID-DE-FUENTE-REGISTRADA",
      "rol": "principal",
      "localizador": "Sección 4.2",
      "nota_atribucion": "Referencia conceptual; explicación redactada por CodeGuard.",
      "uso_declarado": "original"
    }
  ]
}
```

Los UUID del ejemplo son marcadores ilustrativos; un documento real debe contener UUID válidos y existentes en el catálogo correspondiente.

### 3.1 Correspondencia con el snapshot interno actual

El importador no almacenará `schema_version`, `resumen_cambios` ni `fuentes` dentro del JSON `snapshot` de `VersionContenidoLeccion`.

La conversión será:

| Documento importado | Destino interno |
|---|---|
| `schema_version` | Validación del contrato externo |
| `resumen_cambios` | `VersionContenidoLeccion.resumen_cambios` |
| `snapshot` | `VersionContenidoLeccion.snapshot` |
| `snapshot.esquema_version` | `VersionContenidoLeccion.esquema_version` |
| `fuentes[]` | Filas `ReferenciaFuenteContenido` |
| Identidad de lección | Relación con `Leccion` por `clave_contenido` |
| Identidad de fuente | Relación con `FuenteConocimiento` por `clave` |

La forma de `snapshot` debe coincidir con la que genera actualmente `_serializar_snapshot()` en `apps/roadmaps/knowledge.py`. No se añadirán silenciosamente propiedades que el lector actual no conoce.

## 4. Reglas de validación

La validación se ejecutará en memoria antes de crear cualquier fila. Si un documento o un lote contiene un error bloqueante, no se importará parcialmente.

### 4.1 Esquema y tipos

- Aceptar exclusivamente `schema_version = 1`.
- Rechazar propiedades desconocidas en cada nivel; evita errores tipográficos que aparenten haber sido importados.
- Exigir los objetos `snapshot`, `leccion`, `contenido`, `ejemplos`, `ejercicios` y la lista `fuentes`.
- Comprobar que los tipos JSON coinciden exactamente con el contrato: cadenas, booleanos, enteros, listas y objetos.
- Rechazar valores nulos donde el contrato exige un valor.
- No convertir automáticamente números a cadenas, cadenas a booleanos ni UUID mal formados a valores aproximados.
- Rechazar listas u objetos anidados donde se espera texto plano.

### 4.2 Identidad y alineación con ASCENSO

- `snapshot.leccion.clave` debe ser un UUID válido y corresponder a una única fila `Leccion`.
- El título y tipo recibidos deben coincidir con el registro curricular, salvo que una operación editorial explícita autorice una actualización estructural. La importación de contenido no modifica el roadmap.
- Cada ejemplo y ejercicio debe tener un UUID válido.
- No puede repetirse un UUID dentro del mismo documento ni en otra unidad del mismo lote cuando represente recursos distintos.
- Un UUID ya conocido no puede reasignarse a otra lección ni a otro tipo de recurso.
- Un recurso existente puede conservar su UUID entre versiones cuando mantiene la misma identidad pedagógica. Un cambio sustancial de objetivo o criterio requiere una nueva identidad.
- Los IDs autoincrementales de SQLite no se aceptan como identificadores del paquete.

### 4.3 Contenido académico

- Exigir teoría técnica y explicación sencilla no vacías.
- Exigir al menos un objetivo de aprendizaje y validar que no sea una cadena compuesta solo por espacios.
- Validar que `tipo` pertenezca a las opciones de `Leccion.TIPOS`.
- Validar los campos de ejemplos y ejercicios según los tipos y longitudes definidos por los modelos.
- `orden` debe ser entero no negativo; no aceptar booleanos como enteros.
- `obligatorio` debe ser booleano real.
- No aceptar campos de evaluación ejecutables, scripts, imports, comandos, migraciones ni funciones Python/JavaScript.
- No ejecutar, importar ni evaluar el código de los ejemplos durante la importación.
- El código de ejemplo se almacena como texto para su posterior visualización y revisión.
- El esquema v1 no transporta configuraciones de evaluadores ni pistas progresivas. Estos requieren un contrato específico, pruebas y control editorial posterior.

### 4.4 Fuentes y derechos de uso

- Cada UUID de fuente debe corresponder a una fila `FuenteConocimiento` existente.
- No aceptar fuentes inactivas.
- No crear fuentes automáticamente durante la importación; primero deben registrarse y revisarse por separado.
- La referencia debe incluir rol válido (`principal`, `complementaria` o `normativa`), localizador, nota de atribución y `uso_declarado` (`original`, `cita_breve`, `adaptacion` o `reproduccion`).
- No considerar que HTTPS, dominio oficial o acceso público equivalen a permiso de reutilización.
- No permitir que el importador marque una fuente como verificada ni modifique su licencia.
- La versión importada siempre queda en borrador. Las fuentes pendientes se registran como advertencia y bloquean el envío a revisión hasta resolver la licencia.

### 4.5 Límites de recursos

Los límites concretos se centralizarán en constantes de configuración y se probarán. Como valores iniciales de diseño:

| Recurso | Límite propuesto |
|---|---:|
| Tamaño máximo de un documento JSON | 2 MiB |\n| Tamaño máximo del lote completo | 100 MiB |
| Documentos por lote de importación inicial | 500 |
| Ejemplos por lección | 50 |
| Ejercicios por lección | 50 |
| Fuentes por lección | 20 |
| Profundidad máxima JSON | 8 |
| Longitud de un campo de texto | Nunca superar el límite del modelo destino |

Estos límites son topes técnicos, no objetivos editoriales. Podrán ajustarse mediante una decisión documentada y pruebas de memoria/rendimiento.

## 5. Detección de conflictos y duplicados

El validador debe producir un informe determinista con errores, advertencias y resumen. No debe resolver conflictos de forma silenciosa.

| Situación | Resultado |
|---|---|
| Lección UUID inexistente | Error bloqueante |
| Lección repetida dentro del lote | Error bloqueante |
| UUID de ejemplo/ejercicio repetido en el lote | Error bloqueante |
| UUID asociado a otro padre o tipo de recurso | Error bloqueante |
| Fuente inexistente o inactiva | Error bloqueante |
| Fuente con licencia sin revisar | Advertencia editorial; no se permite avanzar a revisión/publicación |
| Mismo hash y misma lección con las mismas referencias | Duplicado idempotente; no crear otra versión |
| Misma lección con hash diferente | Crear una nueva versión borrador mediante importación explícita; nunca sobrescribir la anterior. UUID de recurso ligado a otro padre/tipo sí es conflicto |
| Título curricular distinto al de ASCENSO | Error; no renombrar la lección desde el paquete |
| Campo desconocido o versión de esquema no soportada | Error bloqueante |

El validador debe distinguir:
- **Error:** el lote no se importa.
- **Advertencia:** el borrador puede conservarse, pero no puede avanzar a revisión/publicación hasta resolverla.
- **Duplicado idempotente:** no crea filas adicionales y devuelve el estado de la versión existente.
- **Conflicto:** exige intervención editorial; nunca sobrescribe el contenido previo.

## 6. Integración con el ciclo editorial

Flujo objetivo:

1. El editor prepara el documento conforme al contrato.
2. El comando de validación analiza todo el lote sin escribir en la base de datos.
3. Se genera un informe con errores, advertencias, duplicados y conflictos.
4. Si no existen errores bloqueantes, el editor puede ejecutar la importación explícita.
5. El servicio crea un `VersionContenidoLeccion` en estado `borrador`, calcula SHA-256 del snapshot canónico y crea las relaciones `ReferenciaFuenteContenido`.
6. El importador no cambia `ContenidoLeccion`, ejemplos, ejercicios, progreso, intentos ni evaluadores activos.
7. El editor revisa el borrador mediante el flujo editorial existente.
8. La versión solo puede publicarse después de completar las verificaciones técnicas, pedagógicas y de licencia.

La validación y la importación deben separar sus operaciones:

- `validar_paquete_contenido`: solo lectura; devuelve informe.
- `importar_paquete_contenido`: requiere confirmación explícita; transacción atómica.
- El comando de importación no debe aceptar una opción `--publicar`.
- La publicación continúa usando exclusivamente `gestionar_version_leccion` y los servicios editoriales.

### 6.1 Idempotencia y concurrencia

- El hash del snapshot se calcula con JSON canónico UTF-8, claves ordenadas y separadores deterministas, siguiendo la estrategia ya usada por `knowledge.py`. La idempotencia compara además las referencias de fuente (rol, uso, localizador y atribución), porque la procedencia no forma parte del hash del snapshot.
- Una segunda importación del mismo contenido no debe crear versiones duplicadas.
- El cálculo del siguiente número de versión y la creación del borrador deben ejecutarse bajo transacción y bloqueo de la fila de lección.
- Las restricciones únicas de base de datos siguen siendo la última defensa ante carreras.
- Si falla la creación de cualquier referencia, se revierte la versión y todas sus asociaciones.

## 7. Revisión de licencias: control obligatorio antes de publicar

El modelo actual guarda `identificador_licencia` y `url_licencia`, pero ambos pueden estar vacíos y no hay un estado verificable de revisión. El comando de registro solo advierte al operador. Esto no basta para el objetivo de contenido trazable.

Antes de implementar publicación masiva, se debe ampliar el registro de fuente con una revisión explícita y auditable. Diseño propuesto:

- Estado: `pendiente`, `compatible`, `solo_referencia`, `requiere_permiso`, `no_reutilizable`.
- Responsable de revisión: usuario editorial activo.
- Fecha de revisión.
- Evidencia: URL exacta de los términos, identificador/licencia, permiso escrito o nota verificable.
- Alcance permitido: atribución, adaptación, fragmentos, redistribución u otras condiciones relevantes.
- Nota de decisión y, si procede, condiciones de atribución.

Reglas de publicación:

1. Una fuente `pendiente` bloquea el paso a revisión/publicación.
2. `compatible` permite reutilización dentro del alcance documentado y con la atribución requerida.
3. `solo_referencia` permite respaldar una explicación original, pero no copiar ni adaptar material protegido.
4. `requiere_permiso` bloquea la publicación hasta registrar evidencia del permiso y revisar su alcance.
5. `no_reutilizable` no puede respaldar material copiado/adaptado; el editor debe retirar ese material o sustituir la fuente.
6. La decisión no se infiere por dominio, protocolo HTTPS ni disponibilidad pública.
7. Al enviar a revisión, cada referencia congela el estado, evidencia, alcance, nota, editor y fecha de revisión de licencia. Esos datos quedan asociados a la versión y no pueden cambiar después; si la decisión de la fuente cambia durante la revisión, aprobación o publicación se bloquea hasta crear/revisar una versión coherente.

La validación de licencia debe residir en el servicio de dominio que envía una versión a revisión y que la publica, no solo en el comando de importación. Así se evita eludir el control mediante otra interfaz o llamada interna.

Este control se implementó inicialmente en las migraciones 0009 y 0010 y requiere validación local de migraciones y pruebas antes de considerarse cerrado.

## 8. Seguridad y privacidad

- El importador solo acepta datos declarativos JSON.
- Rechazar archivos comprimidos en este primer incremento; la validación ZIP corresponde al instalador de paquetes posterior.
- Rechazar symlinks, rutas y nombres de archivo como entradas de datos; no extraer archivos en este incremento.
- No realizar peticiones HTTP al importar.
- No descargar documentación desde URLs incluidas en el paquete.
- No ejecutar ejemplos ni ejercicios.
- No cargar módulos Python ni plugins definidos por el contenido.
- No incluir progreso, intentos, respuestas, preferencias, cuentas ni información personal.
- No modificar claves UUID existentes.
- No escribir en el roadmap curricular.
- Limitar tamaño y profundidad para evitar consumo descontrolado de memoria.
- Informar errores sin volcar respuestas del estudiante ni datos sensibles.

## 9. Comandos previstos

Interfaz de CLI propuesta (nombres sujetos a revisión al implementar):

```bash
python manage.py validar_paquete_contenido --directorio ./contenido/
python manage.py importar_paquete_contenido --directorio ./contenido/ --confirmar
```

El primer comando no escribe datos. El segundo importa borradores y no ofrece publicación automática.

Salida mínima del validador:
- Documentos analizados.
- Lecciones válidas.
- Ejemplos y ejercicios encontrados.
- Fuentes referenciadas.
- Errores bloqueantes con archivo y ruta JSON.
- Advertencias editoriales.
- Duplicados idempotentes.
- Conflictos que requieren decisión humana.

## 10. Matriz de pruebas propuesta

| ID | Caso | Resultado esperado |
|---|---|---|
| IMP-001 | Documento válido con lección y fuente existente | Valida sin escribir datos |
| IMP-002 | JSON mal formado | Error controlado con ubicación |
| IMP-003 | Versión de esquema desconocida | Rechazo |
| IMP-004 | Propiedad desconocida | Rechazo |
| IMP-005 | UUID de lección inexistente | Rechazo |
| IMP-006 | UUID de ejemplo/ejercicio inválido | Rechazo |
| IMP-007 | UUID duplicado dentro del lote | Rechazo |
| IMP-008 | UUID de recurso ligado a otra lección | Rechazo |
| IMP-009 | Fuente inexistente/inactiva | Rechazo |
| IMP-010 | Fuente con licencia pendiente | Advertencia y bloqueo editorial |
| IMP-011 | Teoría o explicación vacía | Rechazo |
| IMP-012 | Tipo o nivel no permitido | Rechazo |
| IMP-013 | Texto que supera el modelo | Rechazo antes de escribir |
| IMP-014 | Documento superior al tamaño máximo | Rechazo antes de parsear completo |
| IMP-015 | Mismo snapshot y procedencia importados dos veces | Idempotencia; no duplica versión |
| IMP-016 | Misma lección con snapshot distinto | Nueva versión borrador; no sobrescribe versiones previas |
| IMP-017 | Error al crear una referencia | Rollback completo del lote |
| IMP-018 | Usuario sin privilegios intenta importar | Rechazo |
| IMP-019 | Importación válida | Crea solo borradores y referencias |
| IMP-020 | Intentos/progreso previos | Permanecen intactos |
| IMP-021 | Contenido con código malicioso como texto | Se almacena como texto; nunca se ejecuta |
| IMP-022 | Dos importaciones concurrentes | Sin números de versión duplicados ni versiones parciales |
| IMP-023 | Fuente `requiere_permiso` sin evidencia | Publicación bloqueada |
| IMP-024 | Fuente `solo_referencia` | Solo permite contenido original y atribución; sin reproducción del material |
| IMP-025 | Intento de publicar borrador importado directamente | Rechazado por el flujo editorial existente |

## 11. Criterios de aceptación del incremento

El importador podrá considerarse implementado cuando:

- El contrato v1 esté versionado y documentado.
- La validación sea determinista y no escriba en la base de datos.
- La importación cree únicamente borradores inmutables con hash y referencias.
- Se rechacen identidades, relaciones, campos y esquemas desconocidos.
- Se detecten duplicados y conflictos sin sobrescritura.
- La revisión de licencia sea auditable y obligatoria antes de publicación, con evidencia congelada por versión.
- Un fallo revierta el lote completo.
- Los datos de estudiantes permanezcan intactos.
- Todos los casos IMP-001 a IMP-025 tengan pruebas automatizadas.
- La suite local completa y las migraciones se validen antes de continuar con el publicador central.

## 12. Fuera de alcance

- Publicar automáticamente o actualizar contenido visible a estudiantes.
- Activar snapshots en las vistas de estudio. La resolución de versión activa requiere un incremento separado y una estrategia de migración de lectura.
- Modificar títulos, orden, relaciones o prerrequisitos de ASCENSO.
- Importar evaluadores ejecutables o scripts.
- Ejecutar código de ejemplos o estudiantes.
- Descargar fuentes o paquetes remotos.
- Crear el servidor central, manifiesto firmado, cliente de sincronización o instalador ZIP.
- Sincronizar datos personales, progreso o intentos.

**Regla de cierre:** importar un documento válido significa crear una propuesta editorial trazable, no certificar que su contenido sea correcto ni hacerlo visible para estudiantes.


## 13. Estado de implementación — 11 de noviembre de 2026

Se incorporó en la rama de trabajo:

- Modelo de revisión de licencia con estado, evidencia HTTPS, alcance, nota, editor responsable y fecha.
- Uso declarado por referencia de fuente.
- Servicio `revisar_licencia_fuente()` y comando `revisar_licencia_fuente`.
- Bloqueo de envío a revisión y publicación para fuentes pendientes, que requieren permiso o no reutilizables.
- Fuentes `compatible` exigen evidencia, auditoría y alcance documentado.
- Fuentes `solo_referencia` solo permiten referencias de contenido original; se bloquean citas, adaptaciones y reproducciones en esta primera política conservadora.
- Validador JSON v1 de solo lectura, con límites, claves estrictas, UUID canónicos, validación contra ASCENSO y detección de duplicados.
- Importador atómico, autorizado solo a editores activos, con creación de borradores, referencias y detección idempotente por hash.
- Comandos `validar_paquete_contenido` e `importar_paquete_contenido`; el segundo exige `--confirmar --usuario` y no ofrece publicación.

**Límites explícitos:** el importador no descarga URLs, no extrae ZIP, no ejecuta código, no modifica los modelos curriculares, no reemplaza contenido editable y no modifica progreso ni intentos. La revisión de licencia es una decisión humana registrada; el sistema no determina automáticamente la legalidad de una licencia.

**Pendiente antes de considerar cerrado el incremento:** ejecutar migraciones, `makemigrations --check --dry-run`, las pruebas de `apps.roadmaps` y la suite completa en el entorno local. Las pruebas nuevas están incorporadas al repositorio, pero no se declaran aprobadas hasta ejecutar esos comandos.
