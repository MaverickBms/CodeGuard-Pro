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
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.02 — Telemetría
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.03 — Threat Indicators
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.04 — Anomaly Detection
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.05 — Event Correlation
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.06 — TTP
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.07 — Threat Investigation
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.1.08 — Documentation
Comprender el concepto, los datos o controles involucrados y su papel dentro de threat hunting; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 28.2 — Inteligencia de amenazas

#### 28.2.01 — Threat Intelligence
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.02 — Threat Actors
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.03 — Campaigns
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.04 — Attack Patterns
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.05 — IOC
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.06 — IOA
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.07 — MITRE ATT&CK
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.08 — Threat Feeds
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.2.09 — Threat Reports
Comprender el concepto, los datos o controles involucrados y su papel dentro de inteligencia de amenazas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 28.3 — Incident Response

#### 28.3.01 — Preparation
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.02 — Identification
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.03 — Analysis
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.04 — Containment
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.05 — Eradication
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.06 — Recovery
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.07 — Lessons Learned
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.3.08 — Incident Reporting
Comprender el concepto, los datos o controles involucrados y su papel dentro de incident response; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 28.4 — Forense digital (DFIR)

#### 28.4.01 — Digital Forensics
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.02 — Incident Response
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.03 — Evidence Preservation
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.04 — Chain of Custody
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.05 — Disk Forensics
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.06 — Memory Forensics
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.07 — File System Analysis
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.08 — Metadata
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.09 — Timeline Analysis
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.10 — Log Analysis
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.4.11 — Incident Reconstruction
Comprender el concepto, los datos o controles involucrados y su papel dentro de forense digital (dfir); relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 28.5 — Herramientas

#### 28.5.01 — Autopsy
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.5.02 — Sleuth Kit
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.5.03 — Volatility
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.5.04 — KAPE
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.5.05 — Sysmon
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.5.06 — Eric Zimmerman Tools (introducción)
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 28.6 — Estándares

#### 28.6.01 — NIST SP 800-61
Comprender el concepto, los datos o controles involucrados y su papel dentro de estándares; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.6.02 — NIST CSF 2.0
Comprender el concepto, los datos o controles involucrados y su papel dentro de estándares; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.6.03 — MITRE ATT&CK
Comprender el concepto, los datos o controles involucrados y su papel dentro de estándares; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 28.6.04 — CSRC
Comprender el concepto, los datos o controles involucrados y su papel dentro de estándares; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.
