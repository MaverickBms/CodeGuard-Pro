# Etapa 6 · Módulo 6.7 — Complejidad

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.7. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.7 — Complejidad. **Lecciones oficiales:** 8 (6.7.1 a 6.7.8).

## Lección 6.7.1 — Big O
- **Oficial:** 6.7.1 — Big O. **Sec:** 1/8. **Resultados:** describir cota superior asintótica.
- **Desarrollo:** Big O describe crecimiento del costo con el tamaño de entrada. Ignora constantes y términos menores. Ej: O(1), O(log n), O(n), O(n log n), O(n^2).
- **Práctica:** clasifica 5 algoritmos por Big O. **Eval:** ¿Qué ignora Big O? **Ref:** Cormen.

## Lección 6.7.2 — Big Omega
- **Oficial:** 6.7.2 — Big Omega. **Sec:** 2/8. **Resultados:** entender cota inferior.
- **Desarrollo:** Ω describe el mejor crecimiento garantizado/cota inferior. Complementa Big O.
- **Práctica:** da Ω para búsqueda lineal. **Eval:** ¿Diferencia con Big O? **Ref:** Cormen.

## Lección 6.7.3 — Big Theta
- **Oficial:** 6.7.3 — Big Theta. **Sec:** 3/8. **Resultados:** cota ajustada.
- **Desarrollo:** Θ indica que el algoritmo crece asintóticamente igual en cota superior e inferior.
- **Práctica:** identifica Θ de recorrido de array. **Eval:** ¿Cuándo usar Θ? **Ref:** Cormen.

## Lección 6.7.4 — Complejidad temporal
- **Oficial:** 6.7.4 — Complejidad temporal. **Sec:** 4/8. **Resultados:** analizar tiempo según entrada.
- **Desarrollo:** contar operaciones dominantes, bucles anidados, recursión. Considerar mejor/promedio/peor caso.
- **Práctica:** analiza complejidad de dos bucles anidados. **Eval:** ¿Qué caso suele reportarse? **Ref:** Cormen.

## Lección 6.7.5 — Complejidad espacial
- **Oficial:** 6.7.5 — Complejidad espacial. **Sec:** 5/8. **Resultados:** analizar memoria usada.
- **Desarrollo:** incluye memoria auxiliar y, según convención, entrada. Recursión consume stack. Tradeoff tiempo/espacio.
- **Práctica:** compara espacio de merge sort vs quicksort. **Eval:** ¿La recursión usa espacio? **Ref:** Cormen.

## Lección 6.7.6 — Análisis de mejor caso
- **Oficial:** 6.7.6 — Análisis de mejor caso. **Sec:** 6/8. **Resultados:** identificar entrada más favorable.
- **Desarrollo:** útil pero no suficiente. Ej: insertion sort en array ordenado es O(n).
- **Práctica:** mejor caso de insertion sort. **Eval:** ¿Por qué no basta el mejor caso? **Ref:** Cormen.

## Lección 6.7.7 — Análisis de peor caso
- **Oficial:** 6.7.7 — Análisis de peor caso. **Sec:** 7/8. **Resultados:** garantizar límite superior.
- **Desarrollo:** importante para garantías. Ej: quicksort peor O(n^2), búsqueda lineal O(n).
- **Práctica:** peor caso de quicksort. **Eval:** ¿Por qué es útil? **Ref:** Cormen.

## Lección 6.7.8 — Análisis de caso promedio
- **Oficial:** 6.7.8 — Análisis de caso promedio. **Sec:** 8/8. **Resultados:** estimar comportamiento esperado.
- **Desarrollo:** requiere modelo de distribución de entradas. Útil cuando el peor caso es raro pero posible.
- **Práctica:** compara promedio y peor caso de quicksort. **Eval:** ¿Qué necesita el análisis promedio? **Ref:** Cormen.