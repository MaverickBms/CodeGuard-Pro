# Etapa 22 — Laboratorio de ciberseguridad, hardening y administración segura

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** construir un laboratorio donde puedas practicar seguridad de sistemas y redes sin poner en riesgo equipos ajenos.  
**Proyecto oficial:** montar un laboratorio con una máquina de pruebas, una máquina objetivo vulnerable y una máquina de administración; documentar topología, aislamiento y medidas de seguridad.

## Principio de seguridad del laboratorio
Todo ejercicio se realiza en infraestructura propia o expresamente autorizada. El laboratorio debe estar aislado de redes de terceros, utilizar datos ficticios y tener reglas de alcance. No conectes máquinas vulnerables a redes públicas ni expongas servicios inseguros. Conserva snapshots limpios y un procedimiento para destruir/restaurar el entorno.

## Resultados de aprendizaje
Seleccionar un hipervisor; crear máquinas virtuales y redes aisladas; administrar distribuciones Linux y Windows; aplicar hardening básico; configurar segmentación y firewall; revisar servicios, permisos y logs; y documentar un laboratorio reproducible.

## 22.1 — Virtualización
Un hipervisor ejecuta máquinas virtuales y asigna recursos virtualizados. Comprende snapshots, CPU, RAM, almacenamiento, adaptadores y redes. NAT permite conectividad saliente mediada; Host-only crea una red entre host y VMs; las redes internas aíslan máquinas virtuales entre sí según el hipervisor. Verifica la configuración real: el nombre de un modo no garantiza aislamiento absoluto.

Antes de iniciar:
- documenta rangos IP y adaptadores;
- desactiva port forwarding no necesario;
- evita interfaces bridge para objetivos vulnerables;
- limita carpetas compartidas y portapapeles;
- crea snapshots y prueba restauración;
- restringe salida a Internet cuando no sea necesaria.

**Laboratorio:** crea red aislada con máquina atacante/administración, máquina objetivo vulnerable y servidor de apoyo. Comprueba rutas y conectividad permitida/no permitida.

## 22.2 — Distribuciones Linux
Comprende Ubuntu, Debian y Kali Linux como distribuciones con propósitos y políticas distintas. Kali se orienta a pruebas de seguridad y no sustituye una distribución general para todos los servidores. Aprende kernel, paquetes, usuarios, grupos, permisos, servicios, logs y procesos. Instala solo herramientas necesarias desde repositorios confiables y mantén sistema actualizado.

**Práctica:** documenta paquetes instalados, usuarios, servicios activos y archivos de log de una VM propia.

## 22.3 — Seguridad Linux
- SSH hardening: claves, control de acceso, configuración restrictiva y protección de claves privadas.
- Usuarios y grupos: cuentas individuales, cuentas de servicio y bajas oportunas.
- sudo: privilegios mínimos, reglas justificadas y auditoría.
- File permissions: propietario, grupo, bits de modo y ACL cuando aplique.
- Firewall/UFW: política por defecto restrictiva y reglas explícitas.
- Fail2ban: respuesta automatizada a patrones definidos; no sustituye MFA ni políticas de acceso.
- Actualizaciones: parches de seguridad, reinicios controlados y registro.
- Servicios: deshabilita lo que no se requiere y verifica dependencias.
- Logs y auditoría: protege integridad, acceso y retención de registros.

**Práctica:** crea usuario sin privilegios, configura acceso administrativo limitado, aplica firewall y verifica que los servicios esperados siguen disponibles.

## 22.4 — Seguridad Windows
Estudia Microsoft Defender, Windows Firewall, Windows Update, UAC, permisos NTFS, usuarios y grupos, procesos, servicios, registro, Event Viewer y PowerShell. Mantén Defender y actualizaciones activos; utiliza cuentas estándar para trabajo diario; revisa reglas de firewall y privilegios; audita cambios del sistema. No deshabilites controles para facilitar un laboratorio salvo aislamiento, alcance y restauración definidos.

**Práctica:** crea VM Windows, revisa estado de protección, permisos de una carpeta, servicio y evento de seguridad; registra evidencia sanitizada.

## 22.5 — Seguridad de redes
Firewall rules filtran tráfico según origen, destino, protocolo y puerto. ACL controlan acceso. NAT traduce direcciones; VLAN y segmentación separan dominios de red; DMZ aloja servicios expuestos con controles entre zonas. Network Access Control limita conexión según política. Revisa puertos expuestos y servicios innecesarios. La segmentación reduce movimiento lateral, pero debe probarse desde cada zona.

**Práctica:** diseña zonas administración, objetivo y servicios; define matriz de flujos permitidos y valida con herramientas de diagnóstico locales.

## 22.6 — Laboratorios
Kali Linux, Ubuntu Server, Windows y Windows Server pueden formar el entorno. OWASP Juice Shop y DVWA son aplicaciones intencionalmente vulnerables para formación; ejecútalas solo dentro de red aislada y no las publiques. Selecciona máquinas de entrenamiento con licencia y procedencia conocidas. Evita descargar imágenes de fuentes no confiables.

## Proyecto oficial — Laboratorio aislado
### Requisitos
1. Diagrama de topología, adaptadores y rangos IP.
2. Inventario de VMs, recursos y versiones.
3. Reglas de aislamiento y conectividad.
4. Snapshots y procedimiento de restauración.
5. VM de administración y objetivo vulnerable.
6. Hardening básico Linux y Windows.
7. Firewall y segmentación documentados.
8. Evidencia de servicios, usuarios, permisos y logs.
9. Matriz de puertos y flujos autorizados.
10. Lista de riesgos residuales y procedimiento de apagado.

### Entregables
Diagrama, inventario, configuración, reglas de firewall, evidencias sin secretos, guía de reconstrucción, resultados de pruebas de conectividad y plan de restauración.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Topología y aislamiento | 20 |
| Virtualización y snapshots | 15 |
| Administración Linux | 15 |
| Hardening Windows | 15 |
| Segmentación y firewall | 15 |
| Logs, evidencias y auditoría | 10 |
| Reproducibilidad y documentación | 10 |

Aprobación orientativa: 80/100 y ningún servicio vulnerable expuesto a redes ajenas.

## Autoevaluación
1. Diferencia NAT, Host-only y red interna.
2. ¿Por qué no usar bridge para una VM vulnerable?
3. ¿Qué riesgo resuelve un snapshot y cuál no?
4. ¿Por qué Kali no es una distribución universal de servidor?
5. ¿Qué hace sudo y por qué debe limitarse?
6. ¿Qué diferencia hay entre permisos NTFS y UAC?
7. ¿Qué función cumple una DMZ?
8. ¿Por qué una VLAN no es por sí sola una política de seguridad completa?
9. ¿Qué evidencias no deberían publicarse?
10. ¿Cómo demostrarías que el laboratorio quedó aislado?

## Recursos audiovisuales
No se incluyen videos aprobados. Solo se incorporarán videos en español directamente relacionados con VirtualBox/VMware, hardening Linux/Windows, firewall o redes virtuales, después de comprobar audio y contenido.

## Referencias oficiales
- VirtualBox User Manual: https://www.virtualbox.org/manual/
- VMware Documentation: https://docs.vmware.com/
- Ubuntu Server Guide: https://documentation.ubuntu.com/server/
- Debian Documentation: https://www.debian.org/doc/
- Kali Documentation: https://www.kali.org/docs/
- Microsoft Security: https://learn.microsoft.com/en-us/windows/security/
- Microsoft Defender: https://learn.microsoft.com/en-us/defender/
- UFW: https://manpages.ubuntu.com/manpages/
- Fail2ban: https://www.fail2ban.org/
- OWASP Juice Shop: https://owasp.org/www-project-juice-shop/
- DVWA: https://github.com/digininja/DVWA

**Consulta documental:** 2026-11-19. **Verificación práctica:** no se crearon VMs ni se probaron reglas de firewall en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.


## Desglose granular de lecciones oficiales — etapa 22

Este desglose conserva las entradas del roadmap maestro, incluidas las notas explicativas que aparecen dentro de algunas listas curriculares. Los apartados son guías de estudio y no acreditan pruebas, autorización de laboratorio ni ejecución de herramientas.

### Módulo 22.1 — Virtualización

#### 22.1.01 — Hipervisores
Un hipervisor crea y administra máquinas virtuales y asigna recursos físicos a sistemas invitados. Distingue tipo 1 y tipo 2 y mantén el hipervisor actualizado; la virtualización no elimina todos los riesgos entre host y guest.

#### 22.1.02 — Máquinas virtuales
Una máquina virtual ejecuta un sistema operativo invitado con CPU, memoria, disco y dispositivos virtuales. Usa imágenes confiables, recursos limitados y credenciales de laboratorio; no conectes máquinas deliberadamente vulnerables a redes públicas.

#### 22.1.03 — Snapshots
Snapshots registran un estado de VM para volver a un punto anterior, según capacidades del hipervisor. No son copias de seguridad completas; documenta su ciclo de vida y no dependas de snapshots como única protección de datos.

#### 22.1.04 — Redes aisladas
Redes aisladas restringen comunicación de laboratorio para que ejercicios no afecten redes externas. Verifica rutas, interfaces y reglas antes de iniciar y confirma que el segmento no tenga salida no prevista.

#### 22.1.05 — NAT
NAT permite que máquinas virtuales compartan una salida mediante traducción de direcciones del host o hipervisor. Comprende qué conexiones entrantes se permiten y no asumas que NAT equivale a aislamiento total.

#### 22.1.06 — Host-only
Host-only conecta host y máquinas virtuales dentro de una red privada sin exponerlas directamente a la LAN externa. Revisa interfaces y rutas para impedir puentes accidentales.

#### 22.1.07 — Segmentación
Segmentación separa sistemas según función, sensibilidad y nivel de confianza. Define flujos permitidos entre segmentos y verifica que reglas de red hagan cumplir el diseño.

#### 22.1.08 — Laboratorios vulnerables
Laboratorios vulnerables ofrecen aplicaciones o sistemas intencionalmente inseguros para aprender pruebas defensivas. Ejecútalos aislados, con datos ficticios, alcance escrito y sin publicar puertos en redes accesibles desde Internet.

### Módulo 22.2 — Distribuciones Linux

#### 22.2.01 — Ubuntu
Ubuntu es una distribución Linux con ciclos de soporte y paquetes definidos. Selecciona una versión soportada para el laboratorio, aplica actualizaciones y consulta documentación de esa versión.

#### 22.2.02 — Debian
Debian es una distribución comunitaria con ramas y políticas de estabilidad. Identifica versión y repositorios configurados antes de instalar o actualizar software.

#### 22.2.03 — Kali Linux
Kali Linux es una distribución orientada a pruebas de seguridad y análisis, con herramientas especializadas. No es una distribución de uso general obligatorio ni autoriza a probar sistemas ajenos.

#### 22.2.04 — Kali Tools
Kali Tools agrupa herramientas para tareas de seguridad y análisis. Instala solo lo necesario desde repositorios confiables, comprende el propósito y ejecuta cada herramienta dentro del alcance autorizado.

#### 22.2.05 — Gestión de paquetes
La gestión de paquetes instala, actualiza y elimina software junto con sus dependencias. Verifica origen de repositorios, firmas y versiones y evita descargar instaladores de sitios desconocidos.

#### 22.2.06 — Usuarios
Usuarios identifican cuentas que ejecutan procesos y acceden a recursos. Usa cuentas nominales, deshabilita cuentas innecesarias y evita iniciar sesiones de trabajo cotidiano como root.

#### 22.2.07 — Grupos
Grupos facilitan asignar permisos compartidos a conjuntos de usuarios. Mantén membresías mínimas y revisa cambios de grupo, especialmente en grupos con privilegios administrativos.

#### 22.2.08 — Permisos
Permisos Linux controlan lectura, escritura y ejecución para propietario, grupo y otros, con ACL y atributos adicionales. Comprueba contexto de archivo/directorio y evita `chmod 777` como solución universal.

#### 22.2.09 — Servicios
Servicios son procesos administrados por el sistema de inicio, como systemd en muchas distribuciones. Deshabilita solo servicios identificados y necesarios, y conserva un procedimiento de recuperación.

#### 22.2.10 — Logs
Logs registran eventos de sistema, autenticación, servicios y aplicaciones. Protege acceso e integridad, sincroniza reloj y controla retención para preservar utilidad de auditoría.

#### 22.2.11 — Procesos
Procesos son instancias de programas en ejecución con PID, usuario y recursos. Identifica el proceso y su función antes de terminarlo y evita intervenir servicios críticos sin plan.

### Módulo 22.3 — Seguridad Linux

#### 22.3.01 — SSH Hardening
SSH Hardening reduce superficie de acceso remoto mediante autenticación fuerte, restricciones de usuarios, configuración y monitoreo. Prueba cambios en una sesión secundaria antes de cerrar la actual para evitar perder administración.

#### 22.3.02 — Gestión de usuarios
La gestión de usuarios Linux controla altas, bajas, grupos, shells y expiración de cuentas. Aplica proceso formal de provisión y desprovisión y revisa cuentas inactivas.

#### 22.3.03 — Sudo
Sudo permite ejecutar comandos con privilegios delegados según reglas explícitas. Limita comandos y grupos, valida sintaxis de sudoers y evita permisos amplios que equivalgan a root sin justificación.

#### 22.3.04 — File Permissions
File Permissions define acceso sobre archivos y directorios, incluyendo propietario, grupo, ACL y permisos especiales. Evalúa permisos efectivos y herencia y evita cambios recursivos sin conocer el alcance.

#### 22.3.05 — Firewall
Firewall en Linux controla tráfico entrante, saliente y reenviado mediante el framework disponible. Documenta reglas, orden y política por defecto y conserva acceso administrativo durante la aplicación de cambios.

#### 22.3.06 — UFW
UFW ofrece una interfaz simplificada para administrar reglas de firewall en sistemas compatibles. Comprueba estado y reglas efectivas, permite primero el acceso remoto necesario y valida desde una segunda conexión autorizada.

#### 22.3.07 — Fail2ban
Fail2ban analiza registros y aplica bloqueos temporales ante patrones configurados de abuso. Ajusta filtros y umbrales para evitar falsos positivos y no lo uses como sustituto de autenticación fuerte.

#### 22.3.08 — Actualizaciones
Actualizaciones corrigen vulnerabilidades y errores en sistema y aplicaciones. Define ventanas, pruebas, priorización y rollback; aplica parches desde fuentes oficiales y registra excepciones temporales.

#### 22.3.09 — Servicios innecesarios
Los servicios innecesarios aumentan superficie y consumo de recursos. Inventaría listeners y dependencias, deshabilita solo servicios no requeridos y verifica que no rompas funciones legítimas.

#### 22.3.10 — Logs de seguridad
Logs de seguridad registran autenticaciones, privilegios, cambios y eventos relevantes. Protege su integridad, centraliza cuando proceda y redacta secretos y datos personales de los mensajes.

#### 22.3.11 — Auditoría básica
Auditoría básica compara configuración real con una línea base definida y registra desviaciones. Usa listas de comprobación versionadas, evidencia con fecha y responsable y vuelve a medir tras remediar.

### Módulo 22.4 — Seguridad Windows

#### 22.4.01 — Windows Defender
Windows Defender agrupa capacidades de protección integradas, como antivirus y controles de seguridad de endpoint. Verifica estado, actualizaciones y políticas administradas y no desactives protección para ejecutar herramientas desconocidas.

#### 22.4.02 — Windows Firewall
Windows Firewall filtra conexiones según perfiles, aplicaciones, direcciones y puertos. Mantén reglas mínimas, revisa perfiles Domain/Private/Public y prueba conectividad sin abrir rangos innecesarios.

#### 22.4.03 — Windows Update
Windows Update distribuye actualizaciones del sistema y componentes. Define anillos, ventanas y validación, prioriza parches críticos y registra sistemas que no pueden actualizarse.

#### 22.4.04 — UAC
UAC solicita elevación cuando una acción requiere privilegios administrativos. Mantén configuración adecuada y usa cuentas estándar para tareas cotidianas; no desactives UAC para evitar avisos.

#### 22.4.05 — NTFS Permissions
NTFS Permissions utiliza ACL para controlar acceso a archivos y carpetas. Revisa permisos heredados, grupos y acceso efectivo; evita conceder control total a Everyone o cuentas amplias.

#### 22.4.06 — Users and Groups
Users and Groups administran identidades locales o de dominio y sus pertenencias. Usa cuentas individuales, grupos por función y procesos de baja; protege cuentas administrativas separadas.

#### 22.4.07 — Process Security
Process Security examina identidad, privilegios, integridad y comportamiento de procesos. Investiga procesos desconocidos con fuentes confiables y no finalices servicios críticos sin comprender su función.

#### 22.4.08 — Services
Services son componentes ejecutados en segundo plano bajo cuentas y permisos configurados. Limita privilegios, revisa rutas y dependencias y deshabilita únicamente servicios no necesarios.

#### 22.4.09 — Registry
Registry almacena configuración de Windows y aplicaciones mediante claves y valores. Realiza cambios solo con justificación, exporta respaldo cuando proceda y evita importar archivos de registro de origen desconocido.

#### 22.4.10 — Event Viewer
Event Viewer permite consultar registros de sistema, seguridad y aplicaciones. Filtra por periodo, origen e identificador, conserva contexto y protege exportaciones que puedan contener datos sensibles.

#### 22.4.11 — PowerShell
PowerShell automatiza administración mediante comandos, objetos y scripts. Firma o controla procedencia, valida parámetros, aplica mínimo privilegio y evita ejecutar scripts descargados sin inspección.

### Módulo 22.5 — Seguridad de redes

#### 22.5.01 — Firewall Rules
Firewall Rules permiten aceptar o bloquear tráfico según política de red. Documenta origen, destino, servicio, dirección y motivo, aplica denegación por defecto y revisa reglas obsoletas.

#### 22.5.02 — ACL
ACL filtra tráfico o acceso a recursos mediante reglas ordenadas. Comprueba orden de evaluación y política final y prueba tanto el tráfico permitido como el que debe denegarse.

#### 22.5.03 — NAT
NAT traduce direcciones y, en algunos casos, puertos entre redes. Comprende NAT de origen/destino y sus efectos sobre trazabilidad y conectividad; no lo consideres control de seguridad suficiente.

#### 22.5.04 — VLAN
VLAN separa dominios de broadcast en una infraestructura conmutada. Define VLAN de acceso y trunking, limita VLAN nativa y verifica segmentación con reglas de capa 3.

#### 22.5.05 — DMZ
DMZ ubica servicios expuestos en una zona separada de redes internas sensibles. Permite solo flujos necesarios y monitorea conexiones entre DMZ, Internet y redes corporativas.

#### 22.5.06 — Network Segmentation
Network Segmentation separa activos por función, sensibilidad y riesgo. Define matriz de flujos y valida controles entre segmentos, incluyendo administración y servicios compartidos.

#### 22.5.07 — Network Access Control
Network Access Control evalúa identidad o postura de dispositivo antes de permitir acceso a red. Define criterios transparentes, excepciones controladas y procedimientos para dispositivos no conformes.

#### 22.5.08 — Exposed Ports
Exposed Ports son puertos accesibles desde una red que pueden revelar servicios. Inventaría listeners, justifica cada exposición y limita origen; un puerto abierto no demuestra por sí mismo una vulnerabilidad.

#### 22.5.09 — Unnecessary Services
Unnecessary Services son servicios sin necesidad operativa que incrementan superficie y mantenimiento. Identifica propietario y dependencias antes de retirarlos y verifica que la desactivación no afecte procesos críticos.

#### 22.5.10 — Network Hardening
Network Hardening combina segmentación, reglas mínimas, protocolos seguros, gestión de equipos, monitoreo y actualización. Mantén una línea base y evidencia de pruebas autorizadas de conectividad y denegación.

### Módulo 22.6 — Laboratorios

#### 22.6.01 — Kali Linux
Kali Linux se utiliza en el laboratorio como estación de análisis con herramientas de seguridad. Mantén la VM aislada, actualizada y con snapshots controlados; no conectes adaptadores bridge a redes no autorizadas.

#### 22.6.02 — Ubuntu Server
Ubuntu Server funciona como objetivo de administración y hardening defensivo dentro de una red de práctica. Usa cuentas ficticias, snapshots y servicios mínimos y restaura el entorno al terminar.

#### 22.6.03 — Windows
Windows en laboratorio permite practicar configuración de firewall, cuentas, permisos y eventos en un sistema no productivo. Evita unirlo a dominios reales y no reutilices credenciales corporativas.

#### 22.6.04 — Windows Server
Windows Server permite estudiar roles, políticas y administración de servicios en un dominio ficticio aislado. Documenta DNS, red y cuentas del laboratorio y evita puentes con redes empresariales.

#### 22.6.05 — OWASP Juice Shop
OWASP Juice Shop es una aplicación intencionalmente vulnerable para formación y práctica de seguridad web. Despliega solo en entorno aislado, utiliza datos ficticios y limita el acceso al laboratorio.

#### 22.6.06 — DVWA
DVWA es una aplicación vulnerable diseñada para enseñar conceptos de seguridad web. Mantén sus modos inseguros dentro de una VM/red aislada, registra el alcance y destruye/restaura el entorno al concluir.

#### 22.6.07 — Máquinas de entrenamiento vulnerables
Las máquinas de entrenamiento vulnerables simulan configuraciones o aplicaciones con debilidades deliberadas. Verifica licencia y procedencia, usa snapshots y redes privadas, y no las expongas a Internet ni a redes compartidas.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 58 orientaciones genéricas por explicaciones específicas de virtualización, distribuciones, administración segura de Linux/Windows, hardening de red y laboratorios.

**Revisión interna:** 58/58 entradas desarrolladas y cotejadas con el roadmap. Se reforzaron aislamiento de redes, límites de snapshots, mínimo privilegio, firewall, protección de logs y secretos, y uso de máquinas intencionalmente vulnerables. Todo laboratorio debe permanecer en entornos propios, aislados y autorizados. Pendiente: ejecutar la matriz de hardening en VMs desechables, comprobar reglas y restauración, y obtener revisión especializada. No se ejecutaron herramientas ni se declara aprobación externa.
