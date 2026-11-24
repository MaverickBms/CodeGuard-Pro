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

**Propósito y modelo.** El kernel es el núcleo privilegiado que coordina CPU, memoria, dispositivos, sistemas de archivos y mecanismos de comunicación. El sistema operativo completo incluye además bibliotecas, servicios, utilidades y aplicaciones; por eso kernel y distribución no son sinónimos. En Linux, varias distribuciones pueden utilizar el mismo kernel upstream, pero diferir en configuración, parches, integración y ciclo de soporte.

**Ejemplo desarrollado.** Cuando una aplicación solicita leer un archivo, utiliza una interfaz de usuario; el kernel comprueba permisos y estado del descriptor, coordina el sistema de archivos y devuelve datos o un error. La aplicación no controla directamente el dispositivo de almacenamiento.

**Práctica guiada.** Ejecuta `uname -r` y `uname -m`. Registra versión del kernel en ejecución y arquitectura. Contrasta con `cat /etc/os-release` para identificar por separado kernel y distribución.

**Actividad independiente.** Explica qué responsabilidades conserva un servidor sin entorno gráfico y dibuja el recorrido de una solicitud de lectura.

**Criterios de aceptación.** Diferencia kernel, distribución y utilidades; interpreta ambos comandos; identifica tres recursos administrados por el kernel.

**Errores frecuentes.** Afirmar que Linux es únicamente el kernel o que `uname -r` identifica la versión de Ubuntu/Debian.

**Comprobación.** ¿Por qué una distribución puede actualizar componentes sin que todos compartan el mismo número de versión?

### 7.1.2 — User Space

**Propósito y modelo.** User Space es el contexto donde se ejecutan aplicaciones y servicios con privilegios restringidos. Los procesos poseen identidad, permisos y recursos; solicitan operaciones privilegiadas mediante interfaces controladas en vez de manipular directamente el hardware. Namespaces, seccomp y otros mecanismos pueden reforzar el aislamiento, según la plataforma y configuración.

**Ejemplo desarrollado.** Un editor puede leer un documento si los permisos lo permiten, pero no escribe directamente en bloques del dispositivo. Solicita la operación al sistema y recibe un descriptor o un error.

**Práctica guiada.** Ejecuta `ps -eo pid,user,stat,comm --sort=pid | head`. Interpreta PID, usuario, estado y comando en tres filas. No finalices procesos ajenos a la práctica.

**Actividad independiente.** Describe qué permisos necesitaría un proceso para leer un archivo privado de otra cuenta y qué controles pueden impedirlo.

**Criterios de aceptación.** Explica ejecución sin privilegios, interpreta la salida de `ps` y distingue proceso de usuario.

**Errores frecuentes.** Tratar User Space como una carpeta o asumir que todos los procesos de usuario tienen idénticos permisos.

**Comprobación.** ¿Por qué una aplicación solicita al kernel abrir un archivo en lugar de acceder directamente al disco?

### 7.1.3 — Kernel Space

**Propósito y modelo.** Kernel Space es el espacio de direcciones y privilegio administrado por el sistema y el procesador. No es una carpeta, partición física exclusiva ni directorio. El procesador aplica niveles de privilegio y protección de memoria para impedir que un proceso ordinario acceda libremente al núcleo. Una llamada al sistema permite ejecutar una operación controlada en contexto privilegiado; no convierte permanentemente la aplicación en kernel.

**Ejemplo desarrollado.** Al solicitar la creación de un proceso, la aplicación entra por una interfaz del sistema; el kernel valida parámetros, aplica políticas y devuelve un identificador o un error.

**Práctica guiada.** Dibuja User Space y Kernel Space. Añade aplicación, biblioteca, llamada al sistema y controlador. Marca quién inicia la solicitud y quién valida el acceso.

**Actividad independiente.** Explica por qué una vulnerabilidad en código privilegiado puede tener mayor impacto que un fallo aislado en una aplicación sin privilegios.

**Criterios de aceptación.** Diferencia espacio de direcciones y memoria física; explica privilegios, aislamiento y transición controlada.

**Errores frecuentes.** Decir que Kernel Space es una ubicación del disco o que cualquier llamada al sistema concede privilegios administrativos al usuario.

**Comprobación.** ¿Qué propiedad de seguridad se debilitaría si un proceso pudiera escribir arbitrariamente en memoria del kernel?

### 7.1.4 — Procesos

**Propósito y modelo.** Un proceso es una instancia de ejecución con PID, espacio de direcciones, estado, credenciales y recursos asociados. Puede crear procesos hijos y finalizar normalmente o mediante señales. En Linux, la columna STAT de `ps` resume estados como ejecutable, interrumpible, detenido o zombi. Un programa almacenado en disco no es por sí mismo un proceso activo.

**Ejemplo desarrollado.** Al iniciar `sleep 45 &`, la shell crea una instancia en segundo plano. `ps -p PID -o pid,ppid,stat,etime,cmd` permite inspeccionarla, sustituyendo PID por el identificador real de esa sesión.

**Práctica guiada.** En Bash ejecuta `sleep 45 & pid=$!`, consulta `ps -p "$pid" -o pid,ppid,stat,etime,cmd` y termina solo esa instancia con `kill -TERM "$pid"`. Verifica que dejó de aparecer.

**Actividad independiente.** Dibuja la relación padre-hijo entre una shell y el proceso que inicia; explica qué representa PID y PPID.

**Criterios de aceptación.** Diferencia programa y proceso, interpreta PID/PPID/estado y demuestra la terminación controlada del proceso propio.

**Errores frecuentes.** Confundir PID con nombre de archivo o usar `kill -9` como primera opción.

**Comprobación.** ¿Por qué dos instancias del mismo ejecutable tienen PID distintos?

### 7.1.5 — Hilos

**Propósito y modelo.** Un hilo es una unidad de ejecución dentro de un proceso. Los hilos suelen compartir espacio de direcciones y recursos del proceso, pero cada uno mantiene su propio contador de programa, registros y pila. El modelo concreto depende del sistema y del runtime. Compartir memoria facilita cooperación, pero exige sincronización cuando varias tareas acceden a datos mutables.

**Ejemplo desarrollado.** Dos hilos incrementan una variable compartida. Si ambos leen 10 antes de escribir, cada uno calcula 11 y el resultado puede quedar en 11 en vez de 12: leer-modificar-escribir no es necesariamente atómico.

**Práctica guiada.** Dibuja un proceso con dos hilos. Etiqueta memoria y descriptores compartidos, pila individual y contexto de CPU. Representa el intercalado que pierde una actualización.

**Actividad independiente.** Propón una solución mediante mutex u operación atómica e identifica exactamente qué sección debe protegerse.

**Criterios de aceptación.** Identifica recursos compartidos y propios, describe una condición de carrera y justifica un mecanismo de sincronización.

**Errores frecuentes.** Afirmar que cada hilo tiene un espacio de direcciones independiente o que usar varios hilos garantiza paralelismo.

**Comprobación.** ¿Por qué compartir memoria reduce ciertos costes de comunicación y aumenta el riesgo de condiciones de carrera?

### 7.1.6 — Scheduler

**Propósito y modelo.** El scheduler selecciona entre tareas listas para ejecutarse según políticas, prioridades, afinidad y objetivos de equidad o latencia. Una tarea bloqueada esperando I/O no compite igual que una tarea ejecutable. La implementación cambia entre sistemas y versiones; no presentes un algoritmo concreto como universal. Prioridad y nice afectan la planificación, pero no sustituyen el análisis de carga.

**Ejemplo desarrollado.** Un proceso que calcula puede permanecer ejecutable, mientras otro espera una lectura de disco. El segundo aparece en la tabla de procesos, pero no consume CPU continuamente mientras está bloqueado.

**Práctica guiada.** Ejecuta `ps -eo pid,stat,ni,pcpu,comm --sort=-pcpu | head`. Identifica estado, nice y consumo observado. No cambies prioridades durante la práctica.

**Actividad independiente.** Compara una tarea intensiva en CPU y otra limitada por I/O; predice qué recurso limita cada una y qué observarías.

**Criterios de aceptación.** Diferencia ejecutable y bloqueado, interpreta nice de forma básica y explica la competencia por CPU.

**Errores frecuentes.** Confundir scheduler con cron o interpretar una muestra instantánea como medida completa de rendimiento.

**Comprobación.** ¿Qué diferencia existe entre una tarea lista para ejecutar y otra que espera una operación de entrada/salida?

### 7.1.7 — Context Switching

**Propósito y modelo.** Un cambio de contexto guarda el estado necesario para reanudar una tarea —registros, contador de programa, puntero de pila y metadatos— y restaura el de otra. Puede involucrar cambios de espacio de direcciones y efectos en cachés o TLB, por lo que tiene coste. No es sinónimo de cualquier transición entre modo usuario y modo kernel: una llamada al sistema puede regresar al mismo hilo sin cambiar de tarea.

**Ejemplo desarrollado.** La tarea A se ejecuta; una interrupción o decisión de planificación provoca que el kernel guarde su contexto y seleccione B. Más tarde restaura A desde el punto en que quedó suspendida.

**Práctica guiada.** Construye una línea temporal con dos tareas: ejecución de A, interrupción, guardado, selección de B, restauración y reanudación.

**Actividad independiente.** Explica dos costes posibles de cambios de contexto frecuentes y una razón por la que el sistema los necesita.

**Criterios de aceptación.** Identifica el estado que debe preservarse y diferencia cambio de contexto de cambio de modo.

**Errores frecuentes.** Afirmar que cada llamada al sistema produce obligatoriamente un cambio de contexto.

**Comprobación.** ¿Por qué una transición a Kernel Space puede ocurrir sin que cambie el hilo ejecutado?

### 7.1.8 — Memoria virtual

**Propósito y modelo.** La memoria virtual separa las direcciones utilizadas por un proceso de las ubicaciones físicas. El hardware y las tablas de páginas realizan traducciones; la TLB conserva traducciones recientes. Un fallo de página es una excepción que obliga al sistema a resolver una traducción o informar de un acceso inválido; no significa siempre que haya ocurrido swap. Swap es un mecanismo de respaldo, no RAM equivalente.

**Ejemplo desarrollado.** Dos procesos pueden utilizar la misma dirección virtual y referirse a páginas físicas distintas. Esto permite aislamiento y simplifica la asignación de memoria.

**Práctica guiada.** En Linux consulta `free -h`, `vmstat 1 3` y, si está instalado, `pmap $$`. Registra memoria total, disponible, swap y mapa de la shell. No fuerces agotamiento de memoria.

**Actividad independiente.** Dibuja dos traducciones de direcciones virtuales a marcos físicos distintos y describe qué ocurre ante una página no presente.

**Criterios de aceptación.** Diferencia direcciones virtuales/físicas, página/TLB/fallo de página y memoria virtual/swap.

**Errores frecuentes.** Afirmar que memoria virtual es lo mismo que swap o que todo fallo de página representa un error del programa.

**Comprobación.** ¿Qué ventaja de aislamiento se obtiene al mantener espacios de direcciones separados?

### 7.1.9 — Sistema de archivos

**Propósito y modelo.** Un sistema de archivos organiza directorios, metadatos, asignación de bloques y operaciones sobre datos persistentes. En Linux, VFS ofrece una interfaz común a diferentes sistemas de archivos. Un nombre se asocia a un inode con metadatos; el contenido ocupa bloques. Montar integra el árbol de un volumen en un punto del espacio de nombres. Enlaces duros y simbólicos tienen semánticas distintas.

**Ejemplo desarrollado.** Dos nombres pueden referirse al mismo inode mediante enlaces duros; un enlace simbólico almacena una ruta que se resuelve al acceder. Eliminar un nombre no destruye necesariamente los datos si quedan otros enlaces o un proceso mantiene el archivo abierto.

**Práctica guiada.** Crea un archivo en `~/lab/etapa7`, consulta `stat`, crea un enlace simbólico con `ln -s` y compara con `ls -li`. Inspecciona montajes con `findmnt`.

**Actividad independiente.** Explica la diferencia entre espacio libre (`df`) y uso de directorios (`du`) y plantea por qué pueden diferir.

**Criterios de aceptación.** Identifica inode, nombre, montaje y diferencia entre enlaces; interpreta las salidas de las herramientas.

**Errores frecuentes.** Tratar un directorio como dispositivo físico independiente o asumir que borrar un nombre siempre destruye inmediatamente los datos.

**Comprobación.** ¿Por qué un archivo puede seguir ocupando espacio después de eliminar su nombre visible si un proceso lo mantiene abierto?

### 7.1.10 — Drivers

**Propósito y modelo.** Un driver traduce operaciones del sistema a interacciones específicas con un dispositivo. Puede ejecutarse en kernel o en espacio de usuario según la arquitectura. No debe confundirse con firmware: el firmware se ejecuta en el dispositivo/controlador, mientras el driver es software del sistema anfitrión. La instalación debe provenir de fuentes confiables y ser compatible con hardware y sistema.

**Ejemplo desarrollado.** En Linux, `lspci -k` puede mostrar el controlador asociado a un dispositivo PCI y módulos disponibles. Esa asociación no demuestra por sí sola que todas las funciones del dispositivo trabajen correctamente.

**Práctica guiada.** Ejecuta `lspci -k` si está disponible y `lsmod` para observar módulos cargados. Relaciona un dispositivo con el controlador informado, sin descargar ni modificar módulos.

**Actividad independiente.** Explica las diferencias entre driver, módulo del kernel y firmware utilizando una tarjeta de red como ejemplo.

**Criterios de aceptación.** Describe el papel del controlador, distingue driver de firmware y obtiene información de solo lectura.

**Errores frecuentes.** Descargar módulos al azar, asumir que todo driver es un módulo cargable o confundir el nombre comercial del dispositivo con el controlador activo.

**Comprobación.** ¿Qué riesgo puede introducir un controlador ejecutado con privilegios de kernel?

### 7.1.11 — System Calls

**Propósito y modelo.** Una llamada al sistema es un punto de entrada definido por la ABI para solicitar operaciones como crear procesos, leer archivos o comunicarse. Una función de biblioteca puede preparar argumentos y llamar al mecanismo del kernel; por ello, una función como printf no equivale necesariamente a una única system call. El kernel valida parámetros y permisos, realiza o rechaza la operación y devuelve un resultado. En interfaces POSIX, muchos errores se reflejan mediante valores de retorno y errno.

**Ejemplo desarrollado.** `open()` solicita abrir una ruta y, si tiene éxito, devuelve un descriptor. `read()` utiliza ese descriptor para solicitar bytes. La aplicación debe comprobar retorno, error y fin de archivo.

**Práctica guiada.** Consulta `man 2 open`, `man 2 read` y `man 2 write`. Si existe `strace`, ejecuta `strace -e trace=openat,read,write echo prueba` y relaciona llamadas con la salida.

**Actividad independiente.** Describe el flujo abrir-leer-cerrar e identifica errores posibles por permisos, ruta o descriptor inválido.

**Criterios de aceptación.** Diferencia API de biblioteca y llamada al sistema; explica descriptor, retorno y errno.

**Errores frecuentes.** Afirmar que toda función de biblioteca invoca una llamada al sistema o que una llamada exitosa garantiza que se escribieron todos los bytes solicitados.

**Comprobación.** ¿Por qué read puede devolver menos bytes de los solicitados sin que exista un error?

### 7.1.12 — IPC (comunicación entre procesos)

**Propósito y modelo.** IPC agrupa mecanismos como pipes anónimas o con nombre, colas de mensajes, memoria compartida, señales y sockets. Cada mecanismo ofrece propiedades diferentes: flujo de bytes, mensajes delimitados, notificación, sincronización o comunicación local/remota. La elección depende del volumen, patrón de acceso, persistencia, controles de seguridad y complejidad de coordinación. Compartir memoria suele exigir sincronización adicional.

**Ejemplo desarrollado.** En `printf 'uno\\ndos\\n' | grep dos`, el shell conecta stdout del primer proceso con stdin del segundo mediante una pipe. El productor no necesita conocer la implementación del consumidor.

**Práctica guiada.** Ejecuta el pipeline anterior y luego sustituye el filtro por `wc -l`. Identifica productor, consumidor, canal y resultado. Investiga `set -o pipefail` para comprender cómo se propagan errores en pipelines.

**Actividad independiente.** Selecciona un mecanismo IPC para notificar un evento, transferir un flujo de texto y compartir un bloque grande de datos. Justifica cada elección.

**Criterios de aceptación.** Describe tres mecanismos y explica una ventaja y limitación de cada uno; distingue comunicación de sincronización.

**Errores frecuentes.** Considerar una pipe equivalente a un archivo persistente o asumir que memoria compartida garantiza acceso concurrente seguro.

**Comprobación.** ¿Por qué procesos que comparten memoria necesitan coordinar el acceso a datos mutables?

### 7.1.13 — Concurrencia

**Propósito y modelo.** Concurrencia describe tareas cuyo progreso se intercala o solapa; puede existir incluso con un único núcleo. Una condición de carrera ocurre cuando el resultado depende de un orden de ejecución no controlado. Las secciones críticas protegen estado compartido mediante mutex, semáforos, monitores, operaciones atómicas o diseño sin estado compartido. La sincronización incorrecta puede causar interbloqueo o inanición.

**Ejemplo desarrollado.** Dos tareas ejecutan contador = contador + 1. La operación implica leer, calcular y escribir; si ambas leen el mismo valor antes de escribir, una actualización puede perderse.

**Práctica guiada.** Construye una tabla de intercalado de dos tareas sobre un contador inicial de cero. Anota lecturas y escrituras y calcula el resultado de cada orden.

**Actividad independiente.** Diseña una solución con exclusión mutua e identifica qué operaciones quedan dentro de la sección crítica. Añade un posible riesgo de interbloqueo si se utilizan dos locks.

**Criterios de aceptación.** Define concurrencia, identifica una condición de carrera, propone sincronización y explica un riesgo introducido por locks.

**Errores frecuentes.** Confundir concurrencia con paralelismo o suponer que toda línea de código de alto nivel es atómica.

**Comprobación.** ¿Puede existir una condición de carrera en un equipo con un solo núcleo? Justifica.

### 7.1.14 — Paralelismo

**Propósito y modelo.** El paralelismo ocurre cuando varias operaciones se ejecutan simultáneamente en recursos distintos, como núcleos o dispositivos especializados. Para acelerar una tarea, el trabajo debe poder dividirse, el coste de coordinación debe ser razonable y las dependencias secuenciales no deben dominar. La ley de Amdahl explica por qué la parte secuencial limita la aceleración máxima. Paralelismo no elimina la necesidad de sincronización.

**Ejemplo desarrollado.** Procesar cuatro bloques independientes en cuatro núcleos puede reducir el tiempo frente a una ejecución secuencial, pero preparación, combinación de resultados y contención de memoria añaden costes.

**Práctica guiada.** Clasifica: un servidor que alterna solicitudes en un núcleo; un cálculo dividido entre cuatro núcleos; y una aplicación que atiende solicitudes concurrentes mientras realiza cálculos paralelos. Justifica la clasificación.

**Actividad independiente.** Propón una tarea divisible, identifica dependencias y estima qué fracción debe permanecer secuencial.

**Criterios de aceptación.** Diferencia concurrencia y paralelismo, reconoce límites de escalabilidad y explica por qué añadir núcleos no garantiza aceleración lineal.

**Errores frecuentes.** Usar ambos términos como sinónimos o asumir que cualquier aplicación multihilo ejecuta simultáneamente todos sus hilos.

**Comprobación.** ¿Qué efecto tiene una fracción secuencial grande sobre la aceleración máxima?

## 7.2 — Linux

### 7.2.1 — Distribuciones

**Propósito y modelo.** Una distribución integra el kernel Linux con bibliotecas, utilidades, gestor de paquetes, políticas, instalador y repositorios. La selección debe considerar soporte, estabilidad, compatibilidad de aplicaciones, ciclo de mantenimiento, comunidad y requisitos del entorno. Una distribución no se define solo por su escritorio.

**Ejemplo desarrollado.** Para un servidor de producción, una edición con ciclo de soporte extendido puede reducir cambios frecuentes; para aprendizaje, una distribución con documentación y comunidad amplias puede facilitar la resolución de problemas. La elección depende del uso y no existe una distribución universalmente mejor.

**Práctica guiada.** Compara las páginas oficiales de Ubuntu y Debian. Registra modelo de publicación, edición estable disponible, política de soporte y gestor de paquetes. No uses artículos de terceros como única evidencia.

**Actividad independiente.** Recomienda una distribución para un servidor web pequeño y otra para un laboratorio de aprendizaje. Justifica ambas decisiones con criterios explícitos.

**Criterios de aceptación.** Explica qué integra una distribución y sustenta la recomendación con al menos tres criterios verificables.

**Errores frecuentes.** Confundir distribución con entorno de escritorio o asumir que una versión de soporte extendido recibe indefinidamente todas las mismas actualizaciones.

**Comprobación.** ¿Qué riesgos introduce elegir una distribución sin revisar su ciclo de soporte?

### 7.2.2 — Kernel Linux

**Propósito y modelo.** El kernel Linux es el núcleo del sistema y se publica como proyecto abierto. Una distribución selecciona una versión, aplica parches, configura opciones y empaqueta módulos y herramientas. Debes distinguir versión upstream, paquete del proveedor y kernel actualmente arrancado; pueden no coincidir exactamente.

**Ejemplo desarrollado.** Una actualización puede instalar un kernel nuevo sin cambiar el que está ejecutándose hasta el siguiente reinicio. Por eso el gestor de paquetes puede mostrar una versión instalada distinta de la informada por uname.

**Práctica guiada.** Ejecuta `uname -r`, `cat /proc/version` y, en Debian/Ubuntu, consulta paquetes instalados con `dpkg -l 'linux-image*'`. Registra qué dato ofrece cada fuente.

**Actividad independiente.** Explica qué pasos de verificación harías después de instalar una actualización del kernel antes de retirar una versión anterior.

**Criterios de aceptación.** Diferencia versión en ejecución, paquete instalado y versión upstream; explica por qué puede requerirse reinicio.

**Errores frecuentes.** Suponer que `uname -r` muestra la versión completa de la distribución o eliminar todos los kernels anteriores inmediatamente.

**Comprobación.** ¿Por qué el kernel instalado más reciente no tiene que ser el kernel que está ejecutándose ahora?

### 7.2.3 — Ubuntu

**Propósito y modelo.** Ubuntu es una distribución basada en Debian publicada por Canonical, con ediciones y periodos de mantenimiento definidos. Las versiones LTS y las versiones intermedias responden a ciclos distintos; la cobertura de actualizaciones puede variar por edición, paquete y modalidad de soporte. Verifica siempre la política vigente en documentación oficial.

**Ejemplo desarrollado.** Un servidor puede permanecer en una LTS por estabilidad operativa, mientras un laboratorio puede probar una versión más reciente. La decisión debe contemplar compatibilidad, soporte de hardware, ventana de mantenimiento y aplicaciones requeridas.

**Práctica guiada.** En una VM ejecuta `cat /etc/os-release` y, si está disponible, `lsb_release -a`. Identifica ID, versión y codename. Consulta la página oficial de ciclo de vida para esa versión.

**Actividad independiente.** Elabora una ficha de instalación para un servidor Ubuntu que incluya edición, origen de la ISO, verificación de integridad y plan de actualización.

**Criterios de aceptación.** Identifica la versión real, distingue LTS de no-LTS y aporta la referencia oficial del ciclo aplicable.

**Errores frecuentes.** Elegir una versión solo por ser la más nueva o confundir fecha de publicación con fin de soporte.

**Comprobación.** ¿Qué información debe verificarse antes de desplegar una versión de Ubuntu en un servidor que debe mantenerse varios años?

### 7.2.4 — Debian

**Propósito y modelo.** Debian es una distribución comunitaria con políticas de publicación y ramas propias. Stable prioriza estabilidad; Testing participa en la preparación de la siguiente versión estable y Unstable es una rama de desarrollo continuo. Estas denominaciones no equivalen por sí solas a niveles de seguridad o a una recomendación para todo uso.

**Ejemplo desarrollado.** Un servidor que prioriza previsibilidad puede utilizar Stable y recibir actualizaciones de seguridad según la política del proyecto. Mezclar repositorios de distintas ramas puede introducir dependencias incompatibles y actualizaciones inesperadas.

**Práctica guiada.** En una VM consulta `cat /etc/os-release` y revisa en modo lectura los archivos de configuración de APT bajo `/etc/apt/`. No cambies ni mezcles repositorios.

**Actividad independiente.** Compara el ciclo de Debian Stable con el de una distribución de publicación continua y describe qué tipo de operación podría beneficiarse de cada modelo.

**Criterios de aceptación.** Explica las diferencias generales entre ramas, identifica la configuración presente y justifica por qué no deben mezclarse repositorios sin planificación.

**Errores frecuentes.** Interpretar Unstable como sinónimo de inseguro o considerar Testing como una versión estable lista para cualquier servidor.

**Comprobación.** ¿Por qué una política de repositorios coherente es importante para la reproducibilidad y estabilidad del sistema?

### 7.2.5 — Estructura del sistema de archivos

**Propósito y modelo.** Linux presenta una jerarquía unificada bajo la raíz `/`. Los volúmenes y dispositivos se integran en puntos de montaje; no se navega mediante letras de unidad como en Windows. Las rutas pueden ser absolutas o relativas y los permisos se evalúan en cada componente del camino.

**Ejemplo desarrollado.** La ruta `/var/log/app.log` parte de la raíz y atraviesa directorios. Aunque el archivo tenga permiso de lectura, la cuenta también necesita permiso de búsqueda (x) en los directorios para llegar a él.

**Práctica guiada.** Recorre `/`, `/home`, `/etc` y `/var` con `ls -ld` y consulta montajes con `findmnt`. No modifiques archivos del sistema.

**Actividad independiente.** Dibuja una jerarquía que incluya raíz, directorio personal y un volumen montado bajo `/mnt/datos`. Explica cómo cambia la ruta visible sin cambiar el contenido del volumen.

**Criterios de aceptación.** Distingue ruta absoluta/relativa, raíz y punto de montaje; identifica permisos de recorrido.

**Errores frecuentes.** Suponer que `/mnt` es necesariamente un disco o que cada directorio representa una partición independiente.

**Comprobación.** ¿Qué diferencia existe entre un directorio y un punto de montaje?

### 7.2.6 — Directorios /etc, /var, /home, /usr, /tmp, /opt

**Propósito y modelo.** La jerarquía FHS asigna convenciones a directorios habituales: `/etc` para configuración del host; `/var` para datos variables como logs y colas; `/home` para directorios personales; `/usr` para programas y datos compartidos; `/tmp` para temporales; y `/opt` para software adicional. La distribución y los paquetes pueden introducir variaciones.

**Ejemplo desarrollado.** Un archivo de configuración de un servicio suele residir bajo `/etc`, mientras sus registros pueden encontrarse bajo `/var/log`. No deben confundirse configuración, datos de aplicación y temporales.

**Práctica guiada.** Localiza las seis rutas con `ls -ld`. Escoge un archivo de configuración y un registro de ejemplo y explica por qué se ubican allí. No leas ni publiques secretos.

**Actividad independiente.** Decide dónde ubicarías configuración, datos persistentes, caché y temporales de una aplicación propia; justifica la decisión y permisos requeridos.

**Criterios de aceptación.** Clasifica correctamente los seis directorios y distingue datos persistentes de temporales.

**Errores frecuentes.** Guardar datos importantes en `/tmp` o tratar `/usr` como directorio personal.

**Comprobación.** ¿Qué problema operativo surgiría si una aplicación guardara su única copia de datos en un directorio temporal?

### 7.2.7 — Usuarios

**Propósito y modelo.** Las cuentas locales representan identidades del sistema mediante UID, grupo principal, directorio personal, shell y otros atributos. El nombre es una etiqueta; el UID es el identificador numérico utilizado por el sistema. Las cuentas de servicio suelen limitarse a ejecutar procesos y no deberían usarse como cuentas interactivas generales.

**Ejemplo desarrollado.** Dos procesos iniciados por una misma cuenta comparten la identidad efectiva salvo que intervenga un mecanismo de cambio de credenciales. Los permisos de archivos se evalúan utilizando UID y grupos, no solo el nombre que aparece en una terminal.

**Práctica guiada.** Ejecuta `whoami`, `id` y `getent passwd "$(whoami)"`. Identifica UID, GID, grupos y shell sin divulgar datos de otras cuentas.

**Actividad independiente.** Diseña tres identidades para un servidor: administrador, operador de despliegue y servicio web. Define qué tareas necesita cada una y cuáles no debe poder realizar.

**Criterios de aceptación.** Interpreta UID/GID, distingue cuenta humana y de servicio y aplica mínimo privilegio.

**Errores frecuentes.** Compartir cuentas administrativas entre personas o ejecutar servicios como root sin necesidad.

**Comprobación.** ¿Por qué los permisos siguen funcionando aunque se cambie el nombre visible de una cuenta pero se conserve su UID?

### 7.2.8 — Grupos

**Propósito y modelo.** Los grupos permiten asignar permisos a conjuntos de cuentas. Cada usuario tiene un grupo principal y puede pertenecer a grupos suplementarios. La pertenencia a un grupo puede afectar el acceso a archivos, dispositivos y servicios, por lo que debe concederse según responsabilidades reales.

**Ejemplo desarrollado.** Un directorio de proyecto puede pertenecer al grupo `desarrollo` y permitir escritura al grupo, evitando que cada integrante necesite privilegios administrativos. El bit setgid en un directorio puede hacer que los archivos nuevos hereden el grupo del directorio, según el sistema de archivos y la configuración.

**Práctica guiada.** Consulta `id` y `getent group`. En un laboratorio propio, crea un directorio temporal y analiza cómo se representan propietario y grupo con `ls -ld`. No alteres grupos del sistema anfitrión.

**Actividad independiente.** Propón una matriz de acceso para un equipo de desarrollo con lectores, editores y administradores; asigna grupos y justifica cada permiso.

**Criterios de aceptación.** Diferencia grupo principal y suplementario y explica cómo se evalúan los permisos de grupo.

**Errores frecuentes.** Añadir usuarios a grupos privilegiados para resolver problemas puntuales o asumir que un cambio de grupo se aplica siempre a sesiones ya abiertas.

**Comprobación.** ¿Por qué los grupos simplifican la administración frente a asignar permisos individualmente a cada usuario?

### 7.2.9 — Permisos

**Propósito y modelo.** Los permisos Unix tradicionales definen lectura (r), escritura (w) y ejecución (x) para propietario, grupo y otros. En archivos, x permite ejecutar; en directorios, x permite atravesar/buscar entradas. ACL y bits especiales amplían el modelo. La máscara umask influye en los permisos iniciales de nuevos objetos.

**Ejemplo desarrollado.** El modo 640 significa propietario rw-, grupo r-- y otros ---; 750 significa propietario rwx, grupo r-x y otros ---. En un directorio, el permiso x es necesario para acceder a entradas aunque se conozca su nombre.

**Práctica guiada.** Crea un archivo temporal, aplica `chmod 640 archivo` y consulta `stat` y `ls -l`. Luego prueba 750 sobre un directorio de laboratorio y compara el efecto de r y x.

**Actividad independiente.** Define permisos mínimos para un archivo de configuración que solo el propietario debe editar y para un directorio compartido donde un grupo pueda listar y crear archivos.

**Criterios de aceptación.** Traduce modos octales a simbólicos, distingue permisos de archivo/directorio y justifica mínimo privilegio.

**Errores frecuentes.** Aplicar 777 como solución general o creer que r en un directorio permite siempre abrir archivos sin x.

**Comprobación.** ¿Por qué un usuario puede conocer el nombre de un archivo y aun así no poder acceder a él?

### 7.2.10 — Propietarios

**Propósito y modelo.** Cada objeto del sistema de archivos mantiene propietario de usuario y grupo. La propiedad determina qué clase de permisos se evalúa y puede influir en cuotas, auditoría y operaciones administrativas. El propietario actual no tiene que ser la persona que creó originalmente el archivo; una transferencia puede cambiarlo.

**Ejemplo desarrollado.** Un archivo creado por root dentro de un directorio de aplicación puede quedar inaccesible para el servicio si la propiedad y permisos no se ajustan a la cuenta de ejecución. Cambiar propietario indiscriminadamente puede abrir acceso o romper servicios.

**Práctica guiada.** Ejecuta `stat archivo` y `ls -ln archivo` en un objeto de laboratorio. Compara nombres resueltos con UID/GID numéricos.

**Actividad independiente.** Diseña la propiedad de un directorio de despliegue con una cuenta administradora, un grupo operativo y una cuenta de servicio de solo lectura.

**Criterios de aceptación.** Identifica propietario y grupo, explica su relación con permisos y justifica una asignación segura.

**Errores frecuentes.** Ejecutar `chown -R` sobre rutas amplias sin revisar alcance o confundir el propietario con el proceso que tiene abierto el archivo.

**Comprobación.** ¿Qué puede salir mal si se cambia recursivamente el propietario de todo un directorio de sistema?

### 7.2.11 — Root

**Propósito y modelo.** Root es la cuenta cuyo UID es 0 y posee privilegios administrativos amplios. No es simplemente un usuario normal con una contraseña fuerte. Los procesos con identidad efectiva root pueden modificar componentes críticos, por lo que el uso cotidiano debe limitarse y las tareas administrativas deben ser deliberadas y auditables.

**Ejemplo desarrollado.** Leer información pública o editar un archivo propio normalmente no requiere root; instalar paquetes, modificar configuración global o administrar servicios puede requerir elevación. El requisito depende de permisos y políticas concretas.

**Práctica guiada.** Ejecuta `id` y `whoami` en una cuenta ordinaria. Identifica qué operaciones del laboratorio funcionan sin elevación y no habilites acceso root remoto.

**Actividad independiente.** Clasifica diez tareas administrativas en: usuario normal, elevación puntual o privilegio administrativo continuo; justifica las excepciones.

**Criterios de aceptación.** Explica UID 0, mínimo privilegio y dos riesgos del uso permanente de root.

**Errores frecuentes.** Usar root para ejecutar cualquier aplicación o asumir que ocultar la cuenta root sustituye controles de acceso.

**Comprobación.** ¿Cómo reduce el principio de mínimo privilegio el impacto de un error o compromiso?

### 7.2.12 — Sudo

**Propósito y modelo.** sudo permite ejecutar órdenes con otra identidad, normalmente root, conforme a reglas de autorización. La política puede restringir usuarios, comandos, argumentos y contexto; las decisiones deben ser específicas y auditables. Una regla demasiado amplia puede equivaler a conceder administración completa.

**Ejemplo desarrollado.** Una persona autorizada puede ejecutar una operación administrativa puntual sin mantener una sesión root abierta. La autorización no debe inferirse por pertenecer a cualquier grupo: depende de la política sudoers efectiva.

**Práctica guiada.** Ejecuta `sudo -l` para inspeccionar los permisos de tu cuenta. En un entorno de laboratorio, consulta `man sudoers` y estudia el uso de `visudo`; no edites la política del host compartido.

**Actividad independiente.** Diseña una regla conceptual que permita reiniciar un servicio específico sin conceder shell root ni comandos arbitrarios. Identifica riesgos de rutas y argumentos.

**Criterios de aceptación.** Diferencia autenticación y autorización, interpreta una lista de permisos y explica por qué se utiliza visudo.

**Errores frecuentes.** Conceder `NOPASSWD: ALL` como solución rápida o editar sudoers directamente sin validación sintáctica.

**Comprobación.** ¿Por qué permitir ejecutar un editor como root puede equivaler a conceder privilegios mucho mayores que editar un archivo concreto?

### 7.2.13 — Procesos

**Propósito y modelo.** En Linux, la administración de procesos utiliza PID, señales, prioridades y herramientas de observación. Los estados incluyen ejecución, espera, detención y zombi. Una señal solicita una acción al proceso; no todas las señales pueden capturarse o ignorarse. Debes identificar el proceso y su propietario antes de actuar.

**Ejemplo desarrollado.** `pgrep -a sleep` localiza procesos por nombre, pero puede devolver procesos ajenos a la práctica. Por eso la actividad debe crear un proceso propio y guardar su PID para actuar únicamente sobre él.

**Práctica guiada.** En una shell Bash ejecuta `sleep 90 & pid=$!`, inspecciona `ps -p "$pid" -o pid,stat,cmd` y envía `kill -TERM "$pid"`. Comprueba el resultado con `kill -0 "$pid"` y consulta el código de salida.

**Actividad independiente.** Explica cuándo utilizarías SIGTERM y por qué SIGKILL debe reservarse para casos en que el proceso no responde.

**Criterios de aceptación.** Identifica el PID propio, interpreta estado y explica diferencia entre solicitud de terminación y terminación forzada.

**Errores frecuentes.** Matar por nombre sin verificar, usar PID obsoleto o terminar procesos de sistema para liberar recursos.

**Comprobación.** ¿Qué oportunidad ofrece SIGTERM que SIGKILL no ofrece?

### 7.2.14 — Servicios

**Propósito y modelo.** Un servicio es una función persistente o de larga duración administrada por el sistema. En muchas distribuciones actuales, systemd gestiona unidades, dependencias, activación y estados. Servicio, proceso y unidad no son sinónimos: una unidad puede representar servicios, sockets, timers y otros recursos.

**Ejemplo desarrollado.** Una unidad de servicio puede estar activa ahora pero no habilitada para iniciar automáticamente en el siguiente arranque. El estado activo describe ejecución; habilitado describe relación con el arranque o activación configurada.

**Práctica guiada.** Ejecuta `systemctl status` sobre un servicio no crítico y consulta `systemctl is-active nombre` y `systemctl is-enabled nombre`. No inicies, detengas ni habilites servicios del host.

**Actividad independiente.** Redacta un procedimiento de cambio para reiniciar un servicio de laboratorio: autorización, impacto, dependencias, ventana, reversión y verificación.

**Criterios de aceptación.** Diferencia servicio/proceso/unidad y activo/habilitado; interpreta estado y dependencias.

**Errores frecuentes.** Reiniciar servicios desconocidos o asumir que habilitar un servicio significa que está ejecutándose ahora.

**Comprobación.** ¿Puede un servicio estar activo pero deshabilitado para el siguiente arranque? Explica.

### 7.2.15 — Paquetes

**Propósito y modelo.** Un gestor de paquetes instala, actualiza y elimina software a partir de metadatos y repositorios, resolviendo dependencias y registrando archivos. APT se utiliza en Debian/Ubuntu; otros sistemas utilizan gestores diferentes. La confianza depende de repositorios, firmas, claves y configuración de origen.

**Ejemplo desarrollado.** `apt show paquete` presenta metadatos del paquete disponible; `apt-cache policy paquete` ayuda a identificar versiones candidatas y orígenes. Ninguno exige instalar el paquete.

**Práctica guiada.** Consulta información de un paquete conocido con `apt show` y `apt-cache policy`. Registra versión instalada, candidata y repositorio. No ejecutes actualizaciones globales en el host.

**Actividad independiente.** Describe un procedimiento seguro para evaluar e instalar una actualización en un servidor: respaldo, origen, changelog, dependencias, ventana, verificación y reversión.

**Criterios de aceptación.** Explica repositorio, paquete, dependencia y firma; interpreta la versión candidata y su origen.

**Errores frecuentes.** Instalar paquetes desde scripts o repositorios desconocidos, mezclar ramas o usar `apt upgrade -y` sin revisar impacto.

**Comprobación.** ¿Qué garantiza la firma de un repositorio y qué aspectos de seguridad no garantiza por sí sola?

### 7.2.16 — Logs

**Propósito y modelo.** Los logs registran eventos del sistema y aplicaciones. Pueden almacenarse en archivos, journal u otros sistemas centralizados. Su utilidad depende de marcas temporales, zona horaria, severidad, origen, retención y correlación. Los registros pueden contener datos personales o secretos y deben tratarse como información sensible.

**Ejemplo desarrollado.** Un evento de autenticación fallida aislado puede ser un error de usuario; una secuencia correlacionada por hora, cuenta y origen puede indicar un patrón. No concluyas que existe un incidente sin contexto adicional.

**Práctica guiada.** Consulta `journalctl -b -p warning` y limita la salida a un servicio de laboratorio con `journalctl -u nombre-servicio`. Resume un evento sin copiar tokens, direcciones privadas sensibles ni datos personales.

**Actividad independiente.** Construye una línea temporal con tres eventos sintéticos y explica qué campos permitirían correlacionarlos.

**Criterios de aceptación.** Identifica hora, origen, nivel y mensaje; distingue observación de inferencia y protege datos sensibles.

**Errores frecuentes.** Interpretar todo warning como fallo crítico, asumir que la ausencia de logs demuestra ausencia de actividad o borrar registros para liberar espacio.

**Comprobación.** ¿Por qué sincronización horaria y retención son importantes para investigar un incidente?

### 7.2.17 — Variables de entorno

**Propósito y modelo.** Las variables de entorno transmiten configuración a un proceso y, normalmente, a sus procesos hijos. Ejemplos comunes son PATH, LANG y variables específicas de aplicaciones. No son un almacén seguro de secretos por defecto: pueden filtrarse mediante procesos, diagnósticos, volcados o configuraciones.

**Ejemplo desarrollado.** Una variable asignada en una shell sin exportar está disponible para esa shell, pero no necesariamente para un proceso hijo. Al exportarla, se incorpora al entorno que recibe el subproceso.

**Práctica guiada.** En Bash ejecuta `APP_MODE=lab`, consulta `printenv APP_MODE`, luego ejecuta `export APP_MODE=lab` y vuelve a consultar. Lanza `sh -c 'printf "%s\\n" "$APP_MODE"'` y compara resultados.

**Actividad independiente.** Diseña cómo configurarías una aplicación por entorno (desarrollo/pruebas/producción) sin incluir credenciales en el repositorio ni imprimirlas en logs.

**Criterios de aceptación.** Diferencia variable de shell y variable exportada; explica herencia a procesos hijos y al menos dos riesgos al manejar secretos.

**Errores frecuentes.** Suponer que exportar una variable la hace persistente entre sesiones o que ocultar su valor en la terminal evita su exposición a otros mecanismos.

**Comprobación.** ¿Por qué una variable de entorno no debe considerarse automáticamente un gestor de secretos?

## 7.3 — Administración Linux

### 7.3.1 — pwd

**Propósito.** Confirmar el directorio de trabajo antes de ejecutar órdenes relativas. La ruta actual influye en el significado de nombres como `archivo.txt` y en el alcance de operaciones posteriores.

**Ejemplo.** `pwd -P` muestra la ruta física resolviendo enlaces simbólicos; `pwd -L` conserva, cuando es posible, la ruta lógica de la shell.

**Caso aplicado.** Antes de ejecutar una copia relativa, una persona comprueba la ruta actual y detecta que sigue dentro de /tmp en vez de su carpeta de proyecto. Detenerse y corregir el directorio evita escribir datos en una ubicación equivocada.

**Práctica guiada.** Ejecuta `pwd` en tu directorio personal y después de entrar en `/tmp`. Registra ambas salidas y compara con `pwd -P` si hay enlaces simbólicos.

**Actividad independiente.** Explica qué archivo afectaría una orden relativa si se ejecuta desde dos directorios distintos.

**Criterios de aceptación.** Distingue ruta absoluta y relativa y verifica el directorio antes de una operación de escritura.

**Error frecuente.** Ejecutar `rm` o `cp` suponiendo un directorio actual distinto del real.

**Pregunta de comprensión.** ¿Por qué conocer el directorio actual es un control preventivo antes de ejecutar una orden que modifica archivos?

### 7.3.2 — ls

**Propósito.** Inspeccionar nombres y metadatos sin modificar el contenido del directorio.

**Ejemplo.** `ls -lah` muestra entradas ocultas, permisos y tamaños legibles; `ls -ln` presenta UID/GID numéricos, útil cuando no hay resolución de nombres.

**Caso aplicado.** Un archivo de configuración no aparece en un listado normal porque su nombre comienza por punto. El listado con opción para entradas ocultas permite localizarlo sin cambiar atributos ni contenido.

**Práctica guiada.** En una carpeta de laboratorio compara `ls`, `ls -la` y `ls -lh`. Identifica permisos, enlaces, propietario, tamaño y fecha. No interpretes el tamaño de un directorio como suma recursiva de su contenido.

**Actividad independiente.** Documenta qué diferencias observas entre un archivo regular, un directorio y un enlace simbólico usando `ls -l`.

**Criterios de aceptación.** Interpreta los campos principales y explica por qué una entrada oculta no aparece en el listado simple.

**Error frecuente.** Tratar el tamaño mostrado para un directorio como el espacio total que consumen todos sus archivos.

**Pregunta de comprensión.** ¿Qué información adicional aporta un listado largo frente a mostrar solo nombres?

### 7.3.3 — cd

**Propósito.** Cambiar el directorio de trabajo de la shell y comprender cómo se resuelven las rutas.

**Ejemplo.** `cd ..` sube al directorio padre; `cd ~` entra al directorio personal; `cd -` vuelve al directorio anterior cuando la shell mantiene esa referencia.

**Caso aplicado.** Un script interactivo necesita cambiar de carpeta y continuar con rutas relativas. cd debe ejecutarse en la shell que mantiene el flujo, no en un subproceso que terminará sin cambiar el contexto del llamador.

**Práctica guiada.** Navega entre `/tmp`, `~` y una carpeta de laboratorio usando rutas absolutas y relativas. Confirma cada cambio con `pwd`.

**Actividad independiente.** Escribe una secuencia de comandos que llegue desde tu directorio personal a una carpeta hermana sin utilizar rutas absolutas.

**Criterios de aceptación.** Explica `.`, `..`, `~` y diferencia entre rutas absolutas y relativas.

**Error frecuente.** Suponer que `cd` puede cambiar el directorio de trabajo del proceso padre; se ejecuta como builtin porque la shell debe cambiar su propio estado.

**Pregunta de comprensión.** ¿Por qué cd es un builtin de shell y qué ocurriría si se ejecutara en un proceso hijo?

### 7.3.4 — mkdir

**Propósito.** Crear directorios con una estructura predecible y permisos adecuados.

**Ejemplo.** `mkdir -p ~/lab/etapa7/entrada` crea los componentes ausentes y no falla simplemente porque los directorios intermedios ya existan.

**Caso aplicado.** Un pipeline requiere separar archivos de entrada y resultados. Crear una jerarquía explícita evita mezclar archivos originales con productos generados y facilita aplicar permisos distintos.

**Práctica guiada.** Crea una jerarquía temporal con `mkdir -p` y verifica con `find` o `ls -R`. Inspecciona permisos iniciales y considera la umask.

**Actividad independiente.** Diseña una estructura para separar entradas, resultados y logs de un ejercicio; define quién debe poder escribir en cada carpeta.

**Criterios de aceptación.** Crea la estructura solicitada, verifica cada nivel y explica el efecto de `-p`.

**Error frecuente.** Crear directorios con permisos demasiado abiertos o utilizar rutas fuera del espacio de laboratorio.

**Pregunta de comprensión.** ¿Qué ventaja operativa aporta crear la estructura antes de iniciar un proceso automatizado?

### 7.3.5 — touch

**Propósito.** Crear archivos vacíos y modificar marcas temporales, comprendiendo que touch no escribe contenido.

**Ejemplo.** `touch nota.txt` crea el archivo si no existe; si existe, actualiza marcas temporales según opciones y permisos.

**Caso aplicado.** Una herramienta de compilación utiliza marcas temporales para decidir qué archivos necesitan reconstrucción. Cambiar timestamps puede alterar esa decisión aunque el contenido permanezca idéntico.

**Práctica guiada.** Crea un archivo temporal, consulta `stat nota.txt`, espera unos segundos y vuelve a ejecutar touch. Compara modificación y acceso, teniendo en cuenta las políticas de montaje.

**Actividad independiente.** Explica cómo diferenciar un archivo vacío recién creado de uno que contiene datos usando `stat` y `wc -c`.

**Criterios de aceptación.** Describe el efecto de touch sobre existencia y marcas temporales; demuestra que no añade contenido.

**Error frecuente.** Usar touch como si fuera un editor o asumir que todas las marcas temporales se actualizan idénticamente en cualquier sistema de archivos.

**Pregunta de comprensión.** ¿Por qué la fecha de modificación no demuestra por sí sola que el contenido de un archivo haya cambiado?

### 7.3.6 — cp

**Propósito.** Copiar archivos o directorios sin confundir copia de contenido con preservación completa de metadatos.

**Ejemplo.** `cp origen destino` copia un archivo; `cp -a arbol/ copia/` intenta preservar atributos y estructura de forma recursiva.

**Caso aplicado.** Antes de editar un archivo de configuración se crea una copia de trabajo. Comparar hashes permite comprobar igualdad de contenido, mientras los metadatos deben revisarse por separado.

**Práctica guiada.** Copia un archivo creado en el laboratorio y compara SHA-256 con `sha256sum`. Después copia un subdirectorio con `cp -a` y revisa permisos y marcas temporales.

**Actividad independiente.** Decide qué opción utilizarías para duplicar una carpeta de configuración y qué metadatos necesitas preservar.

**Criterios de aceptación.** Comprueba igualdad del contenido y explica cuándo se necesita copia recursiva o preservación de atributos.

**Error frecuente.** Sobrescribir el destino sin verificarlo o asumir que una copia simple conserva propietarios y permisos originales.

**Pregunta de comprensión.** ¿Por qué un hash coincidente no demuestra que propietario y permisos también sean iguales?

### 7.3.7 — mv

**Propósito.** Mover o renombrar entradas y comprender las diferencias entre operaciones dentro y entre sistemas de archivos.

**Ejemplo.** En el mismo sistema de archivos, mv suele cambiar la entrada de directorio; entre sistemas de archivos puede requerir copiar y eliminar, con implicaciones de metadatos y atomicidad.

**Caso aplicado.** Renombrar un archivo dentro del mismo volumen suele ser una operación de metadatos; moverlo a otro volumen puede implicar copia y eliminación. Para datos críticos, se verifica integridad antes de retirar el origen.

**Práctica guiada.** Renombra un archivo del laboratorio y muévelo a otra carpeta del mismo volumen. Verifica ruta, contenido y permisos antes y después.

**Actividad independiente.** Describe riesgos al mover un archivo grande entre volúmenes y plantea cómo verificar integridad tras la operación.

**Criterios de aceptación.** Distingue renombrar y mover, y verifica que el origen y destino son los esperados.

**Error frecuente.** Usar comodines sin revisar la expansión o asumir que el movimiento entre volúmenes es siempre una operación atómica.

**Pregunta de comprensión.** ¿Qué riesgo adicional aparece cuando un movimiento cruza sistemas de archivos?

### 7.3.8 — rm

**Propósito.** Eliminar entradas de forma controlada, comprendiendo que rm no proporciona una papelera ni una reversión sencilla.

**Ejemplo.** `rm archivo-temporal` elimina una entrada; `rm -r directorio-lab` recorre el árbol. `-f` suprime ciertas confirmaciones y errores, por lo que aumenta el riesgo de una equivocación.

**Caso aplicado.** Una variable de ruta vacía podría hacer que una orden de eliminación opere sobre un objetivo distinto del esperado. Un script robusto valida que la variable no esté vacía y que la ruta permanezca dentro del directorio permitido.

**Práctica guiada.** Crea un único archivo temporal, confirma la ruta con `pwd` y `ls -l` y elimina solo ese archivo. No utilices `sudo rm` ni `rm -rf` sobre rutas del sistema.

**Actividad independiente.** Diseña una rutina previa a la eliminación de un árbol: validar variable de ruta, mostrar objetivo, confirmar alcance y disponer de copia si corresponde.

**Criterios de aceptación.** Demuestra eliminación de un objeto creado para la práctica y explica por qué la verificación previa es esencial.

**Error frecuente.** Ejecutar una expansión de comodines o una variable vacía sin inspeccionar qué ruta terminará usando rm.

**Pregunta de comprensión.** ¿Qué controles deben preceder a una eliminación recursiva?

### 7.3.9 — find

**Propósito.** Buscar archivos y directorios mediante criterios de nombre, tipo, tamaño, tiempo y permisos.

**Ejemplo.** `find ~/lab -type f -name '*.log'` busca archivos regulares con esa extensión bajo el árbol de laboratorio. Las comillas evitan que la shell expanda el patrón antes de que find lo procese.

**Caso aplicado.** Un administrador busca archivos de log antiguos dentro de una carpeta de aplicación concreta. Limitar la ruta inicial evita recorrer sistemas de archivos ajenos al objetivo y reduce ruido y carga.

**Práctica guiada.** Crea tres archivos de prueba y localízalos por nombre y tipo. Añade `-print` explícitamente y observa cómo cambia la búsqueda al limitar la ruta inicial.

**Actividad independiente.** Construye una búsqueda que identifique archivos vacíos dentro de tu carpeta de práctica sin recorrer el resto del sistema.

**Criterios de aceptación.** Explica ruta inicial, expresión de búsqueda y tipo; evita búsquedas innecesariamente amplias.

**Error frecuente.** Ejecutar búsquedas desde `/` con privilegios elevados sin necesidad o olvidar citar patrones con comodines.

**Pregunta de comprensión.** ¿Por qué la ruta inicial es una decisión de seguridad y rendimiento?

### 7.3.10 — grep

**Propósito.** Filtrar líneas de texto que coinciden con patrones y comprender el alcance de las expresiones regulares.

**Ejemplo.** `grep -n 'ERROR' aplicación.log` muestra líneas coincidentes con número de línea. `-i` ignora mayúsculas/minúsculas y `-r` recorre directorios, con cuidado de no incluir datos sensibles.

**Caso aplicado.** Una investigación revisa registros anonimizados para encontrar mensajes de error. El patrón filtra líneas candidatas, pero no determina por sí solo la causa ni la gravedad del evento.

**Práctica guiada.** Crea un archivo de texto con líneas INFO, WARN y ERROR; filtra ERROR con `grep -n` y luego cuenta coincidencias con `grep -c`.

**Actividad independiente.** Diseña un patrón para localizar direcciones IPv4 en datos sintéticos y explica por qué una expresión regular simple no valida por completo todos los rangos posibles.

**Criterios de aceptación.** Explica patrón, coincidencia y código de salida; utiliza datos sintéticos y rutas delimitadas.

**Error frecuente.** Tratar grep como parser completo de formatos estructurados o asumir que ausencia de coincidencias equivale a error del comando.

**Pregunta de comprensión.** ¿Por qué una coincidencia de texto debe interpretarse en contexto y no como diagnóstico final?

### 7.3.11 — chmod

**Propósito.** Cambiar permisos de archivos y directorios de forma deliberada.

**Ejemplo.** `chmod 640 archivo` concede lectura/escritura al propietario, lectura al grupo y ningún permiso a otros. La forma simbólica `chmod u=rw,g=r,o= archivo` expresa la misma intención.

**Caso aplicado.** Una clave privada de laboratorio no debe ser legible por otros usuarios. Se establece un modo restrictivo y luego se inspecciona el resultado; no se amplían permisos para resolver fallos sin comprender el propietario.

**Práctica guiada.** Crea un archivo de prueba, aplica ambos modos en pasos separados y verifica con `stat`. En un directorio, compara el efecto de r y x sobre listar y atravesar.

**Actividad independiente.** Define permisos mínimos para una clave privada de laboratorio y para un directorio de trabajo compartido por un grupo.

**Criterios de aceptación.** Traduce octal/simbólico y justifica permisos de archivo frente a directorio.

**Error frecuente.** Aplicar 777 para resolver cualquier problema de acceso o cambiar permisos recursivamente sin revisar el árbol.

**Pregunta de comprensión.** ¿Por qué los permisos mínimos son preferibles a utilizar 777?

### 7.3.12 — chown

**Propósito.** Cambiar propietario y/o grupo cuando exista una necesidad administrativa legítima.

**Ejemplo.** `chown usuario:grupo archivo` asigna ambos atributos. La operación suele requerir privilegios; las reglas exactas para transferir propiedad dependen del sistema.

**Caso aplicado.** Un servicio no puede leer un archivo porque el propietario y grupo no corresponden a su identidad de ejecución. La corrección se limita al archivo necesario y se documenta antes de cualquier operación recursiva.

**Práctica guiada.** Inspecciona propietario y grupo con `stat` y `ls -ln`. En un laboratorio desechable, si dispones de autorización, cambia la propiedad de un archivo creado para la práctica y vuelve a verificar. Si no tienes permisos, documenta el error sin elevar privilegios.

**Actividad independiente.** Diseña un plan de corrección de propiedad para un directorio de aplicación, incluyendo alcance, respaldo, identidad de servicio y validación.

**Criterios de aceptación.** Distingue usuario y grupo propietarios y demuestra que comprende el impacto de un cambio recursivo.

**Error frecuente.** Aplicar `chown -R` sobre rutas amplias o usarlo como sustituto de comprender los permisos.

**Pregunta de comprensión.** ¿Por qué una corrección de propietario debe delimitar el alcance con precisión?

### 7.3.13 — ps

**Propósito.** Obtener una instantánea de procesos y sus atributos principales.

**Ejemplo.** `ps -ef` presenta procesos en formato amplio; `ps -p PID -o pid,ppid,stat,etime,cmd` permite inspeccionar una instancia concreta. La salida refleja un instante, no un historial continuo.

**Caso aplicado.** Una aplicación inicia varios procesos con nombres similares. Inspeccionar PID, PPID, propietario y comando completo permite identificar la instancia pertinente antes de tomar una acción.

**Práctica guiada.** Inicia `sleep 60 & pid=$!` y consulta únicamente ese PID con ps. Registra PID, PPID, estado y tiempo transcurrido; termina el proceso propio al finalizar.

**Actividad independiente.** Compara dos formatos de ps y explica qué campos ayudan a identificar relación padre-hijo y estado.

**Criterios de aceptación.** Interpreta PID/PPID/STAT y reconoce que la salida es una instantánea.

**Error frecuente.** Elegir un proceso por nombre sin comprobar PID, propietario y comando completo.

**Pregunta de comprensión.** ¿Por qué un nombre de proceso no es un identificador suficiente?

### 7.3.14 — top

**Propósito.** Observar dinámicamente carga de CPU, memoria y procesos para formular hipótesis de rendimiento.

**Ejemplo.** top actualiza periódicamente estadísticas; el porcentaje de CPU depende del número de núcleos y de la forma de cálculo. La vista es una observación, no un diagnóstico completo de causa.

**Caso aplicado.** Una alerta indica CPU elevada. top ayuda a observar el patrón en tiempo real, pero la hipótesis debe contrastarse con métricas históricas, I/O y comportamiento esperado de la aplicación.

**Práctica guiada.** Ejecuta `top` durante un periodo corto. Identifica carga, procesos con mayor consumo y memoria disponible. Sal con q y no cambies prioridades ni finalices procesos desde la herramienta.

**Actividad independiente.** Describe qué mediciones adicionales recopilarías para distinguir saturación de CPU, espera de I/O y presión de memoria.

**Criterios de aceptación.** Interpreta al menos tres indicadores y separa observación de hipótesis causal.

**Error frecuente.** Considerar load average como porcentaje de CPU o asumir que el proceso que aparece arriba es necesariamente la causa raíz.

**Pregunta de comprensión.** ¿Qué diferencia existe entre observar correlación temporal y demostrar causalidad?

### 7.3.15 — kill

**Propósito.** Enviar señales a procesos identificados y distinguir solicitud de terminación de terminación forzada.

**Ejemplo.** `kill -TERM PID` solicita terminación ordenada; `kill -KILL PID` fuerza al kernel a terminar el proceso y no permite que este gestione la señal. No debe actuarse sobre PID desconocidos.

**Caso aplicado.** Un proceso propio de laboratorio deja de responder. SIGTERM permite que intente cerrar archivos y liberar recursos; SIGKILL queda como último recurso cuando la terminación ordenada no funciona.

**Práctica guiada.** En Bash crea `sleep 90 & pid=$!`, verifica el PID y envía SIGTERM a esa instancia. Comprueba su salida. No utilices killall ni pkill sobre procesos generales.

**Actividad independiente.** Explica cuándo una aplicación necesita liberar archivos o guardar estado antes de salir y qué implica recibir SIGKILL.

**Criterios de aceptación.** Identifica el proceso propio, utiliza SIGTERM y explica las limitaciones de SIGKILL.

**Error frecuente.** Enviar señales a PID reutilizados u obtenerlos de una lista antigua sin volver a verificarlos.

**Pregunta de comprensión.** ¿Qué tareas de limpieza puede realizar un proceso al recibir SIGTERM que no puede realizar al recibir SIGKILL?

### 7.3.16 — systemctl

**Propósito.** Consultar y administrar unidades gestionadas por systemd, diferenciando observación de modificación.

**Ejemplo.** `systemctl status servicio` muestra estado y detalles; `is-active` consulta ejecución y `is-enabled` consulta habilitación para arranque/activación. `start`, `stop` y `enable` modifican el sistema.

**Caso aplicado.** Un servicio figura habilitado pero está detenido. Consultar por separado is-enabled e is-active evita confundir configuración de arranque con estado operativo actual.

**Práctica guiada.** Consulta el estado de un servicio no crítico con `systemctl status`, `systemctl is-active` y `systemctl is-enabled`. No cambies su estado en el host.

**Actividad independiente.** Redacta una secuencia segura para reiniciar un servicio de laboratorio, incluyendo autorización, dependencias, ventana y comprobación posterior.

**Criterios de aceptación.** Distingue consulta de cambio y activo de habilitado; identifica nombre de unidad.

**Error frecuente.** Ejecutar `systemctl restart` sobre un servicio desconocido sin evaluar impacto.

**Pregunta de comprensión.** ¿Puede una unidad estar habilitada y no estar activa? Explica por qué.

### 7.3.17 — journalctl

**Propósito.** Consultar el journal de systemd para investigar eventos por arranque, unidad, prioridad y tiempo.

**Ejemplo.** `journalctl -b` muestra registros del arranque actual; `journalctl -u servicio` filtra por unidad; `-p warning` limita por prioridad. La disponibilidad y persistencia del journal dependen de la configuración.

**Caso aplicado.** Una aplicación falla al iniciar. Filtrar el journal por unidad y ventana temporal reduce ruido; correlacionar mensajes con cambios recientes permite formular hipótesis que luego deben probarse.

**Práctica guiada.** Consulta `journalctl -b -p warning` y luego filtra por un servicio de laboratorio. Registra timestamp, unidad, prioridad y mensaje, ocultando datos sensibles.

**Actividad independiente.** Construye una línea temporal a partir de eventos sintéticos y explica qué evidencia adicional necesitas para confirmar una causa.

**Criterios de aceptación.** Aplica al menos dos filtros, interpreta los campos y distingue evento observado de conclusión.

**Error frecuente.** Suponer que journalctl contiene todos los eventos históricos o que un warning equivale a un incidente.

**Pregunta de comprensión.** ¿Qué limitaciones tiene investigar un fallo utilizando solo una línea de log?

### 7.3.18 — df

**Propósito.** Medir capacidad y espacio disponible de sistemas de archivos montados.

**Ejemplo.** `df -h` presenta tamaños legibles; `df -i` muestra uso de inodos. Un volumen puede quedarse sin inodos aunque todavía informe espacio en bytes.

**Caso aplicado.** Una aplicación no puede crear archivos pese a que df muestra espacio libre. Revisar inodos y punto de montaje ayuda a identificar límites que no se ven al observar únicamente bytes disponibles.

**Práctica guiada.** Ejecuta `df -hT` y `df -i`. Identifica punto de montaje, tipo de sistema de archivos, capacidad, usado y disponible. No llenes volúmenes para probar límites.

**Actividad independiente.** Explica dos causas por las que una aplicación puede fallar al crear archivos aunque `df -h` muestre espacio disponible.

**Criterios de aceptación.** Interpreta capacidad y punto de montaje; diferencia espacio en bytes de inodos.

**Error frecuente.** Confundir uso de un directorio con uso de todo el sistema de archivos o interpretar tamaños redondeados como valores exactos.

**Pregunta de comprensión.** ¿Cómo puede agotarse la capacidad de crear archivos sin agotar los bytes del volumen?

### 7.3.19 — du

**Propósito.** Estimar cuánto espacio ocupa un árbol de archivos desde la perspectiva de sus entradas.

**Ejemplo.** `du -sh ~/lab` resume el uso del directorio; `du -h --max-depth=1 ruta` compara subdirectorios. El resultado depende de enlaces, archivos dispersos y unidades de asignación.

**Caso aplicado.** Un directorio de logs crece rápidamente. du ayuda a localizar subdirectorios con mayor consumo, pero antes de borrar se debe identificar el servicio propietario, la política de retención y si los archivos siguen abiertos.

**Práctica guiada.** Crea archivos de distintos tamaños en una carpeta de prueba y compara `du -sh` con `ls -lh`. No uses directorios del sistema como objetivo de limpieza.

**Actividad independiente.** Investiga por qué la suma de tamaños aparentes de archivos puede diferir del espacio asignado que muestra du o del espacio disponible que muestra df.

**Criterios de aceptación.** Distingue tamaño aparente, bloques asignados y espacio del volumen; limita el análisis a una ruta autorizada.

**Error frecuente.** Borrar archivos grandes basándose solo en du sin identificar qué proceso o servicio los necesita.

**Pregunta de comprensión.** ¿Por qué localizar el mayor directorio no autoriza automáticamente a eliminar su contenido?

### 7.3.20 — mount

**Propósito.** Comprender cómo un sistema de archivos se incorpora al árbol de directorios y qué controles rodean el montaje.

**Ejemplo.** `findmnt` consulta montajes existentes; `mount` sin argumentos suele listar montajes. Montar un dispositivo requiere identificar correctamente origen, tipo y punto de montaje, y puede alterar qué contenido queda visible en esa ruta.

**Caso aplicado.** Un volumen de datos se monta sobre un directorio que ya contiene archivos. El contenido previo queda oculto mientras el montaje está activo, lo que puede confundir a procesos y operadores.

**Práctica guiada.** Ejecuta `findmnt` y `mount` en modo de consulta. Identifica un punto de montaje, su origen y opciones. No montes ni desmontes dispositivos del host durante esta práctica.

**Actividad independiente.** Diseña un procedimiento para montar un volumen de laboratorio: identificar dispositivo, revisar sistema de archivos, crear punto de montaje, aplicar opciones seguras, verificar y desmontar de forma controlada.

**Criterios de aceptación.** Explica origen, tipo y punto de montaje; interpreta una entrada de findmnt y reconoce riesgos de montaje/desmontaje.

**Error frecuente.** Desmontar un volumen ocupado o montar un dispositivo no verificado sobre una ruta que contiene datos importantes.

**Pregunta de comprensión.** ¿Qué puede ocurrir si se monta un volumen sobre una ruta que ya contiene datos?

## 7.4 — Bash

### 7.4.1 — Variables

**Desarrollo conceptual.** Las variables de Bash contienen cadenas y se expanden antes de ejecutar una orden. La asignación no admite espacios alrededor del signo igual; las comillas controlan separación de palabras y expansión de comodines. Una variable no se hereda por procesos hijos salvo que se exporte.

**Ejemplo técnico.** nombre="servidor de pruebas"; printf '%s\n' "$nombre" conserva el espacio como parte de un solo valor. Sin comillas, el shell puede dividir el resultado en varias palabras.

**Práctica guiada.** Asigna una variable con espacios, imprímela con printf y compárala con su versión exportada en un proceso hijo. Usa valores sintéticos.

**Actividad independiente.** Diseña una validación que compruebe que una variable requerida no está vacía sin imprimir su contenido.

**Criterios de aceptación.** Distingue asignación, expansión y exportación; conserva espacios mediante quoting.

**Errores frecuentes.** Poner espacios alrededor de =, olvidar comillas o asumir que exportar hace persistente la variable entre sesiones.

**Comprobación.** ¿Qué diferencia existe entre una variable de shell y una variable exportada al entorno?

### 7.4.2 — Operadores

**Desarrollo conceptual.** Bash ofrece pruebas condicionales, aritmética y operadores de control. [[ ... ]] evalúa condiciones de shell; (( ... )) evalúa expresiones aritméticas. La sintaxis y reglas de expansión no son intercambiables con [ ... ].

**Ejemplo técnico.** [[ -f "$archivo" ]] comprueba archivo regular; (( contador += 1 )) incrementa una variable numérica.

**Práctica guiada.** Prueba condiciones para archivo existente, directorio y variable vacía dentro de tu carpeta de laboratorio.

**Actividad independiente.** Valida un argumento entero no negativo y define cómo rechazar entradas vacías, negativas o no numéricas.

**Criterios de aceptación.** Elige el operador apropiado y prueba casos verdaderos, falsos y límite.

**Errores frecuentes.** Confundir sintaxis de prueba o evaluar entrada no confiable mediante eval.

**Comprobación.** ¿Por qué [[ ... ]] suele ser preferible a [ ... ] en scripts Bash nuevos?

### 7.4.3 — Condicionales

**Desarrollo conceptual.** if, elif y else seleccionan ramas según el estado de salida de una orden o expresión. En shell, cero representa éxito y cualquier valor distinto de cero indica una condición no exitosa.

**Ejemplo técnico.** Un script comprueba [[ -d "$ruta" ]] antes de listar una carpeta; si no existe, informa por stderr y termina con estado distinto de cero.

**Práctica guiada.** Escribe un bloque que distinga directorio válido, ruta inexistente y ruta que no es directorio.

**Actividad independiente.** Añade una comprobación de permiso de lectura y explica el efecto de no tener permiso de búsqueda en un directorio padre.

**Criterios de aceptación.** Prueba cada rama y comprueba los códigos de salida.

**Errores frecuentes.** Tratar cualquier cadena no vacía como éxito o ignorar fallos de comandos internos.

**Comprobación.** ¿Por qué el código de salida de una orden no es lo mismo que el texto que imprime?

### 7.4.4 — Bucles

**Desarrollo conceptual.** for recorre listas o expansiones; while repite mientras una condición tenga éxito; until repite hasta que la condición tenga éxito. El quoting evita que los espacios dividan elementos.

**Ejemplo técnico.** for elemento in "${lista[@]}"; do ...; done conserva cada elemento de un array como unidad.

**Práctica guiada.** Recorre tres nombres sintéticos, uno con espacios, e imprime cada elemento delimitado por corchetes.

**Actividad independiente.** Procesa un archivo de laboratorio línea por línea sin perder espacios ni interpretar barras invertidas.

**Criterios de aceptación.** El bucle procesa todos los elementos y tiene una condición de terminación explícita.

**Errores frecuentes.** Usar for x in $(cat archivo) para leer líneas o crear un ciclo infinito por no actualizar su condición.

**Comprobación.** ¿Qué ventaja ofrece while IFS= read -r linea para procesar texto?

### 7.4.5 — Funciones

**Desarrollo conceptual.** Las funciones agrupan órdenes reutilizables y reciben argumentos posicionales. "$@" conserva cada argumento por separado. return devuelve un estado numérico; la salida textual se comunica por stdout.

**Ejemplo técnico.** validar_directorio() { [[ -d "$1" ]]; } devuelve éxito cuando el primer argumento es un directorio.

**Práctica guiada.** Implementa la función y pruébala con una ruta válida y otra inexistente.

**Actividad independiente.** Crea una función que valide dos argumentos, escriba errores en stderr y no cambie el sistema si falta alguno.

**Criterios de aceptación.** Maneja argumentos, espacios y códigos de retorno correctamente.

**Errores frecuentes.** Usar return con texto o expandir $@ sin comillas.

**Comprobación.** ¿Cuándo conviene devolver un código de estado y cuándo imprimir un resultado?

### 7.4.6 — Arrays

**Desarrollo conceptual.** Los arrays indexados almacenan secuencias; los asociativos relacionan claves y valores. Las expansiones [@] y [*] difieren especialmente al utilizar comillas. Los arrays asociativos requieren Bash compatible.

**Ejemplo técnico.** servicios=("web" "base de datos"); recorrer "${servicios[@]}" mantiene dos elementos distintos.

**Práctica guiada.** Crea un array con tres valores, uno con espacios; imprime cada elemento y el total usando ${#servicios[@]}.

**Actividad independiente.** Representa un inventario pequeño con array asociativo y comprueba la existencia de cada clave.

**Criterios de aceptación.** Conserva límites de elementos y explica la diferencia entre arrays indexados y asociativos.

**Errores frecuentes.** Confundir [*] con [@] en expansión citada o asumir que POSIX sh ofrece arrays Bash.

**Comprobación.** ¿Por qué importa citar "${array[@]}" cuando un elemento contiene espacios?

### 7.4.7 — Pipes

**Desarrollo conceptual.** Una pipe conecta stdout de un proceso con stdin de otro. Las etapas se ejecutan como pipeline y pueden fallar independientemente. Por defecto, el estado suele reflejar la última orden, salvo configuración pipefail.

**Ejemplo técnico.** printf '%s\n' alfa beta | grep beta | wc -l compone generación, filtrado y conteo.

**Práctica guiada.** Ejecuta el pipeline y compara el estado cuando una etapa intermedia falla, primero sin pipefail y luego con set -o pipefail.

**Actividad independiente.** Construye un pipeline que filtre eventos sintéticos y conserve evidencia de fallos en las etapas.

**Criterios de aceptación.** Identifica productor, consumidor, flujo de datos y efecto de pipefail.

**Errores frecuentes.** Creer que stderr viaja automáticamente por la pipe o ignorar fallos intermedios.

**Comprobación.** ¿Qué fallo podría quedar oculto si solo se consulta el estado de la última orden?

### 7.4.8 — Redirecciones

**Desarrollo conceptual.** Los descriptores habituales son stdin 0, stdout 1 y stderr 2. > trunca, >> añade, 2> redirige errores y 2>&1 duplica un descriptor según el orden de evaluación.

**Ejemplo técnico.** comando >salida.txt 2>errores.txt separa flujos; comando >todo.txt 2>&1 los dirige al mismo destino.

**Práctica guiada.** Usa una orden inocua con salida normal y un error controlado; guarda cada flujo en un archivo temporal separado.

**Actividad independiente.** Explica cómo dirigir stdout y stderr a un único archivo y predice el resultado al invertir el orden de redirección.

**Criterios de aceptación.** Identifica descriptores y predice el destino de cada flujo.

**Errores frecuentes.** Sobrescribir archivos importantes o asumir que 2>&1 >archivo equivale a >archivo 2>&1.

**Comprobación.** ¿Por qué el orden de las redirecciones cambia el resultado?

### 7.4.9 — Exit codes

**Desarrollo conceptual.** El código de salida comunica el resultado de una orden: cero suele indicar éxito y valores distintos de cero indican fallo o condición especial. $? contiene el estado de la última orden y debe guardarse inmediatamente.

**Ejemplo técnico.** grep puede devolver 0 si encuentra coincidencias, 1 si no encuentra y otro valor si ocurre un error.

**Práctica guiada.** Prueba una orden válida, una búsqueda sin coincidencias y una ruta inexistente; captura cada estado inmediatamente.

**Actividad independiente.** Diseña un script que distinga éxito, ausencia de datos y error operativo.

**Criterios de aceptación.** Interpreta los estados y no sobrescribe el valor antes de utilizarlo.

**Errores frecuentes.** Consultar $? después de ejecutar otra orden o tratar todos los estados no cero como idénticos.

**Comprobación.** ¿Por qué debe guardarse inmediatamente el código de salida?

### 7.4.10 — Scripts

**Desarrollo conceptual.** Un script es un archivo de órdenes interpretado. Debe declarar el intérprete, validar entradas, citar variables, gestionar errores y devolver un estado útil. set -e tiene excepciones y no sustituye el manejo explícito.

**Ejemplo técnico.** Un script recibe una ruta, comprueba cantidad de argumentos y valida [[ -d "$1" ]] antes de operar.

**Práctica guiada.** Crea un script Bash con shebang y validación de argumento; pruébalo con ruta válida, argumento ausente y ruta inexistente.

**Actividad independiente.** Añade logging con timestamp y manejo de error a una operación inocua dentro de una carpeta temporal.

**Criterios de aceptación.** Gestiona casos válidos e inválidos, espacios y exit code.

**Errores frecuentes.** No citar variables, ocultar errores o suponer que set -e detiene todos los fallos.

**Comprobación.** ¿Qué debe comprobarse antes de usar una variable de entrada en una ruta?

### 7.4.11 — Cron

**Desarrollo conceptual.** cron programa tareas periódicas mediante cinco campos: minuto, hora, día del mes, mes y día de semana. El entorno suele ser reducido y puede diferir de una sesión interactiva. Zona horaria, PATH y disponibilidad del daemon afectan la ejecución.

**Ejemplo técnico.** 0 2 * * 1 representa las 02:00 cada lunes según el daemon y la zona horaria configurada.

**Práctica guiada.** Interpreta expresiones de ejemplo sin instalarlas en el host; consulta tu tabla personal si existe.

**Actividad independiente.** Diseña una tarea de respaldo para laboratorio con frecuencia, retención, logging, manejo de errores y prevención de solapamiento.

**Criterios de aceptación.** Interpreta cinco campos y explica diferencias entre entorno cron y terminal.

**Errores frecuentes.** Asumir que cron hereda PATH interactivo o ignorar zona horaria y solapamientos.

**Comprobación.** ¿Por qué una orden que funciona en terminal puede fallar bajo cron?

### 7.4.12 — Automatización

**Desarrollo conceptual.** La automatización fiable combina repetibilidad, idempotencia, registros, manejo de errores, control de concurrencia y mínimo privilegio. Una tarea debe permitir detectar fallos sin exponer secretos.

**Ejemplo técnico.** Crear un directorio si no existe y escribir un registro fechado es idempotente respecto a la creación de la carpeta.

**Práctica guiada.** Diseña un script que cree una carpeta de reportes si falta y registre timestamp; ejecútalo dos veces en un entorno de práctica.

**Actividad independiente.** Propón una comprobación automática de espacio en disco que alerte al superar un umbral sin borrar archivos ni cambiar servicios.

**Criterios de aceptación.** Explica idempotencia, registra resultado y evita privilegios innecesarios.

**Errores frecuentes.** Automatizar acciones destructivas sin dry-run, ignorar concurrencia o guardar contraseñas en texto plano.

**Comprobación.** ¿Qué propiedad permite repetir una tarea sin duplicar efectos no deseados?

## 7.5 — Windows

### 7.5.1 — Arquitectura de Windows

**Propósito y modelo.** Windows separa ejecución en modo usuario y modo kernel. El kernel, el ejecutivo y los controladores gestionan recursos con privilegios elevados; las aplicaciones ordinarias utilizan APIs y llamadas al sistema. El aislamiento entre procesos, los tokens de acceso y los límites de privilegios reducen el impacto de errores, aunque no sustituyen actualizaciones ni configuración segura.

**Ejemplo desarrollado.** Una aplicación gráfica puede crear procesos auxiliares y servicios. Cerrar su ventana no garantiza que todos terminen; el Administrador de tareas permite observar procesos, usuarios, consumo y relaciones, pero finalizar procesos del sistema puede causar pérdida de datos o inestabilidad.

**Práctica guiada.** En un equipo autorizado, consulta Configuración > Sistema > Acerca de y el Administrador de tareas. Registra edición, versión, arquitectura y tres procesos de usuario. Usa `Get-ComputerInfo` para obtener información del sistema sin cambiar configuración.

**Actividad independiente.** Dibuja el flujo conceptual de una aplicación que solicita leer un archivo: proceso en modo usuario, API, comprobación de identidad/permisos y acceso al sistema de archivos.

**Criterios de aceptación.** Diferencia modo usuario/kernel, proceso/servicio y arquitectura/edición; sustenta los datos con la versión observada.

**Errores frecuentes.** Suponer que cada ventana equivale a un proceso, que x64 identifica la edición o que un proceso con nombre conocido es necesariamente legítimo.

**Comprobación.** ¿Qué aporta la separación entre modo usuario y modo kernel?

**Laboratorio de profundización — Mapa de componentes y límites de privilegio.**

1. Identifica versión, edición y arquitectura con `Get-ComputerInfo`. 2. Dibuja una aplicación, sus procesos, APIs y el kernel como capas conceptuales. 3. Marca qué operaciones requieren privilegios elevados y por qué.

**Evidencia esperada.** El diagrama diferencia modo usuario y modo kernel, proceso y servicio, y relaciona elevación con una operación concreta.

**Seguridad y límites.** No finalizar procesos críticos ni cambiar configuración de seguridad durante la observación.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.2 — Sistema de archivos NTFS

**Propósito y modelo.** NTFS organiza archivos y directorios mediante metadatos, ACL, journaling, enlaces y otras funciones. La seguridad depende de propietario, permisos explícitos y heredados, grupos y contexto de acceso. Para recursos SMB se evalúan además los permisos de uso compartido; el acceso remoto efectivo puede quedar más restringido que el acceso local.

**Ejemplo desarrollado.** Una cuenta puede tener lectura NTFS local y no poder leer por red porque el permiso de uso compartido limita el acceso. También puede existir una denegación explícita o una herencia desde un directorio superior.

**Práctica guiada.** Crea una carpeta de laboratorio y abre Propiedades > Seguridad > Opciones avanzadas. Registra propietario, entradas ACL y estado de herencia. Consulta `icacls ruta` desde PowerShell o CMD. No alteres carpetas del sistema.

**Actividad independiente.** Diseña dos escenarios de acceso —local y SMB— para una carpeta de informes y determina qué permisos deben revisarse en cada uno.

**Criterios de aceptación.** Diferencia ACL NTFS y permisos SMB, identifica herencia y explica cómo verificar el acceso efectivo.

**Errores frecuentes.** Conceder Control total para resolver un problema de lectura, deshabilitar herencia sin analizar el impacto o aplicar ACL recursivas a una ruta amplia.

**Comprobación.** ¿Por qué una ACL NTFS no basta para describir el acceso a un recurso compartido?

**Laboratorio de profundización — Evaluación de ACL local frente a recurso compartido.**

1. Crea una carpeta temporal. 2. Consulta sus ACL con `icacls`. 3. Inspecciona propietario y herencia desde Propiedades > Seguridad > Opciones avanzadas. 4. Explica cómo cambiaría el análisis si la carpeta se compartiera por SMB.

**Evidencia esperada.** La explicación diferencia ACL NTFS de permisos de recurso compartido e identifica herencia y propietario.

**Seguridad y límites.** No aplicar ACL recursivas ni modificar permisos de carpetas del sistema o de otros usuarios.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.3 — Usuarios y grupos

**Propósito y modelo.** Windows identifica cuentas mediante SID, no solo por el nombre visible. Las cuentas locales, de dominio y de servicio tienen ámbitos y usos distintos. Los grupos simplifican asignación de derechos, pero pertenecer a Administradores, Remote Desktop Users u otros grupos sensibles amplía la superficie de impacto.

**Ejemplo desarrollado.** Cambiar el nombre de una cuenta no equivale a crear otra identidad si el SID permanece igual. Un grupo puede recibir permiso sobre una carpeta y los miembros heredan ese acceso mediante su token de seguridad.

**Práctica guiada.** Ejecuta `whoami /user` y `whoami /groups`. En PowerShell consulta `Get-LocalUser` y `Get-LocalGroup` si tu edición y permisos lo permiten. No habilites ni deshabilites cuentas.

**Actividad independiente.** Diseña grupos para operadores, desarrolladores y auditores; asigna permisos por función y explica por qué no deben compartir cuentas.

**Criterios de aceptación.** Distingue nombre, SID, usuario y grupo; justifica mínimo privilegio y reconoce diferencias entre cuenta local y de dominio.

**Errores frecuentes.** Usar Administradores como grupo general, compartir credenciales o asumir que cambiar el nombre cambia el SID.

**Comprobación.** ¿Qué ventaja aporta un SID para identificar una cuenta de forma estable?

**Laboratorio de profundización — Inventario de identidad y pertenencia.**

1. Ejecuta `whoami /user` y `whoami /groups`. 2. Consulta cuentas locales con `Get-LocalUser` si está disponible. 3. Compara nombre visible, SID y grupos del token. 4. Diseña una matriz de funciones para operador, desarrollador y auditor.

**Evidencia esperada.** Se explica que el SID identifica la cuenta y que los permisos pueden llegar por pertenencia a grupos.

**Seguridad y límites.** No agregar cuentas a grupos privilegiados ni compartir credenciales.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.4 — Permisos

**Propósito y modelo.** Los permisos de Windows se expresan mediante entradas de control de acceso (ACE) dentro de una DACL. Pueden conceder o denegar derechos y heredarse desde directorios superiores. El resultado depende del token de seguridad, grupos, orden y alcance de las ACE; no se debe inferir solo por el nombre de un usuario.

**Ejemplo desarrollado.** Una cuenta puede recibir lectura por pertenecer a un grupo y escritura por otra ACE. Una denegación explícita aplicable puede impedir una operación aunque exista una concesión más general. El acceso efectivo debe probarse con identidad y contexto representativos.

**Práctica guiada.** En una carpeta temporal abre Seguridad > Opciones avanzadas y registra permisos, herencia y ámbito. Consulta `icacls .` para observar la representación textual. No cambies permisos de carpetas compartidas.

**Actividad independiente.** Crea una matriz de acceso para propietario, grupo de edición y grupo de solo lectura. Indica qué permisos requieren y cómo probarías cada caso.

**Criterios de aceptación.** Explica ACE, DACL y herencia; diferencia lectura, modificación y control total con un ejemplo.

**Errores frecuentes.** Desactivar herencia sin documentar, conceder control total indiscriminadamente o creer que el nombre mostrado prueba la identidad real.

**Comprobación.** ¿Por qué la pertenencia a varios grupos puede cambiar el acceso efectivo?

**Laboratorio de profundización — Matriz de acceso y herencia.**

1. En una carpeta de laboratorio inspecciona las ACE con `icacls`. 2. Registra concesiones, denegaciones y herencia. 3. Diseña permisos para propietario, editores y lectores. 4. Indica cómo comprobarías el acceso con cuentas representativas.

**Evidencia esperada.** La matriz asigna solo los permisos necesarios y explica cómo la pertenencia a grupos afecta el acceso efectivo.

**Seguridad y límites.** No deshabilitar herencia ni conceder Control total para resolver una prueba de lectura.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.5 — Procesos

**Propósito y modelo.** Un proceso es una instancia de programa con espacio de direcciones, identificador, token de seguridad y recursos. Los hilos ejecutan dentro del proceso; los servicios pueden iniciar procesos no interactivos. PID y nombre no bastan para decidir si un proceso es legítimo: revisa ruta, firma, editor, usuario, padre y comportamiento.

**Ejemplo desarrollado.** Dos procesos pueden compartir el mismo nombre de ejecutable pero provenir de rutas distintas. La ruta y firma digital aportan contexto, aunque ninguna observación aislada demuestra legitimidad.

**Práctica guiada.** En Administrador de tareas abre Detalles y agrega columnas de PID, nombre de usuario y línea de comandos si está disponible. En PowerShell consulta `Get-Process | Select-Object -First 10 Id,ProcessName,CPU`. No finalices procesos desconocidos.

**Actividad independiente.** Analiza un caso sintético de proceso sospechoso y enumera evidencia que recopilarías antes de contenerlo: hash, ruta, firma, padre, conexiones y usuario.

**Criterios de aceptación.** Diferencia proceso e hilo, interpreta PID y explica por qué nombre y consumo no son evidencia suficiente.

**Errores frecuentes.** Finalizar procesos críticos por su nombre o confundir un proceso legítimo con otro que suplanta su nombre.

**Comprobación.** ¿Qué atributos revisarías antes de concluir que un proceso es malicioso?

**Laboratorio de profundización — Triage observacional de un proceso.**

1. En Administrador de tareas agrega PID, usuario y línea de comandos. 2. Consulta procesos con `Get-Process`. 3. Para un caso sintético registra ruta, hash, firma, proceso padre y conexiones que investigarías. 4. Separa hechos de hipótesis.

**Evidencia esperada.** El análisis no declara malicioso un proceso por su nombre o consumo; identifica evidencia adicional necesaria.

**Seguridad y límites.** No finalizar procesos desconocidos ni ejecutar muestras sospechosas.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.6 — Servicios

**Propósito y modelo.** Los servicios de Windows son componentes de larga duración administrados por Service Control Manager. Pueden ejecutarse con cuentas específicas, iniciar bajo demanda o durante el arranque y depender de otros servicios. Su estado, tipo de inicio, cuenta y ruta ejecutable deben revisarse antes de cualquier cambio.

**Ejemplo desarrollado.** Un servicio detenido puede estar configurado como Manual o Deshabilitado; cambiar su estado de inicio no lo ejecuta inmediatamente. Un servicio que corre como LocalSystem tiene privilegios amplios y merece especial atención.

**Práctica guiada.** Abre `services.msc` y consulta nombre, estado, tipo de inicio y cuenta de un servicio conocido. En PowerShell utiliza `Get-Service` para inspección. No detengas ni modifiques servicios del host.

**Actividad independiente.** Elabora un procedimiento de cambio para reiniciar un servicio de laboratorio, con impacto, dependencias, autorización, ventana, rollback y verificación.

**Criterios de aceptación.** Diferencia estado y tipo de inicio; identifica cuenta de servicio y dependencias.

**Errores frecuentes.** Deshabilitar servicios por listas genéricas de internet o cambiar la cuenta de ejecución sin validar permisos y dependencias.

**Comprobación.** ¿Por qué la cuenta con la que se ejecuta un servicio forma parte de su superficie de seguridad?

**Laboratorio de profundización — Inventario de servicios y cuenta de ejecución.**

1. Inspecciona un servicio conocido en `services.msc`. 2. Consulta su estado y configuración con `Get-Service` y `Get-CimInstance Win32_Service`. 3. Registra cuenta, ruta, tipo de inicio y dependencias. 4. Diseña un cambio con reversión, sin aplicarlo.

**Evidencia esperada.** Se distinguen estado, tipo de inicio, cuenta y dependencia del servicio.

**Seguridad y límites.** No detener servicios del host ni cambiar la cuenta de ejecución durante la práctica.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.7 — Registro de Windows

**Propósito y modelo.** El Registro es una base jerárquica de configuración del sistema, usuarios y aplicaciones. Sus raíces lógicas incluyen HKLM y HKCU; las vistas de 32/64 bits pueden diferir en determinadas rutas. Las claves y valores pueden estar protegidos por ACL y cambios incorrectos pueden impedir el inicio o funcionamiento de componentes.

**Ejemplo desarrollado.** Una preferencia por usuario suele residir en HKCU; una configuración de equipo suele encontrarse en HKLM. La ubicación exacta depende de la aplicación y de sus convenciones, no de una regla universal.

**Práctica guiada.** Abre Regedit solo para inspección y navega a una clave documentada no crítica. Consulta una clave equivalente con `Get-ItemProperty` en PowerShell. No cambies valores ni importes archivos .reg.

**Actividad independiente.** Documenta una clave de configuración de una aplicación de prueba: ruta, valor, tipo, ámbito y procedimiento de respaldo/restauración.

**Criterios de aceptación.** Distingue hive, clave, valor y tipo; explica HKCU/HKLM y el riesgo de editar directamente.

**Errores frecuentes.** Borrar claves por nombre desconocido, asumir que el Registro es una carpeta o importar archivos .reg sin revisar su contenido.

**Comprobación.** ¿Qué diferencia existe entre una clave del Registro y un valor almacenado en ella?

**Laboratorio de profundización — Inspección de clave sin modificación.**

1. Abre Regedit en modo de consulta. 2. Identifica una clave no crítica documentada y registra ruta, valor y tipo. 3. Consulta el valor con `Get-ItemProperty`. 4. Especifica respaldo y restauración hipotéticos antes de cualquier cambio.

**Evidencia esperada.** Se diferencia hive, clave, valor y tipo, y se reconoce el riesgo de importar archivos `.reg`.

**Seguridad y límites.** No editar ni borrar claves; no importar archivos de registro de origen no verificado.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.8 — Administrador de tareas

**Propósito y modelo.** El Administrador de tareas ofrece una vista operativa de procesos, rendimiento, aplicaciones de inicio, usuarios y servicios. Sus métricas son instantáneas o agregados y dependen del intervalo de muestreo; no reemplazan registros ni herramientas de diagnóstico profundo.

**Ejemplo desarrollado.** Un proceso que muestra CPU elevada durante un intervalo puede ser una tarea legítima. Antes de concluir que existe un problema se correlaciona duración, tendencia, memoria, disco, usuario y actividad esperada.

**Práctica guiada.** Abre Rendimiento y Detalles. Registra CPU, memoria, disco y PID de un proceso de usuario durante dos observaciones separadas. No finalices tareas ni deshabilites elementos de inicio.

**Actividad independiente.** Construye un diagnóstico preliminar para un equipo lento y separa observaciones, hipótesis y pruebas adicionales.

**Criterios de aceptación.** Interpreta al menos tres métricas y distingue medición puntual de tendencia.

**Errores frecuentes.** Finalizar procesos del sistema para bajar consumo o atribuir causalidad a la primera fila de una lista ordenada.

**Comprobación.** ¿Qué datos adicionales necesitas antes de atribuir lentitud a un proceso específico?

**Laboratorio de profundización — Observación de rendimiento con dos muestras.**

1. Registra CPU, memoria y disco en dos momentos separados. 2. Identifica un proceso de usuario y registra PID, usuario y consumo. 3. Formula dos hipótesis alternativas para una lentitud simulada. 4. Propón qué telemetría adicional permitiría distinguirlas.

**Evidencia esperada.** El diagnóstico separa mediciones, tendencias e hipótesis y no atribuye causalidad a una sola instantánea.

**Seguridad y límites.** No finalizar procesos ni deshabilitar aplicaciones de inicio para reducir métricas.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.9 — Visor de eventos

**Propósito y modelo.** Event Viewer centraliza registros de Windows como Application, Security y System, además de canales específicos. Cada evento puede incluir proveedor, Event ID, nivel, timestamp, equipo y detalles. Un ID aislado no define por sí mismo un incidente; debe correlacionarse con contexto y otros eventos.

**Ejemplo desarrollado.** Un evento de inicio de sesión fallido debe analizarse con cuenta, tipo de inicio, origen, hora y secuencia. La ausencia de un evento no prueba que la acción no ocurrió: la auditoría puede no estar habilitada o el registro haber rotado.

**Práctica guiada.** Abre `eventvwr.msc`, consulta Application y System y filtra un intervalo breve. En PowerShell utiliza `Get-WinEvent -LogName System -MaxEvents 10`. No exportes registros con datos sensibles.

**Actividad independiente.** Analiza tres eventos sintéticos y crea una línea temporal; marca hechos observados, correlaciones e hipótesis.

**Criterios de aceptación.** Identifica proveedor, ID, nivel y hora; explica límites de una interpretación basada en un único evento.

**Errores frecuentes.** Buscar un ID en internet y asumir que cualquier coincidencia indica compromiso, o borrar logs para resolver problemas de almacenamiento.

**Comprobación.** ¿Por qué la correlación temporal y contextual es necesaria al investigar eventos?

**Laboratorio de profundización — Línea temporal de eventos sintéticos.**

1. Consulta Application y System en `eventvwr.msc`. 2. Filtra un intervalo breve. 3. Extrae proveedor, Event ID, nivel y timestamp de tres eventos no sensibles. 4. Correlaciónalos con un conjunto de eventos sintéticos y marca qué conclusiones no pueden sostenerse.

**Evidencia esperada.** La línea temporal distingue observación, correlación e hipótesis y explica límites de la ausencia de eventos.

**Seguridad y límites.** No borrar logs ni exportar registros con datos personales o secretos.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.10 — Firewall

**Propósito y modelo.** Microsoft Defender Firewall aplica reglas de filtrado según perfil de red, dirección, protocolo, puerto, programa y alcance. Las reglas de entrada y salida responden a flujos distintos. Desactivar el firewall completo para resolver conectividad elimina una capa de defensa y no es un método de diagnóstico aceptable.

**Ejemplo desarrollado.** Una aplicación cliente puede iniciar conexiones salientes mientras un servidor requiere una regla de entrada específica. La regla debe limitarse a los perfiles y orígenes necesarios, con registro y revisión periódica.

**Práctica guiada.** Inspecciona perfiles y estado con `Get-NetFirewallProfile` y lista reglas habilitadas con `Get-NetFirewallRule -Enabled True`. No deshabilites perfiles ni abras puertos en el equipo anfitrión.

**Actividad independiente.** Diseña una regla hipotética para permitir un servicio de laboratorio desde una subred autorizada; especifica dirección, protocolo, puerto, perfil, origen y justificación.

**Criterios de aceptación.** Distingue perfiles, tráfico entrante/saliente y alcance; aplica el principio de mínima exposición en el diseño.

**Errores frecuentes.** Crear reglas Any/Any, habilitar reglas en todos los perfiles o apagar el firewall como primera medida.

**Comprobación.** ¿Por qué restringir el origen de una regla puede reducir el riesgo sin impedir el servicio esperado?

**Laboratorio de profundización — Diseño de regla de mínima exposición.**

1. Inspecciona perfiles con `Get-NetFirewallProfile`. 2. Lista reglas habilitadas. 3. Diseña una regla hipotética de entrada con programa, protocolo, puerto, origen y perfil delimitados. 4. Explica cómo comprobarías conectividad y registro sin desactivar el firewall.

**Evidencia esperada.** La regla limita origen y alcance al servicio necesario y diferencia tráfico entrante de saliente.

**Seguridad y límites.** No deshabilitar perfiles ni abrir puertos en el host; aplicar cambios solo en laboratorio autorizado.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.11 — PowerShell

**Propósito y modelo.** PowerShell es una shell y lenguaje de automatización basado en objetos .NET. Los cmdlets siguen normalmente el patrón Verbo-Sustantivo y devuelven objetos, no solo texto. La canalización pasa objetos entre comandos; convertir todo a cadenas demasiado pronto dificulta filtrar y seleccionar propiedades.

**Ejemplo desarrollado.** `Get-Service | Where-Object Status -eq 'Running' | Select-Object -First 5 Name,Status` filtra servicios activos y selecciona propiedades. El resultado es una colección de objetos con campos.

**Práctica guiada.** Ejecuta `Get-Process | Select-Object -First 5 Name,Id` y consulta el tipo con `Get-Member`. Prueba `Get-Help Get-Service -Examples` si la ayuda está disponible.

**Actividad independiente.** Construye un pipeline que liste servicios detenidos sin cambiarlos y exporte un reporte CSV a una carpeta de laboratorio.

**Criterios de aceptación.** Explica cmdlet, objeto y pipeline; filtra y selecciona propiedades sin ejecutar cambios administrativos.

**Errores frecuentes.** Tratar PowerShell como CMD, usar `Format-Table` a mitad de un pipeline destinado a procesamiento o ejecutar scripts descargados sin inspección.

**Comprobación.** ¿Qué ventaja ofrece transportar objetos frente a transportar solo texto en la canalización?

**Laboratorio de profundización — Pipeline de objetos y reporte.**

1. Ejecuta `Get-Service` y examina el resultado con `Get-Member`. 2. Filtra servicios detenidos con `Where-Object`. 3. Selecciona propiedades con `Select-Object`. 4. Exporta el resultado a CSV dentro de una carpeta de laboratorio.

**Evidencia esperada.** El pipeline conserva objetos hasta la etapa de presentación y el CSV contiene las columnas previstas.

**Seguridad y límites.** No utilizar `Format-Table` antes de una etapa que necesita objetos ni ejecutar scripts externos sin inspección.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.

### 7.5.12 — Administración de servicios

**Propósito y modelo.** La administración segura de servicios requiere identificar el servicio real, su ejecutable, cuenta, dependencias, tipo de inicio, recuperación y efecto sobre usuarios. Los cambios deben seguir control de cambios y contar con rollback. El nombre visible puede diferir del nombre interno utilizado por herramientas.

**Ejemplo desarrollado.** `Get-Service` muestra estado y nombre; `Get-CimInstance Win32_Service` permite consultar cuenta, ruta y modo de inicio. Una ruta ejecutable con permisos de escritura para usuarios no privilegiados puede representar un riesgo, pero debe validarse junto con ACL y firma.

**Práctica guiada.** Consulta un servicio no crítico con `Get-CimInstance Win32_Service -Filter "Name='Spooler'"` si está disponible. Registra Name, State, StartMode, StartName y PathName; no cambies valores.

**Actividad independiente.** Redacta un cambio controlado para modificar el inicio de un servicio de laboratorio, incluyendo precondiciones, autorización, respaldo de configuración, impacto y reversión.

**Criterios de aceptación.** Diferencia nombre interno/visible, estado/tipo de inicio y reconoce el contexto de seguridad de la cuenta.

**Errores frecuentes.** Deshabilitar servicios en lote, modificar rutas o cuentas sin comprobar ACL y dependencias, y no documentar cómo revertir el cambio.

**Comprobación.** ¿Qué elementos deben verificarse antes de cambiar el tipo de inicio de un servicio?


**Laboratorio de profundización — Procedimiento de cambio con rollback.**

1. Selecciona un servicio no crítico de un laboratorio Windows. 2. Registra Name, State, StartMode, StartName y PathName con CIM. 3. Documenta autorización, precondiciones, impacto y método de reversión. 4. Realiza el cambio solo en VM desechable y con snapshot, si la práctica está autorizada.

**Evidencia esperada.** El procedimiento incluye evidencia anterior y posterior, comprobación del servicio y un rollback verificable; si no se ejecuta, queda identificado como diseño.

**Seguridad y límites.** No modificar servicios del equipo anfitrión ni asumir que un nombre visible identifica de forma única el servicio.

**Registro sugerido.** Anota edición y versión de Windows, comando o herramienta, resultado observado, fecha y cualquier diferencia. No declares ejecutada la práctica sin evidencia real.
## 7.6 — Virtualización

### 7.6.1 — VirtualBox

**Propósito y modelo.** VirtualBox es un hipervisor alojado que ejecuta invitados sobre un host. Una VM define firmware, CPU virtual, memoria, controladoras, discos y adaptadores. Las capacidades dependen de versión, plataforma y extensiones; no se debe asumir que una opción documentada para otra versión está disponible.

**Ejemplo desarrollado.** Asignar 8 GB a una VM no reserva necesariamente memoria física exclusiva, pero reduce el margen del host. La configuración debe mantener recursos suficientes para ambos sistemas.

**Práctica guiada.** Con una VM apagada, registra versión de VirtualBox, sistema invitado, RAM, vCPU, controladora de almacenamiento y adaptadores. No alteres máquinas compartidas.

**Actividad independiente.** Diseña una VM Linux de laboratorio con recursos moderados, disco virtual expansible y red aislada. Justifica cada ajuste.

**Criterios de aceptación.** Distingue host e invitado, identifica recursos virtuales y sustenta la configuración según versión.

**Errores frecuentes.** Asignar todos los recursos al invitado, confundir disco virtual con disco físico dedicado o asumir que Guest Additions es obligatorio.

**Comprobación.** ¿Por qué una VM puede degradar el host aunque el invitado parezca disponer de recursos suficientes?

**Laboratorio de profundización — Diseño de una VM reproducible.**

1. Registra versión de VirtualBox y sistema anfitrión. 2. Diseña una VM Linux con RAM y vCPU moderadas. 3. Define disco virtual expansible, firmware y controladora. 4. Justifica el modo de red y los recursos reservados al host.

**Evidencia esperada.** La ficha identifica host, invitado, versión y recursos; conserva margen suficiente para el host.

**Seguridad y límites.** No modificar VMs compartidas. No descargar imágenes de sitios no oficiales ni ejecutar appliances sin revisar su procedencia.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.2 — VMware

**Propósito y modelo.** VMware comprende productos distintos, como Workstation, Fusion y plataformas de hipervisor para centros de datos. Compatibilidad, licenciamiento, formatos de VM y redes varían por producto y versión; identifica el producto exacto antes de seguir un procedimiento.

**Ejemplo desarrollado.** Una VM puede abrirse en dos productos y requerir actualización del hardware virtual. La conversión debe realizarse sobre una copia y con respaldo.

**Práctica guiada.** Identifica producto, versión, host y formato de VM de un entorno autorizado. Inspecciona CPU, memoria, discos y redes sin modificar máquinas ajenas.

**Actividad independiente.** Compara dos productos VMware mediante documentación oficial de sus versiones: plataforma, gestión, redes, compatibilidad y licencia.

**Criterios de aceptación.** Identifica producto y versión, documenta fuentes y explica una diferencia relevante.

**Errores frecuentes.** Aplicar instrucciones de ESXi a Workstation, asumir licencias equivalentes o actualizar hardware virtual sin comprobar compatibilidad.

**Comprobación.** ¿Qué datos deben conocerse antes de importar una VM creada en otro producto VMware?

**Laboratorio de profundización — Identificación de producto y compatibilidad.**

1. Identifica el producto VMware exacto y versión. 2. Consulta su documentación oficial. 3. Registra formato de VM, hardware virtual, redes y compatibilidad. 4. Diseña un plan de conversión basado en una copia, sin actualizar la VM original.

**Evidencia esperada.** El análisis no mezcla instrucciones de productos distintos y documenta compatibilidades que deben verificarse.

**Seguridad y límites.** No convertir ni actualizar hardware virtual sin respaldo y comprobación de compatibilidad.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.3 — Máquinas virtuales

**Propósito y modelo.** Una VM presenta hardware abstraído al sistema invitado y comparte recursos físicos mediante el hipervisor. Incluye CPU virtual, memoria, firmware, controladoras, discos y dispositivos. El aislamiento ayuda, pero no es una frontera absoluta: existen redes, carpetas compartidas, portapapeles, dispositivos y vulnerabilidades del hipervisor.

**Ejemplo desarrollado.** Cuatro vCPU no equivalen necesariamente a cuatro núcleos físicos reservados; la carga concurrente y la sobreasignación influyen en el rendimiento.

**Práctica guiada.** Dibuja host–hipervisor–invitado y registra recursos virtuales de una VM apagada. Identifica qué recursos se comparten.

**Actividad independiente.** Diseña una topología cliente-servidor con dos VMs, recursos, límites de comunicación y mecanismo de respaldo.

**Criterios de aceptación.** Explica abstracción, asignación y límites del aislamiento.

**Errores frecuentes.** Considerar la VM independiente del host o asignar recursos sin medir carga agregada.

**Comprobación.** ¿Qué recursos comparte el hipervisor y cuáles administra el invitado?

**Laboratorio de profundización — Mapa de recursos y límites de aislamiento.**

1. Dibuja host, hipervisor y dos invitados. 2. Registra vCPU, RAM, disco, adaptadores y dispositivos compartidos. 3. Marca recursos sobreasignados y canales de integración. 4. Diseña una topología cliente-servidor con reglas mínimas.

**Evidencia esperada.** El diagrama diferencia recursos virtuales de físicos y señala límites de aislamiento y vías de comunicación.

**Seguridad y límites.** No conectar invitados vulnerables a redes productivas ni compartir carpetas o portapapeles sin necesidad.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.4 — Snapshots

**Propósito y modelo.** Un snapshot registra un estado de VM, habitualmente disco y opcionalmente memoria. Permite volver a un punto anterior, pero no equivale a un respaldo independiente: puede depender de discos base y cadenas diferenciales. Retener snapshots consume almacenamiento y complica consolidación.

**Ejemplo desarrollado.** Revertir descarta cambios posteriores incluidos en el estado restaurado. Un respaldo externo protege ante pérdida del datastore o del host; un snapshot junto a la VM no.

**Práctica guiada.** Inspecciona snapshots de una VM de laboratorio y registra fecha, descripción y espacio ocupado. No reviertas ni elimines snapshots compartidos.

**Actividad independiente.** Diseña política de creación, autorización, retención, espacio y respaldo independiente.

**Criterios de aceptación.** Diferencia snapshot y backup; explica reversión y riesgo de retención prolongada.

**Errores frecuentes.** Usar snapshots como única copia o borrar manualmente archivos de la cadena.

**Comprobación.** ¿Qué pérdida de datos no resolvería un snapshot almacenado junto a la VM?

**Laboratorio de profundización — Política de snapshot y respaldo.**

1. Inspecciona snapshots de una VM de laboratorio. 2. Registra fecha, descripción, cadena y almacenamiento ocupado. 3. Diseña política de creación, retención y consolidación. 4. Identifica un backup independiente del datastore.

**Evidencia esperada.** La política explica reversión, consumo, dependencia de discos base y recuperación ante pérdida del host.

**Seguridad y límites.** No borrar archivos de snapshot manualmente. No utilizar snapshots como única copia de seguridad.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.5 — Recursos virtualizados

**Propósito y modelo.** CPU, memoria, almacenamiento, GPU y E/S se presentan al invitado mediante abstracciones y controladores virtuales. Capacidad configurada no equivale siempre a reserva física; importan límites, reservas, sobreasignación, NUMA y carga concurrente.

**Ejemplo desarrollado.** Una VM con 16 GB virtuales puede no tener 16 GB dedicados si existe asignación dinámica o sobrecompromiso. Bajo presión, el host puede intercambiar páginas y degradar varias VMs.

**Práctica guiada.** Registra vCPU, RAM, tamaño del disco y controladoras. Compara configuración con uso durante una carga moderada, sin saturar el host.

**Actividad independiente.** Dimensiona dos VMs simultáneas en un host limitado y conserva margen para el host.

**Criterios de aceptación.** Distingue capacidad configurada, asignada y utilizada; identifica riesgos de sobreasignación.

**Errores frecuentes.** Sumar recursos virtuales como si fueran exclusivos o ignorar espacio para snapshots.

**Comprobación.** ¿Por qué aumentar vCPU no garantiza acelerar una aplicación?

**Laboratorio de profundización — Dimensionamiento con margen del host.**

1. Registra RAM, CPU y almacenamiento disponibles en el host. 2. Propón recursos para dos invitados simultáneos. 3. Calcula el margen que conserva el host. 4. Identifica efectos de sobreasignación y presión de memoria.

**Evidencia esperada.** El dimensionamiento distingue capacidad configurada, asignada y utilizada; no supone que vCPU equivalen a núcleos dedicados.

**Seguridad y límites.** No saturar el host para probar límites ni asignar toda la memoria disponible a los invitados.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.6 — Redes virtuales

**Propósito y modelo.** El hipervisor proporciona switches, bridges y adaptadores que conectan invitados entre sí, con el host o con redes externas. La topología define dominios de broadcast, rutas, acceso y aislamiento. El modo se elige según el objetivo del laboratorio.

**Ejemplo desarrollado.** Una red interna puede conectar dos VMs sin acceso a la LAN; una red puente expone el invitado como equipo de esa LAN, ampliando su superficie de ataque.

**Práctica guiada.** Inspecciona la red de una VM apagada y dibuja host, adaptador, switch y destino. No conectes laboratorios vulnerables a redes productivas.

**Actividad independiente.** Diseña una red de dos VMs con segmentación, acceso mínimo y administración separada.

**Criterios de aceptación.** Explica tres modos de conectividad y justifica uno según la práctica.

**Errores frecuentes.** Confundir NAT con aislamiento total o conectar máquinas vulnerables en modo puente a una LAN real.

**Comprobación.** ¿Qué propiedad se pierde al conectar directamente una VM vulnerable a la red física?

**Laboratorio de profundización — Diagrama comparativo de modos de red.**

1. Dibuja NAT, puente y red interna/Host-only. 2. Identifica qué nodos se alcanzan en cada modo. 3. Especifica DHCP, gateway, rutas y firewall. 4. Selecciona el modo adecuado para un laboratorio aislado.

**Evidencia esperada.** El diagrama representa conectividad y justifica el modo según objetivo y exposición.

**Seguridad y límites.** No utilizar modo puente para invitados vulnerables en una LAN real. No confundir NAT con aislamiento completo.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.7 — NAT

**Propósito y modelo.** En modo NAT, el hipervisor traduce tráfico de la VM para utilizar conectividad del host. El invitado suele iniciar conexiones salientes; las entrantes requieren reenvío de puertos u otro mecanismo. NAT no sustituye firewall ni garantiza aislamiento entre todas las VMs.

**Ejemplo desarrollado.** Una VM descarga actualizaciones, pero un equipo externo no inicia conexión al servicio invitado sin una regla de reenvío y permisos de firewall.

**Práctica guiada.** Revisa la configuración NAT de una VM apagada. Si el laboratorio está autorizado, verifica conectividad saliente y registra gateway y dirección. No publiques puertos a Internet.

**Actividad independiente.** Diseña un reenvío local temporal con interfaz, puerto host, puerto invitado, duración y procedimiento de retirada.

**Criterios de aceptación.** Distingue tráfico entrante y saliente y explica límites de NAT.

**Errores frecuentes.** Creer que NAT vuelve invulnerable al invitado o dejar redirecciones amplias permanentes.

**Comprobación.** ¿Por qué puede funcionar una conexión saliente mientras la entrante no está disponible?

**Laboratorio de profundización — Flujo de conexión saliente y entrante.**

1. Dibuja una VM que inicia una conexión saliente a través de NAT. 2. Explica por qué una conexión entrante no se establece automáticamente. 3. Diseña un reenvío local hipotético con puerto, interfaz, origen y duración. 4. Define cómo retirar la regla.

**Evidencia esperada.** Se diferencia traducción saliente y reenvío de puertos, y se limita el alcance de cualquier regla propuesta.

**Seguridad y límites.** No publicar puertos administrativos a Internet ni dejar redirecciones temporales permanentes.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.8 — Host-only

**Propósito y modelo.** Host-only conecta el host con una o varias VMs mediante una red virtual que normalmente no se enruta a la red física. Es útil para administración y prácticas aisladas. El alcance depende de DHCP, rutas, firewall y plataforma.

**Ejemplo desarrollado.** El host administra una VM por Host-only sin que esta tenga Internet. Si se agrega una interfaz NAT, la VM puede obtener salida externa por esa segunda interfaz.

**Práctica guiada.** Inspecciona adaptador Host-only y registra subred, DHCP y dirección del host. Dibuja nodos alcanzables sin modificar rutas del host.

**Actividad independiente.** Diseña dos VMs administrables desde el host sin acceso a la LAN externa; indica reglas y pruebas de aislamiento.

**Criterios de aceptación.** Describe nodos comunicables y explica cómo una segunda interfaz cambia el alcance.

**Errores frecuentes.** Suponer aislamiento total aunque existan otras interfaces o rutas.

**Comprobación.** ¿Qué debes revisar si una VM Host-only también tiene una interfaz NAT?

**Laboratorio de profundización — Comprobación conceptual de aislamiento.**

1. Inspecciona la subred y adaptador Host-only. 2. Dibuja host y dos invitados. 3. Define qué conexiones deberían funcionar. 4. Analiza cómo cambiaría el alcance si una VM añadiera otra interfaz NAT o puente.

**Evidencia esperada.** El diseño identifica el dominio privado y explica que una segunda interfaz puede habilitar otra ruta de comunicación.

**Seguridad y límites.** No asumir que Host-only aísla una VM si existen interfaces adicionales, rutas o servicios compartidos.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.

### 7.6.9 — Adaptadores de red virtuales

**Propósito y modelo.** El adaptador virtual conecta la interfaz del invitado con el switch o modo de red del hipervisor. Deben revisarse modelo, estado conectado, MAC, VLAN, DHCP, rutas, DNS y firewall. El controlador del invitado influye en la conectividad.

**Ejemplo desarrollado.** La interfaz puede aparecer conectada en el hipervisor y no obtener IP porque DHCP no responde o falta el controlador. Una MAC duplicada puede causar conflictos de capa 2.

**Práctica guiada.** Con una VM apagada registra modelo, MAC y modo de red. Dentro del invitado consulta `ip addr` o `ipconfig /all` y correlaciona dirección, gateway y DNS. No clones MAC en redes compartidas.

**Actividad independiente.** Diagnostica un enlace activo sin IP y ordena comprobaciones: adaptador, switch, DHCP, VLAN, controlador, firewall y rutas.

**Criterios de aceptación.** Distingue enlace y conectividad IP; identifica MAC, IP, gateway y DNS.

**Errores frecuentes.** Cambiar varios parámetros simultáneamente o asumir que «conectado» significa que DHCP y rutas funcionan.

**Comprobación.** ¿Qué evidencias separan un problema de enlace de uno de DHCP o rutas?


**Laboratorio de profundización — Diagnóstico por capas de conectividad.**

1. Registra tipo de adaptador, MAC y modo de red. 2. Dentro del invitado consulta `ip addr` o `ipconfig /all`. 3. Comprueba enlace, dirección IP, gateway y DNS por separado. 4. Construye un árbol de diagnóstico para fallo de enlace, DHCP, VLAN, ruta o resolución DNS.

**Evidencia esperada.** El diagnóstico separa conectividad de enlace, configuración IP, enrutamiento y DNS; documenta evidencia de cada capa.

**Seguridad y límites.** No clonar MAC en redes compartidas ni cambiar varias variables a la vez durante el diagnóstico.

**Registro sugerido.** Anota hipervisor y versión, configuración observada, diagrama, comandos o pantallas consultadas y diferencias respecto del diseño. No marques la práctica como ejecutada sin evidencia real.
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
