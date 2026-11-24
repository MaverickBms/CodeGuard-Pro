# Etapa 18 — Arquitectura, diseño y planeación de software

**Prioridad:** P1 · Obligatoria  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA  
**Objetivo oficial:** aprender a planear y diseñar sistemas antes de comenzar a programar.  
**Proyecto oficial:** recibir un problema empresarial, analizarlo, documentarlo, modelarlo, diseñar su arquitectura y elaborar un plan de trabajo antes de escribir código.

## Resultados de aprendizaje
Convertir necesidades en requisitos verificables; organizar trabajo ágil; documentar decisiones; modelar estructura y comportamiento; aplicar principios y patrones con criterio; comparar arquitecturas; razonar sobre sistemas distribuidos; modelar dominios; y trabajar mediante especificaciones proporcionales al riesgo.

## 18.1 — Análisis de requerimientos
Los requisitos funcionales describen capacidades o comportamientos. Los no funcionales expresan cualidades, restricciones o condiciones medibles, por ejemplo latencia, disponibilidad, seguridad, accesibilidad o mantenibilidad. Evita requisitos vagos como “rápido”, “seguro” o “fácil”: define escenario, métrica, umbral y contexto.

Historias de usuario expresan necesidad desde una perspectiva; casos de uso describen actores, condiciones y flujos. Criterios de aceptación hacen verificable el resultado. Reglas de negocio definen políticas del dominio; restricciones limitan diseño o implementación. Stakeholders son personas o grupos afectados o con interés legítimo. Define alcance, exclusiones, supuestos, dependencias y riesgos.

**Ejercicio:** transforma una petición ambigua de inventario en requisitos funcionales y no funcionales, historias, casos de uso y criterios comprobables.

## 18.2 — Metodologías ágiles
El Manifiesto Ágil expresa valores y principios; no prescribe una herramienta ni elimina planificación. Scrum organiza trabajo mediante responsabilidades, eventos y artefactos definidos. Kanban visualiza flujo, limita trabajo en progreso (WIP) y busca mejorar entrega continua.

Comprende Product Backlog, Sprint Backlog, Planning, Daily Scrum, Review, Retrospective y Definition of Done. Story Points son una técnica relativa de estimación, no horas universales ni medida individual de productividad. WIP limita tareas simultáneas y ayuda a detectar cuellos de botella.

**Ejercicio:** crea un backlog priorizado, divide una historia en tareas, define DoD y simula un flujo Kanban con límite WIP.

## 18.3 — Documentación
README explica propósito, requisitos, instalación, configuración, ejecución, pruebas y limitaciones. La especificación de requisitos conserva alcance y trazabilidad. Documentación técnica explica arquitectura y operación; funcional describe capacidades y reglas. API Documentation debe reflejar el contrato real. ADR registra una decisión, contexto, opciones, decisión y consecuencias. Changelog documenta cambios relevantes.

Incluye manual de instalación, usuario, pruebas y despliegue cuando el producto lo requiera. La documentación debe actualizarse junto al código y diferenciar lo implementado, probado y planificado.

**Ejercicio:** escribe un ADR que compare monolito modular y microservicios para una aplicación pequeña; registra consecuencias y condiciones que podrían hacer revisar la decisión.

## 18.4 — Diagramas
Usa diagramas de flujo para procesos; UML para estructura y comportamiento; clases para tipos y relaciones; secuencia para mensajes en el tiempo; actividades para flujos; componentes para módulos y dependencias; despliegue para nodos y artefactos; ER para datos. C4 modela contexto, contenedores, componentes y código con niveles distintos de detalle.

Un diagrama debe responder una pregunta y declarar límites. Evita diagramas ornamentales sin relación con decisiones. Mantén coherencia entre diagramas y sistema real.

**Ejercicio:** modela el sistema de ventas con contexto C4, contenedores, secuencia de venta y ER.

## 18.5 — Principios de diseño
- **SOLID:** cinco principios para organizar responsabilidades, extensibilidad y dependencias; no son reglas mecánicas.
- **DRY:** evita duplicación de conocimiento que debería tener una única fuente; no abstraigas coincidencias accidentales.
- **KISS:** favorece soluciones simples que satisfagan requisitos.
- **YAGNI:** no construyas capacidades especulativas sin necesidad demostrable.
- **Separation of Concerns:** separa aspectos con motivos de cambio distintos.
- **High Cohesion / Low Coupling:** agrupa responsabilidades relacionadas y reduce dependencias innecesarias.
- **Dependency Inversion:** políticas de alto nivel no deben depender directamente de detalles; ambos deben depender de abstracciones apropiadas.

Evalúa coste de abstracción, testabilidad y complejidad. Una interfaz para cada clase no garantiza buen diseño.

## 18.6 — Patrones GoF
Los patrones describen soluciones recurrentes en contextos específicos; no son recetas obligatorias.

**Creacionales:** Factory, Abstract Factory, Builder, Singleton y Prototype. Estudia qué problema de creación resuelven, cómo afectan acoplamiento y pruebas y qué alternativas ofrece el lenguaje/framework.

**Estructurales:** Adapter, Decorator, Facade, Proxy, Composite, Bridge y Flyweight. Compara adaptación de interfaces, composición, acceso indirecto, simplificación y uso compartido.

**Comportamiento:** Strategy, Observer, Command, State, Iterator, Mediator, Template Method y Chain of Responsibility. Identifica cómo distribuyen decisiones, mensajes y responsabilidades.

**Ejercicio:** elige tres patrones para escenarios distintos, implementa ejemplos pequeños y documenta cuándo sería mejor no utilizarlos.

## 18.7 — Arquitecturas
- Monolítica: una unidad principal de despliegue; puede ser modular internamente.
- Monolito modular: módulos con límites y dependencias controlados en un despliegue coordinado.
- Layered: separa presentación, aplicación, dominio y persistencia según diseño.
- MVC: separa modelo, vista y controlador en contextos apropiados.
- Clean Architecture: centra reglas de negocio y controla dirección de dependencias.
- Hexagonal: organiza puertos y adaptadores alrededor del núcleo.
- Onion: capas concéntricas con dominio en el centro.
- Event-Driven: componentes reaccionan a eventos; exige contratos, idempotencia y observabilidad.
- Microservices: servicios autónomos con despliegue y datos/contratos distribuidos; añade complejidad operacional.

No confundas patrones de arquitectura con frameworks. Selecciona según equipo, escala, dominio, operación y requisitos; un monolito bien modularizado puede ser la decisión más adecuada.

## 18.8 — Diseño de sistemas
Razonar sobre scalability, availability, reliability, consistency y fault tolerance exige escenarios y métricas. CAP se refiere al compromiso bajo particiones en sistemas distribuidos; no es una clasificación simplista de bases de datos. Load balancing distribuye carga; caching reduce trabajo a cambio de invalidación y frescura; message queues desacoplan procesos; distributed systems deben gestionar fallos parciales, latencia y duplicados. API Gateway concentra políticas de entrada; service discovery permite localizar servicios.

**Ejercicio:** diseña un servicio de pedidos para carga creciente. Identifica cuellos de botella, puntos únicos de fallo, estrategia de caché, cola y comportamiento ante indisponibilidad de un servicio.

## 18.9 — Modelado de dominios
Domain-Driven Design (DDD) centra el diseño en el dominio y su lenguaje. Entity posee identidad; Value Object se define por sus valores; Aggregate agrupa invariantes y establece una raíz; Repository abstrae persistencia de agregados; Bounded Context define límites donde un modelo y lenguaje tienen significado coherente; Ubiquitous Language alinea vocabulario entre especialistas y equipo técnico.

No conviertas cada tabla en agregado ni cada entidad en microservicio. Modela invariantes, transacciones y límites del contexto antes de decidir estructura de código.

## Ampliación metodológica — SDD (Spec-Driven Development)
El desarrollo guiado por especificaciones comienza por definir problema, usuarios, alcance y reglas. Escribe requisitos funcionales/no funcionales, historias y criterios verificables; modela datos, módulos, responsabilidades, interfaces y decisiones; divide la especificación en tareas y dependencias; implementa respetándola y registra cambios; crea pruebas para criterios de aceptación; mantiene trazabilidad requisito-código-prueba.

La especificación debe ser proporcional al tamaño y riesgo: breve para una práctica pequeña, más rigurosa para un sistema empresarial. SDD no significa producir documentos extensos antes de cada ejercicio ni reemplaza el juicio de ingeniería.

## Proyecto oficial — Diseño de un sistema empresarial
Antes de programar, entrega:
1. Problema, usuarios, stakeholders y alcance.
2. Requisitos funcionales y no funcionales verificables.
3. Historias, casos de uso y criterios de aceptación.
4. Reglas de negocio, restricciones y riesgos.
5. Modelo de dominio y lenguaje ubicuo.
6. Modelo ER y diagramas UML/C4 pertinentes.
7. Comparación de al menos dos arquitecturas con ADR.
8. Patrones justificados por necesidad concreta.
9. Backlog priorizado, tareas, dependencias y Definition of Done.
10. Plan de pruebas vinculado a requisitos.
11. Especificación técnica y plan de implementación.
12. Revisión de consistencia entre documentos.

### Rúbrica (100 puntos)
| Criterio | Puntos |
|---|---:|
| Requisitos, alcance y criterios | 15 |
| Método ágil y planificación | 10 |
| Documentación y ADR | 10 |
| Diagramas y modelado | 15 |
| Principios y patrones | 15 |
| Selección de arquitectura | 15 |
| Diseño de sistemas y resiliencia | 10 |
| DDD y SDD | 10 |

Criterio orientativo: 80/100 y trazabilidad entre problema, requisitos, diseño y pruebas.

## Autoevaluación
1. ¿Cómo conviertes un requisito no funcional en verificable?
2. Diferencia historia de usuario y caso de uso.
3. ¿Qué limita WIP?
4. ¿Qué debe contener un ADR?
5. ¿Qué pregunta responde un diagrama de secuencia?
6. ¿Por qué DRY no significa eliminar toda repetición?
7. ¿Cuándo un monolito modular es preferible a microservicios?
8. ¿Qué problema resuelve un Aggregate?
9. ¿Qué significa bounded context?
10. ¿Cómo se relacionan especificación, implementación y pruebas en SDD?

## Recursos audiovisuales
No se incluyen videos aprobados. Se incorporarán únicamente con audio hablado en español y correspondencia directa con el subtema: requisitos, Scrum/Kanban, UML/C4, patrones, arquitectura o DDD. No se usarán charlas generales como sustituto de explicación técnica.

## Referencias oficiales y técnicas
- Agile Manifesto: https://agilemanifesto.org/
- Scrum Guide: https://scrumguides.org/
- Kanban Guide: https://kanbanguides.org/
- OMG UML: https://www.omg.org/spec/UML/
- C4 Model: https://c4model.com/
- ISO Systems and software engineering standards: https://www.iso.org/committee/45086.html
- Martin Fowler — Architecture: https://martinfowler.com/architecture/
- Microsoft Architecture Center: https://learn.microsoft.com/en-us/azure/architecture/
- Domain-Driven Design Community: https://www.domainlanguage.com/
- ADR GitHub: https://adr.github.io/

**Consulta documental:** 2026-11-19. **Verificación práctica:** proyecto de diseño no implementado ni validado en esta sesión. **Estado:** base de trabajo activa; sin aprobación ni publicación.
