# Etapa 15 — Backend II: Node.js y NestJS

**Prioridad:** Especialización complementaria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** desarrollar aplicaciones backend con JavaScript y TypeScript.  
**Proyecto oficial:** API completa con NestJS, autenticación, roles, bases de datos y documentación.

## Resultados de aprendizaje
Explicar Node.js como runtime; construir servicios HTTP con Express; organizar aplicaciones NestJS mediante módulos e inyección de dependencias; integrar persistencia; aplicar controles de seguridad; y reconocer patrones avanzados de procesamiento.

## 15.1 — Node.js
Node.js ejecuta JavaScript fuera del navegador mediante un runtime basado en V8 y APIs de plataforma. No es un lenguaje ni un framework web. Comprende Event Loop, operaciones de I/O, módulos, CommonJS, ES Modules, npm y pnpm. La elección del sistema de módulos debe ser coherente con package metadata, runtime y dependencias.

Estudia filesystem, events, streams, buffers y HTTP module. Los streams procesan datos por fragmentos y permiten limitar memoria; los buffers representan datos binarios. Maneja errores de forma explícita y cierra recursos. No bloquees el Event Loop con trabajo síncrono intensivo; deriva tareas CPU-bound a mecanismos apropiados.

**Laboratorio:** crea una utilidad CLI que lea un archivo grande mediante streams, procese registros y emita resumen sin cargar todo el archivo en memoria.

## 15.2 — Express.js
Express ofrece routing y middleware para aplicaciones HTTP. Un middleware recibe request, response y next; debe terminar la respuesta o transferir el control, evitando dobles respuestas. Separa rutas, controllers, servicios y acceso a datos. Centraliza el manejo de errores y valida entradas en la frontera.

No confíes en datos del body, query o headers. Define límites de tamaño, tipos esperados y errores coherentes. Evita guardar estado de usuario en variables globales del proceso cuando el servicio pueda escalar a varias instancias.

**Laboratorio:** implementa endpoints CRUD de una entidad, validación, middleware de logging sin secretos y manejo uniforme de errores.

## 15.3 — NestJS
Nest organiza aplicaciones en módulos, controllers y providers. Los módulos encapsulan capacidades; controllers reciben solicitudes; providers implementan lógica inyectable. Dependency Injection facilita composición y pruebas.

Estudia DTOs y pipes para transformación/validación; guards para decisiones de autorización; interceptors para lógica transversal; middleware para procesamiento de solicitudes; exception filters para normalizar errores; y configuración externa. Cada mecanismo tiene un propósito distinto: no uses un interceptor como sustituto de autorización ni un guard como validación de todos los datos de negocio.

**Laboratorio:** organiza módulos de usuarios, catálogo y ventas. Añade DTOs, validación, guard de roles y filtro global de errores.

## 15.4 — Persistencia
Prisma y TypeORM son opciones de acceso a datos con modelos distintos; aprende migraciones, relaciones, consultas y transacciones antes de seleccionar. Comprende diferencias entre MySQL, PostgreSQL y MongoDB; Redis suele emplearse para datos en memoria/caché, no como reemplazo automático de la base transaccional.

Define límites de conexión, pool, timeout, manejo de errores y cierre del cliente. No crees conexiones ilimitadas por solicitud. Las migraciones deben estar versionadas y ser repetibles.

**Laboratorio:** implementa repositorios para PostgreSQL o MySQL con migraciones y pruebas de integración; documenta por qué la persistencia elegida corresponde al modelo de dominio.

## 15.5 — Seguridad
Autenticación establece identidad; autorización decide acceso. Passport integra estrategias de autenticación, pero no define por sí solo una política completa. JWT requiere verificación criptográfica y de claims; OAuth 2.0 debe implementarse con flujos apropiados al tipo de cliente. RBAC asigna permisos mediante roles, pero cada operación debe validar el acceso al objeto concreto.

Rate limiting protege recursos frente a abuso; considera identidad, credencial y origen confiable. Valida CORS, cookies, CSRF cuando aplique, expiración y revocación. No expongas secretos, tokens ni información personal en logs.

**Laboratorio:** demuestra con pruebas que un usuario no puede consultar ni modificar registros ajenos cambiando el identificador del endpoint.

## 15.6 — Avanzado
WebSockets habilita comunicación bidireccional persistente; protege conexión y mensajes. Queues y background jobs permiten desacoplar trabajo, pero requieren idempotencia, reintentos, backoff y estrategia de mensajes fallidos. Event-driven architecture comunica cambios mediante eventos; define contratos, orden, duplicados y versionado. Microservices separa servicios desplegables, pero añade latencia, fallos parciales, observabilidad y complejidad operativa: no los adoptes por moda.

Incluye testing unitario, integración y end-to-end. Sustituye dependencias externas por dobles en pruebas unitarias; utiliza servicios reales o contenedores controlados para integración cuando sea viable.

**Laboratorio:** procesa una tarea asíncrona de generación de reporte, expone su estado y comprueba reintentos y duplicados.

## Proyecto oficial — API NestJS
Construye una API completa con autenticación, roles, persistencia y documentación.

### Requisitos
1. Módulos de usuarios, productos e inventario.
2. Controllers y providers separados.
3. DTOs con validación.
4. Persistencia MySQL/PostgreSQL y migraciones.
5. Autenticación y autorización por rol y recurso.
6. Documentación OpenAPI.
7. Manejo de errores y logging seguro.
8. Pruebas unitarias, integración y API.
9. Rate limiting y configuración de seguridad.
10. Un proceso asíncrono o cola con idempotencia.

### Entregables
Repositorio, diagrama modular, modelo de datos, migraciones, contrato OpenAPI, colección HTTP, matriz de permisos, pruebas, guía de despliegue y registro de limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Node.js y asincronía | 15 |
| Express y fundamentos HTTP | 10 |
| NestJS y DI | 20 |
| Persistencia | 15 |
| Seguridad | 20 |
| Procesamiento avanzado | 10 |
| Pruebas y documentación | 10 |

Criterio orientativo: 80/100 y sin vulnerabilidad crítica de autorización ni exposición de secretos.

## Autoevaluación
1. ¿Qué diferencia hay entre JavaScript y Node.js?
2. ¿Qué problema resuelven streams?
3. ¿Qué diferencia existe entre CommonJS y ES Modules?
4. ¿Qué responsabilidad tiene middleware en Express?
5. ¿Qué diferencia hay entre módulo, controller y provider en NestJS?
6. ¿Cuándo utilizarías un pipe o un guard?
7. ¿Qué problema resuelve un ORM y qué no resuelve?
8. ¿Cómo evitarías IDOR/BOLA?
9. ¿Por qué un job debe ser idempotente?
10. ¿Cuándo no conviene adoptar microservicios?

## Recursos audiovisuales
No se aprueban videos todavía. Solo se añadirán piezas con audio hablado en español y relación directa con Node Event Loop, Express middleware, NestJS DI, persistencia o seguridad; no se asumirá que un curso general cubre todos los objetivos.

## Referencias oficiales
- Node.js Documentation: https://nodejs.org/docs/latest/api/
- Node.js Guides: https://nodejs.org/en/learn
- Express: https://expressjs.com/
- NestJS: https://docs.nestjs.com/
- Passport: https://www.passportjs.org/docs/
- Prisma: https://www.prisma.io/docs
- TypeORM: https://typeorm.io/
- PostgreSQL: https://www.postgresql.org/docs/
- MySQL: https://dev.mysql.com/doc/
- Redis: https://redis.io/docs/
- OWASP API Security: https://owasp.org/www-project-api-security/

**Consulta documental:** 2026-11-19. **Verificación práctica:** proyecto no ejecutado en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 15

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados organizan el estudio de los conceptos y los relacionan con la guía técnica y el proyecto de la etapa; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 15.1 — Node.js

#### 15.1.01 — Runtime
Node.js es un runtime que permite ejecutar JavaScript fuera del navegador, construido sobre V8 y APIs del sistema. Distingue el lenguaje, el motor y el runtime; fija versión de Node y política de soporte para que el proyecto sea reproducible.

#### 15.1.02 — V8
V8 compila y ejecuta JavaScript y gestiona memoria mediante técnicas como garbage collection y optimización JIT. El rendimiento depende del patrón de carga y del runtime completo, por lo que evita asumir que una optimización del motor corrige un diseño bloqueante.

#### 15.1.03 — Event Loop
El Event Loop coordina callbacks, temporizadores, operaciones de I/O y otras colas para que Node procese muchas operaciones concurrentes. El código CPU-intensivo puede bloquear el hilo principal; utiliza workers o procesos separados cuando el perfil de carga lo justifique.

#### 15.1.04 — Modules
Los módulos permiten dividir la aplicación y declarar dependencias entre archivos. Node soporta sistemas de módulos con reglas diferentes; elige un formato por proyecto y evita mezclar importaciones incompatibles sin una configuración deliberada.

#### 15.1.05 — CommonJS
CommonJS utiliza `require`, `module.exports` y resolución propia de Node. Comprende caché de módulos y diferencias con ESM; evita depender de comportamientos implícitos cuando una biblioteca ofrece formatos distintos.

#### 15.1.06 — ES Modules
ES Modules utiliza `import` y `export` estáticos y forma parte del estándar JavaScript. Configura correctamente extensión, `type` y resolución de paquetes; prefiere imports explícitos y evita ciclos complejos entre módulos.

#### 15.1.07 — npm
npm instala dependencias, ejecuta scripts y publica paquetes mediante el registro configurado. Revisa scripts de instalación, fija versiones y lockfile y no ejecutes paquetes desconocidos sin verificar procedencia y mantenedor.

#### 15.1.08 — pnpm
pnpm administra dependencias mediante un almacén compartido y enlaces, favoreciendo instalaciones eficientes y reproducibles. Conserva el lockfile, fija versión del gestor y verifica que herramientas CI utilicen la misma configuración.

#### 15.1.09 — Filesystem
El módulo `fs` permite consultar, leer y escribir archivos y directorios mediante APIs síncronas o asíncronas. Prefiere operaciones asíncronas en servidores, controla errores y permisos y evita confiar en rutas construidas con datos del usuario.

#### 15.1.10 — Events
El sistema de eventos de Node usa emisores y listeners para notificar sucesos dentro del proceso. Gestiona listeners y errores de forma explícita, elimina suscripciones cuando dejan de ser necesarias y evita eventos globales que oculten dependencias.

#### 15.1.11 — Streams
Streams procesan datos de forma incremental sin cargar necesariamente todo el contenido en memoria. Comprende Readable, Writable, Duplex y Transform, backpressure y cierre; utiliza pipelines para propagar errores y liberar recursos.

#### 15.1.12 — Buffers
Buffers representan secuencias de bytes para datos binarios. Define codificación al convertir texto, valida límites y no asumas que cada byte equivale a un carácter; evita exponer segmentos de memoria que contengan datos sensibles.

#### 15.1.13 — HTTP Module
El módulo HTTP permite crear servidores y clientes HTTP de bajo nivel. Gestiona método, ruta, headers, body, streams y cierre de conexión; limita tamaño de solicitudes y añade timeouts y manejo de errores antes de exponer el servicio.

#### 15.1.14 — Async Programming
La programación asíncrona en Node utiliza callbacks, promesas y async/await para operaciones de I/O. Propaga errores, limita concurrencia y cancela trabajo cuando sea posible; lanzar miles de promesas simultáneas puede agotar conexiones o memoria.

### Módulo 15.2 — Express.js

#### 15.2.01 — Routing
Routing de Express asocia método y ruta con handlers que procesan una solicitud. Define rutas específicas, valida parámetros y versiona contratos; no mezcles rutas administrativas con públicas sin controles de autorización.

#### 15.2.02 — Middleware
Middleware de Express recibe request, response y next para ejecutar lógica transversal o finalizar la respuesta. El orden de registro determina su comportamiento; no llames `next` después de responder y maneja errores mediante middleware especializado.

#### 15.2.03 — Controllers
Los controllers coordinan entrada HTTP, validación y respuesta, delegando reglas de negocio a servicios. Devuelve códigos y estructuras consistentes, evita consultas y lógica de dominio complejas dentro del handler.

#### 15.2.04 — Error Handling
Error Handling centraliza errores síncronos y asíncronos y los transforma en respuestas controladas. No envíes stack traces al cliente, conserva contexto interno protegido y asegúrate de que errores rechazados lleguen al middleware correspondiente.

#### 15.2.05 — Request
El objeto Request contiene método, ruta, headers, parámetros, query y body según el middleware configurado. Valida y tipa cada entrada, no confíes en el tipo declarado por el cliente y evita registrar credenciales o datos personales.

#### 15.2.06 — Response
El objeto Response permite establecer status, headers y body y finalizar el intercambio HTTP. Envía una sola respuesta por solicitud, define status semánticos y evita filtrar detalles internos o encabezados inseguros.

#### 15.2.07 — REST APIs
Una REST API con Express organiza recursos y operaciones mediante rutas HTTP. Define DTOs, validación, autenticación, paginación y errores; añade pruebas de contrato para que cambios internos no rompan consumidores.

### Módulo 15.3 — NestJS

#### 15.3.01 — Modules
Un módulo NestJS agrupa controllers, providers e imports y delimita capacidades de la aplicación. Diseña módulos por funcionalidad, exporta solo lo que otros módulos necesitan y evita ciclos de dependencia.

#### 15.3.02 — Controllers
Controllers de NestJS declaran rutas y traducen solicitudes HTTP a llamadas de aplicación mediante decoradores. Manténlos delgados y valida parámetros/body antes de invocar servicios.

#### 15.3.03 — Providers
Providers son clases u objetos que Nest puede administrar e inyectar, como servicios, repositorios o adaptadores. Define tokens y alcance del provider con claridad para que su ciclo de vida no introduzca estado compartido inesperado.

#### 15.3.04 — Services
Services encapsulan lógica de aplicación y reglas de negocio y se registran normalmente como providers. Mantén operaciones testables y dependencias explícitas; no utilices el contenedor para resolver servicios de forma oculta en cualquier parte del código.

#### 15.3.05 — Dependency Injection
Dependency Injection resuelve dependencias a partir de tokens registrados en el módulo. Usa inyección por constructor, configura providers de prueba y evita dependencias circulares que señalen límites de módulo mal definidos.

#### 15.3.06 — DTOs
DTOs describen la forma de los datos que entran o salen de una API. Separa DTO de entidad persistente, valida tipos y restricciones y evita exponer propiedades internas o sensibles.

#### 15.3.07 — Pipes
Pipes transforman o validan argumentos antes de que lleguen al handler. Configura validación global o por ruta con whitelist y transformación controlada; no asumas que una anotación TypeScript valida automáticamente datos en runtime.

#### 15.3.08 — Guards
Guards deciden si una solicitud puede continuar, normalmente mediante autenticación o autorización. Aplica políticas por endpoint y recurso, y recuerda que los guards deben verificar permisos reales, no solo presencia de un token.

#### 15.3.09 — Interceptors
Interceptors envuelven la ejecución de handlers para añadir comportamiento como transformación, logging, métricas o timeout. Evita alterar silenciosamente contratos de respuesta y excluye secretos y payloads sensibles de la telemetría.

#### 15.3.10 — Middleware
Middleware NestJS se ejecuta antes del handler y puede modificar request o finalizar la respuesta. Úsalo para tareas HTTP transversales; prefiere guards para autorización y pipes para validación cuando el framework ofrece esas capas.

#### 15.3.11 — Exception Filters
Exception Filters controlan cómo se convierten excepciones en respuestas. Define un formato de error estable, mapea errores conocidos y oculta detalles internos; no conviertas todos los fallos en un 200 o un mensaje genérico sin trazabilidad.

#### 15.3.12 — Validation
Validation en NestJS suele combinar class-validator y class-transformer con DTOs. Configura transformación y rechazo de propiedades desconocidas, y valida nuevamente en servicios o base de datos las invariantes de negocio.

#### 15.3.13 — Configuration
Configuration administra valores de entorno y perfiles mediante módulos y esquemas de validación. Comprueba variables requeridas al iniciar y mantén secretos fuera del repositorio, logs, imágenes de contenedor y artefactos de build.

### Módulo 15.4 — Persistencia

#### 15.4.01 — Prisma
Prisma ofrece un ORM y cliente tipado generado a partir de un schema. Define relaciones, restricciones y migraciones con revisión; el tipado generado no elimina validación de entradas ni garantiza que la consulta sea eficiente.

#### 15.4.02 — TypeORM
TypeORM mapea entidades y repositorios a tablas y operaciones relacionales. Comprende decoradores, relaciones y carga de datos; revisa SQL generado y evita sincronizar esquemas automáticamente en producción sin migraciones controladas.

#### 15.4.03 — MySQL
MySQL ofrece persistencia relacional con transacciones, índices y restricciones. Fija versión y motor, parametriza consultas y revisa aislamiento y planes; no construyas SQL concatenando entradas del usuario.

#### 15.4.04 — PostgreSQL
PostgreSQL proporciona un motor relacional con tipos, constraints, transacciones y extensiones. Diseña migraciones reproducibles, roles con privilegio mínimo y consultas verificables mediante EXPLAIN.

#### 15.4.05 — MongoDB
MongoDB almacena documentos BSON y permite modelar datos embebidos o referenciados. Elige estructura según patrones de acceso y atomicidad; valida documentos, define índices y no trates esquema flexible como ausencia de reglas.

#### 15.4.06 — Redis
Redis ofrece estructuras en memoria para caché, colas, sesiones y coordinación. Define TTL, persistencia, límites y seguridad de red; no lo uses como fuente de verdad sin un diseño explícito de durabilidad y recuperación.

### Módulo 15.5 — Seguridad

#### 15.5.01 — Authentication
Authentication verifica identidad mediante credenciales, sesiones o proveedores externos. Usa bibliotecas mantenidas, protege el ciclo de credenciales y aplica MFA cuando el riesgo lo justifique.

#### 15.5.02 — Authorization
Authorization comprueba permisos sobre operaciones y recursos después de identificar al sujeto. Aplica mínimo privilegio y validación a nivel de objeto para prevenir acceso horizontal o vertical no autorizado.

#### 15.5.03 — Passport
Passport es middleware de autenticación extensible mediante estrategias. Configura estrategia, callbacks y sesión con cuidado; valida issuer/audience cuando uses tokens y no confundas que una estrategia autentique con autorización de negocio.

#### 15.5.04 — JWT
JWT puede transportar claims firmados para autenticar solicitudes. Valida algoritmo, firma, issuer, audience y expiración, limita claims y diseña revocación/rotación; la codificación Base64URL no cifra el contenido.

#### 15.5.05 — OAuth2
OAuth2 permite autorización delegada con scopes y tokens de acceso. Selecciona flujos actuales y usa PKCE para clientes públicos; nunca solicites contraseñas del usuario para sustituir el flujo del proveedor.

#### 15.5.06 — RBAC
RBAC asigna permisos mediante roles asociados a usuarios o grupos. Define roles pequeños y revisables, comprueba acceso a cada recurso y evita reglas implícitas basadas únicamente en el nombre del rol.

#### 15.5.07 — Rate Limiting
Rate Limiting restringe frecuencia o volumen de solicitudes para proteger disponibilidad y controlar abuso. Elige clave y ventana, responde con códigos/headers adecuados y considera almacenamiento distribuido cuando hay múltiples instancias.

### Módulo 15.6 — Avanzado

#### 15.6.01 — WebSockets
WebSockets mantiene comunicación bidireccional y persistente entre cliente y servidor. Autentica la conexión y autoriza mensajes, valida origen, limita payloads y define reconexión, heartbeat y cierre de sesiones.

#### 15.6.02 — Queues
Queues permiten procesar tareas fuera del ciclo de una solicitud HTTP. Diseña reintentos, backoff, dead-letter, idempotencia y métricas; evita asumir orden o entrega exactamente una vez.

#### 15.6.03 — Background jobs
Background jobs ejecuta trabajos diferidos o periódicos como reportes, correos o procesamiento de archivos. Define timeout, cancelación, concurrencia y recuperación tras reinicio, y no dependas de memoria local para estado que debe persistir.

#### 15.6.04 — Event-driven architecture
Event-driven architecture conecta componentes mediante eventos que anuncian hechos ocurridos. Define contratos versionados, entrega y orden, idempotencia y observabilidad; diferencia eventos de dominio de comandos que piden ejecutar una acción.

#### 15.6.05 — Microservices
Microservices separa un sistema en servicios desplegables con límites de dominio y contratos de red. Evalúa coste operativo, consistencia distribuida, observabilidad y resiliencia; no dividas una aplicación pequeña solo por seguir una moda arquitectónica.

#### 15.6.06 — Testing
Testing verifica comportamiento mediante pruebas unitarias, integración, contrato y extremo a extremo. Aísla dependencias externas, prueba rutas de error y seguridad, y ejecuta suites en CI; una prueba que solo comprueba status 200 es insuficiente.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 53 orientaciones genéricas por explicaciones específicas. Se desarrollaron el runtime Node/V8, event loop y streams, Express, módulos/providers/guards/interceptors/pipes de NestJS, persistencia SQL/NoSQL, seguridad de identidad, OAuth2/JWT/RBAC, colas, jobs, microservicios y pruebas.

**Revisión interna:** 53/53 entradas desarrolladas y cotejadas con el roadmap. Se añadieron límites de concurrencia, validación en runtime, idempotencia, autorización por recurso, control de archivos/configuración y manejo de errores. Pendiente: fijar versiones exactas de Node/Nest/Express/ORMs, ejecutar pruebas automatizadas e integración, revisar migraciones y verificar flujos de autenticación en entorno aislado. No se declara ejecución ni aprobación externa.
