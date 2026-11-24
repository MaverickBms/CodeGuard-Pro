# Etapa 6 · Módulo 6.6 — Técnicas

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.6. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.6 — Técnicas. **Lecciones oficiales:** 7 (6.6.1 a 6.6.7).

## Lección 6.6.1 — Divide y vencerás
- **Oficial:** 6.6.1 — Divide y vencerás. **Sec:** 1/7. **Resultados:** dividir, resolver, combinar.
- **Desarrollo:** aplica en merge sort, quick sort, búsqueda binaria. Útil cuando subproblemas son independientes.
- **Práctica:** analiza merge sort con divide y vencerás. **Eval:** ¿Qué problemas encajan? **Ref:** Cormen.

## Lección 6.6.2 — Programación dinámica
- **Oficial:** 6.6.2 — Programación dinámica. **Sec:** 2/7. **Resultados:** subproblemas solapados, memoización/tabulación.
- **Desarrollo:** DP guarda resultados para evitar recomputo. Ejemplo: Fibonacci memoizado, mochila.
- **Práctica:** Fibonacci con memoización. **Eval:** ¿Diferencia con divide y vencerás? **Ref:** Cormen.

## Lección 6.6.3 — Backtracking
- **Oficial:** 6.6.3 — Backtracking. **Sec:** 3/7. **Resultados:** explorar soluciones y retroceder.
- **Desarrollo:** útil en N-reinas, Sudoku, combinaciones. Poda reduce espacio de búsqueda.
- **Práctica:** generar permutaciones. **Eval:** ¿Qué es poda? **Ref:** Cormen.

## Lección 6.6.4 — Recursión
- **Oficial:** 6.6.4 — Recursión. **Sec:** 4/7. **Resultados:** caso base, progreso, pila de llamadas.
- **Desarrollo:** ver 3.3.7; aquí aplicada a algoritmos/estructuras. Considerar stack y convertir a iterativo si necesario.
- **Práctica:** recorrido recursivo de árbol. **Eval:** ¿Riesgo de recursión profunda? **Ref:** Cormen.

## Lección 6.6.5 — Memoización
- **Oficial:** 6.6.5 — Memoización. **Sec:** 5/7. **Resultados:** cachear resultados de función pura.
- **Desarrollo:** top-down con caché. Requiere claves de estado válidas. Reduce tiempo a costa de memoria.
- **Práctica:** memoizar Fibonacci. **Eval:** ¿Cuándo usar memoización? **Ref:** Cormen.

## Lección 6.6.6 — Tabulación
- **Oficial:** 6.6.6 — Tabulación. **Sec:** 6/7. **Resultados:** DP bottom-up con tabla.
- **Desarrollo:** construye solución desde casos base hacia el objetivo. Evita recursión profunda.
- **Práctica:** Fibonacci tabulado. **Eval:** ¿Diferencia con memoización? **Ref:** Cormen.

## Lección 6.6.7 — Algoritmos aleatorizados
- **Oficial:** 6.6.7 — Algoritmos aleatorizados. **Sec:** 7/7. **Resultados:** usar aleatoriedad para rendimiento/robustez.
- **Desarrollo:** ejemplo: quicksort con pivote aleatorio, hashing aleatorizado. Analizar esperado vs peor caso.
- **Práctica:** randomizar pivote. **Eval:** ¿Qué mejora la aleatorización? **Ref:** Cormen.