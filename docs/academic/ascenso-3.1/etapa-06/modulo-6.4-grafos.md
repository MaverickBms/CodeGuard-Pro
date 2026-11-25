# Etapa 6 · Módulo 6.4 — Grafos

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.4. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.4 — Grafos. **Lecciones oficiales:** 7 (6.4.1 a 6.4.7).

## Lección 6.4.1 — Representación de grafos
- **Oficial:** 6.4.1 — Representación de grafos. **Sec:** 1/7. **Resultados:** usar lista y matriz de adyacencia.
- **Desarrollo:** lista de adyacencia eficiente en grafos dispersos; matriz útil en grafos densos y consultas rápidas de arista. Elegir según operación y memoria.
- **Práctica:** representa un grafo con ambas estructuras.
- **Independiente:** compara memoria para grafo disperso.
- **Criterios:** representación correcta.
- **Errores:** elegir matriz para grafo muy grande y disperso.
- **Eval:** ¿Cuándo conviene lista de adyacencia?
- **Ref:** Cormen et al.

## Lección 6.4.2 — BFS
- **Oficial:** 6.4.2 — BFS. **Sec:** 2/7. **Propósito:** recorrer grafo por niveles.
- **Resultados:** implementar BFS con cola, encontrar camino más corto en aristas no ponderadas.
- **Desarrollo:** BFS usa queue y conjunto de visitados. Explora por capas. Útil para shortest path en grafos no ponderados.
- **Práctica:** BFS desde nodo origen.
- **Independiente:** encuentra distancia mínima en saltos.
- **Criterios:** no revisita nodos, orden por niveles.
- **Errores:** no marcar visitado al encolar.
- **Eval:** ¿Qué estructura usa BFS?
- **Ref:** Cormen et al.

## Lección 6.4.3 — DFS
- **Oficial:** 6.4.3 — DFS. **Sec:** 3/7. **Propósito:** recorrer en profundidad.
- **Resultados:** implementar DFS recursivo/iterativo.
- **Desarrollo:** DFS explora lo más profundo posible antes de retroceder. Usa stack/recursión. Útil para detección de ciclos, componentes, orden topológico.
- **Práctica:** DFS recursivo.
- **Independiente:** detecta ciclo en grafo dirigido.
- **Criterios:** visitados correctos.
- **Errores:** stack overflow en grafos profundos.
- **Eval:** ¿Qué estructura usa DFS iterativo?
- **Ref:** Cormen et al.

## Lección 6.4.4 — Dijkstra
- **Oficial:** 6.4.4 — Dijkstra. **Sec:** 4/7. **Propósito:** camino más corto con pesos no negativos.
- **Resultados:** aplicar Dijkstra con priority queue.
- **Desarrollo:** mantiene distancias tentativas y expande el nodo de menor distancia. No funciona con pesos negativos. Complejidad depende de implementación.
- **Práctica:** ejecuta Dijkstra en grafo pequeño.
- **Independiente:** explica por qué falla con pesos negativos.
- **Criterios:** distancias correctas.
- **Errores:** usar con pesos negativos.
- **Eval:** ¿Qué restricción tiene Dijkstra?
- **Ref:** Cormen et al.

## Lección 6.4.5 — Bellman-Ford
- **Oficial:** 6.4.5 — Bellman-Ford. **Sec:** 5/7. **Propósito:** caminos más cortos con pesos negativos.
- **Resultados:** aplicar relajación repetida, detectar ciclo negativo.
- **Desarrollo:** relaja todas las aristas V-1 veces. Puede detectar ciclos negativos. Más lento que Dijkstra pero más general.
- **Práctica:** ejecuta Bellman-Ford en grafo con peso negativo.
- **Independiente:** detecta ciclo negativo.
- **Criterios:** distancias correctas, detección de ciclo.
- **Errores:** no hacer V-1 iteraciones.
- **Eval:** ¿Qué ventaja tiene sobre Dijkstra?
- **Ref:** Cormen et al.

## Lección 6.4.6 — Floyd-Warshall
- **Oficial:** 6.4.6 — Floyd-Warshall. **Sec:** 6/7. **Propósito:** caminos más cortos entre todos los pares.
- **Resultados:** entender DP sobre matriz de distancias.
- **Desarrollo:** algoritmo DP O(V^3). Útil para grafos pequeños/medianos donde se necesitan todas las parejas. Maneja pesos negativos sin ciclos negativos.
- **Práctica:** ejecuta en matriz 4x4.
- **Independiente:** identifica ruta reconstruida.
- **Criterios:** matriz final correcta.
- **Errores:** inicialización incorrecta.
- **Eval:** ¿Cuál es su complejidad?
- **Ref:** Cormen et al.

## Lección 6.4.7 — Topological Sort
- **Oficial:** 6.4.7 — Topological Sort. **Sec:** 7/7. **Propósito:** ordenar nodos en DAG.
- **Resultados:** aplicar Kahn o DFS para orden topológico.
- **Desarrollo:** orden topológico es posible solo en DAGs (grafos dirigidos acíclicos). Útil para dependencias, builds, cursos.
- **Práctica:** ordena tareas con dependencias.
- **Independiente:** detecta si no existe orden (ciclo).
- **Criterios:** respeta dependencias.
- **Errores:** aplicar en grafo con ciclo.
- **Eval:** ¿Qué tipo de grafo requiere?
- **Ref:** Cormen et al.