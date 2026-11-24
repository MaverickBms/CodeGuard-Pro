# Etapa 27 — Blue Team, SOC, SIEM e ingeniería de detección

**Prioridad:** P2 · Especialización defensiva  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a detectar, analizar y responder a comportamientos sospechosos.  
**Proyecto oficial:** construir un pequeño SOC de laboratorio que recopile registros de Linux y Windows, centralice eventos y genere alertas ante comportamientos simulados.

## Resultados de aprendizaje
Diseñar controles defensivos; comprender operaciones SOC y triage; recolectar y normalizar logs; distinguir IOC, IOA y TTP; explicar IDS/IPS; utilizar sensores y SIEM en laboratorio; y desarrollar reglas de detección versionadas y probadas.

## 27.1 — Blue Team
Blue Team reúne prácticas de defensa: prevención, detección, respuesta y recuperación. Defense in Depth combina controles; Zero Trust exige evaluación explícita y continua de identidad/contexto. Security Monitoring observa sistemas y señales relevantes. Clasifica controles preventivos, detectivos y correctivos según función y limitaciones.

**Ejercicio:** construye una matriz de activos, amenazas, controles preventivos, señales de detección y acciones correctivas.

## 27.2 — SOC
Un Security Operations Center coordina monitorización y respuesta. Un SOC Analyst realiza alert triage, clasifica eventos, recopila contexto, determina severidad y escala incidentes según procedimientos. No toda alerta es incidente ni toda anomalía es ataque. Define playbooks, criterios de escalamiento, tiempos, responsables y comunicación.

**Ejercicio:** clasifica alertas sintéticas por severidad, evidencia, falso positivo y acción siguiente.

## 27.3 — Logs
Application logs, system logs, authentication logs, network logs y security events describen actividad desde distintas capas. Correlaciona timestamps y fuentes para construir timelines. Sincroniza relojes y conserva zona horaria. Normaliza campos como usuario, host, proceso, origen, destino, acción y resultado.

Minimiza datos personales; limita acceso, retención y exportación. Evita registrar contraseñas, tokens o payloads sensibles. Protege integridad de registros y documenta lagunas de telemetría.

## 27.4 — Indicadores
IOC (Indicator of Compromise) describe artefactos/señales asociados con compromiso; IOA (Indicator of Attack) describe comportamiento relacionado con actividad adversaria; TTP son tácticas, técnicas y procedimientos. Anomalía es desviación de una línea base y no implica necesariamente ataque. Behavioral analysis requiere contexto, periodo, población y límites.

**Ejercicio:** utiliza registros ficticios para construir una línea temporal y distinguir IOC confirmado, IOA sospechoso e hipótesis no validada.

## 27.5 — IDS/IPS
IDS detecta actividad sospechosa y genera alertas; IPS puede bloquear o modificar tráfico según configuración. La detección basada en firmas identifica patrones conocidos; la basada en anomalías busca desviaciones. Ambas tienen falsos positivos y negativos. Network monitoring y traffic analysis deben respetar privacidad, políticas y alcance.

## 27.6 — Herramientas
Wireshark y tcpdump analizan tráfico; Suricata ofrece detección de red; Zeek genera telemetría de protocolos; Sysmon aporta eventos detallados de Windows. Configura fuentes, retención y filtros. No captures tráfico ajeno ni recolectes contenido privado sin autorización.

## 27.7 — SIEM
SIEM centraliza eventos, normaliza, correlaciona, presenta dashboards y genera alertas para investigación. Splunk, Elastic Stack y Wazuh son opciones con arquitecturas, licencias y capacidades distintas. Evalúa ingestión, retención, consultas, control de acceso, escalabilidad y costos. Una plataforma no produce detecciones útiles sin fuentes, reglas y tuning.

**Ejercicio:** incorpora logs de laboratorio, normaliza campos y crea un dashboard con volumen de autenticaciones, fallos y cambios administrativos.

## 27.8 — Detection Engineering
Sigma expresa reglas de detección en un formato genérico que puede convertirse a distintos backends. Detection-as-Code versiona reglas, pruebas, documentación y cambios. Alert tuning reduce ruido sin eliminar cobertura. Mide falsos positivos, falsos negativos conocidos, cobertura de fuentes y fatiga de alertas. Rule validation usa datos sintéticos y escenarios de laboratorio antes de desplegar.

**Ejercicio:** crea una regla Sigma sencilla sobre evento sintético, prueba caso positivo/negativo y documenta fuente, campos, severidad, limitaciones y respuesta.

## Proyecto oficial — SOC de laboratorio
### Requisitos
1. Topología y autorización del laboratorio.
2. Fuentes Linux y Windows con datos ficticios.
3. Recolección centralizada y normalización.
4. Almacenamiento con acceso y retención definidos.
5. Dashboard con eventos de autenticación y sistema.
6. Alertas para comportamientos simulados.
7. Una regla documentada y versionada.
8. Triage con clasificación y escalamiento.
9. Registro de falsos positivos y ajustes.
10. Guía de respuesta y restauración.

### Entregables
Diagrama, fuentes de logs, reglas, dashboards, casos sintéticos, resultados de validación, playbook de triage y documentación de privacidad.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Arquitectura defensiva | 10 |
| SOC y triage | 15 |
| Recolección y normalización | 15 |
| Indicadores y análisis | 10 |
| IDS/IPS y herramientas | 10 |
| SIEM y dashboards | 15 |
| Detection engineering | 15 |
| Privacidad y documentación | 10 |

Criterio orientativo: 80/100 y alertas reproducibles con casos positivos y negativos.

## Autoevaluación
1. Diferencia control preventivo y detectivo.
2. ¿Qué información necesita un analista para triage?
3. ¿Por qué sincronizar relojes importa?
4. Diferencia IOC, IOA y TTP.
5. ¿Qué diferencia hay entre IDS e IPS?
6. ¿Qué hace la normalización SIEM?
7. ¿Por qué una alerta no equivale a incidente?
8. ¿Qué es Detection-as-Code?
9. ¿Cómo reduces alert fatigue sin ocultar ataques?
10. ¿Qué datos no deben aparecer en logs?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo tras confirmar audio hablado en español y relación directa con SOC, SIEM, Suricata, Zeek, Sysmon o Sigma. No se utilizarán demostraciones con tráfico o datos ajenos.

## Referencias oficiales
- NIST SP 800-92 — Log Management: https://csrc.nist.gov/pubs/sp/800/92/final
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- Wireshark: https://www.wireshark.org/docs/
- Suricata: https://docs.suricata.io/
- Zeek: https://docs.zeek.org/
- Microsoft Sysmon: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
- Splunk Docs: https://docs.splunk.com/
- Elastic Security: https://www.elastic.co/guide/en/security/current/index.html
- Wazuh: https://documentation.wazuh.com/
- Sigma: https://sigmahq.io/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se desplegó SIEM ni se generaron alertas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 27

Este desglose conserva los títulos y el orden del roadmap maestro. Las guías de estudio se orientan a administración defensiva, monitoreo y análisis autorizado; no constituyen evidencia de operación en un entorno empresarial.

### Módulo 27.1 — Blue Team

#### 27.1.01 — Defensive Security
Defensive Security protege activos mediante prevención, detección, respuesta y recuperación. Parte de inventario, clasificación y riesgo y coordina controles técnicos con procesos y responsables.


**Práctica y evidencia:** Diseña controles defensivos para un activo y clasifícalos por prevención, detección y respuesta. **Evidencia:** relaciona control con riesgo.

#### 27.1.02 — Defense in Depth
Defense in Depth combina controles en endpoint, identidad, red, aplicación y datos. Diseña capas independientes y comprueba que una falla no deje el activo sin protección ni visibilidad.


**Práctica y evidencia:** Crea una defensa por capas para una aplicación expuesta. **Evidencia:** explica cómo se complementan controles y qué ocurre si uno falla.

#### 27.1.03 — Preventive Controls
Preventive Controls reducen probabilidad de incidentes mediante hardening, parches, MFA y segmentación. Define cobertura y excepciones y valida que los controles estén activos.


**Práctica y evidencia:** Selecciona controles preventivos para identidad, endpoint y red. **Evidencia:** define cobertura y limitaciones.

#### 27.1.04 — Detective Controls
Detective Controls identifican actividad anómala o incumplimientos mediante logs, alertas y monitoreo. Mide cobertura, tiempo de detección y falsos positivos.


**Práctica y evidencia:** Diseña detecciones para inicios de sesión anómalos y cambios de privilegio. **Evidencia:** define señal, umbral y fuente de datos.

#### 27.1.05 — Corrective Controls
Corrective Controls contienen o corrigen condiciones detectadas y restauran operación segura. Incluye aislamiento, revocación, parcheo y recuperación, con autorización y preservación de evidencia.


**Práctica y evidencia:** Planifica corrección de un hallazgo y restauración de servicio. **Evidencia:** define responsable, tiempo y verificación.

#### 27.1.06 — Zero Trust
Zero Trust evita confianza implícita basada únicamente en ubicación de red y exige verificación contextual. Integra identidad, dispositivo, recurso y política; no es un producto aislado.


**Práctica y evidencia:** Aplica verificación explícita y mínimo privilegio en un flujo de acceso. **Evidencia:** identifica sujeto, dispositivo, recurso y contexto.

#### 27.1.07 — Security Monitoring
Security Monitoring observa eventos y estado de controles para detectar desviaciones. Define fuentes, casos de uso, retención, responsables y alertas accionables.


**Práctica y evidencia:** Define un plan de monitoreo con fuentes, retención, alertas y responsables. **Evidencia:** vincula cada alerta con un procedimiento.

### Módulo 27.2 — SOC

#### 27.2.01 — Security Operations Center
Security Operations Center coordina monitoreo, triage, investigación y respuesta de seguridad. Define turnos, escalamiento, herramientas, métricas y coordinación con TI y negocio.


**Práctica y evidencia:** Dibuja funciones de un SOC: monitoreo, triage, investigación, respuesta y mejora. **Evidencia:** asigna roles y escalamiento.

#### 27.2.02 — SOC Analyst
SOC Analyst interpreta alertas, valida contexto, recopila evidencia y escala incidentes. Sigue procedimientos, registra decisiones y evita acciones disruptivas sin autorización.


**Práctica y evidencia:** Resuelve un caso de triage como analista SOC con evidencia sintética. **Evidencia:** registra hipótesis, prioridad y siguiente acción.

#### 27.2.03 — Alert Triage
Alert Triage prioriza alertas según severidad, confianza, alcance e impacto potencial. Correlaciona activo, usuario, tiempo y contexto y documenta por qué se cierra o escala.


**Práctica y evidencia:** Clasifica una alerta por severidad, confianza e impacto. **Evidencia:** justifica prioridad y evita equiparar severidad técnica con impacto real.

#### 27.2.04 — Event Classification
Event Classification categoriza eventos por tipo, severidad y relación con incidentes. Usa taxonomía consistente y evita asignar severidad únicamente por el nombre de la alerta.


**Práctica y evidencia:** Define taxonomía de eventos para autenticación, endpoint y red. **Evidencia:** documenta campos y criterios de clasificación.

#### 27.2.05 — Incident Escalation
Incident Escalation transfiere casos a equipos con autoridad o especialidad adecuada. Define umbrales, tiempos, contactos y evidencia mínima para evitar retrasos o pérdida de contexto.


**Práctica y evidencia:** Escala un incidente con contexto, alcance, evidencia y urgencia. **Evidencia:** redacta handoff completo y reproducible.

#### 27.2.06 — Security Monitoring
Security Monitoring en SOC integra telemetría de endpoints, identidad, red, aplicaciones y cloud. Evalúa cobertura de activos críticos y detecta interrupciones en la ingestión de datos.


**Práctica y evidencia:** Construye cobertura de monitoreo para un servicio crítico. **Evidencia:** identifica fuentes faltantes y puntos ciegos.

#### 27.2.07 — Threat Detection
Threat Detection identifica patrones asociados a actividad maliciosa o comportamiento anómalo. Combina inteligencia, contexto y reglas y valida hipótesis antes de declarar un compromiso.


**Práctica y evidencia:** Diseña una detección para un comportamiento anómalo de laboratorio. **Evidencia:** documenta señal, contexto y validación.

### Módulo 27.3 — Logs

#### 27.3.01 — Application Logs
Application Logs registran eventos funcionales y técnicos de aplicaciones. Estandariza campos, niveles y correlación, evita secretos y datos personales innecesarios y conserva contexto de error.


**Práctica y evidencia:** Analiza logs de aplicación sintéticos para encontrar errores de autenticación o autorización. **Evidencia:** extrae hora, usuario, acción y resultado.

#### 27.3.02 — System Logs
System Logs registran eventos de sistema operativo, servicios, recursos y cambios. Sincroniza tiempo, centraliza fuentes relevantes y protege integridad y retención.


**Práctica y evidencia:** Correlaciona logs de sistema con reinicio de servicio en VM. **Evidencia:** reconstruye secuencia temporal.

#### 27.3.03 — Authentication Logs
Authentication Logs registran intentos, resultados y cambios de identidad. Detecta patrones de fallo, MFA y accesos anómalos, y redacta credenciales o tokens.


**Práctica y evidencia:** Revisa eventos de autenticación exitosa y fallida y detecta patrón anómalo. **Evidencia:** diferencia fallo legítimo de posible abuso.

#### 27.3.04 — Network Logs
Network Logs reflejan conexiones, flujos, DNS, firewall y dispositivos de red. Relaciona origen/destino y tiempo con activos y evita interpretar metadatos aislados como prueba concluyente.


**Práctica y evidencia:** Inspecciona logs de firewall o proxy de laboratorio y relaciona origen/destino/puerto. **Evidencia:** documenta flujo permitido y bloqueado.

#### 27.3.05 — Security Events
Security Events son sucesos relevantes para controles, políticas o amenazas. Define taxonomía y severidad y diferencia evento individual, alerta correlacionada e incidente confirmado.


**Práctica y evidencia:** Define campos mínimos de un evento de seguridad y política de redacción. **Evidencia:** no incluye contraseñas, tokens ni datos personales innecesarios.

#### 27.3.06 — Event Correlation
Event Correlation relaciona múltiples registros mediante tiempo, identidad, activo y comportamiento. Controla desfases de reloj y duplicados y documenta reglas de correlación.


**Práctica y evidencia:** Correlaciona dos fuentes mediante identidad, IP, host y ventana temporal. **Evidencia:** declara límites de calidad y sincronización de relojes.

#### 27.3.07 — Timelines
Timelines ordenan eventos para reconstruir secuencias y relaciones temporales. Conserva zona horaria, origen y precisión de timestamp y distingue tiempos observados de inferidos.


**Práctica y evidencia:** Construye una línea temporal de un incidente con eventos sintéticos. **Evidencia:** separa observaciones, inferencias y vacíos.

### Módulo 27.4 — Indicadores

#### 27.4.01 — IOC (Indicators of Compromise)
IOC son indicadores asociados a posible compromiso, como hashes, dominios o direcciones IP. Añade fuente, vigencia y confianza; evita bloquear indicadores sin evaluar impacto y contexto.


**Práctica y evidencia:** Clasifica IOC como hash, dominio, IP o ruta y define caducidad/confianza. **Evidencia:** registra fuente y contexto antes de bloquear.

#### 27.4.02 — IOA (Indicators of Attack)
IOA describe comportamientos o secuencias que sugieren actividad de ataque, en lugar de depender solo de artefactos conocidos. Diseña detecciones centradas en comportamiento y valida con actividad legítima.


**Práctica y evidencia:** Define IOA como comportamiento observable y crea una regla conceptual. **Evidencia:** explica por qué el comportamiento puede ser más durable que un IOC.

#### 27.4.03 — TTP (Tactics, Techniques and Procedures)
TTP resume tácticas, técnicas y procedimientos observados o modelados de adversarios. Mapea a MITRE ATT&CK con versión y plataforma y no atribuyas actor por una técnica aislada.


**Práctica y evidencia:** Mapea una secuencia defensiva a tácticas y técnicas MITRE ATT&CK. **Evidencia:** cita técnica y telemetría asociada sin atribuir actor sin pruebas.

#### 27.4.04 — Anomalies
Anomalies son desviaciones respecto de una línea base de comportamiento. Considera estacionalidad, cambios legítimos y calidad de datos antes de clasificarlas como amenaza.


**Práctica y evidencia:** Establece baseline de comportamiento para usuario o host de laboratorio. **Evidencia:** detecta desviación y descarta variaciones legítimas.

#### 27.4.05 — Behavioral Analysis
Behavioral Analysis estudia patrones de usuarios, procesos y redes para identificar actividad inusual. Minimiza datos personales, define finalidad y aplica controles de acceso y retención.


**Práctica y evidencia:** Analiza patrones de proceso, red y autenticación en datos sintéticos. **Evidencia:** explica contexto y evita conclusiones por una única señal.

### Módulo 27.5 — IDS/IPS

#### 27.5.01 — Intrusion Detection System
Intrusion Detection System detecta actividad potencialmente maliciosa y genera alertas sin necesariamente bloquearla. Define fuentes, firmas, umbrales y proceso de triage.


**Práctica y evidencia:** Compara IDS y firewall y despliega un sensor pasivo en red de laboratorio. **Evidencia:** documenta interfaz, reglas y alertas.

#### 27.5.02 — Intrusion Prevention System
Intrusion Prevention System puede bloquear tráfico o acciones que coincidan con políticas de detección. Prueba reglas para evitar falsos bloqueos y define modo de operación y recuperación.


**Práctica y evidencia:** Explica riesgos de IPS inline y prueba bloqueo solo en entorno aislado. **Evidencia:** documenta falso positivo y procedimiento de bypass seguro.

#### 27.5.03 — Signature-based Detection
Signature-based Detection compara eventos con patrones conocidos de amenazas. Es eficaz para amenazas identificadas, pero requiere actualización y no detecta necesariamente variantes nuevas.


**Práctica y evidencia:** Escribe una regla de detección por firma para un patrón sintético. **Evidencia:** demuestra coincidencia y límite ante variaciones.

#### 27.5.04 — Anomaly-based Detection
Anomaly-based Detection identifica desviaciones frente a modelos o líneas base. Ajusta sensibilidad y contexto para reducir falsos positivos y vigila cambios de comportamiento legítimos.


**Práctica y evidencia:** Diseña una detección por anomalía con baseline y umbral. **Evidencia:** evalúa falsos positivos y deriva del comportamiento.

#### 27.5.05 — Network Monitoring
Network Monitoring observa disponibilidad, flujos, protocolos y eventos de infraestructura. Define puntos de captura, privacidad y retención; una vista parcial de red no representa todo el tráfico.


**Práctica y evidencia:** Define puntos de captura y métricas de red para un segmento propio. **Evidencia:** identifica visibilidad, pérdida de paquetes y privacidad.

#### 27.5.06 — Traffic Analysis
Traffic Analysis interpreta metadatos y contenido permitido para comprender comunicaciones y anomalías. Minimiza captura de payloads sensibles, documenta filtros y protege archivos PCAP.


**Práctica y evidencia:** Analiza flujo de red con origen, destino, protocolo, bytes y duración. **Evidencia:** identifica comportamiento atípico con contexto.

### Módulo 27.6 — Herramientas

#### 27.6.01 — Wireshark
Wireshark permite analizar paquetes capturados para investigar protocolos y anomalías. Captura solo tráfico autorizado, filtra datos sensibles y protege PCAP porque pueden contener credenciales o información privada.


**Práctica y evidencia:** Captura tráfico de una VM propia con Wireshark y aplica filtro de visualización. **Evidencia:** documenta protocolo y campos relevantes.

#### 27.6.02 — tcpdump
tcpdump captura tráfico desde interfaces y permite filtros para reducir volumen. Verifica interfaz y alcance antes de capturar y protege archivos resultantes.


**Práctica y evidencia:** Ejecuta tcpdump con filtro BPF limitado sobre interfaz de laboratorio. **Evidencia:** conserva comando, número de paquetes y archivo anonimizado.

#### 27.6.03 — Suricata
Suricata es un motor de IDS/IPS y monitoreo de seguridad de red basado en reglas y protocolos. Ajusta reglas a la red, valida alertas y controla impacto si opera en modo prevención.


**Práctica y evidencia:** Configura Suricata en modo IDS pasivo sobre tráfico sintético/lab. **Evidencia:** valida alerta y documenta regla.

#### 27.6.04 — Zeek
Zeek analiza tráfico y genera registros de actividad de protocolos y conexiones. Utiliza logs para contexto y hunting, verifica cobertura de interfaces y protege datos capturados.


**Práctica y evidencia:** Usa Zeek para generar logs de conexiones DNS/HTTP de laboratorio. **Evidencia:** relaciona conn.log con protocolo y origen.

#### 27.6.05 — Sysmon
Sysmon registra eventos detallados de actividad en Windows mediante configuración definida. Selecciona eventos útiles, controla volumen, protege logs y valida que la versión y configuración sean consistentes.


**Práctica y evidencia:** Configura Sysmon en VM Windows con política controlada. **Evidencia:** identifica eventos de proceso y red y registra versión de configuración.

### Módulo 27.7 — SIEM

#### 27.7.01 — Security Information and Event Management
Security Information and Event Management centraliza y correlaciona eventos de múltiples fuentes para apoyar detección e investigación. Define casos de uso, cobertura, retención y responsabilidades.


**Práctica y evidencia:** Diseña arquitectura SIEM con fuentes, colectores, almacenamiento, búsquedas y alertas. **Evidencia:** documenta flujo y controles de acceso.

#### 27.7.02 — Log Collection
Log Collection ingiere eventos desde endpoints, aplicaciones, redes y servicios cloud. Valida continuidad, timestamps, formato y volumen y detecta fuentes que dejaron de reportar.


**Práctica y evidencia:** Recolecta logs de dos fuentes de laboratorio con transporte seguro. **Evidencia:** demuestra integridad y timestamp.

#### 27.7.03 — Log Normalization
Log Normalization convierte fuentes heterogéneas a campos y formatos comunes. Conserva campos originales, mapea correctamente semántica y registra pérdida o transformación de datos.


**Práctica y evidencia:** Normaliza campos de origen, usuario, host, evento y severidad. **Evidencia:** muestra evento original y normalizado.

#### 27.7.04 — Correlation Rules
Correlation Rules relacionan eventos para generar alertas con contexto. Documenta lógica, fuentes, ventanas temporales y excepciones y prueba con datos históricos y casos benignos.


**Práctica y evidencia:** Crea una regla de correlación con umbral y ventana temporal. **Evidencia:** prueba caso positivo y negativo.

#### 27.7.05 — Dashboards
Dashboards muestran estado, tendencias y métricas para analistas y responsables. Diseña vistas por función y evita métricas decorativas que no guían decisiones.


**Práctica y evidencia:** Diseña dashboard que muestre tendencias y alertas relevantes sin exponer datos sensibles. **Evidencia:** vincula panel con pregunta operativa.

#### 27.7.06 — Alerts
Alerts notifican condiciones que requieren revisión o respuesta. Define severidad, responsable, contexto, deduplicación y umbral para evitar fatiga y omisiones.


**Práctica y evidencia:** Define alerta con severidad, deduplicación, contexto y ruta de escalamiento. **Evidencia:** demuestra que alerta repetida no genera ruido excesivo.

#### 27.7.07 — Detection
Detection identifica señales de amenazas mediante reglas, analítica y contexto. Mide cobertura y eficacia, y actualiza detecciones ante cambios de infraestructura y adversarios.


**Práctica y evidencia:** Construye detección a partir de un caso de uso y fuentes disponibles. **Evidencia:** documenta cobertura y limitaciones.

#### 27.7.08 — Incident Investigation
Incident Investigation valida una alerta, delimita alcance y reúne evidencia para decidir contención. Mantén cadena de custodia cuando aplique y separa hechos, hipótesis y conclusiones.


**Práctica y evidencia:** Investiga incidente sintético correlacionando identidad, endpoint y red. **Evidencia:** presenta hipótesis, timeline y evidencia.

#### 27.7.09 — Herramientas
La entrada «Herramientas» del roadmap agrupa plataformas de SIEM que se estudian en las siguientes lecciones. Se conserva como rótulo de agrupación curricular y no como producto o procedimiento independiente.


**Práctica y evidencia:** Compara herramientas SIEM por ingestión, consulta, correlación y operación. **Evidencia:** matriz de criterios para un escenario pequeño.

#### 27.7.10 — Splunk
Splunk indexa y consulta datos de máquina para monitoreo e investigación. Define fuentes, campos, permisos y retención; protege búsquedas y dashboards que puedan exponer datos sensibles.


**Práctica y evidencia:** Crea una búsqueda Splunk sobre datos sintéticos y transforma resultados en alerta. **Evidencia:** guarda consulta y resultado reproducible.

#### 27.7.11 — Elastic Stack (ELK)
Elastic Stack integra componentes para ingestión, almacenamiento, búsqueda y visualización de datos. Dimensiona ingestión y retención, protege acceso y valida mappings y reglas.


**Práctica y evidencia:** Ingiere eventos en Elastic Stack de laboratorio y consulta campos normalizados. **Evidencia:** documenta pipeline y retención.

#### 27.7.12 — Wazuh
Wazuh ofrece capacidades de seguridad de endpoint, análisis de logs y monitoreo de integridad. Configura agentes y reglas según activos, revisa alertas y protege la consola y sus credenciales.


**Práctica y evidencia:** Configura Wazuh agent/manager en entorno aislado y valida una alerta de prueba. **Evidencia:** registra versión, regla y respuesta.

### Módulo 27.8 — Detection Engineering

#### 27.8.01 — Sigma
Sigma es un formato genérico para describir reglas de detección que pueden convertirse a distintos backends. Declara logsource, condición y referencias y valida traducción en el SIEM objetivo.


**Práctica y evidencia:** Escribe una regla Sigma para un evento sintético y valida campos requeridos. **Evidencia:** conserva regla y prueba positiva/negativa.

#### 27.8.02 — Detection Rules
Detection Rules formalizan condiciones que identifican comportamientos o eventos de interés. Incluye hipótesis, fuentes, umbral, excepciones, severidad y pasos de validación.


**Práctica y evidencia:** Define una regla de detección con condición, fuente, severidad y excepción. **Evidencia:** documenta caso de uso y cobertura.

#### 27.8.03 — Detection-as-Code
Detection-as-Code versiona reglas, pruebas y configuración de detección como artefactos mantenibles. Revisa cambios por pares, automatiza validación y conserva historial de despliegue.


**Práctica y evidencia:** Versiona reglas como código y somete cambios a revisión y pruebas. **Evidencia:** demuestra historial y rollback.

#### 27.8.04 — Alert Tuning
Alert Tuning ajusta umbrales, filtros y contexto para mejorar precisión sin perder cobertura. Registra motivo y efecto de cada ajuste y mide falsos positivos y falsos negativos.


**Práctica y evidencia:** Ajusta una alerta con umbral, ventana y allowlist justificada. **Evidencia:** compara precisión antes/después sin ocultar actividad real.

#### 27.8.05 — False Positives
False Positives son alertas que no corresponden a actividad maliciosa o incumplimiento real. Analiza causa, conserva contexto y ajusta detección sin suprimir señales relevantes.


**Práctica y evidencia:** Investiga un falso positivo y registra causa raíz. **Evidencia:** ajusta detección sin eliminar la señal relevante.

#### 27.8.06 — Alert Fatigue
Alert Fatigue ocurre cuando volumen o baja calidad de alertas reduce atención del analista. Prioriza por riesgo, deduplica, automatiza enriquecimiento seguro y mide carga de trabajo.


**Práctica y evidencia:** Mide volumen de alertas y prioriza reducción de ruido. **Evidencia:** define criterios para deduplicación y escalamiento.

#### 27.8.07 — Log Sources
Log Sources son sistemas y componentes que generan datos para detección. Prioriza fuentes según activos y amenazas y monitorea retrasos, pérdida y cambios de formato.


**Práctica y evidencia:** Inventaría fuentes de logs por activo, cobertura y retención. **Evidencia:** identifica fuentes críticas ausentes.

#### 27.8.08 — Rule Validation
Rule Validation prueba una detección con eventos positivos, negativos y casos límite antes de desplegarla. Documenta cobertura, rendimiento y falsos resultados y repite pruebas tras cambios de fuente.


**Práctica y evidencia:** Prueba una regla con datos positivos, negativos y límites. **Evidencia:** conserva dataset sintético y resultado esperado.

#### 27.8.09 — Correlation
Correlation combina señales de varias fuentes para identificar secuencias o patrones con mayor contexto. Define ventanas y claves de unión, controla duplicados y valida que la regla no una eventos de usuarios distintos.



**Práctica y evidencia:** Correlaciona señales de varias fuentes para aumentar confianza. **Evidencia:** documenta ventana, claves y riesgo de correlación incorrecta.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 58 orientaciones genéricas por explicaciones específicas de Blue Team, SOC, logs, indicadores, IDS/IPS, herramientas, SIEM e ingeniería de detección.

**Revisión interna:** 58/58 entradas desarrolladas y cotejadas con el roadmap. Se aclaró que «Herramientas» en 27.7 es un rótulo curricular, no una plataforma. Se reforzaron protección de PCAP/logs, privacidad, sincronización temporal, tuning y validación de reglas. Pendiente: desplegar SIEM/IDS en laboratorio aislado, validar ingestión y reglas con datos sintéticos, medir cobertura/falsos positivos y obtener segunda revisión. No se conectaron entornos empresariales ni se declara aprobación externa.
