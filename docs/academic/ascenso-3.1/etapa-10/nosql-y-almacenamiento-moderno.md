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

En MongoDB, un documento es una estructura BSON con campos y valores anidados; su diseño debe responder a las consultas y límites del dominio. **Práctica:** modela un documento de producto con atributos y variantes. **Evidencia:** identifica campos obligatorios, opcionales y reglas de validación.

#### 10.2.2 — Colecciones

Una colección agrupa documentos y puede aplicar validación y opciones de índices; no exige que todos los documentos tengan exactamente los mismos campos. **Práctica:** crea una colección de productos en una instancia local y consulta su listado. **Evidencia:** explica la diferencia entre colección y documento.

#### 10.2.3 — BSON

BSON es una representación binaria de documentos con tipos adicionales a JSON, como fechas y datos binarios. **Práctica:** compara la representación conceptual de una fecha y un número decimal en JSON y BSON. **Evidencia:** explica por qué los tipos BSON importan al serializar y consultar.

#### 10.2.4 — JSON

JSON es un formato textual de intercambio con objetos, arrays, cadenas, números, booleanos y null; no conserva por sí solo tipos de fecha ni binarios específicos. **Práctica:** valida un documento JSON de producto y detecta comas, comillas o tipos inválidos. **Evidencia:** entrega JSON válido y explica qué valores requieren convención adicional.

#### 10.2.5 — CRUD

CRUD resume Create, Read, Update y Delete, operaciones fundamentales de persistencia. **Práctica:** en una base local de laboratorio inserta un documento, léelo, actualiza un campo y elimínalo. **Evidencia:** registra filtros, cantidad afectada y estado después de cada operación.

#### 10.2.6 — Queries

Una query expresa qué documentos recuperar y qué proyección o transformación aplicar. **Práctica:** consulta productos por categoría y proyecta solo nombre y precio. **Evidencia:** explica el filtro y por qué limitar campos puede reducir transferencia.

#### 10.2.7 — Filters

Los filtros combinan condiciones de igualdad, rangos, existencia, arrays y operadores lógicos. **Práctica:** construye una consulta con categoría y rango de precio, y otra con `$and`/`$or`. **Evidencia:** describe qué documentos coinciden y prueba casos límite.

#### 10.2.8 — Indexes

Los índices aceleran consultas al mantener estructuras auxiliares, pero consumen espacio y encarecen escrituras. **Práctica:** crea un índice sobre un campo de consulta frecuente y examina el plan con `explain`. **Evidencia:** compara antes/después y explica selectividad y coste.

#### 10.2.9 — Aggregation Pipeline

Aggregation Pipeline procesa documentos mediante etapas como `$match`, `$project`, `$group`, `$sort` y `$limit`. **Práctica:** agrupa ventas por categoría y calcula suma y cantidad. **Evidencia:** explica el orden de etapas y cómo el filtrado temprano puede reducir trabajo.

#### 10.2.10 — Relationships

Las relaciones entre documentos pueden representarse mediante embedding o referencias; la decisión depende de cardinalidad, frecuencia de lectura y ciclo de vida. **Práctica:** modela cliente-pedidos y explica si cada pedido debe embebirse o almacenarse aparte. **Evidencia:** justifica la estrategia con consultas esperadas.

#### 10.2.11 — Embedding

Embedding almacena datos relacionados dentro del mismo documento y favorece lecturas atómicas de un agregado, pero puede duplicar datos y acercarse a límites de tamaño. **Práctica:** embebe direcciones de entrega dentro de un pedido. **Evidencia:** identifica qué ocurre si la dirección maestra del cliente cambia.

#### 10.2.12 — Referencing

Referencing guarda identificadores de otros documentos y permite relaciones independientes, a costa de consultas adicionales o joins mediante agregación. **Práctica:** separa clientes y pedidos y recupera pedidos de un cliente por referencia. **Evidencia:** compara consistencia de actualización y número de consultas frente a embedding.

#### 10.2.13 — Replication

La replicación mantiene copias de datos en varios nodos para tolerancia a fallos y continuidad; puede introducir retraso y decisiones de elección de primario. **Práctica:** dibuja un replica set con primario y secundarios. **Evidencia:** explica elección, lectura desde réplica y posible lectura desactualizada.

#### 10.2.14 — Sharding

Sharding distribuye documentos entre shards mediante una clave de partición; una mala elección puede crear hotspots o consultas dispersas. **Práctica:** evalúa claves candidatas para distribuir pedidos por cliente o fecha. **Evidencia:** analiza cardinalidad, monotonía, distribución y patrón de consulta.

### 10.3 — Redis

#### 10.3.1 — Key-value

Un almacén key-value asocia claves únicas con valores y optimiza acceso directo por clave; el valor puede ser opaco para el servidor. **Práctica:** diseña claves con prefijos por dominio para sesiones y caché. **Evidencia:** define convención, expiración y estrategia para evitar colisiones.

#### 10.3.2 — Strings

Redis Strings almacenan cadenas o secuencias binarias y admiten operaciones como SET, GET e incrementos atómicos sobre valores numéricos. **Práctica:** guarda un contador de laboratorio con `SET`, `GET` e `INCR`. **Evidencia:** explica atomicidad de INCR y por qué no equivale a leer, sumar y escribir desde el cliente.

#### 10.3.3 — Lists

Redis Lists mantienen secuencias ordenadas con operaciones en extremos, útiles para colas simples o historiales acotados. **Práctica:** usa LPUSH, RPUSH, LRANGE y LPOP en una lista de tareas ficticias. **Evidencia:** dibuja el orden después de cada operación y distingue cola y pila.

#### 10.3.4 — Sets

Redis Sets almacenan miembros únicos sin orden garantizado y ofrecen operaciones de unión, intersección y diferencia. **Práctica:** crea conjuntos de etiquetas para dos productos y calcula elementos comunes. **Evidencia:** explica cómo se elimina duplicación y cuándo el orden no debe asumirse.

#### 10.3.5 — Hashes

Redis Hashes almacenan pares campo-valor dentro de una clave, adecuados para representar atributos de una entidad pequeña. **Práctica:** crea un hash de perfil de prueba con HSET y consulta campos con HGET/HGETALL. **Evidencia:** explica por qué un hash no sustituye automáticamente una base relacional.

#### 10.3.6 — Sorted Sets

Sorted Sets asocian miembros únicos con puntuaciones numéricas y permiten consultas por rango o ranking. **Práctica:** registra puntuaciones de jugadores ficticios y consulta el top con ZREVRANGE o equivalente de la versión. **Evidencia:** explica desempates y por qué la puntuación no garantiza unicidad.

#### 10.3.7 — TTL

TTL define cuánto tiempo permanece una clave antes de expirar; es útil para cachés y datos temporales, no para registros que requieren retención permanente. **Práctica:** crea una clave con expiración breve y consulta TTL y existencia. **Evidencia:** registra el tiempo restante y explica la diferencia entre expiración y borrado manual.

#### 10.3.8 — Cache

Una caché conserva temporalmente resultados para reducir latencia y carga, pero introduce invalidación, obsolescencia y límites de memoria. **Práctica:** diseña cache-aside para una ficha de producto. **Evidencia:** describe hit, miss, TTL e invalidación tras actualizar el producto.

#### 10.3.9 — Sessions

Una sesión mantiene estado temporal asociado a un usuario o cliente entre solicitudes; el identificador debe ser impredecible y protegido. **Práctica:** diseña una clave de sesión sin almacenar contraseñas ni datos sensibles en texto claro. **Evidencia:** define expiración, renovación y revocación.

#### 10.3.10 — Pub/Sub

Pub/Sub permite publicar mensajes a canales y distribuirlos a suscriptores conectados; no debe asumirse persistencia o entrega a clientes desconectados. **Práctica:** publica eventos sintéticos en un canal y suscríbete desde dos terminales de laboratorio. **Evidencia:** describe qué ocurre si un suscriptor se desconecta.

#### 10.3.11 — Rate Limiting

Rate limiting limita solicitudes por identidad, token o recurso para reducir abuso y proteger capacidad. Redis puede apoyar contadores con expiración, pero la estrategia debe considerar concurrencia y múltiples nodos. **Práctica:** diseña un límite de cinco solicitudes por minuto con ventana definida. **Evidencia:** describe clave, contador, expiración y respuesta al exceder el límite.

### 10.4 — Otras arquitecturas de almacenamiento

#### 10.4.1 — Document databases

Las bases documentales almacenan registros flexibles como documentos y facilitan consultas sobre campos y estructuras anidadas. **Práctica:** compara el modelo de un catálogo de productos en MongoDB y relacional. **Evidencia:** identifica consultas favorecidas y riesgos de duplicación.

#### 10.4.2 — Key-value databases

Las bases key-value optimizan acceso por clave y suelen ofrecer operaciones simples de baja latencia; su consulta por atributos internos puede ser limitada. **Práctica:** modela tokens temporales o caché de configuración con claves explícitas. **Evidencia:** define ciclo de vida, colisiones y estrategia de expiración.

#### 10.4.3 — Column-family databases

Las bases de columnas anchas organizan datos por familias de columnas y se diseñan alrededor de consultas y particiones distribuidas. **Práctica:** diseña una clave de partición y clustering para eventos por dispositivo y tiempo. **Evidencia:** explica riesgo de particiones calientes y consultas que requieren escaneo.

#### 10.4.4 — Graph databases

Las bases de grafos representan entidades como nodos y relaciones como aristas, con propiedades asociadas. Son útiles para recorridos de relaciones, no para cualquier dato conectado. **Práctica:** modela usuarios, dispositivos y conexiones sospechosas como grafo. **Evidencia:** formula una consulta de dos saltos y explica su utilidad analítica.

#### 10.4.5 — Time-series databases

Las bases de series temporales optimizan datos ordenados por tiempo, etiquetas, retención y agregaciones por ventana. **Práctica:** diseña un esquema para métricas de CPU por host y minuto. **Evidencia:** define timestamp, etiquetas, política de retención y consulta de promedio por intervalo.

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
