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

**Propósito y modelo.** Una base de datos es una colección organizada de datos administrada para persistencia, consulta y actualización. Su diseño representa entidades y relaciones de un dominio y define reglas de integridad. No equivale a un archivo aislado: incluye estructuras, metadatos y mecanismos de acceso.

**Ejemplo desarrollado.** Un sistema académico almacena estudiantes, cursos, matrículas y calificaciones. Cada dato debe tener significado, formato, reglas de validación y relaciones claras para evitar inconsistencias.

**Práctica guiada.** Identifica entidades y atributos de un escenario de biblioteca. Distingue datos maestros, transacciones y catálogos.

**Actividad independiente.** Redacta requisitos de datos para un inventario pequeño: qué se almacena, quién consulta, quién modifica y cuánto tiempo se conserva.

**Criterios de aceptación.** Explica propósito, persistencia y organización y propone un conjunto coherente de entidades.

**Errores frecuentes.** Confundir base de datos con DBMS o diseñar tablas sin conocer las reglas del negocio.

**Comprobación.** ¿Qué diferencia existe entre los datos almacenados y el software que los administra?

**Laboratorio de profundización — Inventario de datos de un dominio.**

1. Toma el caso de una biblioteca. 2. Identifica entidades, datos maestros, transacciones y catálogos. 3. Define quién crea, consulta y modifica cada dato. 4. Propón reglas de retención y respaldo.

**Evidencia esperada.** El inventario separa hechos, catálogos y transacciones y relaciona cada dato con una necesidad del negocio.

**Seguridad y límites.** Usar datos ficticios; no almacenar información personal real en el ejercicio.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.2 — DBMS (Sistema Gestor de Bases de Datos)

**Propósito y modelo.** Un DBMS es el software que define, almacena, consulta, protege y administra bases de datos. Gestiona concurrencia, transacciones, permisos, recuperación, índices y metadatos. MySQL y PostgreSQL son DBMS relacionales; no son el mismo producto ni comparten todas las funciones y sintaxis.

**Ejemplo desarrollado.** Una aplicación envía SQL al DBMS; el gestor valida permisos, planifica la consulta, accede a estructuras y devuelve resultados. La aplicación no debería acceder directamente a archivos internos de datos.

**Práctica guiada.** Compara las funciones que ofrece un DBMS en documentación del producto: usuarios, transacciones, respaldos, índices y registro de actividad.

**Actividad independiente.** Selecciona requisitos para elegir un DBMS en un sistema pequeño: compatibilidad, consistencia, concurrencia, respaldo, operación y licencia.

**Criterios de aceptación.** Diferencia DBMS, base de datos, servidor y cliente; explica al menos cuatro responsabilidades del gestor.

**Errores frecuentes.** Confundir el motor con una interfaz gráfica o suponer que elegir un DBMS resuelve automáticamente el diseño del esquema.

**Comprobación.** ¿Qué responsabilidad del DBMS protege la consistencia cuando dos usuarios modifican datos al mismo tiempo?

**Laboratorio de profundización — Matriz de responsabilidades de un DBMS.**

1. Compara MySQL y PostgreSQL en transacciones, concurrencia, usuarios, respaldo e índices. 2. Identifica qué funciones resuelve el DBMS y cuáles corresponden a la aplicación. 3. Elabora criterios de selección para un sistema de ventas.

**Evidencia esperada.** La matriz distingue motor, base de datos, cliente y aplicación y utiliza criterios verificables.

**Seguridad y límites.** No asumir equivalencia completa entre motores ni utilizar versiones sin soporte en un despliegue.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.3 — Servidor de bases de datos

**Propósito y modelo.** El servidor de bases de datos ejecuta el proceso del DBMS y acepta conexiones según interfaces, puertos, autenticación y configuración. Puede alojar varias bases y esquemas. La ubicación del servidor no determina por sí sola su exposición: importan interfaces de escucha, firewall, rutas y controles de acceso.

**Ejemplo desarrollado.** Una aplicación puede conectarse a PostgreSQL mediante una red privada y una cuenta limitada. Exponer el puerto del motor a Internet aumenta riesgo y rara vez es necesario para una arquitectura de aplicación bien segmentada.

**Práctica guiada.** Dibuja cliente, servidor DBMS, almacenamiento y firewall. Identifica dirección de escucha, puerto y método de autenticación en una configuración de laboratorio, sin abrir puertos.

**Actividad independiente.** Diseña una arquitectura de base de datos para una aplicación web con acceso solo desde el backend.

**Criterios de aceptación.** Distingue proceso servidor, instancia y base de datos; delimita clientes autorizados.

**Errores frecuentes.** Publicar el puerto de base de datos para que el navegador conecte directamente o usar la cuenta administrativa desde la aplicación.

**Comprobación.** ¿Por qué el backend suele ser el único componente autorizado para conectarse al DBMS?

**Laboratorio de profundización — Arquitectura de conexión restringida.**

1. Dibuja navegador, backend, servidor DBMS y almacenamiento. 2. Define qué componente puede abrir conexión al DBMS. 3. Identifica interfaz de escucha, firewall y autenticación. 4. Explica por qué el puerto no debe exponerse al navegador.

**Evidencia esperada.** La arquitectura limita el acceso al backend y diferencia proceso servidor, instancia y base de datos.

**Seguridad y límites.** No abrir puertos ni exponer servicios de bases de datos reales.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.4 — Cliente de bases de datos

**Propósito y modelo.** Un cliente de base de datos es una herramienta o biblioteca que establece conexiones y envía consultas al servidor. Puede ser una interfaz gráfica, CLI o driver embebido en una aplicación. El cliente no sustituye al DBMS ni debe almacenar credenciales de producción de forma insegura.

**Ejemplo desarrollado.** MySQL Workbench y psql son clientes; una biblioteca JDBC también actúa como cliente desde una aplicación Java. Cada uno se autentica y opera con los permisos de la cuenta configurada.

**Práctica guiada.** Identifica clientes gráficos, CLI y drivers para MySQL y PostgreSQL. En un entorno de laboratorio consulta versión y configuración de conexión sin guardar contraseñas en texto plano.

**Actividad independiente.** Elige un cliente para administración y otro para integración de aplicación; justifica trazabilidad, automatización y manejo de secretos.

**Criterios de aceptación.** Distingue cliente, driver y servidor y explica cómo se establece una conexión.

**Errores frecuentes.** Confundir Workbench con el motor MySQL o incrustar credenciales en código fuente.

**Comprobación.** ¿Qué componente traduce las llamadas de una aplicación al protocolo de conexión del DBMS?

**Laboratorio de profundización — Comparación de clientes y drivers.**

1. Compara una GUI, una CLI y un driver de aplicación. 2. Registra cómo autentican, ejecutan consultas y manejan resultados. 3. Diseña conexión con credenciales de laboratorio mediante variables o almacén seguro. 4. Explica qué nunca debe quedar en el repositorio.

**Evidencia esperada.** La comparación diferencia cliente y servidor y describe manejo seguro de credenciales.

**Seguridad y límites.** No almacenar contraseñas en texto plano ni incluirlas en capturas o commits.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.5 — Bases relacionales

**Propósito y modelo.** Una base relacional organiza datos en relaciones (representadas habitualmente como tablas), con atributos, tuplas y restricciones. La teoría relacional utiliza conjuntos y relaciones matemáticas; el SQL práctico incorpora características como NULL, duplicados y orden de salida que requieren cuidado.

**Ejemplo desarrollado.** Las tablas Estudiante y Curso se relacionan mediante Matrícula. Una clave foránea representa la relación y permite aplicar integridad referencial.

**Práctica guiada.** Diseña tres tablas para biblioteca: Libro, Usuario y Préstamo. Identifica claves y restricciones necesarias.

**Actividad independiente.** Explica por qué guardar una lista de cursos separados por comas en una columna dificulta integridad, consultas y relaciones.

**Criterios de aceptación.** Identifica relación, atributo, tupla y claves; modela una relación muchos-a-muchos mediante tabla intermedia.

**Errores frecuentes.** Suponer que el orden de filas está garantizado o almacenar múltiples valores independientes en una sola columna sin justificación.

**Comprobación.** ¿Por qué una relación muchos-a-muchos suele representarse mediante una tabla asociativa?

**Laboratorio de profundización — Diseño de relaciones para biblioteca.**

1. Diseña Libro, Usuario y Préstamo. 2. Define claves primarias y foráneas. 3. Identifica atributos atómicos y reglas de integridad. 4. Explica cómo se representa una relación muchos-a-muchos.

**Evidencia esperada.** El esquema relaciona entidades mediante claves y evita duplicar atributos de otra entidad sin justificación.

**Seguridad y límites.** Usar datos ficticios y no confundir modelo relacional con una hoja de cálculo.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.6 — Tablas

**Propósito y modelo.** Una tabla representa una relación lógica con columnas definidas y filas de datos. El esquema establece nombres, tipos, restricciones y relaciones. Las tablas no garantizan por sí mismas un orden físico o lógico de las filas; el orden de consulta requiere ORDER BY.

**Ejemplo desarrollado.** Una tabla Producto puede tener id, nombre, precio y estado. Una restricción CHECK puede limitar precio a valores no negativos y una clave primaria identifica cada fila.

**Práctica guiada.** Diseña definición de tabla Producto y marca tipos, clave primaria, NOT NULL y restricción de dominio. No uses datos reales personales.

**Actividad independiente.** Revisa un esquema con columnas repetidas y determina si corresponde separar una entidad en otra tabla.

**Criterios de aceptación.** Identifica columnas, filas, esquema y restricciones; explica por qué SELECT sin ORDER BY no garantiza orden.

**Errores frecuentes.** Utilizar posiciones de columnas como contrato o asumir que la tabla conserva el orden de inserción.

**Comprobación.** ¿Qué garantía aporta ORDER BY que la estructura física de la tabla no aporta?

**Laboratorio de profundización — Diseño de estructura tabular.**

1. Define columnas, tipos y restricciones para una tabla Producto. 2. Distingue nombre de columna, valor y metadato. 3. Identifica clave primaria y columnas que no deberían admitir NULL. 4. Evalúa una fila de ejemplo.

**Evidencia esperada.** La tabla tiene propósito único, atributos definidos y restricciones coherentes con el dominio.

**Seguridad y límites.** No diseñar una única tabla universal que mezcle entidades no relacionadas.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.7 — Filas

**Propósito y modelo.** Una fila o tupla representa una instancia de la entidad descrita por la tabla. Cada valor debe respetar el tipo, restricciones y semántica de la columna. La clave primaria permite identificar una fila sin depender de su posición.

**Ejemplo desarrollado.** En Producto, una fila puede representar un artículo específico. Dos filas pueden compartir nombre si el dominio lo permite, pero no deben compartir la clave primaria.

**Práctica guiada.** Crea cinco registros sintéticos y valida qué atributos deben ser únicos, obligatorios o pueden quedar ausentes.

**Actividad independiente.** Define reglas de calidad para filas de una tabla Cliente sin utilizar datos personales reales.

**Criterios de aceptación.** Explica registro, identidad y restricciones de fila; identifica duplicidad semántica frente a duplicidad de clave.

**Errores frecuentes.** Identificar registros por número de fila o asumir que dos nombres iguales representan necesariamente la misma entidad.

**Comprobación.** ¿Por qué una clave primaria es más estable que utilizar el nombre de una persona como identificador?

**Laboratorio de profundización — Integridad de registros.**

1. Crea tres registros ficticios de producto. 2. Comprueba unicidad de clave y obligatoriedad de campos. 3. Explica diferencia entre fila duplicada y dos entidades distintas con atributos similares. 4. Define qué identifica un registro de manera estable.

**Evidencia esperada.** Cada fila representa una instancia y posee una identidad inequívoca dentro de la tabla.

**Seguridad y límites.** No usar datos personales reales ni asumir que el número de fila es una identidad estable.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.8 — Columnas

**Propósito y modelo.** Una columna representa un atributo con nombre, tipo y restricciones. La selección de tipo debe corresponder al dominio y precisión requerida: enteros, decimales, fechas, texto o tipos específicos del motor. Evitar tipos ambiguos facilita validación y consulta.

**Ejemplo desarrollado.** Un precio requiere DECIMAL con precisión definida y no FLOAT si se necesita exactitud decimal de negocio. Una fecha debe almacenarse como DATE/TIMESTAMP, no como texto libre.

**Práctica guiada.** Asigna tipos a atributos de una tabla Pedido: id, fecha, total, estado y observaciones. Justifica precisión, nulabilidad y longitud.

**Actividad independiente.** Detecta problemas de diseño en columnas que almacenan fecha como texto, precio como VARCHAR o varios valores separados por coma.

**Criterios de aceptación.** Selecciona tipos según dominio y explica impacto de precisión y nulabilidad.

**Errores frecuentes.** Utilizar VARCHAR para todo o asumir que FLOAT representa importes monetarios exactos.

**Comprobación.** ¿Por qué conviene elegir DECIMAL para valores monetarios que requieren precisión exacta?

**Laboratorio de profundización — Selección de atributos y tipos.**

1. Define atributos para producto, precio, fecha y estado. 2. Selecciona tipos de datos apropiados. 3. Explica precisión decimal para dinero y longitud de cadenas. 4. Identifica atributos derivados que quizá no deban almacenarse.

**Evidencia esperada.** Cada columna tiene significado, tipo y nulabilidad justificados.

**Seguridad y límites.** Evitar usar FLOAT para importes monetarios cuando se requiere precisión decimal exacta.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.9 — Esquemas

**Propósito y modelo.** Un esquema agrupa objetos de base de datos como tablas, vistas, secuencias y funciones y proporciona un espacio de nombres y límites administrativos. La semántica exacta varía entre DBMS: PostgreSQL utiliza esquemas como contenedores dentro de una base; MySQL usa database y schema como sinónimos en muchos contextos.

**Ejemplo desarrollado.** Una aplicación puede separar objetos en esquemas ventas, inventario y auditoría, otorgando permisos diferentes. El esquema no sustituye a la separación por instancias cuando se requieren límites operativos más fuertes.

**Práctica guiada.** Consulta esquemas disponibles en una instancia de laboratorio y localiza una tabla mediante su nombre calificado esquema.tabla.

**Actividad independiente.** Diseña una convención de esquemas para separar módulos de una aplicación y define quién puede crear o modificar objetos.

**Criterios de aceptación.** Explica esquema como espacio de nombres y reconoce diferencias entre MySQL y PostgreSQL.

**Errores frecuentes.** Suponer que schema significa exactamente lo mismo en todos los motores o confiar en el nombre del esquema como único control de seguridad.

**Comprobación.** ¿Qué ventaja aporta calificar una tabla con el nombre de su esquema?

**Laboratorio de profundización — Organización y namespaces.**

1. Dibuja dos esquemas para separar ventas y auditoría. 2. Define propietarios y permisos por esquema. 3. Explica diferencia entre esquema y base de datos según motor. 4. Diseña nombres consistentes.

**Evidencia esperada.** La propuesta explica el alcance del esquema y no asume que todos los motores implementan idéntica jerarquía.

**Seguridad y límites.** No conceder permisos globales cuando basta acceso a un esquema.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.1.10 — Tipos de datos

**Propósito y modelo.** Los tipos de datos determinan representación, rango, operaciones y validación de valores. Deben elegirse según semántica y motor: INTEGER, BIGINT, DECIMAL, VARCHAR, TEXT, DATE, TIMESTAMP, BOOLEAN y tipos binarios, entre otros. Diferencias entre motores afectan límites, coerción, zona horaria y almacenamiento.

**Ejemplo desarrollado.** Una fecha de nacimiento suele ser DATE; un instante de evento con zona horaria requiere una decisión explícita sobre TIMESTAMP y normalización. Guardar fechas como cadenas complica ordenamiento y comparación.

**Práctica guiada.** Construye una matriz de atributos y tipos para una tabla Evento. Indica rango, precisión, nulabilidad y portabilidad entre MySQL y PostgreSQL.

**Actividad independiente.** Revisa un esquema hipotético y propone cambios para mejorar precisión, restricciones y compatibilidad.

**Criterios de aceptación.** Justifica tipo, precisión, longitud y tratamiento de NULL; reconoce particularidades del motor.

**Errores frecuentes.** Confundir NULL con cadena vacía, no definir zona horaria o asumir que tipos homónimos tienen comportamiento idéntico en todos los DBMS.

**Comprobación.** ¿Qué problemas puede generar almacenar fechas y números como texto?

### 9.2 — Modelado

**Laboratorio de profundización — Catálogo de tipos y validación.**

1. Selecciona tipos para identificadores, texto, fecha, importe, booleano y JSON. 2. Compara precisión y rango. 3. Define restricciones CHECK y NOT NULL cuando sean apropiadas. 4. Explica conversiones implícitas peligrosas.

**Evidencia esperada.** El catálogo evita pérdida de precisión y valida valores según reglas de negocio.

**Seguridad y límites.** No guardar fechas como texto libre ni importes como punto flotante sin analizar precisión.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.1 — Entidades

**Propósito y modelo.** Una entidad representa un objeto o concepto del dominio sobre el que se necesita almacenar información. Puede ser tangible, como Producto, o conceptual, como Pedido o Suscripción. Una entidad debe tener identidad y atributos definidos; no todo sustantivo del requisito se convierte automáticamente en tabla.

**Ejemplo desarrollado.** En una biblioteca, Libro, Ejemplar, Usuario y Préstamo son entidades distintas: Libro describe una obra, Ejemplar una copia física y Préstamo una relación temporal de circulación.

**Práctica guiada.** Lee un caso de biblioteca e identifica entidades candidatas. Para cada una escribe propósito, identidad y dos atributos. Separa entidades de acciones y valores calculados.

**Actividad independiente.** Modela entidades para una tienda en línea y explica por qué Pedido y Producto requieren una entidad intermedia de detalle.

**Criterios de aceptación.** Cada entidad tiene significado claro, identidad y límites no redundantes.

**Errores frecuentes.** Crear una tabla por cada palabra del requisito o mezclar entidad y atributo.

**Comprobación.** ¿Qué diferencia existe entre Libro y Ejemplar en un sistema bibliotecario?

**Laboratorio de profundización — Identificación de entidades del dominio.**

1. Analiza el proceso de ventas. 2. Separa Cliente, Producto, Pedido, LíneaPedido y Pago. 3. Distingue entidades de atributos y eventos. 4. Define identidad y ciclo de vida de cada entidad.

**Evidencia esperada.** Cada entidad representa un concepto persistente con identidad y responsabilidad claras.

**Seguridad y límites.** No convertir cada sustantivo del texto en una tabla sin validar significado y reglas.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.2 — Atributos

**Propósito y modelo.** Los atributos describen propiedades de una entidad y deben tener significado, dominio y reglas. Pueden ser simples, compuestos, derivados o multivaluados en el modelo conceptual; al implementarlos en un modelo relacional se decide cómo representarlos sin perder integridad.

**Ejemplo desarrollado.** Nombre completo puede modelarse como atributo compuesto por nombres y apellidos; edad es derivable de fecha de nacimiento y no suele almacenarse como dato permanente por cambiar con el tiempo.

**Práctica guiada.** Clasifica atributos de Cliente y Producto como obligatorios/opcionales, simples/compuestos y almacenados/derivados.

**Actividad independiente.** Define atributos para una entidad Reserva, indicando tipo conceptual, dominio, nulabilidad y restricciones.

**Criterios de aceptación.** Identifica atributos con semántica precisa y evita duplicar datos derivados sin una razón documentada.

**Errores frecuentes.** Almacenar edad como dato estable o usar una columna genérica «datos» para atributos independientes sin esquema definido.

**Comprobación.** ¿Qué problema de consistencia puede aparecer si se almacena un valor derivado y no se actualiza cuando cambia su origen?

**Laboratorio de profundización — Diccionario de atributos.**

1. Para Cliente y Producto define atributos, descripción, tipo, nulabilidad y ejemplo. 2. Distingue atributo simple, compuesto, multivaluado y derivado. 3. Identifica datos sensibles. 4. Documenta restricciones.

**Evidencia esperada.** El diccionario es consistente y evita duplicación o ambigüedad semántica.

**Seguridad y límites.** Minimizar datos personales y definir propósito y retención.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.3 — Relaciones

**Propósito y modelo.** Una relación expresa asociación entre entidades. En el modelo relacional se implementa normalmente mediante claves foráneas, tablas asociativas o estructuras específicas. Debe describirse con verbo y reglas del negocio: Cliente realiza Pedido, Pedido contiene Producto.

**Ejemplo desarrollado.** Un pedido pertenece a un cliente; la clave foránea cliente_id en Pedido representa la asociación y permite comprobar que el cliente referenciado existe.

**Práctica guiada.** Identifica relaciones en un escenario de cursos: Estudiante se matricula en Curso, Docente imparte Curso y Curso tiene Aula. Añade verbo y regla de negocio.

**Actividad independiente.** Modela relaciones de un sistema de reservas y determina qué entidad conserva la clave foránea.

**Criterios de aceptación.** Describe relación con semántica y define implementación coherente.

**Errores frecuentes.** Crear relaciones solo por similitud de nombres o almacenar el nombre del relacionado en lugar de su clave estable.

**Comprobación.** ¿Qué ventaja aporta una clave foránea frente a copiar el nombre del cliente en cada pedido?

**Laboratorio de profundización — Mapa de relaciones entre entidades.**

1. Relaciona Cliente con Pedido, Pedido con LíneaPedido y Producto con LíneaPedido. 2. Define sentido de cada relación. 3. Identifica opcionalidad. 4. Traduce el modelo a claves foráneas conceptuales.

**Evidencia esperada.** Las relaciones reflejan reglas del negocio y evitan vínculos implícitos o ambiguos.

**Seguridad y límites.** No asumir que una relación existe solo porque dos tablas comparten nombres de columnas.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.4 — Cardinalidad

**Propósito y modelo.** La cardinalidad describe cuántas instancias de una entidad pueden asociarse con otra: uno a uno, uno a muchos y muchos a muchos. La participación puede ser obligatoria u opcional; estas reglas deben derivarse del negocio y reflejarse en restricciones.

**Ejemplo desarrollado.** Un cliente puede realizar muchos pedidos, pero cada pedido pertenece a un cliente: 1:N. Un estudiante puede cursar muchos cursos y cada curso tener muchos estudiantes: N:M.

**Práctica guiada.** Clasifica cinco asociaciones de un sistema académico y especifica mínimos y máximos en ambos extremos.

**Actividad independiente.** Modela un sistema de citas donde un profesional atiende múltiples citas y cada cita corresponde a un profesional y paciente.

**Criterios de aceptación.** Identifica cardinalidad y opcionalidad desde ambas entidades, no solo desde una dirección.

**Errores frecuentes.** Confundir cardinalidad con cantidad actual de filas o interpretar 1:N como una restricción de una sola fila histórica.

**Comprobación.** ¿Qué diferencia hay entre una relación 1:N y una N:M?

**Laboratorio de profundización — Casos de cardinalidad y opcionalidad.**

1. Modela uno-a-uno, uno-a-muchos y muchos-a-muchos. 2. Para cada relación define mínimo y máximo en ambos extremos. 3. Justifica con reglas del negocio. 4. Explica qué cardinalidad requiere una tabla asociativa.

**Evidencia esperada.** Cada extremo de relación tiene multiplicidad y opcionalidad documentadas.

**Seguridad y límites.** No deducir cardinalidad solo a partir de ejemplos de datos pequeños.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.5 — Claves primarias

**Propósito y modelo.** Una clave primaria identifica de forma única cada fila y no admite NULL. Puede ser natural o sustituta; debe ser estable, mínima y no depender de atributos que cambian con frecuencia. En SQL la restricción PRIMARY KEY impone unicidad y no nulidad.

**Ejemplo desarrollado.** Un código interno inmutable puede servir como clave natural; un identificador generado puede ser sustituto. El nombre de una persona no es buena clave porque puede repetirse o cambiar.

**Práctica guiada.** Elige clave primaria para Cliente, Producto y Pedido en un modelo de ejemplo. Comprueba unicidad y estabilidad de las candidatas.

**Actividad independiente.** Evalúa cuándo utilizar clave compuesta frente a identificador sustituto para una tabla de detalle de pedido.

**Criterios de aceptación.** Justifica unicidad, estabilidad y minimalidad; distingue PK de índice no único.

**Errores frecuentes.** Utilizar correo electrónico como clave sin analizar cambios o creer que una PK debe ser siempre un entero autoincremental.

**Comprobación.** ¿Qué características hacen que una clave sea adecuada como identificador primario?

**Laboratorio de profundización — Selección de clave primaria.**

1. Compara clave natural y sustituta para Cliente. 2. Define unicidad, no nulidad y estabilidad. 3. Explica claves compuestas y cuándo evitar exceso de columnas. 4. Diseña una restricción primaria.

**Evidencia esperada.** La clave identifica de forma estable cada fila y no depende de atributos volátiles sin justificación.

**Seguridad y límites.** No usar email o teléfono como clave primaria sin analizar cambios, privacidad y unicidad.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.6 — Claves foráneas

**Propósito y modelo.** Una clave foránea relaciona una o varias columnas con una clave candidata de otra tabla y aplica integridad referencial. Las acciones ON DELETE/UPDATE (RESTRICT, CASCADE, SET NULL u otras según motor) definen comportamiento ante cambios; deben reflejar reglas del dominio.

**Ejemplo desarrollado.** Pedido.cliente_id referencia Cliente.id. Si un cliente tiene pedidos, eliminarlo puede rechazarse o manejarse mediante política explícita; CASCADE indiscriminado podría borrar historial comercial.

**Práctica guiada.** Diseña dos tablas con PK y FK y prueba conceptualmente inserción válida, referencia inexistente y eliminación de padre con hijos.

**Actividad independiente.** Elige acciones referenciales para Usuario, Pedido y DetallePedido; justifica preservación de historial.

**Criterios de aceptación.** Explica integridad referencial y predice resultado de inserción, actualización y borrado.

**Errores frecuentes.** Usar CASCADE sin evaluar consecuencias o asumir que todos los motores aplican restricciones con idéntica configuración por defecto.

**Comprobación.** ¿Qué anomalía evita una clave foránea cuando se inserta una fila hija?

**Laboratorio de profundización — Integridad referencial entre tablas.**

1. Define Pedido con FK hacia Cliente. 2. Simula inserción válida y referencia inexistente. 3. Compara RESTRICT, CASCADE y SET NULL. 4. Decide qué política corresponde al borrado de un cliente con pedidos históricos.

**Evidencia esperada.** La relación impide referencias huérfanas y la política de borrado responde a reglas de negocio.

**Seguridad y límites.** No usar ON DELETE CASCADE por defecto en datos financieros o históricos.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.7 — Restricciones

**Propósito y modelo.** Las restricciones expresan reglas que el DBMS debe hacer cumplir: NOT NULL, UNIQUE, CHECK, PRIMARY KEY y FOREIGN KEY. Son una defensa de integridad incluso cuando varias aplicaciones escriben datos. Las reglas complejas pueden requerir triggers o lógica transaccional, pero no deben reemplazar restricciones declarativas disponibles.

**Ejemplo desarrollado.** CHECK (precio >= 0) rechaza valores negativos; UNIQUE(correo) impide duplicados según reglas de comparación/collation del motor. NULL tiene semántica particular en comparaciones y restricciones.

**Práctica guiada.** Diseña restricciones para Producto y Usuario y simula casos válidos e inválidos. Distingue NULL, cadena vacía y valor por defecto.

**Actividad independiente.** Construye una matriz de reglas de negocio y asigna cada una a NOT NULL, UNIQUE, CHECK, FK o validación de aplicación.

**Criterios de aceptación.** Selecciona restricción adecuada y explica cómo se prueba su cumplimiento.

**Errores frecuentes.** Confiar solo en validación frontend o asumir que CHECK trata NULL como falso en todos los casos.

**Comprobación.** ¿Por qué una regla de integridad debe imponerse también en la base de datos y no solo en la interfaz?

**Laboratorio de profundización — Reglas de integridad de dominio.**

1. Define NOT NULL, UNIQUE, CHECK y DEFAULT para Producto. 2. Diseña ejemplos que deben aceptarse y rechazarse. 3. Explica diferencia entre validación de aplicación y restricción del DBMS. 4. Documenta mensajes de error esperados.

**Evidencia esperada.** Las restricciones protegen invariantes aun cuando distintos clientes escriban en la base.

**Seguridad y límites.** No depender exclusivamente de validación en interfaz para proteger integridad.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.8 — Diagramas entidad-relación

**Propósito y modelo.** Un diagrama entidad-relación representa entidades, atributos, relaciones, cardinalidad y opcionalidad. La notación (Chen, pata de gallo u otras) puede variar; lo importante es que el modelo sea inequívoco y trazable a requisitos.

**Ejemplo desarrollado.** Un diagrama de pedidos muestra Cliente 1:N Pedido y Pedido 1:N Detalle; Detalle N:1 Producto. Así se hace explícita la tabla intermedia que resuelve la relación entre pedido y producto.

**Práctica guiada.** Dibuja ER para biblioteca con Usuario, Libro, Ejemplar y Préstamo. Marca claves y cardinalidades.

**Actividad independiente.** Modela una tienda en línea y revisa si el diagrama permite representar pedidos sin productos, productos nunca vendidos y clientes sin pedidos.

**Criterios de aceptación.** El diagrama cubre requisitos, claves, cardinalidades y opcionalidad sin ambigüedad.

**Errores frecuentes.** Omitir opcionalidad, duplicar entidades o usar relaciones N:M sin explicar su transformación relacional.

**Comprobación.** ¿Qué información comunica la cardinalidad que no se deduce solo del nombre de la relación?

**Laboratorio de profundización — Construcción y lectura de un DER.**

1. Modela ventas con Cliente, Pedido, Producto y LíneaPedido. 2. Añade cardinalidades y opcionalidad. 3. Marca claves y atributos. 4. Revisa el diagrama con dos escenarios de negocio.

**Evidencia esperada.** El DER puede transformarse a tablas sin perder relaciones ni reglas principales.

**Seguridad y límites.** No omitir relaciones de detalle ni representar muchos-a-muchos sin resolver.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.9 — Modelo conceptual

**Propósito y modelo.** El modelo conceptual describe el dominio desde la perspectiva del negocio sin comprometerse con un DBMS o tipos físicos. Define conceptos, reglas, entidades y asociaciones. Debe poder validarse con usuarios y responsables del proceso.

**Ejemplo desarrollado.** Para una clínica, el modelo conceptual incluye Paciente, Profesional, Cita y Especialidad y reglas como «una cita tiene un paciente y un profesional». No decide aún si el identificador será UUID o BIGINT.

**Práctica guiada.** Extrae entidades y reglas de un enunciado de negocio y represéntalas sin tipos SQL.

**Actividad independiente.** Redacta un glosario de datos y un modelo conceptual para una biblioteca, validando términos con supuestos explícitos.

**Criterios de aceptación.** El modelo utiliza lenguaje del dominio, cubre reglas y evita decisiones físicas prematuras.

**Errores frecuentes.** Mezclar nombres de columnas o detalles de motor en el modelo conceptual o ignorar términos ambiguos del negocio.

**Comprobación.** ¿Por qué el modelo conceptual debe ser comprensible para personas que no conocen SQL?

**Laboratorio de profundización — Modelo independiente del motor.**

1. Describe entidades, relaciones y reglas sin elegir MySQL o PostgreSQL. 2. Valida el modelo con escenarios de venta, devolución y pago parcial. 3. Identifica conceptos ambiguos. 4. Registra decisiones y preguntas abiertas.

**Evidencia esperada.** El modelo representa el dominio y puede revisarse con usuarios no técnicos.

**Seguridad y límites.** No incluir decisiones físicas como índices o tipos específicos antes de definir el dominio.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.10 — Modelo lógico

**Propósito y modelo.** El modelo lógico transforma conceptos en estructuras de datos independientes del almacenamiento físico concreto. Define tablas o relaciones, atributos, claves, restricciones y relaciones normalizadas. Debe resolver N:M y precisar dominios antes de elegir índices y parámetros del motor.

**Ejemplo desarrollado.** Cliente, Pedido y DetallePedido constituyen un modelo lógico relacional; DetallePedido contiene claves foráneas a Pedido y Producto y atributos como cantidad y precio_unitario histórico.

**Práctica guiada.** Convierte el modelo conceptual de biblioteca en tablas lógicas con PK, FK, tipos abstractos y restricciones.

**Actividad independiente.** Revisa un modelo lógico para detectar atributos multivaluados, claves ausentes y relaciones N:M no resueltas.

**Criterios de aceptación.** El modelo lógico es consistente, normalizado según necesidades y trazable al modelo conceptual.

**Errores frecuentes.** Saltar directamente a CREATE TABLE sin validar relaciones o copiar datos derivados en múltiples tablas sin estrategia.

**Comprobación.** ¿Qué decisiones pertenecen al modelo lógico y cuáles se reservan para el modelo físico?

**Laboratorio de profundización — Transformación a relaciones.**

1. Convierte el DER en tablas, atributos, claves y restricciones. 2. Resuelve relaciones muchos-a-muchos. 3. Revisa dependencias funcionales iniciales. 4. Comprueba que el modelo cubra escenarios del negocio.

**Evidencia esperada.** El modelo lógico tiene tablas, claves y relaciones completas sin depender aún de un motor concreto.

**Seguridad y límites.** No confundir modelo lógico con diseño de almacenamiento físico.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.

#### 9.2.11 — Modelo físico

**Propósito y modelo.** El modelo físico concreta el diseño para un DBMS y versión: tipos reales, índices, particiones, tablespaces, collation, almacenamiento, parámetros y estrategias de respaldo. Debe considerar carga, volumen, concurrencia, seguridad y operación. La portabilidad puede reducirse por características específicas del motor.

**Ejemplo desarrollado.** Un campo decimal de importe puede definirse como DECIMAL(12,2) en MySQL o NUMERIC(12,2) en PostgreSQL; la semántica es similar pero los detalles de implementación y sintaxis pueden diferir.

**Práctica guiada.** Traduce un modelo lógico de pedidos a DDL para un motor de laboratorio y documenta decisiones de tipos, índices y restricciones.

**Actividad independiente.** Compara dos modelos físicos para una tabla de eventos de alto volumen y justifica índice, partición y retención según consultas esperadas.

**Criterios de aceptación.** Identifica decisiones dependientes del motor y justifica cada una con requisitos medibles.

**Errores frecuentes.** Diseñar índices sin conocer consultas o asumir que el modelo físico es portable entre motores sin ajustes.

**Comprobación.** ¿Por qué un índice útil para una carga de lectura puede perjudicar una carga con muchas escrituras?

### 9.3 — MySQL


**Laboratorio de profundización — Diseño específico del motor.**

1. Selecciona un motor y versión de laboratorio. 2. Traduce tipos y restricciones a DDL. 3. Define índices iniciales según consultas esperadas. 4. Documenta charset, collation, almacenamiento y respaldo.

**Evidencia esperada.** El modelo físico puede implementarse en el motor elegido y registra decisiones dependientes de versión.

**Seguridad y límites.** No copiar DDL entre motores sin revisar diferencias de tipos, índices y restricciones.

**Registro sugerido.** Documenta supuestos, diccionario de datos, diagrama o DDL propuesto, casos aceptados/rechazados y decisiones pendientes. No marques implementación como ejecutada sin evidencia real.
#### 9.3.1 — Instalación de MySQL Server

**Propósito y modelo.** MySQL Server es el proceso DBMS que administra instancias y acepta conexiones. La instalación depende del sistema operativo, versión, repositorio y método de distribución. En entornos productivos se debe usar una versión soportada, verificar origen e integridad de paquetes, definir cuentas y restringir exposición de red.

**Ejemplo desarrollado.** Instalar un paquete no significa que el servidor esté configurado de forma segura. Deben revisarse servicio, puerto, interfaz de escucha, autenticación, cuentas por defecto, actualizaciones y respaldo inicial.

**Práctica guiada.** En una VM desechable, consulta la documentación oficial de instalación para el sistema elegido. Registra versión, origen del paquete, dependencias y método de verificación. No instales ni modifiques el DBMS del host compartido.

**Actividad independiente.** Elabora un procedimiento reproducible para instalar MySQL en una VM, incluyendo requisitos, verificación de paquetes, configuración inicial, rollback y evidencia.

**Criterios de aceptación.** Identifica producto y versión, documenta fuente y distingue instalación de hardening posterior.

**Errores frecuentes.** Descargar binarios de sitios no oficiales, exponer 3306 indiscriminadamente o asumir que el asistente de instalación elimina todas las cuentas inseguras.

**Comprobación.** ¿Qué controles deben verificarse después de instalar MySQL y antes de permitir conexiones de aplicación?

#### 9.3.2 — Configuración

**Propósito y modelo.** MySQL se configura mediante archivos de opciones y parámetros del servidor. Los valores afectan memoria, conexiones, logs, charset, autenticación, rutas y red. Las opciones disponibles y valores por defecto dependen de versión y distribución; deben verificarse con documentación correspondiente.

**Ejemplo desarrollado.** `bind-address` limita interfaces de escucha; `max_connections` limita conexiones concurrentes; `character_set_server` y collation afectan representación y comparación de texto. Cambiar parámetros sin medir puede degradar servicio.

**Práctica guiada.** Consulta variables con `SHOW VARIABLES` en una instancia de laboratorio y documenta puerto, bind address, charset y límites de conexión. No cambies valores de producción.

**Actividad independiente.** Propón configuración mínima para un servidor de laboratorio que solo acepte conexiones locales y registre errores, justificando cada parámetro.

**Criterios de aceptación.** Distingue configuración global, sesión y persistencia de variables según versión; vincula cambios a un objetivo medible.

**Errores frecuentes.** Copiar my.cnf de otra versión, asignar memoria excesiva o abrir bind-address a todas las interfaces sin firewall.

**Comprobación.** ¿Por qué un parámetro que mejora una carga puede perjudicar otra?

#### 9.3.3 — MySQL Workbench

**Propósito y modelo.** MySQL Workbench es una herramienta gráfica para modelado, administración y consulta de MySQL. Es un cliente; no reemplaza al servidor. Las acciones disponibles dependen de versión, permisos de conexión y capacidades del motor.

**Ejemplo desarrollado.** Una conexión guardada contiene host, puerto y usuario; almacenar la contraseña requiere evaluar el mecanismo de credenciales del sistema. Un diagrama EER puede ayudar a visualizar tablas, pero su exportación debe revisarse antes de aplicar cambios.

**Práctica guiada.** Abre Workbench en un entorno de laboratorio y crea una conexión de prueba sin guardar credenciales reales. Inspecciona editor SQL, navegador de esquemas y modelado EER.

**Actividad independiente.** Crea un diagrama para un esquema de biblioteca y documenta cómo generar DDL revisable sin ejecutarlo en una base productiva.

**Criterios de aceptación.** Diferencia cliente y servidor; identifica conexión, editor, esquema y modelo.

**Errores frecuentes.** Creer que Workbench almacena los datos o ejecutar sincronización de modelo directamente contra producción sin revisión.

**Comprobación.** ¿Qué componente debe estar disponible para que Workbench ejecute una consulta SQL?

#### 9.3.4 — Creación de bases de datos

**Propósito y modelo.** CREATE DATABASE crea un contenedor lógico dentro de la instancia MySQL. Charset y collation definen comportamiento de almacenamiento y comparación de texto; deben elegirse según idioma, compatibilidad y requisitos. El nombre debe seguir convenciones y evitar colisiones.

**Ejemplo desarrollado.** `CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE ...` ilustra selección explícita, pero la collation exacta debe elegirse según versión instalada y necesidades de comparación.

**Práctica guiada.** En una instancia desechable crea una base de datos de prueba con charset/collation documentados, consulta `SHOW CREATE DATABASE` y elimina solo el objeto de laboratorio al finalizar.

**Actividad independiente.** Define convención de nombres, charset y collation para una aplicación multilingüe y explica cómo probar ordenamiento y comparaciones.

**Criterios de aceptación.** Explica base lógica, charset y collation y verifica la definición creada.

**Errores frecuentes.** Usar charset heredado sin revisar compatibilidad o ejecutar DROP DATABASE sin confirmar nombre y respaldo.

**Comprobación.** ¿Qué diferencia existe entre charset y collation?

#### 9.3.5 — Creación de tablas

**Propósito y modelo.** CREATE TABLE define columnas, tipos, claves y restricciones. El DDL debe reflejar el modelo lógico, integridad y necesidades de consulta. Tipos, índices y acciones referenciales deben ser compatibles con la versión y motor de almacenamiento seleccionados.

**Ejemplo desarrollado.** Una tabla Pedido puede declarar id como clave primaria, cliente_id como clave foránea, fecha como DATETIME y total como DECIMAL con precisión definida. La restricción debe impedir valores fuera de las reglas de negocio.

**Práctica guiada.** En una base desechable crea tablas Cliente y Pedido con PK, FK y NOT NULL. Inserta una fila válida y prueba que una referencia inexistente sea rechazada.

**Actividad independiente.** Implementa DDL para biblioteca con Usuario, Ejemplar y Préstamo; incluye índices justificados y restricciones.

**Criterios de aceptación.** El DDL corresponde al modelo, aplica integridad y se valida con casos válidos e inválidos.

**Errores frecuentes.** Omitir claves foráneas, usar FLOAT para dinero o crear índices duplicados sin revisar restricciones.

**Comprobación.** ¿Por qué una clave foránea debe definirse además de documentar la relación en un diagrama?

#### 9.3.6 — Usuarios

**Propósito y modelo.** MySQL distingue cuentas por nombre de usuario y host de origen, representadas como 'usuario'@'host'. Una misma etiqueta de usuario con hosts distintos puede representar cuentas diferentes. La autenticación y los plugins disponibles dependen de versión; las aplicaciones deben usar cuentas nominativas y no root.

**Ejemplo desarrollado.** 'app'@'localhost' no es necesariamente la misma cuenta que 'app'@'%'. La segunda puede aceptar conexiones desde más orígenes si la red y el firewall lo permiten.

**Práctica guiada.** Consulta cuentas de una instancia de laboratorio mediante vistas administrativas autorizadas, ocultando hashes y datos sensibles. No crees cuentas con host comodín sin justificación.

**Actividad independiente.** Diseña cuentas separadas para aplicación, migraciones y administración, con orígenes y responsabilidades limitados.

**Criterios de aceptación.** Explica componente usuario/host y diferencia cuenta de aplicación y cuenta administrativa.

**Errores frecuentes.** Compartir root con la aplicación o usar 'usuario'@'%' por comodidad sin restricciones de red.

**Comprobación.** ¿Por qué el componente host forma parte de la identidad de una cuenta MySQL?

#### 9.3.7 — Permisos

**Propósito y modelo.** MySQL utiliza privilegios globales, de base, tabla, columna y otros ámbitos. GRANT concede capacidades; REVOKE las retira. El principio de mínimo privilegio requiere conceder solo operaciones necesarias, evitando privilegios administrativos a cuentas de aplicación.

**Ejemplo desarrollado.** Una aplicación que consulta y registra operaciones puede necesitar SELECT, INSERT y UPDATE en tablas concretas, pero no CREATE USER, FILE, SUPER ni privilegios globales. El conjunto exacto depende del diseño.

**Práctica guiada.** En un entorno desechable inspecciona grants de una cuenta de prueba con `SHOW GRANTS`. Compara permisos de lectura con permisos de modificación sin concederlos en un servidor compartido.

**Actividad independiente.** Diseña privilegios por rol para aplicación, analista de solo lectura y DBA; especifica alcance y proceso de revisión.

**Criterios de aceptación.** Identifica alcance del privilegio y justifica concesiones y revocaciones.

**Errores frecuentes.** Conceder ALL PRIVILEGES globalmente, usar GRANT OPTION innecesariamente o dejar cuentas de prueba activas.

**Comprobación.** ¿Qué daño puede causar una cuenta de aplicación que posee privilegios administrativos globales?

#### 9.3.8 — Conexiones

**Propósito y modelo.** Una conexión MySQL utiliza protocolo cliente-servidor sobre transporte configurado, habitualmente TCP. Host, puerto, usuario, autenticación, TLS y reglas de red determinan si la sesión puede establecerse. El puerto por defecto habitual es 3306, pero puede cambiarse.

**Ejemplo desarrollado.** Una conexión rechazada puede deberse a servicio detenido, puerto incorrecto, bind-address, firewall, cuenta host no coincidente o credenciales inválidas. Diagnosticar requiere separar conectividad TCP de autenticación y autorización SQL.

**Práctica guiada.** Desde una VM de laboratorio consulta estado del servicio y puerto en escucha y realiza conexión local con un usuario de prueba. No expongas el puerto a Internet ni guardes contraseñas en historial.

**Actividad independiente.** Crea un árbol de diagnóstico para timeout, connection refused, access denied y TLS error.

**Criterios de aceptación.** Diferencia conectividad, autenticación y autorización y documenta cada causa posible.

**Errores frecuentes.** Resolver cualquier error abriendo el firewall a todos los orígenes o utilizar credenciales administrativas desde aplicaciones.

**Comprobación.** ¿Qué diferencia existe entre «connection refused» y «access denied»?

#### 9.3.9 — Una distinción importante

**Propósito y modelo.** Deben distinguirse producto MySQL, servidor MySQL, instancia en ejecución, base de datos/esquema, tabla, cliente y protocolo. En MySQL, «schema» y «database» suelen utilizarse como sinónimos en SQL, pero otros motores, como PostgreSQL, tienen una jerarquía distinta. La terminología debe mantenerse precisa al comparar motores.

**Ejemplo desarrollado.** Workbench es un cliente; mysqld es el servidor; una instancia es un proceso/configuración en ejecución; dentro de ella pueden existir varias bases, tablas y cuentas. Instalar Workbench no instala automáticamente el servicio servidor.

**Práctica guiada.** Clasifica los componentes de una instalación local y dibuja cómo el cliente envía una consulta al servidor y recibe filas.

**Actividad independiente.** Redacta un glosario comparativo MySQL/PostgreSQL para database, schema, instance, role/user, client y server.

**Criterios de aceptación.** Usa correctamente la terminología y explica al menos una diferencia semántica entre motores.

**Errores frecuentes.** Tratar cliente, motor e instancia como sinónimos o trasladar convenciones de PostgreSQL a MySQL sin revisar.

**Comprobación.** ¿Por qué es importante aclarar qué significa «schema» cuando se documenta una solución que puede usar distintos DBMS?

### 9.4 — SQL

#### 9.4.1 — DDL

**Propósito y modelo.** DDL (Data Definition Language) define o modifica estructuras de base de datos: tablas, vistas, índices y otros objetos. CREATE, ALTER y DROP son operaciones DDL comunes. El comportamiento transaccional y bloqueos de DDL varían por motor y versión, por lo que no debe suponerse que toda operación es fácilmente reversible.

**Ejemplo desarrollado.** CREATE TABLE define estructura inicial; ALTER TABLE añade o cambia una columna; DROP TABLE elimina la tabla y sus datos. La migración debe planificarse con respaldo y ventana cuando corresponda.

**Práctica guiada.** Clasifica sentencias SQL de ejemplo como DDL, DML, DQL, DCL o TCL. En una base desechable crea una tabla y revisa su definición.

**Actividad independiente.** Diseña una migración que añada una columna obligatoria a una tabla existente sin romper filas anteriores.

**Criterios de aceptación.** Reconoce operaciones DDL y explica su impacto sobre esquema y datos.

**Errores frecuentes.** Ejecutar DROP en el esquema equivocado o asumir rollback universal para cambios estructurales.

**Comprobación.** ¿Qué diferencia de impacto existe entre ALTER TABLE y UPDATE?

#### 9.4.2 — DML

**Propósito y modelo.** DML manipula filas mediante INSERT, UPDATE y DELETE, y en algunas clasificaciones incluye MERGE. Estas operaciones pueden afectar una o muchas filas; una condición WHERE ausente o incorrecta puede modificar datos masivamente. La transacción y el respaldo son controles importantes.

**Ejemplo desarrollado.** UPDATE Producto SET activo = 0 WHERE id = 42 limita el cambio a un registro identificado. Antes de ejecutar, un SELECT con la misma condición permite revisar el conjunto objetivo.

**Práctica guiada.** En una base desechable inserta, actualiza y elimina registros sintéticos. Antes de UPDATE/DELETE ejecuta SELECT con la condición y verifica filas afectadas.

**Actividad independiente.** Prepara una secuencia de corrección de datos con transacción, validación previa, conteo afectado y rollback si el resultado no coincide.

**Criterios de aceptación.** Distingue DML de DDL y demuestra control del alcance de las modificaciones.

**Errores frecuentes.** Ejecutar UPDATE o DELETE sin WHERE, o asumir que una condición devuelve la cantidad de filas esperada sin comprobarla.

**Comprobación.** ¿Qué comprobación debe hacerse antes de ejecutar un DELETE sobre una tabla con muchos registros?

#### 9.4.3 — DQL

**Propósito y modelo.** DQL suele referirse a consultas de recuperación, especialmente SELECT. Aunque la clasificación de SQL varía entre textos, la operación central es proyectar columnas, filtrar filas, combinar relaciones, agrupar y ordenar resultados. La consulta debe devolver solo los datos necesarios.

**Ejemplo desarrollado.** SELECT nombre, precio FROM Producto WHERE activo = 1 ORDER BY nombre obtiene columnas específicas y aplica filtro y orden explícitos.

**Práctica guiada.** Consulta una tabla sintética con SELECT, WHERE y ORDER BY. Compara SELECT * con proyección explícita y observa el tamaño y claridad del resultado.

**Actividad independiente.** Construye consultas para responder cinco preguntas de negocio y explica cómo cada cláusula modifica el conjunto de resultados.

**Criterios de aceptación.** Explica proyección, selección y ordenamiento; evita recuperar columnas innecesarias.

**Errores frecuentes.** Confiar en el orden sin ORDER BY o utilizar SELECT * de forma indiscriminada en aplicaciones.

**Comprobación.** ¿Qué diferencia conceptual existe entre seleccionar columnas y filtrar filas?

#### 9.4.4 — DCL

**Propósito y modelo.** DCL agrupa sentencias de control de acceso, como GRANT y REVOKE en muchos DBMS. El alcance puede ser global, base, esquema, tabla, columna o función. La sintaxis y privilegios disponibles varían; deben probarse con cuentas de laboratorio y no con el usuario administrativo de producción.

**Ejemplo desarrollado.** Conceder SELECT sobre una tabla a un rol de analista permite consulta sin conceder UPDATE o DELETE. Retirar el permiso debe comprobarse mediante una nueva sesión y revisión de grants.

**Práctica guiada.** Lee sentencias GRANT/REVOKE y determina objeto, privilegio, principal y alcance. No concedas permisos reales en un servidor compartido.

**Actividad independiente.** Diseña roles de lectura, escritura operativa y administración con mínimo privilegio.

**Criterios de aceptación.** Identifica quién recibe qué privilegio sobre qué objeto y cómo verificarlo.

**Errores frecuentes.** Conceder ALL PRIVILEGES o WITH GRANT OPTION sin necesidad, o confundir autenticación con autorización.

**Comprobación.** ¿Por qué conviene asignar permisos a roles en vez de replicar grants manuales a cada usuario?

#### 9.4.5 — TCL

**Propósito y modelo.** TCL se refiere a control transaccional: BEGIN/START TRANSACTION, COMMIT, ROLLBACK y, según motor, SAVEPOINT. Permite agrupar cambios para que se confirmen o deshagan como unidad. El soporte depende del motor de almacenamiento, sentencia y configuración; algunas operaciones pueden producir commit implícito.

**Ejemplo desarrollado.** Transferir saldo entre cuentas requiere debitar y acreditar dentro de una transacción. Si falla la segunda operación, rollback evita dejar solo el débito aplicado.

**Práctica guiada.** En un motor transaccional de laboratorio inicia una transacción, modifica una fila sintética, consulta el cambio y ejecuta ROLLBACK. Repite y confirma con COMMIT.

**Actividad independiente.** Diseña transacción de transferencia con validación de saldo, bloqueo adecuado y manejo de errores.

**Criterios de aceptación.** Diferencia COMMIT y ROLLBACK y explica atomicidad de un conjunto de operaciones.

**Errores frecuentes.** Suponer que todas las tablas/operaciones son transaccionales o ejecutar DDL dentro de una transacción esperando rollback universal.

**Comprobación.** ¿Qué riesgo evita agrupar el débito y crédito en una misma transacción?

#### 9.4.6 — CREATE

**Propósito y modelo.** CREATE define objetos como bases de datos, tablas, vistas, índices, roles y otros elementos. Cada objeto tiene sintaxis, permisos y ciclo de vida propios. Antes de crear, comprueba esquema destino, nombre, dependencias, restricciones y convenciones.

**Ejemplo desarrollado.** CREATE TABLE define columnas y restricciones; CREATE INDEX crea una estructura para acelerar ciertas consultas con costo adicional en escrituras y almacenamiento.

**Práctica guiada.** En un esquema desechable crea una tabla con PK, NOT NULL y CHECK cuando el motor lo soporte. Consulta metadatos para verificar definición.

**Actividad independiente.** Escribe DDL para una entidad con dos relaciones y justifica tipos, claves e índices.

**Criterios de aceptación.** El objeto se crea en el esquema esperado y las restricciones corresponden al modelo.

**Errores frecuentes.** Ejecutar CREATE en el esquema incorrecto o crear índices sin una consulta objetivo.

**Comprobación.** ¿Qué verificaciones previas evitan crear accidentalmente un objeto en la base equivocada?

#### 9.4.7 — ALTER

**Propósito y modelo.** ALTER modifica estructura de objetos existentes. Puede añadir, cambiar o eliminar columnas, restricciones e índices. El impacto sobre datos, bloqueos, compatibilidad y tiempo de ejecución depende del DBMS, versión, tamaño y operación.

**Ejemplo desarrollado.** Añadir una columna nullable puede ser menos riesgoso que añadir una columna NOT NULL sin valor por defecto a una tabla grande. Una migración escalonada puede añadir, rellenar y luego restringir.

**Práctica guiada.** En una tabla desechable añade una columna opcional, revisa metadatos y elimina solo el objeto de laboratorio al finalizar.

**Actividad independiente.** Planifica una migración para convertir una columna opcional en obligatoria con datos históricos; incluye validación y rollback posible.

**Criterios de aceptación.** Describe estado previo/posterior, impacto sobre filas y compatibilidad de aplicación.

**Errores frecuentes.** Cambiar tipos en producción sin evaluar truncamiento o asumir que ALTER es instantáneo y no bloqueante.

**Comprobación.** ¿Por qué una migración de esquema debe coordinarse con las versiones de la aplicación que escriben datos?

#### 9.4.8 — DROP

**Propósito y modelo.** DROP elimina objetos de base de datos. DROP TABLE elimina definición y datos de la tabla; DROP DATABASE puede eliminar todo el contenedor lógico. La reversibilidad depende de respaldos, motor y operación; no debe ejecutarse sin verificar objeto, entorno y autorización.

**Ejemplo desarrollado.** Eliminar una tabla temporal de laboratorio no es equivalente a eliminar una tabla de producción con dependencias y datos históricos. Las claves foráneas y vistas pueden impedir o verse afectadas por el cambio.

**Práctica guiada.** En un esquema desechable crea una tabla temporal, inspecciona su contenido y elimínala explícitamente. Nunca ejecutes DROP sobre bases compartidas.

**Actividad independiente.** Redacta un checklist previo a una eliminación: confirmar ambiente, nombre calificado, dependencias, respaldo restaurable, aprobación y plan de recuperación.

**Criterios de aceptación.** Diferencia DROP de DELETE y TRUNCATE y describe consecuencias.

**Errores frecuentes.** Usar DROP por error en lugar de DELETE o ejecutar comandos destructivos en una conexión cuyo entorno no se verificó.

**Comprobación.** ¿Qué información debe confirmarse antes de ejecutar DROP TABLE?

#### 9.4.9 — SELECT

**Propósito y modelo.** SELECT recupera datos mediante proyección, filtros, joins, agrupación, ordenamiento y expresiones. SQL opera sobre conjuntos y el orden solo está garantizado cuando se especifica ORDER BY. NULL requiere operadores IS NULL/IS NOT NULL y lógica de tres valores.

**Ejemplo desarrollado.** SELECT nombre FROM Cliente WHERE ciudad = 'Manizales' ORDER BY nombre; devuelve una proyección filtrada y ordenada. La ubicación del ejemplo es ilustrativa y no implica datos reales.

**Práctica guiada.** Escribe consultas que seleccionen columnas, filtren por rango y ordenen por dos atributos. Incluye una consulta que detecte valores NULL.

**Actividad independiente.** Responde preguntas de negocio con SELECT y explica por qué cada condición está en WHERE o en otra cláusula.

**Criterios de aceptación.** La consulta devuelve filas esperadas, maneja NULL y especifica orden cuando importa.

**Errores frecuentes.** Comparar con NULL usando =, depender del orden físico o filtrar agregados en WHERE en lugar de HAVING.

**Comprobación.** ¿Por qué `columna = NULL` no es la forma correcta de buscar valores nulos?

#### 9.4.10 — INSERT

**Propósito y modelo.** INSERT agrega filas y debe respetar tipos, claves, restricciones y valores obligatorios. Es recomendable declarar explícitamente columnas para evitar dependencia del orden físico del esquema. Inserciones masivas deben validar duplicados, integridad y tamaño de transacción.

**Ejemplo desarrollado.** INSERT INTO Producto(nombre, precio) VALUES ('Teclado', 25.50) es más robusto que omitir la lista de columnas. La PK puede generarse según configuración del motor.

**Práctica guiada.** Inserta registros sintéticos con columnas explícitas. Prueba un caso que viole NOT NULL o UNIQUE y observa el error sin desactivar restricciones.

**Actividad independiente.** Diseña carga de datos de un CSV con validación de tipos, filas rechazadas, duplicados y registro de resultados.

**Criterios de aceptación.** Inserta filas válidas, detecta violaciones y documenta cantidad aceptada/rechazada.

**Errores frecuentes.** Omitir columnas y confiar en orden implícito, concatenar datos de usuario en SQL o ignorar errores de integridad.

**Comprobación.** ¿Qué riesgo reduce indicar explícitamente la lista de columnas en INSERT?

#### 9.4.11 — UPDATE

**Propósito y modelo.** UPDATE modifica columnas de filas que satisfacen una condición. WHERE define el alcance; sin ella, todas las filas pueden cambiar. En operaciones críticas conviene usar transacción, verificar conteo y revisar filas objetivo antes y después.

**Ejemplo desarrollado.** UPDATE Producto SET precio = 30 WHERE id = 7 limita el cambio por clave primaria. Un UPDATE masivo puede ser correcto, pero debe diseñarse y validarse explícitamente.

**Práctica guiada.** En una tabla de laboratorio ejecuta SELECT con la condición, UPDATE dentro de transacción y verifica resultado antes de COMMIT o ROLLBACK.

**Actividad independiente.** Diseña una actualización por lote con criterios de idempotencia, auditoría y recuperación.

**Criterios de aceptación.** La condición coincide con el conjunto esperado y se documenta número de filas afectadas.

**Errores frecuentes.** Omitir WHERE, utilizar condiciones no selectivas o no verificar filas afectadas.

**Comprobación.** ¿Qué paso permite detectar que un UPDATE afectará más filas de las previstas?

#### 9.4.12 — DELETE

**Propósito y modelo.** DELETE elimina filas que cumplen una condición y puede participar en transacciones según motor/tabla. Sin WHERE elimina todas las filas de la tabla, aunque conserva su estructura. Las claves foráneas pueden restringir o propagar eliminación según ON DELETE.

**Ejemplo desarrollado.** DELETE FROM Sesion WHERE expira_en < fecha; puede borrar múltiples filas y debe probarse con SELECT equivalente y transacción antes de confirmar.

**Práctica guiada.** En un esquema de laboratorio identifica filas candidatas con SELECT, elimina solo un registro sintético y comprueba restricciones referenciales.

**Actividad independiente.** Diseña una política de retención que archive o elimine datos vencidos respetando obligaciones y relaciones.

**Criterios de aceptación.** Explica alcance de WHERE, acciones referenciales y diferencia entre DELETE y DROP.

**Errores frecuentes.** Ejecutar DELETE sin filtro, asumir que rollback siempre está disponible o borrar datos históricos requeridos.

**Comprobación.** ¿Por qué un SELECT con la misma condición debe preceder a un DELETE de alcance amplio?

#### 9.4.13 — WHERE

**Propósito y modelo.** WHERE filtra filas antes de agrupación y proyección final. Admite comparaciones, operadores lógicos, BETWEEN, IN, LIKE y pruebas de NULL. La precedencia de AND/OR debe controlarse con paréntesis; las funciones aplicadas a columnas pueden afectar uso de índices.

**Ejemplo desarrollado.** WHERE estado = 'activo' AND (pais = 'CO' OR pais = 'MX') agrupa correctamente las alternativas. Sin paréntesis, la lógica puede incluir filas no deseadas.

**Práctica guiada.** Construye filtros con AND, OR, NOT, IN y BETWEEN sobre datos sintéticos. Compara resultado con y sin paréntesis.

**Actividad independiente.** Traduce requisitos en lenguaje natural a condiciones SQL y prueba valores límite, NULL y cadenas con caracteres especiales.

**Criterios de aceptación.** La condición expresa exactamente el requisito y cubre casos límite.

**Errores frecuentes.** Ignorar precedencia lógica, usar LIKE cuando se requiere igualdad o comparar NULL con operadores ordinarios.

**Comprobación.** ¿Qué cambia al agrupar una condición OR entre paréntesis dentro de una expresión AND?

#### 9.4.14 — ORDER BY

**Propósito y modelo.** ORDER BY define el orden del resultado por una o varias expresiones, con dirección ASC o DESC. Sin ORDER BY el motor puede devolver filas en cualquier orden. El tratamiento de NULL, collation y empates puede variar por motor.

**Ejemplo desarrollado.** ORDER BY fecha DESC, id ASC ordena primero por fecha descendente y usa id para resolver empates de manera determinista.

**Práctica guiada.** Ordena datos sintéticos por fecha, precio y nombre. Añade un segundo criterio para estabilizar empates.

**Actividad independiente.** Diseña orden para paginación consistente y explica por qué ordenar solo por un campo no único puede producir páginas inestables.

**Criterios de aceptación.** Define dirección y desempate; reconoce que orden no se conserva sin cláusula.

**Errores frecuentes.** Suponer orden de inserción o paginar sin orden determinista.

**Comprobación.** ¿Por qué conviene incluir una clave única como último criterio de orden al paginar?

#### 9.4.15 — GROUP BY

**Propósito y modelo.** GROUP BY agrupa filas con valores comunes para calcular agregados como COUNT, SUM, AVG, MIN y MAX. Las columnas seleccionadas deben ser agregadas o formar parte del agrupamiento según reglas del motor y modo SQL.

**Ejemplo desarrollado.** SELECT cliente_id, COUNT(*) FROM Pedido GROUP BY cliente_id obtiene cantidad de pedidos por cliente. El resultado no incluye automáticamente clientes sin pedidos; para ello se requiere otro diseño con LEFT JOIN.

**Práctica guiada.** Agrupa registros sintéticos por categoría y calcula COUNT y AVG. Compara el resultado con las filas originales.

**Actividad independiente.** Construye un reporte de ventas por mes y categoría, documentando cómo tratar meses sin ventas.

**Criterios de aceptación.** Explica agrupamiento y agrega correctamente sin mezclar granularidades.

**Errores frecuentes.** Seleccionar columnas no agrupadas sin agregación o interpretar el agregado como si fuera una fila original.

**Comprobación.** ¿Qué representa cada fila del resultado después de un GROUP BY?

#### 9.4.16 — HAVING

**Propósito y modelo.** HAVING filtra grupos después de la agregación; WHERE filtra filas antes de agrupar. Las condiciones de HAVING suelen utilizar agregados como COUNT o SUM. La ubicación de cada filtro afecta semántica y rendimiento.

**Ejemplo desarrollado.** GROUP BY cliente_id HAVING COUNT(*) >= 3 devuelve clientes con al menos tres pedidos. Un filtro de fecha que limite pedidos analizados suele pertenecer a WHERE.

**Práctica guiada.** Escribe consulta que agrupe pedidos por cliente, filtre por periodo en WHERE y exija al menos dos pedidos mediante HAVING.

**Actividad independiente.** Explica con datos sintéticos cómo cambia el resultado si una condición de agregado se coloca en WHERE (inválido en SQL estándar) frente a HAVING.

**Criterios de aceptación.** Distingue filtros de filas y grupos y justifica ubicación de condiciones.

**Errores frecuentes.** Usar HAVING para todos los filtros o confundir COUNT de filas con COUNT de valores no nulos.

**Comprobación.** ¿Por qué un filtro de fecha suele aplicarse antes de agrupar y un umbral de COUNT después?

#### 9.4.17 — JOIN

**Propósito y modelo.** JOIN combina filas de tablas relacionadas. INNER JOIN devuelve coincidencias; LEFT JOIN conserva todas las filas izquierdas y rellena con NULL cuando no hay coincidencia; RIGHT/FULL OUTER JOIN dependen de soporte del motor. La condición ON debe representar la relación correcta para evitar multiplicación accidental.

**Ejemplo desarrollado.** Cliente JOIN Pedido ON Cliente.id = Pedido.cliente_id relaciona cada pedido con su cliente. Un LEFT JOIN permite listar clientes sin pedidos.

**Práctica guiada.** Crea dos tablas pequeñas con filas coincidentes y no coincidentes. Ejecuta INNER y LEFT JOIN y explica por qué cambia la cantidad de filas.

**Actividad independiente.** Construye reporte de clientes y total de pedidos, incluyendo clientes sin compras y evitando duplicar importes por relaciones adicionales.

**Criterios de aceptación.** Selecciona tipo de JOIN según resultado requerido y utiliza claves de relación explícitas.

**Errores frecuentes.** Omitir ON y producir producto cartesiano o mover una condición del lado derecho a WHERE y convertir inadvertidamente un LEFT JOIN en INNER.

**Comprobación.** ¿Qué filas conserva LEFT JOIN que INNER JOIN descarta?

#### 9.4.18 — Subqueries

**Propósito y modelo.** Una subconsulta es una consulta anidada utilizada como expresión, fuente de filas o condición. Puede ser escalar, de varias filas, correlacionada o no correlacionada. IN, EXISTS y comparaciones deben elegirse considerando NULL, cardinalidad y optimizador.

**Ejemplo desarrollado.** WHERE EXISTS (SELECT 1 FROM Pedido p WHERE p.cliente_id = c.id) selecciona clientes con al menos un pedido sin duplicar cliente por cada pedido.

**Práctica guiada.** Escribe subconsultas con IN y EXISTS sobre datos sintéticos. Compara resultado y plan de ejecución con JOIN cuando sea equivalente.

**Actividad independiente.** Resuelve una consulta de «elementos por encima del promedio» y otra de «entidades sin relación» usando subconsultas.

**Criterios de aceptación.** Identifica correlación, alcance y cardinalidad; valida equivalencia con datos de prueba.

**Errores frecuentes.** Ignorar NULL en NOT IN o utilizar subconsultas correlacionadas sin revisar costo.

**Comprobación.** ¿Por qué NOT EXISTS puede ser más seguro que NOT IN cuando la subconsulta puede devolver NULL?

#### 9.4.19 — CTE

**Propósito y modelo.** Una Common Table Expression (CTE) define un conjunto nombrado temporal para una sentencia mediante WITH. Mejora legibilidad y permite expresar consultas recursivas en motores compatibles. No implica necesariamente materialización: el optimizador puede integrar o materializar según motor y versión.

**Ejemplo desarrollado.** WITH ventas_mes AS (...) SELECT ... FROM ventas_mes separa una etapa de agregación del reporte final. Una CTE recursiva puede recorrer jerarquías con condición de terminación.

**Práctica guiada.** Reescribe una subconsulta como CTE y compara legibilidad y plan. Si el motor lo soporta, prueba una CTE recursiva con jerarquía sintética pequeña.

**Actividad independiente.** Diseña consulta recursiva para árbol de categorías y controla ciclos o profundidad máxima.

**Criterios de aceptación.** Explica alcance de la CTE, referencia y límites de recursión según DBMS.

**Errores frecuentes.** Asumir que CTE siempre mejora rendimiento o escribir recursión sin condición de parada.

**Comprobación.** ¿Qué ventaja de mantenimiento ofrece una CTE frente a repetir la misma subconsulta varias veces?

### 9.5 — Diseño y normalización

#### 9.5.1 — Primera forma normal (1NF)

**Propósito y modelo.** La primera forma normal exige que cada atributo almacene un valor atómico respecto del dominio definido y que no se representen grupos repetitivos en una misma fila. «Atómico» depende del uso: un nombre completo puede ser texto si no se consulta por partes; si se requiere buscar apellido, conviene separar componentes.

**Ejemplo desarrollado.** Una columna telefonos con valores «111,222,333» dificulta validar, buscar y relacionar cada número. Una tabla TelefonoCliente con una fila por teléfono modela mejor la multiplicidad.

**Práctica guiada.** Revisa una tabla con columnas curso1, curso2, curso3 y otra con lista separada por comas. Propón estructura normalizada y claves.

**Actividad independiente.** Transforma un registro de ventas con productos repetidos en una estructura de tablas que cumpla 1NF.

**Criterios de aceptación.** Identifica grupos repetitivos y propone una representación relacional sin listas embebidas no justificadas.

**Errores frecuentes.** Considerar que cualquier texto compuesto viola 1NF o dividir columnas sin necesidad del dominio.

**Comprobación.** ¿Qué problema de consulta y actualización aparece cuando una fila almacena una lista de valores independientes?

#### 9.5.2 — Segunda forma normal (2NF)

**Propósito y modelo.** La segunda forma normal requiere 1NF y que cada atributo no primo dependa de la clave candidata completa, no solo de una parte de una clave compuesta. Se analiza principalmente cuando una tabla tiene claves compuestas y dependencias funcionales parciales.

**Ejemplo desarrollado.** En DetallePedido(pedido_id, producto_id, nombre_producto, cantidad), la clave puede ser (pedido_id, producto_id), pero nombre_producto depende solo de producto_id. El nombre debe residir en Producto y no repetirse por cada pedido.

**Práctica guiada.** Identifica clave compuesta y dependencias funcionales en una tabla de matrículas con estudiante_id, curso_id, nombre_estudiante y nota.

**Actividad independiente.** Descompón una relación con dependencias parciales y demuestra cómo se reduce redundancia conservando las relaciones.

**Criterios de aceptación.** Explica dependencia parcial y separa atributos que dependen de una parte de la clave compuesta.

**Errores frecuentes.** Aplicar la definición sin identificar primero claves candidatas o dividir tablas sin preservar dependencias y uniones.

**Comprobación.** ¿Por qué un atributo que depende solo de una parte de una clave compuesta viola 2NF?

#### 9.5.3 — Tercera forma normal (3NF)

**Propósito y modelo.** La tercera forma normal requiere 2NF y elimina dependencias transitivas de atributos no clave respecto de claves candidatas, bajo la definición formal de 3NF. En términos prácticos, atributos descriptivos deben depender de la clave, de toda la clave y de nada más que la clave, con matices formales para atributos primos.

**Ejemplo desarrollado.** En Empleado(id, departamento_id, nombre_departamento), nombre_departamento depende de departamento_id y no directamente de id. Separar Departamento evita repetir nombre y anomalías al renombrar.

**Práctica guiada.** Analiza una tabla de empleados con dirección y nombre de departamento. Identifica dependencias transitivas y propone tablas separadas.

**Actividad independiente.** Normaliza un esquema de pedidos hasta 3NF y prueba que las consultas necesarias pueden reconstruirse con joins.

**Criterios de aceptación.** Identifica dependencia transitiva y justifica descomposición sin pérdida.

**Errores frecuentes.** Eliminar toda redundancia sin evaluar rendimiento o confundir cualquier dependencia entre atributos con una violación automática de 3NF.

**Comprobación.** ¿Qué anomalía de actualización puede evitar separar un departamento repetido en muchos registros de empleados?

#### 9.5.4 — BCNF

**Propósito y modelo.** Boyce-Codd Normal Form exige que todo determinante de una dependencia funcional no trivial sea una superclave. Es más estricta que 3NF y puede requerir descomposiciones adicionales. El análisis debe considerar todas las dependencias funcionales reales del dominio, no solo los datos de muestra.

**Ejemplo desarrollado.** En una relación Profesor-Curso-Aula, si cada profesor enseña un curso en un aula y cada curso se imparte en un aula por profesor, pueden existir determinantes que no sean superclaves. El modelo debe formular reglas exactas antes de descomponer.

**Práctica guiada.** Recibe un conjunto sintético de dependencias funcionales, identifica cierres de atributos y determina superclaves candidatas.

**Actividad independiente.** Construye un ejemplo donde 3NF se cumpla pero BCNF no, y muestra la descomposición necesaria y sus posibles pérdidas de preservación de dependencias.

**Criterios de aceptación.** Define determinante, superclave y dependencia no trivial; aplica la condición de BCNF.

**Errores frecuentes.** Declarar BCNF solo observando filas actuales o asumir que toda descomposición conserva automáticamente todas las dependencias.

**Comprobación.** ¿Qué condición adicional impone BCNF respecto a 3NF?

#### 9.5.5 — Redundancia

**Propósito y modelo.** La redundancia es repetición de información. Puede producir anomalías de inserción, actualización y eliminación, y aumentar almacenamiento. No toda duplicación es incorrecta: índices, cachés y desnormalización deliberada pueden mejorar rendimiento si existe estrategia de consistencia.

**Ejemplo desarrollado.** Repetir la dirección de un proveedor en cada pedido puede generar versiones contradictorias al actualizarla. Guardar una instantánea histórica de dirección en la factura puede ser correcto si representa el dato vigente al momento de la transacción.

**Práctica guiada.** Identifica redundancia accidental en un conjunto de tablas y clasifica cada repetición como necesaria, histórica o evitable.

**Actividad independiente.** Diseña un caso donde la desnormalización mejore una consulta y define cómo mantener sincronizada la copia derivada.

**Criterios de aceptación.** Distingue redundancia problemática de duplicación intencional con propósito y control.

**Errores frecuentes.** Eliminar toda duplicación sin considerar historial o duplicar atributos sin definir cuál es la fuente de verdad.

**Comprobación.** ¿Qué diferencia existe entre redundancia accidental y desnormalización controlada?

#### 9.5.6 — Integridad referencial

**Propósito y modelo.** La integridad referencial garantiza que las relaciones entre filas mantengan coherencia mediante claves foráneas y acciones referenciales. Debe decidirse cómo tratar borrado, actualización, registros huérfanos y ciclos. Las reglas deben reflejar retención e historia del negocio.

**Ejemplo desarrollado.** Un detalle de pedido referencia un pedido existente. Si se intenta borrar el pedido con detalles, RESTRICT puede impedirlo; CASCADE elimina dependientes y solo es correcto cuando esa eliminación representa la regla del dominio.

**Práctica guiada.** Diseña casos de inserción de hijo sin padre, borrado de padre con hijos y actualización de clave. Predice el resultado según RESTRICT, CASCADE y SET NULL.

**Actividad independiente.** Define política referencial para cliente, pedido, factura y detalle, protegiendo registros contables históricos.

**Criterios de aceptación.** Explica integridad y selecciona acciones según reglas del negocio.

**Errores frecuentes.** Usar cascadas para simplificar sin evaluar eliminación masiva o desactivar restricciones para cargar datos sin validación posterior.

**Comprobación.** ¿Qué riesgo introduce ON DELETE CASCADE en tablas que representan historial legal o financiero?

#### 9.5.7 — Relaciones uno a uno

**Propósito y modelo.** Una relación 1:1 asocia como máximo una fila de una entidad con una de otra. Puede implementarse con FK UNIQUE, PK compartida o tabla de extensión. Debe existir una razón de dominio para separar entidades, como ciclo de vida, sensibilidad o datos opcionales.

**Ejemplo desarrollado.** Usuario y PerfilPrivado pueden relacionarse 1:1; perfil_privado.usuario_id puede ser FK UNIQUE. La unicidad evita varios perfiles para el mismo usuario, mientras NOT NULL/participación define obligatoriedad.

**Práctica guiada.** Diseña Usuario y CredencialesSeparadas con PK/FK compartida o FK única y analiza inserción, eliminación y opcionalidad.

**Actividad independiente.** Decide si dirección de envío debe ser 1:1 o 1:N con Cliente según historial de pedidos y múltiples direcciones.

**Criterios de aceptación.** Implementa unicidad y explica participación opcional/obligatoria.

**Errores frecuentes.** Crear 1:1 sin justificación o olvidar UNIQUE en la FK, permitiendo una relación 1:N.

**Comprobación.** ¿Qué restricción garantiza que una FK no se repita y por tanto limite la relación a 1:1?

#### 9.5.8 — Uno a muchos

**Propósito y modelo.** En una relación 1:N, una fila del lado uno puede asociarse con muchas filas del lado N; cada fila del lado N referencia como máximo una fila del lado uno mediante FK. La FK se ubica normalmente en la tabla del lado muchos.

**Ejemplo desarrollado.** Un cliente puede tener muchos pedidos; Pedido almacena cliente_id. La FK puede ser NOT NULL si cada pedido debe pertenecer a un cliente.

**Práctica guiada.** Diseña Autor y Libro para un caso donde cada libro tiene un autor principal. Coloca PK/FK y define si la participación es obligatoria.

**Actividad independiente.** Modela Departamento y Empleado, considerando empleados sin departamento y departamentos sin empleados.

**Criterios de aceptación.** Ubica FK en el lado N y explica cardinalidad y opcionalidad.

**Errores frecuentes.** Almacenar una lista de IDs en la fila del lado uno o colocar la FK en el lado incorrecto sin necesidad de una relación inversa.

**Comprobación.** ¿En qué tabla se coloca normalmente la clave foránea en una relación 1:N?

#### 9.5.9 — Muchos a muchos

**Propósito y modelo.** Una relación N:M permite que muchas filas de A se asocien con muchas filas de B. En un modelo relacional se implementa con una tabla asociativa que contiene FKs a ambas entidades y puede incluir atributos de la asociación.

**Ejemplo desarrollado.** Estudiante y Curso se conectan mediante Matrícula(estudiante_id, curso_id, fecha, estado). Una clave compuesta o identificador propio más restricción UNIQUE impide matrículas duplicadas según regla.

**Práctica guiada.** Diseña tablas para Producto y Pedido con DetallePedido como asociación. Añade cantidad y precio_unitario histórico.

**Actividad independiente.** Modela autores y libros cuando un libro puede tener varios autores y un autor varios libros; define orden de autoría como atributo de relación.

**Criterios de aceptación.** Crea tabla puente, FKs y clave única; ubica atributos que pertenecen a la relación.

**Errores frecuentes.** Guardar IDs separados por comas o poner atributos de la relación en una de las entidades sin justificación.

**Comprobación.** ¿Por qué cantidad pertenece a DetallePedido y no a Producto ni a Pedido?

### 9.6 — Bases de datos avanzadas

#### 9.6.1 — Índices

**Propósito y modelo.** Un índice es una estructura auxiliar que permite localizar filas sin recorrer toda la tabla en determinados patrones de consulta. Mejora algunas lecturas, pero consume espacio y añade trabajo a INSERT, UPDATE y DELETE. El optimizador decide si utilizarlo según estadísticas y costo estimado.

**Ejemplo desarrollado.** Un índice sobre email puede acelerar búsquedas de igualdad; si la consulta filtra por estado y fecha, un índice diferente podría ser más apropiado. No existe un índice universal para todas las consultas.

**Práctica guiada.** En una base desechable crea una tabla sintética, consulta su plan con EXPLAIN antes y después de un índice y compara filas estimadas y acceso elegido.

**Actividad independiente.** Propón índices para tres consultas reales hipotéticas y justifica selectividad, tamaño y costo de mantenimiento.

**Criterios de aceptación.** Relaciona índice con patrón de consulta y evalúa costo de escritura/almacenamiento.

**Errores frecuentes.** Indexar todas las columnas o asumir que la presencia de índice garantiza que el optimizador lo utilizará.

**Comprobación.** ¿Por qué un índice puede mejorar SELECT y empeorar una carga con muchas escrituras?

#### 9.6.2 — B-Tree

**Propósito y modelo.** B-Tree y variantes como B+Tree mantienen claves ordenadas y equilibran altura para soportar búsquedas, rangos e inserciones con costo logarítmico aproximado. Muchos DBMS utilizan variantes de árboles balanceados para índices, pero implementación, páginas y detalles dependen del motor.

**Ejemplo desarrollado.** Un índice B-Tree sobre fecha puede apoyar consultas por igualdad y rangos temporales. Una búsqueda por prefijo de columna puede aprovechar el orden; una función aplicada a la columna puede impedir el uso directo del índice si no existe índice funcional adecuado.

**Práctica guiada.** Dibuja un árbol balanceado pequeño y muestra cómo localizar una clave y un rango. Relaciona el recorrido con páginas de índice sin asumir estructura exacta del motor.

**Actividad independiente.** Compara búsqueda por igualdad y por rango en índice B-Tree frente a escaneo secuencial.

**Criterios de aceptación.** Explica orden, balance y utilidad en rangos; reconoce que detalles varían por DBMS.

**Errores frecuentes.** Confundir B-Tree con árbol binario simple o asumir que cualquier condición WHERE utiliza el índice.

**Comprobación.** ¿Por qué un índice ordenado puede acelerar consultas de rango?

#### 9.6.3 — Índices compuestos

**Propósito y modelo.** Un índice compuesto incluye varias columnas y su orden importa. El principio de prefijo izquierdo en muchos índices B-Tree permite aprovechar las columnas iniciales; cambiar el orden puede alterar utilidad y selectividad. Debe diseñarse según filtros, joins y ordenamientos frecuentes.

**Ejemplo desarrollado.** Un índice (cliente_id, fecha) puede apoyar búsquedas por cliente y rangos de fecha para ese cliente; no suele equivaler a un índice separado por fecha para consultas sin cliente_id.

**Práctica guiada.** En una tabla sintética compara EXPLAIN para consultas por primera columna, ambas columnas y solo segunda columna de un índice compuesto.

**Actividad independiente.** Diseña un índice compuesto para historial de pedidos por cliente y fecha, explicando orden y consultas esperadas.

**Criterios de aceptación.** Justifica orden de columnas y valida con plan de ejecución y datos representativos.

**Errores frecuentes.** Elegir orden alfabético de columnas o duplicar índices que comparten prefijos sin medir beneficio.

**Comprobación.** ¿Por qué un índice (A,B) no necesariamente optimiza una consulta que filtra solo por B?

#### 9.6.4 — Vistas

**Propósito y modelo.** Una vista es una consulta almacenada que presenta datos como una relación virtual. Puede simplificar consultas, encapsular joins y limitar columnas expuestas. Una vista ordinaria no necesariamente almacena resultados; vistas materializadas existen en algunos motores y tienen ciclo de actualización distinto.

**Ejemplo desarrollado.** Una vista de reporte puede mostrar pedidos y clientes sin exponer columnas de credenciales. La seguridad efectiva depende de permisos y modo de ejecución definido por el DBMS.

**Práctica guiada.** Crea una vista simple en un esquema desechable, consulta sus resultados y revisa definición. Comprueba qué ocurre al cambiar una tabla subyacente.

**Actividad independiente.** Diseña vistas de lectura para analistas que oculten datos personales y mantengan solo columnas necesarias.

**Criterios de aceptación.** Distingue vista virtual y materializada y explica ventajas y límites de seguridad.

**Errores frecuentes.** Creer que una vista siempre mejora rendimiento o que oculta datos frente a usuarios con privilegios suficientes sobre tablas base.

**Comprobación.** ¿Qué diferencia operativa existe entre una vista normal y una materializada?

#### 9.6.5 — Triggers

**Propósito y modelo.** Un trigger ejecuta lógica asociada a eventos de INSERT, UPDATE o DELETE, antes o después según motor. Puede imponer reglas, auditar o mantener datos derivados, pero introduce efectos secundarios implícitos y dificulta depuración. Debe documentarse y probarse con transacciones.

**Ejemplo desarrollado.** Un trigger de auditoría puede registrar cambios de estado de una orden. Si el trigger falla, la operación original puede fallar según motor y contexto.

**Práctica guiada.** Lee un trigger de ejemplo y determina evento, momento, tabla afectada y datos disponibles. En un entorno desechable crea uno que registre cambios sintéticos.

**Actividad independiente.** Diseña auditoría de cambios sin almacenar contraseñas ni datos sensibles innecesarios; especifica retención y control de acceso.

**Criterios de aceptación.** Explica evento/momento y documenta efectos secundarios y condiciones de fallo.

**Errores frecuentes.** Ocultar lógica de negocio crítica en múltiples triggers o crear recursión y efectos difíciles de rastrear.

**Comprobación.** ¿Qué dificultad de mantenimiento puede generar un trigger que modifica varias tablas sin que la aplicación lo indique?

#### 9.6.6 — Stored Procedures

**Propósito y modelo.** Un procedimiento almacenado es lógica ejecutada en el servidor DBMS, con parámetros, control de flujo y permisos propios. Puede reducir viajes de red y centralizar operaciones, pero aumenta dependencia del motor y requiere versionado, pruebas y revisión de privilegios.

**Ejemplo desarrollado.** Un procedimiento puede registrar una orden y sus detalles en una transacción. Debe validar entradas y manejar errores sin revelar información sensible.

**Práctica guiada.** Lee la definición de un procedimiento sintético y describe parámetros IN/OUT, operaciones, transacción y manejo de errores. Si el motor lo permite, ejecútalo solo en un esquema temporal.

**Actividad independiente.** Diseña una operación de negocio que deba ser atómica y compara implementarla en backend frente a procedimiento almacenado.

**Criterios de aceptación.** Identifica parámetros, permisos, transacción y dependencia del DBMS.

**Errores frecuentes.** Dar privilegios elevados al procedimiento sin necesidad o introducir SQL dinámico inseguro.

**Comprobación.** ¿Qué riesgo introduce construir SQL dinámico concatenando parámetros no confiables?

#### 9.6.7 — Transacciones

**Propósito y modelo.** Una transacción agrupa operaciones para preservar consistencia ante concurrencia y fallos. Sus límites se controlan con BEGIN/START TRANSACTION, COMMIT y ROLLBACK, según motor. La atomicidad requiere soporte del motor de almacenamiento y las operaciones deben mantener invariantes del dominio.

**Ejemplo desarrollado.** Una transferencia debita una cuenta y acredita otra dentro de una transacción. Si una validación o escritura falla, rollback evita confirmar solo una parte.

**Práctica guiada.** En tablas de laboratorio ejecuta dos modificaciones dentro de una transacción, verifica estado intermedio y deshaz. Repite con commit.

**Actividad independiente.** Diseña una transacción de compra que reduzca inventario, cree pedido y registre pago con manejo de errores y compensación cuando un servicio externo no pueda participar.

**Criterios de aceptación.** Identifica límites y estados de transacción y explica qué se confirma o revierte.

**Errores frecuentes.** Mantener transacciones abiertas demasiado tiempo o asumir que una llamada a API externa se revierte con rollback SQL.

**Comprobación.** ¿Por qué una transacción de base de datos no puede deshacer automáticamente un cobro realizado por un proveedor externo?

#### 9.6.8 — ACID

**Propósito y modelo.** ACID resume cuatro propiedades: Atomicidad (todo o nada), Consistencia (preservar invariantes), Aislamiento (controlar efectos concurrentes) y Durabilidad (persistencia tras confirmación). El nivel efectivo depende del motor, configuración, almacenamiento y aislamiento; ACID no elimina errores de lógica.

**Ejemplo desarrollado.** Una transferencia conserva el total de fondos (consistencia) y no deja solo un débito confirmado (atomicidad). Tras COMMIT, la durabilidad depende de configuración y garantías del motor.

**Práctica guiada.** Relaciona cada propiedad con un fallo sintético y describe qué comportamiento esperas del DBMS.

**Actividad independiente.** Evalúa una operación de inventario y explica cómo cada propiedad contribuye a evitar inconsistencias.

**Criterios de aceptación.** Define las cuatro propiedades y aporta ejemplo concreto por cada una.

**Errores frecuentes.** Suponer que ACID garantiza reglas de negocio correctas o que todos los niveles de aislamiento ofrecen el mismo comportamiento.

**Comprobación.** ¿Qué propiedad describe que una transacción confirmada sobreviva a un reinicio conforme a las garantías configuradas?

#### 9.6.9 — Commit

**Propósito y modelo.** COMMIT confirma los cambios de una transacción y los hace visibles conforme al aislamiento y las garantías de durabilidad del motor. Una vez confirmado, no se revierte con ROLLBACK ordinario; la corrección posterior requiere otra transacción o recuperación desde respaldo.

**Ejemplo desarrollado.** Después de validar filas afectadas y restricciones, COMMIT consolida el cambio. Un error posterior de la aplicación no deshace por sí solo el commit.

**Práctica guiada.** En una base desechable actualiza una fila dentro de transacción, verifica el valor y ejecuta COMMIT. Abre una nueva sesión y comprueba persistencia.

**Actividad independiente.** Diseña un flujo de aprobación antes de confirmar una operación financiera, incluyendo conteos, validación y registro de auditoría.

**Criterios de aceptación.** Explica momento de confirmación y diferencia entre error previo y posterior al commit.

**Errores frecuentes.** Confirmar antes de validar resultados o asumir que cerrar la conexión equivale siempre a rollback.

**Comprobación.** ¿Qué opciones quedan después de un COMMIT si se detecta un dato incorrecto?

#### 9.6.10 — Rollback

**Propósito y modelo.** ROLLBACK deshace cambios no confirmados dentro de una transacción, hasta el inicio o un SAVEPOINT según motor. No revierte efectos externos ni necesariamente operaciones con commit implícito. Debe conocerse qué motor y almacenamiento se utilizan.

**Ejemplo desarrollado.** Si una actualización cambia por error varias filas, rollback dentro de la transacción puede restaurar el estado previo antes de confirmar. Si ya hubo COMMIT, se necesita una operación compensatoria o restauración.

**Práctica guiada.** Ejecuta un UPDATE sintético, consulta cambios en la sesión y aplica ROLLBACK; verifica con SELECT que se restauró el valor.

**Actividad independiente.** Redacta procedimiento para abortar una carga de datos que detecta más filas afectadas de las esperadas.

**Criterios de aceptación.** Identifica alcance de rollback y diferencia cambios transaccionales de efectos externos/commit implícito.

**Errores frecuentes.** Esperar que rollback revierta un correo enviado, una API llamada o un DDL con commit implícito.

**Comprobación.** ¿Por qué un rollback SQL no puede deshacer un archivo ya enviado a un sistema externo?

#### 9.6.11 — Locks

**Propósito y modelo.** Los locks coordinan acceso concurrente a recursos y protegen operaciones frente a conflictos. Pueden ser de fila, página, tabla, predicado o estructuras internas según motor. El alcance y granularidad influyen en concurrencia; bloquear más de lo necesario reduce rendimiento.

**Ejemplo desarrollado.** Una transacción puede bloquear una fila de inventario mientras comprueba y actualiza unidades disponibles. Otra transacción que requiere el mismo recurso puede esperar o recibir conflicto según timeout y aislamiento.

**Práctica guiada.** Dibuja dos transacciones que acceden a la misma fila y marca cuándo se adquiere y libera el bloqueo. En una instancia de laboratorio observa locks con vistas disponibles, sin bloquear sistemas compartidos.

**Actividad independiente.** Diseña una operación de reserva de inventario que evite vender unidades inexistentes y limite duración de locks.

**Criterios de aceptación.** Explica bloqueo, espera y alcance; relaciona duración de transacción con contención.

**Errores frecuentes.** Mantener transacciones abiertas durante interacción de usuario o asumir que todos los motores bloquean filas de la misma manera.

**Comprobación.** ¿Qué efecto puede producir una transacción larga sobre otras sesiones que necesitan las mismas filas?

#### 9.6.12 — Deadlocks

**Propósito y modelo.** Un deadlock ocurre cuando transacciones esperan recursos retenidos por otras y forman un ciclo de espera. El DBMS suele detectar el ciclo y abortar una transacción víctima, pero el criterio depende del motor. La aplicación debe manejar el error y reintentar de forma segura cuando corresponda.

**Ejemplo desarrollado.** T1 bloquea fila A y solicita B; T2 bloquea B y solicita A. Ninguna puede continuar hasta que el motor resuelva el ciclo.

**Práctica guiada.** Representa dos transacciones con orden de acceso inverso y dibuja el grafo de espera. No provoques deadlocks en una base compartida.

**Actividad independiente.** Propón estrategia para reducir deadlocks: orden consistente de acceso, transacciones breves, índices adecuados y reintentos limitados con backoff.

**Criterios de aceptación.** Identifica ciclo de espera y diferencia deadlock de bloqueo prolongado o timeout.

**Errores frecuentes.** Reintentar infinitamente sin límite o capturar el error y continuar como si la transacción siguiera activa.

**Comprobación.** ¿Por qué acceder a recursos en un orden consistente puede reducir deadlocks?

#### 9.6.13 — Isolation Levels

**Propósito y modelo.** Los niveles de aislamiento regulan anomalías de lectura/escritura concurrente. READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE son niveles habituales, pero comportamientos exactos, MVCC y anomalías permitidas dependen del DBMS. No se debe inferir equivalencia solo por el nombre del nivel.

**Ejemplo desarrollado.** Una lectura no repetible ocurre cuando una fila leída cambia y se vuelve a leer dentro de la misma transacción. Una lectura fantasma implica que una consulta por predicado devuelve nuevas filas tras una inserción concurrente.

**Práctica guiada.** Analiza dos sesiones hipotéticas con lecturas y escrituras intercaladas. Identifica dirty read, non-repeatable read y phantom read según nivel descrito.

**Actividad independiente.** Selecciona nivel de aislamiento para reporte, inventario y transferencia de saldo; explica consistencia, concurrencia y costo.

**Criterios de aceptación.** Define anomalías y relaciona nivel con comportamiento del motor documentado.

**Errores frecuentes.** Suponer que SERIALIZABLE siempre se implementa igual o subir aislamiento sin evaluar bloqueos y rendimiento.

**Comprobación.** ¿Qué anomalía evita impedir que una transacción vea cambios no confirmados de otra?

#### 9.6.14 — Optimización

**Propósito y modelo.** Optimizar consultas implica medir, comprender planes, revisar índices, cardinalidad, estadísticas, selectividad, volumen y patrón de acceso. No consiste en añadir índices indiscriminadamente ni reescribir SQL por intuición. Debe utilizarse datos representativos y comparar antes/después.

**Ejemplo desarrollado.** Un filtro sobre columna indexada puede seguir provocando escaneo completo si devuelve gran parte de la tabla o la estadística no favorece el índice. Una consulta con N+1 desde la aplicación puede ser más costosa que una consulta SQL individual.

**Práctica guiada.** Ejecuta una consulta en un esquema de laboratorio, registra plan y tiempo con dataset fijo, cambia una variable a la vez y vuelve a medir.

**Actividad independiente.** Prepara un informe de optimización con consulta, volumen, plan, índice propuesto, costo de escritura y evidencia comparativa.

**Criterios de aceptación.** Formula hipótesis medible y demuestra efecto con plan y datos representativos.

**Errores frecuentes.** Medir una sola vez, optimizar sin conocer el objetivo o comparar datasets y cachés distintos.

**Comprobación.** ¿Por qué un plan de ejecución es más informativo que afirmar que una consulta «parece lenta»?

#### 9.6.15 — EXPLAIN

**Propósito y modelo.** EXPLAIN muestra el plan estimado de ejecución de una consulta: acceso a tablas, índices posibles/elegidos, orden de joins, cardinalidad estimada y operaciones. Algunos motores ofrecen EXPLAIN ANALYZE para ejecutar y medir el plan real; debe utilizarse con cautela si la consulta tiene efectos o alto costo.

**Ejemplo desarrollado.** Un plan puede mostrar full table scan, index lookup, nested loop o sort. Un escaneo completo no es automáticamente malo: puede ser eficiente cuando se requiere gran parte de la tabla.

**Práctica guiada.** Ejecuta EXPLAIN sobre consultas SELECT en una base sintética. Compara plan antes/después de un índice y anota filas estimadas y método de acceso.

**Actividad independiente.** Analiza un plan de join con tablas pequeñas y señala dónde se concentra el costo estimado; propone una prueba para validar hipótesis.

**Criterios de aceptación.** Interpreta operador, acceso e índices y diferencia plan estimado de ejecución medida.

**Errores frecuentes.** Asumir que usar índice siempre es mejor o ejecutar EXPLAIN ANALYZE sobre operaciones destructivas sin control.

**Comprobación.** ¿Qué diferencia existe entre EXPLAIN y EXPLAIN ANALYZE en los motores que ofrecen ambas opciones?

### 9.7 — PostgreSQL

#### 9.7.1 — Arquitectura

**Propósito y modelo.** PostgreSQL utiliza una arquitectura cliente-servidor. El proceso servidor administra una instancia, acepta conexiones mediante procesos backend y coordina memoria compartida, WAL, checkpoints, autovacuum y almacenamiento. La arquitectura exacta evoluciona entre versiones y debe consultarse en documentación oficial.

**Ejemplo desarrollado.** Una conexión cliente crea o utiliza un proceso backend; las transacciones generan cambios que se registran en WAL antes de persistirse según garantías de durabilidad. Checkpoints y recuperación permiten reconstruir estado tras fallos.

**Práctica guiada.** Consulta versión con `SELECT version();`, parámetros no sensibles y vistas de actividad en una instancia de laboratorio. Distingue proceso cliente, backend y servicio principal.

**Actividad independiente.** Dibuja arquitectura de PostgreSQL con clientes, backend, memoria, WAL, archivos de datos y mecanismos de mantenimiento.

**Criterios de aceptación.** Identifica componentes y describe flujo de conexión y recuperación sin confundir memoria compartida con almacenamiento persistente.

**Errores frecuentes.** Confundir cluster de PostgreSQL con una base de datos o asumir que cada conexión es un hilo dentro de un único proceso.

**Comprobación.** ¿Qué función cumple WAL en la recuperación y durabilidad?

#### 9.7.2 — Roles

**Propósito y modelo.** PostgreSQL utiliza roles para representar usuarios, grupos y capacidades. Un rol puede iniciar sesión (LOGIN), heredar privilegios, crear bases o roles según atributos concedidos. Los privilegios sobre objetos se administran aparte de atributos de rol; crear un rol no implica acceso automático a todas las tablas.

**Ejemplo desarrollado.** Un rol de aplicación con LOGIN recibe CONNECT sobre una base y SELECT/INSERT sobre tablas necesarias, sin CREATEDB ni SUPERUSER. Los roles de grupo permiten asignar privilegios por función.

**Práctica guiada.** Consulta `\du` en psql o catálogos equivalentes de una instancia de laboratorio. Identifica LOGIN, atributos administrativos y membresías sin mostrar secretos.

**Actividad independiente.** Diseña roles para migración, aplicación y lectura de reportes con herencia controlada y mínimo privilegio.

**Criterios de aceptación.** Diferencia rol, usuario tradicional y privilegios sobre objetos; justifica atributos y membresías.

**Errores frecuentes.** Conceder SUPERUSER a la aplicación o asumir que ser miembro de un rol concede automáticamente todos los privilegios sin revisar INHERIT/SET ROLE.

**Comprobación.** ¿Por qué separar el rol de despliegue del rol de ejecución de la aplicación?

#### 9.7.3 — Esquemas

**Propósito y modelo.** En PostgreSQL un esquema es un espacio de nombres dentro de una base de datos que contiene tablas, vistas, funciones y otros objetos. Los privilegios USAGE y CREATE controlan acceso al esquema, mientras los permisos de objeto controlan operaciones sobre tablas y funciones. search_path afecta resolución de nombres y debe configurarse con cuidado.

**Ejemplo desarrollado.** Una consulta a tabla sin calificar puede resolverse mediante search_path. Si un usuario puede crear objetos en un esquema que aparece antes que uno confiable, puede producir riesgos de resolución de nombres.

**Práctica guiada.** Consulta `SHOW search_path;` y lista esquemas con psql. Identifica el esquema actual y practica nombres calificados como `ventas.pedido`.

**Actividad independiente.** Diseña esquemas para ventas, inventario y auditoría con permisos separados y search_path explícito.

**Criterios de aceptación.** Diferencia base y esquema y explica USAGE, CREATE y resolución de nombres.

**Errores frecuentes.** Confiar en search_path implícito o conceder CREATE en esquemas compartidos a roles no confiables.

**Comprobación.** ¿Qué riesgo puede producir un search_path que incluya un esquema donde un usuario no confiable puede crear objetos?

#### 9.7.4 — Tipos de datos

**Propósito y modelo.** PostgreSQL ofrece tipos escalares, temporales, numéricos, UUID, arrays, rangos, JSON/JSONB y tipos definidos por usuario. La elección debe responder a semántica, validación, índices y portabilidad. TIMESTAMP WITH TIME ZONE normaliza instantes; no conserva literalmente la zona original ingresada.

**Ejemplo desarrollado.** NUMERIC ofrece precisión decimal exacta; JSONB almacena datos JSON en representación binaria optimizada para procesamiento; UUID puede servir como identificador distribuido.

**Práctica guiada.** Diseña tabla Evento con id UUID, instante timestamptz, monto numeric y metadatos jsonb. Consulta tipos y valores de ejemplo sin datos personales.

**Actividad independiente.** Compara JSONB con columnas relacionales para atributos que requieren filtros frecuentes y restricciones.

**Criterios de aceptación.** Justifica tipo según dominio y explica al menos dos particularidades de PostgreSQL.

**Errores frecuentes.** Guardar todos los datos en JSONB sin modelar campos críticos o asumir que timestamptz almacena la zona horaria original.

**Comprobación.** ¿Qué diferencia práctica existe entre JSON y JSONB en PostgreSQL?

#### 9.7.5 — JSONB

**Propósito y modelo.** JSONB almacena documentos JSON en formato binario descompuesto, lo que permite operaciones e índices especializados. No conserva necesariamente formato textual, orden de claves ni espacios originales. Debe combinarse con restricciones y diseño relacional cuando ciertos atributos requieren integridad fuerte.

**Ejemplo desarrollado.** Una columna metadata JSONB puede contener atributos variables; consultas con operadores de existencia o extracción pueden aprovechar índices GIN apropiados. El diseño del índice depende de operadores y patrón de consulta.

**Práctica guiada.** En una instancia desechable inserta documentos JSONB sintéticos y consulta claves con operadores ->, ->> y ?. Compara resultado textual y valor JSON.

**Actividad independiente.** Diseña un modelo híbrido con columnas relacionales para campos obligatorios y JSONB para atributos variables; define validaciones y consultas frecuentes.

**Criterios de aceptación.** Diferencia JSON y JSONB, interpreta operadores y justifica cuándo utilizar estructura relacional.

**Errores frecuentes.** Tratar JSONB como sustituto universal de normalización o crear GIN sin conocer consultas.

**Comprobación.** ¿Qué costo de integridad puede aparecer si se almacenan campos críticos exclusivamente dentro de JSONB?

#### 9.7.6 — Índices

**Propósito y modelo.** PostgreSQL soporta varios tipos de índices, como B-tree, Hash, GiST, SP-GiST, GIN y BRIN. Cada uno se adapta a operadores y estructuras diferentes. Los índices aumentan espacio y costo de escritura; el planificador decide su uso según estadísticas, selectividad y costo.

**Ejemplo desarrollado.** B-tree suele ser apropiado para igualdad y rangos; GIN puede apoyar búsquedas en JSONB o arrays; BRIN puede ser útil para tablas grandes cuyos datos correlacionan con orden físico. No son intercambiables.

**Práctica guiada.** En una tabla de laboratorio crea un índice B-tree y consulta EXPLAIN. Si se dispone de JSONB, compara una consulta con GIN. Mide sin extrapolar resultados de tablas pequeñas.

**Actividad independiente.** Selecciona tipo de índice para tres patrones y justifica operadores, cardinalidad, tamaño y mantenimiento.

**Criterios de aceptación.** Relaciona tipo de índice con consulta y valida con plan de ejecución.

**Errores frecuentes.** Asumir que GIN siempre mejora JSONB o crear índices redundantes sin medir.

**Comprobación.** ¿Por qué un índice BRIN puede resultar útil cuando los datos están físicamente correlacionados con una columna?

#### 9.7.7 — Transacciones

**Propósito y modelo.** PostgreSQL implementa transacciones con MVCC, snapshots y niveles de aislamiento. Las lecturas pueden observar versiones consistentes sin bloquear todas las escrituras, pero existen conflictos y bloqueos. SERIALIZABLE utiliza detección de dependencias y puede abortar transacciones que deben reintentarse.

**Ejemplo desarrollado.** Dos transacciones actualizan filas distintas y pueden continuar concurrentemente; si compiten por la misma fila, una espera o encuentra conflicto. En SERIALIZABLE una operación puede abortarse para preservar equivalencia serial.

**Práctica guiada.** En una instancia local abre dos sesiones y analiza lecturas bajo READ COMMITTED y REPEATABLE READ usando datos sintéticos. No ejecutes experimentos de bloqueo en producción.

**Actividad independiente.** Diseña una operación de reserva y define aislamiento, reintento y tratamiento de errores de serialización.

**Criterios de aceptación.** Explica MVCC y diferencias de aislamiento de PostgreSQL sin generalizar a otros motores.

**Errores frecuentes.** Suponer que MVCC elimina todos los bloqueos o ignorar que una transacción SERIALIZABLE puede abortarse.

**Comprobación.** ¿Por qué una aplicación debe estar preparada para reintentar una transacción abortada por serialización?

#### 9.7.8 — Consultas avanzadas

**Propósito y modelo.** Las consultas avanzadas en PostgreSQL pueden utilizar CTE, ventanas, agregaciones FILTER, funciones, JSONB, arrays y operadores específicos. La sintaxis debe ajustarse a la versión y el planificador debe evaluarse con EXPLAIN/ANALYZE en datos representativos.

**Ejemplo desarrollado.** Una función de ventana como ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY fecha DESC) permite numerar pedidos por cliente sin colapsar filas como GROUP BY.

**Práctica guiada.** Construye una consulta con CTE y función de ventana sobre datos sintéticos. Identifica partición, orden y número de fila.

**Actividad independiente.** Diseña un reporte de último pedido por cliente y otro de ranking de ventas por categoría; compara ventana y subconsulta.

**Criterios de aceptación.** Explica OVER, PARTITION BY y ORDER BY de ventana; valida resultados con datos límite.

**Errores frecuentes.** Confundir función de ventana con agregado que reduce filas o usar orden no determinista en ranking con empates.

**Comprobación.** ¿Qué diferencia existe entre GROUP BY y una función de ventana?

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
