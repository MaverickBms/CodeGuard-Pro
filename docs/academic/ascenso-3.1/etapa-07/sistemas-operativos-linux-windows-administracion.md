# Etapa 7 — Sistemas operativos: Linux, Windows y administración

**Estado:** borrador didáctico v0.1.0.  
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

### Kernel, Kernel Space y User Space

El kernel es el núcleo privilegiado del sistema operativo. Gestiona recursos y expone servicios controlados a los programas. Kernel Space es el espacio de ejecución privilegiado donde opera el kernel y ciertos componentes; User Space aloja aplicaciones con privilegios restringidos. La separación contribuye al aislamiento de fallos y limita el impacto de errores de aplicaciones.

Una aplicación normalmente no accede directamente a dispositivos arbitrarios: solicita operaciones al sistema mediante interfaces definidas.

### System Calls y drivers

Una llamada al sistema es una interfaz controlada mediante la cual un programa solicita un servicio del kernel, como abrir un archivo, crear un proceso o comunicarse con un dispositivo. Una función de biblioteca puede preparar argumentos y finalmente invocar una llamada al sistema, pero ambos conceptos no son idénticos.

Los drivers permiten que el sistema operativo interactúe con dispositivos concretos mediante interfaces compatibles. Un driver defectuoso puede afectar estabilidad o seguridad, por lo que debe obtenerse de fuentes confiables y compatibles con el sistema.

### Procesos, hilos y scheduler

Un proceso es una instancia de programa en ejecución con recursos y contexto propios, como espacio de direcciones y descriptores. Un hilo es una secuencia de ejecución dentro de un proceso. Los hilos de un proceso suelen compartir memoria y recursos, aunque cada hilo conserva su propio estado de ejecución y pila.

El scheduler decide qué tarea ejecutable recibe tiempo de CPU según la política del sistema. Un context switch ocurre cuando el procesador deja una tarea y pasa a otra, preservando y restaurando el estado necesario. El cambio de contexto tiene coste y no constituye trabajo útil de la aplicación.

### Memoria virtual

La memoria virtual proporciona a cada proceso una vista lógica de memoria y permite aislar espacios de direcciones. El sistema traduce direcciones virtuales a físicas, administra páginas y puede respaldar parte de la memoria en almacenamiento secundario. Memoria virtual no significa que el disco sea tan rápido como RAM: una paginación intensa puede degradar severamente el rendimiento.

### Sistema de archivos e IPC

El sistema de archivos organiza nombres, directorios, metadatos y contenido persistente. Un dispositivo, un sistema de archivos y un punto de montaje son conceptos distintos: el punto de montaje presenta un sistema de archivos en una ruta del árbol.

Los procesos pueden intercambiar información mediante pipes, sockets, memoria compartida, colas de mensajes y señales. Cada mecanismo presenta compromisos de rendimiento, sincronización y alcance. La memoria compartida puede ser rápida, pero requiere sincronización correcta.

### Concurrencia y paralelismo

La concurrencia organiza varias tareas que progresan de forma intercalada o solapada. El paralelismo implica ejecución simultánea, por ejemplo en varios núcleos. Puede existir concurrencia sin paralelismo.

Ambos conceptos requieren considerar condiciones de carrera, exclusión mutua, orden de operaciones, bloqueos e interbloqueos. Ejercicio: explica qué sucede si dos hilos incrementan una variable compartida sin sincronización y por qué leer, sumar y escribir no necesariamente es una operación atómica.

## 7.2 — Linux

### Distribuciones y kernel Linux

Linux es el kernel; una distribución integra el kernel con utilidades, bibliotecas, gestor de paquetes, configuración y políticas para formar un sistema utilizable. Ubuntu y Debian son distribuciones. Pueden compartir componentes, pero difieren en ciclos de publicación, políticas, versiones y soporte. Consulta la documentación de la versión instalada antes de aplicar instrucciones.

### Estructura del sistema de archivos

El árbol parte de la raíz /.

| Directorio | Uso habitual |
|---|---|
| /etc | configuración del sistema y servicios |
| /var | datos variables, colas y registros |
| /home | directorios personales |
| /usr | programas, bibliotecas y recursos compartidos |
| /tmp | archivos temporales |
| /opt | software adicional |

La distribución concreta puede incorporar enlaces simbólicos o convenciones adicionales. No elimines contenido de estas rutas sin comprender su función.

### Usuarios, grupos, propietarios y root

Linux identifica usuarios y grupos mediante IDs. Los permisos controlan acciones para propietario, grupo y otros. Root es la cuenta privilegiada tradicional. Sudo permite ejecutar comandos autorizados con privilegios elevados según la política configurada.

Aplica mínimo privilegio: utiliza una cuenta normal para tareas cotidianas, eleva privilegios solo cuando sea necesario y revisa el comando antes de usar sudo. No compartas contraseñas ni habilites root remoto sin una necesidad y controles claros.

### Permisos

Los permisos tradicionales se expresan como lectura (r), escritura (w) y ejecución (x) para propietario, grupo y otros. En directorios, x permite atravesarlo; r permite listar nombres; w permite modificar entradas si se combinan los permisos necesarios.

Ejemplos:
- 640: propietario lectura/escritura, grupo lectura, otros sin permisos.
- 755: propietario lectura/escritura/ejecución, grupo y otros lectura/ejecución.

No utilices permisos 777 como solución general. Conceder escritura a todos aumenta el riesgo.

### Procesos, servicios, paquetes, logs y variables

- Procesos: instancias en ejecución; identifica PID, usuario, consumo y relación padre-hijo.
- Servicios: procesos o unidades administradas por el sistema; sistemas modernos basados en systemd suelen utilizar systemctl.
- Paquetes: software distribuido con metadatos y dependencias, instalado mediante el gestor de la distribución.
- Logs: registros de eventos y actividad; pueden contener información sensible y requieren controles de acceso y retención.
- Variables de entorno: configuración heredada por procesos hijos; evita incluir secretos en comandos visibles o registros.

## 7.3 — Administración Linux

### Comandos del temario

| Comando | Función | Práctica |
|---|---|---|
| pwd | muestra directorio actual | consulta dónde estás |
| ls | lista contenido | lista archivos ocultos y permisos |
| cd | cambia directorio | navega a una ruta de laboratorio |
| mkdir | crea directorio | crea laboratorio |
| touch | crea archivo vacío o actualiza fecha | crea notas.txt |
| cp | copia archivos/directorios | copia un archivo de práctica |
| mv | mueve o renombra | renombra una copia |
| rm | elimina | elimina solo un archivo temporal |
| find | busca en directorios | encuentra archivos por nombre |
| grep | busca texto | busca una palabra en un log de prueba |
| chmod | modifica permisos | establece permisos 640 |
| chown | cambia propietario/grupo | practica solo con autorización |
| ps | muestra procesos | consulta procesos del usuario |
| top | muestra procesos y recursos dinámicamente | identifica consumo |
| kill | envía señales a procesos | utiliza un proceso propio de laboratorio |
| systemctl | consulta/administra unidades systemd | consulta un servicio no crítico |
| journalctl | consulta journal systemd | inspecciona logs del laboratorio |
| df | informa espacio de sistemas de archivos | revisa espacio disponible |
| du | estima uso de archivos/directorios | mide el directorio de práctica |
| mount | muestra/administra montajes | inspecciona montajes existentes |

**Precaución:** rm puede eliminar sin papelera. No practiques rm -rf en rutas reales ni con variables sin validar. Comprueba el directorio actual y el destino. No detengas servicios esenciales ni modifiques montajes del host.

### Permisos y propietarios

En un directorio de laboratorio crea un archivo, consulta permisos con ls -l y aplica chmod 640. Interpreta el resultado. En un entorno multiusuario controlado, cambia el propietario con chown solo si tienes autorización y privilegios.

### Procesos y servicios

Antes de detener un proceso o servicio, identifica el PID o unidad, comprueba su función y dependencias, determina el impacto y elige la acción menos disruptiva. Kill envía una señal; no significa necesariamente que el proceso termine inmediatamente.

### Logs y almacenamiento

Journalctl consulta el journal de systemd; df informa espacio de sistemas de archivos; du estima uso de archivos y directorios; mount muestra o administra montajes. Los registros pueden contener rutas, nombres de usuario, direcciones y datos de solicitudes. Comparte extractos redactados, no logs completos indiscriminadamente.

## 7.4 — Bash

### Variables, operadores, condicionales y bucles

Las variables de shell almacenan valores para utilizarlos durante la ejecución. En Bash la asignación no lleva espacios alrededor del signo igual y la expansión se realiza con el signo dólar. Los operadores permiten comparar cadenas o números, combinar condiciones y realizar operaciones aritméticas.

If permite ramificar; for recorre elementos; while repite mientras una condición se cumpla. Evita ciclos sin una condición de salida alcanzable.

### Funciones y arrays

Las funciones encapsulan operaciones reutilizables. Los arrays agrupan elementos indexados. Bash tiene reglas particulares de expansión y quoting: utiliza comillas para preservar espacios y caracteres especiales.

### Pipes, redirecciones y exit codes

Un pipe conecta la salida estándar de un proceso con la entrada del siguiente. Las redirecciones envían salida o errores a archivos y descriptores. Cada comando devuelve un código de salida; convencionalmente cero indica éxito y un valor distinto de cero indica alguna condición de error.

En pipelines, revisa pipefail y el código que realmente necesitas validar. No asumas que el último comando representa siempre el éxito de todos los anteriores.

### Scripts y automatización

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

### Cron

Cron programa tareas periódicas en sistemas que lo utilizan. Verifica la sintaxis del calendario y recuerda que el entorno puede diferir de una sesión interactiva: PATH, directorio de trabajo, permisos y variables pueden ser distintos. No programes tareas destructivas o repetitivas sin logs, control de errores y una forma de detenerlas.

## 7.5 — Windows

### Arquitectura y NTFS

Windows organiza ejecución, memoria, seguridad, dispositivos y servicios mediante componentes del sistema. NTFS es un sistema de archivos con permisos y metadatos. No confundas permisos NTFS con permisos compartidos de red: el acceso efectivo puede depender de ambos conjuntos y de la identidad del usuario.

### Usuarios, grupos, permisos y procesos

Las cuentas y grupos permiten asignar derechos y controlar acceso. Aplica mínimo privilegio y separa cuentas administrativas de cuentas de uso cotidiano cuando corresponda. El Administrador de tareas permite observar aplicaciones, procesos y recursos.

### Servicios, Registro y Visor de eventos

Los servicios son componentes que pueden ejecutarse en segundo plano. El Visor de eventos permite consultar registros de sistema, seguridad y aplicaciones según permisos y configuración.

El Registro es una base jerárquica de configuración del sistema y aplicaciones. Modificar claves incorrectas puede afectar el arranque, seguridad o funcionamiento. Antes de cambiarlo, confirma la clave exacta, consulta documentación oficial, exporta la rama relevante cuando proceda, crea un punto de restauración o snapshot y define cómo revertir.

No ejecutes archivos .reg de procedencia desconocida.

### Firewall y PowerShell

El Firewall aplica reglas de tráfico entrante y saliente según perfiles y configuración. No lo desactives para solucionar un problema sin identificar la regla, el perfil y el alcance. Crea excepciones mínimas y documentadas.

PowerShell es una shell y lenguaje de automatización basado en objetos. Sus cmdlets producen objetos estructurados. Comandos de exploración útiles en laboratorio: Get-Process, Get-Service, Get-WinEvent, Get-Help y Get-Command. Get-EventLog es legado y no resulta adecuado para todos los registros modernos.

Para administrar servicios, consulta primero el estado y nombre exacto; después evalúa si detenerlos o iniciarlos es seguro. Practica cambios administrativos en una VM, no en el equipo principal.

## 7.6 — Virtualización

### Máquinas virtuales y recursos

Una máquina virtual presenta hardware virtual a un sistema operativo invitado. El hipervisor gestiona recursos físicos y virtuales. La VM consume CPU, RAM y almacenamiento del host; asignar demasiados recursos puede degradar ambos. VirtualBox y VMware son plataformas de virtualización; sus funciones dependen de edición, versión, host y configuración.

### Snapshots

Un snapshot captura un estado de una VM para volver a él durante pruebas. No es una copia de seguridad completa ni sustituye backups independientes. Puede depender de discos base y cadenas de diferencias; muchos snapshots consumen almacenamiento y pueden afectar el rendimiento.

Crea snapshots antes de prácticas riesgosas, nómbralos con fecha y objetivo y elimina los obsoletos solo después de confirmar que no se necesitan.

### Redes NAT y Host-only

NAT permite que la VM acceda a redes externas a través del host según la configuración; las conexiones entrantes requieren reglas o mecanismos específicos. Host-only crea una red privada entre host y VMs participantes y normalmente no ofrece acceso externo por sí sola. Los adaptadores virtuales conectan las VMs a redes definidas por la plataforma.

No expongas servicios de laboratorio a Internet. Comprueba direcciones, rutas y reglas del host antes de habilitar adaptadores puente u otros modos de red.

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
**Estado editorial:** borrador.
