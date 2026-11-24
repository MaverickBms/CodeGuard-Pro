# Etapa 6 · Módulo 6.5 — Algoritmos

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.5. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.5 — Algoritmos. **Lecciones oficiales:** 12 (6.5.1 a 6.5.12).

## Lección 6.5.1 — Búsqueda lineal
- **Oficial:** 6.5.1 — Búsqueda lineal. **Sec:** 1/12. **Resultados:** O(n), simple, funciona en datos no ordenados.
- **Práctica:** buscar elemento en array. **Eval:** ¿Peor caso? **Ref:** Cormen.

## Lección 6.5.2 — Búsqueda binaria
- **Oficial:** 6.5.2 — Búsqueda binaria. **Sec:** 2/12. **Resultados:** O(log n), requiere datos ordenados.
- **Desarrollo:** divide rango a la mitad. Cuidado con límites e índices.
- **Práctica:** implementar búsqueda binaria. **Errores:** off-by-one, overflow de mid en otros lenguajes.
- **Eval:** ¿Por qué requiere orden? **Ref:** Cormen.

## Lección 6.5.3 — Bubble Sort
- **Oficial:** 6.5.3 — Bubble Sort. **Sec:** 3/12. **Resultados:** O(n^2), simple, educativo.
- **Práctica:** ordenar array pequeño. **Eval:** ¿Cuándo es aceptable? **Ref:** Cormen.

## Lección 6.5.4 — Selection Sort
- **Oficial:** 6.5.4 — Selection Sort. **Sec:** 4/12. **Resultados:** O(n^2), pocos swaps.
- **Práctica:** implementar y contar swaps. **Eval:** ¿Complejidad? **Ref:** Cormen.

## Lección 6.5.5 — Insertion Sort
- **Oficial:** 6.5.5 — Insertion Sort. **Sec:** 5/12. **Resultados:** bueno para datos pequeños/casi ordenados.
- **Práctica:** ordenar lista casi ordenada. **Eval:** ¿Mejor caso? **Ref:** Cormen.

## Lección 6.5.6 — Merge Sort
- **Oficial:** 6.5.6 — Merge Sort. **Sec:** 6/12. **Resultados:** O(n log n), estable, usa memoria extra.
- **Práctica:** implementar merge sort. **Eval:** ¿Es estable? **Ref:** Cormen.

## Lección 6.5.7 — Quick Sort
- **Oficial:** 6.5.7 — Quick Sort. **Sec:** 7/12. **Resultados:** promedio O(n log n), peor O(n^2), in-place.
- **Desarrollo:** elegir pivote importa. Evitar peor caso con randomización/median-of-three.
- **Práctica:** implementar quicksort. **Eval:** ¿Qué afecta el peor caso? **Ref:** Cormen.

## Lección 6.5.8 — Heap Sort
- **Oficial:** 6.5.8 — Heap Sort. **Sec:** 8/12. **Resultados:** O(n log n), in-place, no estable.
- **Práctica:** ordenar con heap. **Eval:** ¿Diferencia con merge sort? **Ref:** Cormen.

## Lección 6.5.9 — Counting Sort
- **Oficial:** 6.5.9 — Counting Sort. **Sec:** 9/12. **Resultados:** no comparativo, para enteros en rango limitado.
- **Práctica:** ordenar valores 0..k. **Eval:** ¿Cuándo no conviene? **Ref:** Cormen.

## Lección 6.5.10 — Radix Sort
- **Oficial:** 6.5.10 — Radix Sort. **Sec:** 10/12. **Resultados:** ordena por dígitos/caracteres.
- **Práctica:** ordenar enteros por dígitos. **Eval:** ¿Qué dependencia tiene? **Ref:** Cormen.

## Lección 6.5.11 — Búsqueda en grafos
- **Oficial:** 6.5.11 — Búsqueda en grafos. **Sec:** 11/12. **Resultados:** aplicar BFS/DFS según problema.
- **Práctica:** elegir BFS o DFS para 2 casos. **Eval:** ¿BFS para qué? **Ref:** Cormen.

## Lección 6.5.12 — Algoritmos voraces
- **Oficial:** 6.5.12 — Algoritmos voraces. **Sec:** 12/12. **Resultados:** elegir óptimo local cuando es válido.
- **Desarrollo:** greedy funciona si tiene propiedad de elección voraz y subestructura óptima. No siempre da óptimo global.
- **Práctica:** problema de cambio (analizar casos). **Eval:** ¿Cuándo falla greedy? **Ref:** Cormen.