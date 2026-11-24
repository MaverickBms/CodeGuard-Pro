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

### 6.1.1 — Arrays

Un array almacena elementos en posiciones indexadas. En Java su longitud se fija al crearlo y los índices válidos van de 0 a longitud menos uno. Acceder por índice suele ser O(1); insertar o eliminar en medio puede requerir desplazar elementos O(n).

### 6.1.2 — Matrices

Una matriz representa datos en dos dimensiones. En Java suele implementarse como un array de arrays, por lo que las filas pueden incluso tener longitudes distintas. Antes de recorrerla, verifica dimensiones y límites; no asumas que toda matriz es rectangular.

### 6.1.3 — Arrays dinámicos

Un array dinámico mantiene una capacidad que puede crecer. Cuando se agota la capacidad, suele reservarse un bloque mayor y copiar elementos. Por ello, añadir al final puede tener coste amortizado O(1), aunque una expansión individual cuesta O(n).

No confundas tamaño lógico (elementos usados) con capacidad reservada.

### 6.1.4 — Linked Lists

Una lista enlazada simple contiene nodos con valor y referencia al siguiente. Insertar o eliminar al inicio puede ser O(1); buscar una posición por índice suele ser O(n).

### 6.1.5 — Doubly Linked Lists

Una lista doblemente enlazada mantiene referencias al nodo siguiente y al anterior. Facilita recorridos en ambas direcciones y ciertas eliminaciones si ya se tiene la referencia al nodo, a costa de memoria adicional y de mantener dos enlaces coherentes.

### 6.1.6 — Circular Linked Lists

En una lista circular, el último nodo enlaza con el primero. La condición de terminación debe detectar el regreso al punto de partida; esperar encontrar un enlace nulo puede provocar un ciclo infinito.

### 6.1.7 — Stacks

Una pila sigue LIFO: el último elemento en entrar es el primero en salir. Operaciones típicas: push, pop y peek.

Usos: pila de llamadas, deshacer acciones, análisis de expresiones y recorridos iterativos.

### 6.1.8 — Queues

Una cola sigue FIFO: el primer elemento en entrar es el primero en salir. Operaciones habituales: enqueue y dequeue. Una implementación eficiente mantiene referencias a extremos o utiliza un buffer circular.

### 6.1.9 — Deques

Un deque permite insertar y retirar por ambos extremos. Puede utilizarse como cola o pila y resulta útil en algoritmos de ventana deslizante. Define claramente qué operaciones están permitidas y sus costes.

## 6.2 — Estructuras asociativas

### 6.2.1 — Hash Tables

Una tabla hash transforma claves mediante una función hash para ubicarlas en una tabla. Las operaciones de búsqueda, inserción y eliminación tienen coste esperado cercano a O(1) bajo supuestos adecuados; el peor caso puede ser O(n). El rendimiento depende de la distribución, capacidad y estrategia de colisiones.

### 6.2.2 — HashMap

Un HashMap asocia claves únicas con valores. En Java, la unicidad de claves depende de `equals()` y la distribución utiliza `hashCode()`. La API no garantiza un orden de iteración estable.

### 6.2.3 — HashSet

Un HashSet mantiene elementos únicos según igualdad lógica. En Java, su comportamiento depende del contrato coherente entre `equals()` y `hashCode()`.

### 6.2.4 — Diccionarios

Un diccionario es una abstracción clave-valor. El nombre y sus garantías varían por lenguaje: verifica si conserva orden, cómo compara claves y qué ocurre al consultar una clave ausente.

### 6.2.5 — Sets

Un set representa una colección de elementos únicos. Algunas implementaciones no conservan orden; otras mantienen orden de inserción o de comparación. La elección debe responder al contrato requerido.

### 6.2.6 — Hash Functions

Una función hash transforma una clave en un valor entero o código que la tabla utiliza para ubicarla. Una buena función distribuye las claves razonablemente, pero no evita todas las colisiones en un espacio finito.

### 6.2.7 — Hash Collisions

Una colisión ocurre cuando claves distintas comparten un índice o código relevante. Las tablas pueden resolverlas mediante encadenamiento o direccionamiento abierto. El hash de una tabla no es equivalente a un hash criptográfico: persiguen objetivos distintos.

## 6.3 — Árboles

### 6.3.1 — Trees

Un árbol es una estructura jerárquica de nodos conectados. Conceptos esenciales: raíz, padre, hijo, hoja, profundidad, altura y subárbol. En un árbol, cada nodo (salvo la raíz) tiene un único padre.

### 6.3.2 — Binary Trees

Cada nodo tiene como máximo dos hijos. Un árbol binario no necesariamente está ordenado.

### 6.3.3 — Binary Search Trees

En un árbol binario de búsqueda, los valores se organizan según una regla de orden. La búsqueda, inserción y eliminación dependen de la altura: O(h). En un árbol balanceado h es O(log n); en uno degenerado puede ser O(n).

Define qué ocurre con claves duplicadas antes de implementar.

### 6.3.4 — AVL Trees

Un AVL es un árbol binario de búsqueda autoequilibrado que mantiene una diferencia acotada de alturas entre subárboles mediante rotaciones. Las operaciones básicas mantienen O(log n).

### 6.3.5 — Heaps

Un heap binario es un árbol casi completo que mantiene una propiedad de prioridad (min-heap o max-heap). Insertar y extraer el extremo prioritario suelen costar O(log n); consultar el extremo, O(1).

### 6.3.6 — Priority Queues

Una priority queue es una abstracción que permite obtener el elemento de mayor o menor prioridad. Puede implementarse con un heap, pero no es sinónimo de heap. Debe definirse cómo se resuelven empates.

### 6.3.7 — Tries

Un trie organiza claves, a menudo cadenas, por prefijos. La búsqueda depende de la longitud de la clave y de la representación del alfabeto. Es útil para autocompletado y búsquedas por prefijo, aunque puede consumir bastante memoria.


## 6.4 — Grafos

### 6.4.1 — Grafos dirigidos

Un grafo dirigido contiene aristas con orientación: una arista de A a B no implica necesariamente una arista de B a A. Modela dependencias, flujos y relaciones asimétricas.

### 6.4.2 — Grafos no dirigidos

En un grafo no dirigido, una arista conecta dos vértices de forma bidireccional. La relación es simétrica y el grado de un vértice cuenta sus aristas incidentes (con el tratamiento habitual de lazos múltiples según el modelo).

### 6.4.3 — Grafos ponderados

Un grafo ponderado asigna un peso o coste a cada arista. El significado del peso debe documentarse (distancia, tiempo, costo, etc.). Algunos algoritmos requieren pesos no negativos.

### 6.4.4 — Matrices de adyacencia

Una matriz de adyacencia representa conexiones mediante una matriz V×V. Consultar si existe una arista puede ser O(1), pero el espacio es O(V²), incluso si el grafo es disperso. En grafos ponderados, la celda puede almacenar el peso.

### 6.4.5 — Listas de adyacencia

Una lista de adyacencia almacena los vecinos de cada vértice. El espacio suele ser O(V+E), por lo que resulta conveniente para grafos dispersos. Consultar una arista depende del grado y de la estructura usada.

### 6.4.6 — BFS

Breadth-First Search explora por niveles usando una cola. Con listas de adyacencia recorre el grafo en O(V+E). En grafos no ponderados permite encontrar caminos con el menor número de aristas.

### 6.4.7 — DFS

Depth-First Search explora tan profundo como sea posible antes de retroceder. Puede implementarse recursivamente o con una pila. Con listas de adyacencia tiene coste O(V+E) y ayuda a detectar componentes, ciclos y dependencias. En grafos grandes, la versión recursiva puede agotar la pila de llamadas; considera una implementación iterativa.

## 6.5 — Algoritmos

### 6.5.1 — Linear Search

Examina elementos hasta encontrar el objetivo o agotar la colección. Su coste temporal es O(n) en el peor caso y O(1) en el mejor si el primer elemento coincide.

### 6.5.2 — Binary Search

Reduce repetidamente el intervalo a la mitad; su coste es O(log n). Requiere datos ordenados y una representación con acceso eficiente al elemento medio. Mantén una convención coherente para límites inclusivos/exclusivos y evita desbordamientos al calcular el punto medio.

### 6.5.3 — Bubble Sort

Compara elementos adyacentes e intercambia los que están en orden incorrecto. Con una bandera de intercambio puede terminar en O(n) en el mejor caso; promedio y peor caso son O(n²). La implementación habitual es estable.

### 6.5.4 — Selection Sort

Selecciona el mínimo restante y lo coloca en la siguiente posición. Su coste es O(n²) en mejor, promedio y peor caso. La implementación habitual no es estable, pero realiza pocas escrituras.

### 6.5.5 — Insertion Sort

Inserta cada elemento en la posición adecuada de la parte ya ordenada. Es O(n) en el mejor caso y O(n²) en promedio y peor caso; suele ser estable y útil en arreglos pequeños o casi ordenados.

### 6.5.6 — Merge Sort

Divide el arreglo, ordena las mitades y combina los resultados. Su coste temporal es O(n log n) en todos los casos para la versión estándar y suele requerir memoria auxiliar O(n) en arreglos. La combinación habitual es estable.

### 6.5.7 — Quick Sort

Selecciona un pivote y particiona los elementos. Su coste esperado es O(n log n), pero puede degradarse a O(n²) con particiones muy desequilibradas. La versión habitual no es estable; la elección de pivote y partición influye en el rendimiento.

### 6.5.8 — Heap Sort

Construye un heap y extrae repetidamente el extremo prioritario. Tiene coste O(n log n) en mejor, promedio y peor caso, usa espacio auxiliar O(1) en implementaciones in-place y no es estable.

### 6.5.9 — Dijkstra

Encuentra caminos mínimos desde un origen en grafos con pesos no negativos. Con cola de prioridad y listas de adyacencia, una implementación con heap binario suele tener coste O((V+E) log V). No lo apliques directamente a aristas con pesos negativos.

### 6.5.10 — A*

Busca rutas utilizando el coste acumulado y una heurística estimada hacia el destino. La admisibilidad de la heurística es importante para garantizar optimalidad en las condiciones habituales; consistencia facilita la gestión de nodos cerrados. A* no es automáticamente óptimo si la heurística incumple sus condiciones.

### 6.5.11 — Prim

Construye un árbol de expansión mínima en un grafo no dirigido, conexo y ponderado, creciendo desde un vértice y seleccionando una arista de menor peso que conecte el árbol con un vértice nuevo. Para grafos no conexos, se puede repetir por componente para obtener un bosque.

### 6.5.12 — Kruskal

Ordena las aristas por peso y agrega aquellas que no crean ciclos, normalmente mediante una estructura Union-Find. En un grafo no conexo obtiene un bosque de expansión mínima.

## 6.6 — Técnicas

### 6.6.1 — Recursividad

Resuelve un problema mediante subproblemas del mismo tipo. Requiere un caso base y progreso hacia él. Considera profundidad, coste de llamadas y riesgo de desbordar la pila.

### 6.6.2 — Divide and Conquer

Divide un problema en subproblemas, resuelve cada uno y combina resultados. Merge Sort es un ejemplo clásico. Analiza el número de subproblemas, su tamaño y el coste de combinar.

### 6.6.3 — Greedy

Toma decisiones locales que parecen mejores en cada paso. Solo produce una solución óptima cuando el problema y la estrategia satisfacen propiedades que lo justifican. No basta con que una elección parezca buena.

### 6.6.4 — Backtracking

Explora posibilidades y retrocede cuando una decisión parcial viola restricciones o no puede conducir a una solución. Es útil para combinaciones, laberintos y problemas de restricciones, aunque puede tener coste exponencial.

### 6.6.5 — Dynamic Programming

Resuelve subproblemas solapados y reutiliza resultados mediante memoización o tabulación. Se justifica cuando existe subestructura óptima y repetición de subproblemas. Documenta el estado, transición y casos base.

### 6.6.6 — Two Pointers

Utiliza dos índices que avanzan según una regla. Puede reducir una solución O(n²) a O(n) en problemas con condiciones adecuadas, por ejemplo, arreglos ordenados. Justifica por qué mover cada puntero no descarta una solución válida.

### 6.6.7 — Sliding Window

Mantiene una ventana sobre una secuencia y actualiza su estado al mover los límites. Es útil para subarreglos o subcadenas contiguos. La eficiencia depende de poder actualizar la ventana incrementalmente y de las propiedades del problema.

## 6.7 — Complejidad

### 6.7.1 — Big O

Big O expresa una cota asintótica superior: el crecimiento queda acotado por una función multiplicada por una constante para tamaños suficientemente grandes. No significa necesariamente «peor caso» si no se especifica el objeto analizado.

### 6.7.2 — Big Ω

Big Ω expresa una cota asintótica inferior. Tampoco equivale por sí sola al «mejor caso»: describe una cota para la función de coste que se esté estudiando.

### 6.7.3 — Big Θ

Big Θ expresa una cota asintótica ajustada, superior e inferior del mismo orden. Indica que el crecimiento queda acotado por arriba y por abajo por múltiplos constantes de la misma función.

### 6.7.4 — Complejidad temporal

Describe cómo crece el trabajo de un algoritmo respecto al tamaño de entrada. Explicita qué operación se cuenta y cuál es el parámetro de tamaño.

### 6.7.5 — Complejidad espacial

Describe cómo crece la memoria utilizada. Aclara si se cuenta memoria auxiliar, estructuras de salida o la propia entrada; la convención debe mantenerse en la comparación.

### 6.7.6 — Mejor caso

Es el menor coste entre las entradas de tamaño n para la métrica definida. No debe confundirse con una cota Ω sin especificar la función de coste.

### 6.7.7 — Caso promedio

Es el coste esperado o promedio bajo una distribución de entradas declarada. Sin distribución o modelo probabilístico, «promedio» queda indefinido.

### 6.7.8 — Peor caso

Es el máximo coste entre entradas de tamaño n bajo el modelo definido. Es útil para establecer garantías superiores, aunque no describe necesariamente el comportamiento típico.

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
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Registro de revisión editorial interna — 2026-11-24

**Alcance:** cotejo de las entradas oficiales del roadmap, precisión conceptual, secuencia, ejemplos, prácticas, evaluación, seguridad y referencias.

**Resultado:** revisión documental interna realizada con los ajustes y hallazgos siguientes: Se detectó y eliminó una repetición no numerada de la lección Tries. Se revisó la correspondencia de los 57 temas, la distinción entre estructuras y algoritmos, y las condiciones de uso de Dijkstra, árboles balanceados y complejidad asintótica. Pendiente: compilar implementaciones Java, ejecutar pruebas de propiedades/casos límite y medir complejidad empírica sin confundir medición con cota asintótica.

**Límite de validación:** no se ejecutaron laboratorios, scripts, servicios, bases de datos, máquinas virtuales ni capturas de red en esta revisión. No se declara aprobación académica externa. La etapa continúa en desarrollo hasta completar las pruebas reproducibles y la segunda revisión.
