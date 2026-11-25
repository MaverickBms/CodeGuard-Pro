# Etapa 6 · Módulo 6.1 — Estructuras lineales

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.1. **Última actualización:** 2026-11-24

## Identificación
- **Etapa:** 6 — Estructuras de datos y algoritmos. **Objetivo oficial:** dominar estructuras de datos y algoritmos fundamentales.
- **Módulo:** 6.1 — Estructuras lineales. **Lecciones oficiales:** 9 (6.1.1 a 6.1.9).

## Propósito
Comprender y usar estructuras lineales para almacenar y procesar datos secuenciales.

---

## Lección 6.1.1 — Arrays
- **Oficial:** 6.1.1 — Arrays. **Sec:** 1/9. **Propósito:** usar arreglos como estructura base.
- **Prerrequisitos:** 3.4.2. **Resultados:** acceso O(1), recorrido O(n), conocer límites.
- **Desarrollo:** array almacena elementos contiguos, tamaño fijo. Acceso por índice rápido; inserción/eliminación en medio costosa por desplazamiento.
- **Ejemplo:** `int[] a={1,2,3}; a[1]=5;`
- **Práctica:** implementar búsqueda lineal.
- **Independiente:** insertar elemento en posición dada.
- **Criterios:** manejo de índices correcto.
- **Errores:** out of bounds.
- **Eval:** ¿Cuál es el costo de acceso por índice?
- **Ref:** Cormen et al. *Introduction to Algorithms*. MIT Press.

## Lección 6.1.2 — Listas enlazadas
- **Oficial:** 6.1.2 — Listas enlazadas. **Sec:** 2/9. **Propósito:** entender nodos y punteros/referencias.
- **Resultados:** distinguir array vs linked list, implementar inserción/eliminación.
- **Desarrollo:** cada nodo contiene dato y referencia al siguiente. Inserción/eliminación O(1) si tienes referencia; acceso por índice O(n). Más memoria por punteros.
- **Práctica:** implementar lista enlazada simple.
- **Independiente:** invertir lista enlazada.
- **Criterios:** enlaces correctos, sin pérdida de nodos.
- **Errores:** perder referencia al head; ciclos accidentales.
- **Eval:** ¿Cuándo conviene linked list sobre array?
- **Ref:** Cormen et al.

## Lección 6.1.3 — Listas doblemente enlazadas
- **Oficial:** 6.1.3 — Listas doblemente enlazadas. **Sec:** 3/9.
- **Resultados:** recorrer en ambos sentidos, insertar/eliminar con prev/next.
- **Desarrollo:** cada nodo tiene `prev` y `next`. Facilita eliminación y recorrido inverso; cuesta más memoria y cuidado de punteros.
- **Práctica:** insertar al final en lista doble.
- **Independiente:** eliminar nodo dado actualizando prev/next.
- **Criterios:** punteros consistentes.
- **Errores:** no actualizar prev; null pointer.
- **Eval:** ¿Qué ventaja da el puntero prev?
- **Ref:** Cormen et al.

## Lección 6.1.4 — Listas circulares
- **Oficial:** 6.1.4 — Listas circulares. **Sec:** 4/9.
- **Resultados:** entender ciclo final->inicio.
- **Desarrollo:** el último nodo apunta al primero. Útil en round-robin, buffers circulares. Requiere condición de parada cuidadosa para evitar bucles infinitos.
- **Práctica:** recorrer lista circular con límite.
- **Independiente:** implementar cola circular simple.
- **Criterios:** terminación correcta.
- **Errores:** bucle infinito.
- **Eval:** ¿Qué caso de uso tiene una lista circular?
- **Ref:** Cormen et al.

## Lección 6.1.5 — Pilas (Stack)
- **Oficial:** 6.1.5 — Pilas (Stack). **Sec:** 5/9.
- **Resultados:** aplicar LIFO, push/pop/peek.
- **Desarrollo:** stack es LIFO. Operaciones O(1). Usos: undo, llamadas, evaluación de expresiones, DFS.
```java
Deque<Integer> st = new ArrayDeque<>();
st.push(1); st.push(2); st.pop(); // 2
```
- **Práctica:** validar paréntesis balanceados.
- **Independiente:** implementar stack con array.
- **Criterios:** orden LIFO correcto.
- **Errores:** pop en stack vacío.
- **Eval:** ¿Qué significa LIFO?
- **Ref:** Java Docs. *Deque*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Deque.html (2026-11-24).

## Lección 6.1.6 — Colas (Queue)
- **Oficial:** 6.1.6 — Colas (Queue). **Sec:** 6/9.
- **Resultados:** aplicar FIFO, enqueue/dequeue.
- **Desarrollo:** queue es FIFO. Usos: scheduling, BFS, buffers. `ArrayDeque` o `LinkedList` en Java.
```java
Queue<String> q = new ArrayDeque<>();
q.add("a"); q.add("b"); q.poll(); // a
```
- **Práctica:** simular cola de atención.
- **Independiente:** implementar cola con dos stacks (conceptual).
- **Criterios:** orden FIFO correcto.
- **Errores:** usar stack cuando se necesita queue.
- **Eval:** ¿Qué significa FIFO?
- **Ref:** Java Docs. *Queue*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Queue.html (2026-11-24).

## Lección 6.1.7 — Colas de prioridad
- **Oficial:** 6.1.7 — Colas de prioridad. **Sec:** 7/9.
- **Resultados:** usar priority queue, entender heap.
- **Desarrollo:** priority queue entrega primero el elemento de mayor prioridad (según comparador). Implementación típica: heap binario. Inserción/extracción O(log n).
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(5); pq.add(1); pq.add(3); pq.poll(); // 1
```
- **Práctica:** obtener los 3 menores de una lista.
- **Independiente:** simular agenda por prioridad.
- **Criterios:** orden por prioridad correcto.
- **Errores:** asumir orden total interno; mutar elementos clave.
- **Eval:** ¿Cuál es la complejidad de poll en heap?
- **Ref:** Java Docs. *PriorityQueue*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/PriorityQueue.html (2026-11-24).

## Lección 6.1.8 — Deques
- **Oficial:** 6.1.8 — Deques. **Sec:** 8/9.
- **Resultados:** usar cola doblemente terminada.
- **Desarrollo:** deque permite inserción/eliminación por ambos extremos. Puede comportarse como stack o queue. `ArrayDeque` es implementación común.
- **Práctica:** implementar ventana deslizante simple.
- **Independiente:** usar deque como stack y como queue.
- **Criterios:** operaciones correctas en ambos extremos.
- **Errores:** elegir estructura menos adecuada.
- **Eval:** ¿Qué puede hacer un deque que una queue normal no?
- **Ref:** Java Docs. *Deque*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Deque.html (2026-11-24).

## Lección 6.1.9 — Buffers circulares
- **Oficial:** 6.1.9 — Buffers circulares. **Sec:** 9/9.
- **Resultados:** implementar buffer de tamaño fijo con índices circulares.
- **Desarrollo:** buffer circular usa array fijo y dos índices (head/tail) con módulo. Útil en streams, productores/consumidores, audio. Manejar lleno/vacío.
- **Práctica:** implementar buffer circular de tamaño N.
- **Independiente:** simula productor/consumidor simple.
- **Criterios:** sobrescritura o bloqueo definido, índices correctos.
- **Errores:** off-by-one; confundir lleno y vacío.
- **Eval:** ¿Cómo avanzan los índices en un buffer circular?
- **Ref:** Cormen et al.