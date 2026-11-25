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


**Escenario aplicado.** Un servicio se ejecuta en Node.js dentro de un contenedor. El equipo registra versión de runtime y compatibilidad de dependencias para evitar diferencias entre desarrollo y producción.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia hay entre JavaScript, V8 y Node.js?

**Práctica y evidencia:** Ejecuta un script Node.js desde terminal y registra versión, argumentos y código de salida. **Evidencia:** distingue runtime, proceso y entorno de ejecución.

#### 15.1.02 — V8
V8 compila y ejecuta JavaScript y gestiona memoria mediante técnicas como garbage collection y optimización JIT. El rendimiento depende del patrón de carga y del runtime completo, por lo que evita asumir que una optimización del motor corrige un diseño bloqueante.


**Escenario aplicado.** Un bucle síncrono intensivo mantiene ocupado el hilo y retrasa solicitudes aunque la CPU del host no esté saturada por otros procesos.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué el rendimiento de V8 no elimina el problema de código bloqueante?

**Práctica y evidencia:** Inspecciona información de V8 con `process.versions` y ejecuta una operación JavaScript. **Evidencia:** explica que V8 ejecuta JavaScript, mientras Node.js aporta APIs y runtime.

#### 15.1.03 — Event Loop
El Event Loop coordina callbacks, temporizadores, operaciones de I/O y otras colas para que Node procese muchas operaciones concurrentes. El código CPU-intensivo puede bloquear el hilo principal; utiliza workers o procesos separados cuando el perfil de carga lo justifique.


**Escenario aplicado.** Una tarea de I/O tarda mientras otras solicitudes continúan. Una operación CPU-bound larga bloquea el event loop y degrada la latencia de todas ellas.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué tipo de trabajo puede bloquear el event loop y cómo se aísla?

**Práctica y evidencia:** Compara una operación síncrona con una promesa y un temporizador en un script pequeño. **Evidencia:** predice y registra el orden de ejecución del Event Loop.

#### 15.1.04 — Modules
Los módulos permiten dividir la aplicación y declarar dependencias entre archivos. Node soporta sistemas de módulos con reglas diferentes; elige un formato por proyecto y evita mezclar importaciones incompatibles sin una configuración deliberada.


**Escenario aplicado.** Un proyecto define límites de módulos para separar acceso a datos, lógica y transporte, evitando dependencias circulares.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué criterio permite decidir si una función debe exportarse desde un módulo?

**Práctica y evidencia:** Divide un programa en módulos y exporta una función reutilizable. **Evidencia:** documenta dependencias y demuestra que el consumidor no necesita conocer detalles internos.

#### 15.1.05 — CommonJS
CommonJS utiliza `require`, `module.exports` y resolución propia de Node. Comprende caché de módulos y diferencias con ESM; evita depender de comportamientos implícitos cuando una biblioteca ofrece formatos distintos.


**Escenario aplicado.** Un proyecto heredado usa CommonJS y requiere migrar gradualmente a ESM. La interoperabilidad depende de package.json, extensiones y versión del runtime.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué incompatibilidad puede aparecer al mezclar require e import?

**Práctica y evidencia:** Crea un módulo CommonJS con `require` y `module.exports` y úsalo desde otro archivo. **Evidencia:** explica resolución y caché de módulos.

#### 15.1.06 — ES Modules
ES Modules utiliza `import` y `export` estáticos y forma parte del estándar JavaScript. Configura correctamente extensión, `type` y resolución de paquetes; prefiere imports explícitos y evita ciclos complejos entre módulos.


**Escenario aplicado.** Un módulo ESM usa import/export y resuelve extensiones y rutas conforme al modo de módulo configurado. La migración incluye scripts, pruebas y dependencias.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué la configuración del paquete afecta la interpretación de los archivos?

**Práctica y evidencia:** Convierte el ejemplo a ES Modules con `import` y `export`. **Evidencia:** identifica configuración de módulo y diferencia de sintaxis respecto a CommonJS.

#### 15.1.07 — npm
npm instala dependencias, ejecuta scripts y publica paquetes mediante el registro configurado. Revisa scripts de instalación, fija versiones y lockfile y no ejecutes paquetes desconocidos sin verificar procedencia y mantenedor.


**Escenario aplicado.** npm instala dependencias y ejecuta scripts definidos en package.json. El lockfile se versiona y las dependencias se revisan antes de ejecutar scripts de terceros.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia existe entre package.json y package-lock.json?

**Práctica y evidencia:** Añade un paquete con npm y ejecuta un script definido en package.json. **Evidencia:** conserva package-lock y distingue dependencias de runtime y desarrollo.

#### 15.1.08 — pnpm
pnpm administra dependencias mediante un almacén compartido y enlaces, favoreciendo instalaciones eficientes y reproducibles. Conserva el lockfile, fija versión del gestor y verifica que herramientas CI utilicen la misma configuración.


**Escenario aplicado.** pnpm utiliza un almacén de contenido y enlaces para reducir duplicación, pero requiere comprender su estructura y compatibilidad con herramientas del proyecto.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué no deben mezclarse gestores de paquetes y lockfiles sin política?

**Práctica y evidencia:** Instala dependencias con pnpm usando lockfile existente. **Evidencia:** explica reproducibilidad y evita mezclar gestores de paquetes en un mismo proyecto.

#### 15.1.09 — Filesystem
El módulo `fs` permite consultar, leer y escribir archivos y directorios mediante APIs síncronas o asíncronas. Prefiere operaciones asíncronas en servidores, controla errores y permisos y evita confiar en rutas construidas con datos del usuario.


**Escenario aplicado.** Un endpoint de carga guarda archivos en un directorio controlado. El nombre recibido se normaliza y no se concatena directamente a una ruta para evitar traversal.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué validaciones debe superar un nombre de archivo externo?

**Práctica y evidencia:** Lee y escribe un archivo dentro de una carpeta temporal con `node:fs/promises`. **Evidencia:** maneja errores y evita rutas arbitrarias suministradas por usuarios.

#### 15.1.10 — Events
El sistema de eventos de Node usa emisores y listeners para notificar sucesos dentro del proceso. Gestiona listeners y errores de forma explícita, elimina suscripciones cuando dejan de ser necesarias y evita eventos globales que oculten dependencias.


**Escenario aplicado.** Un emisor publica eventos de dominio y varios listeners reaccionan. Se controla el orden, los errores y la posibilidad de listeners duplicados o fugas de memoria.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué problema aparece si se acumulan listeners sin retirarlos?

**Práctica y evidencia:** Implementa un EventEmitter con dos listeners y elimina uno de ellos. **Evidencia:** explica emisión síncrona, orden y riesgo de listeners duplicados.

#### 15.1.11 — Streams
Streams procesan datos de forma incremental sin cargar necesariamente todo el contenido en memoria. Comprende Readable, Writable, Duplex y Transform, backpressure y cierre; utiliza pipelines para propagar errores y liberar recursos.


**Escenario aplicado.** Un pipeline procesa un archivo grande mediante streams en vez de cargarlo completo en memoria. Backpressure regula la velocidad entre productor y consumidor.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué ventaja ofrece backpressure al procesar datos grandes?

**Práctica y evidencia:** Procesa un archivo grande con streams en lugar de cargarlo completo en memoria. **Evidencia:** explica backpressure y demuestra manejo de errores/cierre.

#### 15.1.12 — Buffers
Buffers representan secuencias de bytes para datos binarios. Define codificación al convertir texto, valida límites y no asumas que cada byte equivale a un carácter; evita exponer segmentos de memoria que contengan datos sensibles.


**Escenario aplicado.** Un protocolo binario se recibe en fragmentos Buffer. El parser valida longitud y límites antes de interpretar bytes y evita asumir que cada chunk contiene un mensaje completo.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué un chunk de stream no equivale necesariamente a un mensaje completo?

**Práctica y evidencia:** Convierte texto a Buffer y examina longitud y codificación. **Evidencia:** distingue bytes de caracteres y explica por qué una longitud UTF-8 puede diferir.

#### 15.1.13 — HTTP Module
El módulo HTTP permite crear servidores y clientes HTTP de bajo nivel. Gestiona método, ruta, headers, body, streams y cierre de conexión; limita tamaño de solicitudes y añade timeouts y manejo de errores antes de exponer el servicio.


**Escenario aplicado.** Un servidor HTTP local expone un endpoint de salud y valida método, ruta y tamaño de body. La aplicación no escucha en interfaces públicas por defecto en el laboratorio.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué controles mínimos debe tener un servidor HTTP de prueba?

**Práctica y evidencia:** Crea un servidor HTTP mínimo con ruta de salud y respuesta JSON. **Evidencia:** prueba método, ruta, status y cierre ordenado del servidor.

#### 15.1.14 — Async Programming
La programación asíncrona en Node utiliza callbacks, promesas y async/await para operaciones de I/O. Propaga errores, limita concurrencia y cancela trabajo cuando sea posible; lanzar miles de promesas simultáneas puede agotar conexiones o memoria.


**Escenario aplicado.** Una operación asíncrona propaga errores mediante await/catch y define cancelación o timeout. Las promesas rechazadas no se ignoran ni quedan sin observación.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia existe entre concurrencia de I/O y paralelismo de CPU?

**Práctica y evidencia:** Usa `async`/`await` con dos operaciones concurrentes y una secuencial. **Evidencia:** compara Promise.all con await secuencial y maneja rechazos.

### Módulo 15.2 — Express.js

#### 15.2.01 — Routing
Routing de Express asocia método y ruta con handlers que procesan una solicitud. Define rutas específicas, valida parámetros y versiona contratos; no mezcles rutas administrativas con públicas sin controles de autorización.


**Escenario aplicado.** Un router distingue rutas estáticas y parámetros, y aplica autenticación antes de llegar al handler protegido. La precedencia de rutas se prueba para evitar colisiones.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué puede ocurrir si una ruta comodín se registra antes que una ruta específica?

**Práctica y evidencia:** Define rutas para colección y recurso individual y prueba parámetros de ruta/query. **Evidencia:** documenta coincidencia, método y respuesta 404.

#### 15.2.02 — Middleware
Middleware de Express recibe request, response y next para ejecutar lógica transversal o finalizar la respuesta. El orden de registro determina su comportamiento; no llames `next` después de responder y maneja errores mediante middleware especializado.


**Escenario aplicado.** Un middleware añade correlación y valida una condición transversal. Su orden debe ser explícito y los errores se propagan al manejador central.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué un middleware debe llamar a la continuación o finalizar la respuesta correctamente?

**Práctica y evidencia:** Añade middleware de registro con correlación y excluye datos sensibles. **Evidencia:** muestra orden de ejecución y cómo pasa el control al siguiente middleware.

#### 15.2.03 — Controllers
Los controllers coordinan entrada HTTP, validación y respuesta, delegando reglas de negocio a servicios. Devuelve códigos y estructuras consistentes, evita consultas y lógica de dominio complejas dentro del handler.


**Escenario aplicado.** Un controller recibe parámetros HTTP y delega el caso de uso. No debe contener consultas SQL ni reglas de negocio difíciles de probar.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué responsabilidad debe permanecer fuera del controller?

**Práctica y evidencia:** Separa handlers/controladores de lógica de negocio y acceso a datos. **Evidencia:** prueba un controlador con dependencias sustituidas.

#### 15.2.04 — Error Handling
Error Handling centraliza errores síncronos y asíncronos y los transforma en respuestas controladas. No envíes stack traces al cliente, conserva contexto interno protegido y asegúrate de que errores rechazados lleguen al middleware correspondiente.


**Escenario aplicado.** Una API distingue error de validación, autenticación, dependencia y fallo inesperado. La respuesta pública no revela stack trace y el log protegido conserva correlación.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Cómo se diferencia un error operacional de uno de programación?

**Práctica y evidencia:** Implementa un manejador central de errores y diferencia errores esperados de fallos internos. **Evidencia:** devuelve respuesta segura y registra detalle solo en log protegido.

#### 15.2.05 — Request
El objeto Request contiene método, ruta, headers, parámetros, query y body según el middleware configurado. Valida y tipa cada entrada, no confíes en el tipo declarado por el cliente y evita registrar credenciales o datos personales.


**Escenario aplicado.** Un objeto Request contiene headers, parámetros, body y contexto de conexión. La aplicación valida el origen de cada dato y no confía en tipos declarados por el cliente.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué todos los datos de Request deben considerarse no confiables?

**Práctica y evidencia:** Valida parámetros, query y body antes de ejecutar la operación. **Evidencia:** demuestra rechazo de tipos incorrectos y límites excedidos.

#### 15.2.06 — Response
El objeto Response permite establecer status, headers y body y finalizar el intercambio HTTP. Envía una sola respuesta por solicitud, define status semánticos y evita filtrar detalles internos o encabezados inseguros.


**Escenario aplicado.** La respuesta establece status, headers y formato coherentes. El servidor evita enviar una segunda respuesta después de cerrar el flujo o ante errores asíncronos.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué significa que los headers ya hayan sido enviados y por qué importa al manejar errores?

**Práctica y evidencia:** Construye respuestas consistentes con status, cabeceras y cuerpo apropiados. **Evidencia:** comprueba que errores no se reportan como éxito HTTP.

#### 15.2.07 — REST APIs
Una REST API con Express organiza recursos y operaciones mediante rutas HTTP. Define DTOs, validación, autenticación, paginación y errores; añade pruebas de contrato para que cambios internos no rompan consumidores.


**Escenario aplicado.** Un endpoint REST usa recursos, métodos y códigos HTTP consistentes. La autorización se verifica sobre el recurso solicitado y no solo sobre la ruta.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia hay entre diseñar una ruta REST y nombrar una acción RPC?

**Práctica y evidencia:** Diseña una API REST de recursos con métodos idempotentes y paginación. **Evidencia:** prueba contrato y códigos de estado mediante cliente HTTP.

### Módulo 15.3 — NestJS

#### 15.3.01 — Modules
Un módulo NestJS agrupa controllers, providers e imports y delimita capacidades de la aplicación. Diseña módulos por funcionalidad, exporta solo lo que otros módulos necesitan y evita ciclos de dependencia.


**Escenario aplicado.** Un módulo NestJS agrupa controllers, providers e imports/exports. Los límites del módulo expresan dependencias y evitan que toda la aplicación comparta un contenedor indiscriminado.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué ventaja aporta encapsular providers dentro de módulos?

**Práctica y evidencia:** Crea un módulo NestJS que encapsule una funcionalidad y exporte solo proveedores necesarios. **Evidencia:** explica imports, providers, controllers y exports.

#### 15.3.02 — Controllers
Controllers de NestJS declaran rutas y traducen solicitudes HTTP a llamadas de aplicación mediante decoradores. Manténlos delgados y valida parámetros/body antes de invocar servicios.


**Escenario aplicado.** Un controller NestJS declara rutas y DTOs y delega a providers. Los decoradores describen el contrato, pero no sustituyen validación ni autorización.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué parte del procesamiento debe delegarse al provider?

**Práctica y evidencia:** Implementa un controller NestJS que delegue en un provider. **Evidencia:** prueba ruta y método con aplicación de test.

#### 15.3.03 — Providers
Providers son clases u objetos que Nest puede administrar e inyectar, como servicios, repositorios o adaptadores. Define tokens y alcance del provider con claridad para que su ciclo de vida no introduzca estado compartido inesperado.


**Escenario aplicado.** Un provider puede ser servicio, repositorio o fábrica administrada por Nest. Su scope debe ser consciente del ciclo de vida y de la concurrencia.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué consecuencias tiene elegir un scope request para un provider de uso frecuente?

**Práctica y evidencia:** Declara un provider e inyéctalo por constructor. **Evidencia:** sustituye el provider por un mock en una prueba.

#### 15.3.04 — Services
Services encapsulan lógica de aplicación y reglas de negocio y se registran normalmente como providers. Mantén operaciones testables y dependencias explícitas; no utilices el contenedor para resolver servicios de forma oculta en cualquier parte del código.


**Escenario aplicado.** Un servicio NestJS contiene el caso de uso y recibe dependencias por constructor. La prueba unitaria sustituye providers externos mediante mocks o fakes.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué hace que un servicio sea testeable sin levantar toda la aplicación?

**Práctica y evidencia:** Implementa un servicio con una regla de negocio y errores de dominio. **Evidencia:** prueba casos válidos y no válidos sin depender de HTTP.

#### 15.3.05 — Dependency Injection
Dependency Injection resuelve dependencias a partir de tokens registrados en el módulo. Usa inyección por constructor, configura providers de prueba y evita dependencias circulares que señalen límites de módulo mal definidos.


**Escenario aplicado.** La inyección de dependencias se resuelve mediante tokens y providers. Las dependencias circulares se tratan como señal de diseño que debe evaluarse, no solo ocultarse.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué una dependencia circular suele indicar un límite de módulo mal definido?

**Práctica y evidencia:** Configura inyección de dependencias por token y compara provider de clase, valor y fábrica. **Evidencia:** justifica el tipo según el ciclo de vida.

#### 15.3.06 — DTOs
DTOs describen la forma de los datos que entran o salen de una API. Separa DTO de entidad persistente, valida tipos y restricciones y evita exponer propiedades internas o sensibles.


**Escenario aplicado.** Un DTO define datos de entrada permitidos y el ValidationPipe aplica reglas en runtime. Los tipos TypeScript desaparecen al compilar y no validan por sí solos JSON recibido.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué una interfaz TypeScript no valida automáticamente el body HTTP?

**Práctica y evidencia:** Define DTOs para entrada y salida y evita exponer entidades persistidas. **Evidencia:** demuestra transformación y validación de datos.

#### 15.3.07 — Pipes
Pipes transforman o validan argumentos antes de que lleguen al handler. Configura validación global o por ruta con whitelist y transformación controlada; no asumas que una anotación TypeScript valida automáticamente datos en runtime.


**Escenario aplicado.** Un pipe transforma y valida parámetros antes de invocar el controller. La conversión debe ser explícita y los errores de validación consistentes.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia existe entre transformar un parámetro y autorizar su uso?

**Práctica y evidencia:** Usa Pipes para transformar o validar parámetros y body. **Evidencia:** prueba conversión, validación fallida y respuesta de error.

#### 15.3.08 — Guards
Guards deciden si una solicitud puede continuar, normalmente mediante autenticación o autorización. Aplica políticas por endpoint y recurso, y recuerda que los guards deben verificar permisos reales, no solo presencia de un token.


**Escenario aplicado.** Un guard decide si la solicitud puede continuar según identidad, rol o permiso. La política debe validar acceso al recurso y no depender de datos enviados por el cliente.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué un guard basado solo en un rol general puede ser insuficiente?

**Práctica y evidencia:** Protege una ruta con Guard basado en identidad y permisos. **Evidencia:** demuestra acceso permitido y denegado para distintos contextos.

#### 15.3.09 — Interceptors
Interceptors envuelven la ejecución de handlers para añadir comportamiento como transformación, logging, métricas o timeout. Evita alterar silenciosamente contratos de respuesta y excluye secretos y payloads sensibles de la telemetría.


**Escenario aplicado.** Un interceptor mide duración y añade correlación, pero no debe registrar secretos ni alterar inesperadamente el contrato de respuesta.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué responsabilidad transversal es apropiada para un interceptor?

**Práctica y evidencia:** Añade un Interceptor para medir duración o transformar respuesta sin alterar reglas de negocio. **Evidencia:** demuestra ejecución antes/después y manejo de errores.

#### 15.3.10 — Middleware
Middleware NestJS se ejecuta antes del handler y puede modificar request o finalizar la respuesta. Úsalo para tareas HTTP transversales; prefiere guards para autorización y pipes para validación cuando el framework ofrece esas capas.


**Escenario aplicado.** El middleware NestJS opera en una fase distinta de guards, interceptors y pipes. Comprender el ciclo de solicitud evita aplicar controles en un punto demasiado tardío.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿En qué se diferencia el middleware de un guard en el ciclo de petición?

**Práctica y evidencia:** Implementa Middleware para correlación de solicitud y explica por qué no sustituye a Guard o Interceptor. **Evidencia:** compara momento y contexto disponible.

#### 15.3.11 — Exception Filters
Exception Filters controlan cómo se convierten excepciones en respuestas. Define un formato de error estable, mapea errores conocidos y oculta detalles internos; no conviertas todos los fallos en un 200 o un mensaje genérico sin trazabilidad.


**Escenario aplicado.** Un Exception Filter normaliza errores y evita filtrar detalles internos. Los errores esperados y no esperados reciben tratamiento y registro diferenciados.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué información debe incluir una respuesta de error sin revelar internals?

**Práctica y evidencia:** Centraliza excepciones con Exception Filter y normaliza el contrato de error. **Evidencia:** evita devolver stack trace o información interna.

#### 15.3.12 — Validation
Validation en NestJS suele combinar class-validator y class-transformer con DTOs. Configura transformación y rechazo de propiedades desconocidas, y valida nuevamente en servicios o base de datos las invariantes de negocio.


**Escenario aplicado.** El ValidationPipe rechaza payloads que no cumplen DTO, límites y reglas declaradas. Configurar whitelist/forbidNonWhitelisted reduce campos inesperados, pero la lógica de dominio sigue validándose aparte.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué riesgo reduce rechazar propiedades no declaradas?

**Práctica y evidencia:** Configura ValidationPipe con whitelist y transformación apropiada para DTOs. **Evidencia:** prueba propiedades desconocidas, campos requeridos y tipos inválidos.

#### 15.3.13 — Configuration
Configuration administra valores de entorno y perfiles mediante módulos y esquemas de validación. Comprueba variables requeridas al iniciar y mantén secretos fuera del repositorio, logs, imágenes de contenedor y artefactos de build.


**Escenario aplicado.** La configuración se valida al iniciar mediante esquema y secretos externos. Un valor ausente no debe sustituirse silenciosamente por una configuración insegura.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué fallar rápido al iniciar puede ser más seguro que usar defaults ambiguos?

**Práctica y evidencia:** Carga configuración tipada desde variables de entorno y valida requeridos al iniciar. **Evidencia:** demuestra fallo seguro ante variable ausente sin mostrar secretos.

### Módulo 15.4 — Persistencia

#### 15.4.01 — Prisma
Prisma ofrece un ORM y cliente tipado generado a partir de un schema. Define relaciones, restricciones y migraciones con revisión; el tipado generado no elimina validación de entradas ni garantiza que la consulta sea eficiente.


**Escenario aplicado.** Prisma genera un cliente a partir del schema y las migraciones deben versionarse. Las consultas usan selección explícita de campos y evitan exponer registros completos.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia existe entre el schema Prisma y el estado real de la base de datos?

**Práctica y evidencia:** Modela entidades y consultas con Prisma en una base descartable y ejecuta migración. **Evidencia:** conserva schema y migración y verifica integridad.

#### 15.4.02 — TypeORM
TypeORM mapea entidades y repositorios a tablas y operaciones relacionales. Comprende decoradores, relaciones y carga de datos; revisa SQL generado y evita sincronizar esquemas automáticamente en producción sin migraciones controladas.


**Escenario aplicado.** TypeORM mapea entidades y relaciones, pero las consultas y estrategias de carga deben inspeccionarse para detectar N+1 y transacciones mal delimitadas.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Cómo puede una abstracción ORM ocultar una consulta costosa?

**Práctica y evidencia:** Define entidades y relaciones con TypeORM y compara carga de relaciones con consultas explícitas. **Evidencia:** detecta consultas N+1 y evita sincronizar esquema destructivamente en producción.

#### 15.4.03 — MySQL
MySQL ofrece persistencia relacional con transacciones, índices y restricciones. Fija versión y motor, parametriza consultas y revisa aislamiento y planes; no construyas SQL concatenando entradas del usuario.


**Escenario aplicado.** Una integración MySQL declara charset, collation, engine y versión. El equipo prueba constraints, transacciones y migraciones sobre la versión que usará en producción.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué probar solo la conexión no valida la integración con MySQL?

**Práctica y evidencia:** Conecta el servicio a MySQL con usuario de privilegios mínimos y pool de conexiones. **Evidencia:** prueba conexión y consulta simple sin exponer credenciales.

#### 15.4.04 — PostgreSQL
PostgreSQL proporciona un motor relacional con tipos, constraints, transacciones y extensiones. Diseña migraciones reproducibles, roles con privilegio mínimo y consultas verificables mediante EXPLAIN.


**Escenario aplicado.** PostgreSQL aplica tipos y restricciones que pueden diferir de MySQL. Los tests de persistencia deben ejecutarse sobre el motor objetivo, no solo SQLite en memoria.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencias de tipos o SQL pueden romper una migración entre motores?

**Práctica y evidencia:** Ejecuta pruebas de integración contra PostgreSQL y documenta diferencias relevantes de tipos/SQL. **Evidencia:** demuestra que la suite utiliza el motor real.

#### 15.4.05 — MongoDB
MongoDB almacena documentos BSON y permite modelar datos embebidos o referenciados. Elige estructura según patrones de acceso y atomicidad; valida documentos, define índices y no trates esquema flexible como ausencia de reglas.


**Escenario aplicado.** MongoDB almacena documentos y requiere diseñar índices y esquema de acuerdo con patrones de consulta. Flexibilidad no significa ausencia de validación ni de consistencia.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué decisión de modelado determina si conviene incrustar o referenciar documentos?

**Práctica y evidencia:** Implementa operaciones CRUD en una instancia MongoDB local con validación y filtros. **Evidencia:** prueba consulta, actualización y rechazo de documento inválido.

#### 15.4.06 — Redis
Redis ofrece estructuras en memoria para caché, colas, sesiones y coordinación. Define TTL, persistencia, límites y seguridad de red; no lo uses como fuente de verdad sin un diseño explícito de durabilidad y recuperación.


**Escenario aplicado.** Redis puede servir como caché o almacén de estructuras en memoria. TTL, persistencia, memoria máxima y seguridad de red deben definirse según el uso.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué riesgo aparece si Redis se expone sin autenticación ni segmentación?

**Práctica y evidencia:** Utiliza Redis para caché o sesión temporal y define expiración. **Evidencia:** demuestra invalidación y evita almacenar secretos sin protección.

### Módulo 15.5 — Seguridad

#### 15.5.01 — Authentication
Authentication verifica identidad mediante credenciales, sesiones o proveedores externos. Usa bibliotecas mantenidas, protege el ciclo de credenciales y aplica MFA cuando el riesgo lo justifique.


**Escenario aplicado.** La autenticación verifica identidad y protege credenciales; el servidor limita intentos, aplica expiración y evita enumeración de usuarios.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué controles ayudan a proteger el endpoint de autenticación?

**Práctica y evidencia:** Implementa autenticación con contraseñas hasheadas y respuesta uniforme ante credenciales inválidas. **Evidencia:** comprueba que nunca se almacena contraseña en claro.

#### 15.5.02 — Authorization
Authorization comprueba permisos sobre operaciones y recursos después de identificar al sujeto. Aplica mínimo privilegio y validación a nivel de objeto para prevenir acceso horizontal o vertical no autorizado.


**Escenario aplicado.** Un usuario autenticado intenta leer un recurso ajeno. La autorización valida propiedad y permisos por objeto, no solo si existe un token.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué el control de acceso debe comprobar el recurso específico?

**Práctica y evidencia:** Aplica autorización por recurso después de autenticar al usuario. **Evidencia:** demuestra que un usuario no accede a datos de otro modificando un identificador.

#### 15.5.03 — Passport
Passport es middleware de autenticación extensible mediante estrategias. Configura estrategia, callbacks y sesión con cuidado; valida issuer/audience cuando uses tokens y no confundas que una estrategia autentique con autorización de negocio.


**Escenario aplicado.** Passport delega estrategias de autenticación, pero la aplicación debe configurar validación, callbacks y errores correctamente. Instalar una estrategia no protege rutas automáticamente.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué configuración convierte una estrategia Passport en un control efectivo?

**Práctica y evidencia:** Configura Passport con estrategia adecuada y valida credenciales en servidor. **Evidencia:** prueba éxito, fallo y manejo de sesión/token.

#### 15.5.04 — JWT
JWT puede transportar claims firmados para autenticar solicitudes. Valida algoritmo, firma, issuer, audience y expiración, limita claims y diseña revocación/rotación; la codificación Base64URL no cifra el contenido.


**Escenario aplicado.** El servidor verifica firma, algoritmo, issuer, audience y expiración de JWT. El cliente no toma decisiones de autorización basándose solo en claims decodificados.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué riesgo hay en aceptar un JWT sin verificar audiencia?

**Práctica y evidencia:** Valida JWT con firma, issuer, audience y expiración, usando algoritmo permitido. **Evidencia:** rechaza token manipulado y no registra el token completo.

#### 15.5.05 — OAuth2
OAuth2 permite autorización delegada con scopes y tokens de acceso. Selecciona flujos actuales y usa PKCE para clientes públicos; nunca solicites contraseñas del usuario para sustituir el flujo del proveedor.


**Escenario aplicado.** OAuth2 delega autorización y requiere flujos apropiados al tipo de cliente. Un cliente público usa mecanismos como PKCE en escenarios aplicables y no almacena client secret como secreto.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué una SPA no puede proteger un secreto estático?

**Práctica y evidencia:** Implementa un flujo OAuth2 de prueba y valida redirect URI, state y scopes. **Evidencia:** distingue autorización delegada de autenticación y no guarda secretos en frontend.

#### 15.5.06 — RBAC
RBAC asigna permisos mediante roles asociados a usuarios o grupos. Define roles pequeños y revisables, comprueba acceso a cada recurso y evita reglas implícitas basadas únicamente en el nombre del rol.


**Escenario aplicado.** RBAC asigna permisos mediante roles, pero el sistema necesita reglas adicionales cuando el acceso depende de propiedad, tenant o contexto.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Cuándo RBAC por sí solo no expresa la política de acceso necesaria?

**Práctica y evidencia:** Define roles y permisos y comprueba autorización en endpoints y servicios. **Evidencia:** prueba matriz de acceso y evita confiar en controles de interfaz.

#### 15.5.07 — Rate Limiting
Rate Limiting restringe frecuencia o volumen de solicitudes para proteger disponibilidad y controlar abuso. Elige clave y ventana, responde con códigos/headers adecuados y considera almacenamiento distribuido cuando hay múltiples instancias.


**Escenario aplicado.** Rate limiting se aplica por identidad y recurso además de IP cuando corresponde. Se considera proxy confiable, concurrencia y respuesta 429 para no crear bypasses.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué limitación tiene basar el rate limit únicamente en IP?

**Práctica y evidencia:** Configura rate limiting por usuario/IP con respuesta 429 y protección de rutas sensibles. **Evidencia:** prueba ventana y considera NAT o clientes detrás de proxy.

### Módulo 15.6 — Avanzado

#### 15.6.01 — WebSockets
WebSockets mantiene comunicación bidireccional y persistente entre cliente y servidor. Autentica la conexión y autoriza mensajes, valida origen, limita payloads y define reconexión, heartbeat y cierre de sesiones.


**Escenario aplicado.** Un WebSocket conserva conexión y requiere autenticar handshake, autorizar cada mensaje y limitar tamaño/frecuencia. Un usuario revocado no debe conservar acceso indefinidamente.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué la autorización debe revisarse durante una conexión persistente?

**Práctica y evidencia:** Implementa un Gateway WebSocket con autenticación, autorización por canal y límites de mensajes. **Evidencia:** prueba conexión anónima y cierre de sesión.

#### 15.6.02 — Queues
Queues permiten procesar tareas fuera del ciclo de una solicitud HTTP. Diseña reintentos, backoff, dead-letter, idempotencia y métricas; evita asumir orden o entrega exactamente una vez.


**Escenario aplicado.** Una cola entrega mensajes de forma que puede incluir duplicados. El consumidor usa identificador idempotente, reintentos limitados y dead-letter para fallos permanentes.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué no debe suponerse entrega exactamente una vez?

**Práctica y evidencia:** Publica y consume mensajes en una cola de laboratorio con ack y reintentos. **Evidencia:** demuestra idempotencia del consumidor y tratamiento de mensajes fallidos.

#### 15.6.03 — Background jobs
Background jobs ejecuta trabajos diferidos o periódicos como reportes, correos o procesamiento de archivos. Define timeout, cancelación, concurrencia y recuperación tras reinicio, y no dependas de memoria local para estado que debe persistir.


**Escenario aplicado.** Un job de fondo puede reintentarse después de timeout aunque el efecto anterior haya ocurrido. La operación necesita idempotencia, estado observable y límites de concurrencia.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué duplicación puede ocurrir si un job se reintenta sin idempotencia?

**Práctica y evidencia:** Programa un job de fondo con estado, reintentos y límite temporal. **Evidencia:** registra éxito/fallo y evita que un reintento duplique efectos.

#### 15.6.04 — Event-driven architecture
Event-driven architecture conecta componentes mediante eventos que anuncian hechos ocurridos. Define contratos versionados, entrega y orden, idempotencia y observabilidad; diferencia eventos de dominio de comandos que piden ejecutar una acción.


**Escenario aplicado.** Un evento de dominio expresa un hecho ya ocurrido y desacopla productores/consumidores. El contrato y versionado deben ser explícitos para no romper consumidores.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué diferencia hay entre evento de dominio y una orden dirigida a un servicio?

**Práctica y evidencia:** Modela un flujo event-driven con productor, broker y consumidor. **Evidencia:** explica consistencia eventual, idempotencia y observabilidad.

#### 15.6.05 — Microservices
Microservices separa un sistema en servicios desplegables con límites de dominio y contratos de red. Evalúa coste operativo, consistencia distribuida, observabilidad y resiliencia; no dividas una aplicación pequeña solo por seguir una moda arquitectónica.


**Escenario aplicado.** Un microservicio aporta despliegue independiente, pero introduce red, observabilidad distribuida, consistencia eventual y gestión de fallos parciales. No se justifica por moda.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Qué coste operativo aparece al dividir un monolito en microservicios?

**Práctica y evidencia:** Separa dos servicios por capacidad de negocio y define contratos y fallos de red. **Evidencia:** justifica si microservicios aportan valor frente a un monolito modular.

#### 15.6.06 — Testing
Testing verifica comportamiento mediante pruebas unitarias, integración, contrato y extremo a extremo. Aísla dependencias externas, prueba rutas de error y seguridad, y ejecuta suites en CI; una prueba que solo comprueba status 200 es insuficiente.



**Escenario aplicado.** Una suite combina pruebas unitarias, integración y extremo a extremo. Las dependencias externas se aíslan, pero las pruebas críticas de persistencia y seguridad usan entornos representativos.

**Criterio de análisis.** La respuesta debe justificar el diseño y señalar al menos una prueba o evidencia reproducible. **Pregunta de comprensión:** ¿Por qué una prueba unitaria no demuestra que una integración real funcione?

**Práctica y evidencia:** Escribe pruebas unitarias de servicios y pruebas de integración de rutas y persistencia. **Evidencia:** registra comandos, entorno, resultados y casos cubiertos.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 53 orientaciones genéricas por explicaciones específicas. Se desarrollaron el runtime Node/V8, event loop y streams, Express, módulos/providers/guards/interceptors/pipes de NestJS, persistencia SQL/NoSQL, seguridad de identidad, OAuth2/JWT/RBAC, colas, jobs, microservicios y pruebas.

**Revisión interna:** 53/53 entradas desarrolladas y cotejadas con el roadmap. Se añadieron límites de concurrencia, validación en runtime, idempotencia, autorización por recurso, control de archivos/configuración y manejo de errores. Pendiente: fijar versiones exactas de Node/Nest/Express/ORMs, ejecutar pruebas automatizadas e integración, revisar migraciones y verificar flujos de autenticación en entorno aislado. No se declara ejecución ni aprobación externa.
