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
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.02 — Frontend
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.03 — Backend
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.04 — Database
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.05 — API
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.06 — Sessions
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.07 — Cookies
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.08 — Authentication
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.09 — Authorization
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.1.10 — TLS
Estudiar el concepto dentro de arquitectura de seguridad web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 25.2 — Vulnerabilidades web

#### 25.2.01 — SQL Injection
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.02 — NoSQL Injection
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.03 — Cross-Site Scripting (XSS)
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.04 — Cross-Site Request Forgery (CSRF)
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.05 — Server-Side Request Forgery (SSRF)
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.06 — IDOR
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.07 — Broken Access Control
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.08 — Path Traversal
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.09 — Command Injection
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.10 — Insecure File Upload
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.11 — Authentication Bypass
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.2.12 — Security Misconfiguration
Estudiar el concepto dentro de vulnerabilidades web, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 25.3 — OWASP

#### 25.3.01 — OWASP Top 10:2025
Estudiar el concepto dentro de owasp, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.3.02 — OWASP Web Security Testing Guide
Estudiar el concepto dentro de owasp, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.3.03 — Secure Coding
Estudiar el concepto dentro de owasp, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.3.04 — Threat Modeling
Estudiar el concepto dentro de owasp, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.3.05 — Security Testing
Estudiar el concepto dentro de owasp, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 25.4 — Burp Suite

#### 25.4.01 — Proxy
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.02 — HTTP History
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.03 — Repeater
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.04 — Intruder
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.05 — Decoder
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.06 — Comparer
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.07 — Target
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.08 — Scanner (según disponibilidad y licencia)
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.4.09 — Análisis de requests y responses
Estudiar el concepto dentro de burp suite, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 25.5 — Seguridad de APIs

#### 25.5.01 — REST Security
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.02 — API Authentication
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.03 — API Authorization
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.04 — Token Management
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.05 — API Rate Limiting
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.06 — API Inventory
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.07 — Broken Object Level Authorization
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.08 — Unrestricted Resource Consumption
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.5.09 — Unsafe API Consumption
Estudiar el concepto dentro de seguridad de apis, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 25.6 — Herramientas

#### 25.6.01 — Burp Suite
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.6.02 — Postman
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.6.03 — OWASP ZAP
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.6.04 — OWASP Juice Shop
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 25.6.05 — Web Security Academy
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

**Nota curricular:** el campo oficial `objetivo` de la etapa 25 permanece vacío. Este desglose no añade ni propone un objetivo sustituto.
