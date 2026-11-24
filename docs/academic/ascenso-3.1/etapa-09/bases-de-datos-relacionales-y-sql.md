# Etapa 9 — Bases de datos relacionales y SQL

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
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

## Desarrollo granular por lección

La secuencia siguiente desglosa los 81 títulos oficiales en unidades identificables. Los ejemplos de nombres y sentencias son didácticos; las diferencias de sintaxis, versión y configuración deben comprobarse en la documentación del motor utilizado.

### 9.1 — Fundamentos

#### 9.1.1 — Qué es una base de datos

Una base de datos es una colección organizada de datos mantenida para consulta, actualización y administración. Distingue datos, información, esquema y motor de almacenamiento. **Práctica:** define qué datos necesita el sistema de ventas del proyecto y qué preguntas debe responder. **Evidencia:** presenta cinco requisitos de consulta y relaciona cada uno con datos necesarios.

#### 9.1.2 — DBMS (Sistema Gestor de Bases de Datos)

Un DBMS administra almacenamiento, consultas, concurrencia, integridad, seguridad y recuperación. Distingue el gestor del modelo de datos y de la aplicación cliente. **Práctica:** compara las responsabilidades de MySQL Server y PostgreSQL con las de un cliente SQL. **Evidencia:** clasifica cinco tareas según correspondan al gestor, al cliente o a la aplicación.

#### 9.1.3 — Servidor de bases de datos

El servidor de bases de datos ejecuta el motor y atiende conexiones, autenticación, consultas y transacciones. Puede ser un proceso local o un servicio remoto. **Práctica:** dibuja cliente, red, puerto y proceso servidor para una instalación de laboratorio. **Evidencia:** identifica dónde residen los datos y qué componente escucha las conexiones.

#### 9.1.4 — Cliente de bases de datos

Un cliente de bases de datos envía instrucciones y presenta resultados; puede ser una CLI, interfaz gráfica, ORM o aplicación. **Práctica:** ejecuta una consulta equivalente desde una terminal y una herramienta gráfica. **Evidencia:** compara conexión, consulta y resultado sin confundir el cliente con el servidor.

#### 9.1.5 — Bases relacionales

El modelo relacional organiza datos en relaciones (tablas) y define operaciones sobre conjuntos, con integridad mediante claves y restricciones. **Práctica:** modela clientes y pedidos como relaciones separadas. **Evidencia:** explica por qué una tabla no es simplemente una hoja de cálculo y cómo se representa una asociación.

#### 9.1.6 — Tablas

Una tabla representa una relación con atributos y tuplas; cada columna tiene dominio y restricciones. **Práctica:** diseña la tabla `cliente` con identificador, correo y fecha de alta, justificando nulabilidad y unicidad. **Evidencia:** presenta DDL y explica cada atributo.

#### 9.1.7 — Filas

Una fila representa una tupla o registro con valores para las columnas de una tabla. La identidad lógica debe establecerse mediante una clave, no por la posición física de la fila. **Práctica:** inserta dos clientes de prueba y consulta ambos sin depender del orden natural. **Evidencia:** explica por qué se necesita `ORDER BY` para garantizar orden.

#### 9.1.8 — Columnas

Una columna define un atributo con nombre, tipo y restricciones. La elección del tipo afecta validación, almacenamiento, comparación y operaciones. **Práctica:** selecciona tipos para precio, fecha, correo y estado de pedido. **Evidencia:** justifica precisión, longitud, nulabilidad y posibles restricciones.

#### 9.1.9 — Esquemas

Un esquema agrupa objetos de base de datos y organiza nombres, permisos y dependencias; su significado exacto varía entre motores. **Práctica:** identifica bases de datos y esquemas en MySQL y PostgreSQL. **Evidencia:** describe la diferencia entre database y schema en ambos motores sin asumir que son equivalentes.

#### 9.1.10 — Tipos de datos

Los tipos de datos limitan y describen valores: enteros, decimales, texto, fechas, booleanos y tipos específicos del motor. Evita almacenar importes monetarios en coma flotante binaria cuando se requiere exactitud decimal. **Práctica:** define tipos para precio, cantidad y fecha de pedido. **Evidencia:** explica por qué usar DECIMAL para importes y cómo se controlan rangos.

### 9.2 — Modelado

#### 9.2.1 — Entidades

Una entidad representa un objeto o concepto del dominio sobre el que se almacenan datos, como Cliente, Producto o Pedido. **Práctica:** extrae entidades del enunciado del sistema de ventas y descarta sustantivos que no requieran persistencia propia. **Evidencia:** lista entidades con una breve justificación de existencia.

#### 9.2.2 — Atributos

Un atributo describe una propiedad de una entidad y debe tener significado, dominio y reglas de validación. Distingue atributos simples, compuestos, derivados y multivaluados. **Práctica:** analiza dirección, nombre completo y edad para decidir si requieren descomposición o cálculo. **Evidencia:** documenta decisiones y dependencias.

#### 9.2.3 — Relaciones

Una relación expresa una asociación entre entidades, por ejemplo cliente realiza pedido o pedido contiene producto. **Práctica:** redacta relaciones en ambos sentidos y asigna nombres verbales claros. **Evidencia:** produce un diagrama con roles y explica el significado de cada asociación.

#### 9.2.4 — Cardinalidad

La cardinalidad describe cuántas instancias pueden participar en una relación: uno a uno, uno a muchos o muchos a muchos, con mínimos y máximos. **Práctica:** define cardinalidad entre cliente y pedido y entre pedido y producto. **Evidencia:** justifica participación obligatoria u opcional con reglas del negocio.

#### 9.2.5 — Claves primarias

Una clave primaria identifica de forma única cada fila y no admite valores nulos. Compara claves naturales y sustitutas, y evita elegir atributos que cambien con frecuencia. **Práctica:** define una PK para cliente y pedido. **Evidencia:** explica unicidad, estabilidad y razón de la elección.

#### 9.2.6 — Claves foráneas

Una clave foránea mantiene una referencia válida a una clave candidata de otra tabla y protege integridad referencial. **Práctica:** relaciona pedido con cliente mediante FK y prueba una inserción con cliente inexistente en un entorno de prueba. **Evidencia:** registra el rechazo y explica las acciones ON DELETE/UPDATE seleccionadas.

#### 9.2.7 — Restricciones

Las restricciones expresan reglas que el motor debe hacer cumplir: NOT NULL, UNIQUE, CHECK, PRIMARY KEY y FOREIGN KEY. **Práctica:** define restricciones para correo único, cantidad positiva y estado permitido. **Evidencia:** intenta insertar datos inválidos y registra qué restricción impide cada caso.

#### 9.2.8 — Diagramas entidad-relación

Un diagrama entidad-relación representa entidades, atributos, relaciones y cardinalidades antes de implementar tablas. **Práctica:** dibuja el modelo inicial del sistema de ventas con clientes, pedidos, detalle, productos y pagos. **Evidencia:** marca PK/FK y detecta relaciones muchos a muchos.

#### 9.2.9 — Modelo conceptual

El modelo conceptual expresa reglas y conceptos del negocio sin comprometerse con un motor o tipos SQL. **Práctica:** describe entidades y relaciones del sistema de ventas en lenguaje del dominio. **Evidencia:** entrega un diagrama comprensible para una persona no técnica.

#### 9.2.10 — Modelo lógico

El modelo lógico transforma el modelo conceptual en estructuras relacionales: relaciones, atributos, claves y restricciones. **Práctica:** convierte la relación Pedido–Producto en una entidad asociativa DetallePedido. **Evidencia:** muestra PK, FKs y atributos propios de la asociación.

#### 9.2.11 — Modelo físico

El modelo físico concreta el diseño para un DBMS, incluyendo tipos, índices, particiones, nombres y decisiones de almacenamiento. **Práctica:** transforma una tabla lógica de pedido en DDL para el motor elegido. **Evidencia:** anota qué decisiones dependen del motor y cuáles son independientes.

### 9.3 — MySQL

#### 9.3.1 — Instalación de MySQL Server

Instalar MySQL Server implica elegir una distribución compatible, configurar el servicio, proteger credenciales iniciales y verificar el proceso. La guía exacta depende del sistema operativo y versión. **Práctica:** instala una instancia aislada siguiendo la documentación oficial de la versión elegida. **Evidencia:** registra versión, servicio, puerto y resultado de una conexión local.

#### 9.3.2 — Configuración

La configuración de MySQL controla red, directorios, memoria, registros, autenticación y límites. Cambios deben justificarse y probarse antes de aplicarse a producción. **Práctica:** inspecciona variables de solo lectura como `port`, `datadir` y `version`. **Evidencia:** registra valores efectivos y explica qué componente los define.

#### 9.3.3 — MySQL Workbench

MySQL Workbench es una herramienta gráfica para modelar, consultar y administrar conexiones; no es el servidor que almacena datos. **Práctica:** crea una conexión a una instancia local y ejecuta una consulta de solo lectura. **Evidencia:** identifica host, puerto, usuario y resultado, sin guardar secretos en el repositorio.

#### 9.3.4 — Creación de bases de datos

`CREATE DATABASE` crea un contenedor lógico de objetos; charset y collation determinan aspectos de codificación y comparación. **Práctica:** crea una base de datos de laboratorio con codificación Unicode apropiada. **Evidencia:** consulta metadatos y explica por qué charset/collation afectan búsquedas y ordenamiento.

#### 9.3.5 — Creación de tablas

`CREATE TABLE` define columnas, tipos, claves, restricciones y valores por defecto. **Práctica:** implementa tablas `cliente` y `pedido` con PK y FK. **Evidencia:** presenta el DDL y demuestra que el motor rechaza una referencia inexistente.

#### 9.3.6 — Usuarios

Los usuarios de MySQL son identidades de autenticación asociadas a un origen/host y métodos de autenticación. Distingue cuenta de sistema operativo y cuenta del DBMS. **Práctica:** consulta cuentas de laboratorio con privilegios de lectura, sin exponer hashes ni contraseñas. **Evidencia:** explica cómo se determina la identidad efectiva.

#### 9.3.7 — Permisos

Los permisos conceden acciones sobre objetos y alcance definidos; aplica mínimo privilegio en lugar de usar root para aplicaciones. **Práctica:** crea o diseña un rol de solo lectura para el esquema de ventas y verifica qué operaciones permite. **Evidencia:** muestra permisos otorgados y una operación denegada.

#### 9.3.8 — Conexiones

Una conexión combina host, puerto, protocolo, base de datos y credenciales; puede fallar por red, servicio, autenticación, TLS o permisos. **Práctica:** conecta una CLI a la instancia local y diagnostica por separado servicio, puerto y credenciales. **Evidencia:** registra un árbol de diagnóstico sin incluir secretos.

#### 9.3.9 — Una distinción importante

MySQL Server es el gestor que almacena y administra los datos; MySQL Workbench es un cliente gráfico para diseñar, consultar y administrar conexiones. Workbench no sustituye al servidor ni mantiene por sí solo la base de datos. **Práctica:** detén la conexión del cliente y comprueba que el servicio del servidor sigue siendo un componente separado. **Evidencia:** explica qué ocurre si se cierra Workbench mientras el servidor continúa activo.

### 9.4 — SQL

#### 9.4.1 — DDL

DDL agrupa instrucciones que definen o modifican estructuras, como CREATE, ALTER y DROP. El comportamiento transaccional de DDL puede variar por motor. **Práctica:** identifica qué sentencias de un script cambian esquema y cuáles manipulan filas. **Evidencia:** clasifica instrucciones y advierte antes de operaciones destructivas.

#### 9.4.2 — DML

DML manipula filas mediante operaciones como INSERT, UPDATE y DELETE; algunas clasificaciones incluyen SELECT en DML y otras lo separan como DQL. **Práctica:** prepara un script que inserte y actualice datos de prueba dentro de una transacción cuando el motor lo permita. **Evidencia:** muestra estado antes y después.

#### 9.4.3 — DQL

DQL es una categoría didáctica para consultas, principalmente SELECT; no todos los estándares o motores separan formalmente esta categoría. **Práctica:** formula consultas para filtrar, ordenar y proyectar clientes. **Evidencia:** explica qué columnas y filas devuelve cada consulta.

#### 9.4.4 — DCL

DCL reúne instrucciones de control de privilegios, como GRANT y REVOKE en motores que las implementan. **Práctica:** revisa un ejemplo de concesión de SELECT sobre un esquema de laboratorio. **Evidencia:** identifica sujeto, privilegio, objeto y alcance, y comprueba el principio de mínimo privilegio.

#### 9.4.5 — TCL

TCL describe el control de transacciones mediante COMMIT, ROLLBACK y, según el motor, SAVEPOINT. **Práctica:** ejecuta una modificación dentro de una transacción y decide confirmarla o revertirla. **Evidencia:** demuestra el estado final después de cada decisión.

#### 9.4.6 — CREATE

`CREATE` define objetos como bases de datos, tablas, índices y vistas. La sintaxis y opciones varían entre MySQL y PostgreSQL. **Práctica:** crea una tabla con PK, NOT NULL y CHECK en el motor elegido. **Evidencia:** muestra el DDL y consulta el catálogo para confirmar su estructura.

#### 9.4.7 — ALTER

`ALTER` modifica la definición de objetos, por ejemplo agregando columnas o restricciones. Los cambios pueden bloquear tablas o requerir migraciones cuidadosas. **Práctica:** agrega una columna opcional a una tabla de laboratorio y luego define su restricción si procede. **Evidencia:** presenta antes/después y explica impacto en datos existentes.

#### 9.4.8 — DROP

`DROP` elimina objetos y puede destruir datos dependientes; no debe confundirse con DELETE, que elimina filas. **Práctica:** compara `DROP TABLE` y `DELETE FROM` en una base descartable. **Evidencia:** explica el alcance de cada sentencia y verifica el efecto sin usar datos reales.

#### 9.4.9 — SELECT

`SELECT` proyecta columnas y obtiene filas de una o varias fuentes. Evita `SELECT *` en consultas de aplicación cuando no se necesitan todas las columnas. **Práctica:** consulta nombre y correo de clientes activos. **Evidencia:** explica proyección, origen y cardinalidad del resultado.

#### 9.4.10 — INSERT

`INSERT` agrega filas y debe respetar tipos, restricciones y columnas obligatorias. Especifica columnas para evitar depender del orden físico de la tabla. **Práctica:** inserta un cliente con lista explícita de columnas. **Evidencia:** consulta la fila creada y registra cómo se obtuvo su identificador.

#### 9.4.11 — UPDATE

`UPDATE` modifica filas que cumplen una condición; omitir WHERE puede afectar toda la tabla. **Práctica:** cambia el estado de un pedido de prueba identificándolo por PK y ejecuta primero un SELECT equivalente. **Evidencia:** registra filas afectadas y demuestra que ninguna otra cambió.

#### 9.4.12 — DELETE

`DELETE` elimina filas seleccionadas y puede activar reglas referenciales o triggers. **Práctica:** elimina un registro de prueba después de revisar la condición con SELECT y dentro de una transacción si procede. **Evidencia:** documenta filas afectadas y posibilidad de rollback.

#### 9.4.13 — WHERE

`WHERE` filtra filas mediante condiciones; NULL requiere operadores IS NULL/IS NOT NULL y la lógica ternaria afecta comparaciones. **Práctica:** consulta pedidos por estado, rango de fecha y valores nulos. **Evidencia:** explica por qué `columna = NULL` no produce el resultado esperado.

#### 9.4.14 — ORDER BY

`ORDER BY` ordena el resultado por una o varias expresiones; sin orden explícito no se garantiza la secuencia de filas. **Práctica:** ordena pedidos por fecha descendente y luego por identificador para desempatar. **Evidencia:** justifica orden estable para paginación.

#### 9.4.15 — GROUP BY

`GROUP BY` agrupa filas para calcular agregaciones como COUNT, SUM, AVG, MIN y MAX. **Práctica:** calcula ventas totales por cliente con un conjunto de datos de prueba. **Evidencia:** explica la granularidad del resultado y evita seleccionar columnas no agrupadas sin agregación.

#### 9.4.16 — HAVING

`HAVING` filtra grupos después de la agregación, mientras WHERE filtra filas antes de agrupar. **Práctica:** muestra clientes con más de dos pedidos usando GROUP BY y HAVING. **Evidencia:** explica por qué la condición de agregado no corresponde a WHERE en esa consulta.

#### 9.4.17 — JOIN

JOIN combina filas relacionadas de tablas; INNER, LEFT y otras variantes tienen semánticas distintas. **Práctica:** une pedidos con clientes y conserva clientes sin pedidos mediante LEFT JOIN. **Evidencia:** explica filas con NULL y cómo una condición en WHERE puede convertir accidentalmente el resultado en uno similar a INNER JOIN.

#### 9.4.18 — Subqueries

Una subconsulta es una consulta anidada que puede producir un escalar, conjunto o tabla derivada. Puede ser correlacionada y evaluarse conceptualmente por fila. **Práctica:** busca pedidos cuyo importe supera el promedio global. **Evidencia:** identifica consulta interna, externa y tipo de resultado.

#### 9.4.19 — CTE

Una CTE definida con WITH nombra un resultado temporal dentro de una sentencia y mejora legibilidad; las CTE recursivas permiten recorrer jerarquías en motores compatibles. **Práctica:** expresa una consulta de ventas por cliente mediante CTE. **Evidencia:** compara legibilidad con una subconsulta equivalente y comprueba soporte del motor.

### 9.5 — Diseño y normalización

#### 9.5.1 — Primera forma normal (1NF)

Primera forma normal requiere valores atómicos por celda y ausencia de grupos repetidos en una misma fila, según el modelo relacional clásico. **Práctica:** transforma una tabla que almacena varios teléfonos en una estructura separada. **Evidencia:** explica qué anomalía se evita y cómo se relacionan las tablas.

#### 9.5.2 — Segunda forma normal (2NF)

Segunda forma normal exige 1NF y que cada atributo no primo dependa de toda la clave candidata, no solo de una parte de una clave compuesta. **Práctica:** analiza una tabla detalle con clave pedido-producto y separa datos propios del producto. **Evidencia:** identifica dependencia parcial.

#### 9.5.3 — Tercera forma normal (3NF)

Tercera forma normal elimina dependencias transitivas de atributos no clave respecto de claves candidatas, bajo la definición formal. **Práctica:** separa datos de ciudad/provincia que se repiten en clientes cuando existe dependencia funcional adecuada. **Evidencia:** documenta dependencias antes y después.

#### 9.5.4 — BCNF

BCNF requiere que todo determinante de una dependencia funcional no trivial sea superclave; es más estricta que 3NF. **Práctica:** analiza un ejemplo con dependencias entre curso, instructor y aula. **Evidencia:** identifica el determinante que incumple BCNF y propone descomposición sin pérdida cuando corresponda.

#### 9.5.5 — Redundancia

La redundancia almacena repetidamente hechos y puede provocar anomalías de actualización, inserción y eliminación. No toda duplicación es incorrecta: la desnormalización puede ser una decisión consciente por rendimiento. **Práctica:** identifica un dato repetido en una tabla de ventas. **Evidencia:** describe una anomalía y una estrategia para evitarla.

#### 9.5.6 — Integridad referencial

La integridad referencial asegura que las referencias entre tablas apunten a filas válidas, mediante claves foráneas y acciones referenciales. **Práctica:** intenta insertar un detalle de pedido con producto inexistente en una base descartable. **Evidencia:** registra rechazo y justifica ON DELETE RESTRICT, CASCADE o SET NULL según el dominio.

#### 9.5.7 — Relaciones uno a uno

Una relación uno a uno asocia como máximo una fila de cada lado; puede implementarse con FK UNIQUE o una PK compartida. **Práctica:** modela cliente y perfil extendido con datos opcionales. **Evidencia:** explica cuándo separar el perfil y cómo impedir duplicados.

#### 9.5.8 — Uno a muchos

Una relación uno a muchos coloca normalmente la FK en el lado muchos, por ejemplo pedido pertenece a cliente. **Práctica:** implementa cliente y pedido con FK y crea varios pedidos para un cliente. **Evidencia:** consulta la asociación y explica por qué la FK no se repite en la tabla padre.

#### 9.5.9 — Muchos a muchos

Una relación muchos a muchos se transforma en una tabla asociativa que contiene FKs y atributos de la relación, por ejemplo detalle de pedido. **Práctica:** crea pedido, producto y detalle con PK compuesta o sustituta y restricción única apropiada. **Evidencia:** demuestra múltiples productos por pedido y múltiples pedidos por producto.

### 9.6 — Bases de datos avanzadas

#### 9.6.1 — Índices

Un índice mantiene una estructura auxiliar para acelerar búsquedas, ordenamientos o joins, a cambio de almacenamiento y coste de escritura. **Práctica:** compara EXPLAIN antes y después de indexar una columna selectiva en datos de prueba. **Evidencia:** explica plan y coste, sin asumir que todo índice mejora cualquier consulta.

#### 9.6.2 — B-Tree

B-Tree organiza claves ordenadas y permite búsquedas por rango y prefijos según el motor y la definición del índice. **Práctica:** consulta el plan de una búsqueda por rango sobre una columna indexada. **Evidencia:** explica búsqueda, recorrido y por qué la selectividad importa.

#### 9.6.3 — Índices compuestos

Un índice compuesto contiene varias columnas en un orden definido; el orden de las columnas afecta qué predicados pueden aprovecharlo. **Práctica:** compara índices `(cliente_id, fecha)` y `(fecha, cliente_id)` para consultas distintas. **Evidencia:** relaciona el prefijo izquierdo con los filtros del plan.

#### 9.6.4 — Vistas

Una vista presenta una consulta con nombre y puede simplificar acceso y abstracción; una vista normal no necesariamente almacena resultados. **Práctica:** crea una vista de pedidos con datos no sensibles y consulta desde ella. **Evidencia:** explica dependencia de la consulta base y límites de actualización.

#### 9.6.5 — Triggers

Un trigger ejecuta lógica ante eventos de una tabla, como INSERT, UPDATE o DELETE, según capacidades del motor. Puede ocultar efectos secundarios y complicar depuración. **Práctica:** diseña un trigger de auditoría solo en una base descartable. **Evidencia:** documenta evento, condición, efecto y riesgo de recursión o duplicación.

#### 9.6.6 — Stored Procedures

Un stored procedure encapsula operaciones ejecutadas en el servidor con parámetros y control de flujo propio del motor. **Práctica:** compara una rutina almacenada con una transacción coordinada desde la aplicación. **Evidencia:** identifica qué lógica conviene centralizar y cómo se versiona.

#### 9.6.7 — Transacciones

Una transacción agrupa operaciones para tratarlas como unidad lógica, con confirmación o reversión. **Práctica:** transfiere una cantidad entre dos cuentas de prueba dentro de una transacción. **Evidencia:** demuestra que ambas actualizaciones se confirman o ninguna queda aplicada.

#### 9.6.8 — ACID

ACID resume atomicidad, consistencia, aislamiento y durabilidad; el grado concreto depende del motor, configuración y almacenamiento. **Práctica:** asocia cada propiedad con un fallo posible durante una venta. **Evidencia:** explica qué garantía aporta y qué no cubre cada propiedad.

#### 9.6.9 — Commit

`COMMIT` confirma los cambios de una transacción y los hace visibles/durables según las garantías del motor. **Práctica:** actualiza un pedido dentro de una transacción y confirma. **Evidencia:** abre una segunda sesión y verifica la visibilidad posterior al commit.

#### 9.6.10 — Rollback

`ROLLBACK` revierte cambios no confirmados dentro de la transacción, sujeto a límites del motor y operaciones ejecutadas. **Práctica:** modifica un dato de prueba y revierte la transacción. **Evidencia:** demuestra que el valor original permanece.

#### 9.6.11 — Locks

Los locks coordinan accesos concurrentes y pueden aplicarse a filas, páginas, tablas u otros recursos según el motor. **Práctica:** en dos sesiones de laboratorio, bloquea una fila y observa el comportamiento de una actualización concurrente con timeout controlado. **Evidencia:** identifica bloqueo y espera sin dejar sesiones colgadas.

#### 9.6.12 — Deadlocks

Un deadlock ocurre cuando transacciones esperan recursos retenidos entre sí formando un ciclo; los motores suelen detectar y abortar una de ellas. **Práctica:** modela dos transacciones que bloquean filas en orden opuesto, sin ejecutar cargas peligrosas. **Evidencia:** dibuja el ciclo y propone un orden consistente de adquisición.

#### 9.6.13 — Isolation Levels

Los niveles de aislamiento regulan anomalías de lectura concurrente; nombres y comportamientos exactos dependen del motor. **Práctica:** compara READ COMMITTED y REPEATABLE READ con dos sesiones y un conjunto pequeño de datos. **Evidencia:** registra qué lecturas cambian y cita el comportamiento del motor probado.

#### 9.6.14 — Optimización

Optimizar consultas comienza por medir y comprender el plan, cardinalidad, índices, filtros y volumen, no por añadir índices al azar. **Práctica:** identifica una consulta lenta simulada y formula hipótesis antes de cambiarla. **Evidencia:** registra métrica base, cambio, resultado y posible coste de escritura.

#### 9.6.15 — EXPLAIN

`EXPLAIN` muestra el plan que el optimizador considera para ejecutar una consulta; variantes como EXPLAIN ANALYZE pueden ejecutar realmente la sentencia. **Práctica:** analiza un SELECT de laboratorio y distingue estimaciones de mediciones reales. **Evidencia:** identifica acceso, joins, filas estimadas y advertencias del plan.

### 9.7 — PostgreSQL

#### 9.7.1 — Arquitectura

PostgreSQL utiliza una arquitectura cliente-servidor con procesos backend, memoria compartida y archivos de datos/WAL. **Práctica:** consulta `version()` y vistas de actividad en una instancia de laboratorio. **Evidencia:** explica conexión, proceso servidor y persistencia sin confundir proceso cliente con backend.

#### 9.7.2 — Roles

Los roles de PostgreSQL representan identidades y pueden actuar como usuarios o grupos, con atributos de inicio de sesión y privilegios. **Práctica:** inspecciona roles de laboratorio con `\du` o vistas de catálogo. **Evidencia:** distingue LOGIN, pertenencia y privilegios de superusuario.

#### 9.7.3 — Esquemas

Los esquemas de PostgreSQL organizan objetos dentro de una base de datos y participan en resolución de nombres mediante search_path. **Práctica:** crea un esquema de laboratorio y una tabla cualificada por esquema. **Evidencia:** explica cómo cambia la resolución de una tabla según search_path.

#### 9.7.4 — Tipos de datos

PostgreSQL ofrece tipos nativos como UUID, arrays, interval, JSON/JSONB y tipos geométricos, además de tipos SQL comunes. **Práctica:** selecciona tipos para identificador, fecha de evento y estado. **Evidencia:** justifica precisión, operadores disponibles y validación.

#### 9.7.5 — JSONB

JSONB almacena documentos JSON en una representación binaria que permite operadores e índices específicos; no sustituye automáticamente un modelo relacional. **Práctica:** inserta un documento pequeño y consulta una clave con operadores JSONB. **Evidencia:** compara JSON y JSONB y justifica qué campos deben seguir normalizados.

#### 9.7.6 — Índices

PostgreSQL admite índices B-tree, Hash, GiST, SP-GiST, GIN y BRIN con casos de uso diferentes. **Práctica:** analiza un índice B-tree para igualdad/rango y un GIN para búsqueda en JSONB o arrays. **Evidencia:** explica por qué el tipo de índice debe corresponder al operador y patrón de consulta.

#### 9.7.7 — Transacciones

Las transacciones PostgreSQL siguen el modelo ACID y MVCC para gestionar concurrencia; vacuum mantiene versiones y espacio reutilizable. **Práctica:** observa una transacción en dos sesiones y consulta el estado de actividad. **Evidencia:** explica snapshots y por qué una fila antigua puede permanecer temporalmente visible.

#### 9.7.8 — Consultas avanzadas

Las consultas avanzadas combinan CTE, funciones de ventana, agregaciones, JSONB y joins según el problema. **Práctica:** calcula ranking de ventas por cliente con una función de ventana y CTE. **Evidencia:** explica PARTITION BY, ORDER BY y diferencia entre ranking y agrupación.

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
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** cotejo de las entradas oficiales del roadmap, precisión conceptual, secuencia, ejemplos, prácticas, evaluación, seguridad y referencias.

**Resultado:** revisión documental interna realizada con los ajustes y hallazgos siguientes: Se revisó la correspondencia de las 81 entradas, el modelado relacional, SQL, normalización, transacciones, índices y diferencias de MySQL/PostgreSQL. Se mantiene la entrada 9.3.9 tal como figura en el roadmap, aunque su título debe tratarse como nota de distinción conceptual y no como producto o comando. Pendiente: ejecutar scripts en versiones declaradas, comprobar consultas, constraints, transacciones, planes EXPLAIN, backup y restauración.

**Límite de validación:** no se ejecutaron laboratorios, scripts, servicios, bases de datos, máquinas virtuales ni capturas de red en esta revisión. No se declara aprobación académica externa. La etapa continúa en desarrollo hasta completar las pruebas reproducibles y la segunda revisión.
