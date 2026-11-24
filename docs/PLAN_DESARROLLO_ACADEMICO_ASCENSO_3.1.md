# Plan maestro de desarrollo académico — ASCENSO 3.1

**Proyecto:** CodeGuard Pro  
**Fuente curricular:** `PROYECTO_ASCENSO_Roadmap_Maestro_Consolidado_3_1_2026.docx`  
**Versión estructural:** ASCENSO 3.1  
**Rama objetivo:** `release/1.0.0-final`  
**Estado de este documento:** plan de producción y control editorial; no aprueba ni publica lecciones.

## 1. Propósito

Convertir el inventario ASCENSO 3.1 en una formación progresiva, rigurosa, práctica y evaluable. El trabajo debe completar los contenidos de las 1.946 lecciones nominales sin alterar la estructura oficial ni confundir títulos con material didáctico.

La producción se realizará por lotes pequeños y coherentes, con revisión técnica, pedagógica, práctica, editorial y de fuentes. Ningún lote se considerará terminado por el mero hecho de que exista JSON válido o que el importador lo acepte.

## 2. Estructura inmutable de referencia

La línea base documentada es:

- 33 etapas (0–32).
- 212 módulos.
- 1.946 lecciones nominales.
- 7 prerrequisitos explícitos.
- Prioridades: 24 etapas P1, 6 P2 y 3 P3.
- La etapa 25 no tiene objetivo formal en el documento maestro. La propuesta descrita en el inventario es una propuesta editorial, no una decisión aprobada.

Estos valores deben volver a comprobarse contra `apps/roadmaps/data/ascenso_3_1.json` y la base de datos antes de cada migración o importación masiva. No se deben renumerar, fusionar, eliminar ni inventar módulos o lecciones.

## 3. Estado de partida documentado

Según `docs/CONTENIDO_ACADEMICO.md` y `docs/ROADMAP_ASCENSO_INVENTARIO.md`:

- El módulo 0.1 «Aprender a aprender» contiene 8 lecciones con cuerpo estructurado en `apps/roadmaps/data/contenido_academico_0_1.json`.
- Las 8 están en borrador editorial; 0 aprobadas y 0 publicadas.
- El lote contiene ejemplos, ejercicios deterministas, referencias y videos con metadatos técnicos verificados.
- Los 8 videos tienen pendiente la revisión pedagógica completa.
- Quedan 1.938 lecciones sin cuerpo de contenido en el inventario reportado.
- Los módulos 0.2 «Investigación técnica», 0.3 «Herramientas» y 0.4 «Depuración» son los siguientes lotes naturales de la etapa 0.

Estas cifras son una línea base histórica documentada (21 de noviembre de 2026), no una lectura en tiempo real de la base de datos. Deben actualizarse con una consulta de cobertura antes de declarar avances nuevos.

## 4. Orden de producción

### Lote inicial: completar la etapa 0

1. Revisar y mejorar las 8 lecciones del módulo 0.1 sin sobrescribir su historial ni cambiar su estado editorial sin revisión.
2. Desarrollar las 7 lecciones del módulo 0.2 «Investigación técnica».
3. Desarrollar las 8 lecciones del módulo 0.3 «Herramientas».
4. Desarrollar las 7 lecciones del módulo 0.4 «Depuración».
5. Revisar el proyecto integrador de la etapa 0: ASCENSO-Knowledge-Base.

La etapa 0 contiene 30 lecciones nominales. El resultado esperado es un primer bloque coherente de fundamentos para estudiar, investigar, trabajar con herramientas y depurar problemas.

### Siguiente orden: etapas obligatorias P1

Después de cerrar editorialmente la etapa 0, producir las etapas P1 en orden curricular, respetando las dependencias explícitas. Los módulos P2 y P3 se desarrollarán después o en paralelo solo cuando no se creen lagunas de prerrequisitos y exista capacidad de revisión suficiente.

El orden de producción no cambia el orden oficial ni desbloquea etapas para el estudiante.

## 5. Contrato mínimo de cada lección

Cada lección debe adaptarse a su disciplina y nivel, pero cubrir los elementos aplicables:

1. Identificación: etapa, módulo, título oficial y nivel.
2. Objetivos de aprendizaje observables y evaluables.
3. Conocimientos previos y criterios de entrada.
4. Introducción que explique relevancia y contexto.
5. Desarrollo conceptual y técnico, con precisión terminológica.
6. Explicación accesible sin sacrificar exactitud.
7. Conceptos fundamentales y relaciones entre ellos.
8. Ejemplos resueltos y demostraciones; código ejecutable cuando corresponda.
9. Aplicaciones prácticas y escenarios reales.
10. Errores frecuentes, límites y malas prácticas.
11. Ejercicios graduados con instrucciones y criterios de corrección.
12. Laboratorio o práctica guiada cuando el tema lo requiera.
13. Reto integrador que exija transferencia, no repetición mecánica.
14. Evaluación alineada con los objetivos y criterios explícitos.
15. Soluciones o guías de solución para autoestudio, separadas de la vista inicial del estudiante cuando corresponda.
16. Referencias primarias y secundarias, con versión/fecha y localizador cuando sea posible.
17. Recursos audiovisuales opcionales, solo si se verifica idioma, pertinencia y disponibilidad.

No se debe forzar un bloque de código en una lección conceptual ni añadir un laboratorio artificial cuando no aporte aprendizaje. La profundidad debe corresponder al nivel básico, intermedio o avanzado.

## 6. Estándar de evaluación

- Los objetivos deben utilizar verbos observables: explicar, comparar, configurar, implementar, diagnosticar, justificar, evaluar, diseñar, etc.
- Cada ejercicio debe medir uno o varios objetivos concretos.
- Los evaluadores automáticos deben ser adecuados al tipo de respuesta. Una búsqueda de palabras clave no debe presentarse como evaluación semántica ni como prueba suficiente de dominio.
- Para respuestas abiertas, usar rúbricas con criterios explícitos y revisión humana cuando el sistema no pueda evaluar con fiabilidad.
- Incluir retroalimentación útil para respuestas correctas e incorrectas.
- Separar práctica formativa, evaluación sumativa y criterio de finalización.
- No permitir que una respuesta trivial o un fragmento de texto complete una lección cuyo objetivo exige razonamiento, código o ejecución.

## 7. Fuentes, licencias y vigencia

Prioridad de fuentes:

1. Documentación oficial del lenguaje, plataforma, estándar o herramienta.
2. Estándares y especificaciones originales (RFC, W3C, ECMA, IEEE, NIST, OWASP, MITRE, etc.).
3. Artículos científicos y libros académicos pertinentes.
4. Material docente de instituciones o especialistas reconocidos, como complemento.

Por cada fuente registrar título, autor/editor, URL canónica HTTPS, edición o fecha de publicación, fecha de consulta, localizador y nota de uso. No copiar documentación protegida: redactar explicaciones originales y citar la fuente.

Distinguir explícitamente:
- fuente identificada;
- URL y metadatos comprobados;
- contenido consultado;
- licencia/uso revisado;
- pertinencia técnica revisada.

La existencia de una URL no equivale a verificación de su contenido ni a autorización de reproducción.

## 8. Videos en español

Un video es opcional, nunca un requisito para rellenar una ficha.

Para incorporarlo:
- confirmar que el video existe y está disponible;
- comprobar título, canal/autor, duración y URL;
- comprobar audio original o subtítulos en español;
- revisar el contenido completo o los segmentos relevantes;
- documentar qué objetivo refuerza y qué partes del tema cubre;
- registrar fecha de verificación y cualquier limitación.

No usar un video solo porque contiene palabras similares al título de la lección. Si no se encuentra uno directamente pertinente y de calidad suficiente, dejar el campo vacío y ofrecer documentación escrita.

Los metadatos técnicos y la revisión pedagógica son estados distintos. No marcar un video pedagógicamente aprobado por el mero hecho de tener título, enlace y subtítulos.

## 9. Puertas de calidad y estados editoriales

Mantener separados estos estados:

- **Pendiente:** no existe cuerpo didáctico.
- **En desarrollo:** redacción en curso.
- **Borrador:** contenido estructurado importable, aún sin revisión completa.
- **En revisión:** versión congelada enviada a revisión.
- **Aprobado:** revisión técnica, pedagógica y editorial registrada.
- **Publicado:** versión aprobada activada mediante el flujo editorial.

Puertas obligatorias antes de aprobar:

- Fidelidad al título y alcance curricular oficial.
- Exactitud técnica y compatibilidad con versiones indicadas.
- Secuencia pedagógica y prerrequisitos.
- Objetivos, actividades y evaluación alineados.
- Ejemplos y prácticas reproducibles.
- Soluciones verificadas.
- Referencias pertinentes y trazables.
- Licencias y atribuciones revisadas.
- Lenguaje claro, inclusivo y consistente.
- Revisión de duplicidad y solapamiento con otras lecciones.
- Ausencia de enlaces inventados, citas falsas o videos no revisados.

La importación puede crear borradores, pero no debe aprobar ni publicar automáticamente.

## 10. Seguridad y ética en contenidos técnicos

Para ciberseguridad y administración:
- usar laboratorios locales, CTF o entornos expresamente autorizados;
- definir alcance, permisos, objetivos y limpieza del laboratorio;
- priorizar mitigación, detección y comprensión defensiva;
- no dirigir prácticas contra sistemas reales sin autorización;
- separar demostración controlada de instrucciones operativas peligrosas;
- incorporar privacidad, legalidad, divulgación responsable y gestión de datos.

## 11. Control de duplicidades y progresión

Las 333 coincidencias de títulos registradas en el inventario no se deben eliminar automáticamente. Algunas repeticiones pueden representar profundización o aplicación en otra disciplina.

Antes de redactar una lección con título repetido:
- comparar etapa, módulo, nivel y objetivo;
- decidir si es repaso, profundización o aplicación;
- reutilizar conceptos sin duplicar texto;
- explicitar qué conocimiento previo se presupone;
- evitar que el estudiante repita una lección idéntica sin valor añadido.

## 12. Entregables por lote

Cada lote debe incluir:

- archivo de contenido versionado;
- reporte de validación estructural;
- matriz objetivo → explicación → práctica → evaluación;
- referencias y estado de verificación;
- lista de videos revisados o motivo de ausencia;
- revisión de duplicidades;
- informe de cambios y pendientes;
- conteo de lecciones por estado editorial.

Los lotes deben ser pequeños, revisables e idempotentes. No reemplazar el archivo del módulo 0.1 con una carga masiva ni cambiar su historial.

## 13. Primer backlog

| Orden | Etapa/módulo | Lecciones nominales | Estado de partida |
|---|---|---:|---|
| 1 | 0.1 Aprender a aprender | 8 | Borrador existente; requiere revisión |
| 2 | 0.2 Investigación técnica | 7 | Pendiente |
| 3 | 0.3 Herramientas | 8 | Pendiente |
| 4 | 0.4 Depuración | 7 | Pendiente |
| 5 | Proyecto integrador etapa 0 | 1 proyecto | Requiere diseño de entregables y rúbrica |

### Contenido previsto de los módulos iniciales

**0.2 — Investigación técnica**
- Buscar documentación.
- Buscar soluciones a errores.
- Leer Stack Overflow.
- Consultar GitHub.
- Investigar repositorios.
- Diferenciar información verificada de opiniones.
- Formular preguntas técnicas.

**0.3 — Herramientas**
- Visual Studio Code.
- Terminal.
- Git.
- GitHub.
- Navegador y DevTools.
- Markdown.
- Draw.io.
- Herramientas de diagramación.

**0.4 — Depuración**
- Debugging.
- Breakpoints.
- Stack traces.
- Logs.
- Hipótesis.
- Reproducción de errores.
- Análisis de causas.

## 14. Restricciones editoriales vigentes

- No modificar el documento maestro DOCX ni sustituirlo por una reconstrucción.
- No inventar el objetivo oficial de la etapa 25. Mantener la propuesta en revisión hasta que exista aprobación explícita.
- No cambiar los 33/212/1.946 ni los 7 prerrequisitos sin evidencia y decisión documentada.
- No presentar títulos, descripciones breves, enlaces o videos como lecciones completas.
- No marcar como aprobado ni publicado un lote solo porque pase el importador.
- No cambiar estados de producción sin registrar evidencia de revisión.
- Preservar los datos del estudiante y separar contenido editorial de progreso personal.

## 15. Próxima acción

La siguiente tarea de producción es auditar individualmente las ocho lecciones existentes de 0.1 y desarrollar el lote 0.2 completo con siete lecciones. Después se valida el lote en modo dry-run y contra el esquema del importador, se corrigen los defectos y se incorpora como borrador editorial sin aprobarlo ni publicarlo automáticamente.
