# Etapa 1 · Módulo 1.5 — Memoria

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 1, apartado 1.5.  
**Temas oficiales:** memoria física, memoria virtual, stack, heap, paginación y direccionamiento de memoria.

## Objetivo

Comprender cómo un sistema representa, asigna y administra memoria durante la ejecución de programas, y distinguir memoria física de memoria virtual.

## Resultados de aprendizaje

Podrás explicar memoria física y virtual; describir direcciones virtuales y físicas; explicar el papel de la paginación y las tablas de páginas; diferenciar stack y heap; e interpretar de forma introductoria cómo se reserva y libera memoria.

## 1.5.1 — Memoria física

La memoria física principal suele ser RAM instalada en el equipo. Está organizada en ubicaciones direccionables y su capacidad es finita. El sistema operativo administra su uso entre kernel y procesos.

La RAM no debe confundirse con el espacio de almacenamiento de un SSD/HDD. Ambos guardan información, pero tienen propiedades, latencias y funciones distintas. Algunas plataformas pueden utilizar mecanismos de memoria comprimida o paginación respaldada por almacenamiento; esto no convierte al SSD en RAM equivalente.

## 1.5.2 — Memoria virtual

La memoria virtual ofrece a cada proceso un espacio de direcciones que el sistema operativo y la unidad de gestión de memoria (MMU) traducen y protegen. Los procesos pueden utilizar direcciones virtuales sin conocer directamente la ubicación física de cada dato.

Beneficios:
- aislamiento entre procesos;
- protección de permisos de lectura/escritura/ejecución;
- asignación flexible de memoria;
- posibilidad de mapear archivos y regiones compartidas;
- abstracción de la disposición física.

Una dirección virtual no equivale necesariamente a una dirección física. La traducción puede involucrar tablas de páginas y cachés de traducción (TLB).

## 1.5.3 — Stack (pila de llamadas)

El stack suele almacenar marcos de llamadas, variables locales de duración automática y datos necesarios para retornar de funciones. Su organización exacta depende de ABI, compilador, lenguaje y arquitectura.

Ejemplo conceptual:
1. una función A llama a B;
2. se crea un marco de llamada para B;
3. B utiliza sus datos locales;
4. B retorna y su marco deja de estar activo.

La pila suele tener límites y un crecimiento definido por la plataforma. Una recursión excesiva o estructuras locales demasiado grandes pueden contribuir a un stack overflow.

No todos los objetos de un lenguaje se almacenan necesariamente en el stack: optimizaciones del compilador y reglas del lenguaje pueden cambiar su ubicación.

## 1.5.4 — Heap (memoria dinámica)

El heap es una región utilizada para asignaciones dinámicas cuya duración no está necesariamente ligada al retorno de una función. Los lenguajes y entornos administran esta memoria de formas distintas:
- gestión manual (por ejemplo, reservar y liberar explícitamente);
- conteo de referencias;
- recolector de basura;
- propiedad y préstamos comprobados por el compilador;
- combinaciones de estrategias.

Una fuga de memoria ocurre cuando un programa mantiene memoria que ya no necesita y no la libera o deja de poder acceder a ella para liberarla. La fragmentación puede dificultar aprovechar el espacio disponible. Un uso-after-free aparece cuando se utiliza memoria después de haberla liberado en sistemas donde esa gestión es manual.

**Importante:** stack y heap son conceptos de organización/gestión, no dos chips físicos separados.

## 1.5.5 — Paginación

La paginación divide el espacio virtual en páginas y la memoria física en marcos de página. Las tablas de páginas registran cómo se mapean páginas virtuales a marcos físicos y qué permisos aplican.

Una referencia a una página que no está disponible en memoria física puede provocar un fallo de página. El sistema operativo decide cómo resolverlo: cargar contenido, asignar un marco, recuperar una página respaldada o informar un error si el acceso no es válido.

No todos los fallos de página son errores del programa: algunos son parte normal del funcionamiento de memoria virtual. Un fallo de página no válido, en cambio, puede producir una excepción o terminar el proceso.

## 1.5.6 — Direccionamiento de memoria

Una dirección identifica una posición o región dentro de un espacio de direcciones. En sistemas con memoria virtual, el proceso utiliza direcciones virtuales y la MMU participa en su traducción a direcciones físicas.

Conceptos básicos:
- **espacio de direcciones:** conjunto de direcciones que puede utilizar un contexto;
- **dirección virtual:** dirección vista por el proceso;
- **dirección física:** ubicación en memoria física;
- **página:** bloque del espacio virtual;
- **marco:** bloque correspondiente de memoria física;
- **permiso:** regla que determina si una región puede leerse, escribirse o ejecutarse.

La cantidad de bits de una dirección no siempre equivale directamente a la RAM instalada. Los sistemas pueden implementar menos bits físicos o virtuales que el ancho nominal de los registros.

## Ejemplo integrado

Un programa accede a una variable situada en una dirección virtual. La MMU consulta la TLB; si no existe una traducción válida en caché, puede consultar las tablas de páginas. La traducción determina el marco físico y los permisos. Si la página no está presente, el procesador genera un fallo de página y el sistema operativo decide cómo continuar.

Este ejemplo es conceptual: las optimizaciones y detalles varían entre arquitecturas y sistemas operativos.

## Laboratorio — Observar memoria de procesos

**Objetivo:** observar el uso de memoria de un proceso propio y documentar la diferencia entre memoria virtual y física.

1. Abre una herramienta de monitorización del sistema operativo.
2. Selecciona un proceso no crítico que hayas iniciado.
3. Registra memoria virtual/reservada y memoria residente/física si la herramienta las distingue.
4. Observa cómo cambian los valores al abrir y cerrar una función de la aplicación.
5. Compara dos procesos con cargas diferentes.
6. Explica por qué el valor virtual no equivale automáticamente a RAM ocupada.
7. Dibuja un esquema simple de proceso → espacio virtual → páginas → marcos físicos.

No fuerces agotamiento de memoria, no ejecutes pruebas de estrés en equipos compartidos y no inspecciones procesos de otras personas.

### Extensión opcional: stack y heap

Usa un programa pequeño de tu autoría y la documentación de su lenguaje para identificar:
- una llamada a función y sus variables locales;
- una estructura con duración dinámica;
- cómo el lenguaje administra su ciclo de vida.

No deduzcas la ubicación física exacta de una variable únicamente por su sintaxis: el compilador puede optimizar o transformar la representación.

### Entregables

- tabla de observaciones con herramienta, proceso, unidad y momento;
- diagrama de memoria virtual/física;
- explicación stack/heap con un ejemplo;
- análisis de un fallo de página y su resolución;
- apartado de limitaciones y datos no observados.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Memoria física y virtual | 20 |
| Direccionamiento y traducción | 20 |
| Paginación y fallo de página | 20 |
| Stack y heap | 20 |
| Observación segura y conclusiones | 20 |

## Ejercicios

1. ¿Por qué dos procesos pueden utilizar direcciones virtuales iguales sin referirse a la misma memoria física?
2. ¿Qué diferencia hay entre stack y heap?
3. ¿Qué papel cumple una tabla de páginas?
4. ¿Qué ocurre conceptualmente ante un fallo de página?
5. ¿Por qué no todo fallo de página significa que el programa esté roto?
6. ¿Por qué no es correcto afirmar que cada variable local siempre está físicamente en el stack?

**Respuestas orientativas:** cada proceso tiene un espacio virtual aislado y las traducciones pueden apuntar a marcos distintos; stack suele asociarse a llamadas y heap a asignación dinámica; tablas mapean páginas y permisos; el sistema operativo resuelve el acceso o reporta error; los fallos pueden ser normales cuando una página debe cargarse; optimizaciones del compilador, registros y reglas del lenguaje pueden cambiar la ubicación.

## Autoevaluación

Explica el recorrido de una lectura desde una dirección virtual hasta la memoria física. Incluye TLB, tabla de páginas, permisos y fallo de página. Después explica cómo difieren el ciclo de vida de una variable local y el de una asignación dinámica, evitando asumir detalles que dependen del lenguaje.

## Recursos audiovisuales

No se incluye video en esta versión: no se ha verificado una pieza en español que trate directamente memoria virtual, paginación, stack, heap y direccionamiento con precisión suficiente. La explicación escrita y el laboratorio de observación se mantienen como recursos principales.

## Referencias

- Linux Kernel Documentation, **Concepts overview / Memory Management**: https://docs.kernel.org/admin-guide/mm/
- Microsoft Learn, **Virtual Address Spaces**: https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces
- Intel, **Intel® 64 and IA-32 Architectures Software Developer’s Manuals** (paginación y gestión de memoria): https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- Arm, **Arm Architecture Reference Manuals**: https://developer.arm.com/documentation
- OpenStax, **Computer Science / Computer Architecture** (material educativo abierto, según disponibilidad): https://openstax.org/

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** laboratorio de observación propuesto; no ejecutado.  
**Estado editorial:** borrador.
