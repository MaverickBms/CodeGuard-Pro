# Etapa 0 — Proyecto integrador ASCENSO-Knowledge-Base

**Versión:** 0.1.0  
**Estado de trabajo:** BASE DE TRABAJO ACTIVA · especificación vigente para ejecutar el proyecto. La implementación y sus entregables siguen pendientes de realización.  
**Fecha:** 2026-11-24  
**Alineación curricular:** ASCENSO 3.1 · Etapa 0 · Proyecto oficial: «Crear ASCENSO-Knowledge-Base, un repositorio para documentar todo el aprendizaje».  
**Propósito:** integrar aprendizaje activo, investigación técnica, herramientas y depuración en un repositorio de conocimiento personal reproducible.

> Este documento desarrolla el proyecto indicado por el currículo. No modifica el nombre ni el objetivo oficial. La implementación descrita es una propuesta didáctica de alcance inicial y no se declara ejecutada.

## 1. Contexto y problema

Durante la formación se acumulan notas, comandos, soluciones, enlaces, ejemplos y errores resueltos en lugares diferentes. Cuando la información no registra contexto, fuente, versión o evidencia, se vuelve difícil reutilizarla, corregirla y compartirla.

El proyecto consiste en construir una base de conocimiento versionada que permita encontrar información, comprender de dónde procede, repetir prácticas y aprender de los errores sin exponer datos privados.

## 2. Resultados de aprendizaje demostrables

Al finalizar, el estudiante podrá:

1. organizar información técnica en unidades pequeñas, enlazadas y recuperables;
2. explicar un concepto con palabras propias y distinguir definición, ejemplo y analogía;
3. registrar una investigación con pregunta, contexto, fuentes, hipótesis y conclusión;
4. utilizar terminal, editor, Markdown y Git para mantener un historial revisable;
5. representar la estructura del conocimiento y el flujo de investigación mediante diagramas;
6. documentar un defecto reproducible, su diagnóstico y una prueba de regresión;
7. revisar y mejorar el repositorio a partir de retroalimentación.

## 3. Requisitos funcionales

La base debe permitir:

- crear una nota con título, objetivo, explicación y fecha de revisión;
- clasificar notas por etapa, módulo, tema y etiquetas;
- registrar fuentes con título, autor/organización, URL, tipo, fecha de consulta y afirmación respaldada;
- distinguir hecho comprobado, observación, interpretación, opinión e hipótesis;
- documentar procedimientos con requisitos, pasos y resultado esperado;
- registrar errores con entorno, pasos de reproducción, resultado esperado/real, hipótesis, pruebas y corrección;
- enlazar notas relacionadas y evitar copias completas de una misma explicación;
- mantener historial de cambios mediante Git;
- permitir que otra persona clone o descargue el repositorio y comprenda cómo utilizarlo.

## 4. Requisitos no funcionales y límites

- **Privacidad:** no almacenar contraseñas, tokens, cookies, claves privadas, datos personales ni volcados de producción.
- **Reproducibilidad:** cada procedimiento indica sistema operativo, shell y versiones cuando sean relevantes.
- **Mantenibilidad:** estructura predecible, nombres consistentes y enlaces relativos dentro del repositorio.
- **Accesibilidad:** encabezados jerárquicos, enlaces descriptivos, tablas solo cuando comparen datos y diagramas con descripción textual.
- **Trazabilidad:** una afirmación técnica relevante enlaza la fuente que la respalda.
- **Portabilidad:** contenido en Markdown y diagramas en formato editable.
- **Alcance:** no se requiere construir una aplicación web, base de datos ni motor de búsqueda. Se puede ampliar en etapas posteriores, pero no es requisito de este proyecto inicial.

## 5. Herramientas y requisitos previos

- VS Code u otro editor de texto.
- Git instalado y configurado con identidad de autor.
- Cuenta GitHub opcional para alojamiento remoto y pull request.
- Navegador moderno.
- diagrams.net o herramienta equivalente que permita conservar el archivo fuente.
- Terminal con Bash/Zsh, PowerShell o CMD. Registrar cuál se utiliza.

No se exige instalar extensiones adicionales para completar el proyecto. Si se instala una, justificar su necesidad y revisar su editor, permisos y procedencia.

## 6. Estructura de referencia

La estructura siguiente es una solución orientativa; puede adaptarse si se mantiene la trazabilidad:

```text
ASCENSO-Knowledge-Base/
├── README.md
├── CONTRIBUTING.md
├── index/
│   ├── etapas.md
│   └── mapa-conceptual.md
├── learning/
│   ├── metodo-estudio.md
│   └── reflexiones/
├── research/
│   ├── plantillas/
│   │   ├── pregunta-tecnica.md
│   │   └── ficha-fuente.md
│   └── casos/
├── tools/
│   ├── terminal/
│   ├── git/
│   └── devtools/
├── debugging/
│   ├── casos/
│   └── plantillas/
├── diagrams/
│   ├── knowledge-map.drawio
│   └── workflow.drawio
└── references/
    └── bibliography.md
```

No es obligatorio crear carpetas vacías: crea cada directorio cuando exista contenido real.

## 7. Plantillas mínimas

### 7.1 Nota de aprendizaje

```markdown
# Título del concepto

- Etapa/módulo:
- Fecha:
- Estado de comprensión: por estudiar / en práctica / puedo explicarlo

## Definición
## Explicación con palabras propias
## Ejemplo
## Límites o contraejemplos
## Preguntas de recuperación
## Fuentes
## Próxima revisión
```

### 7.2 Ficha de investigación

```markdown
# Pregunta investigada

## Objetivo y contexto
## Entorno y versiones
## Resultado esperado y observado
## Fuentes y afirmaciones respaldadas
## Hipótesis y predicciones
## Pruebas y resultados
## Conclusión y limitaciones
## Próximo paso
```

### 7.3 Informe de depuración

```markdown
# Identificador local del caso

## Síntoma
## Entorno reproducible
## Pasos mínimos
## Resultado esperado y real
## Stack trace/logs saneados
## Hipótesis
## Pruebas discriminantes
## Causa respaldada por evidencia
## Corrección
## Pruebas de regresión
## Riesgos y limitaciones
```

Los identificadores de estos documentos son etiquetas locales del proyecto, no UUID de CodeGuard Pro.

## 8. Secuencia de construcción

### Fase A — Preparación y aprendizaje (0.1)

1. Crear el repositorio y README.
2. Definir una convención de nombres y un índice.
3. Crear tres notas breves con explicación propia.
4. Diseñar un calendario de recuperación para revisar esas notas.
5. Añadir una reflexión sobre qué se recuerda y qué debe estudiarse de nuevo.

**Criterio de salida:** otra persona puede localizar una nota y responder una pregunta de recuperación sin abrir el material original.

### Fase B — Investigación trazable (0.2)

1. Registrar tres preguntas técnicas reales o simuladas.
2. Para cada una, anotar entorno, versiones y resultado esperado/real.
3. Consultar documentación primaria y al menos una fuente secundaria pertinente.
4. Clasificar afirmaciones como hecho, observación, interpretación, opinión o hipótesis.
5. Escribir una conclusión que identifique límites y evidencia faltante.

**Criterio de salida:** una persona revisora puede abrir las fuentes y reconstruir el razonamiento sin confiar únicamente en la conclusión del autor.

### Fase C — Herramientas y colaboración (0.3)

1. Editar el repositorio desde la carpeta raíz en VS Code.
2. Registrar los comandos de terminal usados y el shell.
3. Realizar al menos tres commits pequeños y descriptivos.
4. Crear una rama para una mejora y abrir un pull request si se dispone de GitHub.
5. Inspeccionar una página propia o de demostración con DevTools.
6. Crear diagramas editables del mapa de conocimiento y del flujo de investigación.

**Criterio de salida:** el historial permite identificar qué cambió y el diagrama conserva fuente editable.

### Fase D — Depuración y mejora (0.4)

1. Documentar un defecto en un programa de práctica local.
2. Registrar el entorno y pasos para reproducirlo.
3. Formular dos hipótesis y diseñar pruebas que las distingan.
4. Usar breakpoint, stack trace o logs según la naturaleza del defecto.
5. Corregir la causa respaldada por evidencia.
6. Añadir una prueba de regresión o un procedimiento de comprobación.
7. Documentar resultado antes/después.

**Criterio de salida:** el informe diferencia observación, hipótesis y causa; la corrección tiene evidencia y no expone datos sensibles.

### Fase E — Revisión por pares

1. Solicitar a otra persona que use el README sin explicación verbal.
2. Pedir que reproduzca un caso de investigación y un caso de depuración.
3. Registrar dudas, errores y pasos ambiguos.
4. Corregir el material y dejar constancia en Git.
5. Revisar enlaces, ortografía, diagramas y privacidad.

**Criterio de salida:** la persona revisora puede seguir al menos un procedimiento completo con la documentación del repositorio.

## 9. Entregables

1. URL del repositorio remoto o copia local empaquetada.
2. README con propósito, requisitos, estructura y guía de uso.
3. Tres o más notas de aprendizaje.
4. Tres expedientes de investigación.
5. Inventario de herramientas y shell utilizado.
6. Historial de commits y, cuando aplique, pull request.
7. Dos diagramas editables con descripción textual.
8. Un expediente de depuración con prueba de regresión.
9. Bibliografía con fuentes y fecha de consulta.
10. Reflexión final: qué se puede recuperar sin apuntes, qué se transfiere a un problema nuevo y qué sigue pendiente.

## 10. Validación de referencia

El proyecto se considera funcional para esta etapa si se cumplen todos estos puntos:

- [ ] README permite entender propósito y comenzar.
- [ ] La estructura no contiene carpetas sin uso ni duplicaciones innecesarias.
- [ ] Cada nota incluye contexto y fuente cuando hace afirmaciones técnicas.
- [ ] Las tres investigaciones distinguen evidencia y opinión.
- [ ] Los procedimientos indican requisitos y resultado esperado.
- [ ] El historial Git muestra cambios comprensibles.
- [ ] Los diagramas son editables y corresponden a su descripción.
- [ ] El caso de depuración puede reproducirse en el entorno declarado.
- [ ] La corrección se comprueba con una prueba o criterio de regresión.
- [ ] No hay secretos ni datos privados.
- [ ] Otra persona pudo seguir las instrucciones y se registró su retroalimentación.

Una casilla no marcada no se sustituye por una afirmación de que el proyecto está terminado.

## 11. Rúbrica analítica (100 puntos)

| Criterio | 4 — Sólido | 3 — Adecuado | 2 — Parcial | 1 — Insuficiente | Peso |
|---|---|---|---|---|---:|
| Organización y recuperación | Índice, etiquetas y notas facilitan recuperar conocimiento | Organización comprensible | Navegación irregular | No se localiza el contenido | 15 |
| Calidad de notas | Explicaciones precisas, ejemplos y límites | Notas correctas con lagunas menores | Predomina copia o descripción superficial | Contenido confuso o sin atribución | 15 |
| Investigación | Fuentes primarias, versiones y conclusiones calibradas | Fuentes pertinentes con trazabilidad básica | Evidencia incompleta | Opiniones sin contraste | 20 |
| Herramientas y Git | Historial, comandos y diagramas reproducibles | Flujo funcional con pequeñas omisiones | Evidencia incompleta | No se puede revisar el trabajo | 15 |
| Depuración | Reproducción, hipótesis discriminantes y regresión | Diagnóstico razonado con lagunas menores | Corrección sin evidencia suficiente | Cambios al azar o caso irreproducible | 20 |
| Comunicación y privacidad | Tercero reproduce; no hay datos sensibles | Documentación clara y segura | Faltan pasos o controles | Exposición de secretos o instrucciones inutilizables | 15 |

**Umbral formativo sugerido:** 75/100, sin fallo crítico de privacidad y con nivel mínimo 3 en investigación y depuración. Este umbral es una propuesta del proyecto, no un criterio oficial de aprobación de la aplicación.

## 12. Errores frecuentes y recuperación

- **Guardar enlaces sin explicar su utilidad:** añade qué afirmación respalda y en qué versión aplica.
- **Copiar tutoriales completos:** redacta una explicación propia y cita la fuente; no redistribuyas material protegido.
- **Crear demasiadas carpetas al principio:** empieza por las que alojan entregables reales y amplía cuando la navegación lo requiera.
- **Usar commits como copias de seguridad sin revisar:** inspecciona el diff antes de registrar cambios.
- **Documentar un error sin reproducirlo:** vuelve a fijar entorno, entrada y pasos mínimos.
- **Confundir una hipótesis con una causa:** diseña una prueba que permita descartarla.
- **Incluir secretos en ejemplos:** reemplázalos por valores ficticios y revisa el historial antes de publicar.
- **Afirmar que otra persona lo probó sin evidencia:** registra quién revisó, qué pasos siguió y qué resultado observó; si no ocurrió, déjalo pendiente.

## 13. Ampliaciones opcionales

- búsqueda local de notas;
- enlaces entre conceptos y prerrequisitos;
- tarjetas de recuperación y agenda espaciada;
- automatización de revisión de enlaces;
- plantillas para futuras etapas;
- publicación de una versión estática del repositorio.

Estas ampliaciones no son requisitos de aprobación de la etapa 0.

## 14. Registro de ejecución y revisión

| Actividad | Estado en esta entrega |
|---|---|
| Especificación y rúbrica redactadas | Sí |
| Repositorio de estudiante creado | Pendiente |
| Notas y expedientes completados por estudiante | Pendiente |
| Comandos ejecutados y evidencias adjuntas | Pendiente |
| Diagramas generados y abiertos en herramienta | Pendiente |
| Depuración reproducida y prueba de regresión ejecutada | Pendiente |
| Revisión por pares realizada | Pendiente |
| Aprobación editorial | Pendiente |
| Publicación en CodeGuard Pro | No realizada |

**Estado del proyecto:** BASE DE TRABAJO ACTIVA. Esta especificación es la referencia vigente para construir y evaluar el proyecto; todavía no demuestra que el repositorio haya sido creado ni ejecutado.

## 15. Referencias de apoyo

- Git Documentation: https://git-scm.com/doc — documentación oficial de Git para historial y colaboración local.
- GitHub Docs: https://docs.github.com/en/repositories — documentación oficial sobre repositorios y colaboración.
- Markdown Guide: https://www.markdownguide.org/ — guía de sintaxis Markdown; los renderizadores pueden implementar variantes.
- diagrams.net Documentation: https://www.drawio.com/doc/ — documentación del formato y herramienta de diagramación.
- Stack Overflow Help, Minimal Reproducible Example: https://stackoverflow.com/help/minimal-reproducible-example — criterios para elaborar ejemplos reproducibles.

**Fecha de consulta de referencias:** 2026-11-24. Revisar vigencia y alcance antes de aprobar o publicar.
