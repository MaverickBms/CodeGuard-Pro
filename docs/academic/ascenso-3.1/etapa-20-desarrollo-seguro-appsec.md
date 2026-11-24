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
