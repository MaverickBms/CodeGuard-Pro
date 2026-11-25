# Etapa 1 · Módulo 1.4 — Arranque

**Estado:** borrador académico desarrollado (pendiente validación editorial externa y verificación técnica formal).  
**Alineación:** ASCENSO 3.1, Etapa 1, Módulo 1.4.  
**Última actualización:** 2026-11-24

## Identificación del módulo
- **Etapa:** 1 — Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.4 — Arranque.
- **Lecciones oficiales:** 7 (1.4.1 a 1.4.7).
- **Prerrequisitos:** Módulos 1.1, 1.2, 1.3.

## Propósito del módulo
Explicar cómo un computador pasa de estar apagado a tener un sistema operativo en ejecución, identificando componentes, secuencias y controles de seguridad.

## Resultados de aprendizaje del módulo
1. Describir BIOS, UEFI, POST, bootloader, kernel y secuencia de arranque.
2. Explicar el rol de Secure Boot.
3. Diagnosticar conceptualmente fallos básicos de arranque.

---

## Lección 1.4.1 — BIOS

### Identificación
- **Lección oficial:** 1.4.1 — BIOS. **Secuencia:** 1/7.

### Propósito de aprendizaje
Comprender qué es la BIOS y su rol histórico en el arranque.

### Conocimientos previos
- ROM/firmware, CPU, memoria.

### Resultados de aprendizaje
- Definir BIOS.
- Explicar funciones básicas de inicialización.
- Reconocer limitaciones frente a UEFI.
- Identificar riesgos de actualización de firmware.

### Desarrollo conceptual
BIOS (Basic Input/Output System) es firmware tradicional de PCs que inicializa hardware básico al encender el equipo y proporciona servicios de arranque. Se ejecuta desde memoria no volátil y prepara el sistema para cargar un bootloader desde un dispositivo de arranque.

Funciones típicas: POST, detección básica de hardware, configuración (CMOS/Setup), orden de arranque y carga del sector de arranque (MBR en esquemas clásicos).

Limitaciones: soporte histórico para MBR, interfaces de configuración limitadas, arranque menos flexible y menos capacidades modernas de seguridad comparado con UEFI. Hoy muchos sistemas usan UEFI, aunque el término “BIOS” se usa coloquialmente.

### Ejemplo técnico desarrollado
**Flujo clásico:**
1. Encendido.
2. BIOS ejecuta POST.
3. Detecta discos/teclado/video básicos.
4. Lee MBR del dispositivo seleccionado.
5. Carga bootloader.

### Práctica guiada
- En un equipo de laboratorio o VM, identifica si el firmware es BIOS/Legacy o UEFI (sin cambiar configuración).
- Registra el método usado.

### Actividad independiente
Compara 3 limitaciones de BIOS clásico frente a UEFI en una tabla.

### Criterios de aceptación
- Define BIOS correctamente.
- Identifica rol en arranque.
- Menciona al menos 2 limitaciones.

### Errores frecuentes y recomendaciones
- **Error:** usar BIOS como sinónimo exacto de UEFI. **Recomendación:** distinguir firmware legacy y UEFI.
- **Error:** actualizar firmware sin necesidad. **Recomendación:** solo con respaldo y guía oficial.

### Evaluación de comprensión
1. ¿Qué hace la BIOS al encender?
2. ¿Qué es MBR en el contexto clásico?
3. ¿Por qué UEFI reemplazó en gran medida a BIOS?

### Referencias
- UEFI Forum. *UEFI Specifications*. https://uefi.org/specifications. Consultado: 2026-11-24.
- Dell Support. *BIOS and UEFI*. https://www.dell.com/support/kbdoc/en-us/000124211/dell-bios-updates. Consultado: 2026-11-24.

---

## Lección 1.4.2 — UEFI

### Identificación
- **Lección oficial:** 1.4.2 — UEFI. **Secuencia:** 2/7.

### Propósito de aprendizaje
Comprender UEFI como firmware moderno de arranque.

### Conocimientos previos
- Lección 1.4.1.

### Resultados de aprendizaje
- Definir UEFI.
- Explicar ventajas frente a BIOS.
- Comprender ESP y arranque UEFI a nivel básico.
- Relacionar UEFI con Secure Boot.

### Desarrollo conceptual
UEFI (Unified Extensible Firmware Interface) es una especificación de interfaz entre firmware y sistema operativo. Proporciona inicialización de hardware, servicios de arranque y un entorno más flexible que BIOS.

Ventajas comunes: soporte para discos GPT grandes, interfaz más rica, drivers y aplicaciones UEFI, arranque desde partición EFI System Partition (ESP), y soporte para Secure Boot.

La ESP es una partición formateada normalmente en FAT32 que contiene cargadores de arranque y archivos necesarios. UEFI puede cargar un ejecutable EFI directamente, según configuración NVRAM.

### Ejemplo técnico desarrollado
**Arranque UEFI típico:**
1. Firmware UEFI inicializa hardware.
2. Lee entradas de arranque en NVRAM.
3. Carga el cargador EFI desde la ESP.
4. El cargador inicia el kernel/sistema operativo.

### Práctica guiada
- En Linux, verifica si el sistema arrancó en UEFI: `test -d /sys/firmware/efi && echo UEFI || echo Legacy`.
- Documenta el resultado.

### Actividad independiente
Crea una tabla comparativa BIOS vs UEFI con 5 criterios: disco, partición, seguridad, interfaz, extensibilidad.

### Criterios de aceptación
- Define UEFI.
- Menciona ESP o NVRAM.
- Compara correctamente con BIOS.

### Errores frecuentes y recomendaciones
- **Error:** decir que UEFI es “una BIOS nueva” sin matizar. **Recomendación:** es una especificación diferente.
- **Error:** confundir UEFI con Secure Boot. **Recomendación:** Secure Boot es una capacidad relacionada.

### Evaluación de comprensión
1. ¿Qué es la ESP?
2. ¿Qué mejora UEFI sobre BIOS clásico?
3. ¿UEFI y Secure Boot son lo mismo?

### Referencias
- UEFI Forum. *UEFI Specification*. https://uefi.org/specifications. Consultado: 2026-11-24.
- Microsoft Learn. *UEFI firmware*. https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-uefi. Consultado: 2026-11-24.

---

## Lección 1.4.3 — POST

### Identificación
- **Lección oficial:** 1.4.3 — POST. **Secuencia:** 3/7.

### Propósito de aprendizaje
Comprender el POST como verificación inicial de hardware.

### Conocimientos previos
- Lecciones 1.4.1 o 1.4.2.

### Resultados de aprendizaje
- Definir POST.
- Identificar qué verifica a alto nivel.
- Interpretar señales de falla básicas (beeps/códigos/LEDs) con cautela.
- Distinguir POST de arranque del SO.

### Desarrollo conceptual
POST (Power-On Self-Test) es un proceso de verificación inicial ejecutado por el firmware al encender el equipo. Comprueba componentes básicos necesarios para iniciar: CPU, memoria, video básico, teclado y otros dispositivos esenciales, según plataforma.

Si detecta fallas críticas, puede emitir códigos de pitidos, códigos en pantalla, LEDs de diagnóstico o detener el arranque. Los códigos son específicos del fabricante/placa.

POST no garantiza que todo el sistema esté perfecto; solo verifica condiciones básicas para continuar el arranque.

### Ejemplo técnico desarrollado
**Caso:** equipo enciende pero no muestra imagen y emite pitidos.
1. Firmware inicia POST.
2. Detecta problema en RAM.
3. Emite código de pitidos según fabricante.
4. No continúa al bootloader.

**Interpretación:** el fallo ocurre antes de cargar el sistema operativo.

### Práctica guiada
- Busca en el manual de una placa base de ejemplo qué significan dos códigos de POST. Registra fabricante y modelo.

### Actividad independiente
Describe un árbol de diagnóstico simple: si no hay video, ¿qué revisarías primero sin abrir la PSU?

### Criterios de aceptación
- Define POST.
- Distingue POST de carga del SO.
- Usa precaución con códigos específicos del fabricante.

### Errores frecuentes y recomendaciones
- **Error:** interpretar cualquier pitido sin consultar el manual. **Recomendación:** revisar documentación del fabricante.
- **Error:** asumir que si pasa POST todo el hardware está bien. **Recomendación:** POST es verificación básica.

### Evaluación de comprensión
1. ¿Cuándo ocurre el POST?
2. ¿Qué tipo de fallas puede detectar?
3. ¿Por qué los códigos de pitido dependen del fabricante?

### Referencias
- AMI. *AMIBIOS Beep Codes / documentation* (referencia de fabricante; verificar modelo específico). https://www.ami.com/support/. Consultado: 2026-11-24.
- HP Support. *POST error messages*. https://support.hp.com/. Consultado: 2026-11-24.

---

## Lección 1.4.4 — Bootloader

### Identificación
- **Lección oficial:** 1.4.4 — Bootloader. **Secuencia:** 4/7.

### Propósito de aprendizaje
Comprender el rol del bootloader en la carga del sistema operativo.

### Conocimientos previos
- Lecciones 1.4.1-1.4.3.

### Resultados de aprendizaje
- Definir bootloader.
- Explicar su función entre firmware y kernel.
- Identificar ejemplos comunes (GRUB, Windows Boot Manager).
- Reconocer riesgos de configuración incorrecta.

### Desarrollo conceptual
El bootloader es un programa pequeño encargado de cargar el sistema operativo o el kernel en memoria y transferirle el control. Puede presentar un menú de arranque, pasar parámetros al kernel y soportar múltiples sistemas.

Ejemplos: GRUB en muchas distribuciones Linux, Windows Boot Manager en Windows, bootloaders de Android/embebidos.

En UEFI, el bootloader suele ser un ejecutable EFI en la ESP. En BIOS legacy, puede cargarse desde MBR y etapas posteriores.

Un bootloader mal configurado puede impedir el arranque, aunque el hardware y el SO estén intactos.

### Ejemplo técnico desarrollado
**GRUB simplificado:**
1. Firmware carga GRUB.
2. GRUB lee su configuración.
3. Muestra opciones de kernel.
4. Usuario selecciona o se usa opción por defecto.
5. GRUB carga kernel e initramfs en memoria.
6. Pasa control al kernel.

### Práctica guiada
- En una VM Linux, observa el menú de GRUB (si está visible) o revisa `/boot/grub/grub.cfg` sin editarlo.
- Identifica una entrada de arranque.

### Actividad independiente
Explica la diferencia entre bootloader y BIOS/UEFI.

### Criterios de aceptación
- Define bootloader.
- Ubica bootloader en la secuencia de arranque.
- Da un ejemplo real.

### Errores frecuentes y recomendaciones
- **Error:** confundir bootloader con kernel. **Recomendación:** bootloader carga; kernel gestiona el sistema.
- **Error:** editar GRUB sin respaldo. **Recomendación:** no modificar en sistemas críticos sin conocimiento.

### Evaluación de comprensión
1. ¿Qué hace el bootloader?
2. ¿Qué carga antes del kernel?
3. Menciona un ejemplo de bootloader.

### Referencias
- GNU GRUB Manual. https://www.gnu.org/software/grub/manual/grub/grub.html. Consultado: 2026-11-24.
- Microsoft Learn. *Boot and UEFI*. https://learn.microsoft.com/en-us/windows-hardware/drivers/bringup/boot-and-uefi. Consultado: 2026-11-24.

---

## Lección 1.4.5 — Kernel

### Identificación
- **Lección oficial:** 1.4.5 — Kernel. **Secuencia:** 5/7.

### Propósito de aprendizaje
Comprender el rol del kernel en el arranque y operación del sistema.

### Conocimientos previos
- Lecciones 1.4.4, 1.3.6, 1.3.8.

### Resultados de aprendizaje
- Definir kernel.
- Explicar qué hace durante el arranque.
- Distinguir kernel de bootloader y de shell.
- Reconocer tipos generales (monolítico, microkernel, híbrido) a nivel básico.

### Desarrollo conceptual
El kernel es el núcleo del sistema operativo. Gestiona CPU, memoria, dispositivos, sistemas de archivos, procesos y seguridad. Durante el arranque, una vez cargado por el bootloader, inicializa subsistemas esenciales, monta el sistema de archivos raíz y arranca el proceso inicial (init/systemd en Linux, sesión de inicio en Windows).

El kernel opera en modo privilegiado. Las aplicaciones se ejecutan en modo usuario y solicitan servicios mediante llamadas al sistema.

Tipos generales: monolítico (muchos servicios en espacio kernel), microkernel (mínimo en kernel, servicios en espacio usuario), híbrido. La clasificación real puede ser matizada.

### Ejemplo técnico desarrollado
**Arranque Linux simplificado:**
1. GRUB carga kernel y initramfs.
2. Kernel inicializa drivers y memoria.
3. Monta root filesystem.
4. Inicia `systemd`/init.
5. Se levantan servicios y login.

### Práctica guiada
- En Linux, ejecuta `uname -r` para ver la versión del kernel.
- Registra el resultado y explica qué indica.

### Actividad independiente
Explica la diferencia entre kernel panic y una aplicación que se cierra.

### Criterios de aceptación
- Define kernel.
- Ubica kernel después del bootloader.
- Distingue kernel de aplicación.

### Errores frecuentes y recomendaciones
- **Error:** confundir kernel con terminal. **Recomendación:** kernel es núcleo; shell es interfaz.
- **Error:** actualizar kernel sin plan en sistemas críticos. **Recomendación:** usar versiones soportadas y respaldo.

### Evaluación de comprensión
1. ¿Qué carga al kernel?
2. ¿Qué hace el kernel durante el arranque?
3. ¿Qué es una llamada al sistema?

### Referencias
- Linux Kernel Documentation. https://www.kernel.org/doc/html/latest/. Consultado: 2026-11-24.
- Microsoft Learn. *Windows architecture*. https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/. Consultado: 2026-11-24.

---

## Lección 1.4.6 — Secuencia de arranque

### Identificación
- **Lección oficial:** 1.4.6 — Secuencia de arranque. **Secuencia:** 6/7.

### Propósito de aprendizaje
Integrar todos los componentes en una secuencia de arranque coherente.

### Conocimientos previos
- Lecciones 1.4.1 a 1.4.5.

### Resultados de aprendizaje
- Describir la secuencia completa de arranque.
- Identificar puntos de fallo comunes.
- Distinguir fases: firmware, bootloader, kernel, espacio usuario.
- Documentar un arranque observado.

### Desarrollo conceptual
La secuencia de arranque típica es:

1. **Energizado:** fuente entrega energía estable.
2. **Firmware (BIOS/UEFI):** inicializa hardware mínimo.
3. **POST:** verifica componentes básicos.
4. **Selección de dispositivo:** según orden de arranque.
5. **Bootloader:** carga kernel e initramfs.
6. **Kernel:** inicializa drivers, memoria, filesystem.
7. **Init/systemd/servicios:** arranca espacio usuario.
8. **Login/interfaz:** sistema listo para uso.

Los puntos de fallo pueden ubicarse por fase: sin energía, fallo POST, no encuentra bootloader, kernel panic, fallo de servicio.

### Ejemplo técnico desarrollado
**Diagnóstico por fase:**
- Sin LEDs/ventiladores: energía/fuente.
- Pitidos, sin video: POST/RAM/GPU.
- “No boot device”: firmware no encuentra dispositivo arrancable.
- Error GRUB: bootloader/configuración.
- Kernel panic: kernel, drivers, filesystem.

### Práctica guiada
- Crea un diagrama de flujo de la secuencia de arranque con 8 pasos y 2 posibles fallos por fase.

### Actividad independiente
Observa el arranque de una VM y anota mensajes visibles o fases identificables. No modifiques configuración crítica.

### Criterios de aceptación
- Secuencia ordenada y completa.
- Fallos ubicados por fase.
- Diagrama legible.

### Errores frecuentes y recomendaciones
- **Error:** culpar al SO por fallos antes del bootloader. **Recomendación:** ubicar la fase.
- **Error:** saltar a reinstalar sin diagnóstico. **Recomendación:** observar mensajes y fase.

### Evaluación de comprensión
1. ¿Qué ocurre antes del bootloader?
2. ¿En qué fase aparece un kernel panic?
3. ¿Cómo ayuda la secuencia a diagnosticar?

### Referencias
- Microsoft Learn. *Boot process*. https://learn.microsoft.com/en-us/windows/client-management/client-tools/boot-process. Consultado: 2026-11-24.
- Linux Kernel Docs. *Booting*. https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html. Consultado: 2026-11-24.

---

## Lección 1.4.7 — Secure Boot

### Identificación
- **Lección oficial:** 1.4.7 — Secure Boot. **Secuencia:** 7/7.

### Propósito de aprendizaje
Comprender Secure Boot como mecanismo de verificación de integridad en el arranque.

### Conocimientos previos
- Lecciones 1.4.2, 1.4.4, 1.4.6.

### Resultados de aprendizaje
- Definir Secure Boot.
- Explicar qué verifica y qué no verifica.
- Reconocer beneficios y limitaciones.
- Identificar casos donde requiere configuración consciente.

### Desarrollo conceptual
Secure Boot es una característica de UEFI que verifica que los componentes de arranque estén firmados por claves confiables antes de ejecutarlos. Su objetivo es reducir el riesgo de bootkits/malware en etapas tempranas del arranque.

Secure Boot verifica la cadena de arranque según la política y claves configuradas. No protege contra todos los ataques: no reemplaza antivirus/EDR, no evita vulnerabilidades en el SO después del arranque, y no garantiza que el sistema esté libre de malware.

Puede requerir configuración especial para dual boot, drivers o kernels personalizados. Deshabilitarlo debe ser una decisión consciente, documentada y reversible.

### Ejemplo técnico desarrollado
**Caso:** instalador Linux no arranca con Secure Boot activo.
1. Firmware verifica firma del bootloader.
2. Si la firma no es confiable según claves, bloquea ejecución.
3. Usuario debe usar medio firmado, registrar clave o ajustar configuración según política del entorno.

**Interpretación:** Secure Boot protege, pero también exige compatibilidad de componentes firmados.

### Práctica guiada
- Verifica estado de Secure Boot: en Linux `mokutil --sb-state` si está disponible; en Windows `Confirm-SecureBootUEFI` en PowerShell con privilegios adecuados.
- Documenta el resultado.

### Actividad independiente
Escribe una recomendación de seguridad: ¿cuándo mantener Secure Boot activo y cuándo documentar una excepción?

### Criterios de aceptación
- Define Secure Boot correctamente.
- Menciona al menos una limitación.
- No presenta Secure Boot como protección total.

### Errores frecuentes y recomendaciones
- **Error:** desactivar Secure Boot “por si acaso”. **Recomendación:** mantenerlo activo salvo necesidad documentada.
- **Error:** creer que Secure Boot protege todo el sistema. **Recomendación:** es una capa de arranque.

### Evaluación de comprensión
1. ¿Qué verifica Secure Boot?
2. ¿Qué no garantiza?
3. ¿Cuándo puede generar fricción legítima?

### Referencias
- UEFI Forum. *Secure Boot*. https://uefi.org/specifications. Consultado: 2026-11-24.
- Microsoft Learn. *Secure Boot*. https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot. Consultado: 2026-11-24.
- Linux Foundation. *Secure Boot*. https://www.linuxfoundation.org/blog/blog/secure-boot-and-linux. Consultado: 2026-11-24.

---

## Cierre del módulo
- **Evaluación:** secuencia de arranque completa, diferencia BIOS/UEFI, rol de bootloader/kernel, explicación de Secure Boot.
- **Criterio:** 75% y diagnóstico por fase correcto.