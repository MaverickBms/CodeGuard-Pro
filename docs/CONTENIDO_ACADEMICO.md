# Contenido académico inicial y flujo editorial

**Fecha:** 2026-11-21
**Alcance:** módulo 0.1 «Aprender a aprender» (8 lecciones).
**Estado:** borradores editoriales visibles para estudio; **ninguna lección se declara publicada**.

## 1. Cobertura real

| Indicador | Valor |
|---|---:|
| Lecciones curriculares totales | 1.946 |
| Lecciones con contenido desarrollado | 8 |
| Lecciones con versión en borrador | 8 |
| Lecciones en revisión | 0 |
| Lecciones aprobadas | 0 |
| Lecciones publicadas | 0 |
| Lecciones pendientes | 1.938 |
| Videos con enlace y metadatos verificados | 8 |
| Videos con revisión pedagógica aprobada | 0 |
| Fuentes únicas registradas en el lote | 13 |
| Referencias de fuente asociadas | 16 |

Estas cifras provienen de SQLite y de `apps.roadmaps.coverage`. No se
confunden con el progreso del estudiante (`Progreso`).

## 2. Lecciones desarrolladas

Todas pertenecen a la etapa 0, módulo 0.1, y conservan el título oficial del
manifiesto ASCENSO 3.1:

1. Aprendizaje activo.
2. Pensamiento crítico.
3. Método Feynman.
4. Repetición espaciada.
5. Práctica deliberada.
6. Resolución de problemas.
7. Descomposición de problemas complejos.
8. Aprendizaje basado en proyectos.

Cada lección incluye, como mínimo:

- objetivos observables;
- conocimientos previos;
- introducción;
- explicación teórica;
- explicación sencilla;
- conceptos fundamentales;
- aplicaciones prácticas;
- errores frecuentes;
- un ejemplo guiado;
- dos ejercicios con evaluador determinista;
- evaluación del aprendizaje con criterios;
- fuentes con URL y nota de uso;
- un video complementario verificado por metadatos.

El texto es original de CodeGuard. Las fuentes se usan para atribución y
ampliación; no se reproduce su contenido.

## 3. Fuentes y evidencia

El lote registra referencias como:

- Dunlosky et al. (2013), *Improving Students' Learning With Effective Learning Techniques*, DOI `10.1177/1529100612453266`.
- Roediger y Karpicke (2006), DOI `10.1111/j.1467-9280.2006.01693.x`.
- Karpicke y Blunt (2011), DOI `10.1126/science.1199327`.
- Facione (1990), informe Delphi, `https://eric.ed.gov/?id=ED315423`.
- Chi et al. (1989), DOI `10.1207/s15516709cog1302_1`.
- Cepeda et al. (2006), DOI `10.1037/0033-2909.132.3.354`.
- Ericsson et al. (1993), DOI `10.1037/0033-295X.100.3.363`.
- Macnamara et al. (2014), DOI `10.1177/0956797614535810`.
- Polya, *How to Solve It* (Princeton University Press).
- Sweller (1988), DOI `10.1207/s15516709cog1202_4`.
- Wing (2006), DOI `10.1145/1118178.1118215`.
- Blumenfeld et al. (1991), DOI `10.1080/00461520.1991.9653139`.
- Kirschner, Sweller y Clark (2006), DOI `10.1207/s15326985ep4102_1`.

Cada registro se marca como `solo_referencia`: la licencia autoriza consulta y
atribución, no reproducción. La decisión queda con evidencia HTTPS, nota y
fecha. **Esta clasificación inicial fue registrada por el importador a partir de
la evidencia declarada en el lote; no constituye una revisión legal
independiente.** El propietario debe revisarla antes de publicar. Las URLs DOI
pueden devolver 403 a clientes automatizados; se validaron contra la API de
Crossref cuando fue posible.

## 4. Videos

Los videos se integran como recurso complementario y se abren en el navegador
del sistema mediante un IPC restringido a HTTPS. No se descargan, incrustan ni
republican.

| Lección | Video | Canal | Duración | Verificación |
|---|---|---|---:|---|
| Aprendizaje activo | El método de aprendizaje activo | Sprouts Español | 7:25 | título, URL, audio/captions `es` |
| Pensamiento crítico | 5 consejos para mejorar su pensamiento crítico | Sé Curioso — TED-Ed | 4:36 | título, URL, captions `es` |
| Método Feynman | La Técnica de Feynman | Sprouts Español | 2:05 | título, URL, audio `es-US` |
| Repetición espaciada | Repetición Espaciada — Técnicas de Aprendizaje | Instituto de Ciencias Interdisciplinarias | 4:29 | título, URL, captions `es` |
| Práctica deliberada | Práctica deliberada: Logra el dominio en cualquier cosa | Sprouts Español | 6:39 | título, URL, audio `es-US` |
| Resolución de problemas | George Polya — Estrategias de Resolución de Problemas | Fernando Faundez | 6:11 | título, URL, captions `es` |
| Descomposición | Descomposición de Problemas | Educatic Uruguay | 2:57 | título, URL, audio `es-US` |
| Aprendizaje basado en proyectos | Aprendizaje basado en proyectos explicado por Common Craft | Eliud Gabriel Porras | 3:52 | título, URL, audio `es-US` |

**Límite:** la verificación acredita metadatos públicos (título, canal,
duración y pista de audio/captions en español). No se ha realizado una revisión
pedagógica completa de cada minuto del video. Desde la auditoría final, el estado
técnico y el pedagógico son campos distintos: `estado_revision` acredita enlace y
metadatos; `estado_pedagogico` permanece **pendiente** en los 8 videos. La
interfaz del estudiante lo declara así y no presenta el video como material
validado didácticamente.

## 5. Estados editoriales

| Estado | Criterio |
|---|---|
| Pendiente | Sin contenido ni versión |
| En desarrollo | Existe contenido editable, sin snapshot |
| Borrador | Existe snapshot en estado borrador |
| En revisión | Snapshot congelado y enviado a revisión |
| Aprobada | Revisión editorial registrada |
| Publicada | Versión aprobada activada para el estudiante |

El progreso editorial se calcula en `apps.roadmaps.coverage`. El panel muestra
solo `Contenido en borrador` cuando corresponde; una lección no se presenta como
publicada sin un puntero `ContenidoLeccionActivo`.

## 6. Cómo se cargó

El comando:

```bash
python manage.py cargar_contenido_academico
python manage.py cargar_contenido_academico --dry-run
```

lee `apps/roadmaps/data/contenido_academico_0_1.json`, valida la estructura,
crea/actualiza contenido, ejemplos, ejercicios, videos y fuentes, y genera un
snapshot borrador. Es idempotente: si el snapshot no cambió, no crea otra
versión. **No publica ni aprueba**.

En un perfil limpio, el arranque ejecuta esta siembra una sola vez si no existe
contenido. No se repite en arranques posteriores.

## 7. Cómo revisar y publicar

1. Abrir **Editorial** en la navegación.
2. Entrar en una lección y revisar el contenido y sus fuentes.
3. Crear un snapshot versionado seleccionando fuentes activas.
4. Enviar a revisión.
5. Aprobar.
6. Publicar.
7. Para videos, revisar primero el enlace y después la ficha pedagógica. Aprobar
   la revisión pedagógica exige notas sobre correspondencia temática, nivel y
   utilidad didáctica; no se deduce de los metadatos.

Cada transición exige el propietario local con permiso editorial, queda
auditada y pasa la puerta de calidad del esquema 2: secciones mínimas, ejemplo,
ejercicio, fuentes y licencias revisadas. La publicación es una decisión
explícita; no ocurre durante la siembra.

## 8. Pendientes

- 1.938 lecciones sin contenido desarrollado.
- Revisión humana independiente del módulo 0.1.
- Revisión pedagógica completa de los 8 videos (0 aprobados actualmente).
- Publicación editorial del módulo cuando el propietario la autorice.
- Ampliar la producción a los módulos 0.2–0.4 y a los prerrequisitos.
- Contenido de evaluaciones formales (quizzes/exámenes) para el módulo.
