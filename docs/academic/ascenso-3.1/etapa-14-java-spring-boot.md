# Etapa 14 — Backend I: Java y Spring Boot

**Prioridad:** Especialización principal  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** construir servicios backend profesionales utilizando Java.  
**Proyecto oficial:** API REST empresarial para administrar usuarios, productos, inventario, ventas y permisos.

## Propósito y prerrequisitos
Esta etapa consolida Java, POO, estructuras de datos, SQL, HTTP y diseño de APIs. El backend recibe solicitudes, aplica reglas de negocio, coordina persistencia y devuelve respuestas. La meta no es acumular anotaciones de Spring, sino diseñar un servicio mantenible, seguro, comprobable y observable.

## Resultados de aprendizaje
- Diseñar una arquitectura backend por responsabilidades.
- Comprender IoC, DI, beans y el contenedor de Spring.
- Construir APIs REST con Spring Boot, DTOs y validación.
- Persistir datos relacionales mediante JPA/Hibernate y migraciones.
- Aplicar autenticación, autorización y gestión segura de credenciales.
- Implementar transacciones, caché, paginación, eventos y operaciones asíncronas.
- Gestionar dependencias y builds con Maven o Gradle.

## 14.1 — Arquitectura backend
En una arquitectura cliente-servidor, el backend recibe solicitudes y responde mediante un contrato. MVC separa responsabilidades de interacción, modelo y presentación; en una API, el controller suele adaptar HTTP al caso de uso. Una separación común es:

- **Controller:** interpreta ruta, parámetros, headers y cuerpo; delega el caso de uso y traduce resultado a respuesta HTTP.
- **Service / caso de uso:** coordina reglas de negocio y transacciones.
- **Repository:** abstrae acceso a persistencia.
- **Model / Entity:** representa conceptos persistidos cuando corresponde.
- **DTO:** contrato de entrada/salida; evita exponer entidades internas.

Middleware y filtros procesan solicitudes en puntos transversales. No conviertas controllers en depósitos de reglas de negocio ni repositories en servicios de dominio. La dirección de dependencias debe favorecer reglas centrales y contratos explícitos.

**Ejercicio:** dibuja la secuencia POST /products desde HTTP hasta la base de datos y de vuelta. Identifica validación, autorización, transacción y errores.

## 14.2 — Spring Framework
### Inversion of Control y Dependency Injection
IoC invierte quién controla la creación y conexión de objetos. Spring administra un contenedor de objetos llamados beans. Dependency Injection entrega a un componente las dependencias que necesita, en vez de construirlas manualmente dentro de él.

Prefiere inyección por constructor: hace visibles las dependencias, facilita pruebas y permite declarar campos final. Evita ciclos de dependencias; resuélvelos revisando responsabilidades, no ocultándolos con inyección tardía.

### Beans, ApplicationContext y configuración
Un bean es un objeto administrado por Spring. ApplicationContext ofrece el contenedor y servicios asociados. Comprende configuración Java, component scanning, perfiles y propiedades. Usa configuración externa para valores por entorno; nunca incluyas secretos en el repositorio. Evita crear beans innecesarios o depender de escaneo implícito sin entender el paquete base.

**Laboratorio:** construye dos implementaciones de una interfaz de notificación y selecciona una mediante configuración. Prueba el servicio sin levantar el servidor HTTP.

## 14.3 — Spring Boot
Spring Boot reduce configuración inicial mediante auto-configuración y convenciones. Spring Initializr permite generar un proyecto con dependencias declaradas. Revisa cada starter añadido: no agregues dependencias que no comprendas.

Organiza paquetes por funcionalidad o capas de forma consistente. Construye controllers, services y repositories; define DTOs de solicitud/respuesta; valida entradas con Jakarta Bean Validation; gestiona excepciones de manera centralizada mediante mecanismos de Spring MVC; y externaliza configuración mediante ConfigurationProperties.

Una API debe definir códigos HTTP, formato de error, paginación, validación y compatibilidad. No devuelvas entidades JPA directamente. Evita mensajes internos, stack traces y datos sensibles en respuestas.

**Laboratorio:** crea CRUD de productos con DTOs, validación, paginación y un manejador de errores consistente. Prueba 201, 400, 404 y conflicto de negocio.

## 14.4 — Persistencia
ORM mapea objetos a tablas, pero no elimina la necesidad de comprender SQL, índices, transacciones ni planes de ejecución. JPA define APIs y contratos de persistencia; Hibernate es una implementación/proveedor común. Spring Data JPA simplifica repositorios, pero no convierte consultas costosas en eficientes automáticamente.

Estudia entidades, identidad, estados, relaciones uno-a-uno/uno-a-muchos/muchos-a-muchos, carga lazy/eager, cascadas y ciclo de vida. Evita exponer asociaciones bidireccionales directamente en JSON; puede provocar ciclos o consultas inesperadas. Usa DTOs y consultas explícitas.

Las migraciones versionan cambios del esquema. Mantén migraciones reproducibles y compatibles con despliegues; no dependas de crear tablas automáticamente en producción. MySQL y PostgreSQL tienen diferencias de tipos, funciones, índices y administración: verifica el motor real.

**Laboratorio:** modela productos, ventas y líneas de venta; crea migraciones; persiste una venta completa dentro de una transacción; comprueba integridad ante fallo intermedio.

## 14.5 — Seguridad
Spring Security proporciona infraestructura para autenticación, autorización y protección de solicitudes. Autenticación responde quién es la identidad; autorización decide qué puede hacer sobre un recurso. Cada endpoint y operación de dominio debe comprobar permisos, no solo ocultar botones.

Password hashing debe utilizar algoritmos adaptativos diseñados para contraseñas y parámetros actualizados; nunca cifrado reversible ni hash rápido generalista. Usa el encoder mantenido por el framework y evita implementar criptografía propia.

JWT exige validar firma, algoritmo permitido, issuer, audience, expiración y claims requeridos. No confundas firma con cifrado. Los roles son agrupaciones amplias; los permisos pueden expresar acciones específicas. Aplica mínimo privilegio y autorización por objeto.

OAuth 2.0 es un marco de autorización delegada; OpenID Connect añade una capa de identidad sobre OAuth 2.0. Selecciona flujos apropiados al tipo de cliente y utiliza bibliotecas mantenidas. Protege secretos, cookies, sesiones, refresh tokens, CSRF y CORS según el modelo de despliegue.

**Laboratorio:** configura usuarios de prueba, roles y permisos. Demuestra que un usuario sin permiso no puede leer ni modificar el recurso de otro, incluso llamando directamente a la API.

## 14.6 — Backend avanzado
- **Transactions:** define límites transaccionales alrededor de una unidad coherente de negocio; entiende rollback, aislamiento y efectos secundarios.
- **Caching:** define clave, TTL, invalidación y consistencia; no caches datos privados bajo claves compartidas.
- **Pagination/filtering:** valida límites y campos ordenables; usa orden determinista y cursores cuando sean adecuados.
- **Async/events:** distingue procesamiento asíncrono de una respuesta inmediata. Diseña idempotencia, reintentos y manejo de fallos.
- **WebSockets:** requiere autorización durante la conexión y por operación/mensaje.
- **File upload:** limita tamaño, valida tipo y contenido, genera nombres seguros, almacena fuera de rutas ejecutables y controla acceso.
- **Email:** maneja colas, reintentos, plantillas y datos personales; no registres contenido sensible innecesariamente.
- **Queues:** comprende entrega al menos una vez, duplicados, dead-letter queues y consumidores idempotentes.

**Laboratorio:** implementa exportación asíncrona de inventario con estado consultable, cola local o mecanismo equivalente y control de acceso al archivo generado.

## 14.7 — Construcción y dependencias
Maven y Gradle administran dependencias, tareas y builds. Comprende coordenadas, repositorios, scopes/configurations, plugins, lifecycle y perfiles. El archivo de dependencias debe permitir builds reproducibles. Revisa dependencias transitivas, licencias, vulnerabilidades y compatibilidad con la versión de Java y Spring Boot seleccionada.

No declares una versión por intuición: el proyecto debe fijar una línea compatible y documentar JDK, framework, plugin y runtime. Evita versiones dinámicas en builds de entrega. Mantén configuración de desarrollo, pruebas y producción separada sin duplicar secretos.

**Laboratorio:** construye el mismo proyecto con el gestor elegido, ejecuta pruebas y build limpio desde checkout nuevo y documenta comandos.

## Proyecto oficial — API REST empresarial
Construye una API para usuarios, productos, inventario, ventas y permisos.

### Requisitos funcionales
1. CRUD de productos y consulta paginada.
2. Registro/administración de usuarios según política definida.
3. Autenticación y autorización por roles y permisos.
4. Registro de ventas con líneas, validación y transacción atómica.
5. Actualización de inventario con protección frente a concurrencia.
6. Historial de movimientos de inventario.
7. Manejo uniforme de errores y validaciones.
8. Migraciones versionadas y datos de prueba no sensibles.
9. Documentación OpenAPI coherente con endpoints reales.
10. Pruebas unitarias, integración y API.
11. Configuración por entorno sin secretos versionados.
12. Logs estructurados sin credenciales ni datos personales innecesarios.

### Entregables
Diagrama de arquitectura; modelo ER; decisiones de diseño; repositorio; migraciones; colección HTTP/OpenAPI; pruebas; matriz de roles/permisos; instrucciones de ejecución; informe de amenazas y limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Arquitectura y separación de responsabilidades | 15 |
| Spring Framework y Spring Boot | 15 |
| Persistencia y transacciones | 15 |
| API, DTOs y validación | 15 |
| Seguridad y autorización por objeto | 20 |
| Operaciones avanzadas | 10 |
| Build, pruebas y documentación | 10 |

Aprobación orientativa: 80/100 y ningún fallo crítico de autorización, exposición de secretos o inconsistencia transaccional.

## Autoevaluación
1. ¿Qué problema resuelve IoC?
2. ¿Por qué se recomienda inyección por constructor?
3. ¿Qué diferencia existe entre Entity y DTO?
4. ¿Qué responsabilidades pertenecen al service y cuáles al controller?
5. ¿Qué diferencia existe entre JPA, Hibernate y Spring Data JPA?
6. ¿Por qué las migraciones son necesarias?
7. ¿Qué diferencia existe entre autenticación y autorización?
8. ¿Qué valida un consumidor de JWT?
9. ¿Qué riesgos aparecen al procesar archivos?
10. ¿Por qué un consumidor de cola debe ser idempotente?

## Recursos audiovisuales
No se incluyen videos aprobados. Para aprobar recursos se comprobarán idioma hablado en español y correspondencia directa con cada bloque (IoC/DI, Spring Boot REST, JPA, Spring Security, transacciones). No se asignará un curso genérico a toda la etapa.

## Referencias oficiales
- Spring Framework Reference: https://docs.spring.io/spring-framework/reference/
- Spring Boot Reference: https://docs.spring.io/spring-boot/reference/
- Spring Security Reference: https://docs.spring.io/spring-security/reference/
- Spring Data JPA: https://docs.spring.io/spring-data/jpa/reference/
- Jakarta Persistence: https://jakarta.ee/specifications/persistence/
- Hibernate ORM: https://hibernate.org/orm/documentation/
- Maven: https://maven.apache.org/guides/
- Gradle: https://docs.gradle.org/current/userguide/userguide.html
- Java Documentation: https://docs.oracle.com/en/java/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ha generado ni ejecutado una API en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 14

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados organizan el estudio de los conceptos y los relacionan con la guía técnica y el proyecto de la etapa; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 14.1 — Arquitectura backend

#### 14.1.01 — Cliente-servidor
El modelo cliente-servidor separa consumidores y proveedores de capacidades mediante solicitudes y respuestas. En backend identifica límites de confianza, responsabilidades de cada proceso y cómo se autentican las llamadas entre componentes.


**Escenario aplicado.** Una aplicación de comercio separa el frontend que solicita el estado del pedido y el backend que aplica reglas de acceso y consulta datos. El navegador no debe conectarse directamente a la base de datos.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué responsabilidades y límites de confianza deben quedar entre cliente, API y persistencia?

**Práctica y evidencia:** Dibuja el intercambio entre cliente HTTP, controlador y servidor de aplicación para una consulta de pedido. **Evidencia:** identifica límites de red y responsabilidad de cada componente.

#### 14.1.02 — Request-response
Request-response describe el intercambio de una solicitud con una respuesta que contiene estado, headers y representación. Define contratos, timeouts, códigos de error e idempotencia para que clientes puedan recuperarse de fallos y reintentos.


**Escenario aplicado.** Un cliente pierde la conexión después de enviar una solicitud. El backend debe definir timeout, estado de operación y posibilidad segura de reintento para no duplicar una compra.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué información necesita el cliente para distinguir una operación fallida de una respuesta perdida?

**Práctica y evidencia:** Traza una petición con método, ruta, cabeceras y respuesta con estado y cuerpo. **Evidencia:** registra un caso exitoso y uno fallido y explica cómo el cliente interpreta ambos.

#### 14.1.03 — MVC
MVC separa modelo, vista y controlador, aunque en una API el controlador suele coordinar entrada/salida sin renderizar vistas. Evita introducir lógica de negocio en controladores y mantén el modelo de dominio independiente del transporte.


**Escenario aplicado.** En una API MVC, el controlador interpreta la entrada y coordina la respuesta; la lógica de negocio permanece en el modelo/servicio y no en la capa de transporte.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué problemas aparecen si se concentran reglas de negocio en los controladores?

**Práctica y evidencia:** Separa una pantalla, controlador y modelo de dominio en un ejemplo MVC. **Evidencia:** explica qué componente recibe interacción y cuál contiene reglas del negocio.

#### 14.1.04 — Middleware
Middleware intercepta solicitudes o respuestas para aplicar funciones transversales como autenticación, logging, CORS o correlación. El orden de ejecución importa; limita los datos registrados y evita que middleware genérico oculte errores o modifique contratos sin documentarlo.


**Escenario aplicado.** Un filtro de correlación añade un identificador a cada solicitud y un manejador de errores transforma excepciones en respuestas uniformes. El middleware no registra credenciales.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Por qué el orden de filtros y middleware puede cambiar la autenticación y el manejo de errores?

**Práctica y evidencia:** Implementa o analiza un middleware/filtro que registre correlación sin registrar credenciales. **Evidencia:** muestra orden de ejecución y cómo se propaga la solicitud.

#### 14.1.05 — Controllers
Un controller recibe solicitudes, interpreta parámetros y delega el caso de uso a servicios. Valida formato y devuelve respuestas HTTP coherentes, pero no debe concentrar reglas de negocio, consultas complejas ni acceso directo a infraestructura.


**Escenario aplicado.** Un controller recibe un DTO, valida el formato y delega el caso de uso. No consulta directamente repositorios ni decide reglas de negocio complejas.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué responsabilidad debe conservar el controller y cuál debe delegar?

**Práctica y evidencia:** Crea un controlador REST que delegue la lógica de negocio y no acceda directamente a infraestructura. **Evidencia:** prueba rutas y códigos HTTP con un cliente de API.

#### 14.1.06 — Services
Un service implementa casos de uso y coordina reglas de negocio. Mantén sus dependencias explícitas y separa la lógica del framework para facilitar pruebas unitarias y cambios de transporte.


**Escenario aplicado.** Un servicio de pedidos verifica disponibilidad y calcula el total antes de solicitar persistencia. Puede probarse sin levantar un servidor HTTP si sus dependencias están abstraídas.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué hace que una regla de negocio sea comprobable sin depender de HTTP?

**Práctica y evidencia:** Implementa un servicio con una regla de negocio y pruebas unitarias aisladas. **Evidencia:** demuestra que la regla no depende de HTTP ni de la base de datos.

#### 14.1.07 — Repositories
Un repository abstrae operaciones de persistencia y consultas sobre agregados o entidades. Define métodos con intención de dominio y evita exponer detalles de SQL/ORM a capas que no deberían conocerlos.


**Escenario aplicado.** Un repositorio ofrece métodos de dominio para consultar pedidos y evita que el controlador conozca SQL o detalles de Hibernate. Las consultas complejas se inspeccionan y miden.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué ventaja aporta el repositorio y qué riesgo existe si oculta consultas costosas?

**Práctica y evidencia:** Define un repositorio para persistencia y separa consultas de reglas de negocio. **Evidencia:** prueba el contrato con datos de prueba y explica límites de la abstracción.

#### 14.1.08 — Models
Un model representa datos y, según la arquitectura, puede representar entidades de dominio o modelos de transporte/persistencia. No mezcles automáticamente entidad JPA, DTO público y modelo de vista: sus ciclos de vida y contratos son distintos.


**Escenario aplicado.** Una entidad persistente contiene relaciones y metadatos internos, mientras un modelo de dominio puede expresar invariantes y un DTO define el contrato externo. No se intercambian automáticamente.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Por qué entidad, modelo de dominio y DTO pueden requerir clases diferentes?

**Práctica y evidencia:** Modela una entidad de dominio con invariantes y distingue modelo de dominio de DTO. **Evidencia:** prueba una transición válida y otra que debe rechazarse.

#### 14.1.09 — DTOs
Un DTO transporta datos entre límites de una aplicación o API sin exponer necesariamente la estructura interna del dominio. Define campos permitidos, valida entrada y evita serializar entidades completas que puedan revelar relaciones o atributos privados.


**Escenario aplicado.** El DTO de creación acepta nombre y dirección, pero no permite que el cliente defina id, rol administrativo ni marcas de auditoría. La respuesta expone solo los campos autorizados.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Cómo reduce un DTO el riesgo de asignación masiva y exposición de datos?

**Práctica y evidencia:** Define DTOs distintos para entrada y salida y evita exponer entidades internas. **Evidencia:** demuestra validación de campos y que la respuesta omite atributos sensibles.

### Módulo 14.2 — Spring Framework

#### 14.2.01 — Inversion of Control
Inversion of Control desplaza la creación y coordinación de dependencias desde las clases hacia un contenedor o mecanismo externo. Esto reduce acoplamiento, pero introduce ciclo de vida y configuración que deben ser explícitos y verificables.


**Escenario aplicado.** La aplicación deja de construir dependencias concretas dentro de cada clase y delega su ciclo de vida al contenedor. Esto facilita reemplazar implementaciones en pruebas.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué acoplamiento se reduce con IoC y qué complejidad introduce el contenedor?

**Práctica y evidencia:** Compara creación manual de dependencias con un contenedor IoC. **Evidencia:** dibuja quién controla el ciclo de vida y qué problema reduce la inversión de control.

#### 14.2.02 — Dependency Injection
Dependency Injection entrega a un componente las dependencias que necesita, en lugar de construirlas directamente. Prefiere inyección por constructor para hacer requisitos visibles y facilitar pruebas con implementaciones sustitutas.


**Escenario aplicado.** Un controlador recibe un servicio por constructor. En pruebas, una implementación sustituta simula el servicio sin acceder a base de datos ni red.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Por qué la inyección por constructor hace más visibles las dependencias?

**Práctica y evidencia:** Inyecta una interfaz de servicio en un controlador mediante constructor. **Evidencia:** sustituye la implementación por un doble de prueba sin modificar el consumidor.

#### 14.2.03 — Beans
Un Bean es un objeto administrado por el contenedor Spring, que controla su creación, configuración y ciclo de vida. Declara componentes con intención y evita convertir cada clase en Bean si no requiere gestión del framework.


**Escenario aplicado.** Un Bean singleton con estado mutable compartido puede provocar condiciones de carrera entre solicitudes concurrentes. Los servicios stateless suelen ser más sencillos de gestionar.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué precaución requiere un Bean singleton cuando atiende múltiples solicitudes?

**Práctica y evidencia:** Declara un Bean con configuración explícita y consulta su tipo en el contexto. **Evidencia:** explica alcance y ciclo de vida configurado.

#### 14.2.04 — Application Context
ApplicationContext es el contenedor central de Spring que registra beans, resuelve dependencias y publica eventos. Comprende cómo se construye y consulta, pero evita usarlo como localizador global de servicios porque oculta dependencias.


**Escenario aplicado.** El ApplicationContext detecta beans ambiguos cuando varias implementaciones satisfacen el mismo tipo. La aplicación debe resolver la selección mediante configuración explícita, qualifier o primary.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Por qué usar el contenedor como localizador global puede ocultar dependencias?

**Práctica y evidencia:** Inspecciona el ApplicationContext y localiza un bean por nombre o tipo en una prueba. **Evidencia:** identifica cómo se resuelven dependencias y qué ocurre ante ambigüedad.

#### 14.2.05 — Configuration
La configuración define cómo se construye y comporta una aplicación, mediante propiedades, clases de configuración y perfiles. Separa configuración por entorno, valida valores requeridos y no almacenes secretos en archivos versionados.


**Escenario aplicado.** La URL de base de datos cambia por entorno y el secreto se inyecta desde un gestor seguro. Los valores requeridos se validan al arrancar para fallar pronto ante configuración incompleta.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué configuración puede versionarse y qué información debe mantenerse fuera del repositorio?

**Práctica y evidencia:** Externaliza parámetros no secretos en configuración y separa secretos por mecanismo de entorno seguro. **Evidencia:** demuestra valores por perfil sin incluir credenciales en el repositorio.

#### 14.2.06 — Component Scanning
Component Scanning detecta clases anotadas en paquetes configurados y las registra como componentes. Mantén paquetes raíz coherentes y evita escaneos demasiado amplios que incorporen accidentalmente implementaciones o configuraciones ajenas.


**Escenario aplicado.** Un componente no aparece porque su paquete está fuera del alcance del escaneo. Ajustar el paquete raíz o declarar configuración explícita corrige el problema sin ampliar indiscriminadamente el escaneo.

**Criterio de análisis.** La explicación debe identificar responsabilidades, dependencias y consecuencias observables, no limitarse a repetir definiciones. **Pregunta de comprensión:** ¿Qué riesgos introduce un component scan demasiado amplio?

**Práctica y evidencia:** Configura escaneo de componentes y observa qué paquetes quedan incluidos. **Evidencia:** diagnostica un bean no detectado y justifica la estructura de paquetes.

### Módulo 14.3 — Spring Boot

#### 14.3.01 — Spring Initializr
Spring Initializr genera una estructura de proyecto y selecciona dependencias iniciales compatibles. Elige versión de Spring Boot, Java y build tool de acuerdo con la matriz oficial; registra esas versiones para que el proyecto sea reproducible.


**Escenario aplicado.** El proyecto se genera con una versión de Spring Boot compatible con la versión de Java elegida. Se registra el wrapper y las dependencias exactas para que el build no dependa de herramientas globales del equipo.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué información hace reproducible la generación y compilación del proyecto?

**Práctica y evidencia:** Genera un proyecto con Spring Initializr seleccionando versión compatible, Java y dependencias mínimas. **Evidencia:** registra coordenadas, versión y motivo de cada dependencia.

#### 14.3.02 — Estructura del proyecto
La estructura del proyecto separa código de aplicación, configuración, recursos y pruebas. Organiza paquetes por funcionalidad o capas de forma consistente y conserva convenciones que permitan localizar controladores, servicios, repositorios y DTOs.


**Escenario aplicado.** La estructura separa controladores, casos de uso, persistencia y configuración. Los paquetes se organizan por dominio cuando esto reduce dependencias cruzadas y facilita cambios.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué señal indica que una estructura por capas está generando acoplamiento circular?

**Práctica y evidencia:** Organiza paquetes por capas o funcionalidad y documenta la convención elegida. **Evidencia:** demuestra que controladores, servicios y persistencia no se acoplan circularmente.

#### 14.3.03 — Controllers
Los controllers de Spring Boot se exponen mediante anotaciones de mapeo como `@RestController` y `@RequestMapping`. Define rutas y métodos explícitos, usa DTOs y delega el procesamiento a servicios en lugar de incluir reglas de negocio en handlers.


**Escenario aplicado.** Un controlador REST recibe un DTO y devuelve 201 con Location al crear un recurso. No devuelve entidades JPA ni acepta propiedades internas no autorizadas.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué debe validar el controlador antes de delegar y qué debe delegar al servicio?

**Práctica y evidencia:** Implementa un controlador con endpoints de lectura y escritura y respuestas HTTP coherentes. **Evidencia:** prueba rutas, parámetros y códigos.

#### 14.3.04 — Services
Los services concentran casos de uso y reglas de aplicación. Mantén operaciones transaccionales en el límite adecuado y evita que el servicio dependa innecesariamente de detalles HTTP o de serialización.


**Escenario aplicado.** El servicio coordina creación de pedido y reserva de inventario dentro de una unidad de trabajo adecuada. La regla puede probarse sin arrancar el contexto web completo.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Dónde debe residir la regla de negocio y cómo se prueba de forma aislada?

**Práctica y evidencia:** Implementa reglas de negocio en un servicio y define límites transaccionales. **Evidencia:** prueba una regla sin levantar el servidor web.

#### 14.3.05 — Repositories
Los repositories de Spring Data proporcionan abstracciones para consultas y persistencia. Selecciona interfaces y métodos derivados con cuidado, inspecciona consultas generadas cuando sean complejas y evita cargar grandes conjuntos sin paginación.


**Escenario aplicado.** Un endpoint de búsqueda devuelve resultados paginados y ordenados. El repositorio evita recuperar toda la tabla y se prueba el caso sin coincidencias.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué problema de rendimiento aparece al devolver todas las filas de una tabla creciente?

**Práctica y evidencia:** Crea un repositorio de Spring Data y utiliza consultas derivadas o declaradas con criterios explícitos. **Evidencia:** prueba paginación y comportamiento con registros inexistentes.

#### 14.3.06 — REST
Una API REST en Spring Boot expone recursos mediante rutas, métodos HTTP y representaciones. Usa status codes correctos, valida entradas, documenta errores y considera idempotencia, paginación y compatibilidad del contrato.


**Escenario aplicado.** GET consulta, POST crea, PUT reemplaza y PATCH modifica parcialmente según el contrato. El cliente recibe códigos coherentes y no se confunde idempotencia con autorización.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Por qué el método HTTP debe reflejar la semántica de la operación?

**Práctica y evidencia:** Diseña recursos REST y métodos HTTP idempotentes según la operación. **Evidencia:** prueba GET, POST, PUT/PATCH y DELETE y justifica códigos de respuesta.

#### 14.3.07 — DTOs
Los DTOs separan la representación externa del modelo interno. Diseña solicitudes y respuestas distintas cuando sus reglas difieran, evita exponer campos de auditoría o credenciales y controla la conversión entre DTO y dominio.


**Escenario aplicado.** El DTO de respuesta omite campos internos y mantiene un contrato estable aunque cambie la entidad. Las conversiones se prueban para evitar exponer información accidentalmente.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué riesgo existe al serializar directamente entidades de persistencia?

**Práctica y evidencia:** Mapea request/response a DTOs y evita devolver entidades JPA directamente. **Evidencia:** demuestra que cambios internos del modelo no alteran accidentalmente el contrato API.

#### 14.3.08 — Validation
Validation aplica restricciones declarativas a datos de entrada, por ejemplo obligatoriedad, longitud, formato y rangos. Valida en el límite de entrada y devuelve errores estructurados; la validación de DTO no sustituye reglas de negocio ni controles de base de datos.


**Escenario aplicado.** Una entrada con correo mal formado o cantidad negativa se rechaza antes de ejecutar el caso de uso. La validación de negocio vuelve a comprobar invariantes que dependen del estado actual.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué diferencia existe entre validación sintáctica de DTO e invariantes del dominio?

**Práctica y evidencia:** Aplica validación declarativa a un DTO y traduce errores en respuestas comprensibles. **Evidencia:** prueba límites, campos obligatorios y tipos inválidos.

#### 14.3.09 — Exception Handling
Exception Handling centraliza la traducción de excepciones a respuestas HTTP mediante mecanismos como `@ControllerAdvice`. Devuelve mensajes seguros y códigos estables, registra detalles internos en logs protegidos y no expongas stack traces al cliente.


**Escenario aplicado.** El manejador global devuelve un código y un identificador de correlación, mientras el detalle técnico permanece en logs protegidos. No se revela stack trace ni SQL al consumidor.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Cómo se puede facilitar soporte sin exponer detalles internos al cliente?

**Práctica y evidencia:** Centraliza excepciones con un manejador y define un esquema estable de error. **Evidencia:** comprueba que los errores no filtran stack traces ni información interna.

#### 14.3.10 — Configuration Properties
Configuration Properties vincula configuración externa tipada con clases de la aplicación. Valida rangos y valores requeridos, separa perfiles y secretos, y evita dispersar lecturas de variables de entorno por toda la lógica de negocio.


**Escenario aplicado.** Un perfil define URL y parámetros no secretos; el secreto se obtiene desde un almacén externo. La aplicación falla al iniciar si una propiedad obligatoria está ausente o mal formada.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Por qué conviene validar configuración al iniciar y no cuando llega la primera solicitud?

**Práctica y evidencia:** Vincula propiedades tipadas desde configuración y valida valores obligatorios al iniciar. **Evidencia:** prueba arranque correcto e incorrecto sin revelar secretos.

### Módulo 14.4 — Persistencia

#### 14.4.01 — Spring Data JPA
Spring Data JPA facilita el acceso a persistencia relacional mediante repositorios y entidades JPA. Comprende el ciclo de vida del contexto de persistencia, transacciones y carga diferida; no asumas que una llamada al repositorio siempre equivale a una consulta simple.


**Escenario aplicado.** Un repositorio guarda una entidad y la transacción delimita la operación. La prueba usa una base de datos aislada y verifica commit o rollback según el resultado.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué parte de la operación debe quedar dentro de una transacción y por qué?

**Práctica y evidencia:** Mapea una entidad y ejecuta operaciones CRUD mediante Spring Data JPA. **Evidencia:** muestra persistencia y consulta en una base de prueba.

#### 14.4.02 — Hibernate
Hibernate es una implementación ORM que mapea objetos Java a estructuras relacionales y administra persistencia. Revisa SQL generado, estrategias de fetching y cachés; abstraer SQL no elimina la necesidad de comprender índices, joins y transacciones.


**Escenario aplicado.** Una relación lazy se accede después de cerrar el contexto de persistencia y genera error. El diseño debe cargar explícitamente lo necesario para el caso de uso.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué problema puede causar una estrategia de fetching no considerada?

**Práctica y evidencia:** Inspecciona SQL generado por Hibernate para una consulta y una relación. **Evidencia:** explica carga lazy/eager y detecta un posible problema N+1.

#### 14.4.03 — ORM
ORM relaciona clases/objetos con tablas/filas y gestiona conversiones y relaciones. Es útil para productividad, pero puede ocultar consultas costosas o diferencias de modelo; utiliza SQL explícito cuando la consulta o el rendimiento lo justifique.


**Escenario aplicado.** Un ORM reduce código repetitivo, pero una consulta con joins y filtros puede requerir SQL específico. La decisión se basa en medición, claridad y mantenimiento.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Cuándo puede ser razonable abandonar una abstracción ORM para una consulta concreta?

**Práctica y evidencia:** Compara ORM con JDBC directo mediante una operación sencilla. **Evidencia:** identifica productividad, control SQL y costes de abstracción.

#### 14.4.04 — Entities
Una Entity representa una entidad persistente con identidad y ciclo de vida administrado por JPA. Define clave primaria, campos y reglas de igualdad cuidadosamente; evita exponer entidades directamente como respuesta pública de una API.


**Escenario aplicado.** Una entidad usa identificador estable y restricciones coherentes con la base. La igualdad no se basa ingenuamente en campos mutables que cambian durante el ciclo de vida.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué problema produce definir igualdad de entidades usando atributos mutables?

**Práctica y evidencia:** Define una entidad con identificador, columnas y restricciones coherentes con el esquema. **Evidencia:** verifica mapping y comportamiento de persistencia.

#### 14.4.05 — Relationships
Las relaciones JPA (`OneToOne`, `OneToMany`, `ManyToOne`, `ManyToMany`) modelan asociaciones y sus lados propietarios. Define cascadas, carga y restricciones según el dominio; una relación bidireccional mal gestionada puede generar ciclos JSON y consultas inesperadas.


**Escenario aplicado.** Una relación ManyToMany puede ocultar atributos propios de la asociación. Si la relación requiere fecha, estado o cantidad, conviene modelar una entidad intermedia explícita.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Cuándo debe una relación muchos-a-muchos convertirse en una entidad propia?

**Práctica y evidencia:** Modela relaciones OneToOne, OneToMany y ManyToMany con lado propietario claro. **Evidencia:** prueba persistencia y carga evitando ciclos infinitos al serializar.

#### 14.4.06 — Repositories
Los repositories encapsulan consultas de entidades y operaciones CRUD. Usa paginación, proyecciones y consultas específicas cuando sea necesario; evita métodos que devuelvan todas las filas si el conjunto puede crecer.


**Escenario aplicado.** Un repositorio usa paginación y proyección para devolver solo los campos necesarios. Las consultas derivadas se revisan cuando los nombres del método se vuelven difíciles de mantener.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué ventaja aporta una proyección frente a cargar una entidad completa?

**Práctica y evidencia:** Define métodos de repositorio y limita consultas a necesidades del caso de uso. **Evidencia:** comprueba consulta generada y resultado con datos de prueba.

#### 14.4.07 — Migrations
Las migrations versionan cambios de esquema para aplicarlos de forma repetible entre entornos. Usa herramientas como Flyway o Liquibase, revisa scripts antes de producción y diseña cambios compatibles con despliegues graduales y rollback realista.


**Escenario aplicado.** Una migración añade una columna nullable antes de que el código nuevo dependa de ella. El despliegue gradual evita exigir simultáneamente una versión de aplicación y un esquema incompatibles.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Por qué una migración debe planearse junto con el ciclo de despliegue?

**Práctica y evidencia:** Crea una migración versionada con Flyway o Liquibase para añadir una columna o índice. **Evidencia:** aplica migración en una base limpia y registra checksum/versión.

#### 14.4.08 — MySQL
MySQL es un DBMS relacional con tipos, índices, transacciones y dialecto SQL propios. Verifica versión, motor de almacenamiento, aislamiento y configuración; no asumas que todas las características de PostgreSQL o SQL estándar se comportan igual.


**Escenario aplicado.** El perfil MySQL utiliza un motor transaccional y configuración de charset/collation explícita. El proyecto prueba índices, restricciones y comportamiento real de consultas en la versión declarada.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Qué aspectos deben verificarse además de que la conexión JDBC funcione?

**Práctica y evidencia:** Configura una base MySQL de prueba con usuario de privilegios mínimos y conexión segura. **Evidencia:** verifica conexión, esquema y migraciones sin usar root para la aplicación.

#### 14.4.09 — PostgreSQL
PostgreSQL ofrece un motor relacional con tipos y capacidades avanzadas, extensibilidad e integridad transaccional. Diseña migraciones y consultas para la versión elegida y utiliza planes de ejecución para comprender costes reales.


**Escenario aplicado.** El perfil PostgreSQL usa tipos y restricciones propios del motor. Las pruebas no asumen que una consulta o tipo específico de MySQL se comporta igual en PostgreSQL.

**Criterio de análisis.** La respuesta debe identificar la decisión técnica, el comportamiento esperado y una prueba que permita comprobarlo. **Pregunta de comprensión:** ¿Por qué cambiar el motor puede exigir revisar SQL, tipos y migraciones?

**Práctica y evidencia:** Configura PostgreSQL para el perfil de integración y compara tipos o funciones utilizadas. **Evidencia:** ejecuta pruebas contra el motor real en vez de asumir compatibilidad SQL total.

### Módulo 14.5 — Seguridad

#### 14.5.01 — Spring Security
Spring Security integra filtros y mecanismos de seguridad para solicitudes y recursos de la aplicación. Configura explícitamente qué rutas son públicas, autenticadas o restringidas y mantén una política de denegación por defecto.


**Escenario aplicado.** La configuración de seguridad debe proteger endpoints por defecto y permitir explícitamente rutas públicas necesarias. Los filtros se ordenan y prueban para evitar rutas que omiten autenticación.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué riesgo introduce una regla de autorización permisiva por defecto?

**Práctica y evidencia:** Configura una cadena de filtros de Spring Security y protege una ruta de laboratorio. **Evidencia:** compara acceso anónimo y autenticado y documenta la política.

#### 14.5.02 — Authentication
Authentication verifica la identidad de quien accede, por ejemplo mediante credenciales, sesión o token. Define el mecanismo, protege el proceso de recuperación y evita confundir autenticación correcta con permiso para ejecutar cualquier operación.


**Escenario aplicado.** La autenticación verifica credenciales y establece una identidad; el servidor limita intentos y evita mensajes que permitan enumerar usuarios. El flujo de sesión se prueba también ante expiración y cierre.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia existe entre validar credenciales y autorizar una acción?

**Práctica y evidencia:** Implementa autenticación de usuario con proveedor seguro y verificación de credenciales. **Evidencia:** demuestra rechazo de credenciales inválidas y respuesta que no revela si la cuenta existe.

#### 14.5.03 — Authorization
Authorization decide si una identidad autenticada puede realizar una acción sobre un recurso. Aplica controles por recurso y operación, valida propiedad cuando corresponda y no confíes en roles globales si el acceso depende del contexto del dato.


**Escenario aplicado.** Un usuario autenticado intenta leer un recurso de otro propietario. La autorización comprueba permisos sobre ese objeto, no solo la presencia de una sesión válida.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué un rol general no siempre basta para autorizar acceso a un recurso concreto?

**Práctica y evidencia:** Protege una operación según identidad y permiso requerido, no solo por estar autenticado. **Evidencia:** prueba usuario autenticado sin permiso y usuario autorizado.

#### 14.5.04 — Password Hashing
Password Hashing almacena verificadores derivados de contraseñas con algoritmos adaptativos como Argon2id, bcrypt o PBKDF2 según política vigente. Usa salt único y parámetros adecuados; nunca cifres reversiblemente ni guardes contraseñas en texto claro.


**Escenario aplicado.** Las contraseñas se almacenan mediante funciones adaptativas de hashing con salt y parámetros adecuados. Nunca se guardan en texto claro ni se cifran de forma reversible para comparar inicios de sesión.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué una función hash rápida general no es la opción adecuada para contraseñas?

**Práctica y evidencia:** Configura un algoritmo de hash de contraseñas adaptativo y verifica contraseñas mediante el encoder. **Evidencia:** comprueba que no se almacena texto claro ni hash reversible.

#### 14.5.05 — JWT
JWT puede transportar claims firmados para verificar integridad y atributos del sujeto. Valida firma, algoritmo permitido, emisor, audiencia, expiración y revocación según diseño; el payload firmado no es secreto por defecto.


**Escenario aplicado.** El servidor valida firma, algoritmo permitido, emisor, audiencia y expiración del JWT. El cliente no confía en claims decodificados localmente para conceder permisos.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué controles deben verificarse antes de aceptar un JWT?

**Práctica y evidencia:** Valida JWT comprobando firma, emisor, audiencia, expiración y algoritmo permitido. **Evidencia:** demuestra rechazo de token manipulado y explica que el payload no está cifrado por defecto.

#### 14.5.06 — Roles
Roles agrupan permisos y simplifican asignación de capacidades. Define roles por responsabilidad y evita roles omnipotentes; revisa altas, bajas y cambios para que los privilegios no permanezcan después de cambiar la función del usuario.


**Escenario aplicado.** Los roles agrupan permisos de alto nivel y se asignan según función. Un usuario puede pertenecer a varios roles, por lo que las reglas de combinación y precedencia deben ser explícitas.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué problema aparece si los roles se asignan por conveniencia y no por responsabilidad?

**Práctica y evidencia:** Asigna roles con alcance claro y evita usar un rol genérico de administrador para todas las acciones. **Evidencia:** prueba matriz de acceso por rol.

#### 14.5.07 — Permissions
Permissions representan acciones concretas autorizadas sobre recursos. Aplica mínimo privilegio y verifica permisos en cada operación sensible, incluyendo endpoints secundarios y descargas; la interfaz cliente solo mejora experiencia, no impone seguridad.


**Escenario aplicado.** Un permiso como order:read se verifica en el servidor para cada operación. La interfaz puede ocultar botones, pero la API debe impedir la acción no autorizada independientemente del cliente.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué ocultar un botón no constituye control de autorización?

**Práctica y evidencia:** Modela permisos específicos y separa rol de permiso cuando el dominio lo requiera. **Evidencia:** demuestra autorización de una acción concreta y auditoría de denegación.

#### 14.5.08 — OAuth2
OAuth 2.0 es un marco de autorización delegada para que un cliente obtenga acceso limitado a recursos. Selecciona el flujo apropiado, utiliza PKCE cuando corresponde y no trates OAuth por sí solo como un protocolo de autenticación.


**Escenario aplicado.** OAuth2 delega autorización mediante scopes y flujos apropiados al tipo de cliente. Un backend confidencial y una SPA pública no deben utilizar el mismo supuesto de almacenamiento de secretos.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué un cliente público no puede proteger un client secret?

**Práctica y evidencia:** Configura OAuth 2.0 como flujo de autorización para un cliente de prueba y protege redirect URIs. **Evidencia:** distingue access token, refresh token, scopes y rol del authorization server.

#### 14.5.09 — OpenID Connect
OpenID Connect añade una capa de identidad sobre OAuth 2.0 y define ID Tokens y descubrimiento. Valida issuer, audience, nonce y firma; diferencia ID Token de access token y no utilices uno como sustituto del otro.


**Escenario aplicado.** OpenID Connect añade una capa de identidad sobre OAuth2 y utiliza ID tokens con propósito distinto al access token. El backend valida issuer, audience, nonce y firma según el flujo.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia funcional existe entre ID token y access token?

**Práctica y evidencia:** Integra OpenID Connect para autenticación y valida issuer, audience, nonce y claims requeridos. **Evidencia:** explica diferencia entre identidad (ID token) y autorización a API (access token).

### Módulo 14.6 — Backend avanzado

#### 14.6.01 — Transactions
Transactions agrupa operaciones para que se apliquen según propiedades transaccionales y límites definidos. Identifica el caso de uso que requiere atomicidad y evita transacciones largas que mantengan locks mientras se espera red o intervención humana.


**Escenario aplicado.** La actualización de inventario y la creación de pedido deben confirmar juntas o revertirse según el límite transaccional. Las llamadas externas no se incluyen ingenuamente dentro de una transacción larga.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué anomalía puede ocurrir si parte de una operación de negocio confirma y otra falla?

**Práctica y evidencia:** Delimita una transacción en el servicio que actualiza pedido e inventario y prueba rollback ante fallo. **Evidencia:** demuestra atomicidad y explica propagación de excepciones.

#### 14.6.02 — Caching
Caching conserva resultados para reducir latencia o carga, pero introduce invalidación y riesgo de datos obsoletos. Define clave, TTL, alcance y estrategia de invalidación; no caches respuestas sensibles compartidas entre usuarios.


**Escenario aplicado.** Una caché acelera lecturas, pero puede devolver datos obsoletos o cruzar usuarios si la clave no incluye el contexto correcto. Define TTL e invalidación como parte del contrato.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué riesgo existe al cachear respuestas personalizadas con una clave insuficiente?

**Práctica y evidencia:** Añade caché a una lectura de referencia y define expiración e invalidación al actualizar. **Evidencia:** mide hit/miss y demuestra que no se sirve dato obsoleto indefinidamente.

#### 14.6.03 — Pagination
Pagination divide resultados en bloques para limitar memoria, transferencia y tiempo de respuesta. Ofrece tamaño máximo, orden estable y metadatos de continuación; cursor pagination puede ser más robusta que offsets para conjuntos cambiantes.


**Escenario aplicado.** La API limita tamaño de página y define orden estable. Para colecciones grandes evalúa cursores y evita exponer consultas sin límites.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué el tamaño máximo de página protege rendimiento y disponibilidad?

**Práctica y evidencia:** Expone paginación con límites máximos y orden estable. **Evidencia:** prueba primera/última página y evita consultas sin límite.

#### 14.6.04 — Filtering
Filtering permite restringir resultados mediante campos y operadores permitidos. Valida y parametriza filtros, controla consultas costosas y no traduzcas directamente expresiones arbitrarias del cliente a SQL o JPQL.


**Escenario aplicado.** Los filtros aceptan una lista permitida de campos y operadores. Se parametrizan valores y se limitan combinaciones que provoquen consultas costosas.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué diferencia hay entre validar un valor y permitir que el cliente defina libremente la consulta?

**Práctica y evidencia:** Valida filtros permitidos y tradúcelos a criterios de repositorio. **Evidencia:** demuestra rechazo de campos desconocidos y consulta parametrizada.

#### 14.6.05 — Async
Async permite ejecutar tareas fuera del hilo que atiende la solicitud o devolver resultados diferidos. Define executor, límites de cola, manejo de excepciones y propagación de contexto; asincronía sin límites puede agotar recursos.


**Escenario aplicado.** Una tarea asíncrona se ejecuta fuera del hilo de solicitud y necesita control de errores, propagación de contexto y límites de concurrencia. No se debe asumir que comparte automáticamente la transacción del llamador.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué ocurre con el contexto transaccional cuando una tarea se ejecuta en otro hilo?

**Práctica y evidencia:** Ejecuta una tarea asíncrona con executor configurado y maneja fallos. **Evidencia:** explica contexto de seguridad/transacción y evita asumir que se propaga automáticamente.

#### 14.6.06 — Events
Events desacopla productores y consumidores mediante publicación de hechos o mensajes. Distingue eventos de dominio y de integración, define esquema/versionado y considera duplicados, orden y entrega al menos una vez.


**Escenario aplicado.** Un evento de dominio comunica que ocurrió un hecho relevante. Los consumidores pueden recibirlo más de una vez, por lo que los efectos deben diseñarse con idempotencia y trazabilidad.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué un consumidor de eventos debe tolerar duplicados?

**Práctica y evidencia:** Publica un evento de dominio tras una operación y define cuándo se procesa. **Evidencia:** distingue evento interno de integración y considera consistencia con la transacción.

#### 14.6.07 — WebSockets
WebSockets mantiene una conexión bidireccional para intercambios en tiempo real. Autentica durante el establecimiento, autoriza cada canal/mensaje y define límites, reconexión y heartbeat; no asumas que el canal es confiable por ser persistente.


**Escenario aplicado.** Un WebSocket autenticado sigue necesitando autorización por mensaje, límites de tamaño y cierre controlado. La conexión persistente no debe convertirse en un canal ilimitado de operaciones.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué controles deben repetirse después de establecer la conexión?

**Práctica y evidencia:** Implementa un canal WebSocket de laboratorio con autenticación y autorización por destino. **Evidencia:** prueba conexión no autorizada y cierre controlado.

#### 14.6.08 — File Upload
File Upload recibe archivos y debe controlar tamaño, extensión, tipo real, nombre y almacenamiento. Renombra de forma segura, analiza contenido cuando corresponda, almacena fuera de rutas ejecutables y aplica autorización al descargar.


**Escenario aplicado.** La carga de archivos valida tamaño, extensión, tipo real, nombre y autorización; almacena fuera del webroot o en almacenamiento aislado y analiza contenido según riesgo.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué confiar solo en la extensión del archivo es insuficiente?

**Práctica y evidencia:** Recibe un archivo con límite de tamaño, tipo permitido y nombre seguro; almacénalo fuera del directorio ejecutable. **Evidencia:** prueba archivo excesivo y nombre malicioso.

#### 14.6.09 — Email
Email integra notificaciones transaccionales y mensajes de sistema. Usa plantillas seguras, controla rebotes y reintentos, no envíes secretos en enlaces sin protección y evita bloquear una solicitud de usuario esperando un proveedor externo.


**Escenario aplicado.** El envío de correo se delega a un componente y gestiona fallos/reintentos sin bloquear solicitudes críticas. Los logs registran identificadores, no contenido sensible del mensaje.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué datos no deberían aparecer en logs de envío de correo?

**Práctica y evidencia:** Configura envío de correo mediante proveedor de prueba y gestiona reintentos sin duplicar notificaciones. **Evidencia:** registra estado y evita almacenar credenciales SMTP en código.

#### 14.6.10 — Queues
Queues desacopla productores y trabajadores para procesar tareas de forma asíncrona. Diseña consumidores idempotentes, reintentos con backoff, dead-letter queues y observabilidad; una cola no garantiza orden global ni entrega exactamente una vez.


**Escenario aplicado.** Una cola desacopla productores y consumidores, pero exige política de reintento, dead-letter, idempotencia y observabilidad. El orden y la entrega dependen de la tecnología elegida.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué una cola no garantiza por sí sola que cada mensaje se procese exactamente una vez?

**Práctica y evidencia:** Publica y consume un mensaje mediante una cola de laboratorio, con manejo de reintentos y mensajes fallidos. **Evidencia:** explica entrega al menos una vez y necesidad de consumidor idempotente.

### Módulo 14.7 — Construcción y dependencias

#### 14.7.01 — Maven
Maven describe el proyecto y sus dependencias en `pom.xml`, y ejecuta fases del ciclo de build mediante plugins. Fija versiones, comprende scopes y evita depender de artefactos no reproducibles o repositorios no confiables.


**Escenario aplicado.** Maven administra dependencias y ciclo de build mediante POM y plugins. El wrapper fija la versión del build tool y los repositorios se revisan para evitar dependencias de procedencia dudosa.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué ventaja aporta el Maven Wrapper en un equipo?

**Práctica y evidencia:** Define dependencias y plugins en Maven y ejecuta el ciclo de build en el proyecto. **Evidencia:** explica fases relevantes y conserva `pom.xml` y wrapper.

#### 14.7.02 — Gradle
Gradle configura builds mediante scripts y tareas, con soporte para dependencias y plugins. Distingue Groovy DSL y Kotlin DSL, fija versiones del wrapper y revisa plugins porque ejecutan código durante el proceso de construcción.


**Escenario aplicado.** Gradle usa scripts de build y puede aprovechar configuración incremental. Las versiones del wrapper y plugins deben fijarse para que el resultado no cambie por actualizaciones globales.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué debe versionarse para reproducir el build Gradle?

**Práctica y evidencia:** Configura Gradle con tareas y dependencias reproducibles. **Evidencia:** ejecuta build mediante wrapper y explica diferencia entre configuración y ejecución.

#### 14.7.03 — Dependencies
Dependencies son bibliotecas externas necesarias para compilar o ejecutar la aplicación. Declara solo lo requerido, revisa licencias y vulnerabilidades, fija versiones y utiliza análisis de composición para detectar dependencias transitivas de riesgo.


**Escenario aplicado.** Una dependencia transitiva puede introducir vulnerabilidades o licencias incompatibles. El equipo inspecciona árbol, versiones, procedencia y política de actualización antes de incorporarla.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Por qué revisar solo dependencias declaradas directamente es insuficiente?

**Práctica y evidencia:** Añade una dependencia y revisa versión, alcance, transitivas y vulnerabilidades conocidas. **Evidencia:** documenta motivo y evita versiones flotantes sin control.

#### 14.7.04 — Build Lifecycle
Build Lifecycle organiza fases como validación, compilación, pruebas, empaquetado y verificación. Define qué tareas son obligatorias en CI y evita marcar como exitoso un build que omite pruebas o controles de calidad.


**Escenario aplicado.** El ciclo de build compila, prueba, empaqueta y verifica artefactos. Una compilación exitosa no sustituye pruebas ni análisis de seguridad y debe conservarse evidencia del resultado.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué evidencia adicional se requiere además de que el build termine sin errores?

**Práctica y evidencia:** Relaciona compilación, pruebas, empaquetado y verificación con el ciclo de build. **Evidencia:** muestra qué fase falla ante un test fallido y qué artefacto se genera.

#### 14.7.05 — Profiles
Profiles permiten variar configuración o tareas para entornos y necesidades específicas. Evita que perfiles de producción desactiven seguridad o pruebas; externaliza secretos y comprueba explícitamente qué perfil está activo al construir y desplegar.



**Escenario aplicado.** Los perfiles separan parámetros de entorno, pero no deben almacenar secretos. La configuración efectiva se inspecciona y valida para evitar activar por error el perfil de producción en desarrollo.

**Criterio de análisis.** La respuesta debe especificar amenaza o fallo, control propuesto y evidencia verificable. **Pregunta de comprensión:** ¿Qué controles evitan que un perfil incorrecto cambie el comportamiento del despliegue?

**Práctica y evidencia:** Crea perfiles de configuración para local, prueba y producción sin duplicar secretos. **Evidencia:** demuestra qué propiedades cambian por perfil y valida que producción falla de forma segura si falta una variable.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 58 orientaciones genéricas por explicaciones específicas para cada lección. Se desarrollaron límites arquitectónicos, IoC/DI, capas backend, Spring Boot REST, JPA/Hibernate, migraciones, autenticación/autorización, OAuth2/OIDC, JWT, transacciones, caché, mensajería, cargas de archivos y build/dependencias.

**Revisión interna:** 58/58 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron seguridad de contraseñas, validación de DTOs, errores HTTP, secretos de configuración, permisos por recurso, control de archivos y consumidores idempotentes. Pendiente: fijar versiones compatibles de Java/Spring, compilar, ejecutar pruebas, migraciones, integración de seguridad y despliegue en entorno aislado. No se declara ejecución ni aprobación externa.
