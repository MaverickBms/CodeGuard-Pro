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

`pwd` muestra el directorio de trabajo actual y ayuda a evitar operaciones sobre rutas equivocadas. Distingue rutas absolutas, relativas y rutas que atraviesan enlaces simbólicos. **Práctica:** ejecuta `pwd` desde tu directorio personal y desde `/tmp`. **Evidencia:** registra ambas rutas y explica cómo afecta el directorio actual a los comandos relativos.

### 7.3.2 — ls

`ls` enumera el contenido de directorios; `-l`, `-a` y `-h` muestran metadatos, archivos ocultos y tamaños legibles. **Práctica:** compara `ls`, `ls -la` y `ls -lh` en una carpeta de laboratorio. **Evidencia:** identifica permisos, propietario, tamaño y nombre, y explica por qué los archivos que comienzan por punto pueden no aparecer en la salida simple.

### 7.3.3 — cd

`cd` cambia el directorio de trabajo de la shell. Practica rutas absolutas, relativas, `..`, `~` y el retorno al directorio anterior con `cd -`. **Práctica:** navega entre `/tmp`, tu directorio personal y una carpeta de laboratorio. **Evidencia:** confirma cada cambio con `pwd` y explica la diferencia entre `.` y `..`.

### 7.3.4 — mkdir

`mkdir` crea directorios y `-p` permite crear jerarquías intermedias. Explica la interacción con permisos del directorio padre y la umask. **Práctica:** crea `~/lab/etapa7/entrada` con `mkdir -p`. **Evidencia:** verifica la estructura con `find` y elimina únicamente el árbol de práctica.

### 7.3.5 — touch

`touch` actualiza marcas temporales o crea un archivo vacío si no existe; no es una herramienta para escribir contenido. **Práctica:** crea `nota.txt`, inspecciona sus marcas con `stat` y vuelve a ejecutar `touch`. **Evidencia:** identifica qué marca temporal cambió.

### 7.3.6 — cp

`cp` copia archivos y directorios; para árboles se requiere una opción recursiva. Explica cómo evitar sobrescrituras y cuándo preservar atributos con `-a`. **Práctica:** copia un archivo de prueba y compara su hash con `sha256sum`. **Evidencia:** demuestra que el contenido coincide y que el original permanece intacto.

### 7.3.7 — mv

`mv` mueve o renombra archivos y directorios. En un mismo sistema de archivos puede cambiar metadatos; entre sistemas de archivos puede implicar copia y eliminación. **Práctica:** renombra un archivo y muévelo dentro del laboratorio. **Evidencia:** verifica ubicación final y contenido.

### 7.3.8 — rm

`rm` elimina entradas y normalmente no ofrece una papelera ni reversión sencilla. Explica por qué `rm -r` y especialmente `rm -rf` requieren revisar las rutas con cuidado. **Práctica:** elimina un único archivo creado para esta actividad. **Evidencia:** registra la ruta comprobada antes de ejecutar y verifica que no afectaste otros archivos.

### 7.3.9 — find

`find` recorre árboles y filtra por nombre, tipo, tamaño, propietario o tiempo. Distingue una búsqueda de una acción destructiva como `-delete` o `-exec`. **Práctica:** localiza archivos `.log` dentro de una carpeta de laboratorio. **Evidencia:** explica cada criterio y conserva la salida.

### 7.3.10 — grep

`grep` busca patrones y admite expresiones regulares; `-n`, `-i` y `-r` controlan líneas, mayúsculas y recursividad. **Práctica:** crea un texto sintético y busca una palabra con `grep -n`. **Evidencia:** explica el patrón y la línea encontrada.

### 7.3.11 — chmod

`chmod` modifica permisos mediante modos simbólicos u octales. Explica que en directorios los bits de lectura, escritura y ejecución controlan listar, modificar entradas y atravesar la ruta. **Práctica:** aplica `chmod 640` a un archivo de prueba y verifica con `stat`. **Evidencia:** traduce el modo a permisos efectivos.

### 7.3.12 — chown

`chown` cambia propietario y, opcionalmente, grupo; suele requerir privilegios administrativos. Evita cambios recursivos amplios sin inspección previa. **Práctica:** consulta propiedad con `stat`; si la VM lo permite, cambia el grupo de un archivo temporal. **Evidencia:** verifica el cambio y explica el riesgo de `-R` sobre rutas del sistema.

### 7.3.13 — ps

`ps` muestra una instantánea de procesos. Compara `ps -ef` y `ps aux`, e interpreta PID, PPID, usuario, estado y comando sin asumir que las columnas son idénticas. **Práctica:** localiza un proceso `sleep` creado en el laboratorio. **Evidencia:** identifica padre e hijo y explica el estado.

### 7.3.14 — top

`top` presenta una vista dinámica de procesos, carga y memoria; los porcentajes dependen del número de CPU y del intervalo de muestreo. **Práctica:** observa el sistema durante un minuto sin terminar procesos. **Evidencia:** explica la diferencia entre porcentaje de CPU y memoria residente.

### 7.3.15 — kill

`kill` envía una señal a un proceso; no significa necesariamente terminarlo de inmediato. Distingue SIGTERM como solicitud ordenada y SIGKILL como terminación no capturable, reservada para casos justificados. **Práctica:** termina únicamente el proceso `sleep` que creaste. **Evidencia:** explica por qué se prefiere una terminación ordenada.

### 7.3.16 — systemctl

`systemctl` consulta y administra unidades de systemd. Distingue estado actual (`status`), arranque automático (`is-enabled`) y acciones que cambian el estado. **Práctica:** consulta el estado de un servicio conocido sin modificarlo. **Evidencia:** interpreta `active`, `enabled` y el proceso asociado.

### 7.3.17 — journalctl

`journalctl` consulta el journal y permite filtrar por arranque, unidad, prioridad y tiempo. No todos los logs de aplicaciones necesariamente se almacenan allí. **Práctica:** ejecuta `journalctl -b -n 30` y filtra por una unidad existente. **Evidencia:** identifica hora, unidad y prioridad sin exponer datos sensibles.

### 7.3.18 — df

`df` informa espacio disponible por sistema de archivos montado; `-h` facilita la lectura y `-T` muestra el tipo. Distingue capacidad del volumen del espacio atribuido a un directorio. **Práctica:** ejecuta `df -hT` y localiza el montaje que contiene tu carpeta personal. **Evidencia:** registra tipo, tamaño, uso y disponibilidad.

### 7.3.19 — du

`du` estima el espacio atribuido a archivos y directorios; sus resultados pueden diferir de `df` por archivos borrados aún abiertos, puntos de montaje y bloques asignados. **Práctica:** compara `du -sh` sobre tu carpeta de laboratorio con el volumen mostrado por `df`. **Evidencia:** explica por qué los valores no tienen que coincidir.

### 7.3.20 — mount

`mount` conecta un sistema de archivos a un punto de montaje y `umount` lo desconecta cuando no está en uso. Explica dispositivos, UUID, opciones y riesgos de montar volúmenes desconocidos. **Práctica:** inspecciona montajes con `findmnt` o `mount` sin montar dispositivos nuevos. **Evidencia:** identifica origen, destino y tipo.

### Permisos y propietarios

En un directorio de laboratorio crea un archivo, consulta permisos con ls -l y aplica chmod 640. Interpreta el resultado. En un entorno multiusuario controlado, cambia el propietario con chown solo si tienes autorización y privilegios.

### Procesos y servicios

Antes de detener un proceso o servicio, identifica el PID o unidad, comprueba su función y dependencias, determina el impacto y elige la acción menos disruptiva. Kill envía una señal; no significa necesariamente que el proceso termine inmediatamente.

### Logs y almacenamiento

Journalctl consulta el journal de systemd; df informa espacio de sistemas de archivos; du estima uso de archivos y directorios; mount muestra o administra montajes. Los registros pueden contener rutas, nombres de usuario, direcciones y datos de solicitudes. Comparte extractos redactados, no logs completos indiscriminadamente.

## 7.4 — Bash

### 7.4.1 — Variables

En Bash las variables se asignan sin espacios alrededor del igual. Distingue variable de shell y variable exportada al entorno; compara comillas simples y dobles. **Práctica:** asigna un valor con espacios, imprímelo y expórtalo a un subproceso. **Evidencia:** demuestra cuándo se conserva la expansión y cuándo se transmite al proceso hijo.

### 7.4.2 — Operadores

Bash ofrece operadores de comparación, aritmética y lógica; `[[ ]]`, `(( ))` y `[ ]` tienen reglas distintas. **Práctica:** comprueba si un archivo temporal existe y si una variable no está vacía. **Evidencia:** explica el valor lógico de cada condición y evita mezclar sintaxis de otros lenguajes.

### 7.4.3 — Condicionales

`if`, `elif` y `else` seleccionan ramas según el estado de salida de una orden o una expresión de prueba. Bash evalúa códigos de salida, no valores booleanos de otros lenguajes. **Práctica:** comprueba si un directorio existe antes de listar su contenido. **Evidencia:** prueba ambos caminos y registra la salida.

### 7.4.4 — Bucles

`for`, `while` y `until` repiten instrucciones; la elección depende de si se recorre una colección o se espera una condición. Advierte sobre expansión de nombres de archivo y lectura de líneas. **Práctica:** recorre una lista sintética cuyos elementos incluyen espacios. **Evidencia:** demuestra que cada elemento se conserva como unidad.

### 7.4.5 — Funciones

Las funciones encapsulan instrucciones reutilizables y reciben argumentos mediante `$1`, `$2` y `"$@"`. Distingue salida por stdout de código de retorno; `return` no devuelve cadenas arbitrarias. **Práctica:** crea una función que valide si una ruta es un directorio. **Evidencia:** invócala con una ruta válida y otra inexistente.

### 7.4.6 — Arrays

Los arrays indexados almacenan secuencias y los asociativos relacionan claves con valores; la sintaxis depende de la versión de Bash. Explica `${array[@]}` y la importancia de citar la expansión. **Práctica:** recorre un array de servicios ficticios conservando elementos con espacios. **Evidencia:** demuestra que cada elemento llega como argumento independiente.

### 7.4.7 — Pipes

Una pipe (`|`) conecta stdout de un proceso con stdin de otro y permite componer herramientas. Explica que el estado del pipeline puede requerir `set -o pipefail`. **Práctica:** usa `printf` y `grep` para filtrar líneas sintéticas. **Evidencia:** identifica productor, filtro y resultado.

### 7.4.8 — Redirecciones

Las redirecciones controlan stdin, stdout y stderr; `>` sobrescribe, `>>` añade y `2>` redirige errores. Explica el orden de las redirecciones y el riesgo de truncar archivos. **Práctica:** separa salida normal y errores de una orden inocua en dos archivos temporales. **Evidencia:** interpreta los descriptores 0, 1 y 2.

### 7.4.9 — Exit codes

El exit code comunica el resultado de una orden: por convención cero indica éxito y otro valor indica alguna condición de fallo. `$?` contiene el estado de la última orden y debe capturarse inmediatamente. **Práctica:** ejecuta una orden válida y otra que falle de forma controlada. **Evidencia:** usa los estados en una condición.

### 7.4.10 — Scripts

Un script Bash debe declarar intérprete, validar argumentos, citar variables y gestionar errores. `set -e` tiene excepciones y no sustituye el manejo explícito de fallos. **Práctica:** escribe un script que valide una ruta y muestre un mensaje claro. **Evidencia:** prueba entrada válida, ausente y ruta inexistente; conserva código y resultados.

### 7.4.11 — Cron

`cron` programa tareas periódicas mediante expresiones de cinco campos y un entorno reducido. Distingue cron de usuario y del sistema; PATH, zona horaria y permisos pueden diferir de una sesión interactiva. **Práctica:** interpreta una expresión y redacta una entrada de ejemplo sin instalarla en el host. **Evidencia:** explica cada campo.

### 7.4.12 — Automatización

La automatización combina scripts, planificación, logs, manejo de errores, idempotencia y permisos mínimos. Una tarea debe poder repetirse sin efectos inesperados. **Práctica:** diseña un script que cree una carpeta de salida si no existe y registre fecha y estado. **Evidencia:** ejecútalo dos veces en el laboratorio y demuestra estabilidad.

## 7.5 — Windows

### 7.5.1 — Arquitectura de Windows

La arquitectura de Windows coordina procesos, memoria, seguridad, dispositivos, servicios y subsistemas mediante componentes del sistema. Distingue kernel, modo usuario, servicios y API Win32 a nivel conceptual. **Práctica:** consulta Información del sistema y Administrador de tareas para identificar versión, arquitectura y procesos. **Evidencia:** relaciona una aplicación con procesos observables sin inferir detalles internos no expuestos.

### 7.5.2 — Sistema de archivos NTFS

NTFS organiza archivos, directorios, metadatos, permisos y características como journaling y enlaces. Distingue permisos NTFS de permisos compartidos SMB: el acceso remoto efectivo depende de ambos conjuntos. **Práctica:** inspecciona propiedades de una carpeta de laboratorio y su pestaña Seguridad. **Evidencia:** explica una entrada de control de acceso y el efecto de herencia.

### 7.5.3 — Usuarios y grupos

Las cuentas y grupos de Windows permiten asignar derechos y permisos a identidades locales o de dominio. Distingue cuentas estándar, administradores y cuentas de servicio. **Práctica:** consulta `whoami /all` y `Get-LocalGroup` en una VM. **Evidencia:** identifica grupos habilitados y justifica el principio de mínimo privilegio.

### 7.5.4 — Permisos

Los permisos NTFS determinan acciones permitidas sobre archivos y carpetas, incluyendo lectura, escritura, modificación y control total. Explica herencia, entradas explícitas y denegaciones; evita simplificar la evaluación efectiva a una sola casilla. **Práctica:** revisa permisos de una carpeta de laboratorio sin cambiar los del sistema. **Evidencia:** calcula qué puede hacer una cuenta según sus grupos.

### 7.5.5 — Procesos

Los procesos son instancias de programas con identificadores, memoria y recursos; el Administrador de tareas y PowerShell permiten observarlos. Distingue proceso, servicio y aplicación visible. **Práctica:** ejecuta `Get-Process` y filtra un proceso conocido. **Evidencia:** registra PID, nombre y uso de recursos y explica por qué no debes finalizar procesos desconocidos.

### 7.5.6 — Servicios

Un servicio de Windows ejecuta una función en segundo plano y puede iniciar automáticamente, manualmente o bajo desencadenadores. Antes de detenerlo revisa dependencias, cuenta de servicio e impacto. **Práctica:** consulta `Get-Service` y `sc.exe qc` sobre un servicio no crítico. **Evidencia:** identifica estado, tipo de inicio y dependencias.

### 7.5.7 — Registro de Windows

El Registro de Windows almacena configuración jerárquica en claves y valores, con hives y permisos propios. Modificarlo incorrectamente puede impedir el funcionamiento del sistema o de aplicaciones. **Práctica:** consulta una clave documentada mediante `reg query` sin editarla. **Evidencia:** registra ruta, tipo y dato, y explica cómo se realizaría una copia de seguridad antes de un cambio autorizado.

### 7.5.8 — Administrador de tareas

El Administrador de tareas permite observar aplicaciones, procesos, rendimiento, usuarios y elementos de inicio. Explica que la vista resumida no sustituye un análisis detallado de eventos o rendimiento. **Práctica:** compara CPU, memoria y disco en reposo y durante una tarea inocua. **Evidencia:** describe el cambio observado y evita atribuir causalidad sin más datos.

### 7.5.9 — Visor de eventos

El Visor de eventos centraliza registros de Windows, incluidos eventos de sistema, aplicación y seguridad según permisos y auditoría configurada. Aprende a filtrar por origen, nivel, ID y periodo. **Práctica:** revisa eventos recientes del registro Sistema en una VM. **Evidencia:** resume un evento con hora, origen e ID, protegiendo información personal.

### 7.5.10 — Firewall

Windows Defender Firewall filtra tráfico según perfiles y reglas de entrada y salida. Explica alcance, programa, puerto, protocolo y perfil de red; desactivarlo globalmente no es una solución de diagnóstico aceptable. **Práctica:** inspecciona reglas activas con `Get-NetFirewallProfile` y `Get-NetFirewallRule`. **Evidencia:** describe una regla sin modificar la política.

### 7.5.11 — PowerShell

PowerShell es una shell y lenguaje de automatización que trabaja con objetos .NET, no solo texto. Introduce cmdlets, tuberías de objetos, módulos y ayuda integrada. **Práctica:** ejecuta `Get-Command`, `Get-Help Get-Process` y `Get-Process`. **Evidencia:** explica cómo seleccionar propiedades con `Select-Object` y filtrar con `Where-Object`.

### 7.5.12 — Administración de servicios

La administración de servicios requiere revisar estado, tipo de inicio, identidad de ejecución, dependencias y eventos asociados. Distingue consulta de cambio: `Get-Service` observa, mientras `Start-Service` y `Stop-Service` alteran el estado. **Práctica:** consulta un servicio de laboratorio sin detenerlo. **Evidencia:** redacta un procedimiento seguro que incluya autorización, impacto, reversión y verificación.

## 7.6 — Virtualización

### 7.6.1 — VirtualBox

VirtualBox permite crear y administrar máquinas virtuales con discos, controladores y redes virtuales configurables. Las funciones disponibles dependen de versión, sistema anfitrión y paquetes instalados. **Práctica:** inspecciona la configuración de una VM apagada. **Evidencia:** identifica memoria, CPU, disco virtual y adaptador de red sin modificar la máquina principal.

### 7.6.2 — VMware

VMware comprende distintos productos de virtualización con funciones, licencias y compatibilidades que no son idénticas. Compara el producto concreto y su documentación antes de aplicar instrucciones. **Práctica:** identifica el hipervisor y la versión instalados en un entorno de laboratorio. **Evidencia:** documenta host compatible, formato de VM y opciones de red disponibles.

### 7.6.3 — Máquinas virtuales

Una máquina virtual presenta hardware virtual a un sistema invitado y comparte recursos físicos del host mediante el hipervisor. Explica invitado, anfitrión, firmware virtual, disco y dispositivos. **Práctica:** crea una VM de prueba con recursos moderados y una imagen de instalación legítima. **Evidencia:** registra configuración y confirma que el host conserva recursos suficientes.

### 7.6.4 — Snapshots

Un snapshot captura el estado de una VM para facilitar pruebas y reversión; no equivale a un backup independiente ni protege necesariamente frente a pérdida del host. **Práctica:** crea un snapshot antes de un cambio inocuo y vuelve a él. **Evidencia:** describe qué estado se restauró y qué datos externos podrían no estar incluidos.

### 7.6.5 — Recursos virtualizados

La virtualización asigna CPU, memoria, almacenamiento y dispositivos al invitado; una asignación excesiva puede degradar al host. Explica sobreasignación, memoria dinámica, E/S y límites de rendimiento. **Práctica:** compara recursos asignados con recursos disponibles antes de iniciar la VM. **Evidencia:** justifica una configuración equilibrada.

### 7.6.6 — Redes virtuales

Las redes virtuales conectan VMs entre sí, con el host o con redes externas según el modo elegido. Distingue conmutador virtual, interfaz virtual, DHCP y rutas. **Práctica:** dibuja una topología con dos VMs y el host, indicando segmentos y puertas de enlace. **Evidencia:** predice qué pares pueden comunicarse antes de probarlo.

### 7.6.7 — NAT

NAT permite que una VM acceda a redes externas mediante traducción realizada por el host o hipervisor; las conexiones entrantes suelen requerir reglas de reenvío. **Práctica:** verifica conectividad saliente desde una VM aislada sin exponer servicios. **Evidencia:** explica por qué la VM puede navegar sin ser directamente alcanzable desde la LAN.

### 7.6.8 — Host-only

Host-only crea una red privada entre el host y las VMs conectadas a ese segmento; normalmente no proporciona salida a Internet por sí misma. **Práctica:** conecta dos VMs de laboratorio a la misma red host-only y verifica conectividad con direcciones privadas. **Evidencia:** identifica qué rutas existen y cuáles no.

### 7.6.9 — Adaptadores de red virtuales

Los adaptadores virtuales conectan la interfaz de una VM con modos como NAT, host-only o bridge, según el hipervisor. El modo bridge puede exponer el invitado a la red física y debe elegirse con autorización. **Práctica:** inspecciona el modo y dirección IP de cada adaptador. **Evidencia:** documenta MAC, IP, modo y alcance de conectividad.

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
