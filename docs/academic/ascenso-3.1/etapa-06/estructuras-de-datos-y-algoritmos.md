# Etapa 6 — Estructuras de datos y algoritmos

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 6.  
**Prioridad:** P1 · Obligatoria.  
**Objetivo oficial:** comprender cómo organizar información y desarrollar soluciones eficientes.

## Temario oficial

- **6.1 Estructuras lineales:** arrays, matrices, arrays dinámicos, linked lists, doubly linked lists, circular linked lists, stacks, queues y deques.
- **6.2 Estructuras asociativas:** hash tables, HashMap, HashSet, diccionarios, sets, hash functions y hash collisions.
- **6.3 Árboles:** trees, binary trees, binary search trees, AVL trees, heaps, priority queues y tries.
- **6.4 Grafos:** dirigidos, no dirigidos, ponderados, matrices/listas de adyacencia, BFS y DFS.
- **6.5 Algoritmos:** búsqueda lineal y binaria; Bubble, Selection, Insertion, Merge, Quick y Heap Sort; Dijkstra, A*, Prim y Kruskal.
- **6.6 Técnicas:** recursividad, divide and conquer, greedy, backtracking, dynamic programming, two pointers y sliding window.
- **6.7 Complejidad:** Big O, Big Ω, Big Θ, complejidad temporal y espacial, mejor caso, caso promedio y peor caso.

**Proyecto oficial:** biblioteca de estructuras de datos implementadas desde cero en Java.

## Resultados de aprendizaje

Podrás seleccionar estructuras según las operaciones dominantes; implementar estructuras básicas y probar invariantes; comparar búsquedas y ordenamientos; recorrer árboles y grafos; aplicar técnicas algorítmicas y justificar complejidad temporal y espacial sin confundir notación asintótica con mediciones de un equipo concreto.

## 6.1 — Estructuras lineales

### Arrays y matrices

Un array almacena elementos en posiciones indexadas. En arrays de tamaño fijo, acceder por índice suele ser O(1), mientras que insertar o eliminar en medio puede requerir desplazar elementos O(n).

Una matriz es una estructura bidimensional, que puede implementarse como array de arrays. Su representación en memoria depende del lenguaje y la implementación.

### Arrays dinámicos

Un array dinámico mantiene una capacidad que puede crecer. Cuando se agota la capacidad, suele reservarse un bloque mayor y copiar elementos. Por ello, añadir al final puede tener coste amortizado O(1), aunque una expansión individual cuesta O(n).

No confundas tamaño lógico (elementos usados) con capacidad reservada.

### Linked Lists

Una lista enlazada simple contiene nodos con valor y referencia al siguiente. Insertar/eliminar al inicio puede ser O(1), pero buscar una posición por índice suele ser O(n).

Una lista doblemente enlazada mantiene referencias al siguiente y anterior, facilitando recorridos en ambas direcciones, a costa de memoria adicional y más invariantes.

Una lista circular enlaza el último nodo con el primero. Debes controlar condiciones de terminación para evitar recorridos infinitos.

### Stacks

Una pila sigue LIFO: el último elemento en entrar es el primero en salir. Operaciones típicas: push, pop y peek.

Usos: pila de llamadas, deshacer acciones, análisis de expresiones y recorridos iterativos.

### Queues y deques

Una cola sigue FIFO: primero en entrar, primero en salir. Operaciones: enqueue y dequeue.

Un deque permite insertar y retirar por ambos extremos. Puede utilizarse como cola o pila y es útil en algoritmos de ventana deslizante.

**Comparación de selección:** arrays favorecen acceso indexado; listas enlazadas favorecen ciertas inserciones con referencia al nodo; pilas/colas expresan restricciones de acceso; deques permiten ambos extremos. No elijas solo por nombre: analiza operaciones, memoria y localidad de caché.

## 6.2 — Estructuras asociativas

### Hash tables

Una tabla hash utiliza una función hash para transformar una clave en una posición o índice de almacenamiento. Permite búsquedas, inserciones y eliminaciones con coste esperado cercano a O(1) bajo supuestos adecuados; el peor caso puede ser O(n).

### HashMap, HashSet, diccionarios y sets

- **HashMap/diccionario:** asocia claves con valores.
- **HashSet/set:** mantiene elementos únicos según su criterio de igualdad.
- Los nombres y contratos concretos dependen del lenguaje.

En Java, `HashMap` y `HashSet` dependen de `hashCode()` y `equals()`. Si dos objetos se consideran iguales, deben producir códigos hash iguales. No modifiques campos que afectan hash/equality mientras el objeto sea clave dentro de una tabla hash.

### Funciones hash y colisiones

Una colisión ocurre cuando dos claves producen el mismo índice/hash relevante. Las implementaciones resuelven colisiones mediante estrategias como encadenamiento o direccionamiento abierto.

Una buena función hash distribuye claves razonablemente, pero no elimina matemáticamente todas las colisiones en un espacio finito. Hash de tablas no es lo mismo que hash criptográfico: tienen objetivos y propiedades diferentes.

## 6.3 — Árboles

Un árbol es una estructura jerárquica de nodos conectados. Conceptos: raíz, padre, hijo, hoja, profundidad, altura y subárbol.

### Binary Trees

Cada nodo tiene como máximo dos hijos. Un árbol binario no necesariamente está ordenado.

### Binary Search Trees

En un árbol binario de búsqueda, los valores se organizan según una regla de orden. La búsqueda, inserción y eliminación dependen de la altura: O(h). En un árbol balanceado h es O(log n); en uno degenerado puede ser O(n).

Define qué ocurre con claves duplicadas antes de implementar.

### AVL Trees

Un AVL es un árbol binario de búsqueda autoequilibrado que mantiene una diferencia acotada de alturas entre subárboles mediante rotaciones. Las operaciones básicas mantienen O(log n).

### Heaps y priority queues

Un heap binario es un árbol casi completo que mantiene una propiedad de prioridad (min-heap o max-heap). Insertar y extraer el extremo prioritario suelen costar O(log n); consultar el extremo, O(1).

Una priority queue es una abstracción que permite obtener el elemento de mayor o menor prioridad. Puede implementarse con heap, no es sinónimo de heap.

### Tries

Un trie organiza claves, a menudo cadenas, por prefijos. La búsqueda depende de la longitud de la clave y del alfabeto/representación. Es útil para autocompletado y búsquedas por prefijo, aunque puede consumir mucha memoria.

## 6.4 — Grafos

Un grafo contiene vértices y aristas. Puede modelar rutas, dependencias, redes y relaciones.

- **Dirigido:** cada arista tiene dirección.
- **No dirigido:** la relación es bidireccional.
- **Ponderado:** las aristas tienen un peso o coste.

### Matriz de adyacencia

Representa conexiones mediante una matriz V×V. Consultar si existe una arista puede ser O(1), pero el espacio es O(V²), incluso si el grafo es disperso.

### Lista de adyacencia

Almacena vecinos de cada vértice. El espacio suele ser O(V+E), por lo que es conveniente para grafos dispersos. Consultar una arista depende del grado del vértice y de la estructura usada.

### BFS

Breadth-First Search explora por niveles usando una cola. En listas de adyacencia recorre el grafo en O(V+E). En grafos no ponderados permite encontrar caminos con el menor número de aristas.

### DFS

Depth-First Search explora tan profundo como sea posible antes de retroceder. Puede implementarse recursivamente o con una pila. También tiene coste O(V+E) con listas de adyacencia y ayuda a detectar componentes, ciclos y dependencias.

En grafos grandes, la versión recursiva puede agotar la pila de llamadas; considera implementación iterativa.

## 6.5 — Algoritmos

### Búsquedas

- **Linear Search:** examina elementos hasta encontrar el objetivo o agotar la colección; O(n).
- **Binary Search:** reduce repetidamente el intervalo a la mitad; O(log n), pero requiere datos ordenados y acceso apropiado al elemento medio.

La búsqueda binaria aplicada a datos no ordenados no produce resultados fiables.

### Ordenamientos

| Algoritmo | Mejor/medio/peor (general) | Estable | Observación |
|---|---|---|---|
| Bubble Sort | O(n) optimizado / O(n²) / O(n²) | Sí, con implementación usual | Didáctico; poco eficiente a gran escala |
| Selection Sort | O(n²) / O(n²) / O(n²) | No, en implementación usual | Pocas escrituras |
| Insertion Sort | O(n) / O(n²) / O(n²) | Sí | Bueno para arreglos pequeños o casi ordenados |
| Merge Sort | O(n log n) / O(n log n) / O(n log n) | Sí, implementación usual | Requiere memoria auxiliar para arrays |
| Quick Sort | O(n log n) esperado / O(n log n) esperado / O(n²) | No, usualmente | Depende de pivote y partición |
| Heap Sort | O(n log n) en casos habituales | No | Orden in-place con heap |

Las propiedades pueden variar con la implementación. En proyectos reales, usa bibliotecas estándar salvo que el objetivo sea aprender o exista una necesidad justificada.

### Dijkstra

Encuentra caminos mínimos desde un origen en grafos con pesos no negativos. Con cola de prioridad y listas de adyacencia, su complejidad depende de la implementación (por ejemplo, O((V+E) log V) con heap binario). No debe aplicarse sin más a aristas con pesos negativos.

### A*

Busca rutas utilizando coste acumulado y heurística estimada hacia el destino. La calidad y admisibilidad de la heurística afectan optimalidad y rendimiento. A* no es automáticamente óptimo si la heurística viola sus condiciones.

### Prim y Kruskal

Ambos construyen un árbol de expansión mínima en un grafo no dirigido, conexo y ponderado:
- Prim crece un árbol seleccionando aristas de menor coste que conectan el árbol con un nuevo vértice.
- Kruskal ordena aristas y agrega aquellas que no crean ciclos, normalmente usando Union-Find.

Si el grafo no es conexo, el resultado natural es un bosque de expansión mínima.

## 6.6 — Técnicas

### Recursividad

Resuelve un problema mediante subproblemas del mismo tipo. Requiere caso base y progreso hacia él. Considera profundidad y coste de llamadas.

### Divide and Conquer

Divide un problema en subproblemas, resuelve cada uno y combina resultados. Merge Sort es un ejemplo clásico.

### Greedy

Toma decisiones locales que parecen mejores en cada paso. Solo produce una solución óptima cuando el problema y la estrategia satisfacen propiedades que lo justifican. No basta con que una elección «parezca buena».

### Backtracking

Explora posibilidades y retrocede cuando una decisión parcial viola restricciones o no puede conducir a una solución. Es útil para problemas de combinaciones, laberintos y restricciones, aunque puede tener coste exponencial.

### Dynamic Programming

Resuelve subproblemas solapados y reutiliza resultados mediante memoización o tabulación. Se justifica cuando hay subestructura óptima y repetición de subproblemas.

### Two Pointers

Utiliza dos índices que avanzan según una regla. Puede reducir una solución O(n²) a O(n) en problemas con condiciones adecuadas, por ejemplo arreglos ordenados.

### Sliding Window

Mantiene una ventana sobre una secuencia y actualiza su estado al mover los límites. Es útil para subarreglos/subcadenas contiguos. La eficiencia depende de poder actualizar la ventana incrementalmente.

## 6.7 — Complejidad

### Complejidad temporal y espacial

La complejidad temporal describe cómo crece el trabajo de un algoritmo respecto al tamaño de entrada. La espacial describe cómo crece la memoria adicional utilizada, aclarando si se cuenta o no la entrada.

### Big O, Big Ω y Big Θ

- **O(g(n)):** cota asintótica superior.
- **Ω(g(n)):** cota asintótica inferior.
- **Θ(g(n)):** cota ajustada, superior e inferior del mismo orden.

Estas notaciones describen crecimiento cuando n aumenta; no indican segundos exactos ni velocidad de un equipo.

### Mejor, promedio y peor caso

- mejor caso: entrada más favorable para la métrica;
- caso promedio: promedio bajo una distribución de entradas declarada;
- peor caso: máximo coste entre entradas de tamaño n.

No se debe afirmar un caso promedio sin especificar supuestos de distribución.

### Reglas de análisis inicial

- operaciones secuenciales: sumar costes y conservar el término dominante;
- ciclos anidados: analizar cuántas veces se ejecuta cada uno;
- dividir el tamaño por una constante: suele producir crecimiento logarítmico;
- recursión: formular una recurrencia y resolverla;
- estructuras de datos: considerar coste de operaciones y supuestos de implementación.

Ejemplos:
- recorrer n elementos: O(n);
- dos bucles completos anidados: O(n²);
- búsqueda binaria: O(log n);
- merge sort: O(n log n).

## Proyecto oficial — Biblioteca de estructuras de datos en Java

Implementa desde cero, con fines educativos, las estructuras y algoritmos principales estudiados. No reemplaces la implementación por llamadas a colecciones estándar; puedes utilizarlas en pruebas de referencia, pero no como implementación de la estructura evaluada.

### Alcance progresivo

1. Array dinámico.
2. Lista enlazada simple y doble.
3. Stack, queue y deque.
4. Hash table con estrategia de colisiones documentada.
5. BST y AVL.
6. Heap y priority queue.
7. Trie.
8. Grafo con lista y matriz de adyacencia.
9. BFS y DFS.
10. Búsquedas y ordenamientos.
11. Dijkstra, A*, Prim y Kruskal, con supuestos explícitos.
12. Técnicas de resolución y análisis de complejidad.

### Contrato de cada implementación

Documenta:
- operaciones soportadas;
- precondiciones y postcondiciones;
- tratamiento de duplicados y elementos nulos;
- invariantes;
- complejidad temporal y espacial;
- casos límite;
- pruebas unitarias;
- limitaciones conocidas.

### Pruebas mínimas

- estructura vacía;
- un elemento;
- muchos elementos;
- duplicados;
- valores extremos;
- eliminación de raíz/primer/último elemento;
- colisiones hash;
- árbol degenerado y balanceado;
- grafo desconectado;
- ciclo;
- peso cero y peso negativo cuando el algoritmo lo permita o deba rechazarlo;
- ordenamiento de datos repetidos y ya ordenados.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Estructuras lineales | 15 |
| Estructuras asociativas | 15 |
| Árboles y heaps | 15 |
| Grafos y recorridos | 15 |
| Algoritmos de búsqueda/ordenamiento | 15 |
| Técnicas algorítmicas | 10 |
| Complejidad, pruebas y documentación | 15 |

## Autoevaluación

1. ¿Qué operación favorece un array y cuál una lista enlazada?
2. ¿Qué diferencia existe entre stack y queue?
3. ¿Qué condición permite esperar O(1) promedio en una tabla hash?
4. ¿Qué diferencia hay entre BST y AVL?
5. ¿Cuándo conviene una lista de adyacencia frente a matriz?
6. ¿Por qué binary search requiere datos ordenados?
7. ¿Qué algoritmo de camino mínimo requiere pesos no negativos?
8. ¿Cuándo se utiliza Prim o Kruskal?
9. ¿Qué diferencia hay entre greedy y dynamic programming?
10. ¿Qué expresa Θ(n log n) y qué no expresa?

**Respuestas orientativas:** arrays permiten acceso indexado; listas permiten ciertas inserciones con referencia al nodo; stack es LIFO y queue FIFO; hash requiere distribución adecuada y control de colisiones; AVL mantiene equilibrio; lista de adyacencia suele ser eficiente en grafos dispersos; binary search descarta mitades según orden; Dijkstra requiere pesos no negativos; Prim/Kruskal obtienen expansión mínima; greedy toma decisiones locales y DP reutiliza subproblemas; Θ describe crecimiento ajustado, no tiempo exacto.

## Recursos audiovisuales

No se incorporan videos en esta versión. Cada estructura o algoritmo requiere una pieza en español que enseñe ese concepto y no solo una introducción general. Hasta verificar audio, exactitud y correspondencia temática, el contenido escrito, las implementaciones y las pruebas constituyen la ruta principal.

## Referencias

- OpenDSA, **Data Structures and Algorithms** (material educativo abierto): https://opendsa-server.cs.vt.edu/
- MIT OpenCourseWare, **Introduction to Algorithms**: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/
- Princeton, **Algorithms, 4th Edition — Online material**: https://algs4.cs.princeton.edu/home/
- Oracle, **Java Collections Framework** (para comparar contratos de API; no sustituye la implementación desde cero): https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/doc-files/coll-reference.html
- NIST, **Dictionary of Algorithms and Data Structures**: https://www.nist.gov/dads

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** implementaciones y proyecto propuestos; no compilados ni ejecutados en esta sesión.  
**Estado editorial:** en desarrollo; no aprobado ni publicado..
