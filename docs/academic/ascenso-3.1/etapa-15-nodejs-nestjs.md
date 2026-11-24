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
