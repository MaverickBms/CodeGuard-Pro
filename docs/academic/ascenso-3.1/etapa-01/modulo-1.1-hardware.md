# Etapa 1 · Módulo 1.1 — Hardware

**Estado:** borrador académico desarrollado (contenido didáctico; pendiente validación editorial externa y ejecución/revisión técnica formal).  
**Alineación:** ASCENSO 3.1, Etapa 1 «Fundamentos de computación y arquitectura del computador», Módulo 1.1.  
**Prioridad de etapa:** P1 · Obligatoria.  
**Ruta de ubicación:** `docs/academic/ascenso-3.1/etapa-01/modulo-1.1-hardware.md`  
**Última actualización:** 2026-11-24

## Identificación del módulo

- **Etapa:** 1 — Fundamentos de computación y arquitectura del computador.
- **Objetivo oficial de la etapa:** comprender cómo funciona físicamente y lógicamente un computador.
- **Módulo:** 1.1 — Hardware.
- **Lecciones oficiales:** 16 (1.1.1 a 1.1.16).
- **Prerrequisitos curriculares:** ningún prerrequisito oficial de etapa; se recomienda haber completado la Etapa 0 para método de estudio y documentación técnica.

## Propósito del módulo

Este módulo explica los componentes físicos principales de un computador y su función dentro del sistema. Su objetivo no es formar técnicos de reparación, sino dar al estudiante una base correcta para entender rendimiento, compatibilidad, diagnóstico básico, arquitectura y decisiones de software que dependen del hardware.

## Resultados de aprendizaje del módulo

Al finalizar, el estudiante podrá:

1. Identificar los componentes físicos principales de un computador y describir su función.
2. Distinguir CPU, ALU, registros, núcleos, hilos, frecuencia y caché sin confundir conceptos.
3. Comparar memorias y dispositivos de almacenamiento según volatilidad, latencia, capacidad y uso.
4. Explicar el papel de motherboard, buses, fuente de alimentación y periféricos.
5. Interpretar especificaciones básicas de hardware con criterio técnico y sin simplificaciones engañosas.

## Criterios de avance del módulo

El módulo se considera estudiado cuando el estudiante puede describir cada componente, relacionarlo con el flujo de información, resolver ejercicios de identificación/comparación y justificar decisiones simples de compatibilidad o diagnóstico.

---

## Lección 1.1.1 — CPU (Unidad Central de Procesamiento)

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.1 — CPU (Unidad Central de Procesamiento).
- **Secuencia:** 1 de 16 en el módulo.

### Propósito de aprendizaje
Comprender qué es la CPU, qué hace realmente dentro del computador y por qué su rendimiento no depende de un único valor.

### Conocimientos previos
- Diferencia básica entre hardware y software.
- Idea general de que un programa es una secuencia de instrucciones.

### Resultados de aprendizaje
- Definir CPU con precisión técnica.
- Describir las funciones generales de ejecución, control y coordinación.
- Distinguir CPU de otros componentes como GPU, RAM o disco.
- Explicar por qué la CPU no “piensa” como una persona.

### Desarrollo conceptual
La CPU (Central Processing Unit) es el componente encargado de ejecutar instrucciones de máquina y coordinar gran parte del procesamiento del sistema. Recibe instrucciones desde la jerarquía de memoria, las interpreta mediante su lógica de control y ejecuta operaciones usando unidades internas como la ALU, unidades de punto flotante, registros y mecanismos de control de flujo.

La CPU no trabaja sola. Depende de la memoria para obtener instrucciones y datos, del chipset/motherboard para comunicarse con otros dispositivos, del sistema operativo para la planificación de tareas y de subsistemas de entrada/salida para interactuar con el exterior. Por eso, un computador lento no siempre tiene una “CPU mala”: puede haber cuellos de botella en RAM, almacenamiento, GPU, temperatura o software.

Funciones típicas de la CPU:
- **Búsqueda y decodificación:** obtener instrucciones y determinar qué operación realizar.
- **Ejecución:** realizar cálculos, comparaciones, saltos o accesos a memoria.
- **Control:** gestionar el flujo de instrucciones, interrupciones y estado del procesador.
- **Coordinación:** interactuar con memoria y dispositivos mediante buses e interfaces.

La CPU ejecuta instrucciones según un conjunto de instrucciones (ISA), como x86-64 o ARM. La ISA define qué instrucciones entiende el procesador; la microarquitectura define cómo las implementa internamente.

### Ejemplo técnico desarrollado
**Escenario:** abrir una calculadora y ejecutar `128 + 256`.

1. El sistema operativo carga el programa en memoria y planifica su ejecución.
2. La CPU obtiene instrucciones del programa desde la memoria/caché.
3. La lógica de control decodifica la instrucción de suma.
4. Los operandos se colocan en registros o se leen desde memoria.
5. Una unidad aritmética calcula el resultado.
6. El resultado se guarda en un registro/memoria y luego se envía a la interfaz para mostrarse.

**Interpretación:** la operación visible es simple, pero involucra coordinación entre CPU, memoria, sistema operativo y subsistema gráfico/entrada-salida. La CPU ejecuta instrucciones; no comprende el significado humano de “sumar”.

### Práctica guiada
- **Objetivo:** identificar la CPU del equipo y relacionarla con su función.
- **Herramientas:** sistema operativo actual; en Linux: `lscpu`; en Windows: Administrador de tareas > Rendimiento > CPU o `Get-CimInstance Win32_Processor`.
- **Procedimiento:**
  1. Ejecuta el comando/herramienta disponible.
  2. Anota modelo, arquitectura, núcleos e hilos si aparecen.
  3. Escribe una frase describiendo qué hace la CPU en ese equipo.
  4. Escribe otra frase indicando qué no puede deducirse solo con ese dato.
- **Resultado esperado:** una ficha breve con datos observados y una interpretación correcta.
- **Verificación:** el estudiante no afirma “es rápida/lenta” solo por el nombre comercial.

### Actividad independiente
Elige dos dispositivos distintos (por ejemplo, portátil y teléfono). Investiga qué CPU usan y elabora una tabla con modelo, arquitectura, uso previsto y una limitación de la comparación.

### Criterios de aceptación
- Define CPU sin confundirla con memoria o disco.
- Menciona al menos dos funciones reales de la CPU.
- Incluye una limitación o dependencia de otro componente.
- La tabla compara con cautela, sin conclusiones absolutas.

### Errores frecuentes y recomendaciones
- **Error:** llamar CPU a toda la torre o gabinete. **Recomendación:** distinguir carcasa, placa base y procesador.
- **Error:** creer que más GHz siempre significa mejor. **Recomendación:** considerar arquitectura, núcleos, caché, carga y térmicas.
- **Error:** pensar que la CPU almacena archivos permanentemente. **Recomendación:** separar procesamiento de almacenamiento.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre ejecutar una instrucción y “entender” un problema?
2. Si una aplicación tarda en abrir, ¿qué evidencias buscarías antes de culpar a la CPU?
3. ¿Por qué la ISA es relevante para la compatibilidad de software?

### Referencias
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Arm. *Arm Architecture Reference Manuals*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*. Morgan Kaufmann. Referencia académica de apoyo para organización de computadores.

---

## Lección 1.1.2 — ALU (Unidad Aritmético-Lógica)

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.2 — ALU (Unidad Aritmético-Lógica).
- **Secuencia:** 2 de 16 en el módulo.

### Propósito de aprendizaje
Entender la función de la ALU como unidad de cálculo y comparación dentro del procesador.

### Conocimientos previos
- Lección 1.1.1.
- Nociones básicas de suma, resta y comparaciones.

### Resultados de aprendizaje
- Definir ALU y su rol dentro de la CPU.
- Diferenciar operaciones aritméticas y lógicas.
- Explicar cómo una comparación simple depende de operaciones de la ALU.
- Reconocer que la ALU no controla todo el procesador.

### Desarrollo conceptual
La ALU (Arithmetic Logic Unit) es una unidad funcional del procesador que realiza operaciones aritméticas y lógicas. Entre las operaciones aritméticas comunes están suma, resta, incremento y, según el diseño, operaciones soportadas por circuitos específicos. Entre las operaciones lógicas están AND, OR, NOT, XOR y comparaciones que producen resultados usados por decisiones de control.

La ALU recibe operandos, ejecuta la operación indicada por la instrucción/control y produce un resultado. Además, suele afectar banderas o flags (cero, acarreo, desbordamiento, negativo), que la lógica de control usa para decidir saltos condicionales.

No debe confundirse con la CPU completa. La CPU incluye control, registros, caches, interfaces y otras unidades de ejecución. En procesadores modernos puede haber varias ALU o unidades funcionales especializadas.

### Ejemplo técnico desarrollado
**Escenario:** evaluar la condición `edad >= 18`.

1. El valor de `edad` se carga en un registro, por ejemplo `20`.
2. El valor `18` se coloca en otro registro o se provee como inmediato.
3. La ALU realiza una comparación/resta interna según la ISA.
4. Se actualizan flags: por ejemplo, si el resultado no es negativo según la representación, la condición se cumple.
5. La unidad de control usa el flag para decidir si ejecuta el bloque “permitir acceso” o el bloque alternativo.

**Interpretación:** una decisión de alto nivel en un programa se apoya en operaciones lógicas/aritméticas de bajo nivel.

### Práctica guiada
- **Objetivo:** clasificar operaciones en aritméticas o lógicas.
- **Procedimiento:**
  1. Crea una tabla con estas operaciones: `5+3`, `10-2`, `A AND B`, `NOT verdadero`, `x > y`, `7 XOR 3`.
  2. Clasifica cada una como aritmética, lógica o comparación.
  3. Explica qué tipo de resultado produce (número, booleano/bit, flag).
- **Resultado esperado:** tabla completa con clasificación justificada.
- **Verificación:** el estudiante identifica que las comparaciones alimentan decisiones.

### Actividad independiente
Diseña 6 expresiones propias (2 aritméticas, 2 lógicas, 2 comparaciones) y describe un caso de software donde cada una sería útil.

### Criterios de aceptación
- Define ALU correctamente.
- Clasifica operaciones sin confundir categorías.
- Explica la relación entre comparación y decisión de control.
- Presenta ejemplos propios pertinentes.

### Errores frecuentes y recomendaciones
- **Error:** decir que la ALU ejecuta todo el programa. **Recomendación:** limitarla a operaciones aritméticas/lógicas y resultados asociados.
- **Error:** confundir operación lógica con lógica de negocio. **Recomendación:** distinguir bits/booleanos de reglas de aplicación.
- **Error:** ignorar flags. **Recomendación:** recordar que el resultado de una comparación suele usarse para control de flujo.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre `OR` lógico y una suma aritmética?
2. ¿Por qué una comparación puede influir en un `if`?
3. Da un ejemplo donde la ALU produzca un valor numérico y otro donde produzca un resultado usado como condición.

### Referencias
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Null, L., & Lobur, J. *The Essentials of Computer Organization and Architecture*. Jones & Bartlett Learning. Referencia académica de apoyo.

---

## Lección 1.1.3 — Registros

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.3 — Registros.
- **Secuencia:** 3 de 16 en el módulo.

### Propósito de aprendizaje
Comprender qué son los registros y por qué son críticos para la velocidad de ejecución de la CPU.

### Conocimientos previos
- Lecciones 1.1.1 y 1.1.2.
- Idea básica de memoria y dato.

### Resultados de aprendizaje
- Definir registro como almacenamiento interno de alta velocidad.
- Diferenciar registros de RAM y caché.
- Explicar ejemplos de uso de registros durante la ejecución.
- Reconocer que el conjunto de registros depende de la arquitectura.

### Desarrollo conceptual
Los registros son ubicaciones de almacenamiento muy pequeñas y extremadamente rápidas dentro del procesador. Se usan para mantener datos inmediatos: operandos, direcciones, resultados temporales, punteros de instrucción o información de estado.

A diferencia de la RAM, los registros no están diseñados para almacenar grandes volúmenes de datos de usuario. Su cantidad es limitada y su acceso está integrado al ciclo de ejecución. A diferencia de la caché, que almacena copias de bloques de memoria para reducir latencias, los registros son operados directamente por instrucciones.

Existen distintos tipos, según arquitectura: registros de propósito general, de punto flotante, de instrucción, de pila, de estado/flags, entre otros. El programador de alto nivel normalmente no los gestiona de forma directa, pero el compilador y el sistema sí dependen de ellos.

### Ejemplo técnico desarrollado
**Escenario:** ejecutar `a = b + c`.

1. El valor de `b` se carga desde memoria a un registro.
2. El valor de `c` se carga a otro registro.
3. La ALU suma ambos registros.
4. El resultado se escribe en un registro.
5. El contenido se almacena en la dirección de memoria asociada a `a`.

**Interpretación:** aunque en código fuente se vea una línea, el procesador usa registros como espacio de trabajo inmediato.

### Práctica guiada
- **Objetivo:** visualizar el rol de registros en una operación.
- **Procedimiento:**
  1. Dibuja cuatro cajas: `R1`, `R2`, `R3`, `Memoria[a]`.
  2. Asigna valores de ejemplo a `b` y `c`.
  3. Simula paso a paso la operación anterior.
  4. Indica en qué paso el dato está en memoria y en cuál está en registro.
- **Resultado esperado:** diagrama simple de flujo de datos.
- **Verificación:** el estudiante no coloca el “archivo completo” en un registro.

### Actividad independiente
Investiga el nombre de dos registros en x86-64 o ARM (según la fuente que elijas) y describe su propósito con tus propias palabras, citando la documentación.

### Criterios de aceptación
- Define registro correctamente.
- Diferencia registro, caché y RAM.
- El diagrama muestra movimiento de datos coherente.
- La actividad independiente cita una fuente oficial.

### Errores frecuentes y recomendaciones
- **Error:** confundir registro con registro de base de datos. **Recomendación:** aclarar el contexto: hardware CPU.
- **Error:** creer que más registros siempre se ven directamente como “más GB”. **Recomendación:** separar capacidad de memoria masiva de almacenamiento interno de CPU.
- **Error:** asumir los mismos registros en todas las arquitecturas. **Recomendación:** mencionar la ISA.

### Evaluación de comprensión
1. ¿Por qué la CPU usa registros en lugar de operar siempre directamente sobre RAM?
2. ¿Qué diferencia funcional hay entre un registro y una caché L1?
3. ¿Qué puede cambiar entre arquitecturas respecto a los registros?

### Referencias
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Arm. *AArch64 Registers*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.

---

## Lección 1.1.4 — Núcleos

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.4 — Núcleos.
- **Secuencia:** 4 de 16 en el módulo.

### Propósito de aprendizaje
Entender qué es un núcleo de CPU y cómo influye en el paralelismo.

### Conocimientos previos
- Lecciones 1.1.1 a 1.1.3.

### Resultados de aprendizaje
- Definir núcleo de procesamiento.
- Explicar la diferencia entre un procesador de un núcleo y uno multinúcleo.
- Identificar cuándo más núcleos pueden ayudar.
- Reconocer límites del paralelismo.

### Desarrollo conceptual
Un núcleo es una unidad de procesamiento dentro de la CPU capaz de ejecutar instrucciones. Un procesador multinúcleo integra varios núcleos en un mismo chip o paquete, lo que permite ejecutar múltiples flujos de trabajo simultáneamente, siempre que el software y el sistema operativo puedan distribuirlos.

Más núcleos no equivalen automáticamente a más velocidad en todas las tareas. Algunas aplicaciones son secuenciales: dependen de pasos que deben ocurrir uno tras otro. Otras son paralelizables: compilación, renderizado, compresión, análisis de datos o servidores con múltiples solicitudes.

También importa el equilibrio: frecuencia, caché, temperatura, consumo, memoria y diseño del software. Un núcleo rápido puede superar a varios núcleos lentos en tareas de un solo hilo.

### Ejemplo técnico desarrollado
**Escenario:** exportar 100 imágenes.

- **Caso A:** programa de un solo hilo. Usa principalmente un núcleo; los demás quedan poco aprovechados.
- **Caso B:** programa que procesa 4 imágenes en paralelo. En una CPU de 4 núcleos, puede reducir el tiempo total, si el disco y la RAM no se convierten en cuello de botella.

**Interpretación:** el beneficio depende de la capacidad del software para dividir el trabajo y de los recursos compartidos.

### Práctica guiada
- **Objetivo:** observar uso de núcleos.
- **Herramientas:** Monitor de sistema / Administrador de tareas / `htop` o `top`.
- **Procedimiento:**
  1. Abre el monitor de recursos.
  2. Observa el gráfico por núcleo en reposo.
  3. Ejecuta una tarea exigente (por ejemplo, compresión o navegador con varias pestañas, si es seguro).
  4. Anota si la carga se reparte o se concentra.
- **Resultado esperado:** observación básica de distribución de carga.
- **Verificación:** el estudiante describe lo observado, no lo que supone.

### Actividad independiente
Elige una aplicación que uses (editor, navegador, juego, IDE). Investiga si se beneficia de múltiples núcleos y explica por qué.

### Criterios de aceptación
- Define núcleo correctamente.
- Explica una ventaja y un límite del multinúcleo.
- Relaciona la carga observada con el tipo de tarea.
- La actividad independiente usa una fuente técnica o documentación del software.

### Errores frecuentes y recomendaciones
- **Error:** “8 núcleos = 8 veces más rápido”. **Recomendación:** explicar paralelismo y overhead.
- **Error:** confundir núcleo con procesador físico separado. **Recomendación:** aclarar que varios núcleos pueden estar en el mismo chip.
- **Error:** ignorar el software. **Recomendación:** evaluar si la aplicación está optimizada para paralelismo.

### Evaluación de comprensión
1. ¿Cuándo puede ser más útil un núcleo rápido que muchos núcleos?
2. ¿Qué necesita el software para aprovechar varios núcleos?
3. Da un ejemplo de tarea paralelizable y otra poco paralelizable.

### Referencias
- Intel. *Intel® Hyper-Threading Technology / CPU concepts*. https://www.intel.com/content/www/us/en/gaming/resources/hyper-threading.html. Consultado: 2026-11-24.
- Patterson, D. A., & Hennessy, J. L. *Computer Organization and Design*. Morgan Kaufmann.

---

## Lección 1.1.5 — Hilos de ejecución

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.5 — Hilos de ejecución.
- **Secuencia:** 5 de 16 en el módulo.

### Propósito de aprendizaje
Distinguir hilos de hardware y software, y comprender cómo se relacionan con los núcleos.

### Conocimientos previos
- Lección 1.1.4.
- Noción básica de programa en ejecución.

### Resultados de aprendizaje
- Definir hilo de ejecución en contexto de software.
- Explicar qué es un hilo de hardware / multithreading simultáneo a nivel básico.
- Diferenciar núcleo, hilo de software y hilo de hardware.
- Identificar riesgos de confundir métricas comerciales con rendimiento real.

### Desarrollo conceptual
Un **hilo de software** es una secuencia de ejecución dentro de un proceso. Un proceso puede tener uno o varios hilos; los hilos comparten recursos del proceso, como memoria, pero tienen su propio flujo de ejecución.

Un **hilo de hardware** es una capacidad del procesador para mantener más de un contexto de ejecución por núcleo, según la implementación. Tecnologías como SMT (Simultaneous Multithreading) permiten que un núcleo aproveche mejor sus unidades internas cuando un hilo está esperando recursos. Esto no equivale a duplicar físicamente el núcleo.

Por eso, ver “8 núcleos / 16 hilos” no significa 16 núcleos físicos. Significa, normalmente, 8 núcleos con 2 hilos de hardware por núcleo.

### Ejemplo técnico desarrollado
**Escenario:** un editor de texto guarda un archivo mientras el usuario sigue escribiendo.

- El hilo A atiende la interfaz y el teclado.
- El hilo B guarda el archivo en segundo plano.
- Ambos pertenecen al mismo proceso y comparten datos, pero ejecutan tareas distintas.

Si el CPU tiene SMT, el sistema operativo puede planificar hilos de software sobre hilos de hardware disponibles, mejorando el aprovechamiento. Si la tarea es intensiva en la misma unidad interna, la ganancia puede ser limitada.

### Práctica guiada
- **Objetivo:** diferenciar conceptos en una tabla.
- **Procedimiento:** completa una tabla con columnas: Concepto, Qué es, Ejemplo, Error común.
- **Filas:** núcleo, hilo de software, hilo de hardware.
- **Resultado esperado:** tabla clara y sin confundir niveles.
- **Verificación:** el estudiante indica que el hilo de hardware no es igual a núcleo físico.

### Actividad independiente
Describe un caso donde usar varios hilos de software sea útil y un riesgo que se debe controlar (por ejemplo, acceso simultáneo a datos).

### Criterios de aceptación
- Define correctamente los tres conceptos.
- Distingue software y hardware.
- Identifica un beneficio y un riesgo de concurrencia.

### Errores frecuentes y recomendaciones
- **Error:** asumir que más hilos siempre mejoran todo. **Recomendación:** evaluar tipo de carga y contención de recursos.
- **Error:** usar “hilo” sin especificar contexto. **Recomendación:** indicar si es de software, hardware o ejecución.
- **Error:** ignorar sincronización. **Recomendación:** mencionar que compartir memoria requiere control.

### Evaluación de comprensión
1. ¿Qué diferencia hay entre un proceso y un hilo de software?
2. ¿Por qué 16 hilos no son necesariamente 16 núcleos?
3. ¿Qué problema puede aparecer cuando dos hilos modifican el mismo dato?

### Referencias
- Intel. *Hyper-Threading Technology*. https://www.intel.com/content/www/us/en/gaming/resources/hyper-threading.html. Consultado: 2026-11-24.
- Silberschatz, A., Galvin, P. B., & Gagne, G. *Operating System Concepts*. Wiley. Referencia de apoyo para procesos e hilos.

---

## Lección 1.1.6 — Frecuencia

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.6 — Frecuencia.
- **Secuencia:** 6 de 16 en el módulo.

### Propósito de aprendizaje
Interpretar correctamente la frecuencia de la CPU y sus límites como métrica de rendimiento.

### Conocimientos previos
- Lecciones 1.1.1 a 1.1.5.

### Resultados de aprendizaje
- Definir frecuencia de reloj en Hz/GHz.
- Explicar la diferencia entre frecuencia base, turbo y sostenida.
- Reconocer que frecuencia no equivale a instrucciones por segundo.
- Evaluar especificaciones sin simplificación excesiva.

### Desarrollo conceptual
La frecuencia indica cuántos ciclos por segundo realiza el reloj de un componente, comúnmente expresada en GHz para CPUs modernas. Un ciclo es una unidad temporal interna; la cantidad de trabajo útil por ciclo depende de la arquitectura y del tipo de instrucción.

Los fabricantes pueden indicar frecuencia base y frecuencias turbo/boost. La frecuencia turbo puede alcanzarse bajo ciertas condiciones de temperatura, energía y carga. La frecuencia sostenida real depende del sistema de refrigeración, diseño térmico y límites de potencia.

Por tanto, comparar CPUs solo por GHz es insuficiente. Dos procesadores con la misma frecuencia pueden tener rendimientos muy distintos por diferencias en IPC (instrucciones por ciclo), caché, núcleos, arquitectura y optimizaciones.

### Ejemplo técnico desarrollado
**Escenario:** CPU A: 3.6 GHz, 4 núcleos; CPU B: 3.2 GHz, 8 núcleos, arquitectura más reciente.

- En una tarea de un solo hilo, CPU A podría competir o ganar si su IPC/frecuencia sostenida es mejor.
- En una tarea paralela bien optimizada, CPU B podría ganar por más núcleos y mejor eficiencia.

**Interpretación:** la decisión correcta depende de la carga de trabajo, no de una sola cifra.

### Práctica guiada
- **Objetivo:** leer una especificación de CPU.
- **Procedimiento:**
  1. Busca la ficha oficial de una CPU.
  2. Anota frecuencia base, turbo/boost, núcleos e hilos.
  3. Escribe dos preguntas que aún no puedes responder solo con esos datos (por ejemplo, consumo real, rendimiento en tu aplicación).
- **Resultado esperado:** lectura crítica de especificaciones.
- **Verificación:** incluye al menos una limitación de la métrica.

### Actividad independiente
Compara dos CPUs oficiales y redacta una recomendación para un caso concreto: oficina, edición de video o desarrollo. Justifica con al menos tres criterios.

### Criterios de aceptación
- Define GHz correctamente.
- Distingue base/turbo/sostenida.
- No usa la frecuencia como único criterio.
- La recomendación considera el caso de uso.

### Errores frecuentes y recomendaciones
- **Error:** “Más GHz = siempre mejor”. **Recomendación:** incluir IPC, núcleos, caché y carga.
- **Error:** confundir frecuencia máxima con frecuencia constante. **Recomendación:** considerar térmicas y energía.
- **Error:** comparar GHz entre generaciones sin contexto. **Recomendación:** usar benchmarks o documentación relevante.

### Evaluación de comprensión
1. ¿Qué mide un GHz?
2. ¿Por qué la frecuencia turbo puede no mantenerse?
3. ¿Qué otros datos mirarías antes de elegir una CPU?

### Referencias
- Intel. *CPU Speed: What Is CPU Clock Speed?*. https://www.intel.com/content/www/us/en/gaming/resources/cpu-clock-speed.html. Consultado: 2026-11-24.
- AMD. *Processor Specifications*. https://www.amd.com/en/products/specifications/processors.html. Consultado: 2026-11-24.

---

## Lección 1.1.7 — Caché L1, L2 y L3

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.7 — Caché L1, L2 y L3.
- **Secuencia:** 7 de 16 en el módulo.

### Propósito de aprendizaje
Comprender la jerarquía de caché y su impacto en la latencia de acceso a datos.

### Conocimientos previos
- Lecciones 1.1.1 a 1.1.6.
- Diferencia básica entre memoria rápida y lenta.

### Resultados de aprendizaje
- Explicar qué es la caché y por qué existe.
- Diferenciar L1, L2 y L3 a nivel conceptual.
- Relacionar localidad temporal y espacial con caché.
- Evitar afirmaciones absolutas sobre implementaciones específicas.

### Desarrollo conceptual
La caché es una memoria pequeña y rápida que almacena copias de datos o instrucciones que probablemente se usarán pronto. Su objetivo es reducir el tiempo de acceso respecto a la RAM, que es mayor en capacidad pero más lenta.

La jerarquía típica incluye:
- **L1:** muy pequeña y muy rápida; suele estar cerca del núcleo, a veces separada en instrucciones y datos.
- **L2:** mayor que L1, algo más lenta; puede ser por núcleo o compartida según diseño.
- **L3:** mayor y normalmente más lenta que L2; frecuentemente compartida entre núcleos.

La efectividad de la caché se basa en principios de localidad:
- **Localidad temporal:** si se usa un dato, es probable que se vuelva a usar pronto.
- **Localidad espacial:** si se accede a una dirección, es probable que se acceda a direcciones cercanas.

Las características exactas varían por procesador. Por eso se debe consultar la especificación del modelo concreto.

### Ejemplo técnico desarrollado
**Escenario:** un bucle suma elementos de un arreglo.

1. La CPU solicita el primer elemento; si no está en caché, se trae desde RAM y se guarda una línea de caché.
2. Los elementos cercanos llegan en la misma línea, aprovechando localidad espacial.
3. El bucle reutiliza variables de control, aprovechando localidad temporal.
4. Si los datos caben y se acceden de forma predecible, hay menos esperas a RAM.

**Interpretación:** la caché no “hace magia”; mejora el rendimiento cuando el patrón de acceso es favorable.

### Práctica guiada
- **Objetivo:** relacionar niveles de memoria con latencia y capacidad.
- **Procedimiento:** ordena de mayor a menor velocidad y de mayor a menor capacidad: registros, L1, L2, L3, RAM, SSD.
- **Resultado esperado:** dos listas coherentes.
- **Verificación:** el estudiante explica el compromiso velocidad/capacidad/costo.

### Actividad independiente
Investiga el tamaño de caché L1/L2/L3 de una CPU actual y explica cómo presentarías esos datos sin prometer un porcentaje exacto de mejora.

### Criterios de aceptación
- Define caché y niveles L1/L2/L3.
- Explica localidad temporal y espacial.
- Ordena correctamente la jerarquía.
- Evita promesas de rendimiento sin contexto.

### Errores frecuentes y recomendaciones
- **Error:** creer que L3 siempre es por núcleo. **Recomendación:** verificar diseño del procesador.
- **Error:** confundir caché con RAM. **Recomendación:** diferenciar propósito, tamaño y latencia.
- **Error:** asumir que más caché siempre compensa todo. **Recomendación:** considerar carga de trabajo.

### Evaluación de comprensión
1. ¿Por qué existe más de un nivel de caché?
2. ¿Qué es localidad espacial?
3. ¿En qué caso la caché puede no ayudar mucho?

### Referencias
- Intel. *Memory and Cache*. https://www.intel.com/content/www/us/en/developer/articles/technical/memory-and-cache.html. Consultado: 2026-11-24.
- Hennessy, J. L., & Patterson, D. A. *Computer Architecture: A Quantitative Approach*. Morgan Kaufmann.

---

## Lección 1.1.8 — RAM

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.8 — RAM.
- **Secuencia:** 8 de 16 en el módulo.

### Propósito de aprendizaje
Comprender el rol de la RAM como memoria principal de trabajo del sistema.

### Conocimientos previos
- Lecciones 1.1.1, 1.1.7.
- Diferencia entre almacenamiento temporal y persistente.

### Resultados de aprendizaje
- Definir RAM y volatilidad.
- Explicar qué tipo de datos residen en RAM durante la ejecución.
- Diferenciar capacidad, velocidad y latencia.
- Identificar síntomas comunes de falta de RAM sin diagnosticar en exceso.

### Desarrollo conceptual
La RAM (Random Access Memory) es la memoria principal de trabajo utilizada por el sistema operativo y las aplicaciones para mantener datos e instrucciones en uso. Es generalmente volátil: su contenido se pierde al apagar el equipo.

La capacidad de RAM (por ejemplo, 8 GB, 16 GB) indica cuánto puede mantenerse en memoria de trabajo. La velocidad y latencia también importan, pero su impacto depende del sistema y la carga. Tener más RAM permite manejar más datos o aplicaciones simultáneamente, hasta cierto punto; si una aplicación usa poca memoria, agregar más RAM no la acelerará significativamente.

Cuando la RAM disponible es insuficiente, el sistema puede usar memoria virtual/swap en disco, lo cual suele ser mucho más lento. Esto puede causar lentitud, pero no es la única causa posible.

### Ejemplo técnico desarrollado
**Escenario:** abrir navegador con muchas pestañas, un editor y una máquina virtual.

1. Cada aplicación solicita memoria para código, datos y cachés.
2. El sistema operativo asigna páginas de RAM.
3. Si la RAM se llena, el sistema puede mover páginas menos usadas a swap.
4. El usuario percibe lentitud al cambiar de aplicación.

**Interpretación:** la RAM afecta la multitarea y la capacidad de trabajo activo; el diagnóstico debe considerar también CPU, disco y comportamiento de la aplicación.

### Práctica guiada
- **Objetivo:** observar uso de memoria.
- **Procedimiento:**
  1. Abre el monitor del sistema.
  2. Anota RAM total, usada y disponible.
  3. Abre una aplicación pesada y observa el cambio.
  4. Cierra la aplicación y observa la recuperación.
- **Resultado esperado:** registro de observación con valores antes/después.
- **Verificación:** el estudiante no confunde RAM usada con RAM “dañada”.

### Actividad independiente
Elabora una recomendación de RAM para dos perfiles: estudiante de ofimática y estudiante de desarrollo con máquinas virtuales. Justifica la diferencia.

### Criterios de aceptación
- Define RAM y volatilidad correctamente.
- Interpreta métricas básicas de uso.
- Distingue capacidad de velocidad.
- La recomendación se ajusta al perfil.

### Errores frecuentes y recomendaciones
- **Error:** “La RAM guarda mis archivos”. **Recomendación:** explicar que el almacenamiento persistente es disco/SSD.
- **Error:** borrar RAM físicamente o usar “limpiadores” milagrosos. **Recomendación:** usar herramientas del sistema y diagnosticar con evidencia.
- **Error:** comprar RAM sin verificar compatibilidad. **Recomendación:** revisar tipo, generación, velocidad soportada y placa base.

### Evaluación de comprensión
1. ¿Qué significa que la RAM sea volátil?
2. ¿Qué puede ocurrir cuando falta RAM?
3. ¿Por qué más RAM no siempre mejora el rendimiento?

### Referencias
- Crucial. *What is RAM?*. https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do. Consultado: 2026-11-24.
- Microsoft Learn. *Memory Performance*. https://learn.microsoft.com/en-us/windows/client-management/performance-tuning/subsystem/memory. Consultado: 2026-11-24.

---

## Lección 1.1.9 — ROM

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.9 — ROM.
- **Secuencia:** 9 de 16 en el módulo.

### Propósito de aprendizaje
Comprender el concepto de ROM y su relación con firmware en sistemas modernos.

### Conocimientos previos
- Lecciones 1.1.6 y 1.1.8.
- Noción de arranque del sistema.

### Resultados de aprendizaje
- Definir ROM en sentido histórico y funcional.
- Explicar la relación entre ROM, firmware y memoria flash.
- Diferenciar ROM de RAM y de almacenamiento masivo.
- Evitar la idea simplista de que ROM es siempre “totalmente inmutable”.

### Desarrollo conceptual
ROM (Read-Only Memory) se refiere históricamente a memoria diseñada para ser leída y no modificada durante la operación normal. Su uso clásico fue almacenar firmware: instrucciones esenciales para iniciar hardware o dispositivos.

En equipos modernos, el firmware suele almacenarse en memoria flash no volátil, que puede actualizarse bajo procedimientos controlados (por ejemplo, actualizaciones de UEFI/BIOS). Aunque técnicamente sea reprogramable, la función sigue siendo similar: conservar código crítico de arranque/configuración fuera de la RAM volátil.

La distinción importante para el estudiante es funcional: ROM/firmware no es el lugar donde el usuario guarda documentos, y no es memoria de trabajo volátil como la RAM.

### Ejemplo técnico desarrollado
**Escenario:** encender un computador.

1. Antes de que el sistema operativo cargue desde disco, el procesador necesita instrucciones iniciales.
2. El firmware almacenado en memoria no volátil realiza inicialización básica de hardware.
3. Luego entrega el control al cargador de arranque/sistema operativo.

**Interpretación:** sin ese código inicial persistente, el equipo no sabría cómo comenzar el proceso de arranque.

### Práctica guiada
- **Objetivo:** diferenciar memoria por función.
- **Procedimiento:** crea una tabla con RAM, ROM/firmware y SSD. Columnas: volatilidad, propósito, ejemplo de contenido, ¿el usuario la usa para guardar archivos?
- **Resultado esperado:** tabla correcta.
- **Verificación:** ROM/firmware marcado como no volátil y no destinado a archivos de usuario.

### Actividad independiente
Busca información del firmware/UEFI de tu equipo o de un equipo de ejemplo y registra versión y fabricante. No actualices firmware; solo documenta.

### Criterios de aceptación
- Define ROM con matiz histórico/moderno.
- Relaciona ROM con firmware.
- Distingue claramente de RAM y SSD.
- Actividad realizada con precaución.

### Errores frecuentes y recomendaciones
- **Error:** “ROM nunca se puede cambiar”. **Recomendación:** explicar que firmware moderno puede actualizarse, pero con riesgo y procedimiento controlado.
- **Error:** confundir ROM con disco duro. **Recomendación:** comparar propósito y capacidad.
- **Error:** actualizar firmware sin necesidad. **Recomendación:** solo con respaldo, fuente oficial e instrucciones del fabricante.

### Evaluación de comprensión
1. ¿Por qué el firmware necesita almacenamiento no volátil?
2. ¿Qué diferencia hay entre ROM histórica y flash de firmware moderna?
3. ¿Por qué una actualización de firmware debe hacerse con cautela?

### Referencias
- Dell. *What is BIOS and How to Update the BIOS on Your Dell System*. https://www.dell.com/support/kbdoc/en-us/000124211/dell-bios-updates. Consultado: 2026-11-24.
- UEFI Forum. *UEFI Specifications*. https://uefi.org/specifications. Consultado: 2026-11-24.

---

## Lección 1.1.10 — SSD

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.10 — SSD.
- **Secuencia:** 10 de 16 en el módulo.

### Propósito de aprendizaje
Comprender qué es un SSD, cómo se diferencia de un HDD y qué criterios usar para evaluarlo.

### Conocimientos previos
- Lecciones 1.1.8 y 1.1.9.
- Concepto de almacenamiento persistente.

### Resultados de aprendizaje
- Definir SSD y memoria flash a nivel básico.
- Identificar ventajas y limitaciones comunes de los SSD.
- Distinguir interfaz/protocolo (SATA, NVMe) de tipo de dispositivo.
- Evaluar un SSD según caso de uso.

### Desarrollo conceptual
Un SSD (Solid State Drive) es un dispositivo de almacenamiento persistente que usa memoria flash y controladores electrónicos, sin partes mecánicas móviles para leer/escribir datos como en un HDD. Esto suele ofrecer menor latencia, mayor resistencia a golpes y mejor rendimiento en acceso aleatorio.

Sin embargo, no todos los SSD son iguales. Existen diferencias por interfaz y protocolo: SATA, NVMe sobre PCIe, entre otros. También importan el tipo de memoria, caché, endurance (TBW/DWPD), rendimiento sostenido y controladora.

Un SSD mejora mucho los tiempos de arranque y carga en comparación con HDD en muchos escenarios, pero no sustituye una estrategia de respaldo. La persistencia no implica invulnerabilidad.

### Ejemplo técnico desarrollado
**Escenario:** un equipo tarda 2 minutos en iniciar con HDD y abre aplicaciones lentamente.

- Al migrar el sistema a un SSD, el tiempo de arranque y apertura de programas suele disminuir porque el acceso a archivos pequeños y aleatorios es más rápido.
- Si el equipo tiene poca RAM, puede seguir lento en multitarea.
- Si el SSD se llena casi por completo, el rendimiento puede degradarse según el modelo y condiciones.

**Interpretación:** el SSD ataca un cuello de botella común, pero no resuelve todos los problemas de rendimiento.

### Práctica guiada
- **Objetivo:** comparar dos SSD.
- **Procedimiento:**
  1. Elige dos modelos en sitios oficiales.
  2. Compara capacidad, interfaz, lectura/escritura declarada, garantía/endurance si está disponible.
  3. Indica cuál elegirías para un portátil de estudio y por qué.
- **Resultado esperado:** comparación con criterios explícitos.
- **Verificación:** se mencionan al menos tres criterios.

### Actividad independiente
Redacta una recomendación para migrar un equipo con HDD a SSD: qué datos respaldar, qué verificar antes y qué resultado esperas.

### Criterios de aceptación
- Define SSD correctamente.
- Distingue SSD de HDD y de RAM.
- Menciona ventajas y limitaciones.
- La recomendación incluye respaldo de datos.

### Errores frecuentes y recomendaciones
- **Error:** “SSD nunca falla”. **Recomendación:** mantener backups.
- **Error:** confundir SATA/NVMe como sinónimos de SSD. **Recomendación:** separar forma/interfaz/protocolo.
- **Error:** mirar solo velocidad máxima secuencial. **Recomendación:** considerar uso real y endurance.

### Evaluación de comprensión
1. ¿Qué ventaja principal tiene un SSD frente a un HDD?
2. ¿Por qué un SSD no elimina la necesidad de copias de seguridad?
3. ¿Qué diferencia hay entre interfaz y tipo de dispositivo?

### Referencias
- Kingston. *SSD vs HDD*. https://www.kingston.com/en/blog/pc-performance/ssd-vs-hdd. Consultado: 2026-11-24.
- Samsung Semiconductor. *SSD Basics*. https://semiconductor.samsung.com/consumer-storage/support/faqs/internalssd-product/. Consultado: 2026-11-24.

---

## Lección 1.1.11 — HDD

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.11 — HDD.
- **Secuencia:** 11 de 16 en el módulo.

### Propósito de aprendizaje
Comprender el funcionamiento básico, usos y limitaciones de los discos duros mecánicos.

### Conocimientos previos
- Lección 1.1.10.

### Resultados de aprendizaje
- Definir HDD y sus componentes básicos.
- Explicar por qué la latencia mecánica afecta el rendimiento.
- Comparar HDD y SSD con criterios adecuados.
- Identificar casos donde un HDD aún puede ser útil.

### Desarrollo conceptual
Un HDD (Hard Disk Drive) es un dispositivo de almacenamiento persistente que guarda datos en platos magnéticos giratorios. Cabezales de lectura/escritura se mueven sobre los platos para acceder a la información. Como depende de movimiento mecánico, suele tener mayor latencia y menor rendimiento en acceso aleatorio que un SSD.

Los HDD siguen siendo útiles cuando se prioriza costo por capacidad, almacenamiento masivo o respaldos donde la velocidad máxima no es el criterio principal. Sin embargo, son más sensibles a golpes durante operación y pueden ser más lentos para cargar sistemas operativos y aplicaciones.

Características comunes a evaluar: capacidad, RPM, caché interna, interfaz, factor de forma, fiabilidad y uso previsto.

### Ejemplo técnico desarrollado
**Escenario:** un laboratorio necesita almacenar 20 TB de respaldos locales de bajo acceso.

- **Opción A:** SSD de gran capacidad. Ventaja: rapidez. Limitación: costo mayor.
- **Opción B:** HDD de gran capacidad. Ventaja: mejor costo por TB. Limitación: menor velocidad y partes mecánicas.

**Interpretación:** para respaldos fríos o archivos masivos, un HDD puede ser razonable; para sistema operativo, un SSD suele ser preferible.

### Práctica guiada
- **Objetivo:** decidir almacenamiento según caso.
- **Procedimiento:** dado tres casos (SO, biblioteca multimedia, backup), elige SSD/HDD/mixto y justifica.
- **Resultado esperado:** matriz de decisión.
- **Verificación:** cada decisión tiene al menos una ventaja y una limitación.

### Actividad independiente
Investiga qué significa RPM en un HDD y por qué no es el único factor de rendimiento.

### Criterios de aceptación
- Define HDD correctamente.
- Explica impacto de la mecánica.
- Compara HDD/SSD sin dogmatismo.
- Justifica casos de uso.

### Errores frecuentes y recomendaciones
- **Error:** declarar HDD “obsoleto” en todo contexto. **Recomendación:** evaluar costo, capacidad y uso.
- **Error:** mover un HDD encendido bruscamente. **Recomendación:** manipular con cuidado.
- **Error:** usar HDD sin respaldo. **Recomendación:** toda persistencia requiere estrategia de backup.

### Evaluación de comprensión
1. ¿Qué componente mecánico influye en la latencia del HDD?
2. ¿Cuándo puede ser razonable usar HDD?
3. ¿Qué criterio usarías para un disco de sistema operativo?

### Referencias
- Seagate. *What Is a Hard Disk Drive?*. https://www.seagate.com/tech-insights/what-is-a-hard-disk-drive-master-ti/. Consultado: 2026-11-24.
- Western Digital. *HDD vs SSD*. https://www.westerndigital.com/solutions/hdd-vs-ssd. Consultado: 2026-11-24.

---

## Lección 1.1.12 — GPU

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.12 — GPU.
- **Secuencia:** 12 de 16 en el módulo.

### Propósito de aprendizaje
Comprender el papel de la GPU y diferenciarla de la CPU.

### Conocimientos previos
- Lecciones 1.1.1, 1.1.4 y 1.1.5.

### Resultados de aprendizaje
- Definir GPU y procesamiento paralelo a alto nivel.
- Distinguir GPU integrada y dedicada.
- Identificar casos de uso: gráficos, video, IA, cómputo paralelo.
- Evitar la idea de que GPU sustituye completamente a CPU.

### Desarrollo conceptual
La GPU (Graphics Processing Unit) es un procesador especializado en manejar grandes cantidades de operaciones en paralelo. Fue diseñada originalmente para gráficos, pero hoy también se usa en aceleración de video, cálculo científico, aprendizaje automático y otras cargas paralelizables.

Una **GPU integrada** comparte recursos con la CPU o el paquete del procesador y suele usar memoria del sistema. Una **GPU dedicada** tiene su propia placa o módulo, memoria dedicada (VRAM) y mayor capacidad para cargas gráficas o de cómputo intensivo.

La GPU no reemplaza a la CPU. La CPU gestiona control, lógica general y coordinación; la GPU acelera tareas que se benefician de paralelismo masivo.

### Ejemplo técnico desarrollado
**Escenario:** renderizar un video 3D.

- La CPU prepara escena, lógica, assets, física y coordinación.
- La GPU procesa muchos píxeles/vértices/shaders en paralelo.
- Si la GPU es débil, baja FPS; si la CPU es débil, puede haber cuello de botella aunque la GPU sea potente.

**Interpretación:** el rendimiento gráfico es resultado del equilibrio del sistema.

### Práctica guiada
- **Objetivo:** identificar la GPU del sistema.
- **Procedimiento:**
  1. En Windows: Administrador de tareas > Rendimiento > GPU.
  2. En Linux: `lspci | grep -i vga` o herramientas del sistema.
  3. Registra si es integrada o dedicada.
  4. Anota para qué tipo de tareas sería adecuada.
- **Resultado esperado:** ficha básica de GPU.
- **Verificación:** el estudiante distingue integrada/dedicada.

### Actividad independiente
Compara dos equipos: uno con GPU integrada y otro con dedicada. Indica qué perfil de usuario se beneficia de cada uno.

### Criterios de aceptación
- Define GPU correctamente.
- Distingue integrada y dedicada.
- Relaciona GPU con cargas paralelas.
- No presenta GPU como reemplazo total de CPU.

### Errores frecuentes y recomendaciones
- **Error:** comprar GPU potente para tareas que no la usan. **Recomendación:** evaluar carga real.
- **Error:** ignorar VRAM y consumo. **Recomendación:** revisar requisitos de software.
- **Error:** confundir salida de video con potencia gráfica. **Recomendación:** una GPU integrada también puede dar imagen.

### Evaluación de comprensión
1. ¿Qué tipo de tareas aprovechan bien una GPU?
2. ¿Qué diferencia hay entre GPU integrada y dedicada?
3. ¿Por qué puede existir cuello de botella si solo se mejora la GPU?

### Referencias
- NVIDIA. *What Is a GPU?*. https://www.nvidia.com/en-us/geforce/graphics-cards/what-is-a-gpu/. Consultado: 2026-11-24.
- Intel. *What Is Integrated Graphics?*. https://www.intel.com/content/www/us/en/support/articles/000057824/graphics.html. Consultado: 2026-11-24.

---

## Lección 1.1.13 — Motherboard

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.13 — Motherboard.
- **Secuencia:** 13 de 16 en el módulo.

### Propósito de aprendizaje
Comprender la motherboard como plataforma de interconexión y compatibilidad del sistema.

### Conocimientos previos
- Lecciones 1.1.1 a 1.1.12.

### Resultados de aprendizaje
- Definir motherboard y sus funciones.
- Identificar componentes/conectores principales.
- Explicar por qué la compatibilidad depende de la placa base.
- Leer criterios básicos de compatibilidad.

### Desarrollo conceptual
La motherboard (placa base) es la placa principal que conecta y permite la comunicación entre CPU, RAM, almacenamiento, GPU, fuente de alimentación, periféricos y otros componentes. Incluye socket de CPU, ranuras de memoria, ranuras de expansión, conectores de almacenamiento, chipset, puertos y firmware.

El chipset y el diseño de la placa determinan capacidades como tipos de memoria soportados, número de puertos, líneas PCIe, opciones de expansión y compatibilidad. Por eso, la motherboard no es un simple “soporte físico”: es una plataforma que condiciona la evolución del equipo.

### Ejemplo técnico desarrollado
**Escenario:** actualizar CPU.

1. Verificar socket de la motherboard.
2. Verificar chipset y compatibilidad de CPU según fabricante.
3. Verificar versión de firmware/BIOS si aplica.
4. Verificar soporte de RAM y consumo térmico.

**Interpretación:** una CPU puede ser excelente, pero incompatible con la placa base.

### Práctica guiada
- **Objetivo:** identificar elementos en un diagrama de motherboard.
- **Procedimiento:** usa una imagen oficial o diagrama de fabricante y localiza: socket CPU, ranuras RAM, PCIe, SATA/M.2, conector de energía, puertos USB.
- **Resultado esperado:** lista de componentes ubicados.
- **Verificación:** cada elemento tiene función descrita en una frase.

### Actividad independiente
Crea una checklist de compatibilidad para armar un PC básico. Incluye CPU, RAM, almacenamiento, GPU y fuente.

### Criterios de aceptación
- Define motherboard correctamente.
- Identifica al menos 5 componentes/conectores.
- Explica compatibilidad con un ejemplo.
- Checklist usable y coherente.

### Errores frecuentes y recomendaciones
- **Error:** elegir placa solo por precio o estética. **Recomendación:** priorizar compatibilidad y necesidades.
- **Error:** ignorar firmware. **Recomendación:** revisar soporte oficial.
- **Error:** confundir chipset con CPU. **Recomendación:** distinguir funciones.

### Evaluación de comprensión
1. ¿Por qué la motherboard influye en la compatibilidad?
2. ¿Qué es el socket?
3. ¿Qué información revisarías antes de ampliar RAM?

### Referencias
- ASUS. *Motherboard basics / support documentation*. https://www.asus.com/support/. Consultado: 2026-11-24.
- Intel. *Desktop Chipsets*. https://www.intel.com/content/www/us/en/products/details/chipsets/desktop-chipsets.html. Consultado: 2026-11-24.

---

## Lección 1.1.14 — Buses

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.14 — Buses.
- **Secuencia:** 14 de 16 en el módulo.

### Propósito de aprendizaje
Comprender cómo los buses/interconexiones transportan datos, direcciones y señales de control.

### Conocimientos previos
- Lecciones 1.1.1, 1.1.3, 1.1.13.

### Resultados de aprendizaje
- Definir bus de datos, direcciones y control.
- Explicar por qué la comunicación interna depende de interconexiones.
- Relacionar buses con ancho de banda y latencia a nivel básico.
- Distinguir bus físico/logical conceptualmente.

### Desarrollo conceptual
Un bus es un sistema de comunicación que transfiere información entre componentes. Tradicionalmente se describen tres tipos funcionales:
- **Bus de datos:** transporta los datos.
- **Bus de direcciones:** indica dónde leer o escribir.
- **Bus de control:** transporta señales que coordinan operaciones (lectura, escritura, interrupciones, sincronización).

En sistemas modernos, muchas interconexiones son punto a punto y más complejas que el bus compartido clásico, pero el modelo conceptual sigue siendo útil para entender la comunicación.

El rendimiento de una interconexión depende de ancho, frecuencia, protocolo, latencia y contención. Más ancho de banda teórico no siempre se traduce en el mismo rendimiento percibido.

### Ejemplo técnico desarrollado
**Escenario:** CPU lee un dato de RAM.

1. La CPU coloca la dirección en el bus/línea de direcciones.
2. Envía una señal de lectura por el canal de control.
3. La memoria responde colocando el dato en el canal de datos.
4. La CPU recibe el dato y lo almacena en un registro.

**Interpretación:** leer memoria no es un acto instantáneo; requiere coordinación de señales.

### Práctica guiada
- **Objetivo:** representar una transferencia simple.
- **Procedimiento:** dibuja CPU, RAM y tres flechas etiquetadas: dirección, control, datos. Describe qué ocurre en cada una.
- **Resultado esperado:** diagrama conceptual.
- **Verificación:** las tres funciones están diferenciadas.

### Actividad independiente
Explica con un ejemplo cotidiano la diferencia entre dato, dirección y control (por ejemplo, sistema postal o biblioteca), indicando el límite de la analogía.

### Criterios de aceptación
- Define los tres tipos de bus.
- Describe un ciclo de lectura simplificado.
- Usa la analogía con precaución.
- No presenta el modelo como implementación exacta de todo hardware moderno.

### Errores frecuentes y recomendaciones
- **Error:** creer que solo existe “un bus”. **Recomendación:** distinguir tipos y tecnologías.
- **Error:** confundir bus con puerto externo únicamente. **Recomendación:** incluir interconexiones internas.
- **Error:** reducir rendimiento a “más bits = mejor siempre”. **Recomendación:** considerar latencia y protocolo.

### Evaluación de comprensión
1. ¿Qué transporta el bus de direcciones?
2. ¿Qué papel tiene el bus de control?
3. ¿Por qué el modelo clásico sigue siendo útil?

### Referencias
- Null, L., & Lobur, J. *The Essentials of Computer Organization and Architecture*. Jones & Bartlett Learning.
- Intel. *Intel® 64 and IA-32 Architectures Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.

---

## Lección 1.1.15 — Fuente de alimentación

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.15 — Fuente de alimentación.
- **Secuencia:** 15 de 16 en el módulo.

### Propósito de aprendizaje
Comprender la función de la fuente de alimentación y los criterios básicos de seguridad y selección.

### Conocimientos previos
- Lecciones 1.1.12 y 1.1.13.

### Resultados de aprendizaje
- Definir PSU/fuente de alimentación.
- Explicar conversión de energía y distribución a componentes.
- Identificar criterios básicos: potencia, eficiencia, conectores, protecciones.
- Reconocer riesgos de manipulación inadecuada.

### Desarrollo conceptual
La fuente de alimentación (PSU) convierte corriente alterna de la red eléctrica en corriente continua con voltajes adecuados para los componentes del computador. También distribuye energía mediante conectores específicos y debe proporcionar estabilidad eléctrica.

Una fuente adecuada no solo “enciende” el equipo: protege ante condiciones anómalas según sus protecciones (sobretensión, sobrecorriente, cortocircuito, etc., dependiendo del modelo). Elegir una fuente insuficiente o de baja calidad puede causar inestabilidad, apagados o daños.

La potencia (W) debe dimensionarse según el consumo del sistema y margen razonable. La eficiencia (por ejemplo, certificaciones 80 PLUS) indica cómo convierte energía, no la calidad total por sí sola.

### Ejemplo técnico desarrollado
**Escenario:** PC con CPU de alto consumo y GPU dedicada.

1. Se estima consumo total de componentes.
2. Se añade margen de seguridad razonable.
3. Se verifican conectores necesarios para GPU y placa.
4. Se elige una fuente confiable con protecciones y eficiencia adecuada.

**Interpretación:** una fuente barata con potencia nominal inflada puede ser un riesgo, aunque “diga 750W”.

### Práctica guiada
- **Objetivo:** leer etiqueta de PSU.
- **Procedimiento:** observa una etiqueta de fuente (foto de fabricante o equipo de laboratorio) e identifica: potencia, voltajes, marca/modelo, certificación.
- **Resultado esperado:** ficha de lectura.
- **Verificación:** no se abre la fuente.

### Actividad independiente
Elabora una lista de verificación de seguridad antes de intervenir dentro de un PC (desconectar, descargar estática, no abrir PSU, etc.).

### Criterios de aceptación
- Define PSU correctamente.
- Identifica al menos 4 criterios de selección.
- Incluye advertencias de seguridad.
- No propone abrir la fuente.

### Errores frecuentes y recomendaciones
- **Error:** abrir la PSU para “limpiar” o reparar. **Recomendación:** no abrir; puede retener carga peligrosa.
- **Error:** elegir solo por vatios. **Recomendación:** considerar calidad, protecciones, conectores y eficiencia.
- **Error:** usar adaptadores improvisados. **Recomendación:** usar conectores adecuados y componentes certificados.

### Evaluación de comprensión
1. ¿Qué función cumple la PSU?
2. ¿Por qué la potencia nominal no es el único criterio?
3. ¿Qué riesgo implica manipular una fuente internamente?

### Referencias
- Corsair. *Power Supply Basics*. https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/power-supply-basics/. Consultado: 2026-11-24.
- Seasonic. *PSU Protection Features*. https://seasonic.com/psu-protection-features. Consultado: 2026-11-24.

---

## Lección 1.1.16 — Periféricos

### Identificación
- **Etapa:** 1 · Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.1 · Hardware.
- **Lección oficial:** 1.1.16 — Periféricos.
- **Secuencia:** 16 de 16 en el módulo.

### Propósito de aprendizaje
Clasificar periféricos según su función y comprender su relación con el sistema.

### Conocimientos previos
- Lecciones 1.1.1 a 1.1.15.

### Resultados de aprendizaje
- Definir periférico.
- Clasificar periféricos en entrada, salida, entrada/salida y almacenamiento/comunicación según contexto.
- Explicar cómo un periférico se integra al flujo de procesamiento.
- Identificar consideraciones básicas de compatibilidad y seguridad.

### Desarrollo conceptual
Los periféricos son dispositivos externos o conectados al sistema que permiten la interacción con el usuario u otros sistemas. Se clasifican comúnmente en:
- **Entrada:** teclado, mouse, micrófono, escáner.
- **Salida:** monitor, impresora, altavoces.
- **Entrada/salida:** pantalla táctil, impresora multifunción, adaptadores de red, unidades externas.
- **Almacenamiento externo:** USB, discos externos (también pueden verse como E/S).

La clasificación puede depender de la función. Por ejemplo, una pantalla táctil recibe entrada y produce salida. Un disco externo almacena datos y también participa en operaciones de entrada/salida.

La conexión puede ser USB, Bluetooth, HDMI, DisplayPort, audio jack, red, etc. La compatibilidad incluye puerto físico, protocolo, drivers y soporte del sistema operativo.

### Ejemplo técnico desarrollado
**Escenario:** escanear un documento y enviarlo por correo.

1. El escáner (entrada) digitaliza la imagen.
2. La CPU/RAM procesan el archivo.
3. El sistema lo almacena temporalmente en SSD/RAM.
4. El adaptador de red (E/S) envía el correo.
5. El monitor (salida) muestra la confirmación.

**Interpretación:** una tarea cotidiana usa varios periféricos y componentes internos coordinados.

### Práctica guiada
- **Objetivo:** clasificar periféricos reales.
- **Procedimiento:** haz una lista de 10 dispositivos en tu entorno y clasifícalos. Justifica los casos ambiguos.
- **Resultado esperado:** tabla con clasificación y justificación.
- **Verificación:** al menos un dispositivo mixto bien justificado.

### Actividad independiente
Diseña la configuración de periféricos para un puesto de estudio de ciberseguridad (monitor, teclado, red, backup, etc.) con justificación.

### Criterios de aceptación
- Define periférico correctamente.
- Clasifica con justificación.
- Reconoce dispositivos mixtos.
- Considera compatibilidad o seguridad básica.

### Errores frecuentes y recomendaciones
- **Error:** clasificar por forma y no por función. **Recomendación:** preguntar “¿envía, recibe o ambos?”.
- **Error:** conectar dispositivos desconocidos sin precaución. **Recomendación:** aplicar higiene de seguridad (USB desconocidos).
- **Error:** ignorar drivers/compatibilidad. **Recomendación:** verificar soporte del sistema.

### Evaluación de comprensión
1. ¿Por qué una pantalla táctil es E/S?
2. ¿Qué diferencia hay entre periférico y componente interno?
3. ¿Qué riesgo de seguridad puede tener un periférico USB desconocido?

### Referencias
- HP. *Computer Ports and Connections*. https://support.hp.com/us-en/document/ish_2851059-2411433-16. Consultado: 2026-11-24.
- NIST. *Guidelines for Media Sanitization (SP 800-88 Rev. 1)* — referencia de apoyo para manejo seguro de medios/dispositivos de almacenamiento. https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final. Consultado: 2026-11-24.

---

## Recursos transversales del módulo

### Práctica integradora del módulo
**Laboratorio:** Inventario técnico de un equipo real o virtual.

- Entregar una tabla con CPU, núcleos/hilos, frecuencia, RAM, almacenamiento, GPU, motherboard/fabricante si disponible, fuente (si visible en etiqueta) y periféricos.
- Indicar herramienta usada y fecha.
- Clasificar cada componente por función.
- Redactar 5 conclusiones: capacidad, limitaciones, compatibilidad, riesgos y mejora posible.

### Evaluación del módulo
- **Conceptual (40%):** definiciones precisas y distinción de componentes.
- **Aplicada (40%):** interpretación de especificaciones y clasificación correcta.
- **Criterio técnico (20%):** recomendaciones justificadas y prudentes.

### Checklist de calidad
- [ ] Todas las lecciones oficiales 1.1.1–1.1.16 desarrolladas.
- [ ] Cada lección incluye objetivo, práctica y evaluación.
- [ ] No se presentan métricas únicas como verdad absoluta.
- [ ] Se incluyen advertencias de seguridad básicas.
- [ ] Referencias citadas con fecha de consulta.

## Fuentes del módulo
- Intel. *Developer Manuals and Product Documentation*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- AMD. *Processor and Product Documentation*. https://www.amd.com/en/products/specifications/processors.html. Consultado: 2026-11-24.
- Arm. *Documentation*. https://developer.arm.com/documentation/. Consultado: 2026-11-24.
- UEFI Forum. *Specifications*. https://uefi.org/specifications. Consultado: 2026-11-24.
- NIST. *SP 800-88 Rev. 1*. https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final. Consultado: 2026-11-24.