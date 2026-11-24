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


**Práctica y evidencia:** Entrena o evalúa un clasificador con dataset sintético de eventos y separa train/test. **Evidencia:** registra métricas y limita conclusiones por sesgo y calidad de datos.

#### 30.1.02 — Anomaly Detection
Anomaly Detection identifica observaciones que difieren de una línea base o distribución esperada. Ajusta umbrales al contexto, considera estacionalidad y revisa falsos positivos antes de escalar alertas.


**Práctica y evidencia:** Establece baseline de actividad y detecta desviaciones en telemetría sintética. **Evidencia:** mide falsos positivos y explica por qué anomalía no equivale a ataque.

#### 30.1.03 — Pattern Recognition
Pattern Recognition detecta regularidades en datos como secuencias, eventos o características de archivos. Documenta qué patrón se aprende y qué cambios legítimos pueden producir coincidencias.


**Práctica y evidencia:** Extrae patrones de eventos y compara frecuencia/ventana temporal. **Evidencia:** documenta características y límites de generalización.

#### 30.1.04 — Classification
Classification asigna observaciones a categorías mediante un modelo entrenado o reglas. Evalúa precisión, recall, F1 y matriz de confusión según el coste de falsos positivos y negativos.


**Práctica y evidencia:** Clasifica alertas por tipo usando conjunto etiquetado y matriz de confusión. **Evidencia:** reporta precision, recall y clases desbalanceadas.

#### 30.1.05 — Security Analytics
Security Analytics combina eventos, métricas y contexto para identificar riesgos y apoyar decisiones. Mantén calidad, procedencia y minimización de datos y explica límites de los modelos.


**Práctica y evidencia:** Combina señales de autenticación, red y endpoint para un caso de seguridad. **Evidencia:** identifica variables, sesgos y trazabilidad.

#### 30.1.06 — AI-assisted Investigation
AI-assisted Investigation puede resumir eventos, enriquecer indicadores y sugerir hipótesis para el analista. Verifica cada afirmación contra fuentes primarias y evita que el modelo cierre incidentes o ejecute acciones sin supervisión.


**Práctica y evidencia:** Usa IA para resumir una investigación sintética y exige verificación humana de cada afirmación. **Evidencia:** enlaza resumen con eventos fuente.

#### 30.1.07 — Limitations of AI in Security
Limitations of AI in Security incluyen falsos positivos, sesgo, datos incompletos, deriva, opacidad y manipulación adversarial. Define límites de uso, validación humana y procedimientos alternativos cuando el modelo falla.


**Práctica y evidencia:** Evalúa alucinación, sesgo, privacidad, explicabilidad y deriva en IA aplicada a seguridad. **Evidencia:** define casos donde la decisión debe permanecer humana.

### Módulo 30.2 — LLM Security

#### 30.2.01 — Large Language Models
Large Language Models generan texto y otras salidas a partir de patrones aprendidos y contexto de entrada. Pueden producir errores convincentes; verifica hechos, controla datos enviados y no trates la salida como autoridad.


**Práctica y evidencia:** Explica tokens, contexto, entrenamiento e inferencia de un LLM con un diagrama. **Evidencia:** distingue modelo, prompt, herramienta y fuente externa.

#### 30.2.02 — Prompt Injection
Prompt Injection ocurre cuando instrucciones maliciosas o no confiables influyen en el comportamiento de un modelo. Separa instrucciones de datos, limita herramientas y valida resultados en una capa externa al modelo.


**Práctica y evidencia:** Prueba prompt injection con instrucciones inocuas en un modelo local de laboratorio. **Evidencia:** documenta separación entre instrucciones confiables y contenido no confiable.

#### 30.2.03 — Indirect Prompt Injection
Indirect Prompt Injection llega mediante contenido externo que el modelo consulta, como páginas, documentos o resultados de búsqueda. Trata contenido recuperado como datos no confiables y evita que pueda modificar permisos o instrucciones de sistema.


**Práctica y evidencia:** Construye un documento sintético con instrucciones maliciosas embebidas y comprueba que el sistema no las obedezca. **Evidencia:** registra mitigación y fallo residual.

#### 30.2.04 — Jailbreaking
Jailbreaking intenta inducir al modelo a ignorar restricciones o políticas. Evalúa resistencia en entornos controlados, registra categorías de fallo y aplica defensa en profundidad en lugar de depender de una frase de sistema.


**Práctica y evidencia:** Evalúa intentos de jailbreak en un entorno de prueba con casos seguros y política definida. **Evidencia:** clasifica el resultado y evita usar datos reales o acciones externas.

#### 30.2.05 — Data Leakage
Data Leakage ocurre cuando el sistema revela datos privados, secretos, prompts internos o información de otros usuarios. Minimiza contexto, aplica autorización antes de recuperar datos y filtra salidas en límites de confianza.


**Práctica y evidencia:** Diseña un escenario donde el modelo recibe datos sensibles y aplica minimización/redacción. **Evidencia:** demuestra que el secreto no aparece en prompt, respuesta ni logs.

#### 30.2.06 — Context Manipulation
Context Manipulation altera la información que el modelo recibe para cambiar sus conclusiones o prioridades. Registra fuentes y procedencia, limita contexto recuperado y detecta instrucciones embebidas en documentos.


**Práctica y evidencia:** Prueba contexto contradictorio y fuentes de baja confianza en RAG de laboratorio. **Evidencia:** exige citas y declara incertidumbre.

#### 30.2.07 — Tool Abuse
Tool Abuse ocurre cuando un modelo invoca herramientas con parámetros o finalidades no autorizadas. Valida argumentos, aplica allowlists y permisos por acción y exige confirmación humana para operaciones de alto impacto.


**Práctica y evidencia:** Modela abuso de herramientas con una función simulada de lectura/escritura. **Evidencia:** comprueba validación de argumentos y confirmación para acciones sensibles.

#### 30.2.08 — Agent Security
Agent Security protege agentes que planifican y ejecutan acciones mediante herramientas o servicios. Separa planificación de ejecución, controla identidad y alcance y registra cada llamada con límites de presupuesto y tiempo.


**Práctica y evidencia:** Define límites de identidad, permisos, memoria, herramientas y auditoría para un agente. **Evidencia:** presenta threat model y controles por componente.

#### 30.2.09 — RAG Security
RAG Security protege pipelines de recuperación y generación frente a documentos maliciosos, filtración y acceso cruzado. Aplica autorización a nivel de documento, filtros por usuario y validación de fuentes antes de construir contexto.


**Práctica y evidencia:** Evalúa RAG con documentos sintéticos, permisos por usuario y filtrado de recuperación. **Evidencia:** demuestra que un usuario no recibe documentos ajenos.

#### 30.2.10 — Guardrails
Guardrails son controles de entrada, salida y ejecución que reducen usos no permitidos o resultados inseguros. No son infalibles; combínalos con autorización externa, validación determinista y monitoreo.


**Práctica y evidencia:** Define guardrails de entrada/salida y evalúa evasiones benignas. **Evidencia:** documenta cobertura y por qué no sustituyen controles de servidor.

#### 30.2.11 — Sandboxing
Sandboxing ejecuta código o herramientas en entornos aislados con recursos, red y filesystem restringidos. Define límites de CPU/memoria/tiempo, elimina credenciales del host y destruye el entorno tras la ejecución.


**Práctica y evidencia:** Ejecuta herramientas de agente en sandbox con filesystem y red limitados. **Evidencia:** prueba que la ejecución no accede al host ni a secretos.

#### 30.2.12 — Least Privilege for Agents
Least Privilege for Agents limita cada herramienta y agente a acciones, datos y recursos mínimos. Usa permisos temporales, separación por tarea y aprobación para operaciones irreversibles.


**Práctica y evidencia:** Asigna al agente solo permisos mínimos por herramienta y recurso. **Evidencia:** demuestra denegación de acción fuera del alcance.

### Módulo 30.3 — AI Red Teaming

#### 30.3.01 — Attack Surface
Attack Surface de un sistema de IA incluye modelo, prompts, datos, RAG, herramientas, plugins, APIs, identidad y despliegue. Inventaría cada límite de confianza y propietario y prioriza controles por impacto.


**Práctica y evidencia:** Dibuja superficie de ataque de una aplicación con LLM, RAG y herramientas. **Evidencia:** incluye entradas, salidas, datos, identidad y dependencias.

#### 30.3.02 — Adversarial Inputs
Adversarial Inputs son entradas diseñadas para inducir errores o comportamientos no deseados en modelos. Define categorías de prueba y datos sintéticos, evita probar sobre usuarios o datos reales sin autorización.


**Práctica y evidencia:** Construye entradas adversariales sintéticas y evalúa validación/normalización. **Evidencia:** registra casos y comportamiento esperado.

#### 30.3.03 — Prompt Injection Testing
Prompt Injection Testing evalúa si instrucciones no confiables pueden alterar tareas o políticas. Usa corpus de prueba controlado, mide impacto observable y valida mitigaciones fuera del prompt.


**Práctica y evidencia:** Diseña una batería de pruebas de prompt injection para un sistema local sin conectores externos. **Evidencia:** registra tasa de éxito y controles.

#### 30.3.04 — Tool-use Abuse
Tool-use Abuse Testing verifica si el modelo puede invocar herramientas fuera de permisos o con parámetros peligrosos. Usa herramientas simuladas, permisos mínimos y límites de ejecución para evitar efectos reales.


**Práctica y evidencia:** Simula una herramienta de bajo riesgo y prueba argumentos inesperados, permisos y límites. **Evidencia:** demuestra rechazo de acciones no permitidas.

#### 30.3.05 — Data Exfiltration Scenarios
Data Exfiltration Scenarios evalúa si información sensible puede salir por respuestas, herramientas, logs o contexto compartido. Utiliza canarios sintéticos y valida aislamiento entre usuarios y controles de salida.


**Práctica y evidencia:** Modela exfiltración con datos señuelo y verifica controles de salida. **Evidencia:** confirma que el agente no transmite datos a destinos no autorizados.

#### 30.3.06 — Model Evaluation
Model Evaluation mide calidad, robustez, seguridad y comportamiento del modelo con conjuntos de datos y métricas definidos. Registra versión, prompt, parámetros y entorno para reproducir resultados.


**Práctica y evidencia:** Evalúa modelo con dataset representativo, métricas y revisión humana. **Evidencia:** registra versión, configuración y limitaciones.

#### 30.3.07 — Security Testing of AI Systems
Security Testing of AI Systems combina pruebas de modelo, aplicación, datos, identidad y herramientas. Define alcance y riesgos, prueba fallos y abuso de permisos y documenta limitaciones.


**Práctica y evidencia:** Crea plan de seguridad para IA con abuso, privacidad, integridad, disponibilidad y supply chain. **Evidencia:** asocia pruebas y mitigaciones.

### Módulo 30.4 — Automatización con Python

#### 30.4.01 — Python avanzado
Python avanzado incluye iteradores, generadores, context managers, tipado, excepciones y concurrencia. Selecciona características que simplifiquen el mantenimiento y documenta versiones y dependencias.


**Práctica y evidencia:** Escribe un programa Python con tipos, context managers y manejo de errores. **Evidencia:** ejecuta pruebas unitarias y documenta versión.

#### 30.4.02 — OOP
OOP en Python organiza datos y comportamiento mediante clases, composición y protocolos. Mantén responsabilidades pequeñas y evita jerarquías profundas o estado global compartido.


**Práctica y evidencia:** Modela una clase con composición y métodos tipados. **Evidencia:** demuestra separación de responsabilidades.

#### 30.4.03 — Modules
Modules separan funciones, clases y constantes en unidades importables. Evita efectos secundarios durante importación y define interfaz pública clara.


**Práctica y evidencia:** Divide código en módulos con importaciones explícitas. **Evidencia:** evita efectos secundarios al importar.

#### 30.4.04 — Packages
Packages agrupan módulos bajo una estructura y espacio de nombres. Fija dependencias y versiones, controla origen y utiliza entornos virtuales para reproducibilidad.


**Práctica y evidencia:** Empaqueta una utilidad con dependencias declaradas y entorno reproducible. **Evidencia:** instala desde configuración limpia.

#### 30.4.05 — Requests
Requests facilita solicitudes HTTP desde Python y manejo de respuestas. Configura timeout, TLS, retries acotados y validación de status/content; nunca desactives verificación de certificados para resolver errores.


**Práctica y evidencia:** Realiza una solicitud HTTP con timeout, validación TLS y manejo de status. **Evidencia:** diferencia errores de red y HTTP.

#### 30.4.06 — JSON
JSON serializa estructuras de datos mediante objetos, arrays y valores básicos. Valida esquema y tamaño, maneja errores de parseo y no confíes en tipos o campos enviados por terceros.


**Práctica y evidencia:** Parsea JSON y valida esquema/valores antes de procesar. **Evidencia:** prueba entradas inválidas y campos inesperados.

#### 30.4.07 — YAML
YAML es un formato de configuración legible que admite estructuras anidadas. Usa loaders seguros, valida esquema y evita cargar documentos no confiables con constructores que permitan objetos arbitrarios.


**Práctica y evidencia:** Carga YAML con parser seguro y valida tipos. **Evidencia:** evita deserialización insegura y prueba contenido malformado.

#### 30.4.08 — Regex
Regex define patrones para buscar o validar texto. Controla complejidad para evitar ReDoS, utiliza patrones anclados cuando corresponda y prueba entradas largas y límites.


**Práctica y evidencia:** Usa expresiones regulares con límites y casos adversariales para evitar backtracking excesivo. **Evidencia:** mide tiempo con entradas de prueba.

#### 30.4.09 — subprocess
subprocess permite ejecutar procesos externos y capturar entradas/salidas desde Python. Evita `shell=True` con datos no confiables, pasa argumentos separados, limita tiempo y permisos y registra errores sin secretos.


**Práctica y evidencia:** Invoca un proceso local con lista de argumentos, timeout y entorno controlado. **Evidencia:** no concatena entrada no confiable en shell.

#### 30.4.10 — Sockets
Sockets permiten comunicación de bajo nivel sobre protocolos de red. Define timeouts, framing, validación de mensajes y cierre; practica únicamente con servicios propios o autorizados.


**Práctica y evidencia:** Crea socket de laboratorio en localhost y valida datos recibidos. **Evidencia:** maneja timeout, tamaño y cierre.

#### 30.4.11 — Asyncio
asyncio ofrece concurrencia cooperativa para operaciones asíncronas. Usa tareas y semáforos para limitar concurrencia, propaga cancelación y evita bloquear el event loop con operaciones síncronas.


**Práctica y evidencia:** Implementa concurrencia con asyncio y maneja cancelación/timeout. **Evidencia:** demuestra que una tarea cancelada libera recursos.

#### 30.4.12 — Logging
Logging registra eventos de ejecución con niveles, contexto y destinos configurables. Usa datos estructurados, correlación y rotación; redacta credenciales, tokens y datos personales.


**Práctica y evidencia:** Configura logging estructurado con niveles y redacción de secretos. **Evidencia:** verifica que token y contraseña no aparecen en logs.

#### 30.4.13 — APIs
APIs permiten integrar servicios mediante contratos HTTP u otros protocolos. Gestiona autenticación, cuotas, paginación, errores y cambios de versión y no expongas claves en código.


**Práctica y evidencia:** Consume una API de prueba con autenticación segura y límites de reintento. **Evidencia:** maneja rate limit y no registra credenciales.

#### 30.4.14 — File Processing
File Processing lee y transforma archivos de texto, datos estructurados y binarios. Valida rutas, tamaño, codificación y tipo real; evita path traversal y sobrescritura accidental.


**Práctica y evidencia:** Procesa archivos de laboratorio con límites de tamaño y rutas seguras. **Evidencia:** rechaza traversal y conserva integridad.

### Módulo 30.5 — Automatización de seguridad

#### 30.5.01 — Log Processing
Log Processing normaliza y filtra eventos para extraer información útil. Conserva timestamp, origen y campos de correlación y protege registros contra alteración y filtración.


**Práctica y evidencia:** Procesa logs sintéticos y normaliza timestamp, host, usuario y evento. **Evidencia:** conserva origen y evita descartar campos relevantes.

#### 30.5.02 — IOC Extraction
IOC Extraction identifica indicadores potenciales en logs, documentos o alertas. Valida formato, contexto, confianza y vigencia antes de distribuir o bloquear indicadores.


**Práctica y evidencia:** Extrae IOC de un reporte de prueba y asigna fuente/confianza/caducidad. **Evidencia:** evita publicar indicadores sin contexto.

#### 30.5.03 — Threat Intelligence Collection
Threat Intelligence Collection reúne información de fuentes abiertas, feeds y reportes autorizados. Registra procedencia, licencia, frescura y confianza y evita recopilar datos personales innecesarios.


**Práctica y evidencia:** Consulta una fuente de threat intelligence autorizada y almacena metadatos mínimos. **Evidencia:** registra licencia y fecha.

#### 30.5.04 — Report Generation
Report Generation automatiza informes con plantillas y datos estructurados. Verifica exactitud, contexto y destinatarios y elimina secretos y datos sensibles de los documentos generados.


**Práctica y evidencia:** Genera reporte automático desde hallazgos estructurados y revisa salida humana. **Evidencia:** comprueba que no inventa campos ausentes.

#### 30.5.05 — API Integrations
API Integrations conectan automatizaciones con SIEM, ticketing, inventarios y fuentes de inteligencia. Usa tokens de mínimo privilegio, paginación, retries limitados y manejo de rate limits.


**Práctica y evidencia:** Integra una API de prueba con token desde secret store y timeout. **Evidencia:** demuestra rotación y manejo de errores.

#### 30.5.06 — Vulnerability Reporting
Vulnerability Reporting convierte hallazgos en reportes con activo, versión, evidencia, impacto y remediación. Valida falsos positivos y no adjunta datos sensibles innecesarios.


**Práctica y evidencia:** Convierte hallazgos de vulnerabilidad a un reporte con activo, CVE, riesgo y remediación. **Evidencia:** vincula cada campo a fuente.

#### 30.5.07 — Alert Classification
Alert Classification prioriza alertas por severidad, confianza, activo y contexto. Documenta criterios y permite revisión humana para casos ambiguos.


**Práctica y evidencia:** Clasifica alertas sintéticas y mide precisión/recall. **Evidencia:** conserva conjunto etiquetado y revisión de falsos positivos.

#### 30.5.08 — Security Automation Pipelines
Security Automation Pipelines encadenan recolección, análisis, enriquecimiento y notificación. Diseña etapas idempotentes, permisos mínimos, observabilidad y aprobación para acciones de alto impacto.


**Práctica y evidencia:** Diseña pipeline de automatización con validación, aprobación humana y rollback. **Evidencia:** identifica acciones que no deben ejecutarse automáticamente.

### Módulo 30.6 — Threat Intelligence avanzado

#### 30.6.01 — Threat Intelligence Lifecycle
Threat Intelligence Lifecycle organiza dirección, recolección, procesamiento, análisis, difusión y retroalimentación. Define requisitos del consumidor y mide si la inteligencia cambia una decisión.


**Práctica y evidencia:** Dibuja ciclo de inteligencia: dirección, colección, procesamiento, análisis, difusión y feedback. **Evidencia:** vincula producto con decisión.

#### 30.6.02 — OSINT Automation
OSINT Automation automatiza consultas a fuentes públicas dentro de términos y límites permitidos. Controla frecuencia, registra fuentes y minimiza datos personales.


**Práctica y evidencia:** Automatiza OSINT sobre activos propios usando fuentes permitidas y límites de consulta. **Evidencia:** registra origen y minimiza datos personales.

#### 30.6.03 — MITRE ATT&CK
MITRE ATT&CK estructura conocimiento sobre tácticas y técnicas adversarias. Usa versión y plataforma, vincula detecciones y no atribuyas actor a partir de un único mapeo.


**Práctica y evidencia:** Relaciona un hallazgo con ATT&CK y documenta técnica y telemetría. **Evidencia:** registra versión de matriz.

#### 30.6.04 — TTP Correlation
TTP Correlation relaciona comportamientos observados con técnicas y secuencias conocidas. Evalúa evidencia, temporalidad y alternativas benignas y evita sobreajustar una conclusión.


**Práctica y evidencia:** Correlaciona TTPs entre dos reportes y separa similitud de atribución. **Evidencia:** justifica nivel de confianza.

#### 30.6.05 — Threat Feeds
Threat Feeds distribuyen indicadores y contexto de amenazas. Evalúa calidad, licencia, frescura y falsos positivos y automatiza expiración y revisión.


**Práctica y evidencia:** Consume feed de prueba, valida formato y deduplica indicadores caducos. **Evidencia:** documenta fuente y política de expiración.

#### 30.6.06 — Intelligence Analysis
Intelligence Analysis evalúa fuentes, corroboración, hipótesis y confianza para producir conclusiones accionables. Distingue hechos de inferencias y declara vacíos de información.


**Práctica y evidencia:** Redacta análisis de inteligencia con hipótesis, evidencia, confianza y alternativas. **Evidencia:** separa hechos de inferencias.

### Módulo 30.7 — Criptografía avanzada

#### 30.7.01 — Symmetric Cryptography
Symmetric Cryptography utiliza una clave compartida para cifrar y descifrar o autenticar datos. Protege distribución y almacenamiento de claves y utiliza modos autenticados modernos.


**Práctica y evidencia:** Compara cifrado simétrico y asimétrico por rendimiento, distribución de claves y uso. **Evidencia:** selecciona mecanismo para un escenario.

#### 30.7.02 — Asymmetric Cryptography
Asymmetric Cryptography utiliza pares de claves pública/privada para operaciones como establecimiento de claves y firmas. Comprende usos distintos y protege claves privadas y validación de identidad.


**Práctica y evidencia:** Dibuja intercambio de clave y firma con criptografía asimétrica. **Evidencia:** distingue confidencialidad de autenticidad.

#### 30.7.03 — AES
AES es un cifrador de bloque estandarizado con clave de 128, 192 o 256 bits. Utiliza modos seguros y autenticados como AES-GCM con nonces únicos; no diseñes modos propios.


**Práctica y evidencia:** Utiliza AES mediante biblioteca mantenida y modo autenticado recomendado. **Evidencia:** explica nonce/IV y por qué no reutilizarlo.

#### 30.7.04 — RSA
RSA es un sistema de clave pública usado para cifrado y firmas bajo esquemas adecuados. Selecciona padding moderno y tamaños conforme a estándares; no utilices RSA textbook ni implementes primitivas propias.


**Práctica y evidencia:** Analiza RSA para firma o intercambio según esquema actual y tamaños de clave aceptados por política. **Evidencia:** no usa RSA para cifrado directo de grandes volúmenes.

#### 30.7.05 — ECC
ECC agrupa criptografía de curvas elípticas para firmas y acuerdo de claves. Utiliza curvas y bibliotecas aprobadas, valida puntos y parámetros y protege generación de aleatoriedad.


**Práctica y evidencia:** Compara curvas elípticas y operaciones de clave pública mediante biblioteca. **Evidencia:** identifica curva y protocolo compatibles.

#### 30.7.06 — Hashing
Hashing transforma datos en un resumen de longitud fija y se usa para integridad y otras funciones. Un hash general no es adecuado para almacenar contraseñas; selecciona algoritmo según propósito.


**Práctica y evidencia:** Compara hash criptográfico con checksum y función de password hashing. **Evidencia:** selecciona herramienta según integridad, firma o contraseñas.

#### 30.7.07 — SHA-2
SHA-2 es una familia de funciones hash que incluye SHA-256 y SHA-512. Se utiliza para integridad y construcción criptográfica, pero no cifra ni autentica por sí sola.


**Práctica y evidencia:** Calcula SHA-256 sobre archivo de prueba y verifica integridad tras transferencia. **Evidencia:** explica que hash no autentica origen por sí solo.

#### 30.7.08 — SHA-3
SHA-3 se basa en la construcción Keccak y ofrece funciones hash y extendibles. Distingue SHA3-256 de SHAKE y selecciona variante según protocolo y estándar.


**Práctica y evidencia:** Compara propiedades de SHA-3 con SHA-2 según especificación. **Evidencia:** identifica función y salida sin asumir compatibilidad entre familias.

#### 30.7.09 — Digital Signatures
Digital Signatures permiten verificar integridad y autenticidad del firmante mediante clave pública. Gestiona certificados y claves, valida contexto y revocación y no confundas firma con cifrado.


**Práctica y evidencia:** Firma y verifica un mensaje con biblioteca criptográfica. **Evidencia:** demuestra fallo tras modificar el mensaje y explica custodia de clave privada.

#### 30.7.10 — PKI
PKI administra certificados, autoridades de certificación, claves y políticas de confianza. Define emisión, renovación, revocación y protección de claves raíz y operativas.


**Práctica y evidencia:** Dibuja PKI con CA, certificado, cadena y revocación. **Evidencia:** verifica SAN, issuer, vigencia y confianza.

#### 30.7.11 — TLS
TLS protege canales de comunicación y autentica extremos según configuración. Mantén versiones y suites soportadas, valida certificados y comprende que la seguridad depende también de identidad y aplicación.


**Práctica y evidencia:** Inspecciona una conexión TLS y explica handshake, certificado y claves de sesión. **Evidencia:** distingue TLS de algoritmo de aplicación.

#### 30.7.12 — Key Management
Key Management cubre generación, almacenamiento, distribución, rotación, respaldo y destrucción de claves. Separa funciones, limita acceso, registra operaciones y planifica recuperación y compromiso.


**Práctica y evidencia:** Diseña ciclo de vida de claves: generación, almacenamiento, rotación, backup, revocación y destrucción. **Evidencia:** define responsables y auditoría.

### Módulo 30.8 — Criptografía poscuántica

#### 30.8.01 — Quantum Computing Concepts
Quantum Computing Concepts estudia qubits, superposición, entrelazamiento y algoritmos cuánticos relevantes para criptografía. Distingue capacidades teóricas y hardware actual y evita afirmar que cualquier computador cuántico rompe hoy toda criptografía.


**Práctica y evidencia:** Explica qubits, superposición, entrelazamiento y medición sin extrapolar capacidades actuales. **Evidencia:** diferencia concepto físico de impacto criptográfico práctico.

#### 30.8.02 — Harvest Now, Decrypt Later
Harvest Now, Decrypt Later describe la captura actual de datos cifrados con intención de descifrarlos en el futuro si la capacidad criptanalítica mejora. Prioriza información con vida útil larga y evalúa migración según sensibilidad y horizonte.


**Práctica y evidencia:** Modela riesgo Harvest Now, Decrypt Later para datos de larga confidencialidad. **Evidencia:** prioriza datos por vida útil y plan de migración.

#### 30.8.03 — Post-Quantum Cryptography
Post-Quantum Cryptography desarrolla algoritmos clásicos diseñados para resistir ataques de computadores cuánticos a gran escala. Distingue criptografía poscuántica de criptografía cuántica y utiliza estándares y bibliotecas mantenidas.


**Práctica y evidencia:** Compara familias de criptografía poscuántica y criterios de estandarización. **Evidencia:** consulta estándares NIST publicados y registra fecha/versión.

#### 30.8.04 — ML-KEM
ML-KEM es un mecanismo de encapsulación de claves basado en retículos, estandarizado por NIST en FIPS 203. Permite establecer un secreto compartido; no es un algoritmo de cifrado de archivos por sí solo y requiere implementación validada.


**Práctica y evidencia:** Identifica ML-KEM según FIPS 203 y describe encapsulación/decapsulación de claves. **Evidencia:** distingue mecanismo de establecimiento de clave de cifrado de datos.

#### 30.8.05 — ML-DSA
ML-DSA es un esquema de firma digital basado en retículos estandarizado por NIST en FIPS 204. Se usa para firmar y verificar, no para cifrar; verifica parámetros, claves y actualizaciones/erratas del estándar.


**Práctica y evidencia:** Identifica ML-DSA según FIPS 204 y explica firma/verificación. **Evidencia:** distingue firma digital de cifrado.

#### 30.8.06 — SLH-DSA
SLH-DSA es un esquema de firma digital poscuántica basado en hashes, estandarizado por NIST en FIPS 205. Comprende compensaciones de tamaño y rendimiento y utiliza implementaciones conformes.


**Práctica y evidencia:** Identifica SLH-DSA según FIPS 205 y explica firmas basadas en hash. **Evidencia:** compara tamaño/propiedades sin inventar parámetros.

#### 30.8.07 — Cryptographic Migration
Cryptographic Migration inventaría algoritmos, protocolos, claves y dependencias para sustituir mecanismos vulnerables o obsoletos. Prioriza activos y datos de larga vida, prueba interoperabilidad y planifica transición reversible.


**Práctica y evidencia:** Diseña inventario criptográfico y plan de migración por sistema y dependencia. **Evidencia:** identifica compatibilidad, prioridad y rollback.

#### 30.8.08 — Crypto Agility
Crypto Agility permite cambiar algoritmos y parámetros sin rediseñar por completo sistemas y protocolos. Abstrae suites criptográficas, inventaría dependencias y prueba actualización, revocación y compatibilidad.


**Práctica y evidencia:** Define crypto agility para cambiar algoritmos/proveedores mediante configuración y formatos versionados. **Evidencia:** demuestra transición sin rediseño completo.

#### 30.8.09 — CSRC
CSRC es el Computer Security Resource Center de NIST, repositorio de publicaciones y recursos técnicos, no un estándar individual. Identifica cada documento por número, revisión y fecha antes de adoptarlo.



**Práctica y evidencia:** Localiza FIPS y publicaciones de criptografía poscuántica en NIST CSRC y verifica estado final frente a borrador. **Evidencia:** registra URL, número y fecha.

### Referencias oficiales de criptografía poscuántica

- NIST FIPS 203 — ML-KEM: https://csrc.nist.gov/pubs/fips/203/final
- NIST FIPS 204 — ML-DSA: https://csrc.nist.gov/pubs/fips/204/final
- NIST FIPS 205 — SLH-DSA: https://csrc.nist.gov/pubs/fips/205/final
- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography

Verifica erratas y revisiones de cada publicación antes de implementar. No implementes algoritmos criptográficos propios ni interpretes el carácter poscuántico como garantía absoluta de seguridad.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 75 orientaciones genéricas por explicaciones específicas de IA aplicada a seguridad, LLM/agent security, AI red teaming, Python, automatización, threat intelligence, criptografía y migración poscuántica.

**Revisión interna:** 75/75 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron límites de modelos, prompt injection, RAG, abuso de herramientas, sandboxing, permisos de agentes, manejo seguro de subprocess/archivos y gestión de claves. Se añadieron referencias NIST para FIPS 203/204/205 y se diferenció ML-KEM (encapsulación de claves) de ML-DSA/SLH-DSA (firmas). Pendiente: validar implementaciones y erratas vigentes, ejecutar pruebas en entornos aislados y realizar segunda revisión especializada. No se ejecutaron pruebas de IA ni se implementó criptografía; no se declara aprobación externa.
