# Etapa 4 · Módulo 4.3 — Conceptos de diseño

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 4, Módulo 4.3. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 4.3 — Conceptos de diseño. **Lecciones oficiales:** 5 (4.3.1 a 4.3.5).

## Propósito
Aplicar principios básicos de diseño orientado a objetos para producir código mantenible.

---

## Lección 4.3.1 — Cohesión
- **Oficial:** 4.3.1 — Cohesión. **Sec:** 1/5.
- **Propósito:** diseñar clases con responsabilidad enfocada.
- **Resultados:** identificar alta/baja cohesión, refactorizar clases Dios.
- **Desarrollo:** cohesión mide cuánto se relacionan las responsabilidades de un módulo. Alta cohesión: la clase hace una cosa bien. Baja cohesión: hace muchas cosas no relacionadas. Favorece mantenimiento y pruebas.
- **Ejemplo:** `ReporteService` que genera, envía email, guarda en DB y formatea PDF tiene baja cohesión; separar responsabilidades mejora diseño.
- **Práctica:** refactoriza una clase con 4 responsabilidades en 4 clases.
- **Independiente:** evalúa cohesión de un módulo de tu proyecto.
- **Criterios:** responsabilidades claras, justificación.
- **Errores:** dividir en exceso sin criterio.
- **Eval:** ¿Qué es alta cohesión?
- **Ref:** Martin, R. C. *Clean Architecture*. Prentice Hall.

## Lección 4.3.2 — Acoplamiento
- **Oficial:** 4.3.2 — Acoplamiento. **Sec:** 2/5.
- **Propósito:** reducir dependencias innecesarias entre módulos.
- **Resultados:** identificar acoplamiento fuerte/débil, usar interfaces para desacoplar.
- **Desarrollo:** acoplamiento mide cuánto depende un módulo de otro. Acoplamiento fuerte dificulta cambios y pruebas. Se reduce con interfaces, inyección de dependencias y límites claros.
```java
class Servicio { private Repositorio repo; Servicio(Repositorio repo){this.repo=repo;} }
```
- **Práctica:** reemplaza dependencia concreta por interfaz.
- **Independiente:** identifica acoplamiento fuerte en un diseño y propone mejora.
- **Criterios:** dependencia por abstracción, menor impacto de cambio.
- **Errores:** acoplamiento oculto por estáticos/globales.
- **Eval:** ¿Por qué el acoplamiento fuerte es problemático?
- **Ref:** Martin, R. C. *Clean Code*. Prentice Hall.

## Lección 4.3.3 — SOLID
- **Oficial:** 4.3.3 — SOLID. **Sec:** 3/5.
- **Propósito:** aplicar los cinco principios SOLID a nivel introductorio.
- **Resultados:** explicar SRP, OCP, LSP, ISP, DIP con ejemplos.
- **Desarrollo:** SRP: una razón de cambio. OCP: abierto a extensión, cerrado a modificación. LSP: subtipos sustituibles. ISP: interfaces pequeñas. DIP: depender de abstracciones. Son guías, no dogmas; aplicarlos con criterio.
- **Práctica:** identifica qué principio viola un código dado.
- **Independiente:** refactoriza un ejemplo aplicando SRP y DIP.
- **Criterios:** identifica principios correctamente, aplica sin sobreingeniería.
- **Errores:** aplicar SOLID dogmáticamente; crear demasiadas abstracciones.
- **Eval:** ¿Qué significa SRP?
- **Ref:** Martin, R. C. *Agile Software Development*. Prentice Hall.

## Lección 4.3.4 — DRY
- **Oficial:** 4.3.4 — DRY. **Sec:** 4/5.
- **Propósito:** evitar duplicación de conocimiento.
- **Resultados:** identificar duplicación real vs coincidencia accidental.
- **Desarrollo:** DRY (Don't Repeat Yourself) busca una única fuente autoritativa para cada conocimiento. Duplicar lógica causa inconsistencias. Pero no toda similitud es duplicación: dos piezas pueden parecer iguales hoy y divergir mañana.
- **Práctica:** extrae lógica duplicada en un método reutilizable.
- **Independiente:** encuentra un caso donde duplicar sea mejor que abstraer prematuramente.
- **Criterios:** elimina duplicación real, evita abstracción forzada.
- **Errores:** abstraer demasiado pronto; confundir DRY con “nunca copiar”.
- **Eval:** ¿Cuándo la duplicación puede ser aceptable?
- **Ref:** Hunt, A., & Thomas, D. *The Pragmatic Programmer*. Addison-Wesley.

## Lección 4.3.5 — KISS
- **Oficial:** 4.3.5 — KISS. **Sec:** 5/5.
- **Propósito:** preferir soluciones simples y comprensibles.
- **Resultados:** comparar soluciones compleja vs simple, justificar simplicidad.
- **Desarrollo:** KISS (Keep It Simple, Stupid) promueve evitar complejidad innecesaria. Simple no significa incompleto: significa resolver el problema actual con claridad. La complejidad debe justificarse por requisitos reales.
- **Práctica:** simplifica un método con condiciones anidadas innecesarias.
- **Independiente:** refactoriza código sobreingenierizado.
- **Criterios:** solución más clara, mismo comportamiento.
- **Errores:** simplificar eliminando casos necesarios.
- **Eval:** ¿Simple es lo mismo que fácil?
- **Ref:** Martin, R. C. *Clean Code*. Prentice Hall.