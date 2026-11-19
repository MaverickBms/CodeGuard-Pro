# Etapa 9 — Bases de datos relacionales y SQL

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 9.  
**Prioridad oficial:** P1 · Obligatoria.  
**Objetivo oficial:** aprender a modelar, almacenar, consultar y administrar información.

## Temario oficial

### 9.1. Fundamentos
Qué es una base de datos; DBMS (Sistema Gestor de Bases de Datos); servidor de bases de datos; cliente de bases de datos; bases relacionales; tablas; filas; columnas; esquemas; tipos de datos.

### 9.2. Modelado
Entidades; atributos; relaciones; cardinalidad; claves primarias; claves foráneas; restricciones; diagramas entidad-relación; modelo conceptual, lógico y físico.

### 9.3. MySQL
Instalación de MySQL Server; configuración; MySQL Workbench; creación de bases de datos y tablas; usuarios; permisos; conexiones. **Distinción oficial:** MySQL Server es el gestor que almacena y administra los datos. MySQL Workbench es una herramienta gráfica para diseñar, consultar y administrar ese servidor. También se practican consultas desde terminal.

### 9.4. SQL
DDL, DML, DQL, DCL y TCL; CREATE, ALTER, DROP, SELECT, INSERT, UPDATE, DELETE, WHERE, ORDER BY, GROUP BY, HAVING, JOIN, subqueries y CTE.

### 9.5. Diseño y normalización
1NF, 2NF, 3NF, BCNF; redundancia; integridad referencial; relaciones uno a uno, uno a muchos y muchos a muchos.

### 9.6. Bases de datos avanzadas
Índices; B-Tree; índices compuestos; vistas; triggers; stored procedures; transacciones; ACID; commit; rollback; locks; deadlocks; isolation levels; optimización; EXPLAIN.

### 9.7. PostgreSQL
Arquitectura; roles; esquemas; tipos de datos; JSONB; índices; transacciones; consultas avanzadas.

**Proyecto oficial:** diseñar la base de datos de un sistema de ventas con clientes, productos, proveedores, facturación, inventario y pagos.

## Resultados de aprendizaje

Podrás distinguir motor, servidor, cliente y herramienta gráfica; modelar un dominio relacional; convertir un modelo entidad-relación en tablas; definir claves y restricciones; instalar y configurar MySQL Server; consultar desde Workbench y terminal; escribir SQL de definición, manipulación, consulta, control y transacciones; normalizar esquemas; comprender índices y planes de ejecución; gestionar transacciones y privilegios; y reconocer conceptos principales de PostgreSQL sin confundirlos con características exclusivas de MySQL.

## 9.1 — Fundamentos

### Base de datos y DBMS

Una base de datos es una colección organizada de datos que se conserva y consulta según un modelo. Un DBMS/SGBD es el software que permite definir, almacenar, consultar, proteger y administrar esos datos.

Distingue:
- **Motor/servidor:** proceso o servicio que administra bases de datos y atiende conexiones.
- **Cliente:** programa que se conecta y envía solicitudes.
- **Herramienta gráfica:** interfaz que facilita diseñar y administrar, pero no sustituye el servidor.
- **Esquema:** estructura lógica de objetos como tablas, vistas y restricciones.

### Modelo relacional

El modelo relacional representa información mediante relaciones (habitualmente presentadas como tablas). Una tabla contiene filas y columnas; cada columna tiene un dominio/tipo. Una fila representa una ocurrencia de datos.

La terminología formal de relación y tupla no es exactamente idéntica a la representación física de una tabla en todos los motores. En SQL pueden existir valores NULL y duplicados si no se definen restricciones adecuadas.

### Tipos de datos

Selecciona tipos que representen correctamente el dominio: enteros para cantidades discretas, DECIMAL/NUMERIC para importes exactos, fechas/horas para instantes o fechas, cadenas para texto y tipos booleanos cuando estén disponibles.

No uses FLOAT/DOUBLE para cálculos monetarios que requieren representación decimal exacta. Define límites, precisión, nulabilidad y formato con criterios de negocio. Las diferencias de tipos y comportamiento entre MySQL y PostgreSQL deben verificarse en sus manuales.

## 9.2 — Modelado de datos

### Entidades, atributos y relaciones

Una entidad representa un concepto del dominio del que se necesita conservar información. Sus atributos describen propiedades. Una relación representa una asociación entre entidades.

Ejemplo de ventas:
- Cliente realiza pedidos.
- Pedido contiene detalles.
- Cada detalle referencia un producto.
- Proveedor abastece productos.
- Pago registra una operación relacionada con una venta/factura según reglas del negocio.

No conviertas cada sustantivo del enunciado en una tabla automáticamente. Define identidad, ciclo de vida, reglas y consultas que el sistema necesita soportar.

### Cardinalidad y participación

Cardinalidad describe cuántas ocurrencias pueden relacionarse:
- uno a uno (1:1);
- uno a muchos (1:N);
- muchos a muchos (N:M).

La participación indica si la relación es obligatoria u opcional. Una relación N:M se representa habitualmente mediante una tabla asociativa que contiene las claves de ambas entidades y, cuando proceda, atributos propios de la relación.

### Claves primarias y foráneas

Una clave primaria identifica de forma única cada fila y no admite NULL. Puede ser simple o compuesta. Una clave foránea referencia una clave candidata/única de otra tabla y protege integridad referencial.

No confundas clave primaria con dato de negocio visible: un identificador técnico puede ser útil, pero los atributos naturales que deben ser únicos también pueden requerir restricciones UNIQUE.

### Restricciones

- NOT NULL: exige un valor.
- UNIQUE: evita duplicados según reglas del motor.
- CHECK: valida una condición.
- PRIMARY KEY: identifica filas.
- FOREIGN KEY: controla referencias.
- DEFAULT: establece un valor por omisión cuando corresponde.

Las restricciones deben representar invariantes del dominio. No sustituyen validación de entrada ni autorización en la aplicación.

### Modelo conceptual, lógico y físico

- **Conceptual:** describe entidades y relaciones del negocio sin comprometerse con un motor.
- **Lógico:** define atributos, identificadores, cardinalidades y reglas con mayor detalle.
- **Físico:** concreta tablas, tipos, índices, restricciones y decisiones para un DBMS.

### Diagrama entidad-relación

El DER comunica entidades, atributos, identificadores, cardinalidades y opcionalidad. Debe ser coherente con las reglas escritas. Incluye leyenda y convención de notación; evita diagramas que no aclaren el sentido de cada relación.

## 9.3 — MySQL

### MySQL Server y MySQL Workbench

MySQL Server es el gestor/servidor que almacena y administra datos. MySQL Workbench es una herramienta gráfica que permite modelar, consultar y administrar el servidor. Workbench no reemplaza al motor. También se debe saber conectarse y ejecutar consultas desde terminal.

### Instalación y configuración

Antes de instalar:
1. consulta requisitos y compatibilidad de la versión;
2. descarga desde el sitio oficial;
3. define puerto, almacenamiento y cuenta administrativa;
4. evita exponer el servicio a redes no necesarias;
5. utiliza contraseñas robustas y autenticación apropiada;
6. registra versión y configuración sin guardar secretos.

La instalación y los comandos pueden variar por sistema operativo y versión. Sigue la documentación oficial para el entorno del laboratorio.

### Bases de datos, tablas y conexiones

Una conexión necesita host, puerto, usuario, credencial y base/esquema según configuración. No publiques cadenas de conexión con contraseñas. Crea una base de práctica y usuarios separados por función.

Ejemplo de esquema conceptual convertido a SQL:

    CREATE DATABASE ventas_lab;
    USE ventas_lab;

    CREATE TABLE cliente (
      cliente_id BIGINT PRIMARY KEY AUTO_INCREMENT,
      nombre VARCHAR(120) NOT NULL,
      correo VARCHAR(254) UNIQUE
    );

    CREATE TABLE producto (
      producto_id BIGINT PRIMARY KEY AUTO_INCREMENT,
      nombre VARCHAR(160) NOT NULL,
      precio DECIMAL(12,2) NOT NULL,
      CONSTRAINT chk_producto_precio CHECK (precio >= 0)
    );

    CREATE TABLE pedido (
      pedido_id BIGINT PRIMARY KEY AUTO_INCREMENT,
      cliente_id BIGINT NOT NULL,
      fecha DATETIME NOT NULL,
      CONSTRAINT fk_pedido_cliente
        FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
    );

Este fragmento es didáctico; verifica compatibilidad de sintaxis, versión y motor antes de ejecutarlo. No define todo el proyecto ni todas las reglas fiscales/comerciales.

## 9.4 — SQL

### Categorías del lenguaje

- **DDL:** define estructuras (CREATE, ALTER, DROP).
- **DML:** manipula datos (INSERT, UPDATE, DELETE).
- **DQL:** consulta datos (SELECT; esta categoría se enseña separadamente en muchos programas).
- **DCL:** controla privilegios (GRANT, REVOKE).
- **TCL:** controla transacciones (COMMIT, ROLLBACK, SAVEPOINT).

La clasificación pedagógica puede variar entre textos; lo importante es comprender el propósito de cada sentencia y su efecto.

### CREATE, ALTER y DROP

CREATE crea objetos; ALTER modifica su definición; DROP elimina objetos. DROP puede destruir datos y dependencias. Antes de ejecutarlo, confirma el esquema y el entorno. No practiques sobre bases de producción.

### SELECT, WHERE y ORDER BY

SELECT recupera columnas/expresiones. WHERE filtra filas según condición. ORDER BY ordena el resultado. Un resultado sin ORDER BY no tiene orden garantizado.

Ejemplo:

    SELECT nombre, precio
    FROM producto
    WHERE precio >= 10000
    ORDER BY precio DESC, nombre ASC;

### INSERT, UPDATE y DELETE

INSERT agrega filas. UPDATE modifica filas existentes. DELETE elimina filas. Antes de UPDATE o DELETE verifica el predicado con un SELECT equivalente y utiliza transacciones cuando corresponda.

    UPDATE producto
    SET precio = 12500.00
    WHERE producto_id = 3;

Un UPDATE sin WHERE puede modificar todas las filas. Un DELETE sin WHERE puede eliminarlas todas.

### GROUP BY y HAVING

GROUP BY agrupa filas para calcular agregaciones. HAVING filtra grupos después de la agrupación; WHERE filtra filas antes de agrupar.

    SELECT cliente_id, COUNT(*) AS pedidos
    FROM pedido
    GROUP BY cliente_id
    HAVING COUNT(*) >= 2;

### JOIN

JOIN combina filas de tablas según una condición:
- INNER JOIN: filas con coincidencia.
- LEFT JOIN: conserva todas las filas de la izquierda y completa con NULL cuando no hay coincidencia.
- RIGHT JOIN: conserva todas las filas de la derecha.
- CROSS JOIN: producto cartesiano.
- FULL OUTER JOIN: no está disponible con la misma sintaxis nativa en todas las versiones/motores; verifica la plataforma.

Evita joins sin condición cuando no buscas un producto cartesiano. Comprueba cardinalidades para no multiplicar filas inesperadamente.

### Subqueries y CTE

Una subconsulta es una consulta anidada que aporta un valor, conjunto o relación a otra consulta. Una CTE (Common Table Expression) define un resultado nombrado temporal para una sentencia y mejora la legibilidad de consultas complejas. La sintaxis y capacidades avanzadas dependen de la versión del motor.

## 9.5 — Diseño y normalización

### Redundancia y anomalías

La redundancia innecesaria puede provocar anomalías de inserción, actualización y eliminación. Si la misma información se almacena en varios lugares, un cambio parcial puede dejar datos inconsistentes.

Normalizar consiste en organizar relaciones y dependencias para reducir redundancia y anomalías. No es una meta mecánica: ciertos sistemas desnormalizan deliberadamente por rendimiento, manteniendo reglas para evitar inconsistencias.

### Primera forma normal (1NF)

Cada atributo debe contener valores atómicos según el dominio definido; no almacenes listas repetidas dentro de una celda cuando deban consultarse y relacionarse como elementos independientes.

### Segunda forma normal (2NF)

La relación debe estar en 1NF y cada atributo no primo depender de la clave candidata completa, no de una parte propia de una clave compuesta. Si la clave es simple, no hay dependencia parcial de una parte de ella.

### Tercera forma normal (3NF)

La relación debe estar en 2NF y evitar dependencias transitivas problemáticas de atributos no clave respecto de claves candidatas. La definición formal utiliza atributos primos y dependencias funcionales; no la reduzcas a una regla informal sin revisar las dependencias.

### BCNF

Boyce-Codd Normal Form exige que todo determinante de una dependencia funcional no trivial sea una superclave. Es más estricta que 3NF en ciertos casos.

### Integridad referencial y relaciones

Una relación 1:1 puede representarse con FK y restricción UNIQUE. Una relación 1:N se implementa colocando la FK en el lado N. Una relación N:M requiere una tabla puente, normalmente con dos FKs y una clave/constraint que evite duplicados no deseados.

## 9.6 — Bases de datos avanzadas

### Índices, B-Tree e índices compuestos

Un índice acelera búsquedas y ordenamientos seleccionados a cambio de espacio y coste de mantenimiento en escrituras. B-Tree es una estructura ampliamente utilizada para índices ordenados. Un índice compuesto cubre varias columnas; el orden de columnas importa y debe corresponder a filtros, joins y ordenamientos frecuentes.

No crees índices en todas las columnas por defecto. Evalúa selectividad, tamaño, patrón de consultas y coste de escritura.

### Vistas, triggers y stored procedures

- **Vista:** consulta guardada que presenta datos como una relación virtual; algunas vistas pueden ser actualizables según reglas del motor.
- **Trigger:** lógica que se ejecuta ante eventos definidos sobre una tabla u objeto compatible.
- **Stored procedure:** rutina almacenada que se invoca para ejecutar lógica del lado del servidor.

Estos mecanismos pueden centralizar reglas, pero también ocultar efectos secundarios y dificultar pruebas si se usan indiscriminadamente. Documenta sus efectos y privilegios.

### Transacciones y ACID

Una transacción agrupa operaciones que deben tratarse como una unidad lógica.

ACID:
- **Atomicity:** todas las operaciones se confirman o se revierten como unidad.
- **Consistency:** las restricciones e invariantes se mantienen antes y después.
- **Isolation:** las transacciones concurrentes se comportan según el nivel de aislamiento.
- **Durability:** los cambios confirmados sobreviven a fallos dentro de las garantías del motor/configuración.

COMMIT confirma una transacción; ROLLBACK revierte cambios no confirmados. El soporte y los límites dependen del motor, tablas y configuración.

### Locks, deadlocks e isolation levels

Los locks coordinan accesos concurrentes. Un deadlock ocurre cuando transacciones se bloquean mutuamente esperando recursos. Los motores pueden detectar el ciclo y abortar una transacción.

Los niveles de aislamiento determinan qué anomalías de lectura pueden observarse. Los nombres comunes son Read Uncommitted, Read Committed, Repeatable Read y Serializable, pero el comportamiento exacto y el nivel predeterminado varían entre motores. Estudia las garantías del motor utilizado; no supongas equivalencia exacta solo por el nombre.

### EXPLAIN y optimización

EXPLAIN muestra el plan que el motor considera para ejecutar una consulta. Analiza acceso a tablas, índices, estimaciones de filas, joins y orden de operaciones. Las opciones de análisis real pueden ejecutar la consulta; úsalas con cuidado en operaciones que modifican datos o consumen muchos recursos.

Optimiza a partir de mediciones reproducibles:
1. formula la consulta correcta;
2. mide con datos representativos;
3. inspecciona el plan;
4. identifica el coste dominante;
5. prueba una modificación;
6. compara resultados y plan;
7. conserva la corrección funcional.

## 9.7 — PostgreSQL

### Arquitectura, roles y esquemas

PostgreSQL es un DBMS relacional con arquitectura cliente-servidor. Los roles administran identidades y privilegios; pueden tener capacidad de inicio de sesión y membresías en otros roles. Los esquemas organizan objetos dentro de una base de datos.

Aplica mínimo privilegio y separa roles de aplicación, administración y lectura cuando el caso lo requiera.

### Tipos de datos y JSONB

PostgreSQL ofrece tipos escalares, temporales, numéricos, arrays, tipos definidos por el usuario y JSON/JSONB. JSONB almacena documentos JSON en una representación binaria procesada que admite operadores e índices específicos. No sustituye automáticamente el modelo relacional: elige entre columnas tipadas y documentos según consultas, integridad y evolución del dominio.

### Índices, transacciones y consultas avanzadas

Aprende a crear índices adecuados, analizar planes con EXPLAIN, trabajar con transacciones y comprender concurrencia y bloqueos. PostgreSQL y MySQL comparten SQL, pero tienen diferencias en tipos, sintaxis, funciones, índices, aislamiento y herramientas. No copies comandos entre motores sin verificar compatibilidad.

### Comparación práctica con MySQL

Implementa el mismo modelo reducido de ventas en ambos motores. Compara:
- tipos de datos;
- identidad/autoincremento;
- restricciones;
- funciones y fechas;
- JSON/JSONB;
- índices;
- planes EXPLAIN;
- roles y privilegios;
- transacciones.

El objetivo es transferir conocimiento relacional, no memorizar dos lenguajes SQL independientes.

## Proyecto oficial — Base de datos de un sistema de ventas

### Alcance

Diseña la base de datos de un sistema con clientes, productos, proveedores, facturación, inventario y pagos. El proyecto debe comenzar con reglas del dominio y un modelo relacional antes de implementar SQL.

### Requisitos funcionales de práctica

- registrar clientes y proveedores;
- mantener catálogo de productos;
- registrar compras/abastecimiento e inventario;
- emitir facturas y sus detalles;
- registrar pagos y su relación con documentos;
- consultar ventas por periodo, cliente y producto;
- consultar existencias y movimientos.

Estas operaciones concretan el objetivo del proyecto; las reglas fiscales, moneda, impuestos, devoluciones y métodos de pago deben definirse explícitamente con el alcance académico, sin asumir cumplimiento legal real.

### Diseño sugerido

Entidades candidatas: Cliente, Proveedor, Producto, Compra, DetalleCompra, MovimientoInventario, Factura, DetalleFactura y Pago. Ajusta cardinalidades y atributos según reglas documentadas. Por ejemplo, una factura contiene uno o varios detalles; cada detalle identifica producto, cantidad y precio aplicado en esa operación.

No calcules el historial usando únicamente el precio actual del catálogo: conserva el precio aplicado en el detalle de la transacción para que los documentos históricos no cambien cuando se actualice el producto.

### Entregables

1. requisitos y reglas de negocio;
2. diccionario de datos;
3. modelo conceptual y DER;
4. modelo lógico normalizado;
5. modelo físico MySQL;
6. scripts DDL versionados;
7. datos ficticios de prueba;
8. consultas CRUD, filtros, agrupaciones, JOIN, subconsultas y CTE;
9. roles y privilegios de mínimo alcance;
10. índices justificados y análisis EXPLAIN;
11. demostración de transacción y rollback;
12. pruebas de integridad y casos límite;
13. versión equivalente reducida en PostgreSQL y comparación;
14. respaldo y restauración verificados en laboratorio.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Modelado conceptual/lógico/físico | 20 |
| Claves, relaciones y restricciones | 15 |
| SQL y consultas | 20 |
| Normalización | 10 |
| Transacciones y ACID | 10 |
| Índices y EXPLAIN | 10 |
| Administración, privilegios y backups | 10 |
| Comparación MySQL/PostgreSQL y documentación | 5 |

## Ejercicios de comprensión

1. ¿Qué diferencia hay entre DBMS, servidor y cliente?  
   **Respuesta:** el DBMS administra datos; el servidor atiende operaciones; el cliente se conecta y envía consultas.

2. ¿Qué diferencia existe entre clave primaria y foránea?  
   **Respuesta:** la primaria identifica filas; la foránea referencia una clave de otra relación y protege integridad.

3. ¿Dónde se coloca la FK de una relación 1:N?  
   **Respuesta:** normalmente en el lado N.

4. ¿Cómo se representa una relación N:M?  
   **Respuesta:** con una tabla asociativa que referencia las entidades participantes.

5. ¿Qué diferencia hay entre WHERE y HAVING?  
   **Respuesta:** WHERE filtra filas antes de agrupar; HAVING filtra grupos.

6. ¿Qué evita una restricción CHECK?  
   **Respuesta:** que se almacenen filas que no satisfacen una condición definida.

7. ¿Qué diferencia hay entre COMMIT y ROLLBACK?  
   **Respuesta:** COMMIT confirma cambios; ROLLBACK revierte los cambios no confirmados de la transacción.

8. ¿Qué significa ACID?  
   **Respuesta:** atomicidad, consistencia, aislamiento y durabilidad.

9. ¿Por qué un índice no debe crearse en cada columna?  
   **Respuesta:** consume espacio y aumenta el coste de escrituras y mantenimiento.

10. ¿Qué diferencia hay entre MySQL Server y Workbench?  
    **Respuesta:** el primero almacena y administra datos; Workbench es una herramienta cliente gráfica.

## Autoevaluación práctica

Construye el modelo de ventas y demuestra con consultas que las restricciones impiden referencias inexistentes y valores inválidos. Ejecuta una transacción que pueda revertirse; inspecciona un plan EXPLAIN; crea un usuario con privilegios limitados; y documenta una copia de seguridad restaurada en una base de laboratorio. No uses datos personales reales ni credenciales dentro del repositorio.

## Recursos audiovisuales

No se incluyen videos en esta versión. Se incorporarán por subtema (modelado relacional, SQL, normalización, transacciones, MySQL y PostgreSQL) solo después de confirmar audio hablado en español, pertinencia exacta y vigencia de la versión. Un tutorial de consultas básicas no se presentará como cobertura de normalización o administración avanzada.

## Referencias oficiales y técnicas

- MySQL Reference Manual: https://dev.mysql.com/doc/refman/8.4/en/
- MySQL Workbench Manual: https://dev.mysql.com/doc/workbench/en/
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- PostgreSQL — JSON Types: https://www.postgresql.org/docs/current/datatype-json.html
- PostgreSQL — EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html
- SQL Standard overview (ISO/IEC 9075; consultar edición oficial aplicable): https://www.iso.org/
- Use The Index, Luke! (material didáctico sobre índices y planes): https://use-the-index-luke.com/
- Database System Concepts, Silberschatz, Korth y Sudarshan (referencia bibliográfica).

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** scripts SQL y proyecto propuestos; no ejecutados contra instancias MySQL/PostgreSQL en esta sesión.  
**Estado editorial:** borrador.
