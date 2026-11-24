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
Machine Learning aprende patrones a partir de datos para producir predicciones o clasificaciones. En seguridad define objetivo, población, calidad de etiquetas y coste de error; un modelo no reemplaza el criterio del analista.

#### 30.1.02 — Anomaly Detection
Anomaly Detection identifica observaciones que difieren de una línea base o distribución esperada. Ajusta umbrales al contexto, considera estacionalidad y revisa falsos positivos antes de escalar alertas.

#### 30.1.03 — Pattern Recognition
Pattern Recognition detecta regularidades en datos como secuencias, eventos o características de archivos. Documenta qué patrón se aprende y qué cambios legítimos pueden producir coincidencias.

#### 30.1.04 — Classification
Classification asigna observaciones a categorías mediante un modelo entrenado o reglas. Evalúa precisión, recall, F1 y matriz de confusión según el coste de falsos positivos y negativos.

#### 30.1.05 — Security Analytics
Security Analytics combina eventos, métricas y contexto para identificar riesgos y apoyar decisiones. Mantén calidad, procedencia y minimización de datos y explica límites de los modelos.

#### 30.1.06 — AI-assisted Investigation
AI-assisted Investigation puede resumir eventos, enriquecer indicadores y sugerir hipótesis para el analista. Verifica cada afirmación contra fuentes primarias y evita que el modelo cierre incidentes o ejecute acciones sin supervisión.

#### 30.1.07 — Limitations of AI in Security
Limitations of AI in Security incluyen falsos positivos, sesgo, datos incompletos, deriva, opacidad y manipulación adversarial. Define límites de uso, validación humana y procedimientos alternativos cuando el modelo falla.

### Módulo 30.2 — LLM Security

#### 30.2.01 — Large Language Models
Large Language Models generan texto y otras salidas a partir de patrones aprendidos y contexto de entrada. Pueden producir errores convincentes; verifica hechos, controla datos enviados y no trates la salida como autoridad.

#### 30.2.02 — Prompt Injection
Prompt Injection ocurre cuando instrucciones maliciosas o no confiables influyen en el comportamiento de un modelo. Separa instrucciones de datos, limita herramientas y valida resultados en una capa externa al modelo.

#### 30.2.03 — Indirect Prompt Injection
Indirect Prompt Injection llega mediante contenido externo que el modelo consulta, como páginas, documentos o resultados de búsqueda. Trata contenido recuperado como datos no confiables y evita que pueda modificar permisos o instrucciones de sistema.

#### 30.2.04 — Jailbreaking
Jailbreaking intenta inducir al modelo a ignorar restricciones o políticas. Evalúa resistencia en entornos controlados, registra categorías de fallo y aplica defensa en profundidad en lugar de depender de una frase de sistema.

#### 30.2.05 — Data Leakage
Data Leakage ocurre cuando el sistema revela datos privados, secretos, prompts internos o información de otros usuarios. Minimiza contexto, aplica autorización antes de recuperar datos y filtra salidas en límites de confianza.

#### 30.2.06 — Context Manipulation
Context Manipulation altera la información que el modelo recibe para cambiar sus conclusiones o prioridades. Registra fuentes y procedencia, limita contexto recuperado y detecta instrucciones embebidas en documentos.

#### 30.2.07 — Tool Abuse
Tool Abuse ocurre cuando un modelo invoca herramientas con parámetros o finalidades no autorizadas. Valida argumentos, aplica allowlists y permisos por acción y exige confirmación humana para operaciones de alto impacto.

#### 30.2.08 — Agent Security
Agent Security protege agentes que planifican y ejecutan acciones mediante herramientas o servicios. Separa planificación de ejecución, controla identidad y alcance y registra cada llamada con límites de presupuesto y tiempo.

#### 30.2.09 — RAG Security
RAG Security protege pipelines de recuperación y generación frente a documentos maliciosos, filtración y acceso cruzado. Aplica autorización a nivel de documento, filtros por usuario y validación de fuentes antes de construir contexto.

#### 30.2.10 — Guardrails
Guardrails son controles de entrada, salida y ejecución que reducen usos no permitidos o resultados inseguros. No son infalibles; combínalos con autorización externa, validación determinista y monitoreo.

#### 30.2.11 — Sandboxing
Sandboxing ejecuta código o herramientas en entornos aislados con recursos, red y filesystem restringidos. Define límites de CPU/memoria/tiempo, elimina credenciales del host y destruye el entorno tras la ejecución.

#### 30.2.12 — Least Privilege for Agents
Least Privilege for Agents limita cada herramienta y agente a acciones, datos y recursos mínimos. Usa permisos temporales, separación por tarea y aprobación para operaciones irreversibles.

### Módulo 30.3 — AI Red Teaming

#### 30.3.01 — Attack Surface
Attack Surface de un sistema de IA incluye modelo, prompts, datos, RAG, herramientas, plugins, APIs, identidad y despliegue. Inventaría cada límite de confianza y propietario y prioriza controles por impacto.

#### 30.3.02 — Adversarial Inputs
Adversarial Inputs son entradas diseñadas para inducir errores o comportamientos no deseados en modelos. Define categorías de prueba y datos sintéticos, evita probar sobre usuarios o datos reales sin autorización.

#### 30.3.03 — Prompt Injection Testing
Prompt Injection Testing evalúa si instrucciones no confiables pueden alterar tareas o políticas. Usa corpus de prueba controlado, mide impacto observable y valida mitigaciones fuera del prompt.

#### 30.3.04 — Tool-use Abuse
Tool-use Abuse Testing verifica si el modelo puede invocar herramientas fuera de permisos o con parámetros peligrosos. Usa herramientas simuladas, permisos mínimos y límites de ejecución para evitar efectos reales.

#### 30.3.05 — Data Exfiltration Scenarios
Data Exfiltration Scenarios evalúa si información sensible puede salir por respuestas, herramientas, logs o contexto compartido. Utiliza canarios sintéticos y valida aislamiento entre usuarios y controles de salida.

#### 30.3.06 — Model Evaluation
Model Evaluation mide calidad, robustez, seguridad y comportamiento del modelo con conjuntos de datos y métricas definidos. Registra versión, prompt, parámetros y entorno para reproducir resultados.

#### 30.3.07 — Security Testing of AI Systems
Security Testing of AI Systems combina pruebas de modelo, aplicación, datos, identidad y herramientas. Define alcance y riesgos, prueba fallos y abuso de permisos y documenta limitaciones.

### Módulo 30.4 — Automatización con Python

#### 30.4.01 — Python avanzado
Python avanzado incluye iteradores, generadores, context managers, tipado, excepciones y concurrencia. Selecciona características que simplifiquen el mantenimiento y documenta versiones y dependencias.

#### 30.4.02 — OOP
OOP en Python organiza datos y comportamiento mediante clases, composición y protocolos. Mantén responsabilidades pequeñas y evita jerarquías profundas o estado global compartido.

#### 30.4.03 — Modules
Modules separan funciones, clases y constantes en unidades importables. Evita efectos secundarios durante importación y define interfaz pública clara.

#### 30.4.04 — Packages
Packages agrupan módulos bajo una estructura y espacio de nombres. Fija dependencias y versiones, controla origen y utiliza entornos virtuales para reproducibilidad.

#### 30.4.05 — Requests
Requests facilita solicitudes HTTP desde Python y manejo de respuestas. Configura timeout, TLS, retries acotados y validación de status/content; nunca desactives verificación de certificados para resolver errores.

#### 30.4.06 — JSON
JSON serializa estructuras de datos mediante objetos, arrays y valores básicos. Valida esquema y tamaño, maneja errores de parseo y no confíes en tipos o campos enviados por terceros.

#### 30.4.07 — YAML
YAML es un formato de configuración legible que admite estructuras anidadas. Usa loaders seguros, valida esquema y evita cargar documentos no confiables con constructores que permitan objetos arbitrarios.

#### 30.4.08 — Regex
Regex define patrones para buscar o validar texto. Controla complejidad para evitar ReDoS, utiliza patrones anclados cuando corresponda y prueba entradas largas y límites.

#### 30.4.09 — subprocess
subprocess permite ejecutar procesos externos y capturar entradas/salidas desde Python. Evita `shell=True` con datos no confiables, pasa argumentos separados, limita tiempo y permisos y registra errores sin secretos.

#### 30.4.10 — Sockets
Sockets permiten comunicación de bajo nivel sobre protocolos de red. Define timeouts, framing, validación de mensajes y cierre; practica únicamente con servicios propios o autorizados.

#### 30.4.11 — Asyncio
asyncio ofrece concurrencia cooperativa para operaciones asíncronas. Usa tareas y semáforos para limitar concurrencia, propaga cancelación y evita bloquear el event loop con operaciones síncronas.

#### 30.4.12 — Logging
Logging registra eventos de ejecución con niveles, contexto y destinos configurables. Usa datos estructurados, correlación y rotación; redacta credenciales, tokens y datos personales.

#### 30.4.13 — APIs
APIs permiten integrar servicios mediante contratos HTTP u otros protocolos. Gestiona autenticación, cuotas, paginación, errores y cambios de versión y no expongas claves en código.

#### 30.4.14 — File Processing
File Processing lee y transforma archivos de texto, datos estructurados y binarios. Valida rutas, tamaño, codificación y tipo real; evita path traversal y sobrescritura accidental.

### Módulo 30.5 — Automatización de seguridad

#### 30.5.01 — Log Processing
Log Processing normaliza y filtra eventos para extraer información útil. Conserva timestamp, origen y campos de correlación y protege registros contra alteración y filtración.

#### 30.5.02 — IOC Extraction
IOC Extraction identifica indicadores potenciales en logs, documentos o alertas. Valida formato, contexto, confianza y vigencia antes de distribuir o bloquear indicadores.

#### 30.5.03 — Threat Intelligence Collection
Threat Intelligence Collection reúne información de fuentes abiertas, feeds y reportes autorizados. Registra procedencia, licencia, frescura y confianza y evita recopilar datos personales innecesarios.

#### 30.5.04 — Report Generation
Report Generation automatiza informes con plantillas y datos estructurados. Verifica exactitud, contexto y destinatarios y elimina secretos y datos sensibles de los documentos generados.

#### 30.5.05 — API Integrations
API Integrations conectan automatizaciones con SIEM, ticketing, inventarios y fuentes de inteligencia. Usa tokens de mínimo privilegio, paginación, retries limitados y manejo de rate limits.

#### 30.5.06 — Vulnerability Reporting
Vulnerability Reporting convierte hallazgos en reportes con activo, versión, evidencia, impacto y remediación. Valida falsos positivos y no adjunta datos sensibles innecesarios.

#### 30.5.07 — Alert Classification
Alert Classification prioriza alertas por severidad, confianza, activo y contexto. Documenta criterios y permite revisión humana para casos ambiguos.

#### 30.5.08 — Security Automation Pipelines
Security Automation Pipelines encadenan recolección, análisis, enriquecimiento y notificación. Diseña etapas idempotentes, permisos mínimos, observabilidad y aprobación para acciones de alto impacto.

### Módulo 30.6 — Threat Intelligence avanzado

#### 30.6.01 — Threat Intelligence Lifecycle
Threat Intelligence Lifecycle organiza dirección, recolección, procesamiento, análisis, difusión y retroalimentación. Define requisitos del consumidor y mide si la inteligencia cambia una decisión.

#### 30.6.02 — OSINT Automation
OSINT Automation automatiza consultas a fuentes públicas dentro de términos y límites permitidos. Controla frecuencia, registra fuentes y minimiza datos personales.

#### 30.6.03 — MITRE ATT&CK
MITRE ATT&CK estructura conocimiento sobre tácticas y técnicas adversarias. Usa versión y plataforma, vincula detecciones y no atribuyas actor a partir de un único mapeo.

#### 30.6.04 — TTP Correlation
TTP Correlation relaciona comportamientos observados con técnicas y secuencias conocidas. Evalúa evidencia, temporalidad y alternativas benignas y evita sobreajustar una conclusión.

#### 30.6.05 — Threat Feeds
Threat Feeds distribuyen indicadores y contexto de amenazas. Evalúa calidad, licencia, frescura y falsos positivos y automatiza expiración y revisión.

#### 30.6.06 — Intelligence Analysis
Intelligence Analysis evalúa fuentes, corroboración, hipótesis y confianza para producir conclusiones accionables. Distingue hechos de inferencias y declara vacíos de información.

### Módulo 30.7 — Criptografía avanzada

#### 30.7.01 — Symmetric Cryptography
Symmetric Cryptography utiliza una clave compartida para cifrar y descifrar o autenticar datos. Protege distribución y almacenamiento de claves y utiliza modos autenticados modernos.

#### 30.7.02 — Asymmetric Cryptography
Asymmetric Cryptography utiliza pares de claves pública/privada para operaciones como establecimiento de claves y firmas. Comprende usos distintos y protege claves privadas y validación de identidad.

#### 30.7.03 — AES
AES es un cifrador de bloque estandarizado con clave de 128, 192 o 256 bits. Utiliza modos seguros y autenticados como AES-GCM con nonces únicos; no diseñes modos propios.

#### 30.7.04 — RSA
RSA es un sistema de clave pública usado para cifrado y firmas bajo esquemas adecuados. Selecciona padding moderno y tamaños conforme a estándares; no utilices RSA textbook ni implementes primitivas propias.

#### 30.7.05 — ECC
ECC agrupa criptografía de curvas elípticas para firmas y acuerdo de claves. Utiliza curvas y bibliotecas aprobadas, valida puntos y parámetros y protege generación de aleatoriedad.

#### 30.7.06 — Hashing
Hashing transforma datos en un resumen de longitud fija y se usa para integridad y otras funciones. Un hash general no es adecuado para almacenar contraseñas; selecciona algoritmo según propósito.

#### 30.7.07 — SHA-2
SHA-2 es una familia de funciones hash que incluye SHA-256 y SHA-512. Se utiliza para integridad y construcción criptográfica, pero no cifra ni autentica por sí sola.

#### 30.7.08 — SHA-3
SHA-3 se basa en la construcción Keccak y ofrece funciones hash y extendibles. Distingue SHA3-256 de SHAKE y selecciona variante según protocolo y estándar.

#### 30.7.09 — Digital Signatures
Digital Signatures permiten verificar integridad y autenticidad del firmante mediante clave pública. Gestiona certificados y claves, valida contexto y revocación y no confundas firma con cifrado.

#### 30.7.10 — PKI
PKI administra certificados, autoridades de certificación, claves y políticas de confianza. Define emisión, renovación, revocación y protección de claves raíz y operativas.

#### 30.7.11 — TLS
TLS protege canales de comunicación y autentica extremos según configuración. Mantén versiones y suites soportadas, valida certificados y comprende que la seguridad depende también de identidad y aplicación.

#### 30.7.12 — Key Management
Key Management cubre generación, almacenamiento, distribución, rotación, respaldo y destrucción de claves. Separa funciones, limita acceso, registra operaciones y planifica recuperación y compromiso.

### Módulo 30.8 — Criptografía poscuántica

#### 30.8.01 — Quantum Computing Concepts
Quantum Computing Concepts estudia qubits, superposición, entrelazamiento y algoritmos cuánticos relevantes para criptografía. Distingue capacidades teóricas y hardware actual y evita afirmar que cualquier computador cuántico rompe hoy toda criptografía.

#### 30.8.02 — Harvest Now, Decrypt Later
Harvest Now, Decrypt Later describe la captura actual de datos cifrados con intención de descifrarlos en el futuro si la capacidad criptanalítica mejora. Prioriza información con vida útil larga y evalúa migración según sensibilidad y horizonte.

#### 30.8.03 — Post-Quantum Cryptography
Post-Quantum Cryptography desarrolla algoritmos clásicos diseñados para resistir ataques de computadores cuánticos a gran escala. Distingue criptografía poscuántica de criptografía cuántica y utiliza estándares y bibliotecas mantenidas.

#### 30.8.04 — ML-KEM
ML-KEM es un mecanismo de encapsulación de claves basado en retículos, estandarizado por NIST en FIPS 203. Permite establecer un secreto compartido; no es un algoritmo de cifrado de archivos por sí solo y requiere implementación validada.

#### 30.8.05 — ML-DSA
ML-DSA es un esquema de firma digital basado en retículos estandarizado por NIST en FIPS 204. Se usa para firmar y verificar, no para cifrar; verifica parámetros, claves y actualizaciones/erratas del estándar.

#### 30.8.06 — SLH-DSA
SLH-DSA es un esquema de firma digital poscuántica basado en hashes, estandarizado por NIST en FIPS 205. Comprende compensaciones de tamaño y rendimiento y utiliza implementaciones conformes.

#### 30.8.07 — Cryptographic Migration
Cryptographic Migration inventaría algoritmos, protocolos, claves y dependencias para sustituir mecanismos vulnerables o obsoletos. Prioriza activos y datos de larga vida, prueba interoperabilidad y planifica transición reversible.

#### 30.8.08 — Crypto Agility
Crypto Agility permite cambiar algoritmos y parámetros sin rediseñar por completo sistemas y protocolos. Abstrae suites criptográficas, inventaría dependencias y prueba actualización, revocación y compatibilidad.

#### 30.8.09 — CSRC
CSRC es el Computer Security Resource Center de NIST, repositorio de publicaciones y recursos técnicos, no un estándar individual. Identifica cada documento por número, revisión y fecha antes de adoptarlo.


### Referencias oficiales de criptografía poscuántica

- NIST FIPS 203 — ML-KEM: https://csrc.nist.gov/pubs/fips/203/final
- NIST FIPS 204 — ML-DSA: https://csrc.nist.gov/pubs/fips/204/final
- NIST FIPS 205 — SLH-DSA: https://csrc.nist.gov/pubs/fips/205/final
- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography

Verifica erratas y revisiones de cada publicación antes de implementar. No implementes algoritmos criptográficos propios ni interpretes el carácter poscuántico como garantía absoluta de seguridad.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 75 orientaciones genéricas por explicaciones específicas de IA aplicada a seguridad, LLM/agent security, AI red teaming, Python, automatización, threat intelligence, criptografía y migración poscuántica.

**Revisión interna:** 75/75 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron límites de modelos, prompt injection, RAG, abuso de herramientas, sandboxing, permisos de agentes, manejo seguro de subprocess/archivos y gestión de claves. Se añadieron referencias NIST para FIPS 203/204/205 y se diferenció ML-KEM (encapsulación de claves) de ML-DSA/SLH-DSA (firmas). Pendiente: validar implementaciones y erratas vigentes, ejecutar pruebas en entornos aislados y realizar segunda revisión especializada. No se ejecutaron pruebas de IA ni se implementó criptografía; no se declara aprobación externa.
