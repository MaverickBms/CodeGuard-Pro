# Etapa 1 · Módulo 1.3 — Arquitectura de computadores

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 1, apartado 1.3.  
**Temas oficiales:** arquitectura Von Neumann, arquitectura Harvard, ciclo Fetch-Decode-Execute, conjunto de instrucciones, registros del procesador, memoria, entrada y salida e interrupciones.

## Objetivo

Explicar cómo se organiza un computador a nivel lógico para ejecutar instrucciones, almacenar datos y comunicarse con dispositivos.

## Resultados de aprendizaje

Podrás describir las ideas centrales de Von Neumann y Harvard; recorrer conceptualmente el ciclo de instrucción; distinguir ISA de microarquitectura; identificar la función de registros, memoria y entrada/salida; y explicar qué es una interrupción y por qué existe.

## 1.3.1 — Arquitectura Von Neumann

La arquitectura Von Neumann describe un modelo de programa almacenado en el que instrucciones y datos comparten un espacio de memoria y, en el modelo clásico, caminos de comunicación. La CPU obtiene instrucciones de memoria, las interpreta y opera sobre datos.

Bloques conceptuales:
- CPU: control y procesamiento;
- memoria: instrucciones y datos;
- entrada/salida: comunicación con el exterior;
- interconexiones: transporte de direcciones, datos y señales de control.

El llamado cuello de botella de Von Neumann describe una limitación potencial: instrucciones y datos compiten por transferencias a través de recursos compartidos. Los sistemas modernos incorporan cachés, buses separados, ejecución especulativa y otras optimizaciones; no son una implementación literal y simple del diagrama clásico.

## 1.3.2 — Arquitectura Harvard

La arquitectura Harvard separa memorias o caminos de acceso para instrucciones y datos. Esto puede permitir transferencias simultáneas y características distintas para cada espacio.

En sistemas reales hay variantes, incluida la arquitectura Harvard modificada: por ejemplo, memorias caché separadas para instrucciones y datos con una memoria principal unificada. No clasifiques todo procesador moderno como «Harvard puro» o «Von Neumann puro» sin precisar el nivel de abstracción.

**Comparación:** Von Neumann facilita un espacio unificado; Harvard puede separar accesos y formatos. La elección depende del diseño, coste, rendimiento y requisitos.

## 1.3.3 — Ciclo Fetch-Decode-Execute

El ciclo describe, de forma simplificada, la ejecución de una instrucción:

1. **Fetch (búsqueda):** obtener la instrucción indicada por el contador de programa.
2. **Decode (decodificación):** interpretar la operación y sus operandos.
3. **Execute (ejecución):** realizar la operación, acceder a memoria o iniciar una transferencia.
4. **Write-back (escritura del resultado):** cuando corresponde, guardar el resultado en un registro o destino.

El ciclo real de una CPU moderna puede solaparse y dividirse en etapas (pipeline), ejecutar instrucciones fuera de orden, predecir saltos y retirar resultados en orden arquitectónico. El modelo de tres pasos sirve para comprender la idea, no para describir todos los circuitos de una CPU actual.

**Ejemplo conceptual:** una instrucción suma dos registros y guarda el resultado en otro. La CPU obtiene la instrucción, identifica registros fuente/destino y activa las unidades que realizan la operación.

## 1.3.4 — Conjunto de instrucciones (ISA)

La ISA define el contrato visible entre software de bajo nivel y procesador: instrucciones, registros arquitectónicos, modos de direccionamiento, tipos de datos, excepciones y reglas de ejecución.

Ejemplos de familias ISA son x86-64 y AArch64. Un mismo ISA puede tener múltiples microarquitecturas distintas: implementaciones diferentes que ejecutan el mismo contrato, con distintos diseños internos y rendimiento.

No confundas:
- **ISA:** qué instrucciones y comportamiento debe ofrecer el procesador.
- **Microarquitectura:** cómo está construido internamente para implementar la ISA.
- **Lenguaje de alto nivel:** abstracción que un compilador traduce, directa o indirectamente, a instrucciones de máquina.

## 1.3.5 — Registros del procesador

Los registros visibles por la ISA pueden incluir:
- registros de propósito general;
- contador de programa o equivalente;
- registro de estado/flags;
- registros de control;
- registros vectoriales o de punto flotante.

Los nombres, cantidades y funciones dependen de la ISA. En una explicación introductoria, el contador de programa permite entender qué instrucción se buscará a continuación y los registros generales mantienen operandos/resultados. No todos los procesadores exponen un registro llamado literalmente «contador de programa» al software.

## 1.3.6 — Memoria

El procesador necesita memoria para obtener instrucciones y datos. La jerarquía típica incluye registros, cachés, RAM y almacenamiento persistente. Cada nivel ofrece compromisos distintos de latencia, capacidad, coste y persistencia.

La memoria direccionable se organiza en posiciones identificadas por direcciones. El tamaño de una dirección y el modelo de memoria dependen de la arquitectura y del sistema. Una dirección virtual usada por un proceso no debe confundirse con una dirección física de RAM.

## 1.3.7 — Entrada y salida

Los mecanismos de entrada/salida conectan CPU y memoria con dispositivos externos o internos. Algunos dispositivos se comunican mediante registros mapeados en memoria; otros usan mecanismos específicos de instrucciones o controladores.

**Ejemplo:** al pulsar una tecla, el controlador del dispositivo detecta el evento y el sistema operativo recibe información para entregarla a la aplicación correspondiente. El teclado no escribe directamente caracteres en el código fuente: hay varias capas de hardware y software.

## 1.3.8 — Interrupciones

Una interrupción es una señal o evento que hace que el procesador atienda una condición que requiere servicio. Puede provenir de hardware (por ejemplo, un dispositivo) o de mecanismos internos/arquitectónicos.

Flujo conceptual:
1. ocurre el evento;
2. el procesador reconoce la interrupción según reglas de prioridad y habilitación;
3. conserva el estado necesario;
4. transfiere el control a una rutina de atención;
5. se atiende el evento;
6. se restaura el contexto y continúa la ejecución cuando corresponde.

Una excepción suele ser un evento síncrono asociado a la instrucción que se está ejecutando; una interrupción externa suele ser asíncrona respecto al flujo de instrucciones. La terminología exacta depende de la arquitectura.

No todas las interrupciones implican que la CPU detenga todo el sistema por un tiempo largo. Los manejadores deben ser breves y delegar trabajo cuando el sistema operativo lo requiere.

## Laboratorio conceptual — Simulador de ciclo de instrucción

Construye una simulación en papel, hoja de cálculo o programa sencillo con:
- cuatro registros generales;
- un contador de programa;
- memoria con instrucciones y datos;
- instrucciones abstractas `LOAD`, `ADD`, `STORE`, `JUMP`;
- una secuencia paso a paso de Fetch, Decode, Execute y Write-back.

Programa de ejemplo abstracto:
1. cargar 7 en R1;
2. cargar 5 en R2;
3. sumar R1 y R2 y guardar en R3;
4. almacenar R3 en una posición de memoria.

La simulación debe mostrar el estado de registros, contador de programa y memoria después de cada instrucción. No pretende emular una ISA real; es un modelo didáctico.

### Extensión de interrupción

Añade un evento externo que se produce después de la segunda instrucción. Registra qué estado debe conservarse, qué rutina atiende el evento y cómo se reanuda el programa.

### Entregables y evaluación (100 puntos)

| Criterio | Puntos |
|---|---:|
| Diferencia Von Neumann/Harvard | 15 |
| Explicación correcta del ciclo | 20 |
| Diferencia ISA/microarquitectura | 15 |
| Modelo de registros y memoria | 20 |
| Simulación de E/S e interrupción | 20 |
| Claridad y límites del modelo | 10 |

## Ejercicios

1. ¿Qué característica central distingue el modelo clásico Von Neumann?
2. ¿Qué ventaja potencial ofrece Harvard?
3. ¿Por qué Fetch-Decode-Execute es un modelo simplificado?
4. ¿Qué diferencia hay entre ISA y microarquitectura?
5. ¿Qué representa conceptualmente el contador de programa?
6. ¿Qué evento podría generar una interrupción?
7. ¿Por qué una dirección virtual no es necesariamente una dirección física?

**Respuestas orientativas:** Von Neumann usa un espacio compartido para instrucciones y datos; Harvard separa caminos/memorias; CPUs modernas solapan etapas y usan optimizaciones; ISA es el contrato y microarquitectura la implementación; el contador identifica la siguiente instrucción; un controlador de dispositivo puede generar un evento; la traducción de memoria virtual permite aislar procesos y mapear páginas a marcos físicos.

## Autoevaluación aplicada

Explica el recorrido de una instrucción de suma desde la memoria hasta que el resultado queda disponible. Después describe qué cambia si llega un evento de entrada/salida durante la ejecución. Identifica qué partes de tu explicación son modelo conceptual y cuáles dependen de una ISA concreta.

## Recursos audiovisuales

No se incluye video en esta versión: no se ha comprobado un recurso con audio hablado en español que explique directamente Von Neumann, Harvard, el ciclo de instrucción, ISA e interrupciones con precisión suficiente. No se recomienda una animación genérica sin validar idioma y correspondencia temática.

## Referencias

- Intel, **Intel® 64 and IA-32 Architectures Software Developer’s Manuals**: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- Arm, **Arm Architecture Reference Manuals**: https://developer.arm.com/documentation
- Nand2Tetris, **The Elements of Computing Systems** (material académico del proyecto; útil como ruta de construcción conceptual): https://www.nand2tetris.org/
- IES Antonio González González, **Arquitectura y funcionamiento del ordenador**, material educativo institucional: https://centros.edu.xunta.gal/iesblancoamorculleredo/aulavirtual/mod/book/view.php?chapterid=4332&id=19998

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** simulador propuesto; no ejecutado.  
**Estado editorial:** en desarrollo; no aprobado ni publicado.
