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

El kernel es el componente privilegiado que administra CPU, memoria, dispositivos y servicios fundamentales del sistema. Expón la diferencia entre el kernel y el sistema operativo completo: utilidades, bibliotecas y aplicaciones se ejecutan alrededor de él. **Práctica:** identifica la versión del kernel con `uname -r` en Linux y registra la arquitectura con `uname -m`. **Evidencia:** explica qué información entrega cada comando y por qué no describe por sí solo toda la distribución.

### 7.1.2 — Kernel Space

Kernel Space es el espacio de ejecución protegido donde opera el núcleo y donde se aplican privilegios elevados; no es una carpeta ni una partición de memoria asignada al usuario. Relaciona el modo privilegiado con la protección frente a accesos arbitrarios a hardware y memoria. **Práctica:** dibuja la frontera entre espacio de usuario y espacio de kernel y sitúa una llamada al sistema en el cruce. **Evidencia:** describe qué riesgo evita esa separación.

### 7.1.3 — User Space

User Space es el entorno donde se ejecutan procesos ordinarios con permisos restringidos. Explica cómo una aplicación solicita servicios al kernel sin acceder directamente a recursos privilegiados y por qué el aislamiento entre procesos es una propiedad central. **Práctica:** observa procesos de usuario con `ps` y distingue PID, usuario y comando. **Evidencia:** interpreta tres filas sin confundir proceso con hilo.

### 7.1.4 — System Calls

Una system call es la interfaz controlada mediante la cual un proceso solicita una operación al kernel, por ejemplo abrir un archivo o crear un proceso. Distingue la llamada al sistema de una función de biblioteca: la biblioteca puede preparar argumentos y finalmente invocar el mecanismo del kernel. **Práctica:** examina `open`, `read` o `write` en la documentación local con `man 2`. **Evidencia:** describe la secuencia de solicitud, validación y resultado.

### 7.1.5 — Procesos

Un proceso es una instancia de programa en ejecución con espacio de direcciones, recursos y estado propios. Desarrolla estados, PID, creación y terminación, y diferencia el programa almacenado del proceso activo. **Práctica:** ejecuta `sleep 60 &`, localiza su PID con `ps` y termina únicamente ese proceso de laboratorio. **Evidencia:** registra el cambio de estado y explica por qué el PID identifica la instancia.

### 7.1.6 — Hilos

Un hilo es una secuencia de ejecución dentro de un proceso; los hilos de un mismo proceso comparten recursos como el espacio de direcciones, aunque cada uno mantiene su contexto de ejecución. Compara su coste y coordinación con procesos separados, sin afirmar que todos los lenguajes implementan hilos igual. **Práctica:** dibuja un proceso con dos hilos y marca qué recursos comparten y cuáles son propios. **Evidencia:** identifica un riesgo de condición de carrera.

### 7.1.7 — Scheduler

El scheduler decide qué tarea ejecutable recibe tiempo de CPU y cuándo ocurre el cambio, sujeto a políticas y prioridades del sistema. Distingue planificación de procesos/hilos de la planificación de trabajos de una aplicación. **Práctica:** observa `top` o `htop` y compara estado, prioridad y uso de CPU de procesos de prueba. **Evidencia:** explica por qué un proceso en espera de I/O no consume CPU continuamente.

### 7.1.8 — Context Switching

Un context switch guarda el contexto de una tarea y restaura el de otra para permitir la multiplexación de CPU. Explica que el cambio tiene un coste y puede implicar efectos de caché, pero no debe confundirse con el cambio entre modo usuario y modo kernel. **Práctica:** construye una línea temporal de dos tareas que alternan CPU. **Evidencia:** señala qué estado debe preservarse para reanudar correctamente cada tarea.

### 7.1.9 — Memoria virtual

La memoria virtual ofrece a cada proceso un espacio de direcciones lógico que el sistema traduce a memoria física mediante tablas de páginas y mecanismos del procesador. Explica aislamiento, paginación y fallos de página; diferencia memoria virtual de swap, que es solo uno de los mecanismos posibles de respaldo. **Práctica:** consulta `free -h` y `vmstat` si está disponible, sin interpretar swap como memoria RAM adicional equivalente. **Evidencia:** explica una traducción virtual-física de forma conceptual.

### 7.1.10 — Drivers

Un driver permite que el sistema operativo controle un dispositivo mediante una interfaz definida. Distingue controladores del kernel, módulos cargables y software de usuario; su disponibilidad y modelo varían por sistema operativo y dispositivo. **Práctica:** en Linux consulta `lsmod` y `lspci -k` si las herramientas están instaladas. **Evidencia:** relaciona un dispositivo con el controlador asociado sin descargar ni modificar módulos.

### 7.1.11 — Sistema de archivos

El sistema de archivos organiza nombres, directorios, metadatos y bloques persistentes sobre un dispositivo o volumen. Compara estructura lógica con el soporte físico y explica montaje, permisos, enlaces y journaling a nivel introductorio. **Práctica:** crea un directorio y un archivo temporal, inspecciona tipo y metadatos con `stat` y elimínalos al finalizar. **Evidencia:** diferencia nombre, inode y contenido.

### 7.1.12 — IPC (comunicación entre procesos)

La comunicación entre procesos (IPC) permite intercambiar datos o sincronizar tareas mediante mecanismos como pipes, sockets, memoria compartida, colas y señales. Compara comunicación local y de red, y explica por qué cada mecanismo tiene diferentes garantías y costes. **Práctica:** conecta `printf` con `grep` mediante una pipe y describe el flujo entre procesos. **Evidencia:** identifica productor, consumidor y canal.

### 7.1.13 — Concurrencia

La concurrencia describe la composición de varias tareas cuyo progreso se solapa; puede ocurrir incluso en un único núcleo mediante intercalado. Explica interleavings, secciones críticas, exclusión mutua y condiciones de carrera con un ejemplo de contador compartido. **Práctica:** construye una secuencia de dos hilos que actualizan el mismo valor y marca dónde podría perderse una actualización. **Evidencia:** propone una sincronización adecuada.

### 7.1.14 — Paralelismo

El paralelismo ocurre cuando varias tareas se ejecutan simultáneamente en recursos de cómputo distintos, por ejemplo varios núcleos. Contrástalo con concurrencia y analiza límites como dependencias, contención y coste de coordinación. **Práctica:** clasifica tres escenarios (servidor de solicitudes, descarga concurrente y cálculo dividido entre núcleos) indicando si hay concurrencia, paralelismo o ambos. **Evidencia:** justifica cada clasificación.

## 7.2 — Linux

### 7.2.1 — Distribuciones

Una distribución Linux integra el kernel con utilidades, gestor de paquetes, bibliotecas, instalador, políticas y ciclo de mantenimiento. Compara criterios de selección —soporte, estabilidad, comunidad, repositorios y uso— sin reducir las distribuciones a temas visuales. **Práctica:** compara las páginas oficiales de Ubuntu y Debian para identificar versiones y periodos de soporte publicados. **Evidencia:** recomienda una para un laboratorio y justifica la decisión.

### 7.2.2 — Kernel Linux

El kernel Linux es el núcleo del sistema y se desarrolla como proyecto de código abierto; una distribución selecciona, configura y empaqueta una versión junto con otros componentes. Distingue versión upstream, kernel empaquetado y kernel en ejecución. **Práctica:** consulta `uname -r` y `cat /proc/version`. **Evidencia:** explica por qué el número mostrado no identifica por sí solo la versión completa de la distribución.

### 7.2.3 — Ubuntu

Ubuntu es una distribución basada en Debian que publica ediciones y ciclos de soporte definidos por Canonical. Explica diferencias generales entre LTS y versiones intermedias y la importancia de consultar el ciclo vigente antes de instalar en producción. **Práctica:** identifica versión, codename y origen de paquetes en una VM con `lsb_release -a` o `/etc/os-release`. **Evidencia:** registra la edición y su fuente oficial de soporte.

### 7.2.4 — Debian

Debian es una distribución comunitaria con ramas y políticas de publicación propias, conocida por priorizar estabilidad y criterios de software libre. Distingue stable, testing y unstable como ramas de desarrollo, no como niveles de seguridad garantizados. **Práctica:** inspecciona `/etc/os-release` y la configuración de repositorios de una VM Debian sin cambiarla. **Evidencia:** explica qué rama está configurada y por qué no se deben mezclar repositorios indiscriminadamente.

### 7.2.5 — Estructura del sistema de archivos

La jerarquía del sistema de archivos Linux presenta una vista unificada de recursos y volúmenes bajo una raíz `/`; no equivale a las letras de unidad de Windows. Explica rutas absolutas y relativas, directorios montados y convenciones del Filesystem Hierarchy Standard. **Práctica:** recorre `/`, `/home`, `/etc` y `/var` en modo lectura. **Evidencia:** clasifica qué tipo de información suele residir en cada ubicación.

### 7.2.6 — Directorios del sistema de archivos

Los directorios `/etc`, `/var`, `/home`, `/usr`, `/tmp` y `/opt` tienen propósitos distintos: configuración del sistema, datos variables, perfiles, software y recursos compartidos, temporales y aplicaciones adicionales. Advierte que los detalles pueden variar por distribución y paquete. **Práctica:** localiza un archivo de configuración y un log sin modificarlos. **Evidencia:** justifica por qué cada ruta es apropiada y evita almacenar secretos en ubicaciones públicas.

### 7.2.7 — Usuarios

Las cuentas de usuario representan identidades locales con UID, grupo principal, directorio personal y shell, entre otros atributos. Distingue nombre visible de UID y explica cuentas de servicio frente a cuentas interactivas. **Práctica:** consulta `id`, `getent passwd` y `whoami` en una VM. **Evidencia:** interpreta UID, GID y grupos suplementarios sin revelar datos sensibles del host.

### 7.2.8 — Grupos

Los grupos reúnen identidades para asignar permisos de forma administrable; una cuenta puede pertenecer a un grupo principal y a varios suplementarios. Explica el uso de grupos para compartir recursos sin conceder privilegios globales. **Práctica:** inspecciona `getent group` y `id` con una cuenta de laboratorio. **Evidencia:** diseña un grupo para un directorio compartido y describe qué acceso habilitaría.

### 7.2.9 — Permisos

Los permisos tradicionales de Unix representan lectura, escritura y ejecución para propietario, grupo y otros; también existen ACL y bits especiales. Explica que el significado de ejecución cambia entre archivos y directorios. **Práctica:** crea un archivo de prueba y compara `chmod 640` con `chmod 750` usando `ls -l`. **Evidencia:** traduce ambos modos a permisos efectivos y selecciona el mínimo necesario.

### 7.2.10 — Propietarios

La propiedad de archivos y directorios identifica un usuario y un grupo asociados al objeto. Distingue propietario de quien creó el archivo originalmente y explica cómo la propiedad influye en la evaluación de permisos. **Práctica:** consulta `stat` y `ls -ln` sobre archivos de laboratorio. **Evidencia:** identifica UID/GID propietarios y explica qué cambiaría al reasignar el grupo.

### 7.2.11 — Root

Root es la cuenta de UID 0 con privilegios administrativos amplios; no es simplemente un usuario normal con una contraseña más fuerte. Explica el riesgo de operar como root de forma continua y el principio de mínimo privilegio. **Práctica:** verifica `id` y `whoami` en una cuenta ordinaria; no habilites acceso root remoto. **Evidencia:** describe dos tareas que requieren elevación y dos que no.

### 7.2.12 — Sudo

`sudo` permite ejecutar comandos con privilegios delegados conforme a una política, normalmente registrada en `/etc/sudoers` y archivos asociados. Explica autenticación, alcance, auditoría y el riesgo de conceder permisos demasiado amplios. **Práctica:** en una VM desechable, ejecuta `sudo -l` para inspeccionar permisos; no edites sudoers con un editor ordinario. **Evidencia:** diferencia autorización para un comando concreto de acceso administrativo irrestricto.

### 7.2.13 — Procesos

La administración de procesos en Linux utiliza PID, señales, prioridades y herramientas de observación. Distingue procesos en ejecución, durmientes, detenidos y zombis, y evita terminar procesos desconocidos del sistema. **Práctica:** lanza `sleep 120` en una terminal, localízalo con `pgrep -a sleep` y finaliza solo el PID creado. **Evidencia:** registra comando, PID y resultado.

### 7.2.14 — Servicios

Un servicio es una función persistente o de larga duración administrada por el sistema; en muchas distribuciones modernas systemd gestiona unidades y dependencias. Distingue servicio, proceso y unidad. **Práctica:** consulta `systemctl status` de un servicio existente sin cambiar su estado. **Evidencia:** interpreta activo/inactivo, habilitado/deshabilitado y el proceso asociado.

### 7.2.15 — Paquetes

El gestor de paquetes resuelve dependencias, verifica metadatos y registra la instalación de software desde repositorios configurados. Compara el rol de APT en Debian/Ubuntu con el de otros gestores sin mezclar comandos entre distribuciones. **Práctica:** consulta `apt-cache policy` o `apt show` para un paquete conocido, sin instalarlo. **Evidencia:** identifica versión candidata, repositorio y dependencias declaradas.

### 7.2.16 — Logs

Los logs registran eventos del sistema y aplicaciones; su formato, ubicación y retención dependen del servicio y la distribución. Explica niveles de severidad, marcas temporales, correlación y protección de datos sensibles. **Práctica:** consulta `journalctl -b -p warning` y limita la salida a un servicio de laboratorio. **Evidencia:** resume un evento sin copiar credenciales ni datos personales.

### 7.2.17 — Variables de entorno

Las variables de entorno transmiten configuración a procesos hijos, como rutas, idioma y opciones de ejecución; no son un almacén seguro para secretos por defecto. Distingue variables de shell, entorno exportado y archivos de configuración persistentes. **Práctica:** inspecciona `printenv`, crea una variable temporal y expórtala a un proceso hijo. **Evidencia:** explica por qué una variable no exportada no aparece en el entorno de un subproceso.

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
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** cotejo de las entradas oficiales del roadmap, precisión conceptual, secuencia, ejemplos, prácticas, evaluación, seguridad y referencias.

**Resultado:** revisión documental interna realizada con los ajustes y hallazgos siguientes: Se ordenaron los encabezados numerados de fundamentos y Linux según el roadmap, y se separó la explicación de permisos del concepto de cuenta root. Se revisaron comandos administrativos y advertencias de mínimo privilegio. Pendiente: ejecutar comandos en VMs desechables Linux/Windows, verificar diferencias entre distribuciones y versiones, y validar scripts con pruebas seguras.

**Límite de validación:** no se ejecutaron laboratorios, scripts, servicios, bases de datos, máquinas virtuales ni capturas de red en esta revisión. No se declara aprobación académica externa. La etapa continúa en desarrollo hasta completar las pruebas reproducibles y la segunda revisión.
