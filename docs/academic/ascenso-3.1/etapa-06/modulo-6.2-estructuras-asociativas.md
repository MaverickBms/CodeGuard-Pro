# Etapa 6 · Módulo 6.2 — Estructuras asociativas

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 6, Módulo 6.2. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 6.2 — Estructuras asociativas. **Lecciones oficiales:** 7 (6.2.1 a 6.2.7).

## Lección 6.2.1 — Hash Tables
- **Oficial:** 6.2.1 — Hash Tables. **Sec:** 1/7. **Propósito:** mapear claves a valores con acceso promedio O(1).
- **Resultados:** entender hash, bucket, colisiones, factor de carga.
- **Desarrollo:** hash function transforma clave en índice. Colisiones se manejan por chaining o open addressing. Buen hash y resize mantienen rendimiento.
- **Práctica:** implementa tabla hash simple con chaining.
- **Independiente:** analiza colisiones con una función hash mala.
- **Criterios:** get/put correctos.
- **Errores:** usar claves mutables; mala función hash.
- **Eval:** ¿Qué es una colisión?
- **Ref:** Cormen et al.

## Lección 6.2.2 — HashMap
- **Oficial:** 6.2.2 — HashMap. **Sec:** 2/7. **Propósito:** usar mapa hash en Java.
- **Resultados:** put/get/remove, iterar, entender nulls y orden.
- **Desarrollo:** `HashMap<K,V>` no garantiza orden. Claves deben tener `hashCode/equals` consistentes.
```java
Map<String,Integer> m=new HashMap<>(); m.put("a",1); m.get("a");
```
- **Práctica:** contar frecuencia de palabras.
- **Independiente:** agrupa objetos por clave.
- **Criterios:** uso correcto de equals/hashCode.
- **Errores:** clave mutable.
- **Eval:** ¿HashMap mantiene orden?
- **Ref:** Java Docs. *HashMap*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/HashMap.html (2026-11-24).

## Lección 6.2.3 — HashSet
- **Oficial:** 6.2.3 — HashSet. **Sec:** 3/7. **Propósito:** almacenar elementos únicos.
- **Resultados:** add/contains/remove, deduplicación.
- **Desarrollo:** `HashSet` usa hash table. Útil para membresía y eliminar duplicados.
- **Práctica:** eliminar duplicados de lista.
- **Independiente:** comprobar intersección de dos sets.
- **Criterios:** unicidad correcta.
- **Errores:** asumir orden.
- **Eval:** ¿Qué pasa si agregas duplicado?
- **Ref:** Java Docs. *HashSet*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/HashSet.html (2026-11-24).

## Lección 6.2.4 — TreeMap
- **Oficial:** 6.2.4 — TreeMap. **Sec:** 4/7. **Propósito:** mapa ordenado por clave.
- **Resultados:** usar orden natural/comparador, operaciones log n.
- **Desarrollo:** `TreeMap` mantiene claves ordenadas (árbol rojo-negro). Útil para rangos, mínimos/máximos, navegación.
- **Práctica:** ordenar usuarios por ID con TreeMap.
- **Independiente:** obtener subrango con `subMap`.
- **Criterios:** orden correcto.
- **Errores:** usar TreeMap cuando no se necesita orden.
- **Eval:** ¿Cuál es la complejidad de get en TreeMap?
- **Ref:** Java Docs. *TreeMap*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/TreeMap.html (2026-11-24).

## Lección 6.2.5 — TreeSet
- **Oficial:** 6.2.5 — TreeSet. **Sec:** 5/7. **Propósito:** conjunto ordenado sin duplicados.
- **Resultados:** usar TreeSet, comparadores.
- **Desarrollo:** mantiene elementos ordenados. Útil para rankings, rangos, deduplicación ordenada.
- **Práctica:** mantener top N puntuaciones únicas.
- **Independiente:** usar Comparator personalizado.
- **Criterios:** orden y unicidad.
- **Errores:** comparador inconsistente con equals.
- **Eval:** ¿TreeSet permite duplicados?
- **Ref:** Java Docs. *TreeSet*. https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/TreeSet.html (2026-11-24).

## Lección 6.2.6 — Diccionarios
- **Oficial:** 6.2.6 — Diccionarios. **Sec:** 6/7. **Propósito:** entender concepto general clave-valor.
- **Resultados:** modelar datos como diccionario, elegir implementación.
- **Desarrollo:** diccionario es concepto abstracto; implementaciones: HashMap, TreeMap, LinkedHashMap. Elegir según orden, rendimiento y concurrencia.
- **Práctica:** modela catálogo producto->precio.
- **Independiente:** compara HashMap vs TreeMap para un caso.
- **Criterios:** elección justificada.
- **Errores:** usar lista para búsquedas por clave frecuentes.
- **Eval:** ¿Qué implementación usarías para orden por clave?
- **Ref:** Cormen et al.

## Lección 6.2.7 — Colisiones hash
- **Oficial:** 6.2.7 — Colisiones hash. **Sec:** 7/7. **Propósito:** manejar colisiones y entender impacto.
- **Resultados:** explicar chaining/open addressing, factor de carga.
- **Desarrollo:** dos claves pueden producir mismo índice. Chaining usa listas/árboles en buckets; open addressing busca otro slot. Factor de carga alto degrada rendimiento.
- **Práctica:** simula colisión con hash pequeño.
- **Independiente:** explica por qué hashCode debe ser consistente con equals.
- **Criterios:** entiende impacto en rendimiento.
- **Errores:** asumir O(1) siempre garantizado.
- **Eval:** ¿Qué es factor de carga?
- **Ref:** Cormen et al.