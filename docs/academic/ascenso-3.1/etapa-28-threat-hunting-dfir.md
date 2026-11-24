# Etapa 28 — Threat Hunting, respuesta a incidentes y forense digital

**Prioridad:** P2/P3 · Especialización avanzada  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** investigar incidentes y reconstruir qué ocurrió en un sistema comprometido.  
**Proyecto oficial:** investigar un incidente simulado, construir una línea temporal, identificar la causa, determinar el impacto y elaborar un informe forense.

## Principios de evidencia
La práctica utiliza imágenes, logs y artefactos sintéticos o de laboratorio con autorización. Preserva originales, calcula hashes, registra cadena de custodia, limita accesos y documenta cada acción. No analices dispositivos de terceros ni extraigas datos personales sin base legal y autorización.

## Resultados de aprendizaje
Formular hipótesis de hunting; usar telemetría e inteligencia de amenazas; seguir un proceso de respuesta; preservar evidencia; realizar análisis básico de disco, memoria, sistema de archivos y logs; reconstruir timelines; y documentar conclusiones con límites de confianza.

## 28.1 — Threat Hunting
Threat Hunting busca actividad no detectada mediante hipótesis, telemetría y análisis. Una hipótesis debe ser comprobable y acotada. Define fuentes de datos, ventana temporal, población, consultas, resultados esperados y limitaciones. Correlaciona indicadores, anomalías y TTP; evita convertir una coincidencia aislada en atribución.

**Ejercicio:** formula hipótesis con logs sintéticos, documenta consulta, resultado y evidencia que refutaría la hipótesis.

## 28.2 — Inteligencia de amenazas
Threat Intelligence analiza threat actors, campañas, patrones, IOC, IOA, MITRE ATT&CK y threat feeds/reports. Evalúa procedencia, fecha, confianza, contexto y expiración de indicadores. Un indicador puede ser compartido, reutilizado o falso positivo; no bloquees automáticamente sin evaluar impacto.

ATT&CK organiza tácticas y técnicas observadas. No es una secuencia obligatoria ni una prueba de que un actor específico estuvo presente.

## 28.3 — Incident Response
Un proceso de respuesta incluye preparación, identificación, análisis, contención, erradicación, recuperación y lecciones aprendidas. NIST SP 800-61 Rev. 3 conecta respuesta a incidentes con gestión de riesgo. Define roles, canales alternativos, severidad, preservación de evidencia, comunicaciones y criterios de escalamiento.

Contención debe equilibrar frenar daño y preservar evidencia. Recuperación verifica que servicios vuelvan a operar de forma segura. Lessons learned transforma hallazgos en mejoras concretas.

**Ejercicio:** simula una alerta de acceso sospechoso en laboratorio; registra decisiones, tiempo, evidencia y criterios de contención.

## 28.4 — Forense digital (DFIR)
Digital Forensics analiza evidencia digital con métodos reproducibles. Evidence Preservation conserva originales y metadatos. Chain of Custody registra quién obtuvo, transfirió, almacenó y examinó evidencia, cuándo y cómo. Disk forensics examina imágenes de almacenamiento; memory forensics analiza memoria volátil; file system analysis estudia estructuras; metadata aporta contexto; timeline analysis correlaciona eventos; log analysis integra telemetría.

Trabaja sobre copias verificadas, no originales. Calcula hashes antes/después, documenta herramientas y versiones, zona horaria y errores. Distingue observación, inferencia e hipótesis. No afirmes causalidad sin evidencia suficiente.

## 28.5 — Herramientas
Autopsy y The Sleuth Kit apoyan análisis de disco; Volatility analiza imágenes de memoria; KAPE recopila artefactos según configuración; Sysmon aporta eventos de Windows; herramientas de Eric Zimmerman ayudan a examinar artefactos. Verifica versión, origen, compatibilidad y documentación. Las herramientas automatizan tareas, no sustituyen interpretación.

**Ejercicio:** analiza una imagen sintética/educativa, registra hashes, extrae timeline y explica qué conclusiones sí/no permite.

## 28.6 — Estándares
NIST SP 800-61 Rev. 3 es la referencia indicada para respuesta a incidentes; NIST CSF 2.0 ayuda a situar resultados de gestión de ciberseguridad; MITRE ATT&CK aporta vocabulario de tácticas y técnicas. Consulta la edición oficial vigente y no reproduzcas material protegido extensamente.

## Proyecto oficial — Investigación de incidente simulado
### Fases
1. Define escenario, alcance y roles.
2. Recibe un paquete de evidencias sintéticas.
3. Registra hashes y cadena de custodia.
4. Formula hipótesis y plan de análisis.
5. Construye timeline normalizado.
6. Correlaciona logs, artefactos y telemetría.
7. Identifica causa probable y alcance con nivel de confianza.
8. Propone contención, erradicación y recuperación.
9. Documenta limitaciones y evidencia faltante.
10. Presenta informe técnico y resumen ejecutivo.

### Entregables
Registro de custodia, hashes, metodología, timeline, evidencias sanitizadas, hallazgos, hipótesis y confianza, impacto, acciones de respuesta, lecciones aprendidas e informe.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Preservación y cadena de custodia | 20 |
| Hipótesis y threat hunting | 15 |
| Análisis de inteligencia | 10 |
| Proceso de respuesta | 15 |
| Análisis forense y timeline | 20 |
| Herramientas y reproducibilidad | 10 |
| Informe y limitaciones | 10 |

Criterio orientativo: 80/100; pérdida de trazabilidad de evidencia crítica exige repetir el ejercicio.

## Autoevaluación
1. ¿Qué diferencia hunting de alert triage?
2. ¿Cómo se valida un indicador de amenaza?
3. ¿Por qué ATT&CK no demuestra atribución?
4. ¿Cuáles son las fases de respuesta?
5. ¿Qué equilibrio existe entre contención y preservación?
6. ¿Qué registra una cadena de custodia?
7. ¿Por qué se analiza una copia y no el original?
8. ¿Qué diferencia hay entre análisis de disco y memoria?
9. ¿Cómo expresas nivel de confianza?
10. ¿Qué limitaciones deben incluirse en un informe?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán solo recursos hablados en español y directamente relacionados con threat hunting, respuesta, cadena de custodia o herramientas forenses, utilizando evidencias de laboratorio.

## Referencias oficiales
- NIST SP 800-61 Rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- MITRE ATT&CK: https://attack.mitre.org/
- Autopsy: https://www.autopsy.com/
- The Sleuth Kit: https://www.sleuthkit.org/
- Volatility 3: https://volatility3.readthedocs.io/
- KAPE: https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-and-extractor-kape
- Sysmon: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- NIST SP 800-86: https://csrc.nist.gov/pubs/sp/800/86/final

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se analizaron imágenes ni evidencias reales en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 28

Este desglose conserva los títulos y el orden del roadmap maestro. Las guías de estudio se orientan a administración defensiva, monitoreo y análisis autorizado; no constituyen evidencia de operación en un entorno empresarial.

### Módulo 28.1 — Threat Hunting

#### 28.1.01 — Hipótesis
Una hipótesis de Threat Hunting plantea una explicación comprobable sobre actividad posiblemente maliciosa o no esperada. Formula qué buscar, por qué es plausible, qué fuentes lo pueden confirmar y qué evidencia refutaría la hipótesis.

#### 28.1.02 — Telemetría
Telemetría reúne eventos, métricas y registros de endpoints, red, identidad y aplicaciones. Evalúa cobertura, integridad, sincronización y retención antes de concluir que la ausencia de eventos significa ausencia de actividad.

#### 28.1.03 — Threat Indicators
Threat Indicators son señales que pueden asociarse con actividad de amenaza, como hashes, dominios o comportamientos. Registra procedencia, confianza y vigencia y evita bloquear automáticamente indicadores sin contexto.

#### 28.1.04 — Anomaly Detection
Anomaly Detection identifica desviaciones respecto de líneas base de comportamiento. Considera cambios legítimos, estacionalidad y calidad de datos; una anomalía es una pista, no una confirmación de incidente.

#### 28.1.05 — Event Correlation
Event Correlation relaciona eventos de distintas fuentes mediante tiempo, identidad, activo y comportamiento. Normaliza datos, controla desfases de reloj y documenta reglas de correlación.

#### 28.1.06 — TTP
TTP describe tácticas, técnicas y procedimientos observados en comportamientos adversarios. Mapea a marcos como MITRE ATT&CK con versión y plataforma, sin atribuir actor a partir de una sola técnica.

#### 28.1.07 — Threat Investigation
Threat Investigation valida hipótesis, delimita alcance y determina si existe actividad maliciosa. Conserva evidencia, separa hechos de inferencias y escala cuando el impacto o incertidumbre supera la autoridad del analista.

#### 28.1.08 — Documentation
Documentation registra hipótesis, consultas, fuentes, timestamps, hallazgos, limitaciones y conclusiones. Permite reproducibilidad y revisión por pares y debe proteger datos sensibles.

### Módulo 28.2 — Inteligencia de amenazas

#### 28.2.01 — Threat Intelligence
Threat Intelligence transforma información sobre amenazas en conocimiento contextual y accionable para decisiones defensivas. Define requisitos de inteligencia, fuentes, confianza y audiencia; evita coleccionar indicadores sin uso operativo.

#### 28.2.02 — Threat Actors
Threat Actors son personas o grupos que realizan actividades con objetivos y capacidades determinadas. Usa atribución con cautela y diferencia identidad confirmada, agrupación analítica e hipótesis.

#### 28.2.03 — Campaigns
Campaigns agrupan actividades relacionadas en un periodo y contexto, posiblemente asociadas a un objetivo. Correlaciona infraestructura, TTP y víctimas con evidencia y registra incertidumbre.

#### 28.2.04 — Attack Patterns
Attack Patterns describen secuencias o métodos recurrentes que pueden conducir a compromisos. Úsalos para diseñar controles y detecciones, sin tratarlos como una receta de ejecución.

#### 28.2.05 — IOC
IOC son artefactos observables asociados a posible compromiso. Añade fuente, fecha, confianza, contexto y expiración; los indicadores pueden ser compartidos o reutilizados por actividad legítima.

#### 28.2.06 — IOA
IOA se centra en comportamientos que indican una posible acción adversaria. Diseña detecciones resistentes a cambios superficiales de infraestructura y valida con actividad benigna.

#### 28.2.07 — MITRE ATT&CK
MITRE ATT&CK organiza tácticas y técnicas observadas en plataformas y entornos. Mapea detecciones y brechas con versión y fuente; cobertura de técnicas no equivale a cobertura completa de amenazas.

#### 28.2.08 — Threat Feeds
Threat Feeds distribuyen indicadores y contexto desde proveedores o comunidades. Evalúa calidad, licencias, frescura y falsos positivos y evita integrar feeds sin proceso de validación.

#### 28.2.09 — Threat Reports
Threat Reports comunican actores, campañas, TTP, indicadores, impacto y recomendaciones. Distingue observaciones de atribución, incluye fecha y fuentes y adapta detalle a la audiencia.

### Módulo 28.3 — Incident Response

#### 28.3.01 — Preparation
Preparation establece políticas, responsables, herramientas, contactos, respaldos y ejercicios antes de un incidente. Comprueba que accesos y procedimientos funcionen y que las decisiones críticas tengan autoridad asignada.

#### 28.3.02 — Identification
Identification determina si un evento constituye incidente y cuál es su alcance inicial. Correlaciona fuentes, clasifica impacto y conserva evidencia sin retrasar contención cuando exista riesgo inmediato.

#### 28.3.03 — Analysis
Analysis investiga causa, alcance, vector y efectos del incidente con evidencia verificable. Mantén línea temporal, hipótesis y nivel de confianza y evita modificar fuentes originales.

#### 28.3.04 — Containment
Containment limita propagación e impacto mediante aislamiento, bloqueo o restricción temporal. Selecciona acciones proporcionales, coordina con operaciones y documenta efectos colaterales y autorizaciones.

#### 28.3.05 — Eradication
Eradication elimina causa y persistencia del incidente mediante limpieza, parcheo, rotación de credenciales o reconstrucción. Verifica que no queden mecanismos asociados y conserva evidencia necesaria.

#### 28.3.06 — Recovery
Recovery restaura servicios desde estados confiables y valida integridad y monitoreo reforzado. Define criterios de retorno, comunicación y observación posterior para detectar recurrencia.

#### 28.3.07 — Lessons Learned
Lessons Learned analiza causas, decisiones, controles y oportunidades después del incidente. Convierte hallazgos en acciones con responsable y fecha y evita una retrospectiva centrada en culpabilizar.

#### 28.3.08 — Incident Reporting
Incident Reporting documenta cronología, impacto, decisiones, evidencias, comunicaciones y acciones. Adapta el reporte a destinatarios y obligaciones y evita exponer datos personales o detalles sensibles innecesarios.

### Módulo 28.4 — Forense digital (DFIR)

#### 28.4.01 — Digital Forensics
Digital Forensics aplica métodos reproducibles para identificar, adquirir, preservar y analizar evidencia digital. Mantén integridad, documentación y cadena de custodia y trabaja sobre copias verificadas.

#### 28.4.02 — Incident Response
Incident Response coordina decisiones para gestionar un incidente y reducir impacto. Se articula con forense, operaciones, legal y comunicaciones; preservación de evidencia debe equilibrarse con urgencia de contención.

#### 28.4.03 — Evidence Preservation
Evidence Preservation protege artefactos contra modificación, pérdida o acceso no autorizado. Registra origen, hora, herramienta, operador, hash y almacenamiento y conserva originales protegidos.

#### 28.4.04 — Chain of Custody
Chain of Custody registra cada transferencia, acceso y manipulación de evidencia. Mantén identidad de custodios, fecha, propósito y controles de integridad para permitir revisión posterior.

#### 28.4.05 — Disk Forensics
Disk Forensics analiza medios de almacenamiento y estructuras de archivos para reconstruir actividad. Adquiere imágenes con procedimientos adecuados, verifica hashes y analiza copias para evitar alterar originales.

#### 28.4.06 — Memory Forensics
Memory Forensics examina volcados de memoria para buscar procesos, conexiones y artefactos volátiles. Documenta método y versión de herramientas y protege dumps porque pueden contener credenciales y datos personales.

#### 28.4.07 — File System Analysis
File System Analysis estudia metadatos, estructuras, timestamps y artefactos de sistemas de archivos. Considera zona horaria, precisión y cambios de reloj y evita interpretar timestamps como evidencia aislada.

#### 28.4.08 — Metadata
Metadata describe atributos asociados a archivos y artefactos, como creación, modificación, autor o dispositivo. Puede ser alterada o heredada; corrobora con otras fuentes y minimiza exposición de datos personales.

#### 28.4.09 — Timeline Analysis
Timeline Analysis ordena eventos de múltiples fuentes para reconstruir secuencias. Normaliza zonas horarias y precisión, documenta huecos y distingue hora del evento de hora de recolección.

#### 28.4.10 — Log Analysis
Log Analysis interpreta registros de seguridad, aplicaciones y sistemas para identificar actividad relevante. Conserva fuente y contexto, correlaciona eventos y evita conclusiones basadas en logs incompletos.

#### 28.4.11 — Incident Reconstruction
Incident Reconstruction integra evidencias para explicar qué ocurrió, cuándo, cómo y con qué impacto. Presenta hipótesis alternativas, nivel de confianza y limitaciones sin afirmar más de lo que sostienen los datos.

### Módulo 28.5 — Herramientas

#### 28.5.01 — Autopsy
Autopsy ofrece una interfaz para análisis forense digital y casos basados en imágenes de evidencia. Trabaja sobre copias verificadas, registra módulos utilizados y protege bases de casos.

#### 28.5.02 — Sleuth Kit
The Sleuth Kit proporciona herramientas para analizar sistemas de archivos e imágenes forenses. Verifica hashes, documenta comandos y versiones y evita operar sobre el medio original.

#### 28.5.03 — Volatility
Volatility analiza volcados de memoria para extraer información de procesos, módulos y artefactos. Selecciona versión y símbolos compatibles y trata resultados como evidencia que requiere corroboración.

#### 28.5.04 — KAPE
KAPE recopila y procesa artefactos forenses de Windows mediante objetivos y módulos configurados. Define alcance, evita recolección indiscriminada y protege resultados sensibles.

#### 28.5.05 — Sysmon
Sysmon aporta telemetría detallada de Windows que puede apoyar investigación y hunting. Verifica configuración, retención y continuidad y correlaciona eventos con otras fuentes.

#### 28.5.06 — Eric Zimmerman Tools (introducción)
Eric Zimmerman Tools reúne utilidades para analizar artefactos de Windows y sistemas de archivos. Documenta herramienta y versión, trabaja con copias y corrobora resultados con fuentes independientes.

### Módulo 28.6 — Estándares

#### 28.6.01 — NIST SP 800-61
NIST SP 800-61 proporciona orientación para manejo de incidentes de seguridad informática. Consulta la revisión vigente y adapta roles, preparación, detección, respuesta y mejora al entorno organizacional.

#### 28.6.02 — NIST CSF 2.0
NIST CSF 2.0 organiza resultados de gestión de riesgo mediante Govern, Identify, Protect, Detect, Respond y Recover. Utilízalo para conectar hunting y DFIR con gobernanza y mejora continua.

#### 28.6.03 — MITRE ATT&CK
MITRE ATT&CK sirve como base de conocimiento para mapear comportamientos, detecciones y cobertura defensiva. Registra versión, plataforma y fuentes y no lo uses como sustituto de evidencia forense.

#### 28.6.04 — CSRC
CSRC es el Computer Security Resource Center de NIST, un repositorio de publicaciones y recursos técnicos, no un estándar único. Identifica cada publicación por número, título, revisión y fecha antes de incorporarla a procedimientos.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 46 orientaciones genéricas por explicaciones específicas de Threat Hunting, inteligencia de amenazas, respuesta a incidentes, DFIR, herramientas y estándares.

**Revisión interna:** 46/46 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron hipótesis verificables, confianza de indicadores, preservación de evidencia, cadena de custodia, protección de volcados/logs y distinción entre hallazgos e inferencias. La entrada CSRC se aclara como repositorio de recursos NIST, no como estándar individual. Pendiente: validar procedimientos con evidencia sintética en laboratorio, comprobar compatibilidad de herramientas y revisión especializada. No se procesaron imágenes forenses ni se investigaron incidentes reales; no se declara aprobación externa.
