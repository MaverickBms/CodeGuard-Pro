# Etapa 30 — Inteligencia artificial, automatización y seguridad avanzada

**Prioridad:** P2/P3 · Especialización avanzada  
**Estado:** borrador académico  
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

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se ejecutó agente ni automatización sobre fuentes externas en esta sesión. **Estado:** borrador.
