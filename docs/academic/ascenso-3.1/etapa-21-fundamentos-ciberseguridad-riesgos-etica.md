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
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.02 — Seguridad de la información
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.03 — Ciberseguridad
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.04 — Seguridad de aplicaciones
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.05 — Seguridad de infraestructura
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.06 — Seguridad empresarial
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.07 — Red Team
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.08 — Blue Team
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.1.09 — Purple Team
Estudiar este elemento desde su función y sus límites en introducción a la ciberseguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.2 — Principios fundamentales

#### 21.2.01 — CIA Triad
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.02 — Confidentiality
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.03 — Integrity
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.04 — Availability
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.05 — Authenticity
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.06 — Non-repudiation
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.2.07 — Accountability
Estudiar este elemento desde su función y sus límites en principios fundamentales; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.3 — Conceptos de seguridad

#### 21.3.01 — Assets
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.02 — Threats
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.03 — Vulnerabilities
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.04 — Exploits
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.05 — Attack Vectors
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.06 — Attack Surface
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.07 — Risk
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.08 — Impact
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.09 — Likelihood
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.3.10 — Security Controls
Estudiar este elemento desde su función y sus límites en conceptos de seguridad; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.4 — Gestión de riesgos

#### 21.4.01 — Identificación de activos
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.02 — Clasificación de información
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.03 — Identificación de amenazas
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.04 — Identificación de vulnerabilidades
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.05 — Análisis de probabilidad
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.06 — Análisis de impacto
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.07 — Matriz de riesgos
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.08 — Evaluación de riesgos
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.09 — Tratamiento de riesgos
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.10 — Mitigación
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.11 — Aceptación
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.12 — Transferencia
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.4.13 — Evitación
Estudiar este elemento desde su función y sus límites en gestión de riesgos; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.5 — Ciberamenazas

#### 21.5.01 — Malware
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.02 — Ransomware
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.03 — Spyware
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.04 — Trojan
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.05 — Worms
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.06 — Phishing
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.07 — Spear Phishing
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.08 — Credential Theft
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.09 — Social Engineering
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.10 — Insider Threats
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.11 — Supply Chain Attacks
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.12 — Denial of Service
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.5.13 — Distributed Denial of Service
Estudiar este elemento desde su función y sus límites en ciberamenazas; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.6 — Marcos y estándares

#### 21.6.01 — NIST Cybersecurity Framework 2.0
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.02 — ISO/IEC 27001:2022
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.03 — ISO/IEC 27002:2022
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.04 — ISO/IEC 27005
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.05 — CIS Controls
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.06 — MITRE ATT&CK
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.07 — Principios Zero Trust
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.6.08 — Information security management systems
Estudiar este elemento desde su función y sus límites en marcos y estándares; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.7 — Ética y legislación

#### 21.7.01 — Hacking ético
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.02 — Diferencia entre White Hat, Gray Hat y Black Hat
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.03 — Autorización
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.04 — Alcance
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.05 — Rules of Engagement
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.06 — Confidencialidad
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.07 — Divulgación responsable
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.08 — Protección de datos
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.09 — Gestión de evidencias
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.10 — Responsabilidad profesional
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.7.11 — Consideraciones legales colombianas
Estudiar este elemento desde su función y sus límites en ética y legislación; relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

### Módulo 21.8 — Gestión de identidades (IAM)

#### 21.8.01 — Identity and Access Management
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.02 — Usuarios
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.03 — Roles
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.04 — Permisos
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.05 — Privilegios
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.06 — MFA
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.07 — RBAC
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.08 — ABAC
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.09 — Least Privilege
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.10 — Identity Federation
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.

#### 21.8.11 — Service Accounts
Estudiar este elemento desde su función y sus límites en gestión de identidades (iam); relacionarlo con la reducción de riesgos, la protección de activos y los controles aplicables al escenario autorizado de aprendizaje.
