# Etapa 1 · Módulo 1.1 — Hardware

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 1, apartado 1.1.  
**Prioridad de etapa:** P1 · Obligatoria.  
**Temas oficiales:** CPU (Unidad Central de Procesamiento), ALU (Unidad Aritmético-Lógica), registros, núcleos, hilos de ejecución, frecuencia, caché L1/L2/L3, RAM, ROM, SSD, HDD, GPU, motherboard, buses, fuente de alimentación y periféricos.

## Objetivo curricular

Comprender los componentes físicos principales de un computador y explicar cómo colaboran para recibir, procesar, almacenar y comunicar información.

## Resultados de aprendizaje

Al finalizar podrás:
- identificar CPU, ALU, registros, núcleos e hilos y describir sus responsabilidades;
- distinguir frecuencia, núcleos, hilos y caché sin reducir el rendimiento a una sola cifra;
- comparar RAM, ROM, SSD y HDD según volatilidad, función y persistencia;
- explicar el papel de GPU, motherboard, buses y fuente de alimentación;
- clasificar periféricos por la función que cumplen;
- interpretar una ficha técnica básica sin confundir capacidad, velocidad y compatibilidad.

## Prerrequisitos

Uso básico de un computador y distinción elemental entre hardware y software. No se requiere abrir físicamente el equipo.

## 1.1.1 — CPU

La CPU ejecuta instrucciones de programas y coordina operaciones del sistema. No es una pieza que «piensa» ni realiza por sí sola todas las tareas: trabaja con memoria, dispositivos de entrada/salida y otros procesadores.

## 1.1.2 — ALU

La ALU es una unidad funcional que realiza operaciones aritméticas (por ejemplo, suma y resta) y lógicas (AND, OR, NOT y comparaciones). La CPU también contiene lógica de control y otros bloques; por tanto, ALU y CPU no son sinónimos.

**Ejemplo guiado:** para evaluar `(8 + 4) > 10`, el sistema debe obtener el resultado aritmético y después evaluar una comparación. La ALU puede ejecutar esas operaciones como parte del procesamiento de instrucciones.

**Comprueba tu comprensión:** explica por qué afirmar «la ALU es todo el procesador» es incorrecto.

## 1.1.3 — Registros

Los registros son pequeñas ubicaciones de almacenamiento de muy alta velocidad integradas en el procesador. Mantienen valores que la CPU necesita de inmediato: operandos, direcciones, resultados intermedios o información de control.

Su función se entiende mejor comparándolos con la RAM: los registros son mucho más limitados en cantidad y están estrechamente ligados a la ejecución de instrucciones; la RAM ofrece mucha más capacidad para programas y datos en uso.

No todos los procesadores exponen el mismo conjunto de registros ni usan los mismos nombres. La arquitectura de conjunto de instrucciones (ISA) define aspectos visibles para el software.

**Ejercicio:** describe qué tipo de dato podría mantener un registro durante la suma de dos enteros y qué papel podría tener otro registro al indicar la siguiente instrucción.

## 1.1.4 — Núcleos

Un núcleo es una unidad de procesamiento capaz de ejecutar flujos de instrucciones. Un procesador puede integrar varios núcleos.

## 1.1.5 — Hilos de ejecución

Los hilos de ejecución son secuencias de trabajo planificadas por el sistema operativo; algunas CPU permiten que un núcleo mantenga el estado de más de un hilo de hardware mediante técnicas de multithreading simultáneo.

No confundas:
- **Proceso:** programa en ejecución con recursos y espacio de memoria propios.
- **Hilo de software:** flujo de ejecución dentro de un proceso.
- **Hilo de hardware:** contexto de ejecución que la CPU puede gestionar según su diseño.
- **Núcleo:** recurso físico de procesamiento.

Tener más núcleos o hilos no garantiza que cualquier aplicación sea más rápida. La mejora depende de si el trabajo puede dividirse, de la memoria, de la arquitectura, de la frecuencia sostenida y de otros límites del sistema.

**Caso:** una tarea estrictamente secuencial puede no aprovechar ocho núcleos. Una tarea paralelizable puede distribuir trabajo, aunque debe coordinar resultados y evitar condiciones de carrera.

## 1.1.6 — Frecuencia

La frecuencia del reloj se expresa en hercios (Hz), habitualmente GHz para CPU modernas. Indica ciclos por segundo, no instrucciones completadas por segundo. Una instrucción puede requerir varios ciclos y distintas microarquitecturas pueden completar cantidades diferentes de trabajo por ciclo.

El rendimiento depende, entre otros factores, de:
- arquitectura y trabajo por ciclo;
- frecuencia efectiva y límites térmicos/energéticos;
- número de núcleos y paralelismo disponible;
- cachés y latencias de memoria;
- instrucciones utilizadas y comportamiento del software.

**Error frecuente:** comparar dos CPU únicamente por GHz. Es una comparación insuficiente si difieren en arquitectura, generación, límites de potencia o carga.

## 1.1.7 — Caché L1, L2 y L3

La caché conserva copias de datos e instrucciones que podrían volver a necesitarse. Aprovecha la localidad temporal (reutilizar pronto un dato) y espacial (acceder a direcciones cercanas).

En términos generales:
- **L1:** muy pequeña y de acceso muy rápido; suele estar asociada a cada núcleo y puede dividirse en caché de instrucciones y datos.
- **L2:** mayor que L1 y normalmente algo más lenta; su organización depende del procesador.
- **L3:** suele ser mayor y puede compartirse entre varios núcleos, aunque la implementación varía.

No asumas que todos los fabricantes organizan las cachés de la misma manera. La jerarquía busca equilibrar capacidad, latencia, coste y consumo.

**Analogía y límite:** una mesa de trabajo representa la caché y un almacén distante representa la RAM. La analogía ayuda a entender proximidad, pero no describe políticas de reemplazo, coherencia ni circuitos reales.

## 1.1.8 — RAM

La RAM principal almacena temporalmente programas y datos que el sistema está utilizando. Es volátil en los sistemas habituales: al perder alimentación, su contenido no se conserva.

## 1.1.9 — ROM

ROM significa memoria de solo lectura en sentido histórico. En equipos actuales, el firmware suele almacenarse en memoria flash reprogramable, no necesariamente en una ROM inmutable. La denominación ROM se mantiene en el temario para estudiar la función de memoria no volátil asociada al firmware.

Distingue:
- **RAM:** memoria de trabajo, rápida y normalmente volátil.
- **Firmware:** software de bajo nivel que inicializa y configura hardware; suele residir en memoria no volátil.
- **Almacenamiento:** conserva archivos y programas incluso cuando el equipo se apaga.

## 1.1.10 — SSD

Un SSD utiliza memoria flash y no tiene partes móviles para acceder a los datos.

## 1.1.11 — HDD

Un HDD almacena datos magnéticamente en platos giratorios y utiliza cabezales mecánicos.

| Criterio | HDD | SSD |
|---|---|---|
| Tecnología | Magnética y mecánica | Memoria flash |
| Latencia de acceso | Mayor por movimiento mecánico | Generalmente menor |
| Resistencia a golpes | Sensible a impactos durante operación | Sin platos móviles |
| Coste por capacidad | A menudo menor | A menudo mayor |
| Ruido/vibración | Puede producirlos | Sin ruido mecánico |

El rendimiento real depende de interfaz, controlador, tipo de memoria, carga y estado del dispositivo. No se debe asumir que todo SSD tiene la misma velocidad.

**Ejercicio:** recomienda un tipo de unidad para un portátil que prioriza arranque rápido y movilidad, y otro para un archivo local de gran capacidad con presupuesto limitado. Explica las compensaciones y recuerda que siempre se requiere una estrategia de copias de seguridad.

## 1.1.12 — GPU

La GPU está especializada en procesar grandes cantidades de operaciones gráficas y otras cargas paralelas. Puede estar integrada en el procesador o ser una tarjeta dedicada. En una tarjeta dedicada suelen existir procesador gráfico, memoria propia y circuitos de alimentación y refrigeración.

La GPU no reemplaza a la CPU: ambas cooperan. La CPU coordina gran parte de la ejecución general y la GPU acelera cargas adecuadas para su arquitectura.

**Caso:** renderizar una escena 3D puede aprovechar miles de operaciones paralelas; ejecutar lógica secuencial compleja puede depender más de la CPU.

## 1.1.13 — Motherboard (placa base)

La motherboard es la placa de circuito impreso que conecta procesador, RAM, almacenamiento, expansión, alimentación y periféricos. Incluye zócalos, ranuras, conectores, circuitos de regulación de energía y controladores.

La compatibilidad exige revisar, entre otros elementos:
- socket y compatibilidad de CPU;
- chipset y firmware;
- tipo, generación y capacidad de RAM;
- formato físico y espacio de la caja;
- conectores de almacenamiento y expansión;
- potencia y conectores de la fuente.

No se debe comprar una pieza basándose únicamente en que «cabe» físicamente.

## 1.1.14 — Buses

Un bus o interconexión permite transferir información entre componentes. Para entender su función se distinguen conceptualmente señales de datos, direcciones y control; los diseños actuales pueden usar enlaces punto a punto y protocolos complejos en lugar de un bus único compartido.

Al comparar interconexiones importa el ancho, la velocidad de transferencia, la codificación, el protocolo y la topología. No confundas el ancho de banda teórico con el rendimiento observado por una aplicación.

## 1.1.15 — Fuente de alimentación

La fuente convierte la corriente alterna de la red en tensiones continuas que necesitan los componentes. Debe ofrecer potencia suficiente, conectores compatibles y protecciones eléctricas adecuadas. Una fuente de mayor potencia nominal no hace automáticamente más rápido el computador.

Nunca abras una fuente de alimentación: puede conservar tensiones peligrosas incluso desconectada. Para esta etapa basta identificar su etiqueta, conectores y función externa. Las intervenciones internas corresponden a personal cualificado.

## 1.1.16 — Periféricos

Un periférico permite entrada, salida, almacenamiento o comunicación:
- entrada: teclado, ratón, micrófono, escáner;
- salida: monitor, impresora, altavoces;
- entrada/salida: pantalla táctil, interfaz de red, dispositivos de almacenamiento externos.

La clasificación depende de la función en el flujo de información, no de la apariencia del dispositivo. Una pantalla táctil, por ejemplo, presenta imagen y recibe interacción.

## Laboratorio — Inventario de hardware sin desmontaje

**Objetivo:** identificar los componentes de un computador real o de un equipo de laboratorio y explicar su función.

1. Registra fabricante/modelo del equipo y sistema operativo.
2. Consulta la información de CPU, núcleos e hilos mediante herramientas del sistema.
3. Registra RAM instalada y tipo si la herramienta lo expone.
4. Identifica unidades de almacenamiento y su tipo solo cuando el sistema lo indique de forma fiable.
5. Identifica GPU integrada/dedicada y motherboard si la información está disponible.
6. Dibuja un diagrama de componentes y conexiones.
7. Anota qué datos no pudiste confirmar y cómo los verificarías con documentación del fabricante.

**Seguridad:** no abras el equipo ni desconectes componentes energizados. No publiques números de serie, identificadores únicos ni datos personales del dispositivo.

### Entregables
- tabla de inventario con campo, valor, fuente y nivel de confianza;
- diagrama de relación entre CPU, RAM, almacenamiento, GPU, placa y periféricos;
- análisis de dos posibles cuellos de botella sin afirmar que un componente es culpable sin medición;
- conclusión de compatibilidad o limitaciones observadas.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Identificación correcta de componentes | 25 |
| Explicación de CPU, memoria y GPU | 20 |
| Diagrama coherente | 15 |
| Calidad y trazabilidad del inventario | 15 |
| Análisis razonado de rendimiento/compatibilidad | 15 |
| Seguridad y comunicación técnica | 10 |

## Autoevaluación

1. ¿Qué diferencia hay entre CPU y ALU?
2. ¿Por qué un núcleo no equivale a un hilo de software?
3. ¿Qué información expresa la frecuencia y qué no expresa?
4. ¿Para qué sirve la caché y por qué existen niveles?
5. ¿Qué diferencia existe entre RAM y almacenamiento persistente?
6. ¿Qué papel cumple la GPU y por qué no sustituye a la CPU?
7. ¿Qué compatibilidades revisarías antes de instalar una CPU?
8. ¿Por qué no debes abrir una fuente de alimentación?

**Respuestas orientativas:** la ALU es una unidad funcional dentro del procesador; un hilo de software es una secuencia planificada y un núcleo es recurso físico; GHz mide ciclos por segundo, no instrucciones por segundo; la caché reduce accesos a memoria más distante; RAM es memoria de trabajo volátil y SSD/HDD almacenamiento persistente; GPU acelera cargas paralelas; la compatibilidad incluye socket, chipset, firmware y potencia; la fuente puede retener energía peligrosa.

## Recursos audiovisuales

No se incorpora un video en esta versión: no se ha verificado una pieza concreta cuyo audio hablado sea español y que cubra de forma fiel el conjunto de componentes de este módulo. Se prefiere no recomendar un recurso genérico o no comprobado. La lección puede estudiarse con el texto, el laboratorio y las referencias.

## Referencias

- EducACCIÓN dixital (Xunta de Galicia), **Hardware interno**, material educativo institucional: https://recursos.edu.xunta.gal/sites/default/files/recurso/1639064660/hardware_interno.html
- IES Antonio González González, **Arquitectura y funcionamiento del ordenador**, material didáctico institucional: https://centros.edu.xunta.gal/iesblancoamorculleredo/aulavirtual/mod/book/view.php?chapterid=4332&id=19998
- Intel, **Intel® 64 and IA-32 Architectures Software Developer’s Manuals**, documentación técnica primaria: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- AMD, **Processor Specifications**, documentación de producto: https://www.amd.com/en/products/specifications/processors.html

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** laboratorio propuesto; no ejecutado ni validado en hardware físico en esta entrega.  
**Nota editorial:** mantener el estado de borrador hasta revisión técnica y pedagógica.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** revisión documental de alineación con el módulo 1.1 del roadmap, cobertura de los títulos oficiales, secuencia didáctica, consistencia terminológica, ejemplos, actividad práctica, evaluación, seguridad y referencias.

**Resultado:** revisión interna realizada; no equivale a aprobación académica externa ni a validación práctica. Se identificaron los ajustes anotados en este registro y se mantienen explícitas las actividades pendientes. Los laboratorios y ejemplos no se declaran ejecutados. Antes de cambiar el estado editorial se requiere cotejo bibliográfico final, ejecución reproducible de actividades y revisión por un segundo evaluador.

**Hallazgos y pendientes específicos:** Se revisó la correspondencia temática, secuencia conceptual, terminología, ejemplos, laboratorio, evaluación y referencias. El inventario sin desmontaje y las advertencias eléctricas son adecuados para nivel inicial. Pendiente: cotejar cada referencia externa en la ronda bibliográfica y ejecutar el laboratorio con hardware real.
