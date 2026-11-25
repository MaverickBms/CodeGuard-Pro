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


**Caso de aplicación.** Una aplicación móvil consulta un servicio de inventario y recibe datos estructurados. El móvil actúa como cliente aunque no sea navegador; el servicio que procesa la solicitud es el servidor lógico, aunque se ejecute en infraestructura compartida.

**Criterio y comprobación.** El diagrama identifica iniciador, proveedor, protocolo y límites de confianza. ¿Puede un servidor actuar como cliente de otro servicio en la misma operación?

**Práctica y evidencia:** Dibuja una solicitud desde un navegador hasta un servicio web y la respuesta de retorno. **Evidencia:** identifica cliente, servidor, protocolo y límites de confianza.

#### 13.1.02 — Navegador
El navegador obtiene recursos, interpreta HTML/CSS, ejecuta JavaScript y aplica políticas de seguridad de origen. Usa sus herramientas de desarrollo para inspeccionar solicitudes, consola, almacenamiento y errores sin asumir que el comportamiento local representa todos los navegadores.


**Caso de aplicación.** Una página carga correctamente el HTML pero falla al recuperar un recurso de API. Network permite separar error de transporte, respuesta HTTP y error posterior de JavaScript.

**Criterio y comprobación.** El registro diferencia solicitud, respuesta y error de consola sin exponer cookies ni tokens. ¿Por qué una respuesta 200 no garantiza que la interfaz haya procesado correctamente los datos?

**Práctica y evidencia:** Inspecciona una solicitud generada por el navegador en DevTools, pestaña Network. **Evidencia:** registra URL, método, estado y recursos cargados.

#### 13.1.03 — Servidor
Un servidor recibe solicitudes y ofrece recursos o servicios mediante procesos y puertos. Distingue servidor físico, sistema operativo, proceso de aplicación y servidor HTTP; limita interfaces de administración y expón solo los servicios necesarios.


**Caso de aplicación.** Una aplicación escucha solo en loopback durante desarrollo y no es accesible desde la red. La dirección de escucha, firewall y publicación determinan la exposición; abrir el puerto no debe ser el primer paso de diagnóstico.

**Criterio y comprobación.** Se identifica proceso, socket y dirección de escucha. ¿Qué diferencia hay entre un servicio escuchando en localhost y uno expuesto en todas las interfaces?

**Práctica y evidencia:** Levanta un servidor local de prueba y realiza una solicitud desde otro proceso cliente. **Evidencia:** identifica puerto de escucha, proceso y respuesta.

#### 13.1.04 — DNS
DNS traduce nombres de dominio a registros como A, AAAA, CNAME y MX mediante una jerarquía distribuida y cachés. Comprende TTL, resolución recursiva/autoritativa y propagación; DNS no cifra por sí solo el contenido de las conexiones.


**Caso de aplicación.** Un cambio de dirección IP no se refleja inmediatamente en todos los clientes debido a TTL y cachés. La investigación compara respuesta autoritativa, resolvedor recursivo y caché local antes de atribuirlo a propagación.

**Criterio y comprobación.** La práctica identifica tipo de registro y TTL. ¿Por qué dos clientes pueden resolver temporalmente un mismo nombre a direcciones diferentes?

**Práctica y evidencia:** Consulta registros A, AAAA y CNAME de un dominio de laboratorio con una herramienta DNS. **Evidencia:** explica resolución y TTL sin confundir DNS con HTTP.

#### 13.1.05 — IP
IP identifica interfaces y permite enrutar paquetes entre redes. IPv4 e IPv6 tienen tamaños y mecanismos distintos; una dirección puede ser privada, pública, dinámica o asignada a una interfaz, y no identifica necesariamente a una persona.


**Caso de aplicación.** Un servidor tiene una dirección privada en su interfaz y una dirección pública de salida proporcionada por NAT. No son necesariamente iguales ni permiten identificar de forma individual a una persona.

**Criterio y comprobación.** El diagrama diferencia interfaz, destino y traducción. ¿Qué información adicional se necesita para interpretar una dirección IP observada en un log?

**Práctica y evidencia:** Inspecciona direcciones locales y rutas de la máquina que ejecuta el servidor. **Evidencia:** diferencia IP de interfaz, IP de destino y dirección pública observada.

#### 13.1.06 — Puertos
Un puerto identifica un punto lógico de comunicación de transporte en TCP o UDP. El número de puerto por sí solo no confirma qué servicio está activo; comprueba protocolo, proceso, reglas de red y exposición real.


**Caso de aplicación.** Un escaneo autorizado muestra un puerto abierto, pero eso no basta para identificar de forma fiable el producto o su versión. Se correlaciona socket, PID, servicio y configuración del host.

**Criterio y comprobación.** El inventario asocia protocolo, puerto, proceso y regla de red. ¿Por qué un mismo número de puerto puede existir en TCP y UDP?

**Práctica y evidencia:** Consulta sockets en escucha y relaciona puertos con procesos en un entorno propio. **Evidencia:** explica por qué un puerto identifica un punto de comunicación y no una aplicación por sí solo.

#### 13.1.07 — Hosting
Hosting proporciona infraestructura y servicios para publicar aplicaciones o sitios. Compara recursos, disponibilidad, copias, TLS, soporte, residencia de datos y responsabilidad operativa; la contratación no sustituye la configuración segura del servicio.


**Caso de aplicación.** Un equipo compara hosting compartido con VPS para una aplicación que maneja datos personales. La decisión contempla aislamiento, copias verificadas, soporte, residencia de datos y responsabilidad por parches.

**Criterio y comprobación.** La matriz pondera control, coste y operación. ¿Qué responsabilidades siguen siendo del equipo aunque el proveedor administre la plataforma?

**Práctica y evidencia:** Compara hosting compartido, VPS, dedicado y plataforma administrada para una aplicación de prueba. **Evidencia:** justifica la opción por control, aislamiento, coste y responsabilidad operativa.

#### 13.1.08 — HTTP
HTTP define un protocolo de aplicación basado en mensajes de solicitud y respuesta. Estudia métodos, recursos, headers, códigos de estado y semántica de caché; HTTP no implica cifrado si no se protege mediante TLS.


**Caso de aplicación.** Un cliente solicita un recurso sin cifrado y un observador de red puede leer contenido de la comunicación. La práctica distingue semántica HTTP de la protección que aporta TLS.

**Criterio y comprobación.** El análisis separa método, destino, headers, estado y body. ¿Qué parte del intercambio define HTTP y qué protección no ofrece por sí solo?

**Práctica y evidencia:** Captura una petición HTTP de prueba y analiza línea inicial, cabeceras y respuesta. **Evidencia:** explica el intercambio sin confundir HTTP con el transporte subyacente.

#### 13.1.09 — HTTPS
HTTPS es HTTP transportado sobre una conexión protegida con TLS y validación de identidad del servidor. Comprueba certificado, nombre de host y cadena de confianza; el candado no garantiza que el sitio sea legítimo o que su aplicación sea segura.


**Caso de aplicación.** El certificado de un sitio es válido para otro nombre de dominio. Aunque la conexión esté cifrada, la validación de identidad debe fallar por desajuste del nombre.

**Criterio y comprobación.** La revisión verifica SAN, cadena y vigencia. ¿Por qué el cifrado de una conexión no demuestra que el servidor sea el destinatario esperado?

**Práctica y evidencia:** Compara una URL HTTP con HTTPS y verifica el certificado del servidor de prueba. **Evidencia:** explica qué protege TLS y qué información sigue visible en metadatos de conexión.

#### 13.1.10 — TLS
TLS proporciona confidencialidad, integridad y autenticación del canal mediante negociación criptográfica y certificados. Utiliza versiones y suites modernas soportadas por plataformas mantenidas; evita describir TLS como cifrado de extremo a extremo de toda la aplicación.


**Caso de aplicación.** Un cliente negocia una versión de TLS soportada por ambas partes y valida el certificado. Los metadatos de red, como IP y ciertos parámetros de conexión, no quedan ocultos necesariamente.

**Criterio y comprobación.** El informe identifica versión y certificado sin inferir seguridad absoluta. ¿Qué protege TLS y qué límites permanecen fuera del canal cifrado?

**Práctica y evidencia:** Inspecciona una negociación TLS en una herramienta de diagnóstico autorizada. **Evidencia:** identifica versión, certificado y parámetros negociados sin recomendar versiones obsoletas.

#### 13.1.11 — Certificados
Los certificados digitales vinculan una identidad con una clave pública y son validados mediante una cadena de confianza. Revisa sujeto/SAN, emisor, vigencia y revocación; nunca aceptes advertencias de certificado como una solución permanente.


**Caso de aplicación.** Un certificado está dentro de su periodo de validez, pero su SAN no incluye el hostname solicitado. La aplicación debe rechazar la conexión en vez de ignorar la advertencia.

**Criterio y comprobación.** Se documentan sujeto, SAN, emisor, vigencia y resultado de validación. ¿Por qué la fecha válida no basta para aceptar un certificado?

**Práctica y evidencia:** Examina la cadena de certificados de un dominio propio o de documentación. **Evidencia:** identifica sujeto, emisor, SAN, vigencia y validación de nombre.

#### 13.1.12 — Cookies
Las cookies permiten que el navegador almacene y envíe pequeños datos según dominio, ruta y políticas. Comprende `Secure`, `HttpOnly`, `SameSite`, `Path`, `Domain` y expiración; evita guardar secretos innecesarios y protege contra CSRF según el flujo.


**Caso de aplicación.** Una cookie de sesión se envía en una conexión HTTPS y no debe ser accesible a JavaScript. Secure y HttpOnly limitan canales distintos; SameSite contribuye a mitigar ciertos escenarios CSRF, pero no sustituye todas las defensas.

**Criterio y comprobación.** La configuración justifica Secure, HttpOnly, SameSite y Path. ¿Qué riesgo reduce HttpOnly y cuál no elimina?

**Práctica y evidencia:** Configura una cookie de prueba con Secure, HttpOnly, SameSite y Path adecuados. **Evidencia:** demuestra el alcance y explica por qué una cookie no debe contener credenciales en claro.

#### 13.1.13 — Sesiones
Una sesión mantiene contexto entre solicitudes HTTP que, por diseño, no dependen de una conexión persistente. El servidor suele asociar un identificador aleatorio con estado de sesión; rota el identificador tras autenticación y revoca sesiones al cerrar o detectar riesgo.


**Caso de aplicación.** Tras autenticar, el servidor rota el identificador de sesión para evitar reutilizar el identificador previo. Al cerrar sesión, revoca el estado del lado servidor y expira la cookie del cliente.

**Criterio y comprobación.** Se demuestra rotación, expiración y revocación. ¿Por qué eliminar la cookie del navegador no siempre invalida una sesión en el servidor?

**Práctica y evidencia:** Implementa una sesión de laboratorio con identificador aleatorio y expiración. **Evidencia:** prueba rotación al autenticar, cierre de sesión e invalidación del identificador.

### Módulo 13.2 — HTTP en profundidad

#### 13.2.01 — Requests
Una request HTTP incluye método, destino, versión/protocolo, headers y opcionalmente body. Inspecciona una solicitud real y diferencia URL, query parameters, headers y contenido; nunca registres credenciales o datos personales sin necesidad y controles.


**Caso de aplicación.** Una solicitud de búsqueda contiene parámetros en query string y un token en Authorization. El equipo evita registrar el token y valida que los parámetros no sustituyan la autenticación.

**Criterio y comprobación.** El análisis ubica método, URI, query, headers y body. ¿Qué diferencias de exposición existen entre query parameters y headers?

**Práctica y evidencia:** Construye una solicitud con método, URI, cabeceras y cuerpo, y envíala a un endpoint de prueba. **Evidencia:** identifica cada parte y su función.

#### 13.2.02 — Responses
Una response HTTP contiene estado, headers y, según el caso, un body. El cliente debe interpretar código y tipo de contenido antes de procesar el cuerpo; maneja respuestas vacías, redirecciones y errores de forma explícita.


**Caso de aplicación.** El servidor devuelve 204 sin cuerpo y el cliente intenta parsear JSON, provocando un error local. El consumidor debe interpretar el estado y Content-Type antes de procesar el body.

**Criterio y comprobación.** La prueba cubre respuesta con cuerpo, vacía y de error. ¿Por qué un cliente no debe asumir que todas las respuestas contienen JSON?

**Práctica y evidencia:** Analiza una respuesta HTTP real y separa línea de estado, cabeceras y cuerpo. **Evidencia:** explica cómo el cliente interpreta el resultado.

#### 13.2.03 — Métodos
Los métodos expresan la intención de una solicitud: GET, HEAD, POST, PUT, PATCH, DELETE y otros. Distingue seguridad e idempotencia; no uses GET para modificar estado ni asumas que todos los servidores implementan métodos de la misma manera.


**Caso de aplicación.** Un cliente reintenta una solicitud tras perder la conexión. GET y PUT tienen semántica idempotente en condiciones definidas; POST puede crear recursos duplicados si no existe una estrategia de idempotencia.

**Criterio y comprobación.** La tabla distingue seguridad e idempotencia de los métodos. ¿Qué diferencia existe entre método seguro e idempotente?

**Práctica y evidencia:** Compara GET, POST, PUT, PATCH, DELETE, HEAD y OPTIONS por semántica, seguridad e idempotencia. **Evidencia:** selecciona el método adecuado para cinco operaciones.

#### 13.2.04 — Headers
Los headers transportan metadatos de negociación, autenticación, caché, representación y control. Separa headers de solicitud, respuesta y contenido; evita duplicados contradictorios y no expongas tokens en URLs o logs.


**Caso de aplicación.** Una API utiliza Content-Type para declarar formato y Authorization para credenciales. Los headers sensibles se excluyen de trazas y no se confunden con parámetros de negocio.

**Criterio y comprobación.** Se clasifican headers por función y sensibilidad. ¿Por qué un header no es automáticamente confidencial por no aparecer en la URL?

**Práctica y evidencia:** Inspecciona cabeceras como Host, Accept, Content-Type, Cache-Control y Authorization. **Evidencia:** clasifica cuáles describen contenido, negociación, caché o identidad.

#### 13.2.05 — Body
El body contiene la representación enviada o recibida, por ejemplo JSON, texto o datos binarios. Define límites de tamaño y `Content-Type`, valida estructura y codificación y no confíes en el body por el mero hecho de que el cliente lo haya enviado.


**Caso de aplicación.** Una API recibe un body JSON de gran tamaño. Debe validar tamaño, estructura, tipos y autorización antes de procesar datos, y no confiar en el cliente para las reglas de negocio.

**Criterio y comprobación.** El contrato define formato, límites y validaciones. ¿Qué diferencia hay entre validar sintaxis JSON y validar reglas de negocio?

**Práctica y evidencia:** Envía un cuerpo JSON en POST y verifica su interpretación en servidor. **Evidencia:** distingue cuerpo de solicitud, parámetros de ruta y query string.

#### 13.2.06 — Status codes
Los status codes comunican el resultado general: 2xx éxito, 3xx redirección, 4xx problema asociado a la solicitud/cliente y 5xx fallo del servidor. Selecciona códigos semánticamente correctos y no uses 200 para ocultar errores de negocio.


**Caso de aplicación.** Un servicio devuelve 401 cuando falta autenticación, 403 cuando la identidad no tiene permiso y 404 cuando el recurso no existe o se decide ocultarlo. La semántica elegida debe ser coherente y no filtrar información sensible.

**Criterio y comprobación.** La matriz relaciona escenarios con estados y cuerpo de error. ¿En qué se diferencian 401 y 403?

**Práctica y evidencia:** Clasifica códigos 2xx, 3xx, 4xx y 5xx y selecciona códigos apropiados para un endpoint. **Evidencia:** justifica diferencia entre 400, 401, 403, 404, 409 y 500.

#### 13.2.07 — Content-Type
`Content-Type` declara el tipo de medio del contenido y guía su interpretación. Comprueba que coincida con el body y utiliza tipos específicos como `application/json`; no confundas `Content-Type` con `Accept`, que expresa formatos que el cliente puede recibir.


**Caso de aplicación.** El servidor responde application/json con charset apropiado. El cliente verifica Content-Type antes de parsear y trata de forma segura tipos inesperados.

**Criterio y comprobación.** La prueba valida media type y manejo de tipos no soportados. ¿Qué problema aparece al interpretar como JSON una respuesta HTML de error?

**Práctica y evidencia:** Envía JSON y texto con Content-Type correcto y observa la negociación Accept. **Evidencia:** explica diferencia entre formato enviado y formato solicitado.

#### 13.2.08 — Authorization
Authorization transporta credenciales o pruebas de autorización según un esquema como Bearer. Envía credenciales por canal TLS, aplica scopes mínimos y valida identidad/permisos en el servidor; un token presente no significa que autorice todas las operaciones.


**Caso de aplicación.** Un endpoint exige token bearer y verifica identidad, expiración y permisos. El sistema no acepta tokens enviados por query string ni los registra en logs.

**Criterio y comprobación.** El flujo valida credencial, alcance y fallo de autorización. ¿Por qué autenticación correcta no implica autorización para cualquier recurso?

**Práctica y evidencia:** Compara autenticación básica, bearer token y cookie de sesión en un entorno de prueba. **Evidencia:** identifica cómo se transporta la credencial y qué protección requiere.

#### 13.2.09 — Caching
La caché HTTP reutiliza respuestas según directivas como `Cache-Control`, `ETag`, `Last-Modified` y `Vary`. Configura políticas distintas para contenido público y privado; evita que respuestas personalizadas queden almacenadas en cachés compartidas.


**Caso de aplicación.** Una respuesta pública puede almacenarse en caché, pero un perfil personalizado no debe compartirse entre usuarios. Cache-Control y Vary deben reflejar la sensibilidad y variación de la respuesta.

**Criterio y comprobación.** La política distingue contenido público y personalizado. ¿Qué riesgo introduce almacenar una respuesta privada en una caché compartida?

**Práctica y evidencia:** Configura Cache-Control para un recurso estático y otro personalizado. **Evidencia:** explica max-age, no-store, private y riesgos de cachear datos de usuario.

#### 13.2.10 — Idempotencia
Idempotencia significa que repetir una operación produce el mismo efecto previsto en el estado del servidor. PUT y DELETE se definen como idempotentes por semántica HTTP, mientras POST no lo es necesariamente; claves de idempotencia pueden ayudar en operaciones de creación.


**Caso de aplicación.** Un cliente pierde la respuesta después de enviar una solicitud de pago. Reintentar POST sin clave de idempotencia puede duplicar la operación; el servidor debe definir una estrategia de deduplicación y estado.

**Criterio y comprobación.** El diseño identifica clave, ventana de retención y respuesta repetida. ¿Por qué una operación de negocio puede necesitar idempotencia aunque HTTP no la garantice?

**Práctica y evidencia:** Diseña un endpoint de creación con clave de idempotencia o PUT sobre recurso conocido. **Evidencia:** demuestra que repetir una solicitud no duplica efectos no deseados.

#### 13.2.11 — Statelessness
Statelessness significa que cada solicitud contiene la información necesaria para interpretarse sin depender del estado conversacional de la conexión anterior. No prohíbe sesiones ni almacenamiento en servidor; exige que el contexto se transporte o se recupere mediante un mecanismo definido.


**Caso de aplicación.** Una API no guarda estado de sesión en la memoria del proceso para cada cliente; utiliza credenciales o un almacén compartido según el diseño. Stateless no significa que la aplicación carezca de datos persistentes.

**Criterio y comprobación.** El diagrama identifica qué contexto viaja en cada solicitud y qué estado persiste en servicios externos. ¿Qué ventaja operativa puede aportar statelessness en un despliegue escalado?

**Práctica y evidencia:** Explica por qué una API REST se diseña sin depender de estado de sesión implícito entre solicitudes. **Evidencia:** identifica qué contexto debe acompañar cada solicitud y dónde se mantiene el estado del recurso.

### Módulo 13.3 — APIs

#### 13.3.01 — Qué es una API
Una API define un contrato para que componentes o sistemas intercambien capacidades y datos. Documenta operaciones, entradas, salidas, errores, autenticación y límites; una API es una interfaz contractual, no necesariamente una URL REST.


**Escenario aplicado.** Contrato de API para pedidos: documenta operaciones, autenticación, campos, errores y límites antes de implementar.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué falla cuando el contrato omite errores y límites?

**Práctica y evidencia:** Define el contrato de una API para consultar productos, crear pedidos y consultar su estado. **Evidencia:** lista operaciones, entradas, salidas y errores.

#### 13.3.02 — API pública
Una API pública está disponible para consumidores externos bajo condiciones, límites y políticas explícitas. Revisa términos, cuotas, versiones y tratamiento de datos; pública no significa anónima, ilimitada ni libre de requisitos de autorización.


**Escenario aplicado.** API pública de meteorología: define cuota, clave opcional, términos de uso y límites de consumo; pública no significa ilimitada.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué controles siguen siendo necesarios para una API de lectura pública?

**Práctica y evidencia:** Diseña una API pública con cuotas, autenticación, documentación y política de compatibilidad. **Evidencia:** identifica riesgos de abuso y expectativas del consumidor externo.

#### 13.3.03 — API privada
Una API privada se limita a sistemas, usuarios o redes autorizadas de una organización. Aplica autenticación, autorización, segmentación y observabilidad; no dependas únicamente de que el endpoint no sea conocido públicamente.


**Escenario aplicado.** API privada de facturación: restringe consumidores por identidad de servicio, autorización y segmentación; no confíes solo en que la URL sea desconocida.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué una red privada no sustituye autenticación y autorización?

**Práctica y evidencia:** Diseña una API privada entre servicios internos y delimita quién puede invocarla. **Evidencia:** especifica autenticación de servicio, autorización y segmentación de red.

#### 13.3.04 — API REST
REST es un estilo arquitectónico que utiliza recursos, representaciones, interfaz uniforme y restricciones como statelessness. No toda API JSON es REST; diseña recursos y semántica HTTP coherentes y documenta desviaciones del estilo.


**Escenario aplicado.** Una API usa JSON y HTTP, pero mantiene estado de sesión y acciones RPC. Evalúa sus restricciones REST en vez de etiquetarla REST por el formato.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué REST no significa simplemente JSON sobre HTTP?

**Práctica y evidencia:** Evalúa una API según restricciones REST y distingue estilo arquitectónico de una simple API HTTP con JSON. **Evidencia:** analiza recursos, representaciones, interfaz uniforme y estado de aplicación.

#### 13.3.05 — Endpoints
Un endpoint es una dirección y operación concreta expuesta por una API. Documenta método, ruta, parámetros, autenticación, respuestas y errores; evita incluir datos sensibles en segmentos de URL que pueden registrarse en historial y logs.


**Escenario aplicado.** Un endpoint de actualización usa identificador en la ruta y datos editables en el body; evita credenciales y datos sensibles en la URI.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué información no conviene colocar en una URL y por qué?

**Práctica y evidencia:** Define endpoints con rutas de recursos y métodos HTTP coherentes. **Evidencia:** evita verbos innecesarios en URI y documenta códigos de respuesta.

#### 13.3.06 — Resources
Un resource representa una entidad o concepto sobre el que opera la API. Diseña identificadores estables, relaciones explícitas y representaciones adecuadas; no expongas directamente tablas internas si eso acopla el contrato público al modelo de persistencia.


**Escenario aplicado.** El modelo interno de base de datos cambia, pero la representación pública del pedido se conserva mediante una capa de API.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué ventaja aporta separar el recurso público del esquema de persistencia?

**Práctica y evidencia:** Modela recursos como clientes, pedidos y productos con identificadores estables. **Evidencia:** explica relaciones, subrecursos y límites de agregación.

#### 13.3.07 — JSON
JSON representa objetos, arrays, cadenas, números, booleanos y null mediante una sintaxis textual. Valida tipos y límites, recuerda que JSON no incluye comentarios ni fechas nativas y evita asumir que números grandes conservan precisión en todos los runtimes.


**Escenario aplicado.** Un pedido puede ser JSON válido y contener un identificador de tipo incorrecto. Distingue sintaxis, esquema y reglas de negocio.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Puede un JSON sintácticamente válido ser una solicitud inválida?

**Práctica y evidencia:** Valida un documento JSON y define esquema de campos obligatorios, opcionales y tipos. **Evidencia:** detecta un documento inválido y explica la diferencia entre sintaxis y validez de negocio.

#### 13.3.08 — XML (introducción)
XML representa datos jerárquicos mediante elementos, atributos y namespaces. Comprende esquemas y codificación; al procesar XML no confiable deshabilita entidades externas y configuraciones peligrosas para prevenir XXE y acceso no autorizado a recursos.


**Escenario aplicado.** Una integración XML usa namespaces y procesa datos externos; deshabilita entidades externas para evitar XXE.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué riesgo introduce permitir entidades externas en un parser XML?

**Práctica y evidencia:** Compara XML con JSON mediante un ejemplo equivalente y analiza namespaces y atributos. **Evidencia:** identifica contextos donde XML sigue siendo relevante y sus costes.

#### 13.3.09 — Serialización
Serialización convierte estructuras de datos a una representación transferible o almacenable, como JSON o XML. Define formatos, codificación, compatibilidad y tratamiento de valores no representables; no confundas serialización con cifrado o validación.


**Escenario aplicado.** Al serializar un objeto, define formato de fechas y decimales y excluye secretos internos que no pertenecen al contrato.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué serializar no equivale a cifrar?

**Práctica y evidencia:** Serializa un objeto de dominio a JSON con reglas explícitas para fechas, decimales e identificadores. **Evidencia:** comprueba que la representación no expone campos internos o secretos.

#### 13.3.10 — Deserialización
Deserialización reconstruye estructuras a partir de datos recibidos. Trata el contenido como no confiable, valida esquema y tamaño y evita mecanismos que instancien clases arbitrarias o ejecuten lógica al reconstruir objetos.


**Escenario aplicado.** El servidor rechaza payloads excesivos, campos desconocidos y tipos inválidos antes de persistirlos.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué deserializar objetos arbitrarios desde datos no confiables es peligroso?

**Práctica y evidencia:** Deserializa una entrada externa y valida estructura, tipos, límites y reglas de negocio antes de persistir. **Evidencia:** demuestra rechazo seguro de campos inesperados o inválidos.

#### 13.3.11 — CRUD
CRUD resume crear, leer, actualizar y eliminar recursos. Relaciona cada operación con métodos HTTP y reglas de negocio, controla concurrencia y autorización y evita que una operación de lectura revele campos no permitidos.


**Escenario aplicado.** Una petición de eliminar pedido puede implementar cancelación lógica y auditoría, no necesariamente borrado físico.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué DELETE no implica necesariamente borrar una fila de inmediato?

**Práctica y evidencia:** Mapea operaciones CRUD a métodos y endpoints de una API. **Evidencia:** explica cómo se reflejan creación, consulta, actualización y eliminación sin confundirlas con sentencias SQL concretas.

#### 13.3.12 — Paginación
La paginación limita el volumen devuelto por una consulta mediante páginas, cursores o tokens de continuación. Define orden estable, tamaño máximo y comportamiento ante cambios concurrentes; evita offsets enormes cuando la colección crece.


**Escenario aplicado.** La paginación por offset puede repetir o saltar resultados cuando se insertan registros; un cursor y orden estable reducen esa anomalía.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Qué problema produce paginar sin orden determinista?

**Práctica y evidencia:** Implementa paginación por límite/desplazamiento y analiza cuándo conviene cursor. **Evidencia:** demuestra orden estable, límites máximos y comportamiento ante cambios concurrentes.

#### 13.3.13 — Filtrado
El filtrado restringe resultados mediante criterios declarados por el consumidor. Valida campos y operadores permitidos, parametriza consultas y limita combinaciones costosas para evitar inyección y agotamiento de recursos.


**Escenario aplicado.** Los filtros aceptan solo campos y operadores permitidos y se convierten en parámetros de consulta, nunca en fragmentos SQL concatenados.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué no debe concatenarse directamente un filtro recibido?

**Práctica y evidencia:** Añade filtros validados para estado, fecha y categoría mediante parámetros de consulta. **Evidencia:** limita campos y operadores permitidos para evitar consultas arbitrarias.

#### 13.3.14 — Versionado
El versionado permite evolucionar contratos sin romper consumidores. Define política para cambios incompatibles, periodo de soporte y migración; no incrementes versiones por cambios internos que no afectan al contrato observable.


**Escenario aplicado.** Una política de versiones mantiene compatibilidad, comunica deprecación y reserva versión nueva para cambios incompatibles.

**Criterio de análisis.** La respuesta debe justificar controles, datos y consecuencias del escenario. **Pregunta de comprensión:** ¿Por qué versionar cada cambio interno crea complejidad innecesaria?

**Práctica y evidencia:** Define política de versionado de API y documenta cambios incompatibles y compatibles. **Evidencia:** muestra estrategia de transición y retirada de una versión antigua.

### Módulo 13.4 — Consumo de APIs

#### 13.4.01 — Fetch
Fetch consume recursos HTTP desde JavaScript y devuelve promesas. Comprueba `response.ok`, parsea según `Content-Type`, gestiona cancelación y errores de red y no almacenes tokens sensibles en el código fuente del cliente.


**Escenario aplicado.** Una solicitud Fetch debe tratar por separado timeout/red, respuesta 4xx/5xx y error al parsear. Comprueba response.ok antes de procesar JSON y cancela solicitudes obsoletas.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué Fetch puede resolver la promesa aunque el servidor responda 404?

**Práctica y evidencia:** Consume un endpoint con Fetch y gestiona HTTP no exitoso, red, timeout y parseo. **Evidencia:** distingue fallo de transporte de respuesta 4xx/5xx.

#### 13.4.02 — Axios
Axios es una biblioteca cliente HTTP que facilita configuración, interceptores y transformación de datos. Evalúa si el proyecto necesita la dependencia adicional, configura timeouts y evita interceptores que registren credenciales o reintenten indefinidamente.


**Escenario aplicado.** Una instancia Axios centraliza baseURL y timeout. Los interceptores no deben imprimir Authorization y los reintentos deben limitarse a operaciones seguras o protegidas por idempotencia.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué riesgo introduce un interceptor que registra todos los headers?

**Práctica y evidencia:** Implementa una solicitud Axios con configuración central, interceptores y cancelación cuando aplique. **Evidencia:** evita duplicar credenciales o registrar tokens en logs.

#### 13.4.03 — Postman
Postman permite construir solicitudes, organizar colecciones y documentar pruebas de APIs. Usa variables de entorno para endpoints y credenciales de prueba, nunca exportes secretos y diferencia una colección ejecutada de una especificación de comportamiento validada.


**Escenario aplicado.** Una colección Postman organiza pruebas de login, lectura y creación con variables de entorno. Al exportarla se revisa que no contenga tokens, cookies ni datos reales.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué debe verificarse antes de compartir una colección?

**Práctica y evidencia:** Crea una colección Postman con variables de entorno y pruebas de respuesta. **Evidencia:** exporta una colección sin secretos y documenta los asserts.

#### 13.4.04 — Insomnia
Insomnia permite explorar y probar APIs mediante solicitudes, entornos y colecciones. Mantén los entornos separados, controla secretos y registra método, headers, body y respuesta para que otra persona pueda reproducir la prueba.


**Escenario aplicado.** Un workspace Insomnia separa desarrollo y pruebas mediante entornos. La URL cambia por variable, pero las credenciales se obtienen de un mecanismo seguro y no se guardan en el repositorio.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué separar entornos reduce errores de destino y filtración?

**Práctica y evidencia:** Reproduce una solicitud en Insomnia y guarda un entorno de laboratorio con variables no sensibles. **Evidencia:** documenta método, URL, cabeceras y respuesta.

#### 13.4.05 — Thunder Client
Thunder Client integra pruebas HTTP en el editor y facilita trabajar junto al código. Guarda colecciones sin credenciales reales, documenta dependencias del entorno y no confundas una prueba manual aislada con cobertura automatizada.


**Escenario aplicado.** Thunder Client permite probar una API local, pero una solicitud manual no sustituye pruebas automatizadas ni evidencia de cobertura. Registra configuración reproducible y respuesta esperada.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué limitación tiene una colección manual como evidencia de calidad?

**Práctica y evidencia:** Utiliza Thunder Client para enviar solicitudes a un servidor local y comparar respuestas. **Evidencia:** registra configuración y resultado sin incluir tokens reales.

#### 13.4.06 — Manejo de errores
El manejo de errores distingue fallo de conexión, timeout, rechazo HTTP, respuesta inválida y error de negocio. Muestra mensajes útiles al usuario, conserva identificadores de correlación para soporte y evita filtrar stack traces o detalles internos.


**Escenario aplicado.** Un error interno devuelve un identificador de correlación y mensaje seguro; stack trace y detalles técnicos quedan en logs protegidos para soporte.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué información debe ocultarse al cliente y conservarse de forma controlada para diagnóstico?

**Práctica y evidencia:** Diseña un formato uniforme de error con código, mensaje seguro, correlación y detalles internos solo en logs protegidos. **Evidencia:** demuestra que el cliente no recibe stack traces ni secretos.

#### 13.4.07 — Autenticación
La autenticación verifica quién realiza la solicitud y debe separarse de la autorización, que decide qué puede hacer. Utiliza mecanismos mantenidos, protege credenciales y aplica controles de sesión, rotación y revocación según el riesgo.


**Escenario aplicado.** Un usuario autenticado intenta consultar un pedido de otra cuenta. El servidor reconoce su identidad, pero debe denegar el acceso por autorización de recurso.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué autenticar correctamente no autoriza acceso a todos los recursos?

**Práctica y evidencia:** Implementa autenticación de prueba y verifica identidad en servidor antes de acceder a recursos. **Evidencia:** diferencia autenticación de autorización y prueba acceso anónimo y autenticado.

#### 13.4.08 — Headers
Los headers del cliente incluyen negociación de contenido, idioma, autorización y trazabilidad. Añade solo los necesarios, respeta políticas CORS y no pongas secretos en headers que puedan copiarse a registros o herramientas compartidas.


**Escenario aplicado.** Los headers de idioma, contenido y correlación se documentan por separado de Authorization. Solo se aceptan headers necesarios y los valores se validan.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué no deben copiarse indiscriminadamente headers de una solicitud a otra?

**Práctica y evidencia:** Define cabeceras requeridas para correlación, caché, contenido y autenticación. **Evidencia:** documenta cuáles son obligatorias y cómo se validan.

#### 13.4.09 — Tokens
Los tokens representan credenciales o concesiones con alcance y vigencia definidos. Valida emisor, audiencia, expiración y firma cuando aplique; almacénalos con controles apropiados y evita registrarlos, compartirlos o incluirlos en URLs.


**Escenario aplicado.** Un token tiene emisor, audiencia, alcance y expiración. El cliente no debe asumir que decodificar un payload equivale a validar firma o permiso.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué diferencia existe entre decodificar y validar un token?

**Práctica y evidencia:** Compara tokens opacos y autocontenidos, expiración, audiencia, emisor y revocación. **Evidencia:** explica almacenamiento y transmisión seguros sin incluir tokens reales en el repositorio.

#### 13.4.10 — Documentación
La documentación de consumo explica cómo configurar entorno, autenticar, llamar operaciones y tratar errores. Incluye ejemplos sin secretos, respuestas representativas, límites y versiones; verifica que los ejemplos coincidan con el contrato desplegado.


**Escenario aplicado.** La documentación de consumo incluye precondiciones, ejemplo sin secretos, parámetros, respuesta y errores. Otra persona debe reproducir la solicitud sin consultar el código fuente.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué evidencia demuestra que la documentación es suficiente para un consumidor?

**Práctica y evidencia:** Documenta un endpoint con propósito, parámetros, esquema, ejemplos y errores. **Evidencia:** permite que otra persona reproduzca una solicitud usando solo la documentación.

### Módulo 13.5 — Otros estilos de comunicación

#### 13.5.01 — GraphQL
GraphQL permite solicitar datos mediante un esquema tipado y operaciones como query, mutation y subscription. Controla profundidad, complejidad, autorización por campo y exposición de introspección según el entorno; evita resolver datos sin límites.


**Escenario aplicado.** Una consulta GraphQL solicita campos específicos, pero profundidad y complejidad deben limitarse para evitar consultas costosas y resolver permisos por campo.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué una sola consulta GraphQL puede consumir muchos recursos?

**Práctica y evidencia:** Diseña una consulta GraphQL que solicite campos concretos y compara con endpoints REST equivalentes. **Evidencia:** explica resolvers, esquema y riesgos de consultas costosas.

#### 13.5.02 — WebSockets
WebSockets mantiene un canal bidireccional persistente después de un handshake HTTP. Define autenticación, autorización por mensaje, límites, reconexión y heartbeat; valida el origen y no asumas que el canal permanece confiable tras la conexión inicial.


**Escenario aplicado.** Un WebSocket mantiene un canal bidireccional; cada mensaje necesita validación y autorización, incluso después de autenticar el handshake inicial.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué la autenticación del handshake no basta para todos los mensajes?

**Práctica y evidencia:** Construye un intercambio WebSocket en un servidor de laboratorio y gestiona cierre/reconexión. **Evidencia:** documenta autenticación, origen permitido y límites de mensajes.

#### 13.5.03 — gRPC
gRPC utiliza contratos definidos mediante Protocol Buffers y transporte HTTP/2 para comunicación entre servicios. Es útil para APIs tipadas y streaming; documenta compatibilidad de esquemas, deadlines, errores y autenticación entre servicios.


**Escenario aplicado.** Dos servicios gRPC comparten un contrato protobuf versionado. Cambios incompatibles en campos y tipos deben gestionarse con reglas de compatibilidad y deadlines.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué ventaja ofrece un contrato tipado y qué riesgo aparece al cambiarlo sin compatibilidad?

**Práctica y evidencia:** Define un servicio gRPC con mensajes protobuf y un método RPC. **Evidencia:** explica contrato, generación de stubs y negociación de transporte.

#### 13.5.04 — Webhooks
Un webhook envía una notificación HTTP cuando ocurre un evento en un sistema. Verifica firmas, limita reintentos, soporta entregas duplicadas y procesa de forma idempotente; responde rápido y delega tareas largas a una cola.


**Escenario aplicado.** Un proveedor reenvía un webhook si no recibe respuesta. El receptor valida firma y timestamp y deduplica event_id para que una entrega repetida no duplique efectos.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué el receptor debe tolerar eventos duplicados?

**Práctica y evidencia:** Implementa un webhook receptor que valide firma, timestamp y repetición de eventos. **Evidencia:** demuestra rechazo de firma incorrecta y procesamiento idempotente.

#### 13.5.05 — Server-Sent Events
Server-Sent Events permite que el servidor envíe eventos unidireccionales al navegador mediante una conexión HTTP. Define reconexión, identificadores de evento y control de acceso; el cliente no puede enviar mensajes por el mismo canal SSE.


**Escenario aplicado.** SSE envía actualizaciones del servidor al navegador y permite reconexión mediante identificadores de evento. No ofrece un canal de escritura desde el cliente.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿En qué caso SSE es más sencillo que WebSocket y cuál es su limitación?

**Práctica y evidencia:** Construye un flujo SSE que envíe eventos unidireccionales desde servidor al navegador. **Evidencia:** compara SSE con WebSocket y explica reconexión y formato de eventos.

### Módulo 13.6 — Seguridad

#### 13.6.01 — CORS
CORS es un mecanismo del navegador que controla si un origen puede leer respuestas de otro origen. Configura orígenes, métodos y headers permitidos de forma específica; CORS no es autenticación ni impide que clientes no navegador llamen a la API.


**Escenario aplicado.** El navegador envía preflight cuando la solicitud requiere autorización CORS. La API valida origen, método y headers, pero mantiene autenticación independiente.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué CORS no bloquea llamadas directas realizadas por clientes fuera del navegador?

**Práctica y evidencia:** Configura CORS para permitir solo orígenes necesarios, métodos y cabeceras concretas. **Evidencia:** prueba solicitud preflight y explica que CORS no sustituye autenticación.

#### 13.6.02 — API Keys
Una API key identifica una aplicación o proyecto y puede servir para cuotas o control de acceso limitado. No la consideres secreto seguro si está embebida en frontend público; combina controles de servidor, restricciones y rotación.


**Escenario aplicado.** Una API key embebida en JavaScript público puede extraerse. Las claves de servidor se almacenan fuera del repositorio, limitan alcance y se rotan/revocan.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué una API key incluida en frontend no puede tratarse como secreto?

**Práctica y evidencia:** Diseña una API key de prueba con alcance, rotación, almacenamiento seguro y revocación. **Evidencia:** demuestra que la clave no se expone en código cliente ni logs.

#### 13.6.03 — JWT
JWT es un formato de token con claims codificados y, habitualmente, firma o cifrado según el perfil. Verifica algoritmo permitido, firma, emisor, audiencia y expiración; el payload firmado no está cifrado necesariamente y puede ser legible.


**Escenario aplicado.** Un JWT firmado puede ser leído por quien lo obtiene. El servidor valida algoritmo permitido, firma, emisor, audiencia y expiración antes de aceptar claims.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué protección aporta la firma y qué no oculta?

**Práctica y evidencia:** Valida un JWT comprobando firma, algoritmo permitido, issuer, audience y expiración. **Evidencia:** demuestra rechazo de token manipulado y aclara que el payload no está cifrado por defecto.

#### 13.6.04 — Cookies seguras
Las cookies seguras de sesión deben configurarse con `Secure`, `HttpOnly` y `SameSite` según el flujo. Usa TLS, limita alcance con `Path`/`Domain`, rota identificadores y añade defensas CSRF cuando la arquitectura lo requiera.


**Escenario aplicado.** Una cookie de autenticación usa Secure, HttpOnly y SameSite adecuados y la aplicación incorpora protección CSRF cuando el patrón de credenciales lo requiere.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué amenaza reduce SameSite y por qué no elimina toda necesidad de CSRF controls?

**Práctica y evidencia:** Configura cookies de autenticación con Secure, HttpOnly, SameSite y protección CSRF acorde al flujo. **Evidencia:** inspecciona atributos y prueba cierre de sesión.

#### 13.6.05 — Refresh tokens
Refresh tokens permiten obtener nuevos access tokens sin volver a autenticar al usuario en cada ciclo. Almacénalos de forma protegida, rótalos cuando corresponda, detecta reutilización y permite revocación por dispositivo o sesión.


**Escenario aplicado.** La rotación de refresh token invalida el anterior. Si se detecta reutilización de un token ya rotado, el servidor puede revocar la familia y requerir nueva autenticación.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué puede indicar la reutilización de un refresh token antiguo?

**Práctica y evidencia:** Diseña rotación de refresh tokens con detección de reutilización y revocación de familia. **Evidencia:** describe estados, almacenamiento y respuesta ante robo/reuso.

#### 13.6.06 — Rate limiting
Rate limiting restringe solicitudes por usuario, token, IP u otra clave para proteger disponibilidad y cuotas. Define ventanas y respuestas consistentes, considera proxies confiables y evita que una sola dirección compartida bloquee injustamente a muchos usuarios.


**Escenario aplicado.** El rate limiting devuelve 429 y, cuando corresponde, información de reintento. La clave de limitación considera usuarios, credenciales y proxies confiables para evitar bypass o bloqueo injusto.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué problemas surgen al limitar únicamente por IP?

**Práctica y evidencia:** Implementa un límite de solicitudes por usuario o cliente con respuesta 429 y cabeceras informativas. **Evidencia:** prueba ventana, concurrencia y bypasses por identidades compartidas.

### Módulo 13.7 — Documentación

#### 13.7.01 — OpenAPI
OpenAPI describe contratos HTTP mediante un documento estructurado que puede generar documentación, clientes y validaciones. Mantén el esquema junto al código, especifica seguridad y errores y comprueba que las rutas documentadas coincidan con la implementación.


**Escenario aplicado.** La especificación OpenAPI documenta request/response, seguridad, errores y ejemplos. La integración continua puede detectar divergencia entre contrato y código, pero el documento debe mantenerse vigente.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Por qué una especificación válida sintácticamente puede estar desactualizada respecto a la API real?

**Práctica y evidencia:** Escribe una especificación OpenAPI para un endpoint de lectura y otro de escritura. **Evidencia:** valida el documento y comprueba que ejemplos coincidan con esquemas.

#### 13.7.02 — Swagger
Swagger es un conjunto de herramientas del ecosistema OpenAPI para visualizar, editar y probar especificaciones. Distingue la especificación OpenAPI de Swagger UI/Editor y protege las interfaces interactivas en entornos no públicos.


**Escenario aplicado.** Swagger UI permite explorar y ejecutar operaciones documentadas. En producción se restringe el acceso o se configura autenticación para no exponer endpoints internos ni facilitar abuso.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué riesgos existen al dejar una interfaz interactiva de API abierta sin controles?

**Práctica y evidencia:** Utiliza Swagger UI para explorar una especificación y enviar una solicitud al entorno de prueba. **Evidencia:** documenta cómo se autentica el explorador y qué operaciones están disponibles.

#### 13.7.03 — Postman Collections
Postman Collections agrupa solicitudes, variables y scripts para reproducir flujos de API. Incluye datos de prueba no sensibles, assertions sobre status/body y documentación de precondiciones; versiona colecciones sin credenciales ni datos personales.


**Escenario aplicado.** Una colección Postman versionada contiene solicitudes y assertions, pero usa variables no sensibles y datos sintéticos. Su ejecución se registra con entorno y versión de API.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué diferencia hay entre una colección de solicitudes y una especificación contractual OpenAPI?

**Práctica y evidencia:** Organiza una colección Postman por recurso y flujo de negocio con variables no sensibles. **Evidencia:** demuestra ejecución reproducible y ausencia de credenciales incrustadas.

#### 13.7.04 — API versioning
API versioning mantiene compatibilidad mientras evolucionan rutas, representaciones o contratos. Documenta cambios deprecados, soporte y migración; usa versionado explícito y pruebas contractuales para detectar consumidores afectados antes de retirar una versión.



**Escenario aplicado.** Una política de versionado define compatibilidad, fechas de deprecación, métricas de adopción y retirada. Los consumidores reciben aviso y una ruta de migración verificable.

**Criterio de análisis.** La evidencia debe incluir configuración, resultado esperado y límites de seguridad del patrón. **Pregunta de comprensión:** ¿Qué condiciones deben cumplirse antes de retirar una versión antigua?

**Práctica y evidencia:** Documenta política de versionado, compatibilidad, deprecación y retirada para una API. **Evidencia:** crea una matriz de cambios y plan de migración para consumidores.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 63 orientaciones genéricas del desglose por explicaciones específicas de cada entrada oficial. El desarrollo cubre cliente-servidor, DNS/IP/puertos, HTTPS/TLS, semántica HTTP, APIs y contratos, serialización, paginación, consumo, estilos de comunicación, autenticación/autorización, CORS, JWT, cookies, rate limiting y OpenAPI.

**Revisión interna:** 63/63 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron advertencias sobre secretos, validación de entradas, XML externo, exposición de tokens, autorización y diferencias entre CORS y autenticación. Pendiente: probar los ejemplos contra APIs de laboratorio, validar contratos OpenAPI, verificar flujos de autenticación y ejecutar pruebas de integración con controles de seguridad. Esta revisión documental no equivale a aprobación externa ni a despliegue.
