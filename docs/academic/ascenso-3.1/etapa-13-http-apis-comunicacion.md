# Etapa 13 — Internet, HTTP, APIs y comunicación entre sistemas

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** comprender cómo se comunican las aplicaciones y aprender a consumir y construir APIs.  
**Proyecto oficial:** consumir tres APIs públicas y desarrollar una aplicación que combine sus datos.

## Resultados de aprendizaje
Explicar el recorrido de una solicitud web; interpretar mensajes HTTP; diseñar APIs orientadas a recursos; consumir servicios con manejo robusto de errores; reconocer estilos alternativos de comunicación; y aplicar controles básicos de seguridad y documentación.

## 13.1 — Arquitectura web

### Cliente-servidor
El cliente inicia una interacción y el servidor procesa solicitudes y devuelve respuestas. El navegador interpreta recursos y presenta la interfaz; el servidor puede autenticar, aplicar reglas de negocio, consultar datos y responder. Una arquitectura puede incluir proxies, CDN, balanceadores, gateways y servicios internos. Distingue cliente, servidor, proceso, servicio, host y contenedor.

### DNS, IP y puertos
DNS resuelve nombres a registros como direcciones IP. Una dirección IP identifica una interfaz/ruta en un contexto de red; un puerto identifica un endpoint de transporte en un host. Un dominio no es una IP y una IP puede alojar muchos servicios. Comprende resolvers, caché, TTL y registros A, AAAA y CNAME. Los puertos conocidos son convenciones, no prueba de identidad.

### Hosting, HTTP, HTTPS y TLS
Hosting describe infraestructura que hace disponible una aplicación. HTTP define semántica de solicitudes y respuestas. HTTPS protege HTTP mediante TLS: aporta confidencialidad e integridad del canal y autenticación del servidor según validación del certificado. HTTPS no demuestra que una aplicación sea confiable ni corrige vulnerabilidades lógicas.

### Certificados, cookies y sesiones
Un certificado vincula una identidad con una clave pública dentro de un modelo de confianza. Verifica nombre, cadena, vigencia y propósito. Las cookies son datos que el navegador puede enviar; Secure, HttpOnly, SameSite, Path y Domain afectan su comportamiento. Una sesión es un mecanismo de estado asociado a interacciones; puede identificarse mediante cookie o token. Cookie y sesión no son sinónimos.

**Práctica:** dibuja el recorrido desde una URL hasta la respuesta: DNS, conexión, TLS, proxy, servidor y base de datos. Identifica responsabilidades y puntos de fallo.

## 13.2 — HTTP en profundidad

### Requests y responses
Una solicitud contiene método, destino, protocolo, headers y opcionalmente body. La respuesta contiene estado, headers y opcionalmente body. HTTP/1.1, HTTP/2 y HTTP/3 difieren en transporte/encuadre, pero conservan la semántica de alto nivel.

### Métodos
GET recupera una representación; HEAD obtiene metadatos equivalentes sin cuerpo; POST procesa la representación enviada; PUT crea o reemplaza el estado del recurso según contrato; PATCH aplica modificación parcial; DELETE solicita eliminar la asociación/representación; OPTIONS consulta opciones y participa en CORS preflight. Estudia seguridad e idempotencia: repetir una operación idempotente conserva el mismo efecto previsto, aunque la respuesta no tenga que ser idéntica.

### Headers, body y status codes
Headers como Content-Type, Accept, Authorization, Cache-Control, ETag y Location comunican metadatos. Content-Type describe el cuerpo enviado; Accept indica formatos que el cliente puede procesar. Familias: 1xx informativo, 2xx éxito, 3xx redirección, 4xx problema de solicitud/cliente, 5xx problema de servidor. Estudia 200, 201, 202, 204, 301, 302, 304, 400, 401, 403, 404, 405, 409, 413, 415, 422, 429, 500, 502, 503 y 504. Respeta el contrato concreto.

### Authorization, caché y statelessness
Authorization transporta credenciales según esquema; nunca registres su valor en logs ordinarios. La caché utiliza Cache-Control, Expires, ETag, Last-Modified y solicitudes condicionales. No almacenes datos sensibles en cachés compartidas. HTTP es stateless en su semántica básica; las aplicaciones pueden construir estado mediante sesiones, cookies, tokens o almacenamiento.

**Práctica:** inspecciona solicitudes en DevTools o un cliente HTTP. Registra método, URL, headers relevantes, código, tipo de contenido, caché y error; elimina tokens y datos personales.

## 13.3 — APIs

### Concepto, tipos y REST
Una API es un contrato de interacción entre componentes. Pública, privada e interna describen audiencia/acceso, no calidad ni seguridad. REST es un estilo arquitectónico con restricciones; no toda API HTTP es REST. Modela recursos con nombres estables, representaciones y relaciones claras.

Ejemplo ilustrativo:
- GET /api/v1/products
- GET /api/v1/products/{id}
- POST /api/v1/products
- PATCH /api/v1/products/{id}
- DELETE /api/v1/products/{id}

El contrato debe definir autorización, validación, errores, concurrencia y compatibilidad.

### JSON, XML y serialización
JSON representa objetos, arrays, strings, números, booleanos y null. XML utiliza elementos y atributos y aparece en integraciones específicas o heredadas. Serialización transforma datos a una representación transferible; deserialización reconstruye estructuras. Nunca confíes ciegamente en datos externos deserializados.

### CRUD, paginación, filtros y versionado
CRUD resume crear, leer, actualizar y eliminar, pero no sustituye diseño HTTP. Paginación offset/limit es simple; cursores suelen ser más estables en conjuntos cambiantes. Define límites y orden determinista. Valida filtros y ordenamientos mediante allowlists. Versiona cuando exista incompatibilidad real; documenta deprecación y transición, sin cambiar silenciosamente campos.

**Práctica:** diseña un contrato OpenAPI de products con operaciones, esquemas, respuestas de error, paginación y validaciones.

## 13.4 — Consumo de APIs

Fetch es una API nativa; Axios es una biblioteca con configuración y capacidades propias. Selecciona por necesidades. Centraliza base URL, serialización, cancelación, headers y normalización de errores sin ocultar detalles. Postman, Insomnia y Thunder Client permiten construir colecciones; no guardes credenciales reales en repositorios.

Distingue errores de red, cancelación, timeout, HTTP no exitoso, parseo y validación de negocio. Presenta mensajes comprensibles y conserva detalles técnicos en registros controlados. No muestres stack traces, SQL ni secretos al usuario.

Una API puede usar sesión, API key, bearer token, OAuth u otros esquemas. Transmite credenciales solo por canales protegidos. Los tokens tienen alcance y expiración; evita almacenarlos en localStorage por defecto sin análisis de amenaza. No implementes OAuth casero cuando exista una biblioteca mantenida apropiada.

**Práctica:** crea una colección para las tres APIs del proyecto, con casos exitosos y errores 400/401/404/429, variables no secretas y pruebas de estructura.

## 13.5 — Otros estilos de comunicación

- **GraphQL:** esquema tipado, queries, mutations y resolvers. Controla profundidad, coste, autorización y acceso a datos; no elimina problemas de rendimiento.
- **WebSockets:** canal bidireccional persistente. Requiere autenticación, autorización por mensaje, control de origen, límites, reconexión y gestión de desconexiones.
- **gRPC:** RPC que suele utilizar Protocol Buffers y HTTP/2. Considera generación de código, compatibilidad de esquemas, streaming y observabilidad.
- **Webhooks:** notificaciones HTTP emitidas por eventos. Valida firma, controla repetición, procesa idempotentemente y responde rápido.
- **Server-Sent Events:** flujo unidireccional servidor-cliente sobre HTTP. Considera reconexión, Last-Event-ID, autenticación y límites de proxy.

**Práctica:** compara REST, GraphQL, WebSockets, gRPC, webhooks y SSE para cinco escenarios; justifica por dirección del flujo, latencia, complejidad, compatibilidad y seguridad.

## 13.6 — Seguridad

### CORS
CORS es un mecanismo del navegador para controlar si una página puede leer respuestas de otro origen. No es autenticación ni firewall. Configura orígenes, métodos y headers explícitamente. No reflejes cualquier Origin ni uses comodines de forma incompatible con credenciales.

### API keys y JWT
Una API key identifica una aplicación/cliente según el diseño, pero no sustituye autorización de usuario. Limita alcance, rota y revoca. JWT es un formato de token con claims y firma/protección criptográfica según perfil. Verifica algoritmo permitido, firma, issuer, audience, expiración y claims requeridos. Firmar no cifra el contenido; no incluyas secretos.

### Cookies, refresh tokens y rate limiting
Evalúa HttpOnly, Secure, SameSite, expiración y protección CSRF. Refresh tokens requieren almacenamiento, rotación y revocación cuidadosos. Rate limiting puede aplicarse por identidad, credencial, recurso u origen. Responde con semántica coherente, por ejemplo 429 y Retry-After. No confíes ciegamente en headers de IP aportados por clientes.

**Práctica defensiva:** revisa una API local propia: CORS, autenticación, autorización por recurso, secretos, validación, rate limiting y errores. No pruebes sistemas ajenos sin autorización.

## 13.7 — Documentación

OpenAPI describe operaciones, parámetros, cuerpos, respuestas, esquemas y mecanismos de seguridad de una API HTTP. La especificación debe corresponder al comportamiento real. Swagger es un ecosistema de herramientas para describir, visualizar y probar APIs; no es sinónimo de toda la especificación OpenAPI.

Las colecciones Postman agrupan solicitudes de prueba, pero no reemplazan necesariamente un contrato formal. Versiona el contrato junto al código y revisa cambios incompatibles antes de publicar.

**Práctica:** documenta una API con OpenAPI y compara al menos tres operaciones con respuestas reales del servidor.

## Proyecto oficial — Aplicación que combina tres APIs públicas

Selecciona tres APIs con uso legítimo, documentación, condiciones de uso y disponibilidad razonables. Registra proveedor, finalidad, datos, autenticación/coste, límites, privacidad, sandbox y estrategia ante fallos. No elijas servicios que exijan exponer datos personales o credenciales. No hagas scraping cuando exista API oficial.

### Requisitos
1. Interfaz que combine información relacionada de tres fuentes.
2. Adaptador separado por proveedor.
3. Validación y normalización a modelo interno.
4. Manejo de fallos parciales.
5. Estados loading, empty, stale y error.
6. Límites y reintentos con backoff según contrato.
7. Caché respetando términos y frescura.
8. Secretos privados solo en servidor.
9. Documentación de arquitectura y decisiones.
10. Fixtures para que las pruebas no dependan de Internet.

### Entregables
Repositorio y README; diagrama de secuencia; matriz comparativa de APIs; contrato interno; colección y OpenAPI si existe backend propio; pruebas de éxito, error, límite y timeout; informe de privacidad y seguridad; limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Arquitectura web y HTTP | 15 |
| Diseño de API y recursos | 15 |
| Integración de tres APIs | 20 |
| Errores y resiliencia | 15 |
| Seguridad y privacidad | 15 |
| OpenAPI y colección | 10 |
| Pruebas y reproducibilidad | 10 |

Criterio orientativo: 80/100 y sin exposición de secretos, uso no autorizado de datos ni fallo crítico de autorización.

## Autoevaluación
1. Diferencia DNS, IP y puerto.
2. ¿Qué aporta TLS y qué no garantiza?
3. Diferencia Content-Type y Accept.
4. ¿Qué significa idempotencia HTTP?
5. ¿Por qué una API HTTP no es automáticamente REST?
6. ¿Qué paginación conviene para datos que cambian?
7. ¿Qué tipos de error debe distinguir un cliente?
8. Diferencia API key y autorización de usuario.
9. ¿Por qué CORS no protege frente a clientes que no son navegadores?
10. ¿Qué controles necesita un webhook?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán solo tras confirmar audio hablado en español y relación directa con el subtema. No se asignará un curso genérico a HTTP, OAuth, CORS, WebSockets y OpenAPI como si cubriera todo.

## Referencias oficiales
- RFC 9110 — HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- RFC 9112 — HTTP/1.1: https://www.rfc-editor.org/rfc/rfc9112
- RFC 8446 — TLS 1.3: https://www.rfc-editor.org/rfc/rfc8446
- RFC 9113 — HTTP/2: https://www.rfc-editor.org/rfc/rfc9113
- RFC 9114 — HTTP/3: https://www.rfc-editor.org/rfc/rfc9114
- WHATWG Fetch: https://fetch.spec.whatwg.org/
- MDN HTTP: https://developer.mozilla.org/en-US/docs/Web/HTTP
- MDN CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- OpenAPI: https://spec.openapis.org/oas/latest.html
- GraphQL: https://spec.graphql.org/
- WebSocket RFC 6455: https://www.rfc-editor.org/rfc/rfc6455
- gRPC: https://grpc.io/docs/
- Server-Sent Events: https://html.spec.whatwg.org/multipage/server-sent-events.html
- OWASP API Security Top 10: https://owasp.org/www-project-api-security/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se han consumido APIs externas ni ejecutado pruebas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 13

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados desarrollan las lecciones a partir del contenido conceptual de esta guía; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 13.1 — Arquitectura web

#### 13.1.01 — Cliente-servidor
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.02 — Navegador
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.03 — Servidor
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.04 — DNS
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.05 — IP
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.06 — Puertos
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.07 — Hosting
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.08 — HTTP
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.09 — HTTPS
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.10 — TLS
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.11 — Certificados
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.12 — Cookies
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.1.13 — Sesiones
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de arquitectura web. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.2 — HTTP en profundidad

#### 13.2.01 — Requests
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.02 — Responses
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.03 — Métodos
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.04 — Headers
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.05 — Body
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.06 — Status codes
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.07 — Content-Type
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.08 — Authorization
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.09 — Caching
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.10 — Idempotencia
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.2.11 — Statelessness
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de http en profundidad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.3 — APIs

#### 13.3.01 — Qué es una API
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.02 — API pública
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.03 — API privada
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.04 — API REST
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.05 — Endpoints
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.06 — Resources
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.07 — JSON
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.08 — XML (introducción)
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.09 — Serialización
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.10 — Deserialización
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.11 — CRUD
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.12 — Paginación
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.13 — Filtrado
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.3.14 — Versionado
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.4 — Consumo de APIs

#### 13.4.01 — Fetch
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.02 — Axios
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.03 — Postman
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.04 — Insomnia
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.05 — Thunder Client
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.06 — Manejo de errores
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.07 — Autenticación
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.08 — Headers
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.09 — Tokens
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.4.10 — Documentación
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de consumo de apis. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.5 — Otros estilos de comunicación

#### 13.5.01 — GraphQL
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de otros estilos de comunicación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.5.02 — WebSockets
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de otros estilos de comunicación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.5.03 — gRPC
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de otros estilos de comunicación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.5.04 — Webhooks
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de otros estilos de comunicación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.5.05 — Server-Sent Events
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de otros estilos de comunicación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.6 — Seguridad

#### 13.6.01 — CORS
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.6.02 — API Keys
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.6.03 — JWT
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.6.04 — Cookies seguras
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.6.05 — Refresh tokens
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.6.06 — Rate limiting
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de seguridad. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

### Módulo 13.7 — Documentación

#### 13.7.01 — OpenAPI
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de documentación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.7.02 — Swagger
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de documentación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.7.03 — Postman Collections
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de documentación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.

#### 13.7.04 — API versioning
Identificar el concepto, explicar su función y reconocer cómo se aplica dentro de documentación. Relacionarlo con las decisiones de diseño, implementación y mantenimiento del proyecto de la etapa.
