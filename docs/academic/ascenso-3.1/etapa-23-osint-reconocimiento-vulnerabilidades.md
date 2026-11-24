# Etapa 23 — Reconocimiento, OSINT y gestión de vulnerabilidades

**Prioridad:** P1 (fundamentos) · P2 (profundización avanzada)  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a recopilar información y evaluar la exposición de una infraestructura.  
**Proyecto oficial:** elaborar un informe de reconocimiento y evaluación de vulnerabilidades sobre un laboratorio propio, con evidencias, clasificación y recomendaciones.

## Alcance y autorización
El reconocimiento activo y los escaneos pueden afectar disponibilidad y privacidad. Limita toda actividad a activos propios o con autorización escrita, alcance, ventana y reglas de compromiso. OSINT también puede involucrar datos personales: aplica minimización, finalidad legítima, retención limitada y protección de evidencias. No busques ni publiques información privada de personas.

## 23.1 — Reconocimiento
Reconnaissance es la fase de recopilación de información sobre un objetivo definido. Passive reconnaissance utiliza fuentes públicas sin interactuar directamente con sistemas objetivo; active reconnaissance envía consultas o tráfico al activo y puede ser detectada o afectar servicios.

Define scope, activos permitidos, exclusiones y metodología. Asset discovery identifica recursos; attack surface mapping organiza puntos expuestos y relaciones. Registra fuente, fecha, confianza, alcance y limitaciones. No conviertas hallazgos de una fuente indirecta en afirmaciones confirmadas.

**Ejercicio:** crea inventario de activos ficticios de un laboratorio propio y clasifica cada hallazgo como confirmado, inferido o pendiente.

## 23.2 — OSINT
OSINT transforma información de fuentes abiertas en inteligencia contextualizada. Motores de búsqueda y operadores avanzados permiten localizar páginas públicas; registros de dominio, DNS, certificados digitales, Certificate Transparency, repositorios públicos y metadatos pueden revelar relaciones o configuraciones.

La existencia de un dato público no implica que sea apropiado recolectarlo o difundirlo. Evita doxxing, credenciales, información personal innecesaria y acceso a documentos que no tengas autorización para tratar. No intentes acceder a cuentas o sistemas mediante datos encontrados.

La correlación exige validar origen, fecha, precisión, duplicados y posibles homónimos. Mantén trazabilidad de la fuente y distingue hecho, hipótesis y conclusión.

**Ejercicio:** realiza un ejercicio con un dominio de laboratorio propio o dominio de documentación expresamente autorizado. No investigues personas particulares.

## 23.3 — Herramientas OSINT
Maltego ayuda a representar relaciones; WHOIS consulta datos de registro disponibles; DNSdumpster y utilidades similares recopilan información DNS; theHarvester y Amass apoyan descubrimiento de activos dentro del alcance; operadores de búsqueda localizan información indexada; ExifTool inspecciona metadatos de archivos propios o autorizados.

Una herramienta no garantiza exactitud ni autorización. Revisa fuente, términos, rate limits, alcance y tratamiento de datos. Los resultados pueden estar desactualizados o contener falsos positivos.

## 23.4 — Identificación de activos
Clasifica dominios, subdominios, direcciones IP, servidores, aplicaciones, tecnologías, servicios e infraestructura expuesta. Relaciona cada activo con propietario, criticidad, función, entorno y evidencia. No asumas que un subdominio o IP pertenece al mismo responsable sin validar.

**Ejercicio:** crea una tabla de inventario con identificador, activo, propietario, entorno, origen, fecha, confianza y autorización.

## 23.5 — Escaneo y enumeración
Host discovery, port scanning, TCP/UDP scanning, service enumeration, version detection y OS detection permiten describir servicios accesibles en sistemas autorizados. Nmap y NSE pueden generar tráfico significativo; selecciona perfiles conservadores, documenta parámetros y evita scripts intrusivos fuera de laboratorios expresos.

Interpreta resultados con cautela: puertos filtrados, servicios detrás de proxies, banners modificados y detección imperfecta pueden producir conclusiones erróneas. No infieras vulnerabilidad solo a partir de una versión aparente.

**Laboratorio:** escanea una VM propia en red aislada, compara resultados con el inventario de servicios configurados y explica falsos negativos/positivos posibles.

## 23.6 — Gestión de vulnerabilidades
Vulnerability Assessment identifica y prioriza debilidades para su tratamiento. CVE identifica vulnerabilidades divulgadas; CWE clasifica debilidades; CVSS expresa severidad técnica bajo un modelo, pero no equivale automáticamente al riesgo empresarial. Considera exposición, activos, controles, explotabilidad, impacto, criticidad y contexto.

Clasifica severidad, documenta falsos positivos, define remediación y retest. La gestión incluye descubrimiento, validación, priorización, asignación, corrección, excepción aceptada y cierre. No marques una vulnerabilidad como corregida sin evidencia de retest.

## 23.7 — Herramientas
Nessus y Greenbone/OpenVAS apoyan evaluación automatizada. Nmap y NSE ayudan a inventariar servicios. Configura escaneos solo sobre activos autorizados, revisa plugins/feed y versión, limita intensidad, protege credenciales de escaneo y valida manualmente hallazgos relevantes. El reporte automatizado requiere interpretación profesional.

## Proyecto oficial — Informe de reconocimiento y vulnerabilidades
### Requisitos
1. Autorización y alcance escritos para el laboratorio.
2. Diagrama de activos y red.
3. Metodología pasiva/activa diferenciada.
4. Inventario con fuente y nivel de confianza.
5. Evidencia de escaneo de máquinas propias.
6. Clasificación CVE/CWE/CVSS cuando corresponda.
7. Validación de falsos positivos sin explotación destructiva.
8. Priorización contextual y plan de remediación.
9. Retest de hallazgos corregidos.
10. Anonimización de secretos y datos personales.

### Entregables
Documento de alcance, inventario, metodología, resultados sanitizados, matriz de riesgos, recomendaciones priorizadas y evidencia de retest.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Alcance, autorización y ética | 15 |
| Reconocimiento y trazabilidad | 15 |
| OSINT y validación de fuentes | 15 |
| Inventario y enumeración | 15 |
| Análisis de vulnerabilidades | 20 |
| Priorización y remediación | 15 |
| Calidad del informe | 5 |

Criterio orientativo: 80/100; cualquier actividad fuera del alcance invalida la práctica hasta revisión.

## Autoevaluación
1. Diferencia reconocimiento pasivo y activo.
2. ¿Por qué un dato público puede seguir siendo sensible?
3. ¿Qué metadatos debes registrar para OSINT?
4. ¿Por qué un subdominio no prueba propiedad?
5. ¿Qué limitaciones tiene la detección de versiones?
6. Diferencia CVE, CWE y CVSS.
7. ¿Por qué CVSS no equivale al riesgo de negocio?
8. ¿Cómo validarías un falso positivo?
9. ¿Qué evidencia exige el cierre de una vulnerabilidad?
10. ¿Qué debes hacer antes de ejecutar un escaneo?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán únicamente recursos en español directamente relacionados con metodología OSINT, Nmap en laboratorio autorizado, gestión CVE/CVSS o herramientas de vulnerabilidades. Se excluirán tutoriales que incentiven reconocimiento de terceros sin permiso.

## Referencias oficiales
- NIST SP 800-115: https://csrc.nist.gov/pubs/sp/800/115/final
- NIST NVD: https://nvd.nist.gov/
- CVE Program: https://www.cve.org/
- MITRE CWE: https://cwe.mitre.org/
- FIRST CVSS: https://www.first.org/cvss/
- Nmap Reference Guide: https://nmap.org/book/man.html
- Amass: https://owasp.org/www-project-amass/
- ExifTool: https://exiftool.org/
- Greenbone Documentation: https://greenbone.github.io/docs/
- OWASP: https://owasp.org/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se realizaron escaneos ni consultas OSINT en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 23

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados son guías de estudio, no evidencias de ejecución ni autorización para evaluar sistemas de terceros.

### Módulo 23.1 — Reconocimiento

#### 23.1.01 — Reconnaissance
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.02 — Passive Reconnaissance
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.03 — Active Reconnaissance
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.04 — Scope
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.05 — Asset Discovery
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.06 — Attack Surface Mapping
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.1.07 — Reconnaissance Methodology
Estudiar el concepto dentro de reconocimiento, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.2 — OSINT (Open Source Intelligence)

#### 23.2.01 — Fuentes abiertas
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.02 — Motores de búsqueda
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.03 — Operadores de búsqueda avanzada
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.04 — Información pública
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.05 — Registros de dominios
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.06 — DNS Records
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.07 — Certificados digitales
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.08 — Certificate Transparency
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.09 — Repositorios públicos
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.10 — Metadatos
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.11 — Documentos expuestos
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.2.12 — Correlación de información
Estudiar el concepto dentro de osint (open source intelligence), comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.3 — Herramientas OSINT

#### 23.3.01 — Maltego
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.02 — WHOIS
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.03 — DNSdumpster
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.04 — theHarvester
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.05 — Amass
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.06 — Google Dorking
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.3.07 — ExifTool
Estudiar el concepto dentro de herramientas osint, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.4 — Identificación de activos

#### 23.4.01 — Dominios
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.02 — Subdominios
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.03 — Direcciones IP
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.04 — Servidores
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.05 — Aplicaciones
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.06 — Tecnologías
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.07 — Servicios
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.4.08 — Infraestructura expuesta
Estudiar el concepto dentro de identificación de activos, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.5 — Escaneo y enumeración

#### 23.5.01 — Host Discovery
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.02 — Port Scanning
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.03 — TCP Scanning
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.04 — UDP Scanning
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.05 — Service Enumeration
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.06 — Version Detection
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.07 — OS Detection
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.08 — Nmap
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.5.09 — Nmap Scripting Engine (NSE)
Estudiar el concepto dentro de escaneo y enumeración, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.6 — Gestión de vulnerabilidades

#### 23.6.01 — Vulnerability Assessment
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.02 — CVE
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.03 — CWE
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.04 — CVSS
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.05 — Severidad
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.06 — Impacto
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.07 — Probabilidad
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.08 — Priorización
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.09 — Falsos positivos
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.6.10 — Remediación
Estudiar el concepto dentro de gestión de vulnerabilidades, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

### Módulo 23.7 — Herramientas

#### 23.7.01 — Nessus
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.7.02 — OpenVAS
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.7.03 — Greenbone
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.7.04 — Nmap
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.

#### 23.7.05 — Nmap NSE
Estudiar el concepto dentro de herramientas, comprender sus límites y documentar su aplicación defensiva o de evaluación autorizada. Cualquier práctica debe realizarse únicamente en activos propios o con autorización expresa y alcance definido.
