# Etapa 20 — Desarrollo seguro de software (AppSec)

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a desarrollar aplicaciones seguras desde su diseño.  
**Proyecto oficial:** construir una aplicación web deliberadamente vulnerable en un entorno controlado, identificar debilidades, corregirlas y realizar pruebas de regresión de seguridad.

## Resultados de aprendizaje
Aplicar secure coding, security by design/default, mínimo privilegio y defensa en profundidad; modelar amenazas; reconocer vulnerabilidades web y de API; aplicar controles de identidad; y proteger infraestructura, configuración y secretos.

## 20.1 — Fundamentos
Secure Coding incorpora controles durante el desarrollo. Security by Design integra seguridad desde requisitos y arquitectura; Security by Default ofrece configuración inicial restrictiva. Least Privilege limita permisos a lo necesario; Defense in Depth utiliza controles complementarios. Threat Modeling identifica activos, límites de confianza, amenazas, controles y riesgos. Attack Surface describe puntos donde un actor puede interactuar con el sistema.

Modela flujos de datos, actores, fronteras y activos. Prioriza riesgos por impacto y probabilidad, documenta supuestos y actualiza el modelo cuando cambia la arquitectura. STRIDE puede servir como técnica de identificación, pero no sustituye el análisis del contexto.

**Ejercicio:** modela amenazas de una aplicación de inventario: autenticación, roles, carga de archivos, API, base de datos y pipeline.

## 20.2 — Seguridad web
- **SQL Injection:** ocurre cuando datos no confiables alteran una consulta. Usa consultas parametrizadas y APIs seguras; no concatenes entrada en SQL.
- **XSS:** datos no confiables se ejecutan como contenido activo en navegador. Aplica encoding contextual, sanitización cuando sea necesaria y evita sinks inseguros.
- **CSRF:** induce solicitudes no deseadas usando credenciales del navegador. Usa defensas adecuadas al modelo de sesión, SameSite y tokens anti-CSRF cuando corresponda.
- **SSRF:** el servidor realiza solicitudes a destinos controlados por un atacante. Restringe destinos, protocolos, resolución DNS y acceso a redes internas.
- **IDOR / Broken Access Control:** una referencia manipulable permite acceder a recursos sin autorización. Verifica permisos por objeto en el servidor.
- **Path Traversal:** entrada manipula rutas para salir del directorio permitido. Normaliza y restringe rutas; evita confiar en nombres de archivo.
- **Command Injection:** datos alteran comandos del sistema. Evita invocar shell; usa APIs específicas y argumentos separados.
- **File Upload:** archivos maliciosos o inesperados alcanzan almacenamiento/procesamiento. Limita tamaño, verifica contenido, cambia nombre, almacena fuera de rutas ejecutables y controla descarga.
- **Authentication flaws:** sesiones débiles, recuperación insegura, MFA mal aplicada o credenciales expuestas. Diseña ciclo de vida completo y protección contra abuso.

No practiques explotación contra sistemas ajenos. Los laboratorios deben ser locales, aislados y deliberadamente vulnerables.

## 20.3 — OWASP Top 10:2025
El roadmap identifica OWASP Top 10:2025 y enumera:
- A01 Broken Access Control.
- A02 Security Misconfiguration.
- A03 Software Supply Chain Failures.
- A04 Cryptographic Failures.
- A05 Injection.
- A06 Insecure Design.
- A07 Authentication Failures.
- A08 Software or Data Integrity Failures.
- A09 Security Logging and Alerting Failures.
- A10 Mishandling of Exceptional Conditions.

Estudia cada categoría con escenarios, causas, controles preventivos, detección y pruebas. OWASP Top 10 es un documento de concienciación y priorización, no un checklist exhaustivo ni una certificación de seguridad. Comprueba la versión oficial antes de utilizarla en evaluaciones.

**Ejercicio:** mapea funcionalidades del proyecto a categorías OWASP; registra evidencia, riesgo, mitigación y test de regresión.

## 20.4 — Autenticación y autorización
Authentication valida identidad; authorization determina acciones permitidas. Estudia sesiones, cookies, JWT, OAuth 2.0 y OpenID Connect sin tratarlos como alternativas equivalentes. MFA combina factores distintos. RBAC agrupa permisos mediante roles; ABAC toma decisiones según atributos de sujeto, recurso, acción y contexto.

Password hashing debe utilizar algoritmos adaptativos especializados y parámetros mantenidos; nunca almacenes contraseñas en texto claro ni utilices hash rápido generalista. Secure password storage incluye sal única y gestión segura del proceso de verificación. Protege recuperación, cambio de credenciales, sesiones concurrentes, revocación, expiración y registro de eventos.

**Ejercicio:** define matriz rol-recurso-acción y crea pruebas negativas para cada endpoint sensible.

## 20.5 — Seguridad de APIs
OWASP API Security Top 10:2023 es la referencia señalada por el roadmap. Profundiza en Broken Object Level Authorization, Broken Authentication, Unrestricted Resource Consumption, API Misconfiguration y Unsafe API Consumption. Mantén inventario de APIs, versiones y endpoints; valida acceso a cada objeto; limita recursos; valida entradas y salidas; controla proveedores externos y registra eventos de seguridad.

No confundas API authentication con autorización a nivel de objeto. Un usuario autenticado puede no tener derecho sobre el identificador enviado.

**Ejercicio:** en una API local propia, crea dos usuarios y verifica que uno no pueda leer, modificar o eliminar objetos del otro manipulando IDs. Corrige y automatiza regresión.

## 20.6 — Seguridad de infraestructura
HTTPS/TLS protege el canal; selecciona versiones y configuración vigentes. Secure Headers ayudan a mitigar clases de riesgo en navegador, pero deben ajustarse a la aplicación. CORS controla lectura cross-origin del navegador, no sustituye autorización. Secrets Management evita almacenar credenciales en código, logs o artefactos. Las variables de entorno pueden transportar configuración, pero no son por sí solas un gestor completo de secretos.

Rate limiting limita abuso; Input Validation comprueba formato y reglas; Output Encoding reduce interpretación peligrosa; Secure Error Handling evita revelar detalles internos. Aplica mínimo privilegio a cuentas, servicios, almacenamiento, pipeline y base de datos.

**Ejercicio:** revisa configuración de una aplicación local: TLS, headers, CORS, secretos, límites, validación, encoding, errores y logs.

## Proyecto oficial — Aplicación vulnerable y remediación
Construye o utiliza una aplicación deliberadamente vulnerable en entorno local aislado. Define alcance, red y reglas de laboratorio antes de comenzar.

### Fases
1. Documenta autorización, alcance, activos y topología aislada.
2. Implementa un conjunto acotado de fallos didácticos, no un sistema expuesto.
3. Identifica cada vulnerabilidad y explica causa/impacto.
4. Reproduce únicamente en el laboratorio controlado.
5. Corrige mediante controles apropiados.
6. Añade pruebas automatizadas de regresión.
7. Revisa autenticación, autorización por objeto y secretos.
8. Documenta evidencias sin credenciales reales.
9. Ejecuta revisión de configuración y dependencias.
10. Explica riesgos residuales y limitaciones.

### Entregables
Modelo de amenazas; alcance y reglas; inventario de vulnerabilidades; evidencias sanitizadas; commits de corrección; pruebas de regresión; configuración segura; informe final y limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Modelo de amenazas y diseño seguro | 15 |
| Identificación y explicación de vulnerabilidades | 20 |
| Remediación técnica | 25 |
| Identidad y autorización | 15 |
| Seguridad de API e infraestructura | 15 |
| Pruebas de regresión y reporte | 10 |

Criterio orientativo: 80/100. Es obligatorio mantener el laboratorio aislado y no utilizar sistemas ni datos de terceros sin permiso explícito.

## Autoevaluación
1. ¿Qué diferencia hay entre security by design y security by default?
2. ¿Qué activos y fronteras incluirías en un threat model?
3. ¿Por qué parametrizar consultas evita SQL injection?
4. ¿Qué diferencia hay entre XSS y CSRF?
5. ¿Cómo mitigarías SSRF?
6. ¿Qué es IDOR/BOLA y dónde se comprueba autorización?
7. ¿Por qué un hash de contraseña no debe ser rápido?
8. ¿Qué diferencia hay entre RBAC y ABAC?
9. ¿Qué alcance tiene OWASP Top 10?
10. ¿Por qué CORS no sustituye autorización?

## Recursos audiovisuales
No se incluyen videos aprobados. Solo se añadirán recursos hablados en español y específicos para threat modeling, SQLi, XSS, CSRF, SSRF, control de acceso, OWASP o seguridad de APIs. Los videos de explotación deben limitarse a laboratorios autorizados.

## Referencias oficiales
- OWASP Top 10: https://owasp.org/Top10/
- OWASP Top 10:2025: https://owasp.org/Top10/2025/
- OWASP API Security Top 10:2023: https://owasp.org/API-Security/editions/2023/en/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- NIST Secure Software Development Framework: https://csrc.nist.gov/Projects/ssdf
- NIST SP 800-218: https://csrc.nist.gov/pubs/sp/800/218/final
- MITRE CWE: https://cwe.mitre.org/
- MDN Web Security: https://developer.mozilla.org/en-US/docs/Web/Security

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se desplegó aplicación vulnerable ni se ejecutaron pruebas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 20

Este desglose conserva las entradas del roadmap maestro, incluidas las notas explicativas que aparecen dentro de algunas listas curriculares. Los apartados son guías de estudio y no acreditan pruebas, autorización de laboratorio ni ejecución de herramientas.

### Módulo 20.1 — Fundamentos

#### 20.1.01 — Secure Coding
Secure Coding aplica prácticas de implementación que reducen vulnerabilidades: validación, codificación de salida, consultas parametrizadas, manejo de errores y dependencias mantenidas. Integra controles en revisiones y pruebas, no como una lista que se consulta solo antes de publicar.

#### 20.1.02 — Security by Design
Security by Design incorpora amenazas, límites de confianza y requisitos de seguridad desde la arquitectura. Identifica activos, actores y flujos de datos y decide controles antes de que una elección insegura quede integrada en el diseño.

#### 20.1.03 — Security by Default
Security by Default configura el sistema inicialmente con opciones conservadoras, servicios mínimos y permisos restrictivos. El usuario puede habilitar capacidades justificadas, pero la configuración inicial no debe exponer funciones o datos innecesarios.

#### 20.1.04 — Least Privilege
Least Privilege concede a cada identidad solo permisos necesarios durante el tiempo requerido. Separa cuentas humanas y de servicio, revisa permisos periódicamente y evita privilegios administrativos permanentes.

#### 20.1.05 — Defense in Depth
Defense in Depth combina controles independientes en capas para reducir dependencia de una sola barrera. Diseña prevención, detección y recuperación; capas redundantes deben tener fallos y responsables comprendidos.

#### 20.1.06 — Threat Modeling
Threat Modeling identifica activos, amenazas, límites de confianza y posibles mitigaciones antes o durante el desarrollo. Utiliza un método explícito como STRIDE si encaja, registra supuestos y actualiza el modelo cuando cambia arquitectura.

#### 20.1.07 — Attack Surface
Attack Surface comprende interfaces, servicios, entradas, identidades, dependencias y rutas de acceso que pueden ser abusadas. Inventaría puntos expuestos y reduce los innecesarios; no confundas superficie con una lista exclusiva de puertos.

### Módulo 20.2 — Seguridad web

#### 20.2.01 — SQL Injection
SQL Injection ocurre cuando datos no confiables alteran la estructura de una consulta SQL. Usa consultas parametrizadas y APIs seguras del ORM, limita privilegios de la cuenta y prueba entradas hostiles sin concatenar valores en sentencias.

#### 20.2.02 — XSS
XSS permite que contenido no confiable se ejecute como script en el contexto de un sitio. Aplica codificación contextual de salida, sanitización cuando aceptes HTML, políticas CSP y evita insertar datos con APIs que interpretan markup.

#### 20.2.03 — CSRF
CSRF induce al navegador autenticado a enviar una acción no deseada a una aplicación. Usa tokens anti-CSRF o mecanismos equivalentes, cookies SameSite y validación de origen según arquitectura; no asumas que CORS resuelve CSRF.

#### 20.2.04 — SSRF
SSRF ocurre cuando el servidor realiza solicitudes a destinos controlados indirectamente por una entrada externa. Restringe destinos y protocolos, bloquea redes internas/metadatos cloud, valida DNS/IP después de resolución y aplica controles de salida.

#### 20.2.05 — IDOR
IDOR aparece cuando una aplicación permite acceder a un objeto cambiando su identificador sin verificar autorización. Comprueba permisos sobre cada recurso en servidor y prueba acceso cruzado entre usuarios y tenants.

#### 20.2.06 — Broken Access Control
Broken Access Control es una categoría amplia de fallos donde restricciones de acceso no se aplican correctamente. Centraliza políticas, valida autorización en cada operación y evita confiar en controles visuales o identificadores difíciles de adivinar.

#### 20.2.07 — Path Traversal
Path Traversal manipula rutas para acceder a archivos fuera del directorio permitido. Normaliza rutas, utiliza identificadores internos, aplica allowlists y verifica que la ruta final permanezca dentro del directorio autorizado.

#### 20.2.08 — Command Injection
Command Injection ocurre cuando entradas no confiables alteran comandos del sistema operativo. Evita invocar shell con cadenas construidas; utiliza APIs específicas y argumentos separados, permisos mínimos y allowlists estrictas.

#### 20.2.09 — File Upload Vulnerabilities
File Upload Vulnerabilities surgen por controles insuficientes sobre archivos recibidos. Limita tamaño, valida contenido real, renombra, almacena fuera del webroot, deshabilita ejecución y aplica análisis y autorización al descargar.

#### 20.2.10 — Authentication Flaws
Authentication Flaws incluyen contraseñas débiles, recuperación insegura, sesiones mal gestionadas y ausencia de protección contra abuso. Revisa ciclo completo de identidad, MFA, rate limits, rotación y revocación, no solo la pantalla de login.

### Módulo 20.3 — OWASP Top 10

#### 20.3.01 — A01: Broken Access Control
A01: Broken Access Control agrupa fallos de autorización sobre funciones y objetos. Verifica permisos en servidor para cada acción y objeto, aplica denegación por defecto y registra intentos relevantes sin almacenar datos sensibles.

#### 20.3.02 — A02: Security Misconfiguration
A02: Security Misconfiguration incluye configuraciones inseguras, servicios innecesarios, permisos excesivos y errores de despliegue. Mantén configuraciones reproducibles, elimina valores por defecto y valida endurecimiento en cada entorno.

#### 20.3.03 — A03: Software Supply Chain Failures
A03: Software Supply Chain Failures aborda riesgos en dependencias, herramientas, pipelines y artefactos de terceros. Inventaría componentes, verifica procedencia e integridad, limita permisos CI y revisa actualizaciones y alertas de vulnerabilidad.

#### 20.3.04 — A04: Cryptographic Failures
A04: Cryptographic Failures se relaciona con protección insuficiente de datos por algoritmos, claves o configuraciones inadecuadas. Usa bibliotecas mantenidas, TLS vigente, gestión de claves y minimización de datos; no diseñes criptografía propia.

#### 20.3.05 — A05: Injection
A05: Injection comprende entradas que alteran la interpretación de consultas o comandos. Prefiere APIs parametrizadas, separación de datos e instrucciones y validación contextual; prueba múltiples contextos de interpretación.

#### 20.3.06 — A06: Insecure Design
A06: Insecure Design señala ausencia de controles de seguridad desde requisitos y arquitectura. Modela amenazas, define límites y casos de abuso y establece controles verificables antes de implementar.

#### 20.3.07 — A07: Authentication Failures
A07: Authentication Failures abarca errores de identificación, gestión de credenciales y sesiones. Protege recuperación, MFA, almacenamiento de contraseñas, expiración y revocación y prueba abuso automatizado.

#### 20.3.08 — A08: Software or Data Integrity Failures
A08: Software or Data Integrity Failures aborda confianza indebida en actualizaciones, código, datos o procesos sin verificar integridad. Firma y verifica artefactos, protege pipelines y valida fuentes de datos críticas.

#### 20.3.09 — A09: Security Logging and Alerting Failures
A09: Security Logging and Alerting Failures incluye registros insuficientes, alertas ausentes o detección no operativa. Define eventos de seguridad útiles, integridad y retención de logs, alertas accionables y protección contra filtración de secretos.

#### 20.3.10 — A10: Mishandling of Exceptional Conditions
A10: Mishandling of Exceptional Conditions cubre fallos en condiciones excepcionales que pueden provocar estados inseguros o exposición. Define manejo de errores, límites, fallbacks seguros y recuperación; prueba timeouts, interrupciones y entradas inesperadas.

#### 20.3.11 — Esta es la edición publicada más reciente que hemos verificado
La nota de edición del roadmap sobre la versión más reciente de OWASP debe tratarse como metadato editorial sujeto a comprobación, no como una lección técnica ni como afirmación permanente. Antes de aprobar, registrar URL oficial, fecha de publicación y edición utilizada.

#### 20.3.12 — OWASP Top 10:2025
OWASP Top 10:2025 es una edición versionada de una lista de riesgos de aplicaciones web. Estudia sus categorías en el contexto de la edición oficial y conserva el número de versión en materiales y evaluaciones; no mezcles categorías de ediciones distintas.

### Módulo 20.4 — Autenticación y autorización

#### 20.4.01 — Authentication
Authentication verifica la identidad de una persona o servicio mediante credenciales o mecanismos federados. Define recuperación, MFA, rotación y detección de abuso; autenticar no concede automáticamente acceso a todos los recursos.

#### 20.4.02 — Authorization
Authorization decide qué operaciones y recursos puede utilizar una identidad. Aplica controles en servidor por función y objeto, registra decisiones sensibles y prueba escalamiento horizontal y vertical de privilegios.

#### 20.4.03 — Sessions
Sessions mantienen contexto de autenticación entre solicitudes. Genera identificadores impredecibles, rota tras cambios de privilegio, limita duración y revoca al cerrar sesión o ante incidentes.

#### 20.4.04 — Cookies
Cookies transportan datos del navegador al servidor bajo reglas de dominio, ruta y atributos. Para sesiones utiliza Secure, HttpOnly y SameSite apropiados, y protege contra CSRF y fijación de sesión.

#### 20.4.05 — JWT
JWT es un formato de claims que puede firmarse o cifrarse según perfil. Valida algoritmo, emisor, audiencia, expiración y firma; no almacenes secretos en payloads firmados que suelen ser legibles.

#### 20.4.06 — OAuth2
OAuth2 permite delegar autorización a clientes mediante scopes y tokens. Elige flujos seguros para el tipo de cliente, usa PKCE cuando corresponda y limita permisos y vigencia.

#### 20.4.07 — OpenID Connect
OpenID Connect agrega autenticación e identidad a OAuth2 mediante ID Tokens y endpoints estandarizados. Valida issuer, audience, nonce y firma y diferencia el ID Token del access token.

#### 20.4.08 — MFA
MFA combina factores de categorías distintas para reducir dependencia de una sola credencial. Prefiere métodos resistentes al phishing cuando sea viable y define recuperación segura para evitar que el proceso alternativo anule el control.

#### 20.4.09 — RBAC
RBAC asigna permisos a roles y roles a identidades según responsabilidades. Mantén roles revisables, evita privilegios acumulativos y valida permisos sobre recursos concretos.

#### 20.4.10 — ABAC
ABAC toma decisiones según atributos del sujeto, recurso, acción y contexto. Define políticas legibles y auditables, controla calidad de atributos y evita reglas contradictorias o demasiado amplias.

#### 20.4.11 — Password Hashing
Password Hashing transforma contraseñas en verificadores no reversibles mediante funciones adaptativas diseñadas para ese propósito. Usa algoritmo y parámetros vigentes, salt único y actualización gradual de hashes al autenticar.

#### 20.4.12 — Secure Password Storage
Secure Password Storage exige no almacenar contraseñas en texto claro ni cifrado reversible. Protege hashes, limita acceso, evita registros de credenciales y diseña recuperación mediante tokens de un solo uso y expiración.

### Módulo 20.5 — Seguridad de APIs

#### 20.5.01 — OWASP API Security Top 10
OWASP API Security Top 10 reúne riesgos específicos de APIs, incluidos fallos de autorización, autenticación, consumo de recursos y configuración. Utiliza la edición identificada y traduce cada riesgo a controles y pruebas por endpoint.

#### 20.5.02 — Broken Object Level Authorization
Broken Object Level Authorization ocurre cuando el servidor no verifica si el sujeto puede operar sobre el objeto solicitado. Comprueba ownership, tenant y política contextual en cada endpoint que recibe un identificador.

#### 20.5.03 — Broken Authentication
Broken Authentication en APIs incluye validación incorrecta de tokens, credenciales expuestas y sesiones mal gestionadas. Usa bibliotecas y protocolos mantenidos, valida claims y protege emisión, almacenamiento, renovación y revocación.

#### 20.5.04 — Unrestricted Resource Consumption
Unrestricted Resource Consumption permite que solicitudes agoten CPU, memoria, conexiones o servicios de terceros. Limita tamaño, paginación, complejidad, concurrencia y frecuencia; define cuotas y presupuestos por consumidor.

#### 20.5.05 — API Misconfiguration
API Misconfiguration incluye endpoints, headers, CORS, documentación o servicios desplegados con opciones inseguras. Mantén configuración versionada, deshabilita debugging y endpoints innecesarios y valida diferencias entre desarrollo y producción.

#### 20.5.06 — Unsafe API Consumption
Unsafe API Consumption ocurre cuando una aplicación confía excesivamente en datos o respuestas de APIs externas. Valida esquema, TLS, timeouts y origen, limita redirecciones y no reenvíes credenciales a destinos no confiables.

### Módulo 20.6 — Seguridad de infraestructura

#### 20.6.01 — HTTPS
HTTPS protege el transporte HTTP mediante TLS y validación del servidor. Fuerza uso seguro cuando corresponde, renueva certificados y evita contenido mixto; HTTPS no sustituye autenticación, autorización ni seguridad de la lógica.

#### 20.6.02 — TLS
TLS establece un canal criptográfico con negociación de parámetros y validación de certificados. Mantén versiones y suites soportadas, automatiza renovación y verifica configuración con herramientas confiables.

#### 20.6.03 — Secure Headers
Secure Headers comunican políticas del navegador, como CSP, HSTS, X-Content-Type-Options y políticas de framing/referrer. Configúralos según el sitio y prueba compatibilidad; un header mal definido puede romper funciones o dar falsa sensación de protección.

#### 20.6.04 — CORS
CORS regula qué orígenes de navegador pueden leer respuestas cross-origin. Permite orígenes y credenciales de forma específica; no lo utilices como sustituto de autenticación ni como firewall de API.

#### 20.6.05 — Secrets Management
Secrets Management controla creación, almacenamiento, acceso, rotación y revocación de claves y credenciales. Usa gestores dedicados o mecanismos del entorno, limita acceso por servicio y evita secretos en código, imágenes, logs o variables visibles al cliente.

#### 20.6.06 — Environment Variables
Environment Variables permiten configurar aplicaciones fuera del código fuente, pero no son automáticamente un gestor seguro de secretos. Controla quién puede leer procesos y logs, valida valores y utiliza almacenes secretos cuando el entorno lo permita.

#### 20.6.07 — Rate Limiting
Rate Limiting controla frecuencia de solicitudes para reducir abuso y proteger recursos. Define claves, ventanas y límites por operación; responde de forma consistente y considera NAT/proxies para no penalizar usuarios legítimos.

#### 20.6.08 — Input Validation
Input Validation comprueba tipo, formato, rango, tamaño y reglas de negocio de los datos recibidos. Valida en servidor y en límites de confianza, utiliza allowlists y parametrización y no confundas validación con codificación de salida.

#### 20.6.09 — Output Encoding
Output Encoding representa datos según el contexto donde se insertan, como HTML, atributo, URL o JavaScript. Aplica codificación contextual y evita construir scripts/markup mediante concatenación de entradas no confiables.

#### 20.6.10 — Secure Error Handling
Secure Error Handling devuelve respuestas controladas sin revelar rutas, stack traces, consultas o secretos. Registra detalles internos con acceso restringido, usa identificadores de correlación y define fallbacks que no dejen operaciones a medias.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 57 orientaciones genéricas por explicaciones específicas de AppSec, vulnerabilidades web, categorías OWASP, identidad, seguridad de APIs y controles de infraestructura. Se preservó la nota editorial del roadmap sobre edición OWASP como elemento de metadatos sujeto a verificación, sin tratarla como afirmación permanente.

**Revisión interna:** 57/57 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron controles de autorización por objeto, validación/encoding contextual, gestión de secretos, SSRF, subida de archivos, autenticación, CORS y errores. Pendiente: verificar edición OWASP citada y sus categorías con fuente oficial vigente, ejecutar análisis estático/DAST en laboratorio autorizado y probar controles en aplicaciones de referencia. No se realizaron pruebas ofensivas ni se declara aprobación externa.
