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
