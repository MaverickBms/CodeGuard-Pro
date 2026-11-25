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


**Práctica y evidencia:** Clasifica controles físicos, lógicos y administrativos para proteger un activo de laboratorio. **Evidencia:** explica amenaza, control y riesgo residual.

#### 21.1.02 — Seguridad de la información
Seguridad de la información protege información en cualquier formato durante su creación, uso, almacenamiento y eliminación. Aplica controles de confidencialidad, integridad y disponibilidad también a documentos físicos y procesos humanos.


**Práctica y evidencia:** Identifica un conjunto de información sensible y define controles de acceso, integridad y disponibilidad. **Evidencia:** relaciona cada control con el valor de la información.

#### 21.1.03 — Ciberseguridad
Ciberseguridad aborda riesgos sobre sistemas digitales, redes, servicios y datos conectados. Considera amenazas internas y externas, dependencias y continuidad; no se limita a instalar herramientas defensivas.


**Práctica y evidencia:** Dibuja un ecosistema de ciberseguridad que incluya personas, procesos, tecnología y terceros. **Evidencia:** identifica dependencias entre dominios.

#### 21.1.04 — Seguridad de aplicaciones
Seguridad de aplicaciones integra requisitos, diseño, implementación, pruebas y operación para reducir vulnerabilidades del software. Incluye modelado de amenazas, prácticas de código seguro, gestión de dependencias y respuesta a fallos.


**Práctica y evidencia:** Revisa un flujo de aplicación desde entrada hasta almacenamiento y marca puntos de validación y autorización. **Evidencia:** presenta amenazas y controles por etapa.

#### 21.1.05 — Seguridad de infraestructura
Seguridad de infraestructura protege cómputo, redes, almacenamiento, identidades y servicios base. Mantén inventario, configuración endurecida, parches, segmentación, monitoreo y recuperación probada.


**Práctica y evidencia:** Inventaría sistemas, redes, endpoints, respaldos y servicios de infraestructura de un entorno ficticio. **Evidencia:** identifica propietario y criticidad.

#### 21.1.06 — Seguridad empresarial
Seguridad empresarial coordina políticas, personas, procesos, tecnología y terceros para gestionar riesgo organizacional. Define responsabilidades, apetito de riesgo, gobernanza, continuidad y mecanismos de supervisión.


**Práctica y evidencia:** Diseña un programa básico de seguridad empresarial con gobierno, riesgos, controles y respuesta. **Evidencia:** asigna responsables y métricas.

#### 21.1.07 — Red Team
Red Team simula adversarios para evaluar detección y resistencia bajo alcance autorizado. Sus actividades deben tener objetivos, reglas de operación, límites y mecanismos de detención definidos.


**Práctica y evidencia:** Define una actividad Red Team en laboratorio con autorización, alcance y objetivos de simulación. **Evidencia:** documenta reglas de seguridad y límites; no ejecuta acciones contra terceros.

#### 21.1.08 — Blue Team
Blue Team defiende sistemas mediante prevención, monitoreo, detección, respuesta y recuperación. Prioriza telemetría, gestión de vulnerabilidades, control de cambios y aprendizaje posterior a incidentes.


**Práctica y evidencia:** Construye un caso Blue Team para detectar una actividad anómala en logs sintéticos. **Evidencia:** registra hipótesis, señales y respuesta defensiva.

#### 21.1.09 — Purple Team
Purple Team facilita colaboración entre funciones ofensivas y defensivas para convertir hallazgos en mejoras medibles. Documenta técnicas emuladas, detecciones observadas y cambios de control sin asumir que una simulación equivale a un ataque real.


**Práctica y evidencia:** Diseña un ejercicio Purple Team donde hallazgos de simulación se convierten en detecciones y mejoras. **Evidencia:** mapea técnica, telemetría y control defensivo.

### Módulo 21.2 — Principios fundamentales

#### 21.2.01 — CIA Triad
CIA Triad reúne confidencialidad, integridad y disponibilidad como objetivos clásicos de seguridad. Evalúa qué propiedad afecta cada amenaza y evita tratar la tríada como catálogo completo de requisitos.


**Práctica y evidencia:** Evalúa un escenario con pérdida de confidencialidad, integridad y disponibilidad. **Evidencia:** identifica qué dimensión se afecta y controles apropiados.

#### 21.2.02 — Confidentiality
Confidentiality limita la divulgación de información a sujetos autorizados. Aplica clasificación, cifrado, control de acceso y minimización; revisa también copias, logs, respaldos y canales de soporte.


**Práctica y evidencia:** Clasifica información y define quién puede consultarla y bajo qué necesidad. **Evidencia:** propone controles de acceso y manejo seguro.

#### 21.2.03 — Integrity
Integrity protege exactitud y completitud de datos y sistemas frente a cambios no autorizados o accidentales. Usa controles de acceso, validaciones, firmas/hashes cuando corresponda y trazabilidad de cambios.


**Práctica y evidencia:** Define mecanismos para detectar modificación no autorizada de un archivo de evidencia. **Evidencia:** compara hash, firma y control de acceso.

#### 21.2.04 — Availability
Availability garantiza que sistemas e información estén accesibles cuando se requieren dentro de objetivos definidos. Diseña redundancia, capacidad, backup y recuperación y prueba escenarios de interrupción.


**Práctica y evidencia:** Diseña una estrategia de continuidad para un servicio crítico. **Evidencia:** define RTO/RPO y dependencias.

#### 21.2.05 — Authenticity
Authenticity aporta confianza sobre la identidad u origen de una entidad, mensaje o dato. Utiliza mecanismos de autenticación y validación criptográfica adecuados y gestiona claves y certificados.


**Práctica y evidencia:** Valida identidad de una fuente y autenticidad de un artefacto con cadena de confianza. **Evidencia:** diferencia autenticidad de confidencialidad.

#### 21.2.06 — Non-repudiation
Non-repudiation busca aportar evidencia que vincule una acción o comunicación con su origen y contexto. Depende de controles criptográficos, gestión de claves, tiempo y procedimientos; un log simple no garantiza no repudio legal.


**Práctica y evidencia:** Analiza cómo una firma digital puede aportar evidencia de autoría e integridad y sus límites jurídicos/técnicos. **Evidencia:** identifica gestión de claves y validación.

#### 21.2.07 — Accountability
Accountability permite atribuir acciones a identidades y responsabilidades mediante registros y controles. Usa cuentas individuales, sincronización horaria, protección de logs y revisiones de acceso; evita cuentas compartidas sin trazabilidad.


**Práctica y evidencia:** Asocia acciones administrativas con una identidad, hora y recurso para poder auditarlas. **Evidencia:** diseña registro que permita atribución sin almacenar secretos.

### Módulo 21.3 — Conceptos de seguridad

#### 21.3.01 — Assets
Assets son elementos con valor para una organización, como datos, servicios, infraestructura, reputación y procesos. Identifica propietario, ubicación, clasificación y dependencia antes de analizar riesgos.


**Práctica y evidencia:** Construye un inventario de activos con propietario, valor, ubicación y dependencia. **Evidencia:** prioriza activos para análisis de riesgo.

#### 21.3.02 — Threats
Threats son circunstancias o actores capaces de causar daño a activos mediante acciones o eventos. Distingue amenaza, vulnerabilidad e impacto y documenta motivación, capacidad y contexto cuando exista evidencia.


**Práctica y evidencia:** Identifica amenazas internas, externas, accidentales y ambientales para un activo. **Evidencia:** describe actor, capacidad y motivación sin asumir certeza.

#### 21.3.03 — Vulnerabilities
Vulnerabilities son debilidades que pueden ser explotadas o desencadenar un impacto. Prioriza por explotabilidad, exposición y consecuencias, y diferencia hallazgos confirmados de hipótesis.


**Práctica y evidencia:** Distingue vulnerabilidad técnica, debilidad de proceso y configuración incorrecta. **Evidencia:** vincula cada una con un control preventivo.

#### 21.3.04 — Exploits
Exploits son técnicas o artefactos que aprovechan una vulnerabilidad para producir un efecto. Estúdialos con enfoque defensivo, en entornos controlados y autorizados, y vincula mitigación con causa raíz.


**Práctica y evidencia:** Explica la diferencia entre vulnerabilidad y exploit mediante un caso histórico documentado. **Evidencia:** separa debilidad, mecanismo de abuso e impacto sin ejecutar código.

#### 21.3.05 — Attack Vectors
Attack Vectors son rutas o métodos por los que una amenaza puede alcanzar un activo. Incluyen interfaces técnicas, credenciales, personas y terceros; identifica controles preventivos y de detección para cada vector.


**Práctica y evidencia:** Mapea vectores de acceso como correo, web, identidad, red y proveedor. **Evidencia:** identifica controles preventivos y de detección por vector.

#### 21.3.06 — Attack Surface
Attack Surface reúne los puntos expuestos donde una interacción puede afectar un sistema. Mantén inventario actualizado de servicios, identidades, integraciones y entradas y reduce exposición innecesaria.


**Práctica y evidencia:** Dibuja superficie de ataque de una aplicación ficticia con endpoints, roles y dependencias. **Evidencia:** propone reducción de exposición.

#### 21.3.07 — Risk
Risk combina incertidumbre, probabilidad y consecuencias sobre objetivos, según el método de evaluación adoptado. Define escala y contexto; evita presentar una puntuación cualitativa como medición científica exacta.


**Práctica y evidencia:** Calcula riesgo cualitativo con probabilidad e impacto definidos por una escala documentada. **Evidencia:** declara supuestos y no presenta el resultado como precisión matemática.

#### 21.3.08 — Impact
Impact describe la magnitud de consecuencias sobre operaciones, personas, finanzas, cumplimiento y reputación. Define escenarios y criterios de impacto con responsables del negocio.


**Práctica y evidencia:** Evalúa impacto financiero, operativo, legal, reputacional y de seguridad humana de un incidente. **Evidencia:** justifica severidad según contexto.

#### 21.3.09 — Likelihood
Likelihood estima la posibilidad de que ocurra un escenario en un horizonte definido. Fundamenta la estimación con exposición, amenaza, controles y datos disponibles y registra incertidumbre.


**Práctica y evidencia:** Estima probabilidad usando exposición, controles, historial y condiciones del entorno. **Evidencia:** registra incertidumbre y fuente de estimación.

#### 21.3.10 — Security Controls
Security Controls son medidas administrativas, técnicas o físicas que modifican riesgo. Clasifícalas por función preventiva, detectiva, correctiva o compensatoria y comprueba que operen en la práctica.


**Práctica y evidencia:** Clasifica controles como preventivos, detectivos, correctivos, disuasorios o compensatorios. **Evidencia:** asigna control a un riesgo y explica su función.

### Módulo 21.4 — Gestión de riesgos

#### 21.4.01 — Identificación de activos
Identificación de activos determina qué debe protegerse, quién lo posee y qué dependencias tiene. Mantén inventario de datos, aplicaciones, identidades, infraestructura y terceros con criticidad asignada.


**Práctica y evidencia:** Identifica activos de información, hardware, software, personas y servicios externos. **Evidencia:** crea inventario con propietario y criticidad.

#### 21.4.02 — Clasificación de información
Clasificación de información asigna niveles de sensibilidad y reglas de manejo. Define etiquetas, almacenamiento, transmisión, retención y destrucción; clasifica también copias y exportaciones.


**Práctica y evidencia:** Clasifica datos por sensibilidad y define reglas de almacenamiento, transmisión y eliminación. **Evidencia:** produce matriz de clasificación.

#### 21.4.03 — Identificación de amenazas
Identificación de amenazas describe escenarios plausibles que podrían afectar activos y objetivos. Usa fuentes internas y externas y evita convertir listas genéricas en amenazas confirmadas sin contexto.


**Práctica y evidencia:** Realiza taller de amenazas con escenarios de abuso y fallos accidentales. **Evidencia:** registra fuente, activo afectado y consecuencia.

#### 21.4.04 — Identificación de vulnerabilidades
Identificación de vulnerabilidades localiza debilidades mediante inventarios, configuración, análisis y pruebas autorizadas. Registra evidencia, alcance, versión y limitaciones y coordina corrección con propietarios.


**Práctica y evidencia:** Consulta inventario y avisos de vulnerabilidad para un producto de laboratorio y prioriza exposición. **Evidencia:** diferencia vulnerabilidad confirmada de sospecha.

#### 21.4.05 — Análisis de probabilidad
Análisis de probabilidad estima posibilidad de un escenario considerando amenaza, exposición y eficacia de controles. Declara método, escala y horizonte temporal para que distintas evaluaciones sean comparables.


**Práctica y evidencia:** Asigna probabilidad usando criterios definidos y evidencia disponible. **Evidencia:** justifica escala y registra incertidumbre.

#### 21.4.06 — Análisis de impacto
Análisis de impacto estima consecuencias operativas, financieras, legales, humanas y reputacionales. Consulta a propietarios de procesos y define escenarios de peor caso razonable y efectos secundarios.


**Práctica y evidencia:** Estima impacto por dimensiones y horizonte temporal. **Evidencia:** explica supuestos y evita doble conteo.

#### 21.4.07 — Matriz de riesgos
Una matriz de riesgos representa combinación de probabilidad e impacto según escalas definidas. No es universal: documenta umbrales y criterios de aceptación y no ocultes incertidumbre detrás de colores.


**Práctica y evidencia:** Construye matriz de riesgos con escalas y umbrales explícitos. **Evidencia:** ubica riesgos y documenta limitaciones del método.

#### 21.4.08 — Evaluación de riesgos
Evaluación de riesgos compara resultados con criterios de tolerancia y prioriza tratamiento. Asigna propietario, fecha y evidencia; la evaluación debe repetirse cuando cambian activos, amenazas o controles.


**Práctica y evidencia:** Compara riesgos con apetito/tolerancia y criterios de aceptación. **Evidencia:** registra decisión y responsable.

#### 21.4.09 — Tratamiento de riesgos
Tratamiento de riesgos selecciona opciones para modificar el riesgo: mitigar, aceptar, transferir o evitar. Documenta decisión, autoridad, coste, riesgo residual y fecha de revisión.


**Práctica y evidencia:** Selecciona tratamiento: mitigar, aceptar, transferir o evitar. **Evidencia:** relaciona tratamiento con costo, residual y dueño del riesgo.

#### 21.4.10 — Mitigación
Mitigación reduce probabilidad o impacto mediante controles. Prioriza medidas proporcionales y medibles, define responsable y comprueba eficacia después de implantarlas.


**Práctica y evidencia:** Diseña mitigación con acción, responsable, plazo y métrica. **Evidencia:** define cómo verificar reducción del riesgo.

#### 21.4.11 — Aceptación
Aceptación reconoce formalmente un riesgo residual dentro de la autoridad y tolerancia establecidas. Registra justificación, propietario, vencimiento y condiciones que obligan a reconsiderar la decisión.


**Práctica y evidencia:** Documenta aceptación formal de un riesgo residual con vigencia y revisión. **Evidencia:** identifica quién tiene autoridad para aceptar.

#### 21.4.12 — Transferencia
Transferencia comparte parte de consecuencias o responsabilidades mediante seguros, contratos o proveedores. No elimina el riesgo ni la responsabilidad de supervisión; evalúa exclusiones y dependencias de terceros.


**Práctica y evidencia:** Evalúa transferencia mediante seguro o contrato y aclara que no elimina responsabilidad operativa. **Evidencia:** identifica riesgo que permanece.

#### 21.4.13 — Evitación
Evitación elimina la actividad o condición que origina el riesgo. Comprueba efectos sobre objetivos y alternativas y documenta por qué el beneficio de no continuar supera el coste.


**Práctica y evidencia:** Evalúa evitar una actividad o activo que genera riesgo inaceptable. **Evidencia:** documenta impacto de negocio y alternativa.

### Módulo 21.5 — Ciberamenazas

#### 21.5.01 — Malware
Malware es software diseñado para realizar acciones no autorizadas o dañinas, como robo, sabotaje o control remoto. Estudia familias y señales desde defensa y analiza muestras solo en laboratorios aislados.


**Práctica y evidencia:** Clasifica muestras y alertas de malware mediante fuentes confiables y análisis no ejecutable. **Evidencia:** registra indicadores y medidas de contención.

#### 21.5.02 — Ransomware
Ransomware bloquea o cifra datos y suele combinarse con extorsión y robo de información. Previene con backups desconectados/protegidos, segmentación, MFA y respuesta ensayada; no asumas que pagar recupera los datos.


**Práctica y evidencia:** Analiza un escenario ransomware desde respaldo, segmentación y recuperación. **Evidencia:** diseña tabletop sin crear ni ejecutar malware.

#### 21.5.03 — Spyware
Spyware recopila información o actividad sin autorización y puede operar de forma persistente. Busca indicadores en endpoints y tráfico, limita privilegios y protege credenciales y datos.


**Práctica y evidencia:** Identifica indicadores de spyware en un caso documental y controles de privacidad. **Evidencia:** diferencia recolección autorizada de vigilancia no consentida.

#### 21.5.04 — Trojan
Trojan se presenta como software legítimo o útil mientras realiza acciones ocultas. Verifica origen, firma y comportamiento de instaladores y evita ejecutar archivos desconocidos fuera de sandbox.


**Práctica y evidencia:** Compara troyano con virus y gusano mediante ciclo de infección y dependencia de usuario. **Evidencia:** describe controles de prevención y respuesta.

#### 21.5.05 — Worms
Worms se propagan entre sistemas aprovechando conectividad o vulnerabilidades con poca intervención del usuario. Segmenta redes, aplica parches y detecta patrones de propagación.


**Práctica y evidencia:** Analiza propagación de gusanos en un diagrama aislado y propone segmentación/parcheo. **Evidencia:** identifica señales de movimiento automatizado.

#### 21.5.06 — Phishing
Phishing engaña a personas para obtener credenciales, datos o ejecutar acciones. Combina formación con MFA resistente al phishing, filtros, reporte sencillo y procesos de verificación fuera del canal sospechoso.


**Práctica y evidencia:** Examina un correo simulado de phishing y detecta remitente, dominio, urgencia y enlaces sospechosos. **Evidencia:** registra indicadores sin abrir enlaces.

#### 21.5.07 — Spear Phishing
Spear Phishing personaliza el engaño para una persona o grupo usando contexto y relaciones reales. Verifica solicitudes sensibles por un canal independiente y limita información pública que facilite suplantación.


**Práctica y evidencia:** Compara phishing masivo con spear phishing y define controles para ataques dirigidos. **Evidencia:** construye un caso de concienciación sin recolectar credenciales.

#### 21.5.08 — Credential Theft
Credential Theft obtiene contraseñas, tokens o claves mediante engaño, malware, filtración o reutilización. Usa gestores de contraseñas, MFA, rotación/revocación y detección de accesos anómalos.


**Práctica y evidencia:** Diseña respuesta ante posible robo de credenciales: revocación, rotación, MFA y revisión de sesiones. **Evidencia:** ordena acciones por urgencia.

#### 21.5.09 — Social Engineering
Social Engineering manipula comportamientos mediante autoridad, urgencia, confianza o presión. Establece procesos de verificación, doble aprobación y canales de reporte sin culpabilizar a quien recibe el engaño.


**Práctica y evidencia:** Mapea técnicas de ingeniería social y señales de manipulación en un caso de mesa. **Evidencia:** propone verificación fuera de banda y reporte.

#### 21.5.10 — Insider Threats
Insider Threats son riesgos derivados de personas con acceso legítimo, intencionalmente o por error. Aplica mínimo privilegio, segregación de funciones, monitoreo proporcional y procesos de salida/cambio de rol.


**Práctica y evidencia:** Analiza riesgo interno accidental y malicioso con controles proporcionales y protección de privacidad. **Evidencia:** diferencia monitoreo legítimo de vigilancia excesiva.

#### 21.5.11 — Supply Chain Attacks
Supply Chain Attacks comprometen un proveedor, dependencia o proceso de distribución para alcanzar objetivos posteriores. Inventaría terceros, verifica integridad, limita permisos y establece requisitos de seguridad y respuesta contractual.


**Práctica y evidencia:** Evalúa dependencias de proveedor, build y actualización en una cadena de suministro. **Evidencia:** propone SBOM, firma, procedencia y revisión de cambios.

#### 21.5.12 — Denial of Service
Denial of Service busca degradar o interrumpir un servicio mediante agotamiento de recursos o fallos inducidos. Diseña límites, redundancia y filtrado y coordina mitigación con proveedores.


**Práctica y evidencia:** Explica DoS y sus efectos sobre recursos de un servicio. **Evidencia:** define controles de resiliencia y respuesta sin generar tráfico disruptivo.

#### 21.5.13 — Distributed Denial of Service
Distributed Denial of Service utiliza múltiples fuentes para amplificar o distribuir el tráfico dañino. Apóyate en mitigación upstream, CDN/proveedor y planes de continuidad; no intentes responder con acciones de represalia.


**Práctica y evidencia:** Compara DDoS volumétrico, de protocolo y de aplicación en un escenario teórico. **Evidencia:** relaciona mitigación con proveedor, CDN, rate limiting y continuidad.

### Módulo 21.6 — Marcos y estándares

#### 21.6.01 — NIST Cybersecurity Framework 2.0
NIST Cybersecurity Framework 2.0 organiza resultados de ciberseguridad mediante las funciones Govern, Identify, Protect, Detect, Respond y Recover. Úsalo para perfilar estado actual/objetivo y priorizar resultados según riesgo y contexto organizacional.


**Práctica y evidencia:** Mapea un programa de seguridad a las funciones Govern, Identify, Protect, Detect, Respond y Recover de CSF 2.0. **Evidencia:** documenta resultados y perfiles objetivo.

#### 21.6.02 — ISO/IEC 27001:2022
ISO/IEC 27001:2022 especifica requisitos para establecer, mantener y mejorar un sistema de gestión de seguridad de la información. Define alcance, evaluación/tratamiento de riesgos y evidencia; no equivale a una certificación automática por usar controles.


**Práctica y evidencia:** Revisa el alcance de un SGSI y relaciona riesgos, controles y mejora continua con ISO/IEC 27001:2022. **Evidencia:** distingue requisitos certificables de recomendaciones.

#### 21.6.03 — ISO/IEC 27002:2022
ISO/IEC 27002:2022 proporciona orientación sobre controles de seguridad de la información. Selecciona controles según riesgo y contexto y relaciona su aplicación con políticas, responsables y evidencia.


**Práctica y evidencia:** Selecciona controles de referencia de ISO/IEC 27002:2022 para un riesgo específico. **Evidencia:** justifica aplicabilidad y evidencia de implementación.

#### 21.6.04 — ISO/IEC 27005
ISO/IEC 27005 ofrece orientación para gestionar riesgos de seguridad de la información. Integra contexto, identificación, análisis, evaluación, tratamiento y seguimiento con el sistema de gestión.


**Práctica y evidencia:** Aplica un proceso de evaluación y tratamiento de riesgos alineado con ISO/IEC 27005. **Evidencia:** documenta contexto, criterios y tratamiento.

#### 21.6.05 — CIS Controls
CIS Controls reúne salvaguardas priorizadas para reducir riesgos comunes de ciberseguridad. Adapta implementación a activos y capacidad, mide cobertura y no asumas que una lista de controles reemplaza análisis de riesgos.


**Práctica y evidencia:** Selecciona salvaguardas CIS Controls según tamaño y exposición de una organización. **Evidencia:** prioriza implementación y mide cobertura.

#### 21.6.06 — MITRE ATT&CK
MITRE ATT&CK organiza tácticas y técnicas observadas de adversarios para apoyar detección, análisis y emulación autorizada. Usa versión y plataforma identificadas y evita interpretar una técnica mapeada como prueba de que ocurrió un ataque.


**Práctica y evidencia:** Relaciona un comportamiento defensivo observado con tácticas/técnicas MITRE ATT&CK. **Evidencia:** cita técnica y fuente, distinguiendo comportamiento de atribución.

#### 21.6.07 — Principios Zero Trust
Zero Trust parte de no conceder confianza implícita por ubicación de red y requiere verificación explícita y continua según contexto. Aplica identidad, dispositivo, recurso y política; no es un producto único ni una migración instantánea.


**Práctica y evidencia:** Diseña un flujo Zero Trust con verificación explícita, mínimo privilegio y evaluación continua. **Evidencia:** identifica sujeto, dispositivo, recurso y contexto.

#### 21.6.08 — Information security management systems
Un Information Security Management System (ISMS/SGSI) coordina políticas, procesos, evaluación de riesgos, controles, auditoría y mejora continua. Define alcance y liderazgo, conserva evidencia y revisa eficacia en ciclos regulares.


**Práctica y evidencia:** Define alcance, liderazgo, evaluación, tratamiento, auditoría y mejora de un SGSI. **Evidencia:** presenta ciclo de gobierno y responsables.

### Módulo 21.7 — Ética y legislación

#### 21.7.01 — Hacking ético
Hacking ético evalúa controles de forma autorizada y con objetivos defensivos definidos. Exige permiso previo, alcance, reglas de operación, protección de datos y reporte responsable; la intención declarada no sustituye autorización.


**Práctica y evidencia:** Redacta un plan de hacking ético para un laboratorio propio con objetivos defensivos. **Evidencia:** incluye autorización, límites, horario y manejo de hallazgos.

#### 21.7.02 — Diferencia entre White Hat, Gray Hat y Black Hat
White Hat actúa con autorización y propósito defensivo; Gray Hat puede investigar sin autorización suficiente; Black Hat opera con intención maliciosa o ilegal. La etiqueta no determina legalidad: el permiso y el alcance documentado son decisivos.


**Práctica y evidencia:** Clasifica conductas White Hat, Gray Hat y Black Hat en casos hipotéticos. **Evidencia:** explica autorización y consecuencias, no solo intención declarada.

#### 21.7.03 — Autorización
Autorización debe ser explícita, otorgada por quien tiene facultad sobre los activos y vigente durante la actividad. Define métodos, horarios, sistemas, datos, terceros y límites de impacto.


**Práctica y evidencia:** Prepara autorización escrita que identifique propietario, sistemas, técnicas permitidas y fechas. **Evidencia:** demuestra que el permiso precede a cualquier prueba.

#### 21.7.04 — Alcance
Alcance enumera sistemas, direcciones, aplicaciones, cuentas, técnicas permitidas y exclusiones. Mantén una lista inequívoca y detén la actividad si aparece un activo no incluido.


**Práctica y evidencia:** Define alcance con IPs, dominios, aplicaciones, exclusiones y límites de impacto. **Evidencia:** produce lista verificable de activos autorizados.

#### 21.7.05 — Rules of Engagement
Rules of Engagement documentan objetivos, ventanas, contactos, restricciones, tratamiento de hallazgos y condiciones de detención. Deben aprobarse antes de cualquier prueba y estar disponibles para todo el equipo.


**Práctica y evidencia:** Redacta Rules of Engagement con ventanas, contactos, límites y condiciones de parada. **Evidencia:** define procedimiento ante impacto inesperado.

#### 21.7.06 — Confidencialidad
Confidencialidad obliga a proteger información obtenida durante auditorías, incidentes y proyectos. Minimiza copias, limita acceso, cifra evidencias y define retención y destrucción.


**Práctica y evidencia:** Establece obligaciones de confidencialidad y clasificación para datos observados. **Evidencia:** documenta almacenamiento, acceso y eliminación segura.

#### 21.7.07 — Divulgación responsable
Divulgación responsable coordina la comunicación de vulnerabilidades con el propietario y, cuando proceda, un programa de divulgación. Evita publicar datos explotables antes de mitigación y sigue plazos y políticas acordadas.


**Práctica y evidencia:** Diseña divulgación responsable con canal, tiempos, coordinación y no publicación prematura. **Evidencia:** redacta una notificación técnica responsable.

#### 21.7.08 — Protección de datos
Protección de datos exige tratar información personal con finalidad, proporcionalidad, seguridad y derechos aplicables. Minimiza recolección, restringe acceso y consulta normativa vigente y responsables de privacidad antes de procesar datos reales.


**Práctica y evidencia:** Minimiza datos personales en pruebas y aplica finalidad, necesidad y retención limitada. **Evidencia:** identifica base y controles que deben revisarse con asesoría jurídica.

#### 21.7.09 — Gestión de evidencias
Gestión de evidencias preserva integridad, procedencia, contexto y acceso a artefactos de una investigación. Registra quién recolectó, cuándo, cómo, hashes y transferencias; trabaja sobre copias y conserva originales protegidos.


**Práctica y evidencia:** Preserva evidencia con hash, fecha, origen, custodio y registro de transferencias. **Evidencia:** crea una cadena de custodia para un archivo sintético.

#### 21.7.10 — Responsabilidad profesional
Responsabilidad profesional implica competencia, honestidad, confidencialidad y comunicación clara de límites y riesgos. No exageres resultados, informa conflictos de interés y detén actividades que excedan el mandato.


**Práctica y evidencia:** Redacta un informe profesional con alcance, método, hallazgos, impacto, evidencia y remediación. **Evidencia:** separa hechos, inferencias y limitaciones.

#### 21.7.11 — Consideraciones legales colombianas
Las consideraciones legales colombianas requieren revisar legislación vigente sobre delitos informáticos, protección de datos, telecomunicaciones, evidencia y obligaciones sectoriales. Documenta jurisdicción y fecha, consulta fuentes oficiales y asesoría competente; este temario no sustituye concepto jurídico.


**Práctica y evidencia:** Consulta fuentes oficiales colombianas vigentes para Ley 1273 de 2009 y Ley 1581 de 2012 y delimita su alcance. **Evidencia:** registra artículos, fuente oficial y fecha; no emite asesoría jurídica.

### Módulo 21.8 — Gestión de identidades (IAM)

#### 21.8.01 — Identity and Access Management
Identity and Access Management administra el ciclo de vida de identidades, autenticación, autorización y auditoría. Integra altas, cambios y bajas con sistemas y procesos de negocio y revisa accesos periódicamente.


**Práctica y evidencia:** Dibuja ciclo de vida de identidad: alta, cambio, revisión periódica y baja. **Evidencia:** identifica dueño, aprobaciones y trazabilidad.

#### 21.8.02 — Usuarios
Usuarios representan identidades humanas o técnicas con atributos y credenciales. Evita cuentas compartidas, verifica identidad durante el alta y deshabilita accesos cuando termina la necesidad.


**Práctica y evidencia:** Define ciclo de vida de cuentas humanas y de servicio con verificación de identidad. **Evidencia:** establece baja oportuna y revisión de cuentas huérfanas.

#### 21.8.03 — Roles
Roles agrupan responsabilidades y permisos para simplificar asignación de acceso. Mantén catálogo revisado, evita acumulación de roles y vincula cambios de puesto con recertificación.


**Práctica y evidencia:** Asigna roles por función laboral y revisa acumulación de privilegios. **Evidencia:** construye matriz de incompatibilidad de funciones.

#### 21.8.04 — Permisos
Permisos definen acciones concretas sobre recursos. Asigna permisos explícitos, aplica mínimo privilegio y prueba accesos denegados además de los permitidos.


**Práctica y evidencia:** Mapea permisos por recurso y operación y aplica denegación por defecto. **Evidencia:** prueba acceso permitido y denegado.

#### 21.8.05 — Privilegios
Privilegios permiten acciones administrativas o sensibles sobre sistemas y datos. Separa cuentas ordinarias y administrativas, eleva temporalmente y registra actividades de alto impacto.


**Práctica y evidencia:** Inventaría privilegios administrativos y reduce cuentas permanentes mediante elevación temporal cuando sea viable. **Evidencia:** registra aprobación y auditoría.

#### 21.8.06 — MFA
MFA requiere más de un factor independiente para autenticar. Prioriza métodos resistentes al phishing y protege el proceso de recuperación para que no se convierta en el eslabón débil.


**Práctica y evidencia:** Configura MFA con factor resistente al phishing cuando esté disponible y plan de recuperación. **Evidencia:** prueba enrolamiento y revocación.

#### 21.8.07 — RBAC
RBAC vincula usuarios y grupos a roles con permisos predefinidos. Define jerarquías con cautela y revisa conflictos de segregación de funciones.


**Práctica y evidencia:** Implementa RBAC con roles, permisos y herencia controlada. **Evidencia:** prueba matriz de acceso y separación de funciones.

#### 21.8.08 — ABAC
ABAC evalúa atributos de identidad, recurso, acción y contexto para tomar decisiones de acceso. Mantén atributos confiables, políticas auditables y reglas de denegación claras.


**Práctica y evidencia:** Define políticas ABAC con atributos de usuario, recurso y contexto confiables. **Evidencia:** prueba condiciones límite y evita confiar en atributos enviados por el cliente.

#### 21.8.09 — Least Privilege
Least Privilege limita cada identidad a permisos mínimos y temporales. Revisa accesos reales y elimina privilegios heredados que ya no responden a la función.


**Práctica y evidencia:** Revisa permisos excesivos y reduce cada identidad al mínimo necesario. **Evidencia:** demuestra operación funcional con permisos reducidos.

#### 21.8.10 — Identity Federation
Identity Federation permite que una organización confíe en un proveedor de identidad externo mediante protocolos y relaciones configuradas. Valida issuer, audience, certificados y atributos y define revocación y gestión de confianza.


**Práctica y evidencia:** Modela federación de identidad con proveedor de identidad, relying party y claims. **Evidencia:** explica confianza, issuer y validación de audiencia.

#### 21.8.11 — Service Accounts
Service Accounts son identidades no humanas usadas por aplicaciones y automatizaciones. Asigna credenciales de corta duración cuando sea posible, limita permisos, rota secretos y monitorea su uso.



**Práctica y evidencia:** Define cuentas de servicio con propietario, alcance, rotación y monitoreo. **Evidencia:** demuestra que no se usa una cuenta humana compartida ni credencial incrustada.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 82 orientaciones genéricas por explicaciones específicas de fundamentos, principios, conceptos de riesgo, metodología, amenazas, marcos, ética/legislación e IAM.

**Revisión interna:** 82/82 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron autorización, límites de alcance, preservación de evidencia, protección de datos, responsabilidad profesional y controles de identidades técnicas. Las consideraciones legales colombianas se mantienen como materia de verificación normativa vigente y no como asesoría jurídica. Pendiente: cotejar referencias oficiales y legislación aplicable, realizar ejercicios de evaluación de riesgos con escenarios ficticios y obtener segunda revisión especializada. No se ejecutaron operaciones de seguridad ni se declara aprobación externa.


### Referencias normativas y marcos oficiales para la revisión colombiana

- NIST, **Cybersecurity Framework (CSF) 2.0**: https://www.nist.gov/cyberframework
- Colombia, **Ley 1273 de 2009** — protección de la información y los datos / delitos informáticos (texto en Gestor Normativo de Función Pública): https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=34492
- Colombia, **Ley 1581 de 2012** — régimen general de protección de datos personales (texto en Gestor Normativo de Función Pública): https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981

**Precaución jurídica:** estas referencias sirven como punto de partida documental. Antes de impartir o aplicar el contenido, verificar vigencia, reglamentación, modificaciones, jurisprudencia y normas sectoriales en fuentes oficiales. El material no constituye asesoría legal.
