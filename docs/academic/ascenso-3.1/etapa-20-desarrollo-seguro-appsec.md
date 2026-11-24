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
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.02 — Security by Design
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.03 — Security by Default
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.04 — Least Privilege
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.05 — Defense in Depth
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.06 — Threat Modeling
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.1.07 — Attack Surface
Estudiar este elemento desde su función y sus límites en fundamentos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 20.2 — Seguridad web

#### 20.2.01 — SQL Injection
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.02 — XSS
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.03 — CSRF
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.04 — SSRF
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.05 — IDOR
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.06 — Broken Access Control
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.07 — Path Traversal
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.08 — Command Injection
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.09 — File Upload Vulnerabilities
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.2.10 — Authentication Flaws
Estudiar este elemento desde su función y sus límites en seguridad web; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 20.3 — OWASP Top 10

#### 20.3.01 — A01: Broken Access Control
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.02 — A02: Security Misconfiguration
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.03 — A03: Software Supply Chain Failures
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.04 — A04: Cryptographic Failures
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.05 — A05: Injection
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.06 — A06: Insecure Design
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.07 — A07: Authentication Failures
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.08 — A08: Software or Data Integrity Failures
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.09 — A09: Security Logging and Alerting Failures
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.10 — A10: Mishandling of Exceptional Conditions
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.11 — Esta es la edición publicada más reciente que hemos verificado
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.3.12 — OWASP Top 10:2025
Estudiar este elemento desde su función y sus límites en owasp top 10; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 20.4 — Autenticación y autorización

#### 20.4.01 — Authentication
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.02 — Authorization
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.03 — Sessions
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.04 — Cookies
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.05 — JWT
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.06 — OAuth2
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.07 — OpenID Connect
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.08 — MFA
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.09 — RBAC
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.10 — ABAC
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.11 — Password Hashing
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.4.12 — Secure Password Storage
Estudiar este elemento desde su función y sus límites en autenticación y autorización; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 20.5 — Seguridad de APIs

#### 20.5.01 — OWASP API Security Top 10
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.5.02 — Broken Object Level Authorization
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.5.03 — Broken Authentication
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.5.04 — Unrestricted Resource Consumption
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.5.05 — API Misconfiguration
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.5.06 — Unsafe API Consumption
Estudiar este elemento desde su función y sus límites en seguridad de apis; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 20.6 — Seguridad de infraestructura

#### 20.6.01 — HTTPS
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.02 — TLS
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.03 — Secure Headers
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.04 — CORS
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.05 — Secrets Management
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.06 — Environment Variables
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.07 — Rate Limiting
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.08 — Input Validation
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.09 — Output Encoding
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 20.6.10 — Secure Error Handling
Estudiar este elemento desde su función y sus límites en seguridad de infraestructura; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.
