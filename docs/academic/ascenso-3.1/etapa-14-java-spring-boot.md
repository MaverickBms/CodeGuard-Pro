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
