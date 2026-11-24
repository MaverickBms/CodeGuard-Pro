# Etapa 26 — Active Directory y seguridad empresarial Windows

**Prioridad:** P2 · Especialización  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** comprender cómo funcionan los entornos corporativos Windows y cómo protegerlos.  
**Proyecto oficial:** crear un pequeño dominio de Active Directory en laboratorio, configurar usuarios y políticas y elaborar una evaluación de seguridad.

## Alcance del laboratorio
Utiliza un dominio ficticio en máquinas virtuales propias, aisladas y con snapshots. No conectes un Domain Controller de práctica a una red corporativa real. Usa cuentas y contraseñas sintéticas. Las técnicas de enumeración deben centrarse en auditoría defensiva del entorno propio; no se realizarán movimientos laterales ni escaladas fuera del laboratorio autorizado.

## Resultados de aprendizaje
Explicar la estructura de Active Directory; reconocer protocolos de identidad; administrar usuarios, grupos y políticas; identificar configuraciones de riesgo; interpretar herramientas de análisis de relaciones; y aplicar hardening, auditoría y protección de credenciales.

## 26.1 — Active Directory
Active Directory Domain Services organiza identidades y recursos en dominios. Domain Controller aloja servicios de directorio y autenticación. Forest contiene uno o más dominios y define un límite administrativo/lógico importante; Tree agrupa dominios relacionados por espacio de nombres. Organizational Units (OU) organizan objetos y permiten delegación y aplicación de GPO.

Usuarios, grupos y equipos son objetos del directorio. Group Policy Objects aplican configuraciones a usuarios/equipos según vínculo, herencia y filtrado. Comprende sitios, replicación, DNS integrado y catálogo global como conceptos operativos complementarios.

**Ejercicio:** dibuja un forest de laboratorio con dominio, OU, grupos, usuarios y equipos; explica herencia de políticas.

## 26.2 — Protocolos
LDAP permite consultar y modificar directorios mediante operaciones definidas; protege credenciales con configuración segura como LDAPS o mecanismos SASL apropiados. Kerberos usa tickets y un KDC para autenticación en entornos de dominio. NTLM es un protocolo heredado que debe evaluarse y restringirse según compatibilidad y política. SMB permite compartir archivos/impresoras; DNS es esencial para localización de servicios de dominio.

No confundas protocolo de autenticación con autorización. Comprende resolución de nombres, tickets, cuentas de servicio, sincronización horaria y protección de canal.

## 26.3 — Administración
Gestiona usuarios, grupos, permisos, políticas, autenticación y autorización mediante roles administrativos definidos. Aplica mínimo privilegio, separación de cuentas administrativas, proceso de alta/cambio/baja y revisión periódica. Evita cuentas compartidas y privilegios permanentes innecesarios.

**Ejercicio:** crea OU por área ficticia, grupos de seguridad y usuarios de prueba. Documenta qué recurso puede utilizar cada grupo y valida con cuentas separadas.

## 26.4 — Seguridad de Active Directory
Revisa misconfigurations, cuentas privilegiadas, permisos excesivos, seguridad Kerberos, riesgos NTLM, rutas de privilegio, exposición de credenciales y conceptos de movimiento lateral. El análisis debe identificar condiciones de riesgo y corregirlas; no requiere explotar credenciales ni ejecutar acciones destructivas.

Protege cuentas de alto privilegio, separa administración, restringe delegación, aplica políticas de autenticación, supervisa cambios de grupos y revisa cuentas de servicio. La protección de credenciales incluye evitar almacenamiento en texto claro, limitar exposición en endpoints y aplicar controles soportados por la versión.

## 26.5 — Herramientas
BloodHound representa relaciones y rutas potenciales de privilegio; SharpHound recopila datos para análisis en el entorno autorizado. PowerShell permite administrar y consultar Windows; Event Viewer ayuda a revisar eventos. Revisa permisos de recopilación, privacidad, versión y almacenamiento de resultados. Los grafos muestran relaciones potenciales: valida contexto antes de concluir que una ruta es explotable.

**Ejercicio:** importa datos sintéticos o recopilados de tu dominio de laboratorio y genera un informe de relaciones y permisos excesivos. No recolectes datos de dominios ajenos.

## 26.6 — Hardening
Aplica least privilege, administración privilegiada controlada, protección de credenciales, políticas seguras y auditoría. Habilita registros pertinentes, protege respaldos del directorio y prueba restauración en entorno aislado. Supervisa altas de privilegios, cambios de GPO, inicios de sesión anómalos y cuentas inactivas.

**Ejercicio:** define una línea base segura, aplica cambios en una OU de prueba, valida impacto y registra cómo revertir.

## Proyecto oficial — Dominio AD de laboratorio
### Requisitos
1. Topología y aislamiento de red documentados.
2. Domain Controller y cliente de prueba.
3. Dominio y OU con estructura justificada.
4. Usuarios y grupos sintéticos.
5. GPO para configuraciones de seguridad.
6. DNS y protocolo de autenticación documentados.
7. Matriz de permisos y cuentas privilegiadas.
8. Revisión de riesgos Kerberos/NTLM.
9. Auditoría de eventos y cambios.
10. Análisis de relaciones con herramienta autorizada.
11. Hardening y pruebas de regresión.
12. Backup, restauración y cierre seguro del laboratorio.

### Entregables
Diagrama, inventario, configuración, GPO, matriz de acceso, informe de riesgos, evidencia de auditoría, medidas de hardening y guía de restauración.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Arquitectura de AD | 15 |
| Protocolos e identidad | 15 |
| Administración y GPO | 20 |
| Análisis de seguridad | 20 |
| Herramientas y evidencias | 10 |
| Hardening y auditoría | 15 |
| Documentación y restauración | 5 |

Criterio orientativo: 80/100 y laboratorio aislado sin credenciales reales.

## Autoevaluación
1. Diferencia Domain, Tree y Forest.
2. ¿Qué función cumple un Domain Controller?
3. ¿Por qué DNS es crítico para AD?
4. Diferencia LDAP y Kerberos.
5. ¿Qué riesgos tiene NTLM?
6. ¿Qué función cumplen OU y GPO?
7. ¿Por qué separar cuentas administrativas?
8. ¿Qué significa una ruta de privilegio potencial?
9. ¿Qué datos deben protegerse en un informe BloodHound?
10. ¿Qué eventos conviene auditar?

## Recursos audiovisuales
No se incluyen videos aprobados. Solo se incorporarán recursos hablados en español y directamente relacionados con AD DS, GPO, Kerberos, hardening Windows o auditoría defensiva.

## Referencias oficiales
- Microsoft Learn — Active Directory Domain Services: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/
- Microsoft Learn — Group Policy: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/group-policy
- Microsoft Security: https://learn.microsoft.com/en-us/windows/security/
- Microsoft PowerShell: https://learn.microsoft.com/en-us/powershell/
- LDAP, RFC 4511: https://www.rfc-editor.org/rfc/rfc4511
- Kerberos, RFC 4120: https://www.rfc-editor.org/rfc/rfc4120
- BloodHound Documentation: https://bloodhound.specterops.io/
- Sysinternals: https://learn.microsoft.com/en-us/sysinternals/

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se creó un dominio ni se ejecutaron herramientas en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 26

Este desglose conserva los títulos y el orden del roadmap maestro. Las guías de estudio se orientan a administración defensiva, monitoreo y análisis autorizado; no constituyen evidencia de operación en un entorno empresarial.

### Módulo 26.1 — Active Directory

#### 26.1.01 — Domain
Domain es una unidad lógica y administrativa de Active Directory que agrupa objetos y políticas bajo una base común de identidad. Comprende límites de autenticación, replicación y administración y documenta relaciones de confianza.


**Práctica y evidencia:** Diseña un dominio de laboratorio y define su namespace DNS. **Evidencia:** documenta límites y relación con el bosque.

#### 26.1.02 — Domain Controller
Domain Controller autentica identidades y mantiene una copia de los datos del directorio para el dominio. Protege su disponibilidad, parcheado, respaldos y acceso administrativo; un controlador comprometido puede afectar gran parte del entorno.


**Práctica y evidencia:** Identifica roles y servicios de un Domain Controller en VM aislada. **Evidencia:** explica autenticación, directorio y DNS sin usar infraestructura real.

#### 26.1.03 — Forest
Forest es el límite superior de seguridad y esquema en Active Directory, compuesto por uno o más dominios. Evalúa relaciones de confianza y administración forestal antes de delegar privilegios.


**Práctica y evidencia:** Dibuja un forest con dominios de prueba y relaciones de confianza. **Evidencia:** identifica límite administrativo y esquema compartido.

#### 26.1.04 — Tree
Tree agrupa dominios relacionados mediante un espacio de nombres DNS contiguo y relaciones de confianza. Distingue árbol y bosque y verifica estructura real antes de modificar relaciones.


**Práctica y evidencia:** Modela un árbol de dominios y su espacio de nombres contiguo. **Evidencia:** distingue tree de forest.

#### 26.1.05 — Organizational Units
Organizational Units organizan objetos y permiten delegar administración y aplicar GPOs. Diseña OU según responsabilidades y políticas, no solo por organigrama; evita herencia confusa y delegaciones amplias.


**Práctica y evidencia:** Organiza usuarios y equipos en OUs según administración delegada. **Evidencia:** justifica jerarquía sin crear anidamientos innecesarios.

#### 26.1.06 — Users
Users representan identidades humanas o de servicio en el directorio. Define ciclo de vida, atributos, autenticación y revisión de acceso; deshabilita cuentas obsoletas y evita cuentas compartidas.


**Práctica y evidencia:** Crea usuarios de prueba con atributos mínimos y ciclo de vida documentado. **Evidencia:** demuestra alta, cambio y baja.

#### 26.1.07 — Groups
Groups reúnen usuarios y equipos para asignar permisos y políticas. Usa grupos por función, documenta anidamiento y revisa miembros privilegiados regularmente.


**Práctica y evidencia:** Diseña grupos de seguridad por función y aplica estrategia de anidamiento. **Evidencia:** explica alcance y permisos resultantes.

#### 26.1.08 — Computers
Computers son objetos que representan equipos unidos al dominio y su relación de confianza. Controla cuentas de equipo, actualización, ubicación y ciclo de vida; retira objetos obsoletos.


**Práctica y evidencia:** Une una VM Windows al dominio de laboratorio y verifica objeto equipo. **Evidencia:** registra estado y procedimiento de salida.

#### 26.1.09 — Group Policy Objects
Group Policy Objects aplican configuraciones a usuarios y equipos según sitio, dominio y OU. Prueba cambios en una OU piloto, documenta precedencia y evita políticas contradictorias o que bloqueen administración.


**Práctica y evidencia:** Crea una GPO de laboratorio para una configuración no destructiva y aplica a OU específica. **Evidencia:** verifica alcance con gpresult.

### Módulo 26.2 — Protocolos

#### 26.2.01 — LDAP
LDAP es un protocolo para acceder y modificar servicios de directorio. Comprende operaciones, atributos y búsquedas; protege autenticación y transporte y evita exponer consultas o atributos sensibles.


**Práctica y evidencia:** Consulta objetos de directorio mediante LDAP en entorno propio. **Evidencia:** interpreta DN, base de búsqueda y filtros.

#### 26.2.02 — Kerberos
Kerberos autentica mediante tickets y un centro de distribución de claves, reduciendo exposición de contraseñas en cada servicio. Sincroniza tiempo, protege cuentas de servicio y monitorea anomalías de tickets.


**Práctica y evidencia:** Dibuja autenticación Kerberos con AS, TGT y ticket de servicio. **Evidencia:** identifica KDC y dependencia de hora sincronizada.

#### 26.2.03 — NTLM
NTLM es un mecanismo heredado de autenticación desafío-respuesta que puede aumentar riesgos frente a protocolos modernos. Reduce su uso donde sea viable, monitorea dependencias y planifica migración sin romper servicios críticos.


**Práctica y evidencia:** Explica NTLM challenge-response y riesgos de compatibilidad heredada. **Evidencia:** identifica controles para reducir uso sin deshabilitarlo a ciegas.

#### 26.2.04 — SMB
SMB permite compartir archivos, impresoras y otros recursos en redes Windows. Deshabilita versiones inseguras, limita exposición, aplica firma/cifrado cuando proceda y revisa permisos de comparticiones.


**Práctica y evidencia:** Revisa shares SMB de una VM propia y permisos compartidos/NTFS. **Evidencia:** calcula acceso efectivo y desactiva SMB1 solo tras validar compatibilidad.

#### 26.2.05 — DNS
DNS permite localizar servicios y controladores de dominio mediante registros y zonas. Protege actualizaciones dinámicas, delegaciones y resolución; errores DNS pueden interrumpir autenticación y facilitar suplantación.


**Práctica y evidencia:** Verifica registros DNS del dominio de laboratorio y resolución SRV. **Evidencia:** explica cómo clientes localizan servicios del dominio.

### Módulo 26.3 — Administración

#### 26.3.01 — Usuarios
La administración de usuarios controla altas, cambios, bajas, atributos y credenciales. Aplica flujos aprobados, cuentas nominales y desactivación oportuna de accesos.


**Práctica y evidencia:** Crea cuentas estándar y administrativas separadas para una VM de dominio. **Evidencia:** demuestra uso de cuenta de menor privilegio para tareas diarias.

#### 26.3.02 — Grupos
La administración de grupos asigna membresías y permisos según funciones. Usa grupos de seguridad y convenciones de nombres, revisa anidamiento y elimina miembros innecesarios.


**Práctica y evidencia:** Asigna grupos según función y revisa membresías anidadas. **Evidencia:** identifica grupos con privilegios excesivos.

#### 26.3.03 — Permisos
Permisos controlan acceso a objetos y recursos mediante ACL y grupos. Evalúa permisos efectivos, herencia y propietarios; evita conceder control total por conveniencia.


**Práctica y evidencia:** Aplica ACL a una carpeta de laboratorio y comprueba herencia. **Evidencia:** documenta permisos efectivos para dos grupos.

#### 26.3.04 — Políticas
Políticas de dominio aplican configuraciones de seguridad y operación de forma centralizada. Mantén línea base, pruebas piloto, control de cambios y excepciones con fecha de revisión.


**Práctica y evidencia:** Configura una política de contraseñas y bloqueo adecuada al laboratorio. **Evidencia:** comprueba aplicación y registra excepciones.

#### 26.3.05 — Autenticación
Autenticación de dominio verifica identidad y relación de confianza del usuario/equipo. Protege controladores, credenciales y sincronización de tiempo y monitorea fallos repetidos.


**Práctica y evidencia:** Valida autenticación de usuario y observa eventos correspondientes. **Evidencia:** diferencia autenticación correcta, fallida y cuenta bloqueada.

#### 26.3.06 — Autorización
Autorización determina qué recursos y acciones puede utilizar una identidad autenticada. Separa autenticación de permisos y valida acceso en el recurso, no solo en el inicio de sesión.


**Práctica y evidencia:** Protege un recurso con autorización por grupos y permisos explícitos. **Evidencia:** demuestra que autenticación no implica acceso automático.

#### 26.3.07 — Gestión de identidades
Gestión de identidades administra ciclo de vida, roles, privilegios, revisiones y trazabilidad de cuentas. Integra procesos de RR. HH. y operación y automatiza bajas con validación.


**Práctica y evidencia:** Documenta ciclo de vida de identidades, cuentas de servicio y cuentas privilegiadas. **Evidencia:** define propietario, revisión y baja.

### Módulo 26.4 — Seguridad de Active Directory

#### 26.4.01 — Misconfigurations
Misconfigurations incluyen delegaciones excesivas, políticas débiles, servicios heredados y configuraciones por defecto. Compara el dominio con una línea base reconocida y documenta desviaciones con impacto.


**Práctica y evidencia:** Audita configuración de dominio con checklist de baseline y hallazgos priorizados. **Evidencia:** registra desviación y control compensatorio.

#### 26.4.02 — Privileged Accounts
Privileged Accounts tienen capacidad elevada sobre dominios, equipos o datos. Separa cuentas administrativas, exige MFA, limita uso y revisa actividades privilegiadas.


**Práctica y evidencia:** Inventaría cuentas privilegiadas y valida necesidad, propietario y uso. **Evidencia:** propone reducción y monitoreo.

#### 26.4.03 — Excessive Permissions
Excessive Permissions conceden más acceso del necesario a usuarios, grupos o servicios. Revisa ACL y membresías, elimina permisos heredados no requeridos y prueba impacto de cambios.


**Práctica y evidencia:** Revisa permisos delegados y grupos con acceso amplio. **Evidencia:** demuestra una ruta de privilegio excesivo en un diagrama, sin explotarla.

#### 26.4.04 — Kerberos Security
Kerberos Security requiere proteger tickets, claves, SPNs y cuentas de servicio. Utiliza contraseñas robustas o gMSA donde aplique, cifrados actuales y monitoreo de anomalías.


**Práctica y evidencia:** Evalúa políticas Kerberos, cuentas de servicio y cifrados admitidos según baseline vigente. **Evidencia:** identifica configuración heredada y plan de corrección.

#### 26.4.05 — NTLM Risks
NTLM Risks incluyen relay, exposición de hashes y dependencia de autenticación heredada según configuración. Inventaría usos, restringe exposición y migra gradualmente a mecanismos modernos.


**Práctica y evidencia:** Identifica dependencia de NTLM y diseña un plan gradual de reducción. **Evidencia:** registra aplicaciones afectadas y telemetría necesaria.

#### 26.4.06 — Lateral Movement Concepts
Lateral Movement Concepts describe cómo un adversario podría desplazarse entre sistemas usando credenciales o relaciones de confianza. En defensa, segmenta administración, limita credenciales reutilizadas y correlaciona accesos anómalos.


**Práctica y evidencia:** Modela movimiento lateral como riesgo entre equipos y cuentas en un grafo. **Evidencia:** identifica segmentación y controles de detección sin ejecutar técnicas.

#### 26.4.07 — Privilege Escalation Paths
Privilege Escalation Paths son cadenas de permisos y configuraciones que podrían permitir elevar privilegios. Analiza rutas con herramientas defensivas, valida hallazgos y prioriza romper los eslabones de mayor impacto.


**Práctica y evidencia:** Construye un grafo de rutas de privilegio a partir de permisos de laboratorio y prioriza corrección. **Evidencia:** documenta rutas como hipótesis de riesgo, no como explotación confirmada.

#### 26.4.08 — Credential Security
Credential Security protege contraseñas, hashes, tickets, claves y tokens del entorno. Usa MFA, cuentas administradas, protección de memoria, rotación y monitoreo; evita compartir credenciales entre servicios.


**Práctica y evidencia:** Aplica protección de credenciales, MFA y separación de cuentas administrativas. **Evidencia:** presenta controles contra exposición y reutilización.

### Módulo 26.5 — Herramientas

#### 26.5.01 — BloodHound
BloodHound modela relaciones y permisos de Active Directory para identificar rutas de exposición y privilegios. Úsalo para auditoría defensiva autorizada, protege el grafo exportado y valida cada ruta con propietarios.


**Práctica y evidencia:** Importa datos sintéticos del dominio de laboratorio a BloodHound y analiza relaciones. **Evidencia:** identifica permisos y rutas de riesgo con alcance documentado.

#### 26.5.02 — SharpHound
SharpHound recopila datos de directorio y relaciones para alimentar análisis de BloodHound. La recopilación puede ser sensible y detectable; limita alcance, protege archivos y no la ejecutes sin aprobación.


**Práctica y evidencia:** Ejecuta recolección SharpHound solo en el dominio propio de laboratorio con permiso explícito. **Evidencia:** registra colección y elimina datos de directorio al finalizar.

#### 26.5.03 — PowerShell
PowerShell administra Windows y Active Directory mediante cmdlets y objetos. Usa módulos oficiales, sesiones auditables y scripts revisados; firma o controla procedencia y evita ejecutar código remoto no verificado.


**Práctica y evidencia:** Utiliza PowerShell para consultar configuración y eventos de AD en modo lectura. **Evidencia:** conserva comandos reproducibles y limita privilegios.

#### 26.5.04 — Windows Event Viewer
Windows Event Viewer permite revisar eventos de sistema, seguridad y directorio. Define filtros, retención y correlación temporal y protege exportaciones que puedan contener identidades o datos internos.


**Práctica y evidencia:** Filtra eventos de Windows relacionados con autenticación y cambios de grupos. **Evidencia:** construye una línea temporal de laboratorio.

### Módulo 26.6 — Hardening

#### 26.6.01 — Least Privilege
Least Privilege limita cada cuenta a permisos mínimos necesarios y durante el tiempo requerido. Revisa roles y accesos periódicamente y separa administración cotidiana de tareas privilegiadas.


**Práctica y evidencia:** Aplica mínimo privilegio a una cuenta de administración y valida tareas requeridas. **Evidencia:** demuestra reducción de permisos sin perder función.

#### 26.6.02 — Privileged Access
Privileged Access aplica controles reforzados a cuentas administrativas, como MFA, estaciones dedicadas, aprobación temporal y auditoría. Define proceso de emergencia y monitorea uso excepcional.


**Práctica y evidencia:** Diseña estaciones de administración privilegiada y acceso temporal cuando sea viable. **Evidencia:** define controles de sesión y auditoría.

#### 26.6.03 — Credential Protection
Credential Protection reduce exposición de secretos mediante protección de credenciales, rotación, MFA y controles de endpoint. Evita almacenar contraseñas en scripts y protege cuentas de servicio.


**Práctica y evidencia:** Revisa exposición de credenciales y habilita protecciones disponibles según versión. **Evidencia:** documenta configuración y limitaciones.

#### 26.6.04 — Group Policy Security
Group Policy Security establece configuraciones seguras para autenticación, auditoría, firewall, servicios y restricciones de usuario. Prueba GPOs en etapas y mide cumplimiento sin aplicar plantillas incompatibles indiscriminadamente.


**Práctica y evidencia:** Aplica GPO para endurecer una configuración y prueba efecto en OU de laboratorio. **Evidencia:** conserva backup y plan de reversión.

#### 26.6.05 — Auditing
Auditing registra y revisa cambios, autenticaciones, privilegios y accesos relevantes. Define eventos, retención y alertas y verifica que la política realmente genere telemetría suficiente.


**Práctica y evidencia:** Define auditoría de cambios en cuentas, grupos, GPO y objetos sensibles. **Evidencia:** identifica eventos y responsables.

#### 26.6.06 — Logging
Logging centraliza eventos de dominio y endpoints para investigación y detección. Sincroniza relojes, protege integridad, limita acceso y evita que logs almacenen contraseñas o tokens.



**Práctica y evidencia:** Centraliza logs de autenticación y cambios de privilegio con retención y acceso controlado. **Evidencia:** demuestra alerta sobre evento simulado sin exponer datos personales.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 39 orientaciones genéricas por explicaciones específicas de Active Directory, protocolos, administración, seguridad, herramientas y hardening.

**Revisión interna:** 39/39 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron privilegios, cuentas de servicio, protección de credenciales, riesgos de NTLM/Kerberos, revisión de GPO y sensibilidad de datos recopilados por herramientas. Pendiente: validar configuración en un dominio ficticio aislado, revisar eventos con versiones soportadas de Windows Server y obtener segunda revisión especializada. No se conectó a un dominio empresarial ni se ejecutaron herramientas; no se declara aprobación externa.
