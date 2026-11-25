# Etapa 25 — Seguridad de aplicaciones web y APIs

**Prioridad:** P1 para el perfil · P2 avanzado  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Enfoque:** integrar desarrollo de software y ciberseguridad.  
**Proyecto oficial:** construir una aplicación deliberadamente vulnerable en entorno local, evaluarla, documentar hallazgos y desarrollar correcciones.

## Resultados de aprendizaje
Modelar arquitectura de seguridad web; reconocer vulnerabilidades web y de API; utilizar guías OWASP; analizar solicitudes/respuestas con proxies de prueba; evaluar autenticación, autorización y tokens; y corregir vulnerabilidades con pruebas de regresión.

## 25.1 — Arquitectura de seguridad web
Una aplicación web combina cliente, frontend, backend, base de datos y APIs. Identifica límites de confianza, flujos de datos, sesiones, cookies, autenticación, autorización y TLS. Cada capa puede introducir controles y riesgos distintos. El frontend no es una frontera de seguridad: cualquier regla de acceso debe validarse en servidor.

**Ejercicio:** crea un diagrama de flujo de datos para login, consulta de datos y modificación de un recurso. Marca datos sensibles y controles en cada frontera.

## 25.2 — Vulnerabilidades web
- **SQL/NoSQL Injection:** entrada altera consultas; utiliza APIs parametrizadas, validación y construcción segura de consultas.
- **XSS:** contenido no confiable se interpreta como código activo; aplica encoding contextual y evita sinks peligrosos.
- **CSRF:** solicitudes no deseadas usan credenciales del navegador; aplica protección adecuada al tipo de sesión.
- **SSRF:** el servidor solicita destinos controlados por un atacante; restringe destinos, protocolos y acceso a redes internas.
- **IDOR/Broken Access Control:** identificadores manipulables exponen objetos; autoriza cada operación sobre el objeto.
- **Path Traversal:** rutas manipuladas acceden fuera del directorio permitido; normaliza y restringe.
- **Command Injection:** entrada modifica comandos; evita shell y utiliza APIs seguras.
- **Insecure File Upload:** archivos inesperados llegan a procesamiento; limita, valida contenido, renombra y almacena fuera de rutas ejecutables.
- **Authentication Bypass:** fallos de sesión, validación o flujo permiten acceso indebido; prueba estados, expiración, recuperación y MFA.
- **Security Misconfiguration:** configuraciones por defecto, permisos o servicios expuestos elevan riesgo; aplica hardening y revisión continua.

La práctica de vulnerabilidades se limita a aplicaciones propias o deliberadamente vulnerables en red aislada. No pruebes sistemas públicos sin autorización expresa.

## 25.3 — OWASP
OWASP Top 10:2025 aporta categorías de riesgos web; Web Security Testing Guide organiza pruebas; Secure Coding y Threat Modeling incorporan seguridad al ciclo de desarrollo. No confundas guía con certificación ni supongas que una checklist demuestra ausencia de vulnerabilidades.

Construye trazabilidad entre requisito, amenaza, control, prueba y evidencia. Prioriza correcciones según impacto y contexto.

## 25.4 — Burp Suite
Burp Suite permite observar y analizar tráfico HTTP en entornos de prueba. Comprende Proxy, HTTP history, Repeater, Intruder, Decoder, Comparer, Target y Scanner sujeto a edición/licencia. Revisa request y response, cookies, headers, parámetros y estados. Configura el scope para limitar objetivos. No interceptes tráfico de terceros ni de personas sin autorización y consentimiento.

**Ejercicio:** configura proxy local para Juice Shop en VM aislada; captura solicitudes propias, modifica una petición de prueba no destructiva y documenta el cambio de respuesta. No automatices ataques fuera del laboratorio.

## 25.5 — Seguridad de APIs
REST security incluye autenticación, autorización, validación, rate limiting, inventario y gestión de tokens. Broken Object Level Authorization permite acceso indebido a objetos; prueba autorización por objeto, no solo por endpoint. Unrestricted Resource Consumption puede provocar agotamiento; define límites por operación. Unsafe API Consumption surge al confiar en servicios externos sin validar sus respuestas.

Versiona APIs, elimina endpoints obsoletos, protege documentación y controla dependencias. Comprueba que las respuestas no expongan campos internos.

## 25.6 — Herramientas
Burp Suite y OWASP ZAP ayudan a interceptar y analizar tráfico; Postman permite construir solicitudes; OWASP Juice Shop ofrece escenarios intencionalmente vulnerables; Web Security Academy proporciona laboratorios educativos. Verifica versión, licencia, alcance y seguridad del entorno.

## Proyecto oficial — Aplicación vulnerable y remediación
### Fases
1. Diseña aplicación local con alcance y datos ficticios.
2. Documenta arquitectura y modelo de amenazas.
3. Introduce un conjunto acotado de vulnerabilidades didácticas.
4. Evalúa únicamente dentro de red aislada.
5. Registra evidencias sanitizadas y severidad contextual.
6. Corrige cada causa raíz.
7. Añade pruebas automatizadas de regresión.
8. Revisa autenticación, autorización por objeto, tokens y límites.
9. Ejecuta análisis estático/dinámico apropiado al entorno.
10. Documenta riesgos residuales y restauración.

### Entregables
Diagrama de arquitectura, modelo de amenazas, alcance, inventario de hallazgos, evidencias sin secretos, commits de corrección, pruebas de regresión e informe.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Arquitectura y modelo de amenazas | 15 |
| Identificación y análisis de fallos | 20 |
| Uso responsable de herramientas | 10 |
| Seguridad de APIs | 15 |
| Remediación | 20 |
| Pruebas de regresión | 15 |
| Informe y trazabilidad | 5 |

Criterio orientativo: 80/100; el laboratorio debe permanecer aislado y no debe utilizarse contra sistemas ajenos.

## Autoevaluación
1. ¿Por qué el frontend no es una frontera de autorización?
2. Diferencia SQL injection y XSS.
3. ¿Cómo mitigarías SSRF?
4. ¿Qué prueba demuestra una falla BOLA?
5. ¿Por qué el upload requiere validación de contenido?
6. ¿Qué aporta OWASP WSTG frente a OWASP Top 10?
7. ¿Para qué sirve Repeater en un laboratorio?
8. ¿Qué riesgos presenta Intruder si se utiliza fuera de scope?
9. ¿Qué límites reducen consumo abusivo de API?
10. ¿Cómo demostrarías que una corrección no regresó?

## Recursos audiovisuales
No se aprueban videos en esta versión. Se añadirán solo con audio hablado en español y correspondencia directa con el tema. Las demostraciones ofensivas deberán permanecer en aplicaciones de entrenamiento autorizadas.

## Referencias oficiales
- OWASP Top 10:2025: https://owasp.org/Top10/2025/
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP API Security Top 10: https://owasp.org/API-Security/
- Burp Suite Documentation: https://portswigger.net/burp/documentation
- Web Security Academy: https://portswigger.net/web-security
- OWASP ZAP: https://www.zaproxy.org/docs/
- OWASP Juice Shop: https://owasp.org/www-project-juice-shop/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ejecutó proxy ni laboratorio en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 25

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados son guías de estudio, no evidencias de ejecución ni autorización para evaluar sistemas de terceros.

### Módulo 25.1 — Arquitectura de seguridad web

#### 25.1.01 — Cliente-servidor
El modelo cliente-servidor separa interfaz y servicios que procesan solicitudes. Define límites de confianza y valida datos en servidor; el navegador no puede imponer autorización sobre recursos.


**Práctica y evidencia:** Dibuja el flujo navegador, servidor web, API y base de datos e identifica límites de confianza. **Evidencia:** marca validación y autorización en servidor.

#### 25.1.02 — Frontend
Frontend comprende la interfaz y lógica que se ejecuta en el navegador o cliente. Trata el código y variables enviados al navegador como públicos y no almacenes secretos ni reglas de autorización exclusivamente allí.


**Práctica y evidencia:** Inspecciona el frontend de una app de laboratorio y lista datos que nunca deben considerarse confiables por provenir del cliente. **Evidencia:** distingue controles UX de controles de seguridad.

#### 25.1.03 — Backend
Backend recibe solicitudes, aplica reglas, autentica, autoriza y accede a recursos. Valida cada operación y protege servicios internos; no confíes en identificadores o campos enviados por el cliente.


**Práctica y evidencia:** Mapea endpoints, middleware, lógica y persistencia del backend de prueba. **Evidencia:** identifica dónde se aplican autenticación y autorización.

#### 25.1.04 — Database
Database almacena información persistente y puede contener datos personales o críticos. Aplica cuentas con privilegio mínimo, consultas parametrizadas, cifrado y backups; limita acceso desde redes y aplicaciones.


**Práctica y evidencia:** Clasifica datos persistidos y define consultas parametrizadas, privilegios y respaldo. **Evidencia:** presenta esquema y reglas de acceso.

#### 25.1.05 — API
Una API define el contrato mediante el que frontend, backend u otros sistemas intercambian operaciones y datos. Documenta métodos, esquemas, errores, autenticación y límites y protege cada endpoint.


**Práctica y evidencia:** Documenta contrato API con métodos, recursos, autenticación y errores. **Evidencia:** relaciona endpoint con propietario y política de acceso.

#### 25.1.06 — Sessions
Sessions mantienen estado de autenticación o interacción entre solicitudes. Genera identificadores impredecibles, rota tras autenticación y cambios de privilegio y revoca sesiones al cerrar o detectar compromiso.


**Práctica y evidencia:** Analiza ciclo de vida de sesión y prueba expiración, rotación y cierre. **Evidencia:** demuestra invalidación de sesión anterior.

#### 25.1.07 — Cookies
Cookies transportan datos del navegador según atributos y políticas de origen. Configura Secure, HttpOnly y SameSite según el flujo y protege sesiones contra fijación y CSRF.


**Práctica y evidencia:** Configura cookies seguras y verifica atributos y alcance. **Evidencia:** prueba comportamiento en contexto de laboratorio y explica CSRF.

#### 25.1.08 — Authentication
Authentication verifica identidad mediante credenciales, sesión o proveedor federado. Protege alta, recuperación, MFA y revocación; evita revelar si una cuenta existe en mensajes de error.


**Práctica y evidencia:** Prueba autenticación con credenciales válidas, inválidas y recuperación. **Evidencia:** registra respuestas uniformes y protección frente a abuso.

#### 25.1.09 — Authorization
Authorization comprueba si una identidad puede realizar una acción sobre un recurso específico. Valida en servidor por objeto y operación y prueba accesos cruzados entre usuarios/tenants.


**Práctica y evidencia:** Construye matriz de autorización por usuario, recurso y acción. **Evidencia:** prueba acceso directo a endpoint y denegación por defecto.

#### 25.1.10 — TLS
TLS protege el canal de comunicación con confidencialidad e integridad y puede autenticar al servidor. Mantén versiones y certificados válidos, pero recuerda que TLS no corrige fallos de lógica o autorización.


**Práctica y evidencia:** Inspecciona TLS de una aplicación de laboratorio y verifica certificado, nombre y contenido mixto. **Evidencia:** registra configuración y limitaciones.

### Módulo 25.2 — Vulnerabilidades web

#### 25.2.01 — SQL Injection
SQL Injection altera consultas relacionales cuando entradas no confiables se interpretan como parte de SQL. Usa parámetros y APIs seguras, limita privilegios de DB y prueba validación con datos ficticios.


**Práctica y evidencia:** En una app deliberadamente vulnerable local, compara concatenación SQL con consulta parametrizada. **Evidencia:** confirma que la entrada se trata como dato y no ejecuta lógica SQL.

#### 25.2.02 — NoSQL Injection
NoSQL Injection manipula consultas o expresiones de bases documentales mediante entradas no validadas. Construye filtros desde esquemas permitidos, evita pasar objetos arbitrarios del cliente y valida tipos y operadores.


**Práctica y evidencia:** Analiza una consulta NoSQL de laboratorio que recibe filtros externos y aplica validación/allowlist. **Evidencia:** prueba que objetos inesperados no alteran operadores de consulta.

#### 25.2.03 — Cross-Site Scripting (XSS)
Cross-Site Scripting (XSS) ejecuta contenido activo en el navegador de una víctima bajo el origen de la aplicación. Codifica salida por contexto, sanitiza HTML permitido y usa CSP como defensa adicional.


**Práctica y evidencia:** Prueba salida de texto no confiable en contextos HTML y aplica encoding contextual. **Evidencia:** demuestra que el navegador no interpreta el contenido como script.

#### 25.2.04 — Cross-Site Request Forgery (CSRF)
Cross-Site Request Forgery (CSRF) induce al navegador a enviar solicitudes autenticadas sin intención del usuario. Usa tokens y controles de origen/SameSite apropiados; comprueba operaciones sensibles y no confíes en CORS para prevenir CSRF.


**Práctica y evidencia:** Simula una solicitud cruzada contra una app local y añade token CSRF/SameSite según el flujo. **Evidencia:** demuestra rechazo de la solicitud no autorizada.

#### 25.2.05 — Server-Side Request Forgery (SSRF)
Server-Side Request Forgery (SSRF) permite que el servidor solicite recursos elegidos indirectamente por un usuario. Restringe destinos y protocolos, bloquea redes internas/metadatos y valida direcciones después de resolución DNS.


**Práctica y evidencia:** Configura un stub de URL fetcher y prueba allowlist, bloqueo de IP privadas y redirecciones. **Evidencia:** demuestra que destinos internos no autorizados se rechazan.

#### 25.2.06 — IDOR
IDOR permite acceder o modificar objetos cambiando identificadores sin verificar autorización. Valida propiedad y tenant en cada consulta y usa pruebas con identidades ficticias para detectar accesos cruzados.


**Práctica y evidencia:** Usa dos cuentas de prueba y modifica un identificador de objeto en una petición. **Evidencia:** comprueba autorización del lado servidor y ausencia de acceso cruzado.

#### 25.2.07 — Broken Access Control
Broken Access Control aparece cuando el servidor no aplica políticas de acceso en rutas, funciones o datos. Centraliza autorización, aplica denegación por defecto y revisa rutas alternativas y operaciones masivas.


**Práctica y evidencia:** Audita endpoints sensibles por autorización de función y objeto. **Evidencia:** documenta matriz de roles y casos denegados.

#### 25.2.08 — Path Traversal
Path Traversal manipula rutas para salir del directorio permitido y alcanzar otros archivos. Resuelve rutas canónicas, usa identificadores opacos y verifica que el destino final permanezca dentro del área autorizada.


**Práctica y evidencia:** Valida rutas y nombres de archivo mediante normalización/canonicalización en un laboratorio. **Evidencia:** demuestra rechazo de rutas fuera del directorio permitido.

#### 25.2.09 — Command Injection
Command Injection altera comandos del sistema al combinar datos no confiables con intérpretes. Evita invocar shell con cadenas concatenadas, utiliza APIs específicas y restringe argumentos y permisos.


**Práctica y evidencia:** Sustituye ejecución de shell por APIs de sistema seguras y argumentos separados. **Evidencia:** prueba entradas con metacaracteres en entorno local.

#### 25.2.10 — Insecure File Upload
Insecure File Upload permite almacenar o procesar archivos peligrosos por validación insuficiente. Limita tamaño, valida contenido real, renombra, almacena fuera del webroot y evita ejecución de archivos subidos.


**Práctica y evidencia:** Implementa carga de archivos con límite, validación de contenido, nombre generado y almacenamiento no ejecutable. **Evidencia:** prueba archivo sobredimensionado y extensión engañosa.

#### 25.2.11 — Authentication Bypass
Authentication Bypass ocurre cuando se omiten o manipulan controles de identidad. Revisa rutas alternativas, lógica de sesión, recuperación y configuración de middleware y valida autorización tras autenticación.


**Práctica y evidencia:** Revisa controles de autenticación y rutas alternativas de acceso en una aplicación propia. **Evidencia:** demuestra que endpoints secundarios aplican la misma política.

#### 25.2.12 — Security Misconfiguration
Security Misconfiguration incluye defaults inseguros, debugging, servicios innecesarios, CORS permisivo y headers ausentes. Mantén configuración versionada y endurecida y valida diferencias entre entornos.


**Práctica y evidencia:** Aplica checklist de configuración segura para debug, cabeceras, CORS, errores y secretos. **Evidencia:** compara perfil de desarrollo y de prueba endurecido.

### Módulo 25.3 — OWASP

#### 25.3.01 — OWASP Top 10:2025
OWASP Top 10:2025 organiza diez categorías de riesgos de aplicaciones web en una edición concreta. Usa nombres y numeración de 2025, consulta la fuente oficial y no mezcles categorías de 2021.


**Práctica y evidencia:** Relaciona controles de la aplicación con categorías OWASP Top 10:2025 verificando la publicación oficial y su fecha. **Evidencia:** registra versión/fuente y reconoce que la lista no es exhaustiva.

#### 25.3.02 — OWASP Web Security Testing Guide
OWASP Web Security Testing Guide ofrece metodología y casos de prueba para evaluar seguridad web. Selecciona pruebas según alcance y riesgo, registra versiones y limita validaciones activas a sistemas autorizados.


**Práctica y evidencia:** Selecciona pruebas del OWASP Web Security Testing Guide para una funcionalidad de laboratorio. **Evidencia:** registra sección, objetivo, precondiciones y resultado.

#### 25.3.03 — Secure Coding
Secure Coding incorpora prácticas para evitar vulnerabilidades desde implementación: validación, consultas parametrizadas, codificación de salida, gestión de secretos y dependencias seguras. Integra reglas en revisión y CI.


**Práctica y evidencia:** Revisa código de una función para validar entrada, codificar salida, controlar errores y aplicar privilegios mínimos. **Evidencia:** añade prueba de regresión para el hallazgo.

#### 25.3.04 — Threat Modeling
Threat Modeling identifica activos, actores, flujos, límites de confianza y escenarios de abuso. Documenta mitigaciones y riesgos residuales y actualiza el modelo cuando cambian endpoints o arquitectura.


**Práctica y evidencia:** Construye un modelo de amenazas para inicio de sesión y recuperación de contraseña. **Evidencia:** relaciona activos, amenazas, mitigaciones y riesgos residuales.

#### 25.3.05 — Security Testing
Security Testing verifica controles mediante análisis estático, dinámico, dependencias, configuración y pruebas manuales autorizadas. Define cobertura y limitaciones; ninguna herramienta detecta todas las vulnerabilidades.


**Práctica y evidencia:** Define un plan de pruebas de seguridad web con alcance, cuentas, datos y condiciones de parada. **Evidencia:** distingue pruebas automatizadas y revisión manual.

### Módulo 25.4 — Burp Suite

#### 25.4.01 — Proxy
Proxy de Burp Suite intercepta y permite inspeccionar tráfico HTTP entre navegador y aplicación en un laboratorio autorizado. Configura certificado y alcance con cuidado y evita interceptar cuentas o datos de terceros.


**Práctica y evidencia:** Configura un proxy interceptador solo para el navegador y servidor de laboratorio. **Evidencia:** documenta certificado local y evita interceptar tráfico de terceros.

#### 25.4.02 — HTTP History
HTTP History conserva solicitudes y respuestas observadas durante la sesión de proxy. Filtra por host y contexto, redacta secretos y usa datos de prueba para documentar comportamiento.


**Práctica y evidencia:** Inspecciona HTTP history y filtra por host, método y status. **Evidencia:** selecciona una solicitud relevante y anonimiza datos sensibles.

#### 25.4.03 — Repeater
Repeater permite modificar y reenviar solicitudes para comparar respuestas de manera controlada. Limita pruebas a endpoints autorizados, evita operaciones destructivas y registra diferencias reproducibles.


**Práctica y evidencia:** Reenvía una solicitud de laboratorio en Repeater modificando un parámetro benigno. **Evidencia:** compara respuesta y registra hipótesis sin probar sistemas externos.

#### 25.4.04 — Intruder
Intruder automatiza variaciones de solicitudes para pruebas controladas de parámetros. Configura límites y payloads no destructivos en laboratorio y evita fuerza bruta o agotamiento de recursos contra servicios reales.


**Práctica y evidencia:** Utiliza Intruder únicamente con parámetros sintéticos y un endpoint local diseñado para ello, con límites de tasa. **Evidencia:** documenta payloads ficticios y condición de parada.

#### 25.4.05 — Decoder
Decoder transforma representaciones como URL encoding, Base64 y otras codificaciones. Comprende que codificar no cifra; evita asumir que una cadena codificada es secreta.


**Práctica y evidencia:** Decodifica Base64 y URL encoding en datos sintéticos y explica que codificación no es cifrado. **Evidencia:** presenta transformación reversible.

#### 25.4.06 — Comparer
Comparer ayuda a comparar solicitudes o respuestas para identificar diferencias. Elimina datos volátiles y secretos antes de compartir resultados y explica qué diferencia es relevante para el control evaluado.


**Práctica y evidencia:** Compara dos respuestas HTTP y detecta cambios de estado, cabeceras y cuerpo. **Evidencia:** identifica diferencias relevantes sin inferir vulnerabilidad automáticamente.

#### 25.4.07 — Target
Target organiza sitios, alcance y mapa de contenido observado. Configura allowlist de hosts, revisa alcance antes de enviar tráfico y excluye sistemas de terceros.


**Práctica y evidencia:** Define scope de proyecto en Burp para incluir solo hosts del laboratorio. **Evidencia:** demuestra que destinos fuera del alcance quedan excluidos.

#### 25.4.08 — Scanner (según disponibilidad y licencia)
Scanner automatiza detección de ciertos problemas según disponibilidad, edición y licencia. Comprueba permisos y alcance, valida falsos positivos manualmente y no asumas que el escáner cubre toda la lógica de negocio.


**Práctica y evidencia:** Revisa licencia, disponibilidad y perfil de escaneo antes de usar Scanner. **Evidencia:** limita carga al laboratorio y registra falsos positivos.

#### 25.4.09 — Análisis de requests y responses
El análisis de requests y responses revisa método, ruta, headers, cookies, body, status y tiempos. Redacta credenciales y datos personales y correlaciona cada observación con el contrato esperado.


**Práctica y evidencia:** Analiza solicitud y respuesta con método, ruta, headers, cookies, body y status. **Evidencia:** identifica campo controlado por usuario y validación requerida.

### Módulo 25.5 — Seguridad de APIs

#### 25.5.01 — REST Security
REST Security protege recursos y operaciones mediante semántica HTTP, autenticación, autorización y validación. Define políticas por endpoint y objeto, limita datos expuestos y versiona contratos.


**Práctica y evidencia:** Define controles REST para autenticación, autorización, validación, transporte y errores. **Evidencia:** crea matriz por endpoint.

#### 25.5.02 — API Authentication
API Authentication verifica identidad de consumidores mediante mecanismos como OAuth, mTLS o tokens. Selecciona según tipo de cliente, protege credenciales y valida issuer/audience/expiración cuando use tokens.


**Práctica y evidencia:** Protege API con token de prueba y valida firma/expiración o introspección según diseño. **Evidencia:** prueba token inválido y expirado.

#### 25.5.03 — API Authorization
API Authorization determina qué operaciones puede realizar un consumidor sobre cada recurso. Aplica mínimo privilegio y validación por objeto, acción y tenant en el servidor.


**Práctica y evidencia:** Verifica permisos por recurso, propietario y operación en cada endpoint. **Evidencia:** demuestra que cambiar ID no permite acceso horizontal o vertical.

#### 25.5.04 — Token Management
Token Management cubre emisión, almacenamiento, expiración, rotación, revocación y auditoría de tokens. Evita incluirlos en URLs/logs y define qué hacer ante pérdida o compromiso.


**Práctica y evidencia:** Limita tamaño de solicitudes, complejidad de consulta, paginación y concurrencia. **Evidencia:** prueba límites y respuesta 429/413 apropiada.

#### 25.5.05 — API Rate Limiting
API Rate Limiting controla frecuencia y volumen de solicitudes por identidad, operación o cliente. Establece límites acordes al coste, devuelve errores consistentes y monitoriza abuso sin bloquear injustamente usuarios compartidos.


**Práctica y evidencia:** Mantén inventario de APIs, versiones, entornos y responsables. **Evidencia:** identifica endpoint obsoleto y plan de retirada.

#### 25.5.06 — API Inventory
API Inventory mantiene un registro de APIs, versiones, propietarios, exposición y datos procesados. Descubre endpoints obsoletos y shadow APIs y establece proceso para retirar servicios sin propietario.


**Práctica y evidencia:** Valida datos recibidos de APIs externas como no confiables y limita redirecciones/destinos. **Evidencia:** prueba proveedor simulado que devuelve contenido malformado.

#### 25.5.07 — Broken Object Level Authorization
Broken Object Level Authorization ocurre cuando el backend no verifica permiso sobre el objeto identificado por la solicitud. Comprueba ownership y tenant en cada acceso y prueba con cuentas ficticias separadas.


**Práctica y evidencia:** Prueba BOLA con identidades y objetos sintéticos de dos usuarios. **Evidencia:** comprueba control de propiedad en servidor.

#### 25.5.08 — Unrestricted Resource Consumption
Unrestricted Resource Consumption permite abusar de CPU, memoria, almacenamiento o servicios externos mediante solicitudes costosas. Limita tamaño, paginación, profundidad, concurrencia, tiempo y gasto por consumidor.


**Práctica y evidencia:** Define cuotas y límites para operaciones costosas y recursos asociados. **Evidencia:** demuestra protección ante consumo excesivo sin degradar otros usuarios.

#### 25.5.09 — Unsafe API Consumption
Unsafe API Consumption ocurre cuando un sistema confía en respuestas de APIs externas sin validar origen, esquema, TLS y límites. Trata proveedores como entradas no confiables y protege contra redirecciones y respuestas inesperadas.


**Práctica y evidencia:** Diseña consumo seguro de API de terceros con TLS, validación de esquema, timeout y manejo de errores. **Evidencia:** prueba respuesta inesperada en stub.

### Módulo 25.6 — Herramientas

#### 25.6.01 — Burp Suite
Burp Suite es una plataforma de pruebas de seguridad web con herramientas manuales y automatizadas. Utilízala con alcance autorizado, licencia apropiada y datos ficticios; protege proyectos y archivos de sesión.


**Práctica y evidencia:** Configura Burp Suite en entorno local y crea proyecto con scope explícito. **Evidencia:** registra versión y límites de uso.

#### 25.6.02 — Postman
Postman permite explorar contratos, ejecutar colecciones y comprobar respuestas de APIs. Usa entornos de prueba, elimina secretos de exportaciones y añade assertions para estados y esquemas.


**Práctica y evidencia:** Crea colección Postman con variables sintéticas y pruebas de autorización. **Evidencia:** elimina secretos del export y registra resultados.

#### 25.6.03 — OWASP ZAP
OWASP ZAP es una herramienta de proxy y análisis de seguridad web con capacidades automatizadas. Configura alcance, contexto y modo seguro; ejecuta escaneos solo sobre aplicaciones propias o expresamente autorizadas.


**Práctica y evidencia:** Configura OWASP ZAP en modo seguro contra Juice Shop local. **Evidencia:** registra contexto, política y hallazgos confirmados.

#### 25.6.04 — OWASP Juice Shop
OWASP Juice Shop es una aplicación deliberadamente vulnerable para formación y validación de controles. Despliega en red aislada, usa datos ficticios y restaura el entorno al terminar.


**Práctica y evidencia:** Despliega OWASP Juice Shop en red aislada y conserva snapshot antes de practicar. **Evidencia:** demuestra que no es accesible desde redes externas.

#### 25.6.05 — Web Security Academy
Web Security Academy ofrece laboratorios educativos y materiales de seguridad web. Sigue el entorno y reglas del programa, registra conceptos aprendidos y no traslades pruebas a sistemas externos sin autorización.

**Nota curricular:** el campo oficial `objetivo` de la etapa 25 permanece vacío. Este desglose no añade ni propone un objetivo sustituto.



**Práctica y evidencia:** Selecciona un laboratorio de Web Security Academy y documenta objetivo, aprendizaje y mitigación. **Evidencia:** resuelve solo el entorno educativo autorizado y explica corrección defensiva.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 50 orientaciones genéricas por explicaciones específicas de arquitectura web, vulnerabilidades, OWASP, Burp Suite, seguridad de APIs y herramientas.

**Nota curricular:** el campo oficial `objetivo` de la etapa 25 permanece vacío. No se ha creado, inferido ni sustituido un objetivo para esta etapa.

**Revisión interna:** 50/50 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron controles de autorización por objeto, validación, codificación contextual, gestión de tokens, CORS, límites de recursos y pruebas no destructivas. Burp Intruder/Scanner y ZAP se limitan a laboratorios propios o autorizados; la disponibilidad y licencia deben comprobarse. Pendiente: ejecutar pruebas de seguridad en aplicaciones aisladas, validar contratos y obtener segunda revisión especializada. No se realizaron escaneos ni se declara aprobación externa.
