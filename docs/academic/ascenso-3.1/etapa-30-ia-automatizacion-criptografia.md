# Etapa 30 — Inteligencia artificial, automatización y seguridad avanzada

**Prioridad:** P2/P3 · Especialización avanzada  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** comprender amenazas modernas y desarrollar capacidades de automatización de seguridad.  
**Proyecto oficial:** crear un sistema de automatización en Python que recopile información de fuentes autorizadas, procese indicadores de compromiso y genere reportes de seguridad.

## Resultados de aprendizaje
Aplicar conceptos de ML a analítica defensiva; identificar amenazas de LLM y agentes; evaluar sistemas de IA en entornos controlados; automatizar tareas con Python; procesar inteligencia de amenazas; comprender criptografía simétrica/asimétrica y estándares poscuánticos.

## 30.1 — Inteligencia artificial para seguridad
Machine Learning identifica patrones a partir de datos, pero depende de calidad, representatividad y contexto. Anomaly Detection busca desviaciones; Pattern Recognition identifica estructuras; Classification asigna categorías. Security Analytics puede apoyar priorización y correlación. AI-assisted Investigation ayuda a resumir o formular hipótesis, pero las conclusiones deben verificarse con evidencia.

Comprende falsos positivos/negativos, sesgo, drift, explicabilidad, privacidad y límites. No utilices modelos como única autoridad para decisiones de bloqueo, atribución o respuesta crítica.

**Ejercicio:** clasifica registros sintéticos con un modelo simple y compara métricas con una regla determinista; analiza errores y sesgos.

## 30.2 — LLM Security
Los Large Language Models procesan instrucciones y contexto, pero pueden ser vulnerables a Prompt Injection, Indirect Prompt Injection, jailbreaking, data leakage y context manipulation. Tool Abuse ocurre cuando un modelo utiliza herramientas con permisos excesivos o sin validación. Agent Security exige identidad, límites, aprobación, aislamiento y trazabilidad.

RAG Security incluye controles de origen, permisos por documento, filtrado, aislamiento de tenants, protección frente a instrucciones maliciosas en documentos y evaluación de recuperación. Guardrails pueden reducir riesgos, pero no garantizan seguridad. Sandboxing y least privilege for agents limitan impacto.

Diseña agentes para que los datos recuperados sean tratados como contenido no confiable, nunca como política ejecutable. Valida cada acción en el sistema que la realiza; no confíes solo en que el modelo “decida” respetar reglas.

## 30.3 — AI Red Teaming
AI Red Teaming evalúa comportamiento bajo entradas adversariales dentro de alcance aprobado. Estudia attack surface, adversarial inputs, prompt injection, tool-use abuse, escenarios de exfiltración simulada, model evaluation y pruebas de seguridad de sistemas IA.

Utiliza datos sintéticos, herramientas sandbox y destinos de exfiltración simulados. No pruebes sistemas de terceros ni extraigas datos reales. Documenta precondiciones, impacto, reproducibilidad, mitigación y riesgo residual.

**Ejercicio:** crea un agente local con herramienta ficticia de consulta. Diseña casos de prompt injection directa/indirecta y comprueba que permisos y validaciones externas impidan acciones fuera de alcance.

## 30.4 — Automatización con Python
Profundiza en Python, POO, módulos, paquetes, Requests, JSON, YAML, regex, subprocess, sockets, asyncio, logging, APIs y procesamiento de archivos. Valida entradas, maneja excepciones, aplica timeouts, límites de tamaño y allowlists. Evita construir comandos de shell concatenando datos no confiables. Registra errores sin secretos.

**Ejercicio:** crea CLI que lea un conjunto sintético de eventos, valide esquema, normalice fechas y genere un resumen.

## 30.5 — Automatización de seguridad
Log Processing normaliza registros; IOC Extraction identifica indicadores con contexto; Threat Intelligence Collection consulta fuentes autorizadas y respeta límites; Report Generation produce informes; API Integrations conectan servicios; Vulnerability Reporting prioriza hallazgos; Alert Classification organiza señales; Security Automation Pipelines orquestan pasos reproducibles.

Cada automatización debe tener control de acceso, trazabilidad, idempotencia, manejo de errores y revisión humana para acciones de alto impacto.

## 30.6 — Threat Intelligence avanzado
El ciclo de inteligencia comprende dirección, recopilación, procesamiento, análisis, difusión y retroalimentación. OSINT Automation debe respetar alcance, términos y privacidad. MITRE ATT&CK ofrece lenguaje para correlacionar TTP; Threat Feeds deben evaluarse por fuente, frescura, confianza, cobertura y falsos positivos. No atribuyas actores a partir de un IOC aislado.

**Ejercicio:** procesa una fuente pública de indicadores permitida, conserva procedencia y timestamp, deduplica y genera un informe con confianza y caducidad.

## 30.7 — Criptografía avanzada
Symmetric Cryptography usa una clave compartida; AES es un cifrador por bloques estandarizado. Asymmetric Cryptography utiliza pares de claves; RSA y ECC se usan en distintos protocolos y perfiles. Hashing produce resúmenes; SHA-2 y SHA-3 son familias hash, no cifrado. Digital Signatures permiten verificar integridad y autenticidad bajo un esquema; PKI administra certificados y confianza; TLS protege canales. Key Management incluye generación, almacenamiento, rotación, respaldo, revocación y destrucción.

No implementes algoritmos criptográficos propios ni uses modos inseguros. Selecciona bibliotecas mantenidas y parámetros recomendados. Distingue cifrado, hash, MAC, firma y derivación de claves.

## 30.8 — Criptografía poscuántica
Quantum Computing introduce riesgos potenciales para ciertos algoritmos de clave pública. Harvest Now, Decrypt Later describe la recolección actual de datos cifrados para intentar descifrarlos en el futuro. Post-Quantum Cryptography desarrolla mecanismos resistentes a adversarios con capacidades cuánticas relevantes.

NIST FIPS 203 (ML-KEM) especifica encapsulación de claves; FIPS 204 (ML-DSA) y FIPS 205 (SLH-DSA) especifican firmas digitales. Estudia tamaños, rendimiento, interoperabilidad, migración y crypto agility. No asumas que cifrado simétrico y todos los hashes se ven afectados del mismo modo que RSA/ECC. Planifica inventario criptográfico y migración gradual.

## Proyecto oficial — Automatización de seguridad con Python
### Requisitos
1. Fuentes autorizadas y documentadas.
2. Ingesta de registros/indicadores sintéticos o públicos permitidos.
3. Validación de esquema y normalización.
4. Deduplicación y enriquecimiento con procedencia.
5. Correlación con categorías ATT&CK cuando exista evidencia.
6. Clasificación con nivel de confianza y caducidad.
7. Generación de reporte técnico.
8. Integración API con timeouts y rate limits.
9. Logs seguros y manejo de errores.
10. Pruebas unitarias y fixtures reproducibles.
11. Aprobación humana antes de acciones de bloqueo/cambio.
12. Documentación de límites de IA y automatización.

### Entregables
Repositorio, diagrama de flujo, inventario de fuentes, esquema de eventos, pruebas, reportes sintéticos, matriz de confianza, evaluación de seguridad de IA y documentación.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| IA/ML y límites | 10 |
| LLM security y agentes | 20 |
| AI red teaming seguro | 10 |
| Python avanzado | 15 |
| Automatización y APIs | 15 |
| Threat intelligence | 10 |
| Criptografía y gestión de claves | 10 |
| Poscuántica y crypto agility | 5 |
| Pruebas y documentación | 5 |

Criterio orientativo: 80/100; las acciones sensibles requieren validación humana y límites externos.

## Autoevaluación
1. ¿Qué diferencia hay entre clasificación y detección de anomalías?
2. ¿Por qué el output de un modelo no es evidencia suficiente?
3. Diferencia prompt injection directa e indirecta.
4. ¿Por qué un agente necesita permisos mínimos?
5. ¿Qué controles debe tener una herramienta invocable?
6. ¿Por qué no concatenar datos en comandos subprocess?
7. ¿Qué metadatos requiere un IOC?
8. Diferencia cifrado simétrico, asimétrico y hashing.
9. ¿Qué diferencia hay entre ML-KEM y ML-DSA?
10. ¿Qué significa crypto agility?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo con audio español y relación directa con LLM security, prompt injection, automatización defensiva Python o estándares NIST poscuánticos. No se utilizarán demostraciones de exfiltración real.

## Referencias oficiales
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST SSDF: https://csrc.nist.gov/Projects/ssdf
- Python Documentation: https://docs.python.org/3/
- Requests: https://requests.readthedocs.io/
- MITRE ATT&CK: https://attack.mitre.org/
- NIST FIPS 203: https://csrc.nist.gov/pubs/fips/203/final
- NIST FIPS 204: https://csrc.nist.gov/pubs/fips/204/final
- NIST FIPS 205: https://csrc.nist.gov/pubs/fips/205/final
- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ejecutó agente ni automatización sobre fuentes externas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 30

Este desglose conserva los títulos y el orden del roadmap maestro. Las orientaciones organizan el estudio y la aplicación en proyectos controlados; no equivalen a validación de proveedores, certificación, ejecución de laboratorios ni experiencia laboral demostrada.

### Módulo 30.1 — Inteligencia artificial para seguridad

#### 30.1.01 — Machine Learning
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.02 — Anomaly Detection
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.03 — Pattern Recognition
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.04 — Classification
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.05 — Security Analytics
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.06 — AI-assisted Investigation
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.1.07 — Limitations of AI in Security
Comprender el concepto, sus fundamentos y límites dentro de inteligencia artificial para seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

### Módulo 30.2 — LLM Security

#### 30.2.01 — Large Language Models
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.02 — Prompt Injection
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.03 — Indirect Prompt Injection
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.04 — Jailbreaking
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.05 — Data Leakage
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.06 — Context Manipulation
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.07 — Tool Abuse
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.08 — Agent Security
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.09 — RAG Security
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.10 — Guardrails
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.11 — Sandboxing
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.2.12 — Least Privilege for Agents
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

### Módulo 30.3 — AI Red Teaming

#### 30.3.01 — Attack Surface
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.02 — Adversarial Inputs
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.03 — Prompt Injection Testing
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.04 — Tool-use Abuse
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.05 — Data Exfiltration Scenarios
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.06 — Model Evaluation
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

#### 30.3.07 — Security Testing of AI Systems
Comprender el riesgo, los límites y los controles del sistema de IA; probar únicamente entornos propios o autorizados, sin introducir secretos ni datos personales en servicios externos.

### Módulo 30.4 — Automatización con Python

#### 30.4.01 — Python avanzado
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.02 — OOP
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.03 — Modules
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.04 — Packages
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.05 — Requests
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.06 — JSON
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.07 — YAML
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.08 — Regex
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.09 — subprocess
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.10 — Sockets
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.11 — Asyncio
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.12 — Logging
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.13 — APIs
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.4.14 — File Processing
Comprender el concepto, sus fundamentos y límites dentro de automatización con python; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

### Módulo 30.5 — Automatización de seguridad

#### 30.5.01 — Log Processing
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.02 — IOC Extraction
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.03 — Threat Intelligence Collection
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.04 — Report Generation
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.05 — API Integrations
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.06 — Vulnerability Reporting
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.07 — Alert Classification
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.5.08 — Security Automation Pipelines
Comprender el concepto, sus fundamentos y límites dentro de automatización de seguridad; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

### Módulo 30.6 — Threat Intelligence avanzado

#### 30.6.01 — Threat Intelligence Lifecycle
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.6.02 — OSINT Automation
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.6.03 — MITRE ATT&CK
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.6.04 — TTP Correlation
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.6.05 — Threat Feeds
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.6.06 — Intelligence Analysis
Comprender el concepto, sus fundamentos y límites dentro de threat intelligence avanzado; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

### Módulo 30.7 — Criptografía avanzada

#### 30.7.01 — Symmetric Cryptography
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.02 — Asymmetric Cryptography
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.03 — AES
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.04 — RSA
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.05 — ECC
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.06 — Hashing
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.07 — SHA-2
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.08 — SHA-3
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.09 — Digital Signatures
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.10 — PKI
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.11 — TLS
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.7.12 — Key Management
Comprender el concepto, sus fundamentos y límites dentro de criptografía avanzada; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

### Módulo 30.8 — Criptografía poscuántica

#### 30.8.01 — Quantum Computing Concepts
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.02 — Harvest Now, Decrypt Later
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.03 — Post-Quantum Cryptography
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.04 — ML-KEM
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.05 — ML-DSA
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.06 — SLH-DSA
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.07 — Cryptographic Migration
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.08 — Crypto Agility
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.

#### 30.8.09 — CSRC
Comprender el concepto, sus fundamentos y límites dentro de criptografía poscuántica; relacionarlo con decisiones técnicas, seguridad, operación y documentación del proyecto de la etapa.
