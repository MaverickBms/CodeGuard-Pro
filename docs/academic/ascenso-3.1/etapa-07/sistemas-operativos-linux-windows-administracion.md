# Etapa 7 — Sistemas operativos: Linux, Windows y administración

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 7.  
**Prioridad oficial:** P1 · Obligatoria.  
**Objetivo oficial:** aprender a administrar computadores y servidores, comprender sus procesos internos y utilizar la terminal.

## Temario oficial

### 7.1. Fundamentos de sistemas operativos
Kernel; User Space; Kernel Space; procesos; hilos; scheduler; context switching; memoria virtual; sistema de archivos; drivers; system calls; IPC (comunicación entre procesos); concurrencia; paralelismo.

### 7.2. Linux
Distribuciones; kernel Linux; Ubuntu; Debian; estructura del sistema de archivos; directorios /etc, /var, /home, /usr, /tmp, /opt; usuarios; grupos; permisos; propietarios; root; sudo; procesos; servicios; paquetes; logs; variables de entorno.

### 7.3. Administración Linux
pwd, ls, cd, mkdir, touch, cp, mv, rm, find, grep, chmod, chown, ps, top, kill, systemctl, journalctl, df, du y mount.

### 7.4. Bash
Variables; operadores; condicionales; bucles; funciones; arrays; pipes; redirecciones; exit codes; scripts; cron; automatización.

### 7.5. Windows
Arquitectura de Windows; sistema de archivos NTFS; usuarios y grupos; permisos; procesos; servicios; Registro de Windows; Administrador de tareas; Visor de eventos; Firewall; PowerShell; administración de servicios.

### 7.6. Virtualización
VirtualBox; VMware; máquinas virtuales; snapshots; recursos virtualizados; redes virtuales; NAT; Host-only; adaptadores de red virtuales.

**Proyecto oficial:** instalar y administrar dos servidores virtuales: Ubuntu Server y Windows Server (introducción). Administrar usuarios, permisos, servicios, procesos y registros.

---

## Resultados de aprendizaje

Al completar esta etapa podrás explicar el rol del kernel; distinguir procesos e hilos; describir planificación, memoria virtual, llamadas al sistema e IPC; administrar Linux desde terminal; interpretar procesos, servicios, paquetes, registros y almacenamiento; escribir scripts Bash; administrar componentes básicos de Windows y utilizar PowerShell; crear máquinas virtuales y configurar redes NAT y Host-only.

## 7.1 — Fundamentos de sistemas operativos

### Función del sistema operativo

Un sistema operativo coordina el hardware y ofrece abstracciones y servicios a los programas. Gestiona CPU, memoria, dispositivos, almacenamiento, usuarios, aislamiento y comunicación entre procesos. No es únicamente una interfaz gráfica: un servidor puede operar sin escritorio y continuar ejecutando servicios y atendiendo solicitudes.

### 7.1.1 — Kernel

El kernel es el núcleo privilegiado del sistema operativo. Coordina recursos, ofrece abstracciones y media el acceso al hardware.

### 7.1.2 — Kernel Space

Kernel Space es el espacio privilegiado donde opera el kernel y ciertos componentes autorizados.

### 7.1.3 — User Space

User Space aloja aplicaciones y servicios con privilegios restringidos. La separación contribuye al aislamiento de fallos.

### 7.1.4 — System Calls

Una llamada al sistema permite que un programa solicite un servicio controlado al kernel. Una función de biblioteca puede preparar argumentos e invocarla, pero ambos conceptos no son idénticos.

### 7.1.10 — Drivers

Los drivers permiten al sistema operativo interactuar con dispositivos. Obténlos de fuentes confiables y compatibles.

### 7.1.5 — Procesos

Un proceso es una instancia de programa en ejecución con recursos y contexto propios.

### 7.1.6 — Hilos

Un hilo es una secuencia de ejecución dentro de un proceso. Los hilos suelen compartir memoria, pero conservan estado y pila propios.

### 7.1.7 — Scheduler

El scheduler decide qué tarea ejecutable recibe tiempo de CPU según la política del sistema.

### 7.1.8 — Context Switching

Un context switch cambia la tarea que ejecuta el procesador y preserva/restaura su estado. Tiene coste y no es trabajo útil de la aplicación.

### 7.1.9 — Memoria virtual

La memoria virtual proporciona a cada proceso una vista lógica de memoria y permite aislar espacios de direcciones. El sistema traduce direcciones virtuales a físicas, administra páginas y puede respaldar parte de la memoria en almacenamiento secundario. Memoria virtual no significa que el disco sea tan rápido como RAM: una paginación intensa puede degradar severamente el rendimiento.

### 7.1.11 — Sistema de archivos

Organiza nombres, directorios, metadatos y contenido persistente. Un dispositivo, un sistema de archivos y un punto de montaje son conceptos distintos.

### 7.1.12 — IPC (comunicación entre procesos)

Los procesos se comunican mediante pipes, sockets, memoria compartida, colas de mensajes y señales. La memoria compartida requiere sincronización correcta.

### 7.1.13 — Concurrencia

La concurrencia organiza tareas que progresan de forma intercalada o solapada. Considera condiciones de carrera, exclusión mutua e interbloqueos.

### 7.1.14 — Paralelismo

El paralelismo implica ejecución simultánea, por ejemplo en varios núcleos. No es sinónimo de concurrencia.

## 7.2 — Linux

### 7.2.1 — Distribuciones

Linux es el kernel; una distribución integra kernel, utilidades, bibliotecas, gestor de paquetes y políticas. Las distribuciones difieren en soporte y versiones.

### 7.2.2 — Kernel Linux

El kernel Linux administra procesos, memoria, dispositivos, redes y llamadas al sistema.

### 7.2.3 — Ubuntu

Ubuntu es una distribución basada en Debian con políticas propias de publicación, soporte y empaquetado.

### 7.2.4 — Debian

Debian es una distribución comunitaria con ramas y políticas propias. Consulta documentación oficial antes de actualizar.

### 7.2.5 — Estructura del sistema de archivos

El árbol parte de la raíz /.

### 7.2.6 — Directorios del sistema de archivos

| Directorio | Uso habitual |
|---|---|
| /etc | configuración del sistema y servicios |
| /var | datos variables, colas y registros |
| /home | directorios personales |
| /usr | programas, bibliotecas y recursos compartidos |
| /tmp | archivos temporales |
| /opt | software adicional |

La distribución concreta puede incorporar enlaces simbólicos o convenciones adicionales. No elimines contenido de estas rutas sin comprender su función.

### 7.2.7 — Usuarios

Una cuenta identifica una entidad que puede iniciar sesión o ejecutar procesos. Aplica mínimo privilegio.

### 7.2.8 — Grupos

Los grupos permiten asignar permisos a conjuntos de usuarios.

### 7.2.10 — Propietarios

Los archivos y directorios tienen propietario y grupo asociados.

### 7.2.11 — Root

Root es la cuenta privilegiada tradicional; evita usarla en tareas rutinarias.

Linux identifica usuarios y grupos mediante IDs. Los permisos controlan acciones para propietario, grupo y otros. Root es la cuenta privilegiada tradicional. Sudo permite ejecutar comandos autorizados con privilegios elevados según la política configurada.

Aplica mínimo privilegio: utiliza una cuenta normal para tareas cotidianas, eleva privilegios solo cuando sea necesario y revisa el comando antes de usar sudo. No compartas contraseñas ni habilites root remoto sin una necesidad y controles claros.

### 7.2.9 — Permisos

Los permisos tradicionales se expresan como lectura (r), escritura (w) y ejecución (x) para propietario, grupo y otros. En directorios, x permite atravesarlo; r permite listar nombres; w permite modificar entradas si se combinan los permisos necesarios.

Ejemplos:
- 640: propietario lectura/escritura, grupo lectura, otros sin permisos.
- 755: propietario lectura/escritura/ejecución, grupo y otros lectura/ejecución.

No utilices permisos 777 como solución general. Conceder escritura a todos aumenta el riesgo.

### 7.2.12 — Sudo

Sudo permite ejecutar comandos autorizados con privilegios elevados. Revisa el comando antes de elevar privilegios.

### 7.2.13 — Procesos

Identifica PID, usuario, consumo y relación padre-hijo antes de intervenir.

### 7.2.14 — Servicios

Los servicios son unidades administradas por el sistema; systemd suele utilizar systemctl.

### 7.2.15 — Paquetes

Los paquetes distribuyen software con metadatos y dependencias. Revisa origen y versión.

### 7.2.16 — Logs

Los logs registran eventos y pueden contener información sensible; controla acceso y redacción.

### 7.2.17 — Variables de entorno

Transmiten configuración a procesos hijos. No incluyas secretos en comandos visibles ni historiales.

## 7.3 — Administración Linux

### 7.3.1 — pwd

Muestra el directorio actual.

### 7.3.2 — ls

Lista contenido, permisos y metadatos.

### 7.3.3 — cd

Cambia el directorio actual de la shell.

### 7.3.4 — mkdir

Crea directorios; evita colisiones con carpetas existentes.

### 7.3.5 — touch

Crea un archivo vacío o actualiza sus marcas de tiempo.

### 7.3.6 — cp

Copia archivos y directorios; verifica destino y sobrescrituras.

### 7.3.7 — mv

Mueve o renombra; comprueba rutas y posibles sobrescrituras.

### 7.3.8 — rm

Elimina entradas. Practica solo con archivos temporales; evita patrones amplios y rm -rf sobre rutas reales.

### 7.3.9 — find

Busca entradas por nombre, tipo, fecha u otros criterios. Empieza con consultas de solo lectura.

### 7.3.10 — grep

Busca patrones en texto. Cita patrones y rutas con espacios o metacaracteres.

### 7.3.11 — chmod

Modifica permisos mediante notación simbólica u octal. Evita permisos excesivos.

### 7.3.12 — chown

Cambia propietario y grupo. Practica solo en archivos de laboratorio y con autorización.

### 7.3.13 — ps

Muestra información de procesos en un instante.

### 7.3.14 — top

Presenta procesos y consumo de recursos dinámicamente.

### 7.3.15 — kill

Envía una señal a un proceso; no garantiza que termine inmediatamente. Usa procesos propios de laboratorio.

### 7.3.16 — systemctl

Consulta y administra unidades de systemd. Comprueba dependencias e impacto antes de cambiar estado.

### 7.3.17 — journalctl

Consulta el journal. Filtra por unidad o periodo y redacta datos sensibles.

### 7.3.18 — df

Informa espacio utilizado y disponible en sistemas de archivos montados.

### 7.3.19 — du

Estima el espacio utilizado por archivos y directorios.

### 7.3.20 — mount

Muestra o administra sistemas de archivos montados. Practica solo con discos virtuales.

### Permisos y propietarios

En un directorio de laboratorio crea un archivo, consulta permisos con ls -l y aplica chmod 640. Interpreta el resultado. En un entorno multiusuario controlado, cambia el propietario con chown solo si tienes autorización y privilegios.

### Procesos y servicios

Antes de detener un proceso o servicio, identifica el PID o unidad, comprueba su función y dependencias, determina el impacto y elige la acción menos disruptiva. Kill envía una señal; no significa necesariamente que el proceso termine inmediatamente.

### Logs y almacenamiento

Journalctl consulta el journal de systemd; df informa espacio de sistemas de archivos; du estima uso de archivos y directorios; mount muestra o administra montajes. Los registros pueden contener rutas, nombres de usuario, direcciones y datos de solicitudes. Comparte extractos redactados, no logs completos indiscriminadamente.

## 7.4 — Bash

### 7.4.1 — Variables

En Bash las variables se asignan sin espacios alrededor del igual. Cita las expansiones para preservar espacios.

### 7.4.2 — Operadores

Bash ofrece operadores de comparación, aritmética y lógica; [[ ]], (( )) y [ ] tienen reglas distintas.

### 7.4.3 — Condicionales

if ejecuta ramas según el estado de una condición. Comprueba códigos de salida.

### 7.4.4 — Bucles

for recorre listas; while repite mientras una condición tenga éxito. Diseña una salida alcanzable.

### 7.4.5 — Funciones

Encapsulan operaciones reutilizables. Define argumentos, variables locales y códigos de retorno.

### 7.4.6 — Arrays

Agrupan valores indexados. Usa "${array[@]}" entre comillas para conservar cada elemento como argumento.

### 7.4.7 — Pipes

Conectan salida estándar de un proceso con la entrada del siguiente.

### 7.4.8 — Redirecciones

Envían salida o errores a archivos y descriptores. > suele sobrescribir; >> añade. Verifica el destino.

### 7.4.9 — Exit codes

Convencionalmente cero indica éxito y otro valor indica error. pipefail permite detectar fallos previos de un pipeline en Bash.

### 7.4.10 — Scripts

Un script robusto valida argumentos, cita variables, comprueba rutas, gestiona errores y termina con un código de salida coherente.

Un script robusto valida argumentos, cita variables, comprueba rutas, gestiona errores, evita exponer secretos y termina con un código de salida coherente. Debe ejecutarse con el intérprete esperado y documentar sus requisitos.

Ejemplo educativo:

    #!/usr/bin/env bash
    set -u

    if [[ $# -ne 1 ]]; then
      printf 'Uso: %s DIRECTORIO\n' "$0" >&2
      exit 2
    fi

    directorio=$1

    if [[ ! -d "$directorio" ]]; then
      printf 'No existe el directorio indicado\n' >&2
      exit 1
    fi

    find "$directorio" -maxdepth 1 -type f -print
    resultado=$?
    if [[ $resultado -ne 0 ]]; then
      printf 'La búsqueda terminó con error\n' >&2
      exit "$resultado"
    fi
    exit 0

Este ejemplo ilustra argumentos, validación y códigos de salida. En scripts de producción define cómo manejar errores de cada comando y si necesitas pipefail, traps o compatibilidad con otras shells.

### 7.4.11 — Cron

Cron programa tareas periódicas. El entorno puede diferir de una sesión interactiva: PATH, directorio, permisos y variables pueden ser distintos.

### 7.4.12 — Automatización

Combina scripts, programación y supervisión para tareas repetibles. Diseña ejecuciones idempotentes, registra resultados sin secretos y contempla fallos parciales.

Cron programa tareas periódicas en sistemas que lo utilizan. Verifica la sintaxis del calendario y recuerda que el entorno puede diferir de una sesión interactiva: PATH, directorio de trabajo, permisos y variables pueden ser distintos. No programes tareas destructivas o repetitivas sin logs, control de errores y una forma de detenerlas.

## 7.5 — Windows

### 7.5.1 — Arquitectura de Windows

Windows organiza ejecución, memoria, seguridad, dispositivos y servicios mediante componentes del sistema.

### 7.5.2 — Sistema de archivos NTFS

NTFS gestiona archivos, directorios, metadatos y permisos. El acceso efectivo puede depender también de permisos compartidos de red.

### 7.5.3 — Usuarios y grupos

Las cuentas y grupos permiten asignar derechos. Aplica mínimo privilegio.

### 7.5.4 — Permisos

Los permisos NTFS definen acciones sobre archivos y carpetas; considera herencia y grupos.

### 7.5.5 — Procesos

El Administrador de tareas permite observar procesos y consumo. Identifica contexto antes de terminar uno.

### 7.5.6 — Servicios

Antes de detener un servicio, revisa dependencias, función e impacto.

### 7.5.7 — Registro de Windows

El Registro es una base jerárquica de configuración. Confirma la clave exacta y prepara reversión; no ejecutes archivos .reg desconocidos.

### 7.5.8 — Administrador de tareas

Permite observar aplicaciones, procesos, rendimiento y usuarios.

### 7.5.9 — Visor de eventos

Consulta registros de sistema, seguridad y aplicaciones. Filtra y redacta datos sensibles antes de compartir.

### 7.5.10 — Firewall

Aplica reglas de tráfico según perfiles. No lo desactives para solucionar un problema sin identificar regla y alcance.

### 7.5.11 — PowerShell

Es una shell y lenguaje de automatización basado en objetos. Cmdlets de exploración: Get-Process, Get-Service, Get-WinEvent, Get-Help y Get-Command.

### 7.5.12 — Administración de servicios

Consulta nombre, estado, tipo de inicio y dependencias antes de cambiar un servicio. Practica en una VM.

El Firewall aplica reglas de tráfico entrante y saliente según perfiles y configuración. No lo desactives para solucionar un problema sin identificar la regla, el perfil y el alcance. Crea excepciones mínimas y documentadas.

PowerShell es una shell y lenguaje de automatización basado en objetos. Sus cmdlets producen objetos estructurados. Comandos de exploración útiles en laboratorio: Get-Process, Get-Service, Get-WinEvent, Get-Help y Get-Command. Get-EventLog es legado y no resulta adecuado para todos los registros modernos.

Para administrar servicios, consulta primero el estado y nombre exacto; después evalúa si detenerlos o iniciarlos es seguro. Practica cambios administrativos en una VM, no en el equipo principal.

## 7.6 — Virtualización

### 7.6.1 — VirtualBox

VirtualBox permite crear y administrar máquinas virtuales. Sus funciones dependen de versión, host y configuración.

### 7.6.2 — VMware

VMware ofrece plataformas y productos con capacidades y licencias distintas.

### 7.6.3 — Máquinas virtuales

Una VM presenta hardware virtual a un sistema invitado. Consume CPU, RAM y almacenamiento del host.

### 7.6.4 — Snapshots

Un snapshot captura un estado para volver a él durante pruebas. No sustituye backups independientes y puede consumir almacenamiento.

### 7.6.5 — Recursos virtualizados

CPU, memoria, almacenamiento y red se asignan a la VM. Deja recursos suficientes al host.

### 7.6.6 — Redes virtuales

Conectan VMs entre sí, con el host o con redes externas según el modo. Documenta topología y reglas.

### 7.6.7 — NAT

NAT permite acceso externo mediado por el host; las conexiones entrantes requieren reglas específicas.

### 7.6.8 — Host-only

Crea una red privada entre host y VMs participantes y normalmente no ofrece acceso externo por sí sola.

### 7.6.9 — Adaptadores de red virtuales

Conectan VMs a redes definidas por la plataforma. Comprueba modo, interfaz, IP y rutas antes de habilitar modo puente.

## Proyecto oficial — Dos servidores virtuales

### Objetivo y preparación

Instalar y administrar Ubuntu Server y una introducción a Windows Server dentro de máquinas virtuales aisladas. El proyecto debe demostrar administración de usuarios, permisos, servicios, procesos y registros.

1. Comprueba requisitos de hardware y espacio del host.
2. Descarga imágenes de instalación desde fuentes oficiales.
3. Verifica checksums o firmas cuando estén disponibles.
4. Crea dos VMs con recursos moderados.
5. Utiliza NAT o Host-only; no expongas servicios administrativos a Internet.
6. Registra versiones, recursos y configuración de red.
7. Crea snapshots antes de cambios importantes.
8. Define contraseñas únicas y no las incluyas en capturas, scripts ni repositorios.

### Parte A — Ubuntu Server

- Instalar el sistema.
- Crear una cuenta administrativa y una cuenta de uso normal.
- Revisar grupos y permisos.
- Crear directorios y archivos de laboratorio.
- Consultar procesos y servicios.
- Revisar logs.
- Comprobar uso de almacenamiento y montajes.
- Crear un script Bash que informe el estado de un directorio.
- Documentar comandos y resultados.

### Parte B — Windows Server (introducción)

- Instalar una edición de evaluación o medio autorizado.
- Identificar arquitectura y herramientas administrativas.
- Crear cuentas y grupos de laboratorio.
- Configurar permisos NTFS en una carpeta de práctica.
- Inspeccionar procesos y servicios.
- Consultar eventos.
- Revisar firewall y reglas activas.
- Utilizar PowerShell para obtener información del sistema.
- Documentar cambios y procedimiento de reversión.

### Entregables

1. Ficha técnica de ambas VMs.
2. Diagrama de red virtual y justificación NAT/Host-only.
3. Versiones y origen de las imágenes.
4. Evidencias redactadas de instalación y configuración.
5. Matriz de usuarios, grupos y permisos.
6. Inventario de servicios y procesos revisados.
7. Extractos de logs sin secretos ni datos privados.
8. Script Bash y pruebas de códigos de salida.
9. Comandos PowerShell y resultados.
10. Snapshots identificados y plan de recuperación.
11. Bitácora de incidentes y solución.
12. Conclusión sobre diferencias operativas entre Linux y Windows.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Comprensión de fundamentos del SO | 15 |
| Administración Linux y permisos | 20 |
| Bash y automatización segura | 15 |
| Administración Windows y PowerShell | 15 |
| Virtualización y redes | 15 |
| Procesos, servicios y logs | 10 |
| Evidencias, documentación y seguridad | 10 |

## Ejercicios de comprensión

1. ¿Qué diferencia hay entre Kernel Space y User Space?  
   **Respuesta orientativa:** el primero contiene ejecución privilegiada del kernel; el segundo aloja aplicaciones con privilegios restringidos.

2. ¿Qué diferencia existe entre proceso e hilo?  
   **Respuesta:** el proceso posee recursos y espacio de direcciones; los hilos son secuencias de ejecución dentro del proceso y suelen compartir recursos.

3. ¿Concurrencia y paralelismo son sinónimos?  
   **Respuesta:** no; concurrencia organiza tareas que progresan de forma solapada y paralelismo implica ejecución simultánea.

4. ¿Qué hace una system call?  
   **Respuesta:** permite solicitar servicios controlados al kernel.

5. ¿Por qué no debe usarse root para todo?  
   **Respuesta:** aumenta el impacto potencial de errores y compromisos; se aplica mínimo privilegio.

6. ¿Qué diferencia hay entre /etc y /var?  
   **Respuesta:** configuración del sistema frente a datos variables, incluidos logs y colas.

7. ¿Qué significa x en un directorio?  
   **Respuesta:** permite atravesarlo o acceder a entradas según los demás permisos.

8. ¿Qué diferencia hay entre NAT y Host-only?  
   **Respuesta:** NAT permite conectividad externa mediada por el host según reglas; Host-only crea una red privada entre host y VMs.

9. ¿Un snapshot sustituye un backup?  
   **Respuesta:** no; suele depender del disco base y de la cadena de snapshots.

10. ¿Por qué un script debe revisar códigos de salida?  
    **Respuesta:** para detectar fallos y comunicar el resultado real a quien lo ejecuta o a otro proceso.

## Autoevaluación práctica

En la VM realiza sin copiar una guía:
- localizar un archivo;
- crear y cambiar permisos de un directorio;
- identificar un proceso;
- consultar estado y logs de un servicio no crítico;
- comprobar uso de disco;
- ejecutar un script con argumento correcto e incorrecto;
- en Windows, consultar procesos, servicios y eventos;
- explicar el aislamiento de red de ambas VMs.

Registra comandos, resultados y errores. No ejecutes comandos destructivos fuera del directorio de laboratorio.

## Recursos audiovisuales

No se añaden videos en esta versión. La etapa abarca sistemas operativos, administración Linux, Bash, Windows y virtualización; un recurso genérico no cubriría fielmente todos los subtemas. Los recursos se incorporarán por lección cuando se compruebe que el audio hablado está en español, el contenido coincide con el objetivo y la versión no induce a instrucciones obsoletas. No se considera aprobado un video solo por su título o subtítulos.

## Referencias oficiales y técnicas

- Linux kernel documentation: https://docs.kernel.org/
- The Linux man-pages project: https://man7.org/linux/man-pages/
- GNU Bash Reference Manual: https://www.gnu.org/software/bash/manual/
- systemd documentation: https://www.freedesktop.org/wiki/Software/systemd/
- Ubuntu Server documentation: https://documentation.ubuntu.com/server/
- Debian Administrator's Handbook: https://www.debian.org/doc/
- Microsoft Learn — Windows Server: https://learn.microsoft.com/en-us/windows-server/
- Microsoft Learn — PowerShell: https://learn.microsoft.com/en-us/powershell/
- Microsoft Learn — NTFS overview: https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview
- Oracle VirtualBox User Manual: https://www.virtualbox.org/manual/
- VMware documentation: https://docs.vmware.com/

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** comandos, scripts y laboratorio propuestos; no ejecutados en VMs reales durante esta sesión.  
**Estado editorial:** en desarrollo; no aprobado ni publicado..
