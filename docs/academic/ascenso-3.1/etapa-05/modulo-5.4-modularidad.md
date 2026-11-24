# Etapa 5 · Módulo 5.4 — Modularidad

**Estado:** borrador académico desarrollado (pendiente validación editorial/técnica y ejecución).  
**Alineación:** ASCENSO 3.1, Etapa 5, Módulo 5.4. **Última actualización:** 2026-11-24

## Identificación
- **Módulo:** 5.4 — Modularidad. **Lecciones oficiales:** 9 (5.4.1 a 5.4.9).

## Propósito
Organizar código en módulos, paquetes y dependencias manejables.

---

## Lección 5.4.1 — Módulos
- **Oficial:** 5.4.1 — Módulos. **Sec:** 1/9.
- **Propósito:** dividir código en unidades lógicas.
- **Resultados:** definir módulo, identificar límites y responsabilidades.
- **Desarrollo:** módulo agrupa funcionalidad relacionada con interfaz clara. Reduce complejidad y facilita pruebas. El límite debe tener sentido de dominio, no solo técnico.
- **Práctica:** divide un script grande en 3 módulos.
- **Independiente:** identifica módulos en un proyecto existente.
- **Criterios:** responsabilidad clara, bajo acoplamiento.
- **Errores:** módulos por tipo de archivo sin cohesión.
- **Eval:** ¿Qué hace bueno a un módulo?
- **Ref:** Parnas, D. L. *On the Criteria To Be Used in Decomposing Systems into Modules*. 1972.

## Lección 5.4.2 — Importación y exportación
- **Oficial:** 5.4.2 — Importación y exportación. **Sec:** 2/9.
- **Propósito:** compartir funcionalidad entre módulos.
- **Resultados:** importar/exportar en Java, JS/TS o Python según contexto.
- **Desarrollo:** cada lenguaje tiene su mecanismo: Java `import`, JS `import/export`, Python `import`. Exportar solo lo necesario reduce superficie de acoplamiento.
- **Práctica:** crea módulo que exporte función y otro que la importe.
- **Independiente:** refactoriza imports circulares.
- **Criterios:** imports claros, sin ciclos innecesarios.
- **Errores:** imports circulares; exportar todo.
- **Eval:** ¿Por qué limitar lo exportado?
- **Ref:** MDN. *import*. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import (2026-11-24).

## Lección 5.4.3 — Gestión de dependencias
- **Oficial:** 5.4.3 — Gestión de dependencias. **Sec:** 3/9.
- **Propósito:** declarar y controlar dependencias externas.
- **Resultados:** usar gestor (npm, Maven, pip), entender lockfile.
- **Desarrollo:** dependencias externas se declaran en manifiesto y se fijan con lockfile. Actualizar con criterio; revisar licencias y vulnerabilidades.
- **Práctica:** agrega dependencia y explica lockfile.
- **Independiente:** audita dependencias de un proyecto pequeño.
- **Criterios:** versión fijada, lockfile presente.
- **Errores:** no commitear lockfile; dependencias sin uso.
- **Eval:** ¿Para qué sirve el lockfile?
- **Ref:** npm Docs. https://docs.npmjs.com/ (2026-11-24).

## Lección 5.4.4 — Separación de responsabilidades
- **Oficial:** 5.4.4 — Separación de responsabilidades. **Sec:** 4/9.
- **Propósito:** asignar una responsabilidad clara a cada módulo.
- **Resultados:** aplicar SRP a nivel módulo, evitar mezcla UI/negocio/datos.
- **Desarrollo:** separar presentación, lógica de negocio y acceso a datos facilita cambios y pruebas. No es regla absoluta, pero es guía útil.
- **Práctica:** separa lógica de validación de la UI.
- **Independiente:** refactoriza código mezclado.
- **Criterios:** cada módulo tiene propósito claro.
- **Errores:** capas artificiales sin valor.
- **Eval:** ¿Qué gana la separación de responsabilidades?
- **Ref:** Martin, R. C. *Clean Architecture*. Prentice Hall.

## Lección 5.4.5 — Reutilización de código
- **Oficial:** 5.4.5 — Reutilización de código. **Sec:** 5/9.
- **Propósito:** reutilizar sin duplicar ni acoplar en exceso.
- **Resultados:** identificar oportunidades de reutilización, crear utilidades/módulos.
- **Desarrollo:** reutilizar reduce duplicación, pero abstraer mal crea acoplamiento. Reutilizar cuando la abstracción es estable y clara.
- **Práctica:** extrae función reutilizable de 2 casos similares.
- **Independiente:** evalúa si una abstracción vale la pena.
- **Criterios:** reutilización justificada.
- **Errores:** abstracción prematura.
- **Eval:** ¿Cuándo no reutilizar?
- **Ref:** Hunt & Thomas. *The Pragmatic Programmer*. Addison-Wesley.

## Lección 5.4.6 — Namespaces
- **Oficial:** 5.4.6 — Namespaces. **Sec:** 6/9.
- **Propósito:** evitar colisiones de nombres.
- **Resultados:** entender namespaces/paquetes/módulos según lenguaje.
- **Desarrollo:** namespaces organizan nombres en contextos. Java usa paquetes, C# namespaces, JS módulos. Evitan colisiones y mejoran claridad.
- **Práctica:** resuelve colisión de nombres con namespace/paquete.
- **Independiente:** explica cómo tu lenguaje maneja namespaces.
- **Criterios:** usa namespace correctamente.
- **Errores:** nombres globales ambiguos.
- **Eval:** ¿Qué problema resuelve un namespace?
- **Ref:** Oracle. *Packages*. https://docs.oracle.com/javase/tutorial/java/package/index.html (2026-11-24).

## Lección 5.4.7 — Convenciones de estructura
- **Oficial:** 5.4.7 — Convenciones de estructura. **Sec:** 7/9.
- **Propósito:** organizar proyectos de forma predecible.
- **Resultados:** aplicar estructura estándar por ecosistema.
- **Desarrollo:** cada ecosistema tiene convenciones (Maven/Gradle, src/, tests/, docs/). Seguirlas facilita onboarding y tooling. No inventar estructura sin razón.
- **Práctica:** organiza un proyecto siguiendo convención del lenguaje.
- **Independiente:** compara estructura Maven vs proyecto simple.
- **Criterios:** estructura coherente y reconocible.
- **Errores:** estructura arbitraria.
- **Eval:** ¿Por qué importan las convenciones?
- **Ref:** Maven. *Standard Directory Layout*. https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html (2026-11-24).

## Lección 5.4.8 — Monorepos
- **Oficial:** 5.4.8 — Monorepos. **Sec:** 8/9.
- **Propósito:** entender repositorios con múltiples proyectos/paquetes.
- **Resultados:** identificar ventajas y costos de monorepo.
- **Desarrollo:** monorepo contiene varios proyectos en un repo. Facilita cambios atómicos y compartición, pero requiere tooling, CI y límites claros. No es mejor por defecto.
- **Práctica:** compara monorepo vs multirepo para un caso.
- **Independiente:** diseña estructura monorepo simple.
- **Criterios:** tradeoffs claros.
- **Errores:** monorepo sin tooling; acoplamiento interno excesivo.
- **Eval:** ¿Cuándo conviene un monorepo?
- **Ref:** Google. *Why Google Stores Billions of Lines of Code in a Single Repository*. https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/ (2026-11-24).

## Lección 5.4.9 — Gestión de versiones semántica
- **Oficial:** 5.4.9 — Gestión de versiones semántica. **Sec:** 9/9.
- **Propósito:** comunicar cambios mediante versionado semántico.
- **Resultados:** interpretar MAJOR.MINOR.PATCH, aplicar SemVer.
- **Desarrollo:** SemVer: MAJOR por cambios incompatibles, MINOR por funcionalidad compatible, PATCH por fixes compatibles. Ayuda a consumidores a evaluar riesgo de actualización.
- **Práctica:** asigna versión a 3 escenarios de cambio.
- **Independiente:** crea política de versionado para un proyecto.
- **Criterios:** incrementos correctos.
- **Errores:** romper compatibilidad en PATCH; versiones sin criterio.
- **Eval:** ¿Qué significa incrementar MAJOR?
- **Ref:** SemVer. https://semver.org/lang/es/ (2026-11-24).