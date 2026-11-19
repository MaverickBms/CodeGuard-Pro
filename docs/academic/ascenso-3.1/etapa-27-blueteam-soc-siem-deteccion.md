# Etapa 27 — Blue Team, SOC, SIEM e ingeniería de detección

**Prioridad:** P2 · Especialización defensiva  
**Estado:** borrador académico  
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

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se desplegó SIEM ni se generaron alertas en esta sesión. **Estado:** borrador.
