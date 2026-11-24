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
Reconnaissance recopila información sobre un objetivo para comprender activos, relaciones y exposición. En una evaluación profesional se realiza con autorización y alcance definido; separa hechos observados de inferencias.

#### 23.1.02 — Passive Reconnaissance
Passive Reconnaissance utiliza fuentes públicas o datos ya disponibles sin interactuar directamente con los sistemas objetivo. Registra fuente, fecha, confianza y límites, y evita recopilar o conservar datos personales innecesarios.

#### 23.1.03 — Active Reconnaissance
Active Reconnaissance interactúa directamente con activos para confirmar servicios o comportamiento y puede generar alertas o impacto. Requiere autorización explícita, ventanas, límites de tasa y condiciones de detención.

#### 23.1.04 — Scope
Scope define dominios, direcciones, aplicaciones, cuentas, técnicas permitidas y exclusiones. Trata cualquier activo fuera de alcance como no autorizado y detén la actividad si la titularidad es incierta.

#### 23.1.05 — Asset Discovery
Asset Discovery identifica activos relevantes y sus propietarios mediante inventarios, fuentes documentales y observación autorizada. Deduplica resultados y marca nivel de confianza para evitar convertir nombres o direcciones históricas en activos confirmados.

#### 23.1.06 — Attack Surface Mapping
Attack Surface Mapping relaciona activos, interfaces, servicios, identidades y flujos de acceso. Prioriza exposición y criticidad, identifica dependencias y registra qué elementos no pudieron verificarse.

#### 23.1.07 — Reconnaissance Methodology
Reconnaissance Methodology estructura preparación, recopilación, validación, correlación y reporte. Define hipótesis, alcance, fuentes y criterios de cierre para que los resultados sean repetibles y auditables.

### Módulo 23.2 — OSINT (Open Source Intelligence)

#### 23.2.01 — Fuentes abiertas
Las fuentes abiertas incluyen registros públicos, documentación, sitios, repositorios y publicaciones accesibles legalmente. La disponibilidad pública no implica permiso para acceder a sistemas, reutilizar datos sin límite o vulnerar condiciones aplicables.

#### 23.2.02 — Motores de búsqueda
Los motores de búsqueda indexan páginas y permiten localizar información mediante consultas. Documenta consultas y fecha, evita automatización abusiva y no interpretes un resultado indexado como prueba de que el recurso sigue disponible.

#### 23.2.03 — Operadores de búsqueda avanzada
Los operadores de búsqueda avanzada refinan resultados por dominio, tipo de archivo, frase o fecha. Úsalos para investigación documental y evaluación autorizada, sin intentar acceder a contenido restringido ni eludir controles de acceso.

#### 23.2.04 — Información pública
La información pública puede revelar tecnologías, estructura organizacional, contactos o metadatos. Evalúa relevancia y sensibilidad, minimiza recopilación y comunica exposiciones con evidencia y contexto.

#### 23.2.05 — Registros de dominios
Los registros de dominios contienen datos de registro, registrador, fechas y servidores de nombres según políticas de privacidad. Interpreta redacción y datos proxy correctamente; no atribuyas una organización a un registrante sin corroboración.

#### 23.2.06 — DNS Records
DNS Records describen servicios y nombres mediante tipos como A, AAAA, CNAME, MX, NS y TXT. Interpreta TTL y delegación y evita asumir que un registro confirma un servicio operativo.

#### 23.2.07 — Certificados digitales
Los certificados digitales vinculan nombres con claves públicas y cadenas de confianza. Revisa SAN, emisor y vigencia en fuentes autorizadas; un certificado puede revelar nombres históricos, pero no prueba que un host esté activo.

#### 23.2.08 — Certificate Transparency
Certificate Transparency publica registros de certificados para facilitar detección y auditoría. Úsalo para descubrir nombres asociados a dominios bajo alcance, valida vigencia y propiedad y trata nombres internos o históricos con cautela.

#### 23.2.09 — Repositorios públicos
Los repositorios públicos pueden exponer código, configuraciones, historial y, accidentalmente, secretos. Reporta hallazgos mediante el canal responsable, no pruebes credenciales encontradas y evita clonar o redistribuir datos sensibles innecesarios.

#### 23.2.10 — Metadatos
Los metadatos describen autoría, software, fechas, ubicación u otras propiedades de archivos. Extrae solo atributos pertinentes y considera privacidad; los metadatos pueden ser falsos, heredados o alterados.

#### 23.2.11 — Documentos expuestos
Los documentos expuestos pueden contener información que no estaba destinada a difusión pública. Registra ubicación y evidencia mínima, no descargues lotes de información personal y notifica al propietario por un canal responsable.

#### 23.2.12 — Correlación de información
Correlación de información relaciona observaciones independientes para construir hipótesis sobre activos y exposición. Registra fuente, fecha, confianza y contradicciones; evita presentar correlación como causalidad o identidad confirmada.

### Módulo 23.3 — Herramientas OSINT

#### 23.3.01 — Maltego
Maltego facilita visualizar relaciones entre entidades y fuentes de información mediante transformaciones. Revisa qué datos envía a servicios externos, valida cada relación y evita cargar información sensible sin autorización.

#### 23.3.02 — WHOIS
WHOIS consulta datos de registro de dominios o recursos según disponibilidad y políticas. Interpreta campos redactados, proxies y fechas; corrobora información con fuentes oficiales antes de atribuir titularidad.

#### 23.3.03 — DNSdumpster
DNSdumpster recopila relaciones DNS y hosts desde fuentes disponibles. Los resultados pueden ser incompletos o históricos; valida cada observación y respeta condiciones de uso y límites de consulta.

#### 23.3.04 — theHarvester
theHarvester reúne información pública de fuentes configuradas, como dominios, correos y hosts. Limita consultas al alcance aprobado, protege datos personales y valida falsos positivos antes de reportar.

#### 23.3.05 — Amass
Amass apoya descubrimiento y mapeo de superficie de dominios mediante fuentes y técnicas configurables. Selecciona modos pasivos o activos según autorización, limita intensidad y conserva evidencia reproducible.

#### 23.3.06 — Google Dorking
Google Dorking utiliza operadores de búsqueda para localizar información indexada de forma precisa. En contexto defensivo, revisa únicamente dominios propios/autorizados y reporta exposición sin intentar explotar recursos o acceder a documentos restringidos.

#### 23.3.07 — ExifTool
ExifTool lee y modifica metadatos de numerosos formatos. En auditoría, trabaja sobre copias, registra formato y campos examinados y evita publicar coordenadas, nombres o identificadores personales.

### Módulo 23.4 — Identificación de activos

#### 23.4.01 — Dominios
Dominios son nombres jerárquicos que identifican zonas dentro del DNS. Distingue dominio registrable, subdominio y zona delegada; confirma relación con el propietario antes de incluirlo en el inventario.

#### 23.4.02 — Subdominios
Subdominios permiten organizar servicios y aplicaciones bajo un dominio. Pueden ser activos obsoletos o de terceros; valida DNS, propiedad y estado antes de cualquier prueba.

#### 23.4.03 — Direcciones IP
Direcciones IP identifican interfaces en redes y pueden cambiar, compartirse o pertenecer a proveedores. Correlaciona con fecha, DNS y ASN y no las uses como identificador permanente de una organización.

#### 23.4.04 — Servidores
Servidores ofrecen servicios de cómputo, almacenamiento o comunicación. Identifica función, propietario, entorno y criticidad mediante fuentes autorizadas; evita inferir sistema operativo por un único banner.

#### 23.4.05 — Aplicaciones
Aplicaciones son activos de software con usuarios, datos, endpoints y dependencias. Registra versión, propietario, entorno y criticidad y distingue producción, pruebas y servicios retirados.

#### 23.4.06 — Tecnologías
Tecnologías identifican frameworks, bibliotecas, servidores y plataformas utilizadas por un activo. La detección puede ser inexacta o revelar solo una capa; valida con documentación o responsables antes de asignar vulnerabilidades.

#### 23.4.07 — Servicios
Servicios son capacidades disponibles en un host o plataforma, identificadas por protocolo y función. Registra exposición, necesidad de negocio y responsable y evita pruebas intrusivas sin autorización.

#### 23.4.08 — Infraestructura expuesta
Infraestructura expuesta incluye recursos accesibles desde redes públicas o de terceros. Evalúa necesidad, configuración, controles de acceso y dependencia; prioriza reducir exposición no requerida.

### Módulo 23.5 — Escaneo y enumeración

#### 23.5.01 — Host Discovery
Host Discovery identifica qué sistemas parecen responder en una red o conjunto de activos autorizado. Las respuestas pueden bloquearse o falsificarse; registra método y limitaciones sin interpretar ausencia de respuesta como host inexistente.

#### 23.5.02 — Port Scanning
Port Scanning identifica puertos que parecen abiertos, cerrados o filtrados en un objetivo. Ejecuta solo dentro del alcance aprobado, con límites de tasa y ventanas, y no equipares puerto abierto con vulnerabilidad.

#### 23.5.03 — TCP Scanning
TCP Scanning observa respuestas del protocolo TCP para inferir estado de puertos y conectividad. El resultado depende de firewall, NAT y configuración; limita intensidad y documenta método y punto de observación.

#### 23.5.04 — UDP Scanning
UDP Scanning tiene mayor ambigüedad porque muchos servicios UDP no responden a sondas inesperadas. Interpreta estados como open|filtered con cautela y evita escaneos amplios fuera de laboratorio.

#### 23.5.05 — Service Enumeration
Service Enumeration identifica protocolos y capacidades expuestas por un servicio. Utiliza métodos no destructivos autorizados, valida banners y versiones y evita solicitar operaciones que modifiquen datos.

#### 23.5.06 — Version Detection
Version Detection intenta estimar versiones de servicios a partir de respuestas observables. Los banners pueden ocultar o falsificar versiones; confirma con inventario del propietario antes de asociar CVEs.

#### 23.5.07 — OS Detection
OS Detection infiere características del sistema operativo a partir de respuestas de red. Es probabilística y sensible a intermediarios; no la uses como única evidencia para decidir una remediación.

#### 23.5.08 — Nmap
Nmap es una herramienta de descubrimiento y auditoría de redes con múltiples modos y opciones. Aprende a interpretar resultados y documentación, pero realiza pruebas solo sobre activos propios o autorizados y con parámetros acordes al alcance.

#### 23.5.09 — Nmap Scripting Engine (NSE)
Nmap Scripting Engine (NSE) amplía Nmap con scripts de descubrimiento y comprobación. Revisa categoría y efecto de cada script antes de usarlo; algunos realizan acciones intrusivas y no son adecuados para producción.

### Módulo 23.6 — Gestión de vulnerabilidades

#### 23.6.01 — Vulnerability Assessment
Vulnerability Assessment identifica y prioriza debilidades conocidas o configuraciones inseguras. Define alcance, fuentes y limitaciones, valida hallazgos y produce recomendaciones accionables en lugar de una lista sin contexto.

#### 23.6.02 — CVE
CVE identifica públicamente vulnerabilidades divulgadas mediante un identificador único. Comprueba producto, versión, configuración y referencias; la presencia de un CVE no demuestra que un activo sea vulnerable.

#### 23.6.03 — CWE
CWE clasifica tipos de debilidades de software que pueden contribuir a vulnerabilidades. Utilízala para describir causa raíz y controles preventivos, no como identificador de un incidente concreto.

#### 23.6.04 — CVSS
CVSS proporciona una puntuación de severidad técnica basada en métricas definidas y versión del estándar. Registra vector y versión y complementa la puntuación con exposición, impacto de negocio y controles existentes.

#### 23.6.05 — Severidad
Severidad resume gravedad técnica o impacto según una escala declarada. Explica criterios y evita equiparar automáticamente severidad alta con prioridad máxima en todos los contextos.

#### 23.6.06 — Impacto
Impacto estima consecuencias de explotación sobre confidencialidad, integridad, disponibilidad y objetivos de negocio. Considera datos, servicios, usuarios y obligaciones regulatorias.

#### 23.6.07 — Probabilidad
Probabilidad estima posibilidad de que una vulnerabilidad sea explotada en el contexto evaluado. Considera exposición, disponibilidad de exploit, controles y actividad observada, y declara incertidumbre.

#### 23.6.08 — Priorización
Priorización combina severidad, exposición, impacto, probabilidad y facilidad de remediación. Define criterios transparentes y asigna propietario y fecha objetivo; evita ordenar exclusivamente por CVSS.

#### 23.6.09 — Falsos positivos
Falsos positivos son hallazgos reportados que no representan una vulnerabilidad aplicable o confirmada. Valida evidencia, versión y configuración, documenta motivo de cierre y conserva posibilidad de reabrir si cambia el contexto.

#### 23.6.10 — Remediación
Remediación corrige la causa raíz mediante parche, configuración, mitigación o rediseño. Define responsable, prueba de regresión y verificación posterior y registra riesgo residual si la corrección se aplaza.

### Módulo 23.7 — Herramientas

#### 23.7.01 — Nessus
Nessus es un escáner de vulnerabilidades que utiliza plugins y comprobaciones configurables. Verifica alcance, credenciales, intensidad y licencia; valida hallazgos críticos antes de reportar y protege resultados sensibles.

#### 23.7.02 — OpenVAS
OpenVAS es una solución de evaluación de vulnerabilidades dentro del ecosistema Greenbone. Mantén feeds actualizados, limita escaneos a activos autorizados y comprende falsos positivos y cobertura del motor.

#### 23.7.03 — Greenbone
Greenbone ofrece componentes para gestión y evaluación de vulnerabilidades. Define roles, credenciales de escaneo y retención de reportes; trata resultados como información sensible de infraestructura.

#### 23.7.04 — Nmap
Nmap puede complementar inventarios y validación de exposición de servicios, pero no reemplaza un escáner de vulnerabilidades ni una revisión de configuración. Documenta qué pregunta responde cada herramienta.

#### 23.7.05 — Nmap NSE
NSE permite comprobaciones específicas sobre servicios, con scripts de distinto riesgo. Revisa documentación, categorías y efectos secundarios y selecciona solo scripts permitidos por las reglas de operación.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 58 orientaciones genéricas por explicaciones específicas de reconocimiento, OSINT, inventario, escaneo, enumeración y gestión de vulnerabilidades. Se reforzaron la trazabilidad de fuentes, confianza de hallazgos, minimización de datos personales y distinción entre observación, inferencia y confirmación.

**Revisión interna:** 58/58 entradas desarrolladas y cotejadas con el roadmap. Se establecieron límites claros para reconocimiento activo, Nmap/NSE y escáneres: solo activos propios o expresamente autorizados, con alcance, ventana, tasa y condiciones de detención. Pendiente: verificar versiones/licencias de herramientas, ejecutar prácticas solo en laboratorio aislado y revisar resultados con un segundo evaluador. No se escanearon activos ni se declara aprobación externa.
