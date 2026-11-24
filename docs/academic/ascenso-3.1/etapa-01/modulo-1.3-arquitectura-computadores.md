# Etapa 1 · Módulo 1.3 — Arquitectura de computadores

**Estado:** borrador académico desarrollado (pendiente validación editorial externa y verificación técnica formal).  
**Alineación:** ASCENSO 3.1, Etapa 1, Módulo 1.3.  
**Última actualización:** 2026-11-24

## Identificación del módulo
- **Etapa:** 1 — Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.3 — Arquitectura de computadores.
- **Lecciones oficiales:** 8 (1.3.1 a 1.3.8).
- **Prerrequisitos:** Módulos 1.1 y 1.2.

## Propósito del módulo
Explicar cómo se organiza internamente un computador para ejecutar instrucciones, mover datos y atender eventos. Este módulo conecta hardware con ejecución de software.

## Resultados de aprendizaje del módulo
1. Describir modelos Von Neumann y Harvard.
2. Explicar el ciclo Fetch-Decode-Execute.
3. Distinguir ISA, microarquitectura y organización.
4. Comprender registros, memoria, E/S e interrupciones.

---

## Lección 1.3.1 — Arquitectura Von Neumann

### Identificación
- **Lección oficial:** 1.3.1 — Arquitectura Von Neumann. **Secuencia:** 1/8.

### Propósito de aprendizaje
Comprender el modelo Von Neumann y su impacto en el diseño de computadores.

### Conocimientos previos
CPU, memoria, buses, bits/bytes.

### Resultados de aprendizaje
- Describir componentes clave del modelo Von Neumann.
- Explicar el concepto de programa almacenado.
- Identificar el cuello de botella de Von Neumann.
- Relacionar el modelo con computadores de propósito general.

### Desarrollo conceptual
La arquitectura Von Neumann describe un sistema donde instrucciones y datos se almacenan en la misma memoria y comparten rutas de acceso. El modelo clásico incluye CPU (unidad de control y ALU), memoria principal, dispositivos de entrada/salida y buses/interconexiones.

La idea central es el **programa almacenado**: las instrucciones son datos en memoria que la CPU puede leer y ejecutar. Esto permitió computadores más flexibles que los sistemas cableados para una sola tarea.

El **cuello de botella de Von Neumann** se refiere a la limitación de ancho de banda/latencia entre CPU y memoria, especialmente cuando instrucciones y datos compiten por el mismo canal. Cachés, pipelines y arquitecturas modernas mitigan parcialmente este problema, pero no lo eliminan por completo.

### Ejemplo técnico desarrollado
**Ejecución de un programa simple:**
1. El programa compilado se carga en RAM: instrucciones y datos.
2. La CPU lee la siguiente instrucción desde la dirección indicada por el contador de programa.
3. Decodifica y ejecuta la instrucción.
4. Si necesita un dato, lo solicita a la misma memoria (a través de la jerarquía).
5. Repite hasta terminar o ser interrumpida.

**Interpretación:** la flexibilidad viene de almacenar programas en memoria; el costo es la contención en el acceso.

### Práctica guiada
- Dibuja un diagrama con CPU, memoria, E/S y bus. Etiqueta dónde van instrucciones y datos.
- Señala en el diagrama dónde ocurre el cuello de botella.

### Actividad independiente
Explica con tus palabras por qué el programa almacenado fue un cambio importante frente a máquinas de propósito fijo.

### Criterios de aceptación
- Diagrama correcto.
- Define programa almacenado.
- Explica el cuello de botella sin exagerarlo.

### Errores frecuentes y recomendaciones
- **Error:** decir que Von Neumann está “obsoleto”. **Recomendación:** es un modelo base; los sistemas modernos lo extienden.
- **Error:** confundir Von Neumann con una marca o CPU específica. **Recomendación:** es un modelo arquitectónico.

### Evaluación de comprensión
1. ¿Qué significa programa almacenado?
2. ¿Qué comparten instrucciones y datos en Von Neumann?
3. ¿Qué es el cuello de botella de Von Neumann?

### Referencias
- Von Neumann, J. *First Draft of a Report on the EDVAC*, 1945. https://web.mit.edu/STS.035/www/PDFs/edvac.pdf. Consultado: 2026-11-24.
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*. Morgan Kaufmann.

---

## Lección 1.3.2 — Arquitectura Harvard

### Identificación
- **Lección oficial:** 1.3.2 — Arquitectura Harvard. **Secuencia:** 2/8.

### Propósito de aprendizaje
Comprender la arquitectura Harvard y compararla con Von Neumann.

### Conocimientos previos
- Lección 1.3.1.

### Resultados de aprendizaje
- Describir separación de memoria/caminos para instrucciones y datos.
- Comparar ventajas y limitaciones frente a Von Neumann.
- Identificar usos típicos (embebidos, DSP, caches modernas).

### Desarrollo conceptual
La arquitectura Harvard separa físicamente o lógicamente el almacenamiento y/o los buses de instrucciones y datos. Esto permite que la CPU lea una instrucción y acceda a datos al mismo tiempo, reduciendo la contención del modelo Von Neumann.

En la práctica, muchos sistemas modernos usan una **arquitectura Harvard modificada**: cachés separadas para instrucciones y datos (L1i/L1d), pero memoria principal unificada. Esto combina flexibilidad y rendimiento.

Harvard pura es común en microcontroladores y sistemas embebidos simples, donde el programa puede estar en memoria no volátil y los datos en RAM.

### Ejemplo técnico desarrollado
**Comparación:**

| Aspecto | Von Neumann | Harvard |
|---|---|---|
| Memoria | Instrucciones y datos compartidos | Separados |
| Buses | Compartidos (clásico) | Separados |
| Acceso simultáneo instrucción/dato | Limitado | Posible |
| Flexibilidad | Alta | Depende de implementación |
| Uso típico | PCs de propósito general | Embebidos, DSP, caches |

### Práctica guiada
- Completa la tabla anterior con un ejemplo real o hipotético para cada arquitectura.

### Actividad independiente
Investiga si tu CPU tiene caché L1 separada para instrucciones y datos. ¿Eso la hace Harvard pura? Justifica.

### Criterios de aceptación
- Explica separación instrucción/dato.
- Compara correctamente con Von Neumann.
- Reconoce Harvard modificada.

### Errores frecuentes y recomendaciones
- **Error:** clasificar sistemas modernos como puramente Harvard o Von Neumann. **Recomendación:** usar “Harvard modificada” cuando corresponda.
- **Error:** creer que Harvard elimina toda latencia de memoria. **Recomendación:** solo reduce un tipo de contención.

### Evaluación de comprensión
1. ¿Qué separa la arquitectura Harvard?
2. ¿Qué ventaja ofrece sobre Von Neumann?
3. ¿Qué es una Harvard modificada?

### Referencias
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*. Morgan Kaufmann.
- Arm. *Cortex-M Architecture*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.

---

## Lección 1.3.3 — Ciclo Fetch-Decode-Execute

### Identificación
- **Lección oficial:** 1.3.3 — Ciclo Fetch-Decode-Execute. **Secuencia:** 3/8.

### Propósito de aprendizaje
Comprender el ciclo básico de ejecución de instrucciones.

### Conocimientos previos
- Lecciones 1.3.1, 1.1.1-1.1.3.

### Resultados de aprendizaje
- Describir fases fetch, decode y execute.
- Explicar el rol del contador de programa y registros.
- Reconocer que es un modelo simplificado.
- Trazar un ciclo simple paso a paso.

### Desarrollo conceptual
El ciclo Fetch-Decode-Execute (FDE) describe cómo la CPU procesa instrucciones:

1. **Fetch:** la CPU obtiene la instrucción desde la dirección indicada por el Program Counter (PC).
2. **Decode:** la unidad de control interpreta la instrucción: qué operación es, qué operandos usa, dónde está el resultado.
3. **Execute:** se realiza la operación en la ALU/u otra unidad; puede implicar leer/escribir memoria o cambiar el PC.
4. **Writeback/Update:** en muchos modelos se incluye escribir el resultado y actualizar el PC.

Es un modelo simplificado. CPUs modernas usan pipelines, ejecución fuera de orden, predicción de saltos y paralelismo. Pero el FDE sigue siendo útil para entender la base.

### Ejemplo técnico desarrollado
**Instrucción:** `ADD R1, R2, R3` (R1 = R2 + R3).

1. **Fetch:** PC apunta a la dirección de la instrucción; se carga en el registro de instrucción.
2. **Decode:** se identifica operación ADD, operandos R2,R3, destino R1.
3. **Execute:** ALU suma valores de R2 y R3.
4. **Writeback:** resultado se escribe en R1; PC avanza a la siguiente instrucción.

### Práctica guiada
- Traza el ciclo FDE para `LOAD R1, [0x100]`.
- Indica qué componente participa en cada fase.

### Actividad independiente
Simula en papel 3 instrucciones consecutivas: LOAD, ADD, STORE. Muestra PC, IR y registros relevantes en cada paso.

### Criterios de aceptación
- Fases correctas.
- PC actualizado.
- Distingue fetch de execute.

### Errores frecuentes y recomendaciones
- **Error:** creer que FDE describe exactamente todas las CPUs modernas. **Recomendación:** presentarlo como modelo base.
- **Error:** olvidar actualización del PC. **Recomendación:** incluirlo explícitamente.
- **Error:** confundir decodificar con ejecutar. **Recomendación:** separar interpretación de acción.

### Evaluación de comprensión
1. ¿Qué ocurre en fetch?
2. ¿Qué rol tiene el PC?
3. ¿Por qué el FDE es una simplificación útil?

### Referencias
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Null, L., & Lobur, J. *Essentials of Computer Organization and Architecture*. Jones & Bartlett Learning.

---

## Lección 1.3.4 — Conjunto de instrucciones

### Identificación
- **Lección oficial:** 1.3.4 — Conjunto de instrucciones. **Secuencia:** 4/8.

### Propósito de aprendizaje
Comprender qué es una ISA y cómo define la interfaz entre software y hardware.

### Conocimientos previos
- Lecciones 1.1.1, 1.3.3.

### Resultados de aprendizaje
- Definir ISA (Instruction Set Architecture).
- Distinguir ISA y microarquitectura.
- Identificar tipos de instrucciones.
- Reconocer implicaciones de compatibilidad.

### Desarrollo conceptual
El **Instruction Set Architecture (ISA)** es el contrato que define qué instrucciones puede ejecutar un procesador, qué registros son visibles, cómo se direcciona memoria, qué tipos de datos soporta y cómo se comportan interrupciones/excepciones. Ejemplos: x86-64, ARMv8-A, RISC-V.

La **microarquitectura** es la implementación interna de la ISA: pipelines, cachés, ejecución fuera de orden, tamaño de buffers. Dos CPUs pueden implementar la misma ISA pero tener microarquitecturas diferentes y rendimiento distinto.

Tipos comunes de instrucciones: aritméticas/lógicas, transferencia de datos, control de flujo (saltos/llamadas), E/S y sistema.

### Ejemplo técnico desarrollado
**Compatibilidad:** un binario compilado para x86-64 no se ejecuta nativamente en ARM, porque la ISA es diferente. Puede requerir recompilación o emulación/traducción.

**Interpretación:** la ISA define compatibilidad de software a nivel binario.

### Práctica guiada
- Clasifica estas instrucciones hipotéticas: `MOV`, `ADD`, `JMP`, `CMP`, `LOAD`.
- Indica si pertenecen a transferencia, aritmética, control o comparación.

### Actividad independiente
Investiga una diferencia visible entre x86-64 y ARM (licencia, uso típico, o filosofía RISC/CISC) y explica por qué no significa que una sea “mejor” en todo.

### Criterios de aceptación
- Define ISA correctamente.
- Distingue ISA de microarquitectura.
- Explica implicación de compatibilidad.

### Errores frecuentes y recomendaciones
- **Error:** confundir ISA con lenguaje de programación. **Recomendación:** ISA es nivel máquina.
- **Error:** pensar que mismo ISA implica mismo rendimiento. **Recomendación:** la microarquitectura importa.
- **Error:** usar “RISC/CISC” como etiqueta absoluta moderna. **Recomendación:** matizar que las arquitecturas actuales combinan ideas.

### Evaluación de comprensión
1. ¿Qué define una ISA?
2. ¿Qué diferencia hay entre ISA y microarquitectura?
3. ¿Por qué un programa compilado para una ISA puede no funcionar en otra?

### Referencias
- Arm. *Learn the architecture*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.
- RISC-V International. *Specifications*. https://riscv.org/specifications/. Consultado: 2026-11-24.
- Intel. *Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.

---

## Lección 1.3.5 — Registros del procesador

### Identificación
- **Lección oficial:** 1.3.5 — Registros del procesador. **Secuencia:** 5/8.

### Propósito de aprendizaje
Profundizar en los tipos de registros y su rol en la ejecución.

### Conocimientos previos
- Lección 1.1.3, 1.3.3.

### Resultados de aprendizaje
- Identificar tipos comunes de registros.
- Explicar rol de PC, IR, SP y flags.
- Relacionar registros con el ciclo FDE.
- Reconocer variación por arquitectura.

### Desarrollo conceptual
Además de registros de propósito general, la CPU usa registros especiales:

- **PC (Program Counter):** dirección de la siguiente instrucción.
- **IR (Instruction Register):** instrucción actual cargada.
- **SP (Stack Pointer):** tope de la pila.
- **FLAGS/Status Register:** estado de operaciones (cero, carry, overflow, negativo).
- **Registros de propósito general:** operandos y resultados temporales.

Estos registros son visibles en distintos grados según el modelo. En programación de alto nivel, el compilador los asigna; en ensamblador, pueden manipularse directamente según la ISA.

### Ejemplo técnico desarrollado
**Condicional: `if (a == b)`**

1. Se cargan `a` y `b` en registros.
2. Se ejecuta comparación (CMP/SUB según ISA).
3. Se actualiza el flag Z (zero) si son iguales.
4. Una instrucción de salto condicional consulta el flag.
5. El PC cambia a la dirección del bloque correspondiente.

### Práctica guiada
- Crea una tabla con PC, IR, SP, FLAGS, R1. Describe su función en una frase.

### Actividad independiente
Explica qué pasaría si el PC no se actualizara correctamente tras una instrucción.

### Criterios de aceptación
- Identifica al menos 4 registros especiales.
- Relaciona flags con control de flujo.
- Describe consecuencia de PC incorrecto.

### Errores frecuentes y recomendaciones
- **Error:** pensar que hay un único conjunto de registros para todas las CPUs. **Recomendación:** depender de la ISA.
- **Error:** confundir SP con heap. **Recomendación:** SP apunta a pila, no a heap.

### Evaluación de comprensión
1. ¿Qué almacena el IR?
2. ¿Para qué sirve el flag zero?
3. ¿Qué registro indica la siguiente instrucción?

### Referencias
- Intel. *Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Arm. *Programmer's Guide*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.

---

## Lección 1.3.6 — Memoria

### Identificación
- **Lección oficial:** 1.3.6 — Memoria. **Secuencia:** 6/8.

### Propósito de aprendizaje
Comprender la memoria como componente arquitectónico para instrucciones y datos.

### Conocimientos previos
- Lecciones 1.1.7-1.1.9, 1.3.1.

### Resultados de aprendizaje
- Explicar rol de memoria en la arquitectura.
- Distinguir memoria principal, caché y almacenamiento.
- Comprender direccionamiento básico.
- Relacionar memoria con rendimiento.

### Desarrollo conceptual
En la arquitectura del computador, la memoria almacena instrucciones y datos necesarios para la ejecución. La **memoria principal** (RAM) es la zona de trabajo activa. La **caché** reduce latencia entre CPU y RAM. El **almacenamiento** (SSD/HDD) conserva datos persistentes, pero es más lento.

El direccionamiento permite ubicar datos. La CPU usa direcciones para leer/escribir. En sistemas modernos, la dirección virtual se traduce a física mediante MMU y tablas de páginas, lo que permite aislamiento y memoria virtual.

La jerarquía de memoria existe por el compromiso costo/velocidad/capacidad: lo más rápido es pequeño y caro; lo más grande es más lento y barato por bit.

### Ejemplo técnico desarrollado
**Acceso a dato:**
1. CPU solicita dirección X.
2. Busca en L1 → miss.
3. Busca en L2 → miss.
4. Busca en L3 → hit.
5. Se entrega dato a CPU y se copia en niveles superiores según política.

**Interpretación:** varios niveles intentan ocultar la latencia de RAM.

### Práctica guiada
- Dibuja la jerarquía de memoria y anota velocidad/capacidad relativa.

### Actividad independiente
Explica por qué aumentar RAM puede mejorar rendimiento en algunos casos pero no en otros.

### Criterios de aceptación
- Jerarquía correcta.
- Diferencia memoria principal y almacenamiento.
- Explica miss/hit a nivel básico.

### Errores frecuentes y recomendaciones
- **Error:** llamar “memoria” solo al disco. **Recomendación:** distinguir RAM y almacenamiento.
- **Error:** ignorar memoria virtual. **Recomendación:** mencionar que el SO puede usar disco como extensión.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre RAM y SSD en arquitectura?
2. ¿Qué es un cache hit?
3. ¿Por qué existe la jerarquía de memoria?

### Referencias
- Hennessy, J. L., & Patterson, D. A. *Computer Architecture: A Quantitative Approach*. Morgan Kaufmann.
- Microsoft Learn. *Windows memory management*. https://learn.microsoft.com/en-us/windows/win32/memory/memory-management. Consultado: 2026-11-24.

---

## Lección 1.3.7 — Entrada y salida

### Identificación
- **Lección oficial:** 1.3.7 — Entrada y salida. **Secuencia:** 7/8.

### Propósito de aprendizaje
Comprender cómo el sistema se comunica con dispositivos externos.

### Conocimientos previos
- Lecciones 1.1.16, 1.3.1, 1.3.6.

### Resultados de aprendizaje
- Definir subsistema de E/S.
- Distinguir E/S programada, por interrupciones y DMA a nivel básico.
- Explicar rol de controladores/drivers.
- Identificar cuellos de botella de E/S.

### Desarrollo conceptual
La entrada/salida (I/O) permite que el computador reciba datos y envíe resultados. Incluye teclados, discos, red, pantallas, sensores, etc. El subsistema de E/S involucra hardware (controladores, puertos, buses) y software (drivers, sistema operativo).

Modos básicos:
- **E/S programada (polling):** la CPU consulta repetidamente el estado del dispositivo. Simple, pero desperdicia CPU.
- **E/S por interrupciones:** el dispositivo avisa cuando está listo. Más eficiente.
- **DMA (Direct Memory Access):** un controlador transfiere datos entre dispositivo y memoria sin ocupar la CPU en cada byte. La CPU se libera para otras tareas.

Los drivers traducen solicitudes del SO a comandos del dispositivo. Sin driver adecuado, el dispositivo puede no funcionar correctamente.

### Ejemplo técnico desarrollado
**Lectura de disco:**
1. Aplicación pide leer archivo.
2. SO solicita al driver.
3. Controlador inicia lectura.
4. Datos se transfieren a memoria por DMA.
5. Controlador genera interrupción al finalizar.
6. SO entrega datos a la aplicación.

### Práctica guiada
- Compara polling vs interrupciones en una tabla: uso de CPU, complejidad, latencia/respuesta.

### Actividad independiente
Identifica un dispositivo de tu equipo y describe qué tipo de E/S sería más eficiente para él.

### Criterios de aceptación
- Define E/S y menciona 3 modos.
- Explica DMA correctamente.
- Relaciona driver con dispositivo.

### Errores frecuentes y recomendaciones
- **Error:** creer que la CPU siempre mueve todos los datos. **Recomendación:** incluir DMA.
- **Error:** confundir driver con aplicación. **Recomendación:** driver es software de interfaz con hardware.

### Evaluación de comprensión
1. ¿Qué ventaja tiene DMA?
2. ¿Qué problema tiene el polling?
3. ¿Qué es un driver?

### Referencias
- Silberschatz, A., et al. *Operating System Concepts*. Wiley.
- Linux Kernel Documentation. *DMA*. https://www.kernel.org/doc/html/latest/core-api/dma-api.html. Consultado: 2026-11-24.

---

## Lección 1.3.8 — Interrupciones

### Identificación
- **Lección oficial:** 1.3.8 — Interrupciones. **Secuencia:** 8/8.

### Propósito de aprendizaje
Comprender cómo las interrupciones permiten responder a eventos sin espera activa.

### Conocimientos previos
- Lecciones 1.3.3, 1.3.7.

### Resultados de aprendizaje
- Definir interrupción y excepción.
- Explicar el flujo básico de manejo.
- Distinguir interrupciones hardware/software.
- Reconocer importancia para multitarea y E/S.

### Desarrollo conceptual
Una **interrupción** es una señal que altera el flujo normal de ejecución para atender un evento. Puede ser de hardware (teclado, red, disco) o de software (llamada al sistema, instrucción especial). Las **excepciones** suelen generarse por condiciones durante la ejecución: división por cero, fallo de página, instrucción inválida.

Flujo básico:
1. Se recibe la interrupción.
2. CPU guarda estado mínimo (PC, flags, registros necesarios).
3. Se identifica el vector/manejador.
4. Se ejecuta la rutina de servicio (ISR).
5. Se restaura estado y se reanuda la ejecución.

Las interrupciones permiten eficiencia: en lugar de hacer polling, la CPU trabaja en otras tareas y responde cuando llega el evento. También son base para planificación del sistema operativo.

### Ejemplo técnico desarrollado
**Llegada de paquete de red:**
1. NIC recibe paquete y genera interrupción.
2. CPU pausa tarea actual, guarda contexto.
3. ISR/driver procesa el evento o programa procesamiento posterior.
4. CPU restaura contexto y continúa.

### Práctica guiada
- Dibuja el flujo de manejo de interrupción en 5 pasos.

### Actividad independiente
Da un ejemplo de interrupción de hardware y uno de excepción de software. Explica la diferencia.

### Criterios de aceptación
- Define interrupción y excepción.
- Describe flujo correcto.
- Da ejemplos adecuados.

### Errores frecuentes y recomendaciones
- **Error:** confundir interrupción con error siempre. **Recomendación:** muchas interrupciones son eventos normales.
- **Error:** pensar que la ISR debe hacer todo el trabajo pesado. **Recomendación:** suele diferir trabajo al kernel/colas.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre interrupción y excepción?
2. ¿Por qué las interrupciones mejoran eficiencia frente a polling?
3. ¿Qué se debe guardar antes de atender una interrupción?

### Referencias
- Intel. *Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Silberschatz, A., et al. *Operating System Concepts*. Wiley.

---

## Cierre del módulo
- **Evaluación:** trazar FDE, comparar Von Neumann/Harvard, explicar ISA, describir interrupción.
- **Criterio:** 75% y explicación coherente de flujo de ejecución.