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
**Estado editorial:** en desarrollo; no aprobado ni publicado..
