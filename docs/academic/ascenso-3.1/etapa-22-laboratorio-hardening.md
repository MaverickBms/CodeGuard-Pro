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
