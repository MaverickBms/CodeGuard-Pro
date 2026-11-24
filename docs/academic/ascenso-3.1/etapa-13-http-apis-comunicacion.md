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
El modelo cliente-servidor separa al consumidor de una capacidad y al sistema que la ofrece mediante un protocolo. Identifica quién inicia la solicitud, quién procesa y dónde se aplica autenticación; no presupongas que cliente siempre significa navegador.

#### 13.1.02 — Navegador
El navegador obtiene recursos, interpreta HTML/CSS, ejecuta JavaScript y aplica políticas de seguridad de origen. Usa sus herramientas de desarrollo para inspeccionar solicitudes, consola, almacenamiento y errores sin asumir que el comportamiento local representa todos los navegadores.

#### 13.1.03 — Servidor
Un servidor recibe solicitudes y ofrece recursos o servicios mediante procesos y puertos. Distingue servidor físico, sistema operativo, proceso de aplicación y servidor HTTP; limita interfaces de administración y expón solo los servicios necesarios.

#### 13.1.04 — DNS
DNS traduce nombres de dominio a registros como A, AAAA, CNAME y MX mediante una jerarquía distribuida y cachés. Comprende TTL, resolución recursiva/autoritativa y propagación; DNS no cifra por sí solo el contenido de las conexiones.

#### 13.1.05 — IP
IP identifica interfaces y permite enrutar paquetes entre redes. IPv4 e IPv6 tienen tamaños y mecanismos distintos; una dirección puede ser privada, pública, dinámica o asignada a una interfaz, y no identifica necesariamente a una persona.

#### 13.1.06 — Puertos
Un puerto identifica un punto lógico de comunicación de transporte en TCP o UDP. El número de puerto por sí solo no confirma qué servicio está activo; comprueba protocolo, proceso, reglas de red y exposición real.

#### 13.1.07 — Hosting
Hosting proporciona infraestructura y servicios para publicar aplicaciones o sitios. Compara recursos, disponibilidad, copias, TLS, soporte, residencia de datos y responsabilidad operativa; la contratación no sustituye la configuración segura del servicio.

#### 13.1.08 — HTTP
HTTP define un protocolo de aplicación basado en mensajes de solicitud y respuesta. Estudia métodos, recursos, headers, códigos de estado y semántica de caché; HTTP no implica cifrado si no se protege mediante TLS.

#### 13.1.09 — HTTPS
HTTPS es HTTP transportado sobre una conexión protegida con TLS y validación de identidad del servidor. Comprueba certificado, nombre de host y cadena de confianza; el candado no garantiza que el sitio sea legítimo o que su aplicación sea segura.

#### 13.1.10 — TLS
TLS proporciona confidencialidad, integridad y autenticación del canal mediante negociación criptográfica y certificados. Utiliza versiones y suites modernas soportadas por plataformas mantenidas; evita describir TLS como cifrado de extremo a extremo de toda la aplicación.

#### 13.1.11 — Certificados
Los certificados digitales vinculan una identidad con una clave pública y son validados mediante una cadena de confianza. Revisa sujeto/SAN, emisor, vigencia y revocación; nunca aceptes advertencias de certificado como una solución permanente.

#### 13.1.12 — Cookies
Las cookies permiten que el navegador almacene y envíe pequeños datos según dominio, ruta y políticas. Comprende `Secure`, `HttpOnly`, `SameSite`, `Path`, `Domain` y expiración; evita guardar secretos innecesarios y protege contra CSRF según el flujo.

#### 13.1.13 — Sesiones
Una sesión mantiene contexto entre solicitudes HTTP que, por diseño, no dependen de una conexión persistente. El servidor suele asociar un identificador aleatorio con estado de sesión; rota el identificador tras autenticación y revoca sesiones al cerrar o detectar riesgo.

### Módulo 13.2 — HTTP en profundidad

#### 13.2.01 — Requests
Una request HTTP incluye método, destino, versión/protocolo, headers y opcionalmente body. Inspecciona una solicitud real y diferencia URL, query parameters, headers y contenido; nunca registres credenciales o datos personales sin necesidad y controles.

#### 13.2.02 — Responses
Una response HTTP contiene estado, headers y, según el caso, un body. El cliente debe interpretar código y tipo de contenido antes de procesar el cuerpo; maneja respuestas vacías, redirecciones y errores de forma explícita.

#### 13.2.03 — Métodos
Los métodos expresan la intención de una solicitud: GET, HEAD, POST, PUT, PATCH, DELETE y otros. Distingue seguridad e idempotencia; no uses GET para modificar estado ni asumas que todos los servidores implementan métodos de la misma manera.

#### 13.2.04 — Headers
Los headers transportan metadatos de negociación, autenticación, caché, representación y control. Separa headers de solicitud, respuesta y contenido; evita duplicados contradictorios y no expongas tokens en URLs o logs.

#### 13.2.05 — Body
El body contiene la representación enviada o recibida, por ejemplo JSON, texto o datos binarios. Define límites de tamaño y `Content-Type`, valida estructura y codificación y no confíes en el body por el mero hecho de que el cliente lo haya enviado.

#### 13.2.06 — Status codes
Los status codes comunican el resultado general: 2xx éxito, 3xx redirección, 4xx problema asociado a la solicitud/cliente y 5xx fallo del servidor. Selecciona códigos semánticamente correctos y no uses 200 para ocultar errores de negocio.

#### 13.2.07 — Content-Type
`Content-Type` declara el tipo de medio del contenido y guía su interpretación. Comprueba que coincida con el body y utiliza tipos específicos como `application/json`; no confundas `Content-Type` con `Accept`, que expresa formatos que el cliente puede recibir.

#### 13.2.08 — Authorization
Authorization transporta credenciales o pruebas de autorización según un esquema como Bearer. Envía credenciales por canal TLS, aplica scopes mínimos y valida identidad/permisos en el servidor; un token presente no significa que autorice todas las operaciones.

#### 13.2.09 — Caching
La caché HTTP reutiliza respuestas según directivas como `Cache-Control`, `ETag`, `Last-Modified` y `Vary`. Configura políticas distintas para contenido público y privado; evita que respuestas personalizadas queden almacenadas en cachés compartidas.

#### 13.2.10 — Idempotencia
Idempotencia significa que repetir una operación produce el mismo efecto previsto en el estado del servidor. PUT y DELETE se definen como idempotentes por semántica HTTP, mientras POST no lo es necesariamente; claves de idempotencia pueden ayudar en operaciones de creación.

#### 13.2.11 — Statelessness
Statelessness significa que cada solicitud contiene la información necesaria para interpretarse sin depender del estado conversacional de la conexión anterior. No prohíbe sesiones ni almacenamiento en servidor; exige que el contexto se transporte o se recupere mediante un mecanismo definido.

### Módulo 13.3 — APIs

#### 13.3.01 — Qué es una API
Una API define un contrato para que componentes o sistemas intercambien capacidades y datos. Documenta operaciones, entradas, salidas, errores, autenticación y límites; una API es una interfaz contractual, no necesariamente una URL REST.

#### 13.3.02 — API pública
Una API pública está disponible para consumidores externos bajo condiciones, límites y políticas explícitas. Revisa términos, cuotas, versiones y tratamiento de datos; pública no significa anónima, ilimitada ni libre de requisitos de autorización.

#### 13.3.03 — API privada
Una API privada se limita a sistemas, usuarios o redes autorizadas de una organización. Aplica autenticación, autorización, segmentación y observabilidad; no dependas únicamente de que el endpoint no sea conocido públicamente.

#### 13.3.04 — API REST
REST es un estilo arquitectónico que utiliza recursos, representaciones, interfaz uniforme y restricciones como statelessness. No toda API JSON es REST; diseña recursos y semántica HTTP coherentes y documenta desviaciones del estilo.

#### 13.3.05 — Endpoints
Un endpoint es una dirección y operación concreta expuesta por una API. Documenta método, ruta, parámetros, autenticación, respuestas y errores; evita incluir datos sensibles en segmentos de URL que pueden registrarse en historial y logs.

#### 13.3.06 — Resources
Un resource representa una entidad o concepto sobre el que opera la API. Diseña identificadores estables, relaciones explícitas y representaciones adecuadas; no expongas directamente tablas internas si eso acopla el contrato público al modelo de persistencia.

#### 13.3.07 — JSON
JSON representa objetos, arrays, cadenas, números, booleanos y null mediante una sintaxis textual. Valida tipos y límites, recuerda que JSON no incluye comentarios ni fechas nativas y evita asumir que números grandes conservan precisión en todos los runtimes.

#### 13.3.08 — XML (introducción)
XML representa datos jerárquicos mediante elementos, atributos y namespaces. Comprende esquemas y codificación; al procesar XML no confiable deshabilita entidades externas y configuraciones peligrosas para prevenir XXE y acceso no autorizado a recursos.

#### 13.3.09 — Serialización
Serialización convierte estructuras de datos a una representación transferible o almacenable, como JSON o XML. Define formatos, codificación, compatibilidad y tratamiento de valores no representables; no confundas serialización con cifrado o validación.

#### 13.3.10 — Deserialización
Deserialización reconstruye estructuras a partir de datos recibidos. Trata el contenido como no confiable, valida esquema y tamaño y evita mecanismos que instancien clases arbitrarias o ejecuten lógica al reconstruir objetos.

#### 13.3.11 — CRUD
CRUD resume crear, leer, actualizar y eliminar recursos. Relaciona cada operación con métodos HTTP y reglas de negocio, controla concurrencia y autorización y evita que una operación de lectura revele campos no permitidos.

#### 13.3.12 — Paginación
La paginación limita el volumen devuelto por una consulta mediante páginas, cursores o tokens de continuación. Define orden estable, tamaño máximo y comportamiento ante cambios concurrentes; evita offsets enormes cuando la colección crece.

#### 13.3.13 — Filtrado
El filtrado restringe resultados mediante criterios declarados por el consumidor. Valida campos y operadores permitidos, parametriza consultas y limita combinaciones costosas para evitar inyección y agotamiento de recursos.

#### 13.3.14 — Versionado
El versionado permite evolucionar contratos sin romper consumidores. Define política para cambios incompatibles, periodo de soporte y migración; no incrementes versiones por cambios internos que no afectan al contrato observable.

### Módulo 13.4 — Consumo de APIs

#### 13.4.01 — Fetch
Fetch consume recursos HTTP desde JavaScript y devuelve promesas. Comprueba `response.ok`, parsea según `Content-Type`, gestiona cancelación y errores de red y no almacenes tokens sensibles en el código fuente del cliente.

#### 13.4.02 — Axios
Axios es una biblioteca cliente HTTP que facilita configuración, interceptores y transformación de datos. Evalúa si el proyecto necesita la dependencia adicional, configura timeouts y evita interceptores que registren credenciales o reintenten indefinidamente.

#### 13.4.03 — Postman
Postman permite construir solicitudes, organizar colecciones y documentar pruebas de APIs. Usa variables de entorno para endpoints y credenciales de prueba, nunca exportes secretos y diferencia una colección ejecutada de una especificación de comportamiento validada.

#### 13.4.04 — Insomnia
Insomnia permite explorar y probar APIs mediante solicitudes, entornos y colecciones. Mantén los entornos separados, controla secretos y registra método, headers, body y respuesta para que otra persona pueda reproducir la prueba.

#### 13.4.05 — Thunder Client
Thunder Client integra pruebas HTTP en el editor y facilita trabajar junto al código. Guarda colecciones sin credenciales reales, documenta dependencias del entorno y no confundas una prueba manual aislada con cobertura automatizada.

#### 13.4.06 — Manejo de errores
El manejo de errores distingue fallo de conexión, timeout, rechazo HTTP, respuesta inválida y error de negocio. Muestra mensajes útiles al usuario, conserva identificadores de correlación para soporte y evita filtrar stack traces o detalles internos.

#### 13.4.07 — Autenticación
La autenticación verifica quién realiza la solicitud y debe separarse de la autorización, que decide qué puede hacer. Utiliza mecanismos mantenidos, protege credenciales y aplica controles de sesión, rotación y revocación según el riesgo.

#### 13.4.08 — Headers
Los headers del cliente incluyen negociación de contenido, idioma, autorización y trazabilidad. Añade solo los necesarios, respeta políticas CORS y no pongas secretos en headers que puedan copiarse a registros o herramientas compartidas.

#### 13.4.09 — Tokens
Los tokens representan credenciales o concesiones con alcance y vigencia definidos. Valida emisor, audiencia, expiración y firma cuando aplique; almacénalos con controles apropiados y evita registrarlos, compartirlos o incluirlos en URLs.

#### 13.4.10 — Documentación
La documentación de consumo explica cómo configurar entorno, autenticar, llamar operaciones y tratar errores. Incluye ejemplos sin secretos, respuestas representativas, límites y versiones; verifica que los ejemplos coincidan con el contrato desplegado.

### Módulo 13.5 — Otros estilos de comunicación

#### 13.5.01 — GraphQL
GraphQL permite solicitar datos mediante un esquema tipado y operaciones como query, mutation y subscription. Controla profundidad, complejidad, autorización por campo y exposición de introspección según el entorno; evita resolver datos sin límites.

#### 13.5.02 — WebSockets
WebSockets mantiene un canal bidireccional persistente después de un handshake HTTP. Define autenticación, autorización por mensaje, límites, reconexión y heartbeat; valida el origen y no asumas que el canal permanece confiable tras la conexión inicial.

#### 13.5.03 — gRPC
gRPC utiliza contratos definidos mediante Protocol Buffers y transporte HTTP/2 para comunicación entre servicios. Es útil para APIs tipadas y streaming; documenta compatibilidad de esquemas, deadlines, errores y autenticación entre servicios.

#### 13.5.04 — Webhooks
Un webhook envía una notificación HTTP cuando ocurre un evento en un sistema. Verifica firmas, limita reintentos, soporta entregas duplicadas y procesa de forma idempotente; responde rápido y delega tareas largas a una cola.

#### 13.5.05 — Server-Sent Events
Server-Sent Events permite que el servidor envíe eventos unidireccionales al navegador mediante una conexión HTTP. Define reconexión, identificadores de evento y control de acceso; el cliente no puede enviar mensajes por el mismo canal SSE.

### Módulo 13.6 — Seguridad

#### 13.6.01 — CORS
CORS es un mecanismo del navegador que controla si un origen puede leer respuestas de otro origen. Configura orígenes, métodos y headers permitidos de forma específica; CORS no es autenticación ni impide que clientes no navegador llamen a la API.

#### 13.6.02 — API Keys
Una API key identifica una aplicación o proyecto y puede servir para cuotas o control de acceso limitado. No la consideres secreto seguro si está embebida en frontend público; combina controles de servidor, restricciones y rotación.

#### 13.6.03 — JWT
JWT es un formato de token con claims codificados y, habitualmente, firma o cifrado según el perfil. Verifica algoritmo permitido, firma, emisor, audiencia y expiración; el payload firmado no está cifrado necesariamente y puede ser legible.

#### 13.6.04 — Cookies seguras
Las cookies seguras de sesión deben configurarse con `Secure`, `HttpOnly` y `SameSite` según el flujo. Usa TLS, limita alcance con `Path`/`Domain`, rota identificadores y añade defensas CSRF cuando la arquitectura lo requiera.

#### 13.6.05 — Refresh tokens
Refresh tokens permiten obtener nuevos access tokens sin volver a autenticar al usuario en cada ciclo. Almacénalos de forma protegida, rótalos cuando corresponda, detecta reutilización y permite revocación por dispositivo o sesión.

#### 13.6.06 — Rate limiting
Rate limiting restringe solicitudes por usuario, token, IP u otra clave para proteger disponibilidad y cuotas. Define ventanas y respuestas consistentes, considera proxies confiables y evita que una sola dirección compartida bloquee injustamente a muchos usuarios.

### Módulo 13.7 — Documentación

#### 13.7.01 — OpenAPI
OpenAPI describe contratos HTTP mediante un documento estructurado que puede generar documentación, clientes y validaciones. Mantén el esquema junto al código, especifica seguridad y errores y comprueba que las rutas documentadas coincidan con la implementación.

#### 13.7.02 — Swagger
Swagger es un conjunto de herramientas del ecosistema OpenAPI para visualizar, editar y probar especificaciones. Distingue la especificación OpenAPI de Swagger UI/Editor y protege las interfaces interactivas en entornos no públicos.

#### 13.7.03 — Postman Collections
Postman Collections agrupa solicitudes, variables y scripts para reproducir flujos de API. Incluye datos de prueba no sensibles, assertions sobre status/body y documentación de precondiciones; versiona colecciones sin credenciales ni datos personales.

#### 13.7.04 — API versioning
API versioning mantiene compatibilidad mientras evolucionan rutas, representaciones o contratos. Documenta cambios deprecados, soporte y migración; usa versionado explícito y pruebas contractuales para detectar consumidores afectados antes de retirar una versión.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 63 orientaciones genéricas del desglose por explicaciones específicas de cada entrada oficial. El desarrollo cubre cliente-servidor, DNS/IP/puertos, HTTPS/TLS, semántica HTTP, APIs y contratos, serialización, paginación, consumo, estilos de comunicación, autenticación/autorización, CORS, JWT, cookies, rate limiting y OpenAPI.

**Revisión interna:** 63/63 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron advertencias sobre secretos, validación de entradas, XML externo, exposición de tokens, autorización y diferencias entre CORS y autenticación. Pendiente: probar los ejemplos contra APIs de laboratorio, validar contratos OpenAPI, verificar flujos de autenticación y ejecutar pruebas de integración con controles de seguridad. Esta revisión documental no equivale a aprobación externa ni a despliegue.
