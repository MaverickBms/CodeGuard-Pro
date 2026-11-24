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

**Práctica guiada.** Ejecuta `pwd` en tu directorio personal y después de entrar en `/tmp`. Registra ambas salidas y compara con `pwd -P` si hay enlaces simbólicos.

**Actividad independiente.** Explica qué archivo afectaría una orden relativa si se ejecuta desde dos directorios distintos.

**Criterios de aceptación.** Distingue ruta absoluta y relativa y verifica el directorio antes de una operación de escritura.

**Error frecuente.** Ejecutar `rm` o `cp` suponiendo un directorio actual distinto del real.

### 7.3.2 — ls

**Propósito.** Inspeccionar nombres y metadatos sin modificar el contenido del directorio.

**Ejemplo.** `ls -lah` muestra entradas ocultas, permisos y tamaños legibles; `ls -ln` presenta UID/GID numéricos, útil cuando no hay resolución de nombres.

**Práctica guiada.** En una carpeta de laboratorio compara `ls`, `ls -la` y `ls -lh`. Identifica permisos, enlaces, propietario, tamaño y fecha. No interpretes el tamaño de un directorio como suma recursiva de su contenido.

**Actividad independiente.** Documenta qué diferencias observas entre un archivo regular, un directorio y un enlace simbólico usando `ls -l`.

**Criterios de aceptación.** Interpreta los campos principales y explica por qué una entrada oculta no aparece en el listado simple.

**Error frecuente.** Tratar el tamaño mostrado para un directorio como el espacio total que consumen todos sus archivos.

### 7.3.3 — cd

**Propósito.** Cambiar el directorio de trabajo de la shell y comprender cómo se resuelven las rutas.

**Ejemplo.** `cd ..` sube al directorio padre; `cd ~` entra al directorio personal; `cd -` vuelve al directorio anterior cuando la shell mantiene esa referencia.

**Práctica guiada.** Navega entre `/tmp`, `~` y una carpeta de laboratorio usando rutas absolutas y relativas. Confirma cada cambio con `pwd`.

**Actividad independiente.** Escribe una secuencia de comandos que llegue desde tu directorio personal a una carpeta hermana sin utilizar rutas absolutas.

**Criterios de aceptación.** Explica `.`, `..`, `~` y diferencia entre rutas absolutas y relativas.

**Error frecuente.** Suponer que `cd` puede cambiar el directorio de trabajo del proceso padre; se ejecuta como builtin porque la shell debe cambiar su propio estado.

### 7.3.4 — mkdir

**Propósito.** Crear directorios con una estructura predecible y permisos adecuados.

**Ejemplo.** `mkdir -p ~/lab/etapa7/entrada` crea los componentes ausentes y no falla simplemente porque los directorios intermedios ya existan.

**Práctica guiada.** Crea una jerarquía temporal con `mkdir -p` y verifica con `find` o `ls -R`. Inspecciona permisos iniciales y considera la umask.

**Actividad independiente.** Diseña una estructura para separar entradas, resultados y logs de un ejercicio; define quién debe poder escribir en cada carpeta.

**Criterios de aceptación.** Crea la estructura solicitada, verifica cada nivel y explica el efecto de `-p`.

**Error frecuente.** Crear directorios con permisos demasiado abiertos o utilizar rutas fuera del espacio de laboratorio.

### 7.3.5 — touch

**Propósito.** Crear archivos vacíos y modificar marcas temporales, comprendiendo que touch no escribe contenido.

**Ejemplo.** `touch nota.txt` crea el archivo si no existe; si existe, actualiza marcas temporales según opciones y permisos.

**Práctica guiada.** Crea un archivo temporal, consulta `stat nota.txt`, espera unos segundos y vuelve a ejecutar touch. Compara modificación y acceso, teniendo en cuenta las políticas de montaje.

**Actividad independiente.** Explica cómo diferenciar un archivo vacío recién creado de uno que contiene datos usando `stat` y `wc -c`.

**Criterios de aceptación.** Describe el efecto de touch sobre existencia y marcas temporales; demuestra que no añade contenido.

**Error frecuente.** Usar touch como si fuera un editor o asumir que todas las marcas temporales se actualizan idénticamente en cualquier sistema de archivos.

### 7.3.6 — cp

**Propósito.** Copiar archivos o directorios sin confundir copia de contenido con preservación completa de metadatos.

**Ejemplo.** `cp origen destino` copia un archivo; `cp -a arbol/ copia/` intenta preservar atributos y estructura de forma recursiva.

**Práctica guiada.** Copia un archivo creado en el laboratorio y compara SHA-256 con `sha256sum`. Después copia un subdirectorio con `cp -a` y revisa permisos y marcas temporales.

**Actividad independiente.** Decide qué opción utilizarías para duplicar una carpeta de configuración y qué metadatos necesitas preservar.

**Criterios de aceptación.** Comprueba igualdad del contenido y explica cuándo se necesita copia recursiva o preservación de atributos.

**Error frecuente.** Sobrescribir el destino sin verificarlo o asumir que una copia simple conserva propietarios y permisos originales.

### 7.3.7 — mv

**Propósito.** Mover o renombrar entradas y comprender las diferencias entre operaciones dentro y entre sistemas de archivos.

**Ejemplo.** En el mismo sistema de archivos, mv suele cambiar la entrada de directorio; entre sistemas de archivos puede requerir copiar y eliminar, con implicaciones de metadatos y atomicidad.

**Práctica guiada.** Renombra un archivo del laboratorio y muévelo a otra carpeta del mismo volumen. Verifica ruta, contenido y permisos antes y después.

**Actividad independiente.** Describe riesgos al mover un archivo grande entre volúmenes y plantea cómo verificar integridad tras la operación.

**Criterios de aceptación.** Distingue renombrar y mover, y verifica que el origen y destino son los esperados.

**Error frecuente.** Usar comodines sin revisar la expansión o asumir que el movimiento entre volúmenes es siempre una operación atómica.

### 7.3.8 — rm

**Propósito.** Eliminar entradas de forma controlada, comprendiendo que rm no proporciona una papelera ni una reversión sencilla.

**Ejemplo.** `rm archivo-temporal` elimina una entrada; `rm -r directorio-lab` recorre el árbol. `-f` suprime ciertas confirmaciones y errores, por lo que aumenta el riesgo de una equivocación.

**Práctica guiada.** Crea un único archivo temporal, confirma la ruta con `pwd` y `ls -l` y elimina solo ese archivo. No utilices `sudo rm` ni `rm -rf` sobre rutas del sistema.

**Actividad independiente.** Diseña una rutina previa a la eliminación de un árbol: validar variable de ruta, mostrar objetivo, confirmar alcance y disponer de copia si corresponde.

**Criterios de aceptación.** Demuestra eliminación de un objeto creado para la práctica y explica por qué la verificación previa es esencial.

**Error frecuente.** Ejecutar una expansión de comodines o una variable vacía sin inspeccionar qué ruta terminará usando rm.

### 7.3.9 — find

**Propósito.** Buscar archivos y directorios mediante criterios de nombre, tipo, tamaño, tiempo y permisos.

**Ejemplo.** `find ~/lab -type f -name '*.log'` busca archivos regulares con esa extensión bajo el árbol de laboratorio. Las comillas evitan que la shell expanda el patrón antes de que find lo procese.

**Práctica guiada.** Crea tres archivos de prueba y localízalos por nombre y tipo. Añade `-print` explícitamente y observa cómo cambia la búsqueda al limitar la ruta inicial.

**Actividad independiente.** Construye una búsqueda que identifique archivos vacíos dentro de tu carpeta de práctica sin recorrer el resto del sistema.

**Criterios de aceptación.** Explica ruta inicial, expresión de búsqueda y tipo; evita búsquedas innecesariamente amplias.

**Error frecuente.** Ejecutar búsquedas desde `/` con privilegios elevados sin necesidad o olvidar citar patrones con comodines.

### 7.3.10 — grep

**Propósito.** Filtrar líneas de texto que coinciden con patrones y comprender el alcance de las expresiones regulares.

**Ejemplo.** `grep -n 'ERROR' aplicación.log` muestra líneas coincidentes con número de línea. `-i` ignora mayúsculas/minúsculas y `-r` recorre directorios, con cuidado de no incluir datos sensibles.

**Práctica guiada.** Crea un archivo de texto con líneas INFO, WARN y ERROR; filtra ERROR con `grep -n` y luego cuenta coincidencias con `grep -c`.

**Actividad independiente.** Diseña un patrón para localizar direcciones IPv4 en datos sintéticos y explica por qué una expresión regular simple no valida por completo todos los rangos posibles.

**Criterios de aceptación.** Explica patrón, coincidencia y código de salida; utiliza datos sintéticos y rutas delimitadas.

**Error frecuente.** Tratar grep como parser completo de formatos estructurados o asumir que ausencia de coincidencias equivale a error del comando.

### 7.3.11 — chmod

**Propósito.** Cambiar permisos de archivos y directorios de forma deliberada.

**Ejemplo.** `chmod 640 archivo` concede lectura/escritura al propietario, lectura al grupo y ningún permiso a otros. La forma simbólica `chmod u=rw,g=r,o= archivo` expresa la misma intención.

**Práctica guiada.** Crea un archivo de prueba, aplica ambos modos en pasos separados y verifica con `stat`. En un directorio, compara el efecto de r y x sobre listar y atravesar.

**Actividad independiente.** Define permisos mínimos para una clave privada de laboratorio y para un directorio de trabajo compartido por un grupo.

**Criterios de aceptación.** Traduce octal/simbólico y justifica permisos de archivo frente a directorio.

**Error frecuente.** Aplicar 777 para resolver cualquier problema de acceso o cambiar permisos recursivamente sin revisar el árbol.

### 7.3.12 — chown

**Propósito.** Cambiar propietario y/o grupo cuando exista una necesidad administrativa legítima.

**Ejemplo.** `chown usuario:grupo archivo` asigna ambos atributos. La operación suele requerir privilegios; las reglas exactas para transferir propiedad dependen del sistema.

**Práctica guiada.** Inspecciona propietario y grupo con `stat` y `ls -ln`. En un laboratorio desechable, si dispones de autorización, cambia la propiedad de un archivo creado para la práctica y vuelve a verificar. Si no tienes permisos, documenta el error sin elevar privilegios.

**Actividad independiente.** Diseña un plan de corrección de propiedad para un directorio de aplicación, incluyendo alcance, respaldo, identidad de servicio y validación.

**Criterios de aceptación.** Distingue usuario y grupo propietarios y demuestra que comprende el impacto de un cambio recursivo.

**Error frecuente.** Aplicar `chown -R` sobre rutas amplias o usarlo como sustituto de comprender los permisos.

### 7.3.13 — ps

**Propósito.** Obtener una instantánea de procesos y sus atributos principales.

**Ejemplo.** `ps -ef` presenta procesos en formato amplio; `ps -p PID -o pid,ppid,stat,etime,cmd` permite inspeccionar una instancia concreta. La salida refleja un instante, no un historial continuo.

**Práctica guiada.** Inicia `sleep 60 & pid=$!` y consulta únicamente ese PID con ps. Registra PID, PPID, estado y tiempo transcurrido; termina el proceso propio al finalizar.

**Actividad independiente.** Compara dos formatos de ps y explica qué campos ayudan a identificar relación padre-hijo y estado.

**Criterios de aceptación.** Interpreta PID/PPID/STAT y reconoce que la salida es una instantánea.

**Error frecuente.** Elegir un proceso por nombre sin comprobar PID, propietario y comando completo.

### 7.3.14 — top

**Propósito.** Observar dinámicamente carga de CPU, memoria y procesos para formular hipótesis de rendimiento.

**Ejemplo.** top actualiza periódicamente estadísticas; el porcentaje de CPU depende del número de núcleos y de la forma de cálculo. La vista es una observación, no un diagnóstico completo de causa.

**Práctica guiada.** Ejecuta `top` durante un periodo corto. Identifica carga, procesos con mayor consumo y memoria disponible. Sal con q y no cambies prioridades ni finalices procesos desde la herramienta.

**Actividad independiente.** Describe qué mediciones adicionales recopilarías para distinguir saturación de CPU, espera de I/O y presión de memoria.

**Criterios de aceptación.** Interpreta al menos tres indicadores y separa observación de hipótesis causal.

**Error frecuente.** Considerar load average como porcentaje de CPU o asumir que el proceso que aparece arriba es necesariamente la causa raíz.

### 7.3.15 — kill

**Propósito.** Enviar señales a procesos identificados y distinguir solicitud de terminación de terminación forzada.

**Ejemplo.** `kill -TERM PID` solicita terminación ordenada; `kill -KILL PID` fuerza al kernel a terminar el proceso y no permite que este gestione la señal. No debe actuarse sobre PID desconocidos.

**Práctica guiada.** En Bash crea `sleep 90 & pid=$!`, verifica el PID y envía SIGTERM a esa instancia. Comprueba su salida. No utilices killall ni pkill sobre procesos generales.

**Actividad independiente.** Explica cuándo una aplicación necesita liberar archivos o guardar estado antes de salir y qué implica recibir SIGKILL.

**Criterios de aceptación.** Identifica el proceso propio, utiliza SIGTERM y explica las limitaciones de SIGKILL.

**Error frecuente.** Enviar señales a PID reutilizados u obtenerlos de una lista antigua sin volver a verificarlos.

### 7.3.16 — systemctl

**Propósito.** Consultar y administrar unidades gestionadas por systemd, diferenciando observación de modificación.

**Ejemplo.** `systemctl status servicio` muestra estado y detalles; `is-active` consulta ejecución y `is-enabled` consulta habilitación para arranque/activación. `start`, `stop` y `enable` modifican el sistema.

**Práctica guiada.** Consulta el estado de un servicio no crítico con `systemctl status`, `systemctl is-active` y `systemctl is-enabled`. No cambies su estado en el host.

**Actividad independiente.** Redacta una secuencia segura para reiniciar un servicio de laboratorio, incluyendo autorización, dependencias, ventana y comprobación posterior.

**Criterios de aceptación.** Distingue consulta de cambio y activo de habilitado; identifica nombre de unidad.

**Error frecuente.** Ejecutar `systemctl restart` sobre un servicio desconocido sin evaluar impacto.

### 7.3.17 — journalctl

**Propósito.** Consultar el journal de systemd para investigar eventos por arranque, unidad, prioridad y tiempo.

**Ejemplo.** `journalctl -b` muestra registros del arranque actual; `journalctl -u servicio` filtra por unidad; `-p warning` limita por prioridad. La disponibilidad y persistencia del journal dependen de la configuración.

**Práctica guiada.** Consulta `journalctl -b -p warning` y luego filtra por un servicio de laboratorio. Registra timestamp, unidad, prioridad y mensaje, ocultando datos sensibles.

**Actividad independiente.** Construye una línea temporal a partir de eventos sintéticos y explica qué evidencia adicional necesitas para confirmar una causa.

**Criterios de aceptación.** Aplica al menos dos filtros, interpreta los campos y distingue evento observado de conclusión.

**Error frecuente.** Suponer que journalctl contiene todos los eventos históricos o que un warning equivale a un incidente.

### 7.3.18 — df

**Propósito.** Medir capacidad y espacio disponible de sistemas de archivos montados.

**Ejemplo.** `df -h` presenta tamaños legibles; `df -i` muestra uso de inodos. Un volumen puede quedarse sin inodos aunque todavía informe espacio en bytes.

**Práctica guiada.** Ejecuta `df -hT` y `df -i`. Identifica punto de montaje, tipo de sistema de archivos, capacidad, usado y disponible. No llenes volúmenes para probar límites.

**Actividad independiente.** Explica dos causas por las que una aplicación puede fallar al crear archivos aunque `df -h` muestre espacio disponible.

**Criterios de aceptación.** Interpreta capacidad y punto de montaje; diferencia espacio en bytes de inodos.

**Error frecuente.** Confundir uso de un directorio con uso de todo el sistema de archivos o interpretar tamaños redondeados como valores exactos.

### 7.3.19 — du

**Propósito.** Estimar cuánto espacio ocupa un árbol de archivos desde la perspectiva de sus entradas.

**Ejemplo.** `du -sh ~/lab` resume el uso del directorio; `du -h --max-depth=1 ruta` compara subdirectorios. El resultado depende de enlaces, archivos dispersos y unidades de asignación.

**Práctica guiada.** Crea archivos de distintos tamaños en una carpeta de prueba y compara `du -sh` con `ls -lh`. No uses directorios del sistema como objetivo de limpieza.

**Actividad independiente.** Investiga por qué la suma de tamaños aparentes de archivos puede diferir del espacio asignado que muestra du o del espacio disponible que muestra df.

**Criterios de aceptación.** Distingue tamaño aparente, bloques asignados y espacio del volumen; limita el análisis a una ruta autorizada.

**Error frecuente.** Borrar archivos grandes basándose solo en du sin identificar qué proceso o servicio los necesita.

### 7.3.20 — mount

**Propósito.** Comprender cómo un sistema de archivos se incorpora al árbol de directorios y qué controles rodean el montaje.

**Ejemplo.** `findmnt` consulta montajes existentes; `mount` sin argumentos suele listar montajes. Montar un dispositivo requiere identificar correctamente origen, tipo y punto de montaje, y puede alterar qué contenido queda visible en esa ruta.

**Práctica guiada.** Ejecuta `findmnt` y `mount` en modo de consulta. Identifica un punto de montaje, su origen y opciones. No montes ni desmontes dispositivos del host durante esta práctica.

**Actividad independiente.** Diseña un procedimiento para montar un volumen de laboratorio: identificar dispositivo, revisar sistema de archivos, crear punto de montaje, aplicar opciones seguras, verificar y desmontar de forma controlada.

**Criterios de aceptación.** Explica origen, tipo y punto de montaje; interpreta una entrada de findmnt y reconoce riesgos de montaje/desmontaje.

**Error frecuente.** Desmontar un volumen ocupado o montar un dispositivo no verificado sobre una ruta que contiene datos importantes.

## 7.4 — Bash

### 7.4.1 — Variables

Bash mantiene variables locales a la shell y variables exportadas al entorno de procesos hijos. La asignación no admite espacios alrededor de `=`. Las comillas simples conservan texto literal; las dobles permiten expansiones. Ejemplo: `proyecto="laboratorio azul"` y `printf '%s\\n' "$proyecto"`. Sin comillas, los espacios pueden dividir el valor en varios argumentos.

**Práctica guiada:** asigna un valor con espacios, imprímelo y compáralo con el resultado de un subproceso antes y después de exportar la variable. Usa datos ficticios, nunca secretos.

**Actividad independiente:** valida que una variable requerida no esté vacía sin revelar su contenido.

**Criterios de aceptación:** diferencia asignación, expansión y exportación; conserva espacios mediante comillas y demuestra qué recibe el proceso hijo.

**Errores frecuentes:** espacios alrededor de `=`, olvidar comillas o asumir que exportar vuelve persistente la variable entre sesiones.

**Comprobación:** ¿qué cambia al exportar una variable y qué no cambia?

### 7.4.2 — Operadores

Bash ofrece pruebas de archivos, cadenas y números, además de expresiones aritméticas. `[[ ... ]]` es una construcción de Bash; `(( ... ))` evalúa aritmética; `[ ... ]` tiene reglas de argumentos propias. Ejemplo: `[[ -f "$ruta" ]]` comprueba un archivo regular y `(( intentos < 3 ))` compara números.

**Práctica guiada:** crea un archivo temporal dentro del laboratorio y prueba `-f`, `-d`, `-r` y una comparación numérica. Comprueba el estado de salida de cada prueba.

**Actividad independiente:** valida un número entre 1 y 5 y rechaza entradas vacías, no numéricas y fuera de rango.

**Criterios de aceptación:** selecciona la construcción adecuada y prueba casos válidos y límite.

**Errores frecuentes:** mezclar sintaxis de otros lenguajes, no citar rutas o evaluar entradas con `eval`.

**Comprobación:** ¿por qué una prueba de archivo y una comparación aritmética utilizan construcciones distintas?

### 7.4.3 — Condicionales

`if`, `elif` y `else` seleccionan ramas según el estado de salida de una orden. En Unix, cero representa éxito y un valor distinto de cero representa fallo o condición no satisfecha. Ejemplo: verificar `[[ -d "$destino" ]]` antes de escribir en una ruta.

**Práctica guiada:** crea un bloque que reciba una ruta, distinga directorio existente de ruta inexistente y muestre mensajes diferentes. Ejecuta ambos escenarios y registra el código de salida.

**Actividad independiente:** añade una comprobación de permiso de escritura y explica por qué no garantiza que una operación posterior vaya a tener éxito.

**Criterios de aceptación:** prueba ambas ramas y devuelve un estado útil al programa llamador.

**Errores frecuentes:** confundir salida textual con éxito o ignorar fallos de órdenes dentro de una rama.

**Comprobación:** ¿qué información aporta el código de salida que no aporta necesariamente el mensaje impreso?

### 7.4.4 — Bucles

`for` recorre listas o expansiones; `while` repite mientras una condición tenga éxito; `until` repite hasta que tenga éxito. La expansión de palabras y comodines puede alterar elementos si no se cita. Para leer líneas se recomienda `while IFS= read -r linea`.

**Práctica guiada:** recorre una lista sintética de tres elementos, uno con espacios, e imprime cada elemento entre delimitadores para comprobar que se conserva como unidad.

**Actividad independiente:** procesa un archivo de texto sintético línea por línea conservando espacios y barras invertidas.

**Criterios de aceptación:** no se pierden ni fragmentan elementos y el bucle tiene terminación clara.

**Errores frecuentes:** usar `for x in $(cat archivo)` para leer líneas o crear bucles infinitos.

**Comprobación:** ¿qué problema evita la combinación `IFS= read -r`?

### 7.4.5 — Funciones

Las funciones agrupan operaciones reutilizables y reciben argumentos posicionales como `$1` y `$2`. `"$@"` conserva cada argumento como unidad. La función comunica información por stdout/stderr y éxito o fallo mediante su código de retorno; `return` devuelve un estado numérico.

**Ejemplo:** `validar_directorio() { [[ -d "$1" ]]; }` puede utilizarse directamente como condición de un `if`.

**Práctica guiada:** implementa la función y ejecútala con una ruta válida y otra inexistente. Comprueba los estados.

**Actividad independiente:** exige exactamente dos argumentos, valida ambos y prueba nombres de ruta con espacios.

**Criterios de aceptación:** valida argumentos, conserva espacios y separa salida textual de estado.

**Errores frecuentes:** intentar devolver cadenas con `return` o expandir `$@` sin comillas.

**Comprobación:** ¿cuándo conviene imprimir un resultado y cuándo devolver un código de estado?

### 7.4.6 — Arrays

Los arrays indexados almacenan secuencias; los asociativos relacionan claves y valores y requieren una versión de Bash compatible. `"${array[@]}"` expande cada elemento como argumento separado. `"${array[*]}"` puede unir elementos dentro de comillas.

**Práctica guiada:** crea un array con tres servicios ficticios, uno con espacios; imprime cada elemento y cuenta los elementos con `${#servicios[@]}`.

**Actividad independiente:** crea un inventario asociativo de servicios y puertos, comprueba que la clave exista antes de consultarla y anota la versión de Bash.

**Criterios de aceptación:** conserva límites entre elementos, interpreta el conteo y reconoce la dependencia de versión.

**Errores frecuentes:** confundir `[@]` con `[*]`, omitir comillas o asumir que POSIX sh implementa arrays Bash.

**Comprobación:** ¿por qué `"${array[@]}"` es la forma habitual de pasar elementos como argumentos separados?

### 7.4.7 — Pipes

Una tubería conecta stdout de un proceso con stdin del siguiente y permite componer herramientas. Las etapas pueden ejecutarse concurrentemente. Por defecto, el estado suele reflejar la última orden; `set -o pipefail` permite detectar fallos de etapas anteriores.

**Ejemplo:** `printf '%s\\n' INFO WARN ERROR | grep ERROR` filtra líneas sintéticas.

**Práctica guiada:** ejecuta el pipeline y después introduce una orden inexistente en una etapa. Compara el estado antes y después de activar pipefail en una subshell.

**Actividad independiente:** filtra eventos sintéticos por severidad y cuenta coincidencias; explica qué ocurre si falla la fuente.

**Criterios de aceptación:** identifica productor, consumidor, flujo y estado.

**Errores frecuentes:** creer que la tubería transmite stderr automáticamente o ignorar fallos intermedios.

**Comprobación:** ¿qué error puede quedar oculto si solo se consulta el estado de la última orden?

### 7.4.8 — Redirecciones

Los descriptores estándar son stdin (0), stdout (1) y stderr (2). `>` crea o trunca, `>>` añade, `2>` redirige errores y `2>&1` duplica stderr hacia el destino actual de stdout. El orden de evaluación importa.

**Ejemplo:** `comando >salida.txt 2>errores.txt` separa ambos flujos; `comando >todo.txt 2>&1` los dirige al mismo archivo.

**Práctica guiada:** ejecuta órdenes inocuas con salida normal y error controlado; guarda los flujos en archivos temporales separados y revísalos.

**Actividad independiente:** documenta cómo capturar ambos flujos en un archivo y cómo mantenerlos separados.

**Criterios de aceptación:** predice el destino de cada descriptor y diferencia truncar de añadir.

**Errores frecuentes:** sobrescribir registros importantes o asumir que `2>&1 >archivo` equivale a `>archivo 2>&1`.

**Comprobación:** ¿por qué el orden de redirecciones cambia el resultado?

### 7.4.9 — Exit codes

El estado de salida comunica el resultado de una orden. Cero suele significar éxito; otros valores representan fallo o condiciones específicas. En Bash, `$?` contiene el estado de la última orden y debe guardarse inmediatamente.

**Ejemplo:** grep suele devolver 0 si encuentra coincidencias, 1 si no encuentra y otro valor para errores. «Sin coincidencias» no equivale necesariamente a «no pudo leer el archivo».

**Práctica guiada:** ejecuta una búsqueda con coincidencia, otra sin coincidencia y otra sobre un archivo inexistente. Guarda cada estado antes de ejecutar otra orden.

**Actividad independiente:** diseña una función que diferencie resultado positivo, ausencia de resultados y error de lectura.

**Criterios de aceptación:** interpreta los tres escenarios y conserva los estados correctamente.

**Errores frecuentes:** consultar `$?` después de otra orden o tratar todos los estados distintos de cero como iguales.

**Comprobación:** ¿qué diferencia hay entre no encontrar datos y no poder ejecutar correctamente la búsqueda?

### 7.4.10 — Scripts

Un script reúne órdenes en un archivo ejecutable por un intérprete. Puede incluir shebang, validación de argumentos, funciones, control de errores y códigos de salida. `set -e` tiene excepciones y no sustituye comprobaciones explícitas.

**Práctica guiada:** crea un script Bash que valide un argumento de ruta y liste su contenido solo si es un directorio. Prueba argumento ausente, ruta inexistente y ruta válida dentro del laboratorio.

**Actividad independiente:** añade logging con timestamp y salida controlada; nunca registres contraseñas, tokens ni datos sensibles.

**Criterios de aceptación:** gestiona los casos de prueba, preserva espacios en rutas y devuelve estados coherentes.

**Errores frecuentes:** no citar variables, silenciar todos los errores o confiar únicamente en `set -e`.

**Comprobación:** ¿qué validaciones deben preceder a una operación de escritura sobre una ruta recibida como argumento?

### 7.4.11 — Cron

cron programa tareas periódicas mediante cinco campos: minuto, hora, día del mes, mes y día de la semana. Su entorno suele ser reducido y distinto al de una terminal interactiva. PATH, zona horaria, permisos y disponibilidad del daemon influyen en la ejecución.

**Ejemplo:** `0 2 * * 1` representa las 02:00 cada lunes en la interpretación habitual; la expresión no determina por sí sola la zona horaria.

**Práctica guiada:** interpreta expresiones de ejemplo sin instalarlas. Consulta `crontab -l` solo para inspeccionar tu propia tabla.

**Actividad independiente:** diseña una programación semanal de respaldo con destino, retención, logging, comprobación de éxito y prevención de solapamientos.

**Criterios de aceptación:** interpreta los cinco campos y enumera diferencias entre cron y una shell interactiva.

**Errores frecuentes:** asumir que cron hereda PATH, ignorar zona horaria o no controlar tareas simultáneas.

**Comprobación:** ¿por qué una orden que funciona en tu terminal puede fallar desde cron?

### 7.4.12 — Automatización

Una automatización fiable combina repetibilidad, idempotencia, observabilidad, control de errores, privilegios mínimos y reversión. Debe documentar entradas, efectos, dependencias y forma de verificar el resultado.

**Ejemplo:** crear un directorio si no existe es idempotente respecto a su existencia; añadir la misma línea a un archivo en cada ejecución puede duplicar datos.

**Práctica guiada:** crea una tarea que prepare una carpeta de reportes y escriba un timestamp. Ejecútala dos veces y verifica que no duplique estructura ni cambie permisos inesperadamente.

**Actividad independiente:** diseña una comprobación de espacio en disco que alerte al superar un umbral, sin borrar archivos ni reiniciar servicios.

**Criterios de aceptación:** la tarea puede repetirse, registra resultados, gestiona errores y no requiere privilegios innecesarios.

**Errores frecuentes:** acciones destructivas sin simulación, credenciales en texto plano o ejecuciones concurrentes sin control.

**Comprobación:** ¿qué propiedad permite repetir una automatización sin efectos acumulativos no deseados?

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
