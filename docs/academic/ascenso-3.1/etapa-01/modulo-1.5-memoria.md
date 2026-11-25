# Etapa 1 · Módulo 1.5 — Memoria

**Estado:** borrador académico desarrollado (pendiente validación editorial externa y verificación técnica formal).  
**Alineación:** ASCENSO 3.1, Etapa 1, Módulo 1.5.  
**Última actualización:** 2026-11-24

## Identificación del módulo
- **Etapa:** 1 — Fundamentos de computación y arquitectura del computador.
- **Módulo:** 1.5 — Memoria.
- **Lecciones oficiales:** 6 (1.5.1 a 1.5.6).
- **Prerrequisitos:** Módulos 1.1 a 1.4, especialmente 1.1.7-1.1.8 y 1.3.6.

## Propósito del módulo
Comprender cómo se organiza y gestiona la memoria en un sistema informático: física, virtual, stack, heap, paginación y direccionamiento.

## Resultados de aprendizaje del módulo
1. Diferenciar memoria física y virtual.
2. Explicar stack y heap y sus riesgos.
3. Comprender paginación y direccionamiento a nivel conceptual.
4. Relacionar memoria con rendimiento, estabilidad y seguridad.

---

## Lección 1.5.1 — Memoria física

### Identificación
- **Lección oficial:** 1.5.1 — Memoria física. **Secuencia:** 1/6.

### Propósito de aprendizaje
Comprender qué es la memoria física y cómo la usa el sistema.

### Conocimientos previos
- RAM, buses, CPU.

### Resultados de aprendizaje
- Definir memoria física.
- Distinguir memoria física de virtual y de almacenamiento.
- Explicar limitaciones de capacidad.
- Reconocer impacto en rendimiento.

### Desarrollo conceptual
La memoria física es la RAM instalada realmente en el equipo: chips de memoria accesibles por el hardware. El sistema operativo y el firmware gestionan cómo se asigna a procesos, kernel, cachés y buffers.

La cantidad de memoria física es finita. Cuando se agota, el sistema puede recurrir a swap/paginación en disco, lo que degrada rendimiento. La memoria física también tiene características como velocidad, canales, latencia y ECC en algunos entornos.

No debe confundirse con el espacio de direcciones que ve un proceso. Un proceso puede “ver” direcciones virtuales que el sistema mapea a marcos físicos.

### Ejemplo técnico desarrollado
**Equipo con 8 GB RAM:**
- SO y servicios usan ~2 GB.
- Navegador usa ~3 GB.
- IDE usa ~2 GB.
- Queda ~1 GB libre/buffers.
Al abrir una VM de 2 GB, el sistema puede empezar a usar swap.

### Práctica guiada
- Observa memoria física total y usada en tu sistema. Registra valores y calcula porcentaje de uso.

### Actividad independiente
Explica por qué dos equipos con la misma RAM pueden comportarse distinto bajo la misma carga.

### Criterios de aceptación
- Define memoria física correctamente.
- La relaciona con RAM instalada.
- Distingue de memoria virtual.

### Errores frecuentes y recomendaciones
- **Error:** confundir RAM con espacio en disco. **Recomendación:** revisar unidades y métricas.
- **Error:** asumir que RAM libre siempre debe ser 0 o siempre debe ser alta. **Recomendación:** entender cachés y buffers del SO.

### Evaluación de comprensión
1. ¿Qué es memoria física?
2. ¿Qué ocurre cuando se agota?
3. ¿Por qué la memoria física no es lo mismo que la dirección que ve un programa?

### Referencias
- Microsoft Learn. *Memory management*. https://learn.microsoft.com/en-us/windows/win32/memory/memory-management. Consultado: 2026-11-24.
- Linux man-pages. *proc(5)* - `/proc/meminfo`. https://man7.org/linux/man-pages/man5/proc.5.html. Consultado: 2026-11-24.

---

## Lección 1.5.2 — Memoria virtual

### Identificación
- **Lección oficial:** 1.5.2 — Memoria virtual. **Secuencia:** 2/6.

### Propósito de aprendizaje
Comprender la memoria virtual como abstracción del sistema operativo.

### Conocimientos previos
- Lección 1.5.1, 1.3.6.

### Resultados de aprendizaje
- Definir memoria virtual.
- Explicar beneficios: aislamiento, abstracción, uso eficiente.
- Comprender mapeo virtual-físico a alto nivel.
- Identificar costo de page faults/swap.

### Desarrollo conceptual
La memoria virtual es una abstracción que proporciona a cada proceso un espacio de direcciones propio. El sistema operativo y la MMU traducen direcciones virtuales a direcciones físicas. Esto permite aislar procesos, simplificar la programación, usar más memoria aparente que la física disponible y proteger áreas de memoria.

Beneficios:
- **Aislamiento:** un proceso no accede directamente a memoria de otro sin permisos.
- **Comodidad:** cada proceso ve un espacio organizado.
- **Eficiencia:** solo se cargan páginas necesarias.
- **Protección:** permisos de lectura/escritura/ejecución.

Costo: la traducción y los fallos de página tienen overhead. Si el sistema usa swap intensivamente, el rendimiento cae.

### Ejemplo técnico desarrollado
**Proceso A y B:**
- Ambos pueden tener una variable en la dirección virtual `0x00400000`.
- La MMU las mapea a marcos físicos distintos.
- Así, no se pisan entre sí.

### Práctica guiada
- Explica en un párrafo por qué la memoria virtual mejora la seguridad.

### Actividad independiente
Investiga qué es un page fault y diferencia entre minor y major page fault.

### Criterios de aceptación
- Define memoria virtual.
- Explica aislamiento y mapeo.
- Menciona un costo.

### Errores frecuentes y recomendaciones
- **Error:** creer que memoria virtual es solo swap. **Recomendación:** swap es una parte/uso relacionado, no la definición completa.
- **Error:** pensar que memoria virtual elimina límites físicos. **Recomendación:** la RAM física sigue siendo finita.

### Evaluación de comprensión
1. ¿Qué problema resuelve la memoria virtual?
2. ¿Qué hace la MMU?
3. ¿Por qué el swap puede ser lento?

### Referencias
- Silberschatz, A., et al. *Operating System Concepts*. Wiley.
- Intel. *Software Developer Manuals*, capítulos de paging/memory management. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.

---

## Lección 1.5.3 — Stack

### Identificación
- **Lección oficial:** 1.5.3 — Stack. **Secuencia:** 3/6.

### Propósito de aprendizaje
Comprender la pila de ejecución y su uso en llamadas a funciones.

### Conocimientos previos
- Lecciones 1.3.5, 1.5.1-1.5.2.

### Resultados de aprendizaje
- Definir stack.
- Explicar stack frames, variables locales y retorno.
- Identificar stack overflow.
- Relacionar stack con recursión y seguridad.

### Desarrollo conceptual
El **stack** (pila) es una región de memoria usada para gestionar llamadas a funciones. Funciona principalmente con disciplina LIFO (last in, first out). Cada llamada a función suele crear un **stack frame** con parámetros, dirección de retorno, variables locales y estado necesario.

El stack es rápido y gestionado automáticamente. Cuando la función termina, su frame se libera. El tamaño del stack es limitado; recursión profunda o grandes estructuras locales pueden causar **stack overflow**.

En seguridad, desbordamientos de buffer en stack fueron históricamente críticos. Las mitigaciones modernas incluyen canarios, ASLR, NX/DEP y compiladores seguros, pero el concepto sigue siendo importante.

### Ejemplo técnico desarrollado
**Llamada a función:**

```c
int suma(int a, int b) {
  int r = a + b;
  return r;
}
int main() {
  int x = suma(2, 3);
}
```

1. `main` crea frame.
2. Llama a `suma`: se apila frame con `a`, `b`, retorno, `r`.
3. `suma` retorna 5.
4. Frame de `suma` se desapila.
5. `main` continúa con `x=5`.

### Práctica guiada
- Dibuja el stack antes, durante y después de la llamada a `suma`.

### Actividad independiente
Escribe un ejemplo de recursión sin caso base y explica por qué produce stack overflow.

### Criterios de aceptación
- Define stack y frame.
- Muestra orden LIFO.
- Identifica causa de stack overflow.

### Errores frecuentes y recomendaciones
- **Error:** confundir stack con heap. **Recomendación:** stack automático/LIFO; heap dinámico.
- **Error:** creer que stack overflow solo es “error de programación menor”. **Recomendación:** puede ser falla o vector de seguridad.

### Evaluación de comprensión
1. ¿Qué contiene un stack frame?
2. ¿Qué significa LIFO?
3. ¿Cómo puede ocurrir un stack overflow?

### Referencias
- Bryant, R. E., & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective*. Pearson.
- OWASP. *Buffer Overflow*. https://owasp.org/www-community/vulnerabilities/Buffer_Overflow. Consultado: 2026-11-24.

---

## Lección 1.5.4 — Heap

### Identificación
- **Lección oficial:** 1.5.4 — Heap. **Secuencia:** 4/6.

### Propósito de aprendizaje
Comprender la memoria heap y la asignación dinámica.

### Conocimientos previos
- Lección 1.5.3.

### Resultados de aprendizaje
- Definir heap.
- Distinguir asignación estática/automática/dinámica.
- Identificar problemas: fugas, doble liberación, use-after-free.
- Relacionar heap con gestión de memoria.

### Desarrollo conceptual
El **heap** es una región de memoria para asignación dinámica. A diferencia del stack, los objetos en heap pueden vivir más allá del ámbito de una función, pero su gestión depende del lenguaje/runtime: manual (C/C++), o automática por garbage collector (Java, Go, etc.).

El heap es flexible, pero más complejo. Errores comunes:
- **Memory leak:** no liberar memoria ya no usada.
- **Double free:** liberar dos veces.
- **Use-after-free:** usar memoria ya liberada.
- **Fragmentación:** espacios libres dispersos.

La elección stack/heap afecta rendimiento, seguridad y diseño.

### Ejemplo técnico desarrollado
**C:**
```c
int *p = malloc(sizeof(int));
*p = 42;
free(p);
// p ahora es dangling pointer si se usa
```

**Java:**
```java
String s = new String("hola"); // objeto en heap (conceptualmente)
```
El GC libera cuando ya no hay referencias alcanzables.

### Práctica guiada
- Clasifica: variable local int, objeto creado con `new`, array global. ¿Dónde suele vivir?

### Actividad independiente
Explica por qué un memory leak puede ser grave en un servicio que corre semanas.

### Criterios de aceptación
- Define heap.
- Distingue stack/heap.
- Identifica al menos 2 errores de memoria.

### Errores frecuentes y recomendaciones
- **Error:** creer que heap es “malo” y stack “bueno”. **Recomendación:** son herramientas con usos distintos.
- **Error:** asumir que GC elimina toda fuga. **Recomendación:** puede haber fugas lógicas por referencias retenidas.

### Evaluación de comprensión
1. ¿Cuándo usarías heap?
2. ¿Qué es use-after-free?
3. ¿Qué diferencia hay entre fuga de memoria y liberación correcta?

### Referencias
- Bryant, R. E., & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective*. Pearson.
- OWASP. *Memory leak / Use after free* (referencias de vulnerabilidades). https://owasp.org/www-community/vulnerabilities/. Consultado: 2026-11-24.

---

## Lección 1.5.5 — Paginación

### Identificación
- **Lección oficial:** 1.5.5 — Paginación. **Secuencia:** 5/6.

### Propósito de aprendizaje
Comprender la paginación como mecanismo de gestión de memoria virtual.

### Conocimientos previos
- Lecciones 1.5.1-1.5.2.

### Resultados de aprendizaje
- Definir página, marco y tabla de páginas.
- Explicar page fault a nivel básico.
- Comprender beneficios de paginación.
- Identificar costo de thrashing.

### Desarrollo conceptual
La **paginación** divide la memoria virtual en bloques de tamaño fijo llamados **páginas**, y la memoria física en **marcos** del mismo tamaño. La tabla de páginas mapea páginas virtuales a marcos físicos.

Cuando un proceso accede a una página no cargada en RAM, ocurre un **page fault**. El sistema operativo debe cargarla desde disco/swap si aplica. Esto es normal en pequeñas cantidades, pero excesivo causa **thrashing**: el sistema pasa más tiempo paginando que ejecutando.

La paginación permite aislamiento, asignación no contigua y uso eficiente de memoria. También introduce overhead por tablas de páginas y traducción; el TLB (Translation Lookaside Buffer) ayuda a acelerar traducciones recientes.

### Ejemplo técnico desarrollado
**Page fault:**
1. Proceso accede a dirección virtual en página P3.
2. MMU consulta tabla: P3 no está en RAM.
3. Se genera page fault.
4. SO carga P3 desde disco a un marco libre.
5. Actualiza tabla de páginas.
6. Reintenta la instrucción.

### Práctica guiada
- Dibuja un mapeo simple: 4 páginas virtuales a 3 marcos físicos, con una página en disco.

### Actividad independiente
Explica qué es thrashing y qué síntoma podría observar un usuario.

### Criterios de aceptación
- Define página, marco, tabla de páginas.
- Explica page fault.
- Describe thrashing.

### Errores frecuentes y recomendaciones
- **Error:** confundir paginación con segmentación. **Recomendación:** mencionar que son técnicas distintas; aquí se estudia paginación.
- **Error:** pensar que todo page fault es error. **Recomendación:** hay page faults normales.

### Evaluación de comprensión
1. ¿Qué es un marco?
2. ¿Qué ocurre en un page fault?
3. ¿Por qué el thrashing degrada el sistema?

### Referencias
- Silberschatz, A., et al. *Operating System Concepts*. Wiley.
- Intel. *SDM Vol. 3A: Paging*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.

---

## Lección 1.5.6 — Direccionamiento de memoria

### Identificación
- **Lección oficial:** 1.5.6 — Direccionamiento de memoria. **Secuencia:** 6/6.

### Propósito de aprendizaje
Comprender cómo se identifican y acceden ubicaciones de memoria.

### Conocimientos previos
- Lecciones 1.2.3, 1.3.5, 1.5.1-1.5.5.

### Resultados de aprendizaje
- Definir dirección de memoria.
- Distinguir dirección física y virtual.
- Comprender direccionamiento absoluto/relativo a nivel básico.
- Relacionar direccionamiento con punteros y seguridad.

### Desarrollo conceptual
Una **dirección de memoria** identifica una ubicación en el espacio de memoria. En sistemas modernos, los programas suelen usar **direcciones virtuales**, traducidas a **direcciones físicas** por la MMU.

El direccionamiento puede ser:
- **Directo/absoluto:** la instrucción indica la dirección.
- **Indirecto:** la dirección está en un registro o memoria.
- **Relativo a base/desplazamiento:** útil para estructuras, arrays y stack frames.
- **PC-relative:** común en saltos.

Los punteros en lenguajes como C almacenan direcciones. Un puntero inválido puede causar fallos o vulnerabilidades. La memoria virtual y protecciones de página ayudan a limitar daños.

### Ejemplo técnico desarrollado
**Array en C:**
```c
int a[4] = {10,20,30,40};
int *p = &a[2]; // p guarda dirección de a[2]
```
Si `a` empieza en `0x1000` y cada int ocupa 4 bytes, `a[2]` está en `0x1008`. El direccionamiento por base + índice permite acceder eficientemente.

### Práctica guiada
- Calcula la dirección de `a[3]` si `a[0]` está en `0x2000` y cada elemento ocupa 4 bytes. Respuesta: `0x200C`.

### Actividad independiente
Explica la diferencia entre dirección virtual y física con una analogía, indicando su límite.

### Criterios de aceptación
- Define dirección de memoria.
- Distingue física y virtual.
- Calcula desplazamiento simple.

### Errores frecuentes y recomendaciones
- **Error:** asumir que direcciones vistas en un programa son físicas. **Recomendación:** en SO modernos, normalmente son virtuales.
- **Error:** confundir valor con dirección. **Recomendación:** un puntero contiene dirección; al desreferenciar obtienes valor.

### Evaluación de comprensión
1. ¿Qué es una dirección virtual?
2. ¿Cómo se calcula la dirección de un elemento de array?
3. ¿Por qué el direccionamiento incorrecto puede ser peligroso?

### Referencias
- Intel. *Software Developer Manuals*. https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html. Consultado: 2026-11-24.
- Bryant, R. E., & O'Hallaron, D. R. *Computer Systems: A Programmer's Perspective*. Pearson.

---

## Cierre del módulo
- **Evaluación:** explicar memoria física/virtual, diferenciar stack/heap, describir paginación y calcular direccionamiento simple.
- **Criterio:** 75% y capacidad de justificar decisiones básicas de memoria.