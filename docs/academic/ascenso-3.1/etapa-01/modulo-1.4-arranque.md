# Etapa 1 · Módulo 1.4 — Arranque

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 1, apartado 1.4.  
**Temas oficiales:** BIOS, UEFI, POST, bootloader, kernel, secuencia de arranque y Secure Boot.

## Objetivo

Comprender la secuencia general que sigue un computador desde que recibe energía hasta que el sistema operativo toma el control.

## Resultados de aprendizaje

Podrás diferenciar BIOS y UEFI; explicar la función del POST; identificar el cargador de arranque y el kernel; ordenar las fases generales del inicio; explicar qué protege Secure Boot y qué no garantiza.

## 1.4.1 — Secuencia general de arranque

La secuencia exacta depende del firmware, la arquitectura, el sistema operativo y la configuración. Como modelo general:

1. Se aplica alimentación y se inicializan circuitos.
2. El firmware de la plataforma comienza a ejecutarse.
3. Se inicializan y comprueban componentes esenciales.
4. El firmware selecciona un dispositivo u opción de arranque.
5. Se ejecuta un cargador de arranque o una aplicación de arranque.
6. El cargador prepara y transfiere el control al kernel.
7. El kernel inicializa memoria, controladores y subsistemas.
8. Se inician servicios y la interfaz o sesión del usuario.

Esta secuencia es un mapa conceptual; algunos pasos pueden ocurrir en otro orden o combinarse.

## 1.4.2 — BIOS

BIOS (Basic Input/Output System) es el firmware tradicional de arranque de PC. Proporciona inicialización básica y mecanismos para iniciar desde un dispositivo. El término también se usa informalmente para referirse a la configuración del firmware.

Los equipos actuales suelen utilizar UEFI. Por ello, «entrar al BIOS» puede significar realmente abrir la configuración UEFI.

## 1.4.3 — UEFI

UEFI (Unified Extensible Firmware Interface) es una especificación de interfaz entre firmware y software de plataforma. Define servicios de arranque, variables, tablas y aplicaciones EFI, entre otros elementos.

En una configuración UEFI habitual, el firmware puede cargar una aplicación EFI desde una partición del sistema EFI. En equipos con Windows o Linux, esa aplicación puede ser un gestor de arranque del sistema.

UEFI no es un sistema operativo ni un sustituto del kernel. Es parte de la plataforma de firmware que prepara el entorno para iniciar software.

## 1.4.4 — POST

POST (Power-On Self-Test) es el nombre común para las comprobaciones e inicializaciones que el firmware realiza durante el encendido. Puede detectar o informar problemas con memoria, CPU, vídeo u otros componentes esenciales.

No todos los equipos muestran un mensaje «POST» explícito. Pueden comunicar errores mediante códigos, luces, pitidos, registros o mensajes del fabricante. Un POST satisfactorio tampoco demuestra que todos los componentes funcionen perfectamente bajo carga.

**Ejercicio:** consulta el manual del fabricante de un equipo de laboratorio y localiza cómo comunica errores de arranque. No provoques fallos físicos para probarlo.

## 1.4.5 — Bootloader (cargador de arranque)

El bootloader es el software que prepara la carga del sistema operativo y transfiere el control al kernel. Puede mostrar un menú de sistemas, parámetros de inicio o herramientas de recuperación.

Ejemplos dependen del sistema: GRUB es común en muchas distribuciones Linux; Windows Boot Manager forma parte del ecosistema Windows. No todos los equipos utilizan el mismo cargador ni todos los sistemas requieren un menú visible.

## 1.4.6 — Kernel

El kernel (núcleo del sistema operativo) administra recursos esenciales: procesos, memoria, dispositivos, interrupciones, llamadas al sistema y aislamiento. Durante el arranque, el cargador lo ubica en memoria y le transfiere el control con los parámetros y estructuras que correspondan.

El kernel no equivale a toda la experiencia del sistema operativo: después de iniciarse pueden cargarse controladores, servicios, procesos de usuario, entorno gráfico y aplicaciones.

## 1.4.7 — Secure Boot

Secure Boot es una función de UEFI que verifica firmas y políticas de confianza para controlar qué aplicaciones EFI pueden ejecutarse durante el arranque. Su propósito es reducir el riesgo de que código no autorizado se ejecute antes del sistema operativo.

Límites importantes:
- no impide todos los ataques;
- no garantiza que el sistema operativo esté libre de vulnerabilidades;
- depende de claves, bases de confianza, revocaciones y configuración;
- una cadena de arranque confiable no sustituye actualizaciones, cifrado, controles de acceso ni copias de seguridad.

No cambies claves, desactives Secure Boot ni modifiques el modo de arranque de tu equipo principal como parte de este módulo. Un cambio incorrecto puede impedir el inicio o afectar la capacidad de arrancar medios instalados.

## Laboratorio — Reconstruir la ruta de arranque

**Objetivo:** documentar el arranque de un equipo propio sin modificar firmware ni configuración.

1. Identifica modelo y fabricante del equipo.
2. Consulta documentación del fabricante para saber si usa UEFI.
3. Desde el sistema operativo, consulta de forma no invasiva el modo de arranque y la información de Secure Boot, si está disponible.
4. Identifica el gestor de arranque y el sistema operativo instalado.
5. Dibuja la secuencia firmware → selección de arranque → bootloader → kernel → servicios/sesión.
6. Señala qué fases pudiste observar y cuáles inferiste a partir de documentación.
7. Añade un apartado de recuperación: cómo consultar el manual oficial antes de realizar cambios.

No modifiques particiones, entradas de firmware, claves, NVRAM ni configuración de Secure Boot. No ejecutes comandos de reparación ni de escritura.

### Evidencias

- ficha del equipo sin número de serie;
- captura redactada o transcripción de la información no sensible;
- diagrama de secuencia;
- tabla «observado / documentado / inferido»;
- conclusión con límites y fuentes.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Diferencia BIOS/UEFI | 15 |
| Explica POST y firmware | 15 |
| Ubica bootloader y kernel | 20 |
| Ordena la secuencia correctamente | 20 |
| Explica Secure Boot y límites | 20 |
| Seguridad y trazabilidad | 10 |

## Ejercicios

1. ¿Por qué decir «BIOS» puede ser impreciso en un equipo UEFI?
2. ¿Qué objetivo tiene POST?
3. ¿Qué tarea realiza el bootloader?
4. ¿Qué administra el kernel?
5. ¿Qué verifica Secure Boot?
6. ¿Por qué Secure Boot no garantiza un sistema completamente seguro?

**Respuestas orientativas:** muchos equipos usan firmware UEFI; POST inicializa y comprueba componentes; bootloader prepara y carga el kernel; kernel administra recursos y mecanismos centrales; Secure Boot valida confianza/firma de aplicaciones de arranque; la seguridad también depende de vulnerabilidades, configuración, actualizaciones, credenciales y controles posteriores.

## Recursos audiovisuales

No se incorpora video en esta versión porque no se ha verificado una pieza con audio hablado en español que explique de manera precisa BIOS, UEFI, POST, bootloader, kernel y Secure Boot. No se recomienda un tutorial de cambio de BIOS/UEFI como sustituto de una explicación conceptual segura.

## Referencias

- UEFI Forum, **UEFI Specifications**: https://uefi.org/specifications
- Microsoft Learn, **Secure Boot**: https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot
- Microsoft Learn, **Windows boot process**: https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/boot-and-uefi
- GNU GRUB Manual: https://www.gnu.org/software/grub/manual/grub/grub.html
- EducACCIÓN dixital (Xunta de Galicia), **Análise de sistemas. Software** (secuencia de arranque, material institucional): https://recursos.edu.xunta.gal/sites/default/files/recurso/1639064851/32_anlise_de_sistemas_software.html

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** laboratorio de observación propuesto; no ejecutado en un equipo físico.  
**Estado editorial:** borrador.
