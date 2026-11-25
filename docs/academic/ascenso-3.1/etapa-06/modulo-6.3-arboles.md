# Etapa 6 · Módulo 6.3 — Árboles

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.3. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.3 — Árboles. **Lecciones oficiales:** 7 (6.3.1 a 6.3.7).

## Lección 6.3.1 — Árboles binarios
- **Oficial:** 6.3.1 — Árboles binarios. **Sec:** 1/7. **Propósito:** entender estructura jerárquica binaria.
- **Resultados:** definir nodo, raíz, hoja, altura; recorrer árbol.
- **Desarrollo:** cada nodo tiene hasta 2 hijos. Recorridos: preorden, inorden, postorden, por niveles.
- **Práctica:** implementa recorrido inorden.
- **Independiente:** calcula altura de árbol.
- **Criterios:** recorridos correctos.
- **Errores:** confundir recorridos.
- **Eval:** ¿Qué es un nodo hoja?
- **Ref:** Cormen et al.

## Lección 6.3.2 — Árboles binarios de búsqueda
- **Oficial:** 6.3.2 — Árboles binarios de búsqueda. **Sec:** 2/7. **Propósito:** usar BST para búsqueda ordenada.
- **Resultados:** insertar/buscar, entender propiedad BST.
- **Desarrollo:** para cada nodo, izquierda < nodo < derecha (según definición). Búsqueda promedio O(log n), peor caso O(n) si desbalanceado.
- **Práctica:** inserta valores y busca uno.
- **Independiente:** muestra caso degenerado.
- **Criterios:** propiedad BST preservada.
- **Errores:** no manejar duplicados según política.
- **Eval:** ¿Cuál es el peor caso de un BST?
- **Ref:** Cormen et al.

## Lección 6.3.3 — Árboles AVL
- **Oficial:** 6.3.3 — Árboles AVL. **Sec:** 3/7. **Propósito:** mantener BST balanceado.
- **Resultados:** entender factor de balance y rotaciones.
- **Desarrollo:** AVL mantiene diferencia de altura entre subárboles <= 1. Usa rotaciones simples/dobles. Garantiza O(log n).
- **Práctica:** identifica rotación necesaria en ejemplo.
- **Independiente:** traza inserción que requiere rotación.
- **Criterios:** comprende balance.
- **Errores:** aplicar rotación incorrecta.
- **Eval:** ¿Qué garantiza AVL?
- **Ref:** Cormen et al.

## Lección 6.3.4 — Árboles Red-Black
- **Oficial:** 6.3.4 — Árboles Red-Black. **Sec:** 4/7. **Propósito:** conocer árbol balanceado usado en librerías.
- **Resultados:** entender propiedades básicas y uso práctico.
- **Desarrollo:** árbol rojo-negro mantiene balance con reglas de color. Usado en TreeMap/TreeSet de Java. Garantiza O(log n) en operaciones.
- **Práctica:** explica por qué TreeMap usa árbol balanceado.
- **Independiente:** compara AVL y Red-Black a alto nivel.
- **Criterios:** reconoce propósito y complejidad.
- **Errores:** creer que siempre es más rápido que hash en todo.
- **Eval:** ¿Dónde se usa Red-Black en Java?
- **Ref:** Java Docs; Cormen et al.

## Lección 6.3.5 — Árboles B
- **Oficial:** 6.3.5 — Árboles B. **Sec:** 5/7. **Propósito:** entender estructuras para almacenamiento en disco/DB.
- **Resultados:** explicar nodos con múltiples claves, uso en índices.
- **Desarrollo:** B-Trees reducen altura y accesos a disco. Usados en bases de datos y filesystems. Nodos contienen múltiples claves e hijos.
- **Práctica:** explica por qué un índice DB usa B-Tree.
- **Independiente:** compara B-Tree con BST para disco.
- **Criterios:** relaciona con IO.
- **Errores:** confundir con árbol binario.
- **Eval:** ¿Por qué B-Trees son útiles en DB?
- **Ref:** Cormen et al.; PostgreSQL Docs. https://www.postgresql.org/docs/current/indexes-types.html (2026-11-24).

## Lección 6.3.6 — Heaps
- **Oficial:** 6.3.6 — Heaps. **Sec:** 6/7. **Propósito:** usar heap para prioridad y ordenamiento.
- **Resultados:** entender min-heap/max-heap, insert/extract.
- **Desarrollo:** heap es árbol binario casi completo que cumple propiedad de heap. Raíz es mínimo o máximo. Base de priority queue y heapsort.
- **Práctica:** inserta elementos en min-heap.
- **Independiente:** explica heapsort a alto nivel.
- **Criterios:** propiedad de heap correcta.
- **Errores:** confundir heap de memoria con heap estructura de datos.
- **Eval:** ¿Qué es un min-heap?
- **Ref:** Cormen et al.

## Lección 6.3.7 — Tries
- **Oficial:** 6.3.7 — Tries. **Sec:** 7/7. **Propósito:** almacenar cadenas por prefijos.
- **Resultados:** insertar/buscar palabra/prefijo.
- **Desarrollo:** trie (árbol de prefijos) almacena caracteres por aristas/nodos. Útil para autocompletado, diccionarios, routing. Costo depende de longitud de clave.
- **Práctica:** implementa trie simple para insertar/buscar.
- **Independiente:** usa trie para autocompletar prefijos.
- **Criterios:** búsqueda por prefijo correcta.
- **Errores:** alto consumo de memoria sin optimizar.
- **Eval:** ¿Para qué es bueno un trie?
- **Ref:** Cormen et al.