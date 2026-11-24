# Etapa 21 — Fundamentos de ciberseguridad, gestión de riesgos y ética

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** comprender el panorama de la ciberseguridad, sus principios, amenazas, responsabilidades y marcos de protección.  
**Proyecto oficial:** elaborar una evaluación de riesgos para una empresa ficticia, identificando activos, amenazas, vulnerabilidades, impactos y controles.

## Resultados de aprendizaje
Distinguir seguridad informática, seguridad de la información y ciberseguridad; explicar principios CIA y atributos relacionados; identificar activos, amenazas, vulnerabilidades y riesgos; aplicar un proceso básico de gestión de riesgos; reconocer amenazas; interpretar marcos de referencia; respetar autorización y legislación; y diseñar controles IAM.

## 21.1 — Introducción a la ciberseguridad
La seguridad informática protege sistemas y recursos tecnológicos. La seguridad de la información protege información en cualquier formato. La ciberseguridad aborda riesgos y protección en entornos digitales y conectados. La seguridad de aplicaciones se enfoca en software y sus datos; la de infraestructura protege redes, sistemas, plataformas y servicios; la seguridad empresarial integra gobierno, procesos, personas y tecnología.

Red Team simula capacidades adversarias dentro de un alcance autorizado; Blue Team previene, detecta y responde; Purple Team facilita colaboración y transferencia de aprendizaje. No son cargos universales ni equipos que deban competir: son funciones complementarias.

## 21.2 — Principios fundamentales
La tríada CIA comprende confidencialidad, integridad y disponibilidad. Confidencialidad limita divulgación; integridad protege exactitud y cambios autorizados; disponibilidad mantiene acceso cuando se necesita. Autenticidad permite verificar identidad/origen; no repudio aporta evidencia frente a negación bajo un marco técnico/legal apropiado; accountability permite atribuir acciones a identidades y registros confiables.

Ningún control aislado satisface todos los principios. Cifrado puede apoyar confidencialidad, pero no garantiza disponibilidad ni corrige permisos incorrectos.

**Ejercicio:** clasifica cinco activos ficticios según impacto de pérdida de confidencialidad, integridad y disponibilidad.

## 21.3 — Conceptos de seguridad
- **Asset:** recurso con valor para la organización.
- **Threat:** circunstancia o actor capaz de causar daño.
- **Vulnerability:** debilidad que puede ser explotada o contribuir a un incidente.
- **Exploit:** técnica o código que aprovecha una debilidad.
- **Attack vector:** camino o mecanismo de ataque.
- **Attack surface:** puntos de exposición e interacción.
- **Risk:** efecto de incertidumbre sobre objetivos; en ciberseguridad se analiza mediante escenarios, probabilidad/posibilidad e impacto.
- **Security controls:** medidas preventivas, detectivas, correctivas o compensatorias.

Distingue amenaza, vulnerabilidad, incidente y riesgo. Una vulnerabilidad no determina por sí sola el riesgo: importan exposición, controles, impacto y contexto.

## 21.4 — Gestión de riesgos
Proceso recomendado:
1. Identificar activos, propietarios y dependencias.
2. Clasificar información según sensibilidad y criticidad.
3. Definir escenarios de amenaza.
4. Identificar vulnerabilidades y controles existentes.
5. Estimar probabilidad/posibilidad e impacto con escalas documentadas.
6. Priorizar y registrar incertidumbre.
7. Seleccionar tratamiento: mitigar, aceptar, transferir o evitar.
8. Asignar responsable, fecha y evidencia.
9. Revisar riesgo residual y cambios del entorno.

Una matriz de riesgos es una herramienta de comunicación, no una medición objetiva universal. Documenta criterios y evita falsa precisión.

**Ejercicio:** desarrolla un registro de riesgos para una empresa ficticia con inventario, correo, nómina, sitio web y copias de seguridad.

## 21.5 — Ciberamenazas
Estudia malware, ransomware, spyware, troyanos, gusanos, phishing, spear phishing, robo de credenciales, ingeniería social, amenazas internas, ataques a cadena de suministro, DoS y DDoS. Analiza objetivos, señales, impacto, controles y respuesta; no construyas ni distribuyas malware ni realices campañas reales de phishing.

Distingue vector inicial, ejecución, persistencia, movimiento lateral, impacto y recuperación como fases analíticas, sin asumir que todos los incidentes siguen una secuencia única.

## 21.6 — Marcos y estándares
- **NIST Cybersecurity Framework 2.0:** Govern, Identify, Protect, Detect, Respond y Recover. Organiza resultados de ciberseguridad y perfiles; no es una lista de herramientas.
- **ISO/IEC 27001:2022:** requisitos para un sistema de gestión de seguridad de la información; considera enmiendas vigentes y alcance de certificación.
- **ISO/IEC 27002:2022:** guía de controles de seguridad.
- **ISO/IEC 27005:** gestión de riesgos de seguridad de la información; verifica edición aplicable.
- **CIS Controls:** conjunto priorizado de salvaguardas.
- **MITRE ATT&CK:** base de conocimiento de tácticas y técnicas observadas/adversarias; no es un estándar de certificación.
- **Zero Trust:** enfoque que evita confiar implícitamente por ubicación de red y requiere evaluación explícita de identidad, dispositivo y contexto.

No copies contenido protegido de normas ISO. Consulta catálogos oficiales, distingue requisitos de guías y registra versión.

## 21.7 — Ética y legislación
El hacking ético requiere autorización expresa, alcance definido, reglas de compromiso, límites, protección de datos y gestión de evidencias. White Hat, Gray Hat y Black Hat son etiquetas descriptivas; la intención declarada no reemplaza autorización legal.

Antes de una prueba, documenta activos incluidos/excluidos, ventanas, técnicas permitidas, contactos, tratamiento de datos, criterios de parada, reporte y divulgación responsable. En Colombia, consulta normativa vigente y asesoría competente para casos concretos; esta guía educativa no es asesoría jurídica. Considera protección de datos personales, delitos informáticos, contratos y obligaciones de notificación aplicables.

## 21.8 — Gestión de identidades (IAM)
IAM administra identidades y permisos. Distingue usuarios humanos, cuentas de servicio, roles, permisos, privilegios y federación. MFA añade factores de categorías distintas. RBAC asigna acceso mediante roles; ABAC utiliza atributos de sujeto, recurso, acción y contexto. Least Privilege limita permisos; revisa accesos, cuentas inactivas, secretos de servicio y privilegios temporales.

**Ejercicio:** diseña matriz de roles y permisos para una empresa ficticia; incluye proceso de alta, cambio, baja, MFA y revisión periódica.

## Proyecto oficial — Evaluación de riesgos
Entregables:
1. Contexto y alcance de la empresa ficticia.
2. Inventario de activos y propietarios.
3. Clasificación de información.
4. Escenarios de amenaza y vulnerabilidad.
5. Criterios de impacto y probabilidad.
6. Matriz y registro de riesgos.
7. Tratamiento, responsables y fechas.
8. Controles existentes y propuestos.
9. Riesgo residual y aceptación documentada.
10. Modelo IAM y reglas de autorización.
11. Marco de referencia seleccionado y justificación.
12. Resumen ejecutivo y limitaciones.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Conceptos y principios | 15 |
| Inventario y clasificación | 15 |
| Amenazas y vulnerabilidades | 15 |
| Método de análisis de riesgo | 20 |
| Tratamiento y controles | 15 |
| Marcos y estándares | 10 |
| Ética, legalidad e IAM | 10 |

Criterio orientativo: 80/100 y trazabilidad de riesgos a activos y tratamientos.

## Autoevaluación
1. Diferencia seguridad de información y ciberseguridad.
2. ¿Qué aporta CIA y qué no cubre?
3. Diferencia amenaza y vulnerabilidad.
4. ¿Qué factores influyen en el riesgo?
5. ¿Qué diferencia hay entre mitigar y aceptar?
6. ¿Cuáles son las seis funciones de NIST CSF 2.0?
7. ¿Qué diferencia hay entre ISO 27001 y 27002?
8. ¿Qué condiciones hacen ética una prueba de seguridad?
9. Diferencia RBAC y ABAC.
10. ¿Por qué una cuenta de servicio también necesita propietario y revisión?

## Recursos audiovisuales
No se incluyen videos aprobados. Se añadirán solo con audio hablado en español y contenido directamente relacionado con el concepto (NIST CSF 2.0, análisis de riesgos, IAM, ética o marcos de gestión).

## Referencias oficiales
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-30: https://csrc.nist.gov/pubs/sp/800/30/r1/final
- ISO/IEC 27001: https://www.iso.org/standard/27001
- ISO/IEC 27002: https://www.iso.org/standard/75652.html
- ISO/IEC 27005: https://www.iso.org/standard/80585.html
- CIS Controls: https://www.cisecurity.org/controls
- MITRE ATT&CK: https://attack.mitre.org/
- NIST Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- OWASP: https://owasp.org/
- Colombia, MinTIC: https://www.mintic.gov.co/

**Consulta documental:** 2026-11-19. **Verificación práctica:** ejercicio ficticio no auditado en organización real. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 21

Este desglose conserva las entradas del roadmap maestro, incluidas las notas explicativas que aparecen dentro de algunas listas curriculares. Los apartados son guías de estudio y no acreditan pruebas, autorización de laboratorio ni ejecución de herramientas.

### Módulo 21.1 — Introducción a la ciberseguridad

#### 21.1.01 — Seguridad informática
Seguridad informática protege sistemas, equipos, redes y servicios frente a accesos, alteraciones e interrupciones no autorizadas. Incluye controles técnicos y operativos y debe evaluarse según activos, amenazas y contexto.

#### 21.1.02 — Seguridad de la información
Seguridad de la información protege información en cualquier formato durante su creación, uso, almacenamiento y eliminación. Aplica controles de confidencialidad, integridad y disponibilidad también a documentos físicos y procesos humanos.

#### 21.1.03 — Ciberseguridad
Ciberseguridad aborda riesgos sobre sistemas digitales, redes, servicios y datos conectados. Considera amenazas internas y externas, dependencias y continuidad; no se limita a instalar herramientas defensivas.

#### 21.1.04 — Seguridad de aplicaciones
Seguridad de aplicaciones integra requisitos, diseño, implementación, pruebas y operación para reducir vulnerabilidades del software. Incluye modelado de amenazas, prácticas de código seguro, gestión de dependencias y respuesta a fallos.

#### 21.1.05 — Seguridad de infraestructura
Seguridad de infraestructura protege cómputo, redes, almacenamiento, identidades y servicios base. Mantén inventario, configuración endurecida, parches, segmentación, monitoreo y recuperación probada.

#### 21.1.06 — Seguridad empresarial
Seguridad empresarial coordina políticas, personas, procesos, tecnología y terceros para gestionar riesgo organizacional. Define responsabilidades, apetito de riesgo, gobernanza, continuidad y mecanismos de supervisión.

#### 21.1.07 — Red Team
Red Team simula adversarios para evaluar detección y resistencia bajo alcance autorizado. Sus actividades deben tener objetivos, reglas de operación, límites y mecanismos de detención definidos.

#### 21.1.08 — Blue Team
Blue Team defiende sistemas mediante prevención, monitoreo, detección, respuesta y recuperación. Prioriza telemetría, gestión de vulnerabilidades, control de cambios y aprendizaje posterior a incidentes.

#### 21.1.09 — Purple Team
Purple Team facilita colaboración entre funciones ofensivas y defensivas para convertir hallazgos en mejoras medibles. Documenta técnicas emuladas, detecciones observadas y cambios de control sin asumir que una simulación equivale a un ataque real.

### Módulo 21.2 — Principios fundamentales

#### 21.2.01 — CIA Triad
CIA Triad reúne confidencialidad, integridad y disponibilidad como objetivos clásicos de seguridad. Evalúa qué propiedad afecta cada amenaza y evita tratar la tríada como catálogo completo de requisitos.

#### 21.2.02 — Confidentiality
Confidentiality limita la divulgación de información a sujetos autorizados. Aplica clasificación, cifrado, control de acceso y minimización; revisa también copias, logs, respaldos y canales de soporte.

#### 21.2.03 — Integrity
Integrity protege exactitud y completitud de datos y sistemas frente a cambios no autorizados o accidentales. Usa controles de acceso, validaciones, firmas/hashes cuando corresponda y trazabilidad de cambios.

#### 21.2.04 — Availability
Availability garantiza que sistemas e información estén accesibles cuando se requieren dentro de objetivos definidos. Diseña redundancia, capacidad, backup y recuperación y prueba escenarios de interrupción.

#### 21.2.05 — Authenticity
Authenticity aporta confianza sobre la identidad u origen de una entidad, mensaje o dato. Utiliza mecanismos de autenticación y validación criptográfica adecuados y gestiona claves y certificados.

#### 21.2.06 — Non-repudiation
Non-repudiation busca aportar evidencia que vincule una acción o comunicación con su origen y contexto. Depende de controles criptográficos, gestión de claves, tiempo y procedimientos; un log simple no garantiza no repudio legal.

#### 21.2.07 — Accountability
Accountability permite atribuir acciones a identidades y responsabilidades mediante registros y controles. Usa cuentas individuales, sincronización horaria, protección de logs y revisiones de acceso; evita cuentas compartidas sin trazabilidad.

### Módulo 21.3 — Conceptos de seguridad

#### 21.3.01 — Assets
Assets son elementos con valor para una organización, como datos, servicios, infraestructura, reputación y procesos. Identifica propietario, ubicación, clasificación y dependencia antes de analizar riesgos.

#### 21.3.02 — Threats
Threats son circunstancias o actores capaces de causar daño a activos mediante acciones o eventos. Distingue amenaza, vulnerabilidad e impacto y documenta motivación, capacidad y contexto cuando exista evidencia.

#### 21.3.03 — Vulnerabilities
Vulnerabilities son debilidades que pueden ser explotadas o desencadenar un impacto. Prioriza por explotabilidad, exposición y consecuencias, y diferencia hallazgos confirmados de hipótesis.

#### 21.3.04 — Exploits
Exploits son técnicas o artefactos que aprovechan una vulnerabilidad para producir un efecto. Estúdialos con enfoque defensivo, en entornos controlados y autorizados, y vincula mitigación con causa raíz.

#### 21.3.05 — Attack Vectors
Attack Vectors son rutas o métodos por los que una amenaza puede alcanzar un activo. Incluyen interfaces técnicas, credenciales, personas y terceros; identifica controles preventivos y de detección para cada vector.

#### 21.3.06 — Attack Surface
Attack Surface reúne los puntos expuestos donde una interacción puede afectar un sistema. Mantén inventario actualizado de servicios, identidades, integraciones y entradas y reduce exposición innecesaria.

#### 21.3.07 — Risk
Risk combina incertidumbre, probabilidad y consecuencias sobre objetivos, según el método de evaluación adoptado. Define escala y contexto; evita presentar una puntuación cualitativa como medición científica exacta.

#### 21.3.08 — Impact
Impact describe la magnitud de consecuencias sobre operaciones, personas, finanzas, cumplimiento y reputación. Define escenarios y criterios de impacto con responsables del negocio.

#### 21.3.09 — Likelihood
Likelihood estima la posibilidad de que ocurra un escenario en un horizonte definido. Fundamenta la estimación con exposición, amenaza, controles y datos disponibles y registra incertidumbre.

#### 21.3.10 — Security Controls
Security Controls son medidas administrativas, técnicas o físicas que modifican riesgo. Clasifícalas por función preventiva, detectiva, correctiva o compensatoria y comprueba que operen en la práctica.

### Módulo 21.4 — Gestión de riesgos

#### 21.4.01 — Identificación de activos
Identificación de activos determina qué debe protegerse, quién lo posee y qué dependencias tiene. Mantén inventario de datos, aplicaciones, identidades, infraestructura y terceros con criticidad asignada.

#### 21.4.02 — Clasificación de información
Clasificación de información asigna niveles de sensibilidad y reglas de manejo. Define etiquetas, almacenamiento, transmisión, retención y destrucción; clasifica también copias y exportaciones.

#### 21.4.03 — Identificación de amenazas
Identificación de amenazas describe escenarios plausibles que podrían afectar activos y objetivos. Usa fuentes internas y externas y evita convertir listas genéricas en amenazas confirmadas sin contexto.

#### 21.4.04 — Identificación de vulnerabilidades
Identificación de vulnerabilidades localiza debilidades mediante inventarios, configuración, análisis y pruebas autorizadas. Registra evidencia, alcance, versión y limitaciones y coordina corrección con propietarios.

#### 21.4.05 — Análisis de probabilidad
Análisis de probabilidad estima posibilidad de un escenario considerando amenaza, exposición y eficacia de controles. Declara método, escala y horizonte temporal para que distintas evaluaciones sean comparables.

#### 21.4.06 — Análisis de impacto
Análisis de impacto estima consecuencias operativas, financieras, legales, humanas y reputacionales. Consulta a propietarios de procesos y define escenarios de peor caso razonable y efectos secundarios.

#### 21.4.07 — Matriz de riesgos
Una matriz de riesgos representa combinación de probabilidad e impacto según escalas definidas. No es universal: documenta umbrales y criterios de aceptación y no ocultes incertidumbre detrás de colores.

#### 21.4.08 — Evaluación de riesgos
Evaluación de riesgos compara resultados con criterios de tolerancia y prioriza tratamiento. Asigna propietario, fecha y evidencia; la evaluación debe repetirse cuando cambian activos, amenazas o controles.

#### 21.4.09 — Tratamiento de riesgos
Tratamiento de riesgos selecciona opciones para modificar el riesgo: mitigar, aceptar, transferir o evitar. Documenta decisión, autoridad, coste, riesgo residual y fecha de revisión.

#### 21.4.10 — Mitigación
Mitigación reduce probabilidad o impacto mediante controles. Prioriza medidas proporcionales y medibles, define responsable y comprueba eficacia después de implantarlas.

#### 21.4.11 — Aceptación
Aceptación reconoce formalmente un riesgo residual dentro de la autoridad y tolerancia establecidas. Registra justificación, propietario, vencimiento y condiciones que obligan a reconsiderar la decisión.

#### 21.4.12 — Transferencia
Transferencia comparte parte de consecuencias o responsabilidades mediante seguros, contratos o proveedores. No elimina el riesgo ni la responsabilidad de supervisión; evalúa exclusiones y dependencias de terceros.

#### 21.4.13 — Evitación
Evitación elimina la actividad o condición que origina el riesgo. Comprueba efectos sobre objetivos y alternativas y documenta por qué el beneficio de no continuar supera el coste.

### Módulo 21.5 — Ciberamenazas

#### 21.5.01 — Malware
Malware es software diseñado para realizar acciones no autorizadas o dañinas, como robo, sabotaje o control remoto. Estudia familias y señales desde defensa y analiza muestras solo en laboratorios aislados.

#### 21.5.02 — Ransomware
Ransomware bloquea o cifra datos y suele combinarse con extorsión y robo de información. Previene con backups desconectados/protegidos, segmentación, MFA y respuesta ensayada; no asumas que pagar recupera los datos.

#### 21.5.03 — Spyware
Spyware recopila información o actividad sin autorización y puede operar de forma persistente. Busca indicadores en endpoints y tráfico, limita privilegios y protege credenciales y datos.

#### 21.5.04 — Trojan
Trojan se presenta como software legítimo o útil mientras realiza acciones ocultas. Verifica origen, firma y comportamiento de instaladores y evita ejecutar archivos desconocidos fuera de sandbox.

#### 21.5.05 — Worms
Worms se propagan entre sistemas aprovechando conectividad o vulnerabilidades con poca intervención del usuario. Segmenta redes, aplica parches y detecta patrones de propagación.

#### 21.5.06 — Phishing
Phishing engaña a personas para obtener credenciales, datos o ejecutar acciones. Combina formación con MFA resistente al phishing, filtros, reporte sencillo y procesos de verificación fuera del canal sospechoso.

#### 21.5.07 — Spear Phishing
Spear Phishing personaliza el engaño para una persona o grupo usando contexto y relaciones reales. Verifica solicitudes sensibles por un canal independiente y limita información pública que facilite suplantación.

#### 21.5.08 — Credential Theft
Credential Theft obtiene contraseñas, tokens o claves mediante engaño, malware, filtración o reutilización. Usa gestores de contraseñas, MFA, rotación/revocación y detección de accesos anómalos.

#### 21.5.09 — Social Engineering
Social Engineering manipula comportamientos mediante autoridad, urgencia, confianza o presión. Establece procesos de verificación, doble aprobación y canales de reporte sin culpabilizar a quien recibe el engaño.

#### 21.5.10 — Insider Threats
Insider Threats son riesgos derivados de personas con acceso legítimo, intencionalmente o por error. Aplica mínimo privilegio, segregación de funciones, monitoreo proporcional y procesos de salida/cambio de rol.

#### 21.5.11 — Supply Chain Attacks
Supply Chain Attacks comprometen un proveedor, dependencia o proceso de distribución para alcanzar objetivos posteriores. Inventaría terceros, verifica integridad, limita permisos y establece requisitos de seguridad y respuesta contractual.

#### 21.5.12 — Denial of Service
Denial of Service busca degradar o interrumpir un servicio mediante agotamiento de recursos o fallos inducidos. Diseña límites, redundancia y filtrado y coordina mitigación con proveedores.

#### 21.5.13 — Distributed Denial of Service
Distributed Denial of Service utiliza múltiples fuentes para amplificar o distribuir el tráfico dañino. Apóyate en mitigación upstream, CDN/proveedor y planes de continuidad; no intentes responder con acciones de represalia.

### Módulo 21.6 — Marcos y estándares

#### 21.6.01 — NIST Cybersecurity Framework 2.0
NIST Cybersecurity Framework 2.0 organiza resultados de ciberseguridad mediante las funciones Govern, Identify, Protect, Detect, Respond y Recover. Úsalo para perfilar estado actual/objetivo y priorizar resultados según riesgo y contexto organizacional.

#### 21.6.02 — ISO/IEC 27001:2022
ISO/IEC 27001:2022 especifica requisitos para establecer, mantener y mejorar un sistema de gestión de seguridad de la información. Define alcance, evaluación/tratamiento de riesgos y evidencia; no equivale a una certificación automática por usar controles.

#### 21.6.03 — ISO/IEC 27002:2022
ISO/IEC 27002:2022 proporciona orientación sobre controles de seguridad de la información. Selecciona controles según riesgo y contexto y relaciona su aplicación con políticas, responsables y evidencia.

#### 21.6.04 — ISO/IEC 27005
ISO/IEC 27005 ofrece orientación para gestionar riesgos de seguridad de la información. Integra contexto, identificación, análisis, evaluación, tratamiento y seguimiento con el sistema de gestión.

#### 21.6.05 — CIS Controls
CIS Controls reúne salvaguardas priorizadas para reducir riesgos comunes de ciberseguridad. Adapta implementación a activos y capacidad, mide cobertura y no asumas que una lista de controles reemplaza análisis de riesgos.

#### 21.6.06 — MITRE ATT&CK
MITRE ATT&CK organiza tácticas y técnicas observadas de adversarios para apoyar detección, análisis y emulación autorizada. Usa versión y plataforma identificadas y evita interpretar una técnica mapeada como prueba de que ocurrió un ataque.

#### 21.6.07 — Principios Zero Trust
Zero Trust parte de no conceder confianza implícita por ubicación de red y requiere verificación explícita y continua según contexto. Aplica identidad, dispositivo, recurso y política; no es un producto único ni una migración instantánea.

#### 21.6.08 — Information security management systems
Un Information Security Management System (ISMS/SGSI) coordina políticas, procesos, evaluación de riesgos, controles, auditoría y mejora continua. Define alcance y liderazgo, conserva evidencia y revisa eficacia en ciclos regulares.

### Módulo 21.7 — Ética y legislación

#### 21.7.01 — Hacking ético
Hacking ético evalúa controles de forma autorizada y con objetivos defensivos definidos. Exige permiso previo, alcance, reglas de operación, protección de datos y reporte responsable; la intención declarada no sustituye autorización.

#### 21.7.02 — Diferencia entre White Hat, Gray Hat y Black Hat
White Hat actúa con autorización y propósito defensivo; Gray Hat puede investigar sin autorización suficiente; Black Hat opera con intención maliciosa o ilegal. La etiqueta no determina legalidad: el permiso y el alcance documentado son decisivos.

#### 21.7.03 — Autorización
Autorización debe ser explícita, otorgada por quien tiene facultad sobre los activos y vigente durante la actividad. Define métodos, horarios, sistemas, datos, terceros y límites de impacto.

#### 21.7.04 — Alcance
Alcance enumera sistemas, direcciones, aplicaciones, cuentas, técnicas permitidas y exclusiones. Mantén una lista inequívoca y detén la actividad si aparece un activo no incluido.

#### 21.7.05 — Rules of Engagement
Rules of Engagement documentan objetivos, ventanas, contactos, restricciones, tratamiento de hallazgos y condiciones de detención. Deben aprobarse antes de cualquier prueba y estar disponibles para todo el equipo.

#### 21.7.06 — Confidencialidad
Confidencialidad obliga a proteger información obtenida durante auditorías, incidentes y proyectos. Minimiza copias, limita acceso, cifra evidencias y define retención y destrucción.

#### 21.7.07 — Divulgación responsable
Divulgación responsable coordina la comunicación de vulnerabilidades con el propietario y, cuando proceda, un programa de divulgación. Evita publicar datos explotables antes de mitigación y sigue plazos y políticas acordadas.

#### 21.7.08 — Protección de datos
Protección de datos exige tratar información personal con finalidad, proporcionalidad, seguridad y derechos aplicables. Minimiza recolección, restringe acceso y consulta normativa vigente y responsables de privacidad antes de procesar datos reales.

#### 21.7.09 — Gestión de evidencias
Gestión de evidencias preserva integridad, procedencia, contexto y acceso a artefactos de una investigación. Registra quién recolectó, cuándo, cómo, hashes y transferencias; trabaja sobre copias y conserva originales protegidos.

#### 21.7.10 — Responsabilidad profesional
Responsabilidad profesional implica competencia, honestidad, confidencialidad y comunicación clara de límites y riesgos. No exageres resultados, informa conflictos de interés y detén actividades que excedan el mandato.

#### 21.7.11 — Consideraciones legales colombianas
Las consideraciones legales colombianas requieren revisar legislación vigente sobre delitos informáticos, protección de datos, telecomunicaciones, evidencia y obligaciones sectoriales. Documenta jurisdicción y fecha, consulta fuentes oficiales y asesoría competente; este temario no sustituye concepto jurídico.

### Módulo 21.8 — Gestión de identidades (IAM)

#### 21.8.01 — Identity and Access Management
Identity and Access Management administra el ciclo de vida de identidades, autenticación, autorización y auditoría. Integra altas, cambios y bajas con sistemas y procesos de negocio y revisa accesos periódicamente.

#### 21.8.02 — Usuarios
Usuarios representan identidades humanas o técnicas con atributos y credenciales. Evita cuentas compartidas, verifica identidad durante el alta y deshabilita accesos cuando termina la necesidad.

#### 21.8.03 — Roles
Roles agrupan responsabilidades y permisos para simplificar asignación de acceso. Mantén catálogo revisado, evita acumulación de roles y vincula cambios de puesto con recertificación.

#### 21.8.04 — Permisos
Permisos definen acciones concretas sobre recursos. Asigna permisos explícitos, aplica mínimo privilegio y prueba accesos denegados además de los permitidos.

#### 21.8.05 — Privilegios
Privilegios permiten acciones administrativas o sensibles sobre sistemas y datos. Separa cuentas ordinarias y administrativas, eleva temporalmente y registra actividades de alto impacto.

#### 21.8.06 — MFA
MFA requiere más de un factor independiente para autenticar. Prioriza métodos resistentes al phishing y protege el proceso de recuperación para que no se convierta en el eslabón débil.

#### 21.8.07 — RBAC
RBAC vincula usuarios y grupos a roles con permisos predefinidos. Define jerarquías con cautela y revisa conflictos de segregación de funciones.

#### 21.8.08 — ABAC
ABAC evalúa atributos de identidad, recurso, acción y contexto para tomar decisiones de acceso. Mantén atributos confiables, políticas auditables y reglas de denegación claras.

#### 21.8.09 — Least Privilege
Least Privilege limita cada identidad a permisos mínimos y temporales. Revisa accesos reales y elimina privilegios heredados que ya no responden a la función.

#### 21.8.10 — Identity Federation
Identity Federation permite que una organización confíe en un proveedor de identidad externo mediante protocolos y relaciones configuradas. Valida issuer, audience, certificados y atributos y define revocación y gestión de confianza.

#### 21.8.11 — Service Accounts
Service Accounts son identidades no humanas usadas por aplicaciones y automatizaciones. Asigna credenciales de corta duración cuando sea posible, limita permisos, rota secretos y monitorea su uso.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 82 orientaciones genéricas por explicaciones específicas de fundamentos, principios, conceptos de riesgo, metodología, amenazas, marcos, ética/legislación e IAM.

**Revisión interna:** 82/82 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron autorización, límites de alcance, preservación de evidencia, protección de datos, responsabilidad profesional y controles de identidades técnicas. Las consideraciones legales colombianas se mantienen como materia de verificación normativa vigente y no como asesoría jurídica. Pendiente: cotejar referencias oficiales y legislación aplicable, realizar ejercicios de evaluación de riesgos con escenarios ficticios y obtener segunda revisión especializada. No se ejecutaron operaciones de seguridad ni se declara aprobación externa.
