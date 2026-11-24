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
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.02 — Domain Controller
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.03 — Forest
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.04 — Tree
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.05 — Organizational Units
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.06 — Users
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.07 — Groups
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.08 — Computers
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.1.09 — Group Policy Objects
Comprender el concepto, los datos o controles involucrados y su papel dentro de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 26.2 — Protocolos

#### 26.2.01 — LDAP
Comprender el concepto, los datos o controles involucrados y su papel dentro de protocolos; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.2.02 — Kerberos
Comprender el concepto, los datos o controles involucrados y su papel dentro de protocolos; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.2.03 — NTLM
Comprender el concepto, los datos o controles involucrados y su papel dentro de protocolos; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.2.04 — SMB
Comprender el concepto, los datos o controles involucrados y su papel dentro de protocolos; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.2.05 — DNS
Comprender el concepto, los datos o controles involucrados y su papel dentro de protocolos; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 26.3 — Administración

#### 26.3.01 — Usuarios
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.02 — Grupos
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.03 — Permisos
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.04 — Políticas
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.05 — Autenticación
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.06 — Autorización
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.3.07 — Gestión de identidades
Comprender el concepto, los datos o controles involucrados y su papel dentro de administración; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 26.4 — Seguridad de Active Directory

#### 26.4.01 — Misconfigurations
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.02 — Privileged Accounts
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.03 — Excessive Permissions
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.04 — Kerberos Security
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.05 — NTLM Risks
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.06 — Lateral Movement Concepts
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.07 — Privilege Escalation Paths
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.4.08 — Credential Security
Comprender el concepto, los datos o controles involucrados y su papel dentro de seguridad de active directory; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 26.5 — Herramientas

#### 26.5.01 — BloodHound
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.5.02 — SharpHound
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.5.03 — PowerShell
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.5.04 — Windows Event Viewer
Comprender el concepto, los datos o controles involucrados y su papel dentro de herramientas; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

### Módulo 26.6 — Hardening

#### 26.6.01 — Least Privilege
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.6.02 — Privileged Access
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.6.03 — Credential Protection
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.6.04 — Group Policy Security
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.6.05 — Auditing
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.

#### 26.6.06 — Logging
Comprender el concepto, los datos o controles involucrados y su papel dentro de hardening; relacionarlo con prevención, detección, respuesta o documentación, según corresponda.
