# Etapa 10 — Bases de datos NoSQL y almacenamiento moderno

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 10.  
**Prioridad oficial:** P1 · Obligatoria; profundización P2 según el propio roadmap.  
**Objetivo oficial:** aprender cuándo utilizar bases relacionales y cuándo utilizar modelos no relacionales.

## Temario oficial

### 10.1. Fundamentos NoSQL
Qué es NoSQL; diferencias SQL vs. NoSQL; modelos de almacenamiento; consistencia; disponibilidad; escalabilidad; CAP Theorem; denormalización.

### 10.2. MongoDB
Documentos; colecciones; BSON; JSON; CRUD; queries; filters; indexes; aggregation pipeline; relationships; embedding; referencing; replication; sharding.

### 10.3. Redis
Key-value; strings; lists; sets; hashes; sorted sets; TTL; cache; sessions; Pub/Sub; rate limiting.

### 10.4. Otras arquitecturas de almacenamiento
Document databases; key-value databases; column-family databases; graph databases; time-series databases.

**Proyecto oficial:** diseñar un sistema que utilice MySQL para datos transaccionales, MongoDB para documentos y Redis para caché, justificando cada decisión.

## Ubicación dentro de la ruta ampliada de bases de datos

El Roadmap Maestro establece que primero debe comprenderse el modelo relacional y dominar SQL; después se estudian modelos documentales y caché. La ampliación de profundidad incluye MongoDB (CRUD, filtros, proyecciones, documentos embebidos y referencias, aggregation pipeline, índices, validación, replicación y sharding), Redis (estructuras, TTL, caché, sesiones, Pub/Sub y rate limiting), y operación real (conexiones, persistencia, seguridad, monitoreo, ORM, migraciones, seeders, pool de conexiones, consultas lentas, respaldos y restauración).

La secuencia práctica indicada por el roadmap es:
1. Modelado relacional y SQL.
2. MySQL.
3. PostgreSQL.
4. MongoDB.
5. Redis.
6. Integración backend.

El criterio de dominio es poder modelar desde requisitos, explicar relaciones, escribir SQL, comprender transacciones y analizar consultas lentas. No basta memorizar comandos.

## Desarrollo granular por lección

Este desglose conserva los 38 títulos oficiales y añade una unidad identificable para cada uno. Los criterios de selección deben justificarse por requisitos y patrones de acceso, no por popularidad del motor.

### 10.1 — Fundamentos NoSQL

#### 10.1.1 — Qué es NoSQL

**Propósito y modelo.** NoSQL agrupa familias de bases de datos no relacionales o no limitadas al modelo tabular clásico. Incluye documentos, clave-valor, columna ancha y grafos. Cada familia optimiza patrones de acceso distintos; NoSQL no significa ausencia de esquema, ausencia de SQL en sentido estricto ni escalabilidad automática.

**Ejemplo desarrollado.** Un catálogo de productos con atributos variables puede encajar en documentos; un carrito efímero puede usar clave-valor; relaciones sociales complejas pueden beneficiarse de grafos. La elección depende de consultas, consistencia, operación y volumen.

**Práctica guiada.** Clasifica cinco escenarios de aplicación según patrón de lectura/escritura, estructura, relaciones y latencia. Justifica una familia candidata y una alternativa.

**Actividad independiente.** Escribe una decisión arquitectónica breve para un sistema de telemetría, indicando por qué una base relacional o NoSQL podría ser adecuada.

**Criterios de aceptación.** Define NoSQL sin generalizaciones y distingue al menos cuatro modelos de datos.

**Errores frecuentes.** Elegir NoSQL solo porque se espera mucho tráfico o asumir que no requiere modelado.

**Comprobación.** ¿Qué patrón de acceso debería guiar la elección de una base NoSQL?

#### 10.1.2 — Diferencias SQL vs. NoSQL

**Propósito y modelo.** Los DBMS relacionales priorizan relaciones explícitas, restricciones y SQL estandarizado con variaciones por motor. Las familias NoSQL ofrecen modelos y APIs diversos, a menudo con diseño orientado a consultas y escalado distribuido. No existe una superioridad universal: transacciones, consistencia y consultas complejas dependen del producto.

**Ejemplo desarrollado.** Un sistema contable puede beneficiarse de restricciones relacionales y transacciones; un catálogo con atributos heterogéneos puede aprovechar documentos. Ambos escenarios requieren validación, índices, respaldo y seguridad.

**Práctica guiada.** Compara un mismo dominio de pedidos en modelo relacional y documental. Identifica duplicación, joins, actualización y consistencia.

**Actividad independiente.** Redacta una matriz de decisión con estructura, transacciones, escalabilidad, consultas, latencia, operación y costo.

**Criterios de aceptación.** Contrasta características reales y justifica elección por requisitos.

**Errores frecuentes.** Afirmar que NoSQL no soporta transacciones o que SQL no puede escalar horizontalmente.

**Comprobación.** ¿Qué requisitos del dominio pueden hacer preferible un modelo relacional aunque el volumen de datos sea alto?

#### 10.1.3 — Modelos de almacenamiento

**Propósito y modelo.** Las principales familias NoSQL incluyen documentos (JSON/BSON), clave-valor, columna ancha y grafos. También existen motores de series temporales, búsqueda y almacenamiento de objetos, con solapamientos funcionales. El modelo determina cómo se organizan datos, índices y operaciones.

**Ejemplo desarrollado.** Redis es clave-valor con estructuras de datos; MongoDB es documental; Cassandra es columna ancha; Neo4j es grafo. Cada producto posee capacidades y límites específicos que deben revisarse en su documentación.

**Práctica guiada.** Asocia un producto conocido con su modelo principal y un patrón de consulta característico. Identifica al menos un caso donde la categoría no explica todas las capacidades.

**Actividad independiente.** Diseña almacenamiento para sesiones, catálogo, red de dependencias y métricas temporales; justifica modelo por patrón de acceso.

**Criterios de aceptación.** Distingue modelos y evita clasificar todos los sistemas no relacionales como equivalentes.

**Errores frecuentes.** Confundir columna ancha con columnas de una tabla relacional o asumir que todo documento es JSON sin esquema.

**Comprobación.** ¿Por qué el modelo clave-valor puede ser eficiente para búsquedas por identificador, pero limitado para consultas ad hoc complejas?

#### 10.1.4 — Consistencia

**Propósito y modelo.** Consistencia en sistemas distribuidos puede referirse a garantías de lectura/escritura entre réplicas y también a reglas de integridad del dominio; son conceptos relacionados pero no idénticos. Strong consistency, eventual consistency y consistencia causal describen comportamientos distintos. Deben especificarse por operación y producto.

**Ejemplo desarrollado.** Tras escribir en una réplica, una lectura desde otra puede devolver un valor anterior bajo consistencia eventual. La aplicación debe decidir si tolera ese retraso o necesita confirmación fuerte para una operación crítica.

**Práctica guiada.** Analiza una secuencia de escritura y lecturas sobre dos réplicas. Identifica qué resultado sería permitido por consistencia eventual y cuál requeriría garantía más fuerte.

**Actividad independiente.** Clasifica operaciones de una tienda como tolerantes a retraso (contador de vistas) o sensibles (saldo, inventario) y define requisitos de consistencia.

**Criterios de aceptación.** Distingue consistencia de dominio y consistencia distribuida; explica eventual consistency con un escenario.

**Errores frecuentes.** Tratar eventual consistency como pérdida de datos o asumir que una confirmación de escritura garantiza visibilidad inmediata en todas las réplicas.

**Comprobación.** ¿Qué decisión de producto debe tomarse cuando una lectura puede observar datos temporalmente desactualizados?

#### 10.1.5 — Disponibilidad

**Propósito y modelo.** Disponibilidad describe la capacidad de un sistema para responder dentro de condiciones y tiempos definidos. En sistemas distribuidos se busca continuidad ante fallos de nodos o zonas mediante replicación, detección, failover y recuperación. Alta disponibilidad no equivale a cero pérdida de datos ni elimina mantenimiento.

**Ejemplo desarrollado.** Tres nodos distribuidos en dominios de fallo pueden tolerar ciertos fallos de nodo, pero no necesariamente una interrupción de red entre zonas o un error lógico replicado a todos los nodos.

**Práctica guiada.** Dibuja una arquitectura de tres nodos y marca qué fallos tolera y cuáles no. Define RTO y RPO para el servicio.

**Actividad independiente.** Diseña plan de continuidad para un servicio de catálogo y uno de pagos, diferenciando disponibilidad requerida y consistencia de datos.

**Criterios de aceptación.** Define disponibilidad, identifica dominios de fallo y diferencia RTO de RPO.

**Errores frecuentes.** Considerar réplicas como backups o asumir que failover automático resuelve corrupción lógica.

**Comprobación.** ¿Por qué una réplica no sustituye a una copia de seguridad independiente?

#### 10.1.6 — Escalabilidad

**Propósito y modelo.** Escalabilidad es la capacidad de mantener niveles de servicio al aumentar carga o datos. Escalado vertical añade recursos a un nodo; horizontal distribuye carga entre nodos. Ambos tienen límites y costos. El diseño debe identificar cuellos de botella, particionamiento, consistencia, replicación y complejidad operativa.

**Ejemplo desarrollado.** Aumentar RAM puede acelerar un motor hasta que el cuello de botella sea CPU o I/O. Añadir nodos puede aumentar capacidad de lectura, pero requiere distribuir datos y coordinar escrituras.

**Práctica guiada.** Analiza una curva sintética de latencia y throughput bajo carga creciente. Identifica saturación y plantea si conviene escalar vertical u horizontalmente.

**Actividad independiente.** Diseña una estrategia para un servicio con crecimiento de 10x, definiendo métricas, límites y umbrales de escalado.

**Criterios de aceptación.** Diferencia escalado vertical/horizontal y relaciona estrategia con patrón de carga.

**Errores frecuentes.** Añadir nodos sin resolver consultas ineficientes o confundir replicación con particionamiento.

**Comprobación.** ¿Qué complejidad adicional introduce el escalado horizontal en comparación con aumentar recursos de un único nodo?

#### 10.1.7 — CAP Theorem

**Propósito y modelo.** El teorema CAP describe una elección bajo partición de red en sistemas distribuidos: no se puede garantizar simultáneamente consistencia fuerte y disponibilidad total ante una partición, manteniendo tolerancia a particiones. En operación real, la partición es un evento que debe contemplarse; las categorías CP/AP simplifican decisiones de diseño y no describen por sí solas todos los modos del producto.

**Ejemplo desarrollado.** Ante pérdida de comunicación entre réplicas, un sistema CP puede rechazar o demorar algunas operaciones para preservar consistencia; uno AP puede aceptar operaciones localmente y reconciliar después, exponiendo lecturas divergentes temporalmente.

**Práctica guiada.** Dibuja tres nodos separados por una partición y evalúa qué operaciones se aceptan en cada política. Distingue tolerancia a partición de alta disponibilidad general.

**Actividad independiente.** Clasifica operaciones de un sistema de inventario y mensajería según preferencia ante partición, justificando impacto de negocio.

**Criterios de aceptación.** Enuncia CAP con la condición de partición y evita afirmar que el sistema siempre elige solo dos propiedades en condiciones normales.

**Errores frecuentes.** Interpretar CAP como una clasificación permanente de producto o confundir consistencia con disponibilidad de servicio HTTP.

**Comprobación.** ¿Por qué CAP se analiza específicamente cuando existe una partición de red?

#### 10.1.8 — Denormalización

**Propósito y modelo.** Denormalización introduce duplicación o estructuras derivadas para optimizar lecturas, reducir joins o adaptar datos a un patrón de consulta. Debe existir una fuente de verdad, estrategia de actualización, reconciliación y monitoreo de divergencias. No es una solución inicial a consultas lentas sin medición.

**Ejemplo desarrollado.** Un documento de pedido puede incluir una instantánea de dirección y nombre del cliente al momento de compra, aunque esos datos existan en una entidad separada. La duplicación preserva contexto histórico y evita lecturas adicionales.

**Práctica guiada.** Compara un modelo normalizado y uno desnormalizado para un reporte de pedidos. Identifica qué datos se duplican y qué evento debe actualizarlos.

**Actividad independiente.** Diseña una proyección de lectura para un dashboard y define cómo reconstruirla si se desincroniza.

**Criterios de aceptación.** Justifica la duplicación por patrón de acceso y documenta consistencia, actualización y reparación.

**Errores frecuentes.** Denormalizar antes de medir, duplicar datos sin propietario o asumir que las copias se mantienen sincronizadas automáticamente.

**Comprobación.** ¿Qué mecanismo mantiene coherente una proyección desnormalizada cuando cambia la fuente de verdad?

### 10.2 — MongoDB

#### 10.2.1 — Documentos

**Propósito y modelo.** Una base documental almacena registros como documentos, comúnmente JSON o BSON, con campos anidados y arreglos. El diseño se orienta a agregados y patrones de consulta; no elimina la necesidad de definir validaciones, índices, relaciones y políticas de actualización.

**Ejemplo desarrollado.** Un documento de pedido puede incluir datos de dirección como instantánea y líneas de pedido embebidas. La decisión evita joins frecuentes, pero puede duplicar información y generar documentos grandes.

**Práctica guiada.** Diseña un documento JSON para Pedido con identificador, fecha, cliente, dirección histórica y líneas. Valida estructura, tipos y campos obligatorios.

**Actividad independiente.** Compara un documento embebido y otro normalizado para el mismo dominio y determina qué consultas favorece cada diseño.

**Criterios de aceptación.** Explica documento, campos, anidamiento y límites de tamaño según motor; justifica estructura por patrón de acceso.

**Errores frecuentes.** Embutir relaciones ilimitadas o asumir que un documento no necesita esquema ni validación.

**Comprobación.** ¿Qué ventaja y qué costo introduce embutir líneas de pedido dentro del documento Pedido?

#### 10.2.2 — Colecciones

**Propósito y modelo.** Una colección agrupa documentos relacionados y suele ser equivalente conceptual —no estricta— a una tabla. Los documentos pueden variar en campos, pero una estructura heterogénea sin reglas dificulta consultas y mantenimiento. Las colecciones pueden tener índices y validadores según DBMS.

**Ejemplo desarrollado.** Una colección clientes puede almacenar documentos con campos comunes y subdocumentos opcionales. El validador puede exigir email y fecha_creacion aunque algunos atributos sean variables.

**Práctica guiada.** Define colección para dispositivos IoT y propone campos obligatorios, opcionales y tipos. Diseña un validador conceptual para rechazar valores inválidos.

**Actividad independiente.** Establece convención de colecciones para una aplicación y documenta límites entre datos operativos, auditoría y eventos.

**Criterios de aceptación.** Diferencia colección y documento y define reglas de consistencia de estructura.

**Errores frecuentes.** Crear una colección por usuario o mezclar tipos de documentos incompatibles sin un discriminador claro.

**Comprobación.** ¿Por qué una colección documental también necesita un contrato de estructura?

#### 10.2.3 — BSON

**Propósito y modelo.** BSON es una representación binaria de documentos utilizada por MongoDB. Incluye tipos adicionales y metadatos de longitud que no existen de la misma forma en JSON textual, como ObjectId, fechas y datos binarios. La representación en wire/storage no debe confundirse con el JSON que se intercambia en APIs.

**Ejemplo desarrollado.** Un campo _id puede contener ObjectId, mientras una fecha BSON se almacena como valor temporal tipado. Serializar a JSON extendido puede requerir representación especial para conservar tipos.

**Práctica guiada.** Compara un documento JSON con su representación JSON extendida para ObjectId y fecha. Identifica campos que perderían tipo si se convierten a cadenas sin convención.

**Actividad independiente.** Define un contrato de intercambio entre API JSON y MongoDB que preserve fechas, identificadores y decimales.

**Criterios de aceptación.** Explica por qué BSON no es simplemente JSON comprimido y reconoce tipos adicionales.

**Errores frecuentes.** Tratar ObjectId como secreto o convertir fechas a texto local sin zona horaria.

**Comprobación.** ¿Qué ventaja aporta conservar tipos nativos frente a almacenar todos los valores como cadenas?

#### 10.2.4 — JSON

**Propósito y modelo.** JSON es un formato textual de intercambio de datos con objetos, arreglos, cadenas, números, booleanos y null. No define por sí solo esquema, tipos de fecha, referencias ni reglas de negocio. Los consumidores deben validar estructura y limitar tamaño/profundidad para evitar errores y abuso.

**Ejemplo desarrollado.** Un objeto JSON puede representar pedido con arreglo de líneas. Las claves son cadenas; los números no deben utilizarse para identificadores largos si el consumidor pierde precisión numérica.

**Práctica guiada.** Escribe un documento JSON válido y valida sintaxis con herramienta local. Prueba errores de coma, comillas y tipos; no incluyas datos personales.

**Actividad independiente.** Diseña esquema de JSON para un evento de auditoría con versión, timestamp UTC, actor seudónimo y atributos permitidos.

**Criterios de aceptación.** Distingue objeto/arreglo/tipo primitivo y valida sintaxis y contrato semántico.

**Errores frecuentes.** Suponer que JSON admite comentarios o fechas nativas, o confiar en datos recibidos sin validación.

**Comprobación.** ¿Qué diferencia existe entre que un JSON sea sintácticamente válido y que cumpla el contrato de una aplicación?

#### 10.2.5 — CRUD

**Propósito y modelo.** CRUD representa Create, Read, Update y Delete, las operaciones básicas sobre documentos. En MongoDB se implementan con métodos de inserción, consulta, actualización y eliminación. Deben considerarse filtros, atomicidad por documento, concurrencia, validación y autorización.

**Ejemplo desarrollado.** insertOne crea un documento; find consulta; updateOne modifica campos mediante operadores; deleteOne elimina una coincidencia. Los filtros deben identificar el conjunto exacto de documentos.

**Práctica guiada.** En una instancia local o entorno de prueba crea una colección y ejecuta CRUD sobre documentos sintéticos. Antes de borrar, ejecuta el mismo filtro con find y revisa coincidencias.

**Actividad independiente.** Construye secuencia CRUD para inventario con validación, manejo de errores y registro de operaciones.

**Criterios de aceptación.** Ejecuta operaciones sobre datos ficticios y demuestra alcance correcto de filtros.

**Errores frecuentes.** Ejecutar updateMany/deleteMany con filtros vacíos o construir consultas concatenando entrada sin validación.

**Comprobación.** ¿Qué verificación previa reduce el riesgo de borrar documentos no previstos?

#### 10.2.6 — Queries

**Propósito y modelo.** Las consultas documentales seleccionan documentos mediante filtros y proyecciones. Pueden combinar condiciones, operadores de comparación, existencia, arreglos y campos anidados. El rendimiento depende de índices y selectividad; una consulta funcionalmente correcta puede ser costosa.

**Ejemplo desarrollado.** Un filtro por estado y fecha puede recuperar pedidos abiertos de un periodo. La proyección devuelve solo los campos necesarios y reduce transferencia.

**Práctica guiada.** Construye consultas con igualdad, rangos, AND/OR y campos anidados sobre una colección sintética. Compara filtro completo y proyección.

**Actividad independiente.** Define consultas para tablero de pedidos y explica índices necesarios y límites de paginación.

**Criterios de aceptación.** Expresa filtros precisos y limita campos y resultados.

**Errores frecuentes.** Utilizar consultas sin límites sobre colecciones grandes o suponer que la consulta por campo anidado es equivalente a una columna relacional indexada.

**Comprobación.** ¿Por qué una proyección puede reducir costos aunque el filtro encuentre las mismas filas?

#### 10.2.7 — Filters

**Propósito y modelo.** Los filtros de MongoDB usan operadores como $eq, $gt, $gte, $in, $exists, $and, $or y expresiones sobre arreglos. Los tipos importan: comparar número con cadena no es equivalente. La semántica de campos ausentes y null debe probarse explícitamente.

**Ejemplo desarrollado.** `{ precio: { $gte: 10, $lt: 50 } }` selecciona valores dentro de un rango numérico; `{ campo: null }` puede coincidir con null y, según consulta, campos ausentes, por lo que se requiere cuidado.

**Práctica guiada.** Crea documentos con campo ausente, null, número y cadena. Ejecuta filtros con $exists, igualdad y rangos y documenta diferencias.

**Actividad independiente.** Diseña filtros para pedidos con estado, fecha, etiquetas y monto, incluyendo datos incompletos.

**Criterios de aceptación.** Interpreta operadores y distingue null de campo ausente y de tipo incompatible.

**Errores frecuentes.** No validar tipos, asumir semántica SQL de NULL o utilizar $where innecesariamente.

**Comprobación.** ¿Por qué conviene diferenciar un campo ausente de un campo presente con valor null?

#### 10.2.8 — Indexes

**Propósito y modelo.** Los índices MongoDB mantienen estructuras para acelerar consultas y ordenamientos. Tipos comunes incluyen índices simples, compuestos, multikey, geoespaciales, textuales y TTL. Cada índice ocupa memoria/disco y añade costo de escritura; la selección debe basarse en consultas reales y explain.

**Ejemplo desarrollado.** Un índice compuesto {cliente_id:1, fecha:-1} puede apoyar consultas por cliente y fecha descendente. El orden de campos afecta prefijos útiles y sort.

**Práctica guiada.** En una colección de prueba ejecuta explain para una consulta antes y después de un índice. Observa winningPlan, keysExamined y docsExamined cuando estén disponibles.

**Actividad independiente.** Propón índices para tres consultas frecuentes y explica impacto de cada uno en escrituras y almacenamiento.

**Criterios de aceptación.** Justifica índice por patrón de consulta y valida plan con datos representativos.

**Errores frecuentes.** Indexar todos los campos o creer que la presencia de índice garantiza un plan eficiente.

**Comprobación.** ¿Qué costo operativo tiene mantener muchos índices en una colección con escrituras frecuentes?

#### 10.2.9 — Aggregation Pipeline

**Propósito y modelo.** El Aggregation Pipeline procesa documentos mediante etapas como $match, $project, $group, $sort, $unwind y $lookup. El orden de etapas influye en volumen procesado y rendimiento; $match temprano puede reducir documentos que atraviesan el pipeline, cuando la semántica lo permite.

**Ejemplo desarrollado.** Un pipeline puede filtrar pedidos por fecha, agrupar por cliente y sumar totales. $unwind transforma elementos de un arreglo en documentos separados, alterando cardinalidad.

**Práctica guiada.** Construye pipeline sobre datos sintéticos con $match, $group y $sort. Cuenta documentos antes y después de $unwind.

**Actividad independiente.** Diseña reporte de ventas por mes y categoría; incluye manejo de campos faltantes y verifica resultados manualmente con un conjunto pequeño.

**Criterios de aceptación.** Explica etapas y cambios de cardinalidad y valida agregados.

**Errores frecuentes.** Aplicar $unwind sin comprender duplicación de documentos o agrupar antes de filtrar innecesariamente.

**Comprobación.** ¿Qué cambia en el número de documentos cuando se aplica $unwind a un arreglo con varios elementos?

#### 10.2.10 — Relationships

**Propósito y modelo.** Las relaciones entre documentos pueden representarse mediante embedding (datos anidados) o referencing (identificadores relacionados). La elección depende de cardinalidad, frecuencia de lectura, actualización, tamaño, consistencia y ciclo de vida. No existe una regla única de «embebido siempre».

**Ejemplo desarrollado.** Dirección histórica de un pedido puede embebirse para preservar el contexto; una colección de comentarios ilimitados puede referenciarse para evitar crecimiento de documento.

**Práctica guiada.** Modela relación Usuario–Dirección y Pedido–Líneas. Para cada una decide embedding o referencia y explica patrón de acceso.

**Actividad independiente.** Diseña modelo documental para curso y estudiantes con matrículas, historial y cambios frecuentes.

**Criterios de aceptación.** Justifica representación según cardinalidad, crecimiento y consistencia.

**Errores frecuentes.** Embutir arreglos ilimitados o duplicar datos mutables sin estrategia de sincronización.

**Comprobación.** ¿Qué criterio ayuda a decidir si una relación debe embebirse o referenciarse?

#### 10.2.11 — Embedding

**Propósito y modelo.** Embedding guarda subdocumentos o arreglos dentro del documento principal. Favorece lecturas agregadas y actualizaciones atómicas dentro de un documento, pero puede duplicar datos y aumentar tamaño. Debe considerarse límite de documento, crecimiento y frecuencia de modificación.

**Ejemplo desarrollado.** Las líneas de un pedido pueden embebirse porque se consultan junto con el pedido y tienen ciclo de vida relacionado. Un historial ilimitado de eventos no es adecuado si provoca crecimiento sin límite.

**Práctica guiada.** Diseña documento Pedido con líneas embebidas y calcula cómo crece al añadir elementos. Identifica campos mutables y campos históricos.

**Actividad independiente.** Evalúa embedding de direcciones de usuario frente a direcciones históricas de pedido; justifica consistencia y retención.

**Criterios de aceptación.** Explica beneficios y límites y demuestra que el tamaño/cantidad de elementos está acotado.

**Errores frecuentes.** Embutir relaciones N:M de gran tamaño o repetir datos cambiantes sin reconciliación.

**Comprobación.** ¿Por qué un arreglo embebido que crece sin límite puede convertirse en un problema de diseño?

#### 10.2.12 — Referencing

**Propósito y modelo.** Referencing almacena identificadores de otros documentos y recupera datos mediante consultas adicionales o $lookup. Reduce duplicación y permite colecciones independientes, pero puede aumentar operaciones de lectura y requiere gestionar referencias huérfanas y consistencia entre documentos.

**Ejemplo desarrollado.** Una orden puede almacenar cliente_id en vez de copiar todo el perfil. Si el perfil cambia, las consultas reflejan el dato actual, mientras la dirección histórica de compra quizá deba conservarse como snapshot embebido.

**Práctica guiada.** Modela Cliente y Pedido en colecciones separadas y construye consulta conceptual que recupere ambos. Considera qué sucede si el cliente se elimina.

**Actividad independiente.** Diseña estrategia de borrado lógico, integridad referencial a nivel aplicación y detección de referencias huérfanas.

**Criterios de aceptación.** Explica ventajas y costos y define manejo de referencias inválidas.

**Errores frecuentes.** Asumir que el DBMS impone automáticamente FK entre colecciones o realizar N+1 consultas sin evaluar rendimiento.

**Comprobación.** ¿Qué responsabilidad adicional asume la aplicación cuando modela relaciones mediante referencias?

#### 10.2.13 — Replication

**Propósito y modelo.** La replicación mantiene copias de datos en varios nodos para disponibilidad, redundancia y distribución de lecturas. En MongoDB, replica sets eligen un primario y mantienen secundarios mediante oplog. La consistencia observable depende de read concern, write concern, preferencias de lectura y estado de replicación.

**Ejemplo desarrollado.** Una escritura confirmada con una política de write concern limitada puede no estar replicada en todos los secundarios. Una lectura desde secundario puede observar retraso.

**Práctica guiada.** Dibuja un replica set de tres miembros con primario, secundarios y elección. Describe qué ocurre ante caída del primario, sin desplegar nodos en producción.

**Actividad independiente.** Define política de write concern/read concern para un catálogo y para registros financieros; justifica disponibilidad y durabilidad.

**Criterios de aceptación.** Explica elección, replicación y retraso; diferencia réplica de backup.

**Errores frecuentes.** Considerar secundarios como copias de seguridad o asumir que todas las escrituras están inmediatamente disponibles en cada réplica.

**Comprobación.** ¿Por qué una replicación activa no protege frente a una eliminación lógica accidental propagada a todos los nodos?

#### 10.2.14 — Sharding

**Propósito y modelo.** Sharding distribuye documentos entre shards usando una shard key. Permite escalar capacidad horizontal y distribuir carga, pero introduce complejidad de enrutamiento, balanceo, transacciones y operación. La elección de shard key afecta cardinalidad, distribución, monotonicidad y consultas frecuentes.

**Ejemplo desarrollado.** Una shard key monotónica puede concentrar nuevas escrituras en un único shard; una clave de alta cardinalidad y distribución adecuada puede repartirlas mejor, aunque dificulte consultas sin la clave.

**Práctica guiada.** Compara tres shard keys hipotéticas para eventos: timestamp, tenant_id y hash de identificador. Evalúa distribución, consultas y riesgo de hotspots.

**Actividad independiente.** Diseña estrategia de sharding para un SaaS multi-tenant y explica cómo se manejan tenants grandes y consultas globales.

**Criterios de aceptación.** Justifica shard key y describe trade-offs de distribución y enrutamiento.

**Errores frecuentes.** Elegir shard key solo por unicidad o creer que sharding mejora automáticamente cualquier consulta.

**Comprobación.** ¿Qué es un hotspot y cómo puede producirlo una shard key mal elegida?

### 10.3 — Redis

#### 10.3.1 — Key-value

**Propósito y modelo.** El modelo clave-valor asocia una clave única con un valor opaco o estructurado para el motor. Es eficiente cuando la aplicación conoce la clave exacta, pero ofrece consultas por atributos limitadas en comparación con modelos relacionales o documentales. Diseño de claves, expiración y tamaño de valor son decisiones importantes.

**Ejemplo desarrollado.** Una sesión puede almacenarse bajo una clave namespaced como session:token-id y un valor con estado serializado. La clave debe ser impredecible y el contenido no debe incluir secretos innecesarios.

**Práctica guiada.** Diseña convención de claves para sesiones, caché y contadores. Identifica colisiones, expiración y separación por entorno.

**Actividad independiente.** Compara clave-valor con tabla relacional para almacenar preferencias de usuario y explica consultas que cada modelo soporta.

**Criterios de aceptación.** Explica lookup por clave y justifica esquema de nombres, TTL y tamaño.

**Errores frecuentes.** Utilizar claves sin namespace o asumir que una base clave-valor puede responder eficientemente cualquier consulta por campos internos.

**Comprobación.** ¿Qué limitación aparece cuando el sistema necesita buscar valores por atributos y no conoce la clave?

#### 10.3.2 — Strings

**Propósito y modelo.** Redis Strings almacena secuencias de bytes y soporta operaciones de lectura/escritura, incremento atómico y expiración. Puede guardar texto, números codificados o datos binarios; el cliente debe definir serialización y límites de tamaño. Las operaciones atómicas ayudan a evitar carreras en contadores simples.

**Ejemplo desarrollado.** INCR contador:visitas incrementa un contador atómicamente; SET clave valor EX 60 guarda un valor con expiración. La atomicidad de comando no equivale a transacción de negocio completa.

**Práctica guiada.** En Redis de laboratorio ejecuta SET, GET, INCR y TTL sobre claves con prefijo lab:. Comprueba expiración y elimina únicamente tus claves de práctica.

**Actividad independiente.** Diseña un contador de solicitudes por minuto con expiración y analiza qué pasa cuando varios clientes incrementan simultáneamente.

**Criterios de aceptación.** Explica almacenamiento de bytes, operaciones atómicas y TTL; evita claves compartidas con datos reales.

**Errores frecuentes.** Guardar objetos complejos sin versión de serialización o usar un contador como registro financiero durable sin respaldo.

**Comprobación.** ¿Qué ventaja ofrece INCR frente a leer, incrementar en la aplicación y volver a escribir?

#### 10.3.3 — Lists

**Propósito y modelo.** Redis Lists almacena secuencias ordenadas de valores y permite inserción/eliminación en extremos y operaciones de cola. Puede utilizarse para colas sencillas, pero el diseño debe contemplar confirmación, reintentos, duplicados y pérdida de consumidores. Para colas robustas pueden convenir Redis Streams o sistemas especializados.

**Ejemplo desarrollado.** LPUSH agrega trabajo a un extremo y RPOP lo retira del otro, formando una cola FIFO según combinación de operaciones. Si un consumidor falla después de retirar un elemento, puede perderse salvo que se implemente mecanismo de recuperación.

**Práctica guiada.** En instancia de laboratorio crea una lista lab:queue, inserta tres elementos y observa orden con LRANGE y operaciones de extremos.

**Actividad independiente.** Diseña cola de tareas con política de reintento, visibilidad, idempotencia y registro de errores; identifica por qué una lista simple puede no bastar.

**Criterios de aceptación.** Explica orden, operaciones de extremos y riesgo de pérdida al consumir.

**Errores frecuentes.** Confundir pop con confirmación durable o asumir entrega exactamente una vez sin mecanismo adicional.

**Comprobación.** ¿Qué ocurre si un consumidor retira una tarea y se cae antes de procesarla?

#### 10.3.4 — Sets

**Propósito y modelo.** Redis Sets almacena valores únicos sin orden definido y soporta operaciones de pertenencia, unión, intersección y diferencia. Es útil para etiquetas, conjuntos de permisos temporales o membresías, siempre que se consideren cardinalidad y memoria.

**Ejemplo desarrollado.** SADD grupo:lab usuario1 usuario2 crea membresías; SISMEMBER verifica pertenencia. SINTER permite obtener elementos compartidos por dos conjuntos.

**Práctica guiada.** Crea dos sets sintéticos y ejecuta SADD, SISMEMBER, SCARD, SINTER y SDIFF. Elimina solo claves del namespace lab:.

**Actividad independiente.** Modela etiquetas de productos y grupos de usuarios y define operaciones frecuentes de unión e intersección.

**Criterios de aceptación.** Distingue unicidad de orden y aplica operaciones de conjuntos correctamente.

**Errores frecuentes.** Depender del orden de iteración o utilizar Sets para datos que requieren valores repetidos o atributos por elemento.

**Comprobación.** ¿Por qué un Set no es adecuado cuando cada elemento necesita almacenar atributos adicionales asociados?

#### 10.3.5 — Hashes

**Propósito y modelo.** Redis Hash almacena pares campo-valor bajo una clave y es útil para representar objetos pequeños y modificables por campo. Los valores son cadenas de bytes; no hay esquema relacional ni validación automática de tipos. Deben definirse convenciones, versionado y límites.

**Ejemplo desarrollado.** HSET usuario:42 nombre Ana estado activo guarda campos; HGET obtiene uno y HGETALL recupera todos. La clave debe estar namespaced y los datos personales deben minimizarse y protegerse.

**Práctica guiada.** Crea hash lab:usuario:1 con campos ficticios, consulta HGET/HGETALL y aplica expiración a la clave.

**Actividad independiente.** Diseña un hash para estado temporal de proceso y explica cuándo conviene documento MongoDB o fila SQL en su lugar.

**Criterios de aceptación.** Diferencia hash Redis de función hash criptográfica y explica estructura campo-valor.

**Errores frecuentes.** Guardar grandes objetos sin límite o confundir Redis Hash con hash de contraseña.

**Comprobación.** ¿Por qué un Redis Hash no sustituye automáticamente a una tabla relacional?

#### 10.3.6 — Sorted Sets

**Propósito y modelo.** Redis Sorted Sets asocia miembros únicos con puntuaciones numéricas y mantiene orden por score. Soporta rankings, colas priorizadas y ventanas temporales. Deben definirse desempates, precisión, actualización de score y expiración; la puntuación no es una identidad.

**Ejemplo desarrollado.** ZADD ranking 150 usuarioA 120 usuarioB agrega puntuaciones; ZREVRANGE obtiene ranking descendente. Si dos miembros tienen igual score, Redis aplica un orden lexicográfico entre miembros en los comandos correspondientes.

**Práctica guiada.** Crea ranking sintético y ejecuta ZADD, ZSCORE, ZRANGE y ZREVRANGE. Actualiza un score y verifica posición.

**Actividad independiente.** Diseña un ranking semanal que elimine o archive puntuaciones antiguas y gestione empates.

**Criterios de aceptación.** Explica score, miembro y orden; define estrategia de desempate.

**Errores frecuentes.** Usar puntuaciones como identificadores o asumir que score conserva precisión decimal arbitraria.

**Comprobación.** ¿Qué sucede cuando dos miembros tienen la misma puntuación en un Sorted Set?

#### 10.3.7 — TTL

**Propósito y modelo.** TTL define el tiempo restante antes de que una clave expire. Es útil para caché, sesiones y datos temporales. La expiración no debe utilizarse como único mecanismo de cumplimiento legal o borrado seguro; la persistencia, réplicas, snapshots y backups pueden conservar copias según configuración.

**Ejemplo desarrollado.** SET clave valor EX 300 establece cinco minutos. TTL informa segundos restantes, -1 puede indicar ausencia de expiración y -2 clave inexistente, según comando y estado.

**Práctica guiada.** En Redis de laboratorio asigna TTL a una clave lab:, consulta con TTL y espera expiración. No uses claves de otros usuarios.

**Actividad independiente.** Define TTL para caché, token de recuperación y sesión; justifica duración y revocación anticipada.

**Criterios de aceptación.** Interpreta TTL y explica diferencia entre expiración y borrado garantizado de todas las copias.

**Errores frecuentes.** Asumir que TTL es un reloj exacto de ejecución o almacenar secretos de larga duración sin renovación/revocación.

**Comprobación.** ¿Por qué una expiración de clave no equivale necesariamente a eliminación inmediata de todas las copias persistentes?

#### 10.3.8 — Cache

**Propósito y modelo.** Una caché guarda temporalmente resultados para reducir latencia o carga sobre una fuente de verdad. Las estrategias incluyen cache-aside, write-through y write-behind. La invalidación, TTL, consistencia y protección frente a cache stampede son parte del diseño.

**Ejemplo desarrollado.** En cache-aside, la aplicación consulta Redis; si falta el dato, lee SQL, lo almacena con TTL y devuelve el resultado. Al actualizar la fuente debe invalidar o refrescar la clave.

**Práctica guiada.** Dibuja cache hit y cache miss para una ficha de producto. Identifica qué sucede al actualizar el precio en la base principal.

**Actividad independiente.** Diseña estrategia de caché para catálogo con TTL, invalidación, claves versionadas y comportamiento cuando Redis no está disponible.

**Criterios de aceptación.** Distingue fuente de verdad y caché y define política de coherencia.

**Errores frecuentes.** Tratar caché como almacenamiento definitivo o invalidar una clave antes de confirmar la escritura en la fuente de verdad sin estrategia de consistencia.

**Comprobación.** ¿Qué problema puede causar un cache stampede cuando una clave muy consultada expira?

#### 10.3.9 — Sessions

**Propósito y modelo.** Una sesión mantiene estado temporal asociado a un usuario o cliente. Redis puede almacenar identificador opaco y datos de sesión con TTL, pero el diseño requiere aleatoriedad criptográfica del token, protección en tránsito, control de acceso, rotación, revocación y no almacenar secretos innecesarios.

**Ejemplo desarrollado.** El navegador conserva un cookie de sesión con atributos Secure, HttpOnly y SameSite; el servidor usa el identificador para recuperar el estado en Redis. El valor no debe contener contraseña ni datos de tarjeta.

**Práctica guiada.** Diseña flujo de inicio/cierre de sesión sin crear credenciales reales. Identifica dónde se genera token, cómo se almacena y cómo se invalida.

**Actividad independiente.** Define política de TTL, renovación, cierre global, detección de reutilización y protección de sesiones.

**Criterios de aceptación.** Explica token opaco, almacenamiento de sesión y revocación; reconoce que Redis no autentica al usuario por sí mismo.

**Errores frecuentes.** Usar identificadores predecibles, exponer Redis públicamente o confiar solo en TTL para revocar sesiones comprometidas.

**Comprobación.** ¿Qué controles impiden que conocer una clave Redis permita a un atacante suplantar directamente a un usuario?

#### 10.3.10 — Pub/Sub

**Propósito y modelo.** Redis Pub/Sub distribuye mensajes efímeros a suscriptores de canales. Los suscriptores desconectados no reciben mensajes publicados mientras no están conectados; no es una cola durable ni garantiza entrega. Para persistencia y replay se requieren mecanismos como Streams u otro broker.

**Ejemplo desarrollado.** Un servicio publica evento en canal notificaciones y clientes conectados lo reciben. Si un cliente está desconectado, el mensaje no queda esperando para él.

**Práctica guiada.** En Redis local abre dos sesiones de laboratorio, suscribe una al canal lab:events y publica un mensaje sintético desde la otra. Comprueba qué ocurre al desconectar el suscriptor.

**Actividad independiente.** Decide entre Pub/Sub, Streams y una cola durable para notificaciones que pueden perderse frente a órdenes que no deben perderse.

**Criterios de aceptación.** Explica publicación/suscripción y ausencia de persistencia/replay del Pub/Sub clásico.

**Errores frecuentes.** Usar Pub/Sub como registro de eventos duradero o publicar datos sensibles en canales accesibles a demasiados roles.

**Comprobación.** ¿Qué limitación presenta Pub/Sub cuando un consumidor está desconectado durante la publicación?

#### 10.3.11 — Rate Limiting

**Propósito y modelo.** Rate limiting limita frecuencia de operaciones por identidad, IP, token o recurso para reducir abuso y proteger capacidad. Puede implementarse con ventana fija, ventana deslizante, token bucket o leaky bucket. Redis permite contadores y operaciones atómicas, pero la implementación debe manejar concurrencia, expiración y distribución.

**Ejemplo desarrollado.** Un contador con TTL limita solicitudes por usuario durante una ventana; incrementos no atómicos o carreras entre INCR y EXPIRE pueden producir resultados incorrectos si no se diseña con script o transacción apropiada.

**Práctica guiada.** Simula en papel una ventana de 60 segundos con límite de 10 solicitudes y compara ventana fija con token bucket. No generes tráfico contra servicios externos.

**Actividad independiente.** Diseña rate limit por usuario y por IP para una API, incluyendo respuestas 429, cabeceras de cuota y tratamiento de clientes legítimos detrás de NAT.

**Criterios de aceptación.** Explica algoritmo, clave de partición, atomicidad y comportamiento de límite superado.

**Errores frecuentes.** Limitar solo por IP sin considerar NAT, usar contadores no atómicos o permitir bypass con múltiples identificadores triviales.

**Comprobación.** ¿Qué ventaja ofrece token bucket frente a una ventana fija para permitir ráfagas controladas?

### 10.4 — Otras arquitecturas de almacenamiento

#### 10.4.1 — Document databases

**Propósito y modelo.** Las bases documentales almacenan registros como documentos con campos, objetos anidados y arreglos. Favorecen agregados consultados juntos y esquemas evolutivos, pero requieren validación, control de crecimiento y decisiones de embedding/referencing. MongoDB es un ejemplo conocido; otros motores difieren en consultas, consistencia e índices.

**Ejemplo desarrollado.** Un documento de perfil puede agrupar preferencias y direcciones activas; el historial de pedidos puede residir en otra colección por volumen y ciclo de vida.

**Práctica guiada.** Modela un perfil JSON y define campos obligatorios, opcionales y validaciones. Identifica qué atributo debería referenciarse por su crecimiento.

**Actividad independiente.** Compara una base documental con un esquema relacional para catálogo multilingüe y explica consultas, actualizaciones y consistencia.

**Criterios de aceptación.** Explica documento y colección y justifica modelado según patrones de acceso.

**Errores frecuentes.** Interpretar esquema flexible como ausencia de contrato o embeber datos ilimitados.

**Comprobación.** ¿Qué criterio permite decidir si un subdocumento debe embebirse o almacenarse por separado?

#### 10.4.2 — Key-value databases

**Propósito y modelo.** Una base clave-valor asocia claves únicas con valores, con operaciones optimizadas para recuperar por clave. Puede ofrecer estructuras adicionales, persistencia y replicación, pero las consultas por atributos internos suelen ser limitadas o dependen de índices específicos.

**Ejemplo desarrollado.** Un servicio de sesiones puede recuperar estado por token opaco. La clave necesita alta entropía, namespace y TTL; el valor debe minimizar datos sensibles.

**Práctica guiada.** Diseña esquema de claves para sesiones, caché y contadores, definiendo expiración, tamaño y política de invalidación.

**Actividad independiente.** Evalúa Redis frente a una tabla SQL para un servicio de rate limiting y justifica latencia, atomicidad y persistencia requerida.

**Criterios de aceptación.** Identifica ventajas y límites de lookup por clave y documenta política de expiración.

**Errores frecuentes.** Suponer que una clave difícil de adivinar sustituye autorización o usar caché como fuente de verdad sin respaldo.

**Comprobación.** ¿Qué patrón de acceso favorece una base clave-valor y cuál resulta menos natural?

#### 10.4.3 — Column-family databases

**Propósito y modelo.** Las bases de datos de familia de columnas o wide-column organizan datos en filas identificadas por clave y conjuntos de columnas agrupadas en familias. Están diseñadas para distribución y grandes volúmenes con patrones de consulta previstos. No equivalen a columnas de una tabla relacional ni a bases columnares analíticas.

**Ejemplo desarrollado.** Cassandra organiza particiones mediante partition key y clustering columns. Una mala clave de partición puede concentrar carga o crear particiones enormes; el modelado suele partir de consultas que deben soportarse.

**Práctica guiada.** Diseña una tabla conceptual para eventos por dispositivo y fecha, identificando partition key y clustering order. Evalúa tamaño y distribución.

**Actividad independiente.** Compara wide-column y relacional para telemetría de alto volumen, incluyendo consistencia, consultas, modelado y operación.

**Criterios de aceptación.** Diferencia wide-column de almacenamiento columnar analítico y justifica claves según consulta.

**Errores frecuentes.** Diseñar primero entidades normalizadas sin patrón de consulta o usar una partition key de baja cardinalidad.

**Comprobación.** ¿Cómo puede una partition key mal elegida generar hotspots en un clúster distribuido?

#### 10.4.4 — Graph databases

**Propósito y modelo.** Las bases de grafos representan entidades como nodos y relaciones como aristas, a menudo con propiedades. Son útiles cuando las consultas recorren relaciones de profundidad variable o patrones conectados. El rendimiento depende de estructura, índices, dirección y cardinalidad de relaciones.

**Ejemplo desarrollado.** Una red social puede modelar Persona-[:SIGUE]->Persona; una consulta de caminos de amigos explora relaciones sin reconstruir múltiples joins manuales.

**Práctica guiada.** Dibuja grafo de usuarios, productos y compras. Identifica nodos, relaciones y propiedades; formula tres preguntas que requieran recorrido de grafo.

**Actividad independiente.** Evalúa una base de grafos para detección de fraude o dependencias de software frente a un modelo relacional.

**Criterios de aceptación.** Distingue nodos/aristas/propiedades y justifica consultas centradas en relaciones.

**Errores frecuentes.** Elegir grafos solo porque existen relaciones o no limitar profundidad y cardinalidad en consultas de recorrido.

**Comprobación.** ¿Qué tipo de consulta puede ser más natural en un grafo que en un modelo tabular?

#### 10.4.5 — Time-series databases

**Propósito y modelo.** Las bases de series temporales optimizan datos asociados a marcas de tiempo, etiquetas y valores medidos. Incorporan funciones de retención, agregación temporal, compresión y downsampling según producto. El diseño debe considerar resolución, cardinalidad de etiquetas, orden de ingestión y consultas por ventana.

**Ejemplo desarrollado.** Métricas de CPU pueden almacenarse por host y timestamp. Una etiqueta por cada solicitud única puede disparar cardinalidad y consumo; conviene elegir dimensiones acotadas.

**Práctica guiada.** Diseña un esquema para métricas de temperatura de sensores con timestamp, sensor_id y valor. Define retención y agregación horaria.

**Actividad independiente.** Compara almacenamiento relacional, wide-column y series temporales para telemetría de 10.000 dispositivos.

**Criterios de aceptación.** Explica puntos temporales, etiquetas, cardinalidad y retención; justifica estrategia de agregación.

**Errores frecuentes.** Crear etiquetas de cardinalidad ilimitada o conservar todas las muestras de alta resolución indefinidamente sin política.

**Comprobación.** ¿Por qué una etiqueta única por evento puede ser problemática en un motor de series temporales?

## Resultados de aprendizaje

Podrás explicar por qué NoSQL no es un único modelo; distinguir bases documentales, clave-valor, columnares, grafos y series temporales; describir compromisos de consistencia y disponibilidad; modelar documentos en MongoDB; ejecutar operaciones CRUD, filtros, proyecciones y agregaciones; decidir entre embedding y referencing; comprender índices, replicación y sharding; utilizar estructuras Redis para caché y sesiones; aplicar TTL, Pub/Sub y rate limiting; y justificar una arquitectura híbrida junto con controles de seguridad, persistencia y recuperación.

## 10.1 — Fundamentos NoSQL

### ¿Qué significa NoSQL?

NoSQL agrupa familias de sistemas de almacenamiento que no siguen necesariamente el modelo relacional clásico. No significa que «no utilicen consultas», que carezcan de esquema o que sean siempre más rápidas.

Familias habituales:
- documental: documentos con campos y estructuras anidadas;
- clave-valor: acceso por una clave a un valor;
- column-family: organización por familias de columnas y particiones;
- grafos: nodos y relaciones como elementos centrales;
- series temporales: datos asociados a marcas temporales y patrones de consulta temporal.

Cada familia responde a necesidades diferentes. La elección debe partir de consultas, consistencia, volumen, latencia, disponibilidad, operación y capacidades del equipo.

### SQL vs. NoSQL

Los sistemas relacionales destacan cuando las relaciones, restricciones, joins y transacciones del dominio son centrales. Las bases NoSQL pueden ser adecuadas cuando el patrón de acceso, la flexibilidad de documentos, la distribución o el modelo de datos lo justifican.

No es una dicotomía absoluta: los motores relacionales modernos incluyen tipos JSON y capacidades especializadas; algunos sistemas NoSQL soportan transacciones y esquemas/validación. Compara capacidades concretas, no etiquetas.

### Modelos de almacenamiento

Un modelo de almacenamiento determina cómo se representan y recuperan los datos. Preguntas para decidir:
- ¿Qué consultas deben ser rápidas?
- ¿Qué datos se actualizan juntos?
- ¿Qué relaciones requieren integridad?
- ¿Cuánto se duplica y cómo se sincroniza?
- ¿Qué consistencia necesita cada operación?
- ¿Qué estrategia de respaldo y recuperación existe?
- ¿Quién administra y monitorea el servicio?

### Consistencia, disponibilidad y escalabilidad

Consistencia describe qué valores observan las lecturas tras escrituras bajo el modelo del sistema. Disponibilidad se refiere a la capacidad de responder solicitudes, según las garantías definidas. Escalabilidad es la capacidad de mantener servicio al aumentar carga, datos o usuarios.

No confundas disponibilidad con consistencia, ni escalabilidad con «añadir servidores» sin considerar particiones, coordinación, coste y operación.

### CAP Theorem

CAP estudia el compromiso entre consistencia y disponibilidad cuando ocurre una partición de red en un sistema distribuido. Ante una partición, un diseño no puede garantizar simultáneamente disponibilidad total y consistencia fuerte en todos los nodos; debe priorizar un comportamiento y documentar sus garantías.

CAP no significa que un sistema elija solo dos de tres propiedades en todo momento. La partición es la condición relevante. Tampoco reemplaza el análisis de latencia, durabilidad, recuperación o consistencia eventual.

### Denormalización

Denormalizar introduce duplicación o estructuras precomputadas para favorecer patrones de lectura. Puede reducir joins y mejorar ciertas consultas, pero aumenta coste de escritura y riesgo de datos divergentes.

Documenta fuente de verdad, estrategia de actualización, invalidación y reconciliación. No dupliques datos sin definir cómo se mantienen coherentes.

## 10.2 — MongoDB

### Documentos, colecciones, JSON y BSON

MongoDB almacena documentos agrupados en colecciones. JSON es una representación textual ampliamente utilizada para intercambio; BSON es una representación binaria de documentos con tipos adicionales y estructura optimizada para el motor.

Un documento puede contener objetos anidados y arrays. La flexibilidad no elimina la necesidad de modelar: define campos, tipos, límites, validación y consultas esperadas.

Ejemplo conceptual:

    {
      "orderNumber": "ORD-1007",
      "customerId": "C-104",
      "status": "paid",
      "items": [
        { "productId": "P-1", "quantity": 2, "unitPrice": 12.50 },
        { "productId": "P-9", "quantity": 1, "unitPrice": 8.00 }
      ]
    }

Es un ejemplo ilustrativo de documento; no representa un esquema oficial ni una recomendación universal.

### CRUD

CRUD significa Create, Read, Update y Delete:
- crear documentos;
- consultar documentos;
- actualizar campos/documentos;
- eliminar documentos.

Antes de actualizar o eliminar, ejecuta una consulta que confirme el filtro y alcance. Evita operaciones sin filtro accidental. En sistemas reales, añade autorización, validación y límites de resultados.

### Queries, filters y projections

Las queries expresan qué documentos recuperar. Los filtros seleccionan documentos por condiciones; las proyecciones limitan los campos devueltos. La proyección reduce transferencia y exposición de datos, pero no sustituye autorización.

Practica igualdad, rangos, existencia de campos, arrays y operadores lógicos con datos ficticios. Comprueba el comportamiento de tipos y valores nulos según el motor.

### Embedding y referencing

**Embedding** guarda datos relacionados dentro del documento. Puede ser útil cuando los datos se consultan juntos y el tamaño/actualización del documento está controlado.

**Referencing** almacena identificadores que apuntan a otros documentos. Puede ser preferible para entidades compartidas, datos grandes, relaciones complejas o actualizaciones independientes.

Criterios:
- frecuencia de lectura conjunta;
- tamaño y crecimiento;
- frecuencia de actualización;
- necesidad de atomicidad;
- cardinalidad;
- duplicación aceptable;
- límites del motor.

No copies todo el modelo relacional literalmente ni anides sin límite.

### Relationships

Las relaciones en MongoDB se representan mediante documentos embebidos o referencias. Los joins entre colecciones tienen mecanismos propios, pero el modelo debe diseñarse según consultas dominantes y consistencia requerida.

### Aggregation Pipeline

El pipeline procesa documentos mediante etapas encadenadas como filtrado, proyección, agrupación, ordenamiento y transformaciones. Cada etapa recibe el resultado de la anterior.

Ejemplo conceptual de etapas:
1. filtrar ventas de un periodo;
2. agrupar por cliente;
3. calcular suma y cantidad;
4. ordenar por total;
5. limitar resultados.

Verifica operadores y sintaxis en la versión concreta. Un pipeline eficiente filtra temprano cuando es semánticamente correcto y utiliza índices adecuados.

### Indexes

Los índices aceleran consultas que coinciden con sus campos y ordenamientos, con coste de almacenamiento y actualización. Los índices compuestos dependen del orden de campos y patrón de consulta. Revisa explain/planes y evita índices redundantes.

### Validación, replicación y sharding

La validación de esquemas define reglas sobre estructura y tipos aceptados; debe combinarse con validación de negocio en la aplicación.

La replicación mantiene copias de datos en varios miembros para tolerancia a fallos y disponibilidad, con garantías y retrasos que dependen de configuración. Sharding distribuye datos entre particiones/nodos para escalar capacidad; requiere elegir clave de shard con cuidado, ya que una mala distribución puede crear hotspots y consultas costosas.

Replicación no es backup y sharding no es una solución automática a consultas mal diseñadas.

## 10.3 — Redis

### Modelo clave-valor y estructuras

Redis ofrece acceso a datos mediante claves y estructuras de datos. Según versión y configuración puede soportar:
- strings;
- lists;
- sets;
- hashes;
- sorted sets.

Selecciona la estructura según operaciones: strings para valores simples/contadores; lists para secuencias; sets para unicidad y pertenencia; hashes para campos de un objeto; sorted sets para elementos ordenados por puntuación.

No guardes datos arbitrarios sin definir formato, tamaño, expiración y estrategia de persistencia.

### TTL

TTL (Time To Live) define cuánto tiempo debe mantenerse una clave antes de expirar. Es útil para caché, códigos temporales y sesiones con duración limitada. Un TTL no reemplaza autorización ni revocación: una sesión sensible también requiere invalidación explícita y controles adecuados.

### Caché

Una caché conserva temporalmente resultados para reducir latencia o carga sobre la fuente principal. Estrategias habituales incluyen cache-aside: la aplicación consulta caché, lee la fuente si no hay dato y después almacena el resultado con expiración.

El problema crítico es invalidación: define qué ocurre cuando la fuente cambia, cómo se evitan datos obsoletos y cómo se controla una avalancha de solicitudes cuando expiran muchas claves.

Redis como caché no debe convertirse accidentalmente en la única copia de datos críticos sin una arquitectura de persistencia y recuperación deliberada.

### Sessions

Redis puede almacenar sesiones o estado temporal de aplicación. Protege el acceso de red, exige autenticación, limita privilegios, define TTL y evita guardar secretos o datos innecesarios. Diseña logout, expiración, rotación y revocación.

### Pub/Sub

Pub/Sub permite publicar mensajes en canales a los que están suscritos clientes. Es útil para notificaciones efímeras, pero no debe asumirse que ofrece almacenamiento durable o entrega a consumidores desconectados. Si el caso requiere historial, confirmaciones o reintentos, evalúa mecanismos de mensajería persistente apropiados.

### Rate limiting

El rate limiting limita la frecuencia de solicitudes por usuario, token, IP u otra identidad. Debe definir ventana, cuota, tratamiento de concurrencia, claves, expiración y respuesta cuando se excede el límite. Considera NAT/proxies, usuarios autenticados y posibles abusos distribuidos.

## 10.4 — Otras arquitecturas de almacenamiento

| Familia | Modelo | Casos donde puede encajar | Consideración |
|---|---|---|---|
| Document database | documentos estructurados | perfiles, catálogos flexibles, contenido | modelar consultas y validación |
| Key-value | clave y valor | caché, estado temporal, lookup | consultas por clave como patrón central |
| Column-family | filas/particiones y familias de columnas | grandes volúmenes distribuidos por patrón | diseño orientado a claves de partición |
| Graph database | nodos y relaciones | redes de relaciones, recomendaciones, rutas | consultas de traversals y modelo de relaciones |
| Time-series | mediciones con tiempo | métricas, sensores, telemetría | retención, agregación y cardinalidad |

La elección requiere evaluar volumen, patrones de acceso, retención, consistencia, coste y capacidades operativas. No elijas una base solo por popularidad.

## Proyecto oficial — Arquitectura híbrida de ventas

### Objetivo

Diseñar una solución que utilice MySQL para datos transaccionales, MongoDB para documentos y Redis para caché, justificando cada decisión y definiendo límites claros entre fuentes de verdad y copias derivadas.

### Responsabilidades sugeridas

- **MySQL:** fuente de verdad para clientes, productos, pedidos/facturas, inventario y pagos que requieren integridad relacional.
- **MongoDB:** documentos complementarios o contenido documental cuyo esquema y patrón de acceso justifiquen el modelo; no dupliques datos transaccionales sin estrategia de sincronización.
- **Redis:** caché de consultas frecuentes o sesiones temporales con TTL e invalidación explícita; no debe ser fuente de verdad de pagos o inventario.

Estas asignaciones son una propuesta didáctica para el proyecto. El diseño final debe justificarse con requisitos y restricciones reales.

### Diseño y ejecución

1. Define requisitos funcionales y no funcionales.
2. Identifica fuente de verdad de cada entidad/dato.
3. Diseña el esquema relacional en MySQL.
4. Diseña documentos MongoDB y decide embedding/referencing.
5. Define claves Redis, estructuras, TTL y política de invalidación.
6. Implementa operaciones de lectura/escritura desde una aplicación de laboratorio.
7. Define qué ocurre si Redis o MongoDB no están disponibles.
8. Documenta consistencia entre sistemas y manejo de fallos parciales.
9. Implementa permisos mínimos, secretos fuera del código y conexiones protegidas.
10. Prueba respaldo y restauración de cada sistema.
11. Mide consultas y carga representativas.
12. Documenta decisiones, límites y alternativas descartadas.

### Casos de prueba obligatorios

- caché miss y cache hit;
- actualización de la fuente y invalidación;
- expiración por TTL;
- indisponibilidad de Redis;
- documento MongoDB inválido;
- consulta de agregación con datos vacíos y grandes;
- duplicación y consistencia de datos derivados;
- usuario sin privilegios suficientes;
- restauración de backup en un entorno aislado;
- recuperación de una operación fallida o parcial.

### Entregables

1. diagrama de arquitectura;
2. modelo relacional y scripts;
3. modelo documental y validación;
4. diseño de claves y estructuras Redis;
5. contratos de integración entre componentes;
6. política de consistencia e invalidación;
7. configuración de seguridad;
8. estrategia de respaldo y recuperación;
9. pruebas y resultados reproducibles;
10. informe de decisión tecnológica.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Comprensión SQL vs. NoSQL y CAP | 15 |
| Modelo y operaciones MongoDB | 20 |
| Redis, TTL, caché y sesiones | 20 |
| Justificación de otras arquitecturas | 10 |
| Integración y consistencia | 15 |
| Seguridad, backups y recuperación | 10 |
| Pruebas y documentación | 10 |

## Ejercicios de comprensión

1. ¿NoSQL significa que no se utiliza un lenguaje de consulta?  
   **Respuesta:** no; agrupa modelos no relacionales y muchos ofrecen lenguajes o APIs de consulta.

2. ¿Qué analiza CAP?  
   **Respuesta:** el compromiso entre consistencia y disponibilidad ante una partición de red.

3. ¿Cuándo puede convenir embedding?  
   **Respuesta:** cuando datos relacionados se leen juntos y su tamaño/actualización está controlado.

4. ¿Cuándo puede convenir referencing?  
   **Respuesta:** cuando entidades se comparten, actualizan independientemente o crecen demasiado para embebido.

5. ¿Qué diferencia hay entre JSON y BSON?  
   **Respuesta:** JSON es una representación textual; BSON es una representación binaria con tipos y estructura propios.

6. ¿Qué hace un aggregation pipeline?  
   **Respuesta:** transforma y analiza documentos mediante etapas encadenadas.

7. ¿Replicación equivale a backup?  
   **Respuesta:** no; replicar propaga cambios y errores, mientras un backup permite recuperar estados protegidos.

8. ¿Qué problema resuelve TTL?  
   **Respuesta:** expira claves tras un periodo definido.

9. ¿Pub/Sub garantiza que un suscriptor desconectado reciba todos los mensajes?  
   **Respuesta:** no debe asumirse; el patrón es de publicación/suscripción y no equivale a una cola durable.

10. ¿Por qué Redis no debe ser la única fuente de verdad de un pago en este proyecto?  
    **Respuesta:** la caché/estado temporal requiere una estrategia de persistencia, consistencia y recuperación; el registro transaccional debe residir en el sistema definido como fuente de verdad.

## Autoevaluación práctica

Justifica con requisitos por qué cada tipo de dato reside en cada motor. Demuestra caché hit/miss, invalidación y TTL. Explica qué ocurre cuando un servicio deja de responder y cómo recuperar datos. Si no puedes explicar fuente de verdad, consistencia, backup y recuperación, el diseño aún no está listo.

## Recursos audiovisuales

No se incluyen videos en esta versión. MongoDB y Redis requieren recursos separados que expliquen sus modelos y comandos con audio hablado en español. Se añadirán solo tras verificar que el material coincide con los objetivos y con la versión documentada.

## Referencias oficiales y técnicas

- MongoDB Manual: https://www.mongodb.com/docs/manual/
- MongoDB Data Modeling: https://www.mongodb.com/docs/manual/data-modeling/
- MongoDB Aggregation: https://www.mongodb.com/docs/manual/aggregation/
- Redis Documentation: https://redis.io/docs/latest/
- Redis Data Types: https://redis.io/docs/latest/develop/data-types/
- Redis Keyspace and expiration: https://redis.io/docs/latest/develop/use/keyspace/
- Redis Pub/Sub: https://redis.io/docs/latest/develop/pubsub/
- Redis Security: https://redis.io/docs/latest/operate/oss_and_stack/management/security/
- PostgreSQL Documentation (comparación relacional): https://www.postgresql.org/docs/
- MySQL Reference Manual (fuente transaccional de la etapa previa): https://dev.mysql.com/doc/refman/8.4/en/

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** diseños, comandos y pruebas propuestos; no ejecutados contra instancias MongoDB/Redis en esta sesión.  
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** cotejo de las entradas oficiales del roadmap, precisión conceptual, secuencia, ejemplos, prácticas, evaluación, seguridad y referencias.

**Resultado:** revisión documental interna realizada con los ajustes y hallazgos siguientes: Se revisó la cobertura de las 38 entradas oficiales, la precisión del teorema CAP, los modelos de datos, MongoDB, Redis y el diseño híbrido. Se identifica solapamiento entre el desarrollo granular y la sección de síntesis posterior; en una pasada de edición final deberá decidirse si se conserva como recapitulación explícita o se fusiona para evitar repetición. Pendiente: ejecutar operaciones CRUD, índices, agregaciones, TTL, Pub/Sub y pruebas de consistencia/recuperación en instancias aisladas.

**Límite de validación:** no se ejecutaron laboratorios, scripts, servicios, bases de datos, máquinas virtuales ni capturas de red en esta revisión. No se declara aprobación académica externa. La etapa continúa en desarrollo hasta completar las pruebas reproducibles y la segunda revisión.
