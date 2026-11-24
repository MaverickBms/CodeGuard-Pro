# Etapa 4 · Módulo 4.2 — Relaciones

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 4, Módulo 4.2. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 4.2 — Relaciones. **Lecciones oficiales:** 5 (4.2.1 a 4.2.5).

## Propósito
Modelar relaciones entre clases: asociación, agregación, composición, dependencia y multiplicidad.

---

## Lección 4.2.1 — Asociación
- **Oficial:** 4.2.1 — Asociación. **Sec:** 1/5.
- **Propósito:** representar que dos clases se conocen o colaboran.
- **Resultados:** identificar asociación, implementarla con referencias.
- **Desarrollo:** asociación es una relación estructural entre clases. Puede ser unidireccional o bidireccional. Ejemplo: `Profesor` asociado a `Curso`.
```java
class Curso { Profesor profesor; }
class Profesor { String nombre; }
```
- **Práctica:** modela Cliente-Pedido como asociación.
- **Independiente:** dibuja asociación bidireccional y explica riesgos.
- **Criterios:** dirección clara, referencia correcta.
- **Errores:** bidireccionalidad innecesaria; acoplamiento alto.
- **Eval:** ¿Qué indica una asociación?
- **Ref:** UML 2.5 Specification. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.2.2 — Agregación
- **Oficial:** 4.2.2 — Agregación. **Sec:** 2/5.
- **Propósito:** modelar relación todo-parte débil.
- **Resultados:** distinguir agregación de asociación/composición.
- **Desarrollo:** agregación es una asociación "tiene-un" donde la parte puede existir independientemente del todo. Ejemplo: Equipo tiene Jugadores; el jugador puede existir sin el equipo.
```java
class Equipo { List<Jugador> jugadores; }
```
- **Práctica:** modela Departamento-Empleado como agregación.
- **Independiente:** justifica por qué no es composición.
- **Criterios:** ciclo de vida independiente.
- **Errores:** confundir con composición.
- **Eval:** ¿La parte muere con el todo en agregación?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.2.3 — Composición
- **Oficial:** 4.2.3 — Composición. **Sec:** 3/5.
- **Propósito:** modelar relación todo-parte fuerte.
- **Resultados:** implementar composición, entender propiedad del ciclo de vida.
- **Desarrollo:** en composición, la parte pertenece exclusivamente al todo; si el todo se destruye, la parte también. Ejemplo: Casa-Habitación.
```java
class Casa {
    private List<Habitacion> habitaciones = new ArrayList<>();
    Casa() { habitaciones.add(new Habitacion("Sala")); }
}
```
- **Práctica:** modela Pedido-LineaPedido como composición.
- **Independiente:** compara agregación y composición con 2 ejemplos.
- **Criterios:** propiedad clara, ciclo de vida dependiente.
- **Errores:** exponer partes mutables sin control.
- **Eval:** ¿Qué diferencia a composición de agregación?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.2.4 — Dependencia
- **Oficial:** 4.2.4 — Dependencia. **Sec:** 4/5.
- **Propósito:** identificar uso temporal entre clases.
- **Resultados:** reconocer dependencias en parámetros, retornos y variables locales.
- **Desarrollo:** dependencia es una relación de uso: una clase usa otra sin mantenerla como campo. Ejemplo: método que recibe `PdfExporter` como parámetro.
```java
class ReporteService {
    void generar(PdfExporter exporter) { exporter.export(); }
}
```
- **Práctica:** identifica dependencias en un código dado.
- **Independiente:** reduce dependencias innecesarias en un diseño.
- **Criterios:** distingue dependencia de asociación.
- **Errores:** confundir dependencia con campo permanente.
- **Eval:** ¿Cuándo una relación es dependencia?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).

## Lección 4.2.5 — Multiplicidad
- **Oficial:** 4.2.5 — Multiplicidad. **Sec:** 5/5.
- **Propósito:** expresar cuántos objetos participan en una relación.
- **Resultados:** interpretar 1, 0..1, 1..*, 0..*, N:M.
- **Desarrollo:** multiplicidad define cardinalidad: un Cliente puede tener muchos Pedidos (1..*), un Pedido pertenece a un Cliente (1). Se implementa con objetos, listas, sets o tablas intermedias según el caso.
- **Práctica:** modela 1:N y N:M con clases Java.
- **Independiente:** diseña modelo de Curso-Estudiante (N:M).
- **Criterios:** cardinalidad correcta, implementación coherente.
- **Errores:** usar lista cuando debe ser único; ignorar opcionalidad.
- **Eval:** ¿Qué significa 0..*?
- **Ref:** OMG UML. https://www.omg.org/spec/UML/ (2026-11-24).