# Plan de continuación académica — ASCENSO 3.1

**Rama:** `content/ascenso-stage-0-learning-method`  
**PR:** #14 — docs(academic): iniciar desarrollo de contenidos ASCENSO 3.1  
**Estado:** plan de trabajo editorial; no aprueba ni publica contenido.

## 1. Objetivo

Completar los materiales de aprendizaje de ASCENSO 3.1, partiendo de los documentos ya redactados en esta rama. El trabajo debe profundizar y corregir la base existente, no reemplazarla con contenido genérico ni duplicar módulos.

## 2. Fuente curricular y estructura que se preserva

La referencia sigue siendo el documento maestro del propietario y el manifiesto curricular ASCENSO 3.1. Se preservan exactamente:
- 33 etapas (0–32).
- 212 módulos.
- 1.946 lecciones nominales.
- 7 prerrequisitos.
- Prioridades P1/P2/P3 y títulos oficiales.

La etapa 25 carece de objetivo formal en la fuente maestra. No se inventará uno ni se incorporará la propuesta del inventario como objetivo oficial sin decisión editorial.

## 3. Auditoría inicial de los documentos existentes

La rama ya contiene documentos para los módulos 0.1, 0.2, 0.3 y 0.4, además de estándar editorial y política audiovisual.

| Módulo | Documento existente | Evaluación preliminar |
|---|---|---|
| 0.1 Aprender a aprender | `etapa-00/modulo-0.1-aprender-a-aprender.md` | Base extensa (8 lecciones). Requiere auditoría individual de evidencia, ejemplos, evaluaciones y referencias. |
| 0.2 Investigación técnica | `etapa-00/modulo-0.2-investigacion-tecnica.md` | Cubre los 7 temas oficiales y un proyecto/rúbrica. Debe profundizar cada lección con objetivos medibles, práctica reproducible, criterios y fuentes precisas. |
| 0.3 Herramientas | `etapa-00/modulo-0.3-herramientas.md` | Cubre las 8 herramientas oficiales. Requiere laboratorios reproducibles, instrucciones seguras por sistema operativo y criterios de dominio. |
| 0.4 Depuración | `etapa-00/modulo-0.4-depuracion.md` | Cubre el ciclo de depuración y los temas oficiales. Requiere casos guiados, pruebas de hipótesis, ejercicios con solución y criterios de regresión. |

La revisión anterior es de inventario y estructura; no equivale todavía a una aprobación técnica o pedagógica línea por línea.

## 4. Contrato didáctico por lección

Cada uno de los 1.946 títulos debe convertirse en una unidad propia y alineada con su nivel. Incluir cuando corresponda:

1. Identidad curricular exacta: etapa, módulo y título.
2. Objetivos observables y criterios de éxito.
3. Conocimientos previos y conexión con lecciones anteriores.
4. Introducción y relevancia.
5. Explicación conceptual gradual y técnicamente precisa.
6. Vocabulario y conceptos fundamentales.
7. Ejemplo resuelto, con razonamiento paso a paso.
8. Aplicación técnica o caso realista.
9. Errores frecuentes, límites y riesgos.
10. Ejercicios progresivos con instrucciones y soluciones razonadas.
11. Laboratorio reproducible cuando el tema lo requiera.
12. Reto de transferencia o mini-proyecto.
13. Evaluación alineada con los objetivos y rúbrica.
14. Fuentes trazables y fecha de consulta.
15. Recurso audiovisual opcional, únicamente después de verificar audio español y pertinencia directa.

No forzar código, laboratorio ni video en temas donde no aporten aprendizaje. Para respuestas abiertas, usar rúbricas; no confundir coincidencia de palabras con evaluación semántica.

## 5. Fuentes y videos

Priorizar documentación oficial, estándares, especificaciones, organismos públicos y literatura académica revisada por pares. Las respuestas de foros, blogs y videos pueden orientar o complementar, pero no deben ser la única base de afirmaciones importantes.

Para videos:
- comprobar el audio hablado real en español;
- revisar el contenido completo o los segmentos pertinentes;
- comprobar que enseñe directamente el objetivo;
- registrar canal, URL, duración y fecha solo cuando se verifiquen;
- mantener separado el estado de metadatos del estado de revisión pedagógica.

Si no hay video que cumpla los requisitos, la lección queda sin video. No traducir un video en inglés mediante subtítulos y presentarlo como recurso en español.

## 6. Importación: requisito crítico de UUID

El PR #14 utiliza un contrato de importación distinto al cargador de la rama de aplicación. El importador de esta rama exige:

- UUID curricular real de la lección existente.
- UUID reales de ejemplos y ejercicios ya registrados para esa lección.
- UUID de fuentes que existan y estén activas en la base de datos.
- Identidad curricular coincidente con la base de datos.
- JSON v1 estricto y validación del directorio completo antes de escribir.

Por tanto:
- No inventar ni generar UUID.
- No reutilizar UUID entre recursos.
- No copiar el formato del archivo `contenido_academico_0_1.json` de otra rama como si fuera compatible.
- Exportar el manifiesto de la instalación de desarrollo con `exportar_manifiesto_academico` en modo solo lectura.
- Mantener el manifiesto con UUID fuera del repositorio público si contiene identificadores de la instalación.
- Preparar los documentos de contenido y mapearlos al manifiesto real antes de crear paquetes JSON.
- Ejecutar primero `importar_paquete_contenido --directorio ...` sin `--confirmar`; solo crear borradores cuando el lote pase la validación y el editor explícito autorice la importación.

El importador crea borradores; no aprueba ni publica.

## 7. Orden de producción

### Etapa 0 — completar y validar fundamentos

1. Auditar las 8 lecciones de 0.1 y corregir con evidencia.
2. Profundizar las 7 lecciones de 0.2 Investigación técnica.
3. Profundizar las 8 lecciones de 0.3 Herramientas.
4. Profundizar las 7 lecciones de 0.4 Depuración.
5. Diseñar y validar el proyecto integrador ASCENSO-Knowledge-Base.

La etapa 0 contiene 30 lecciones nominales. Debe quedar coherente antes de avanzar.

### Después de la etapa 0

Producir etapas P1 en orden curricular, respetando los 7 prerrequisitos. Después completar P2 y P3 según dependencias y objetivos de especialización. No desbloquear contenido en la aplicación solo porque el documento esté redactado.

## 8. Estados editoriales

- Pendiente: no existe cuerpo didáctico.
- En desarrollo: redacción en curso.
- Borrador: documento estructurado, aún no revisado completamente.
- En revisión: versión congelada con evidencia enviada a revisión.
- Aprobado: revisión técnica, pedagógica, práctica y editorial registrada.
- Publicado: versión aprobada activada en la aplicación.

Los documentos actuales de esta rama siguen siendo borradores. No se aprobarán ni publicarán automáticamente por pasar validadores estructurales.

## 9. Próximas acciones concretas

1. Auditoría línea por línea de las ocho lecciones de 0.1.
2. Crear una matriz de objetivos, evidencia, ejercicios y fuentes para 0.1.
3. Revisar el módulo 0.2 y ampliarlo sin duplicar el material existente.
4. Repetir para 0.3 y 0.4.
5. Preparar el proyecto integrador y su rúbrica.
6. Obtener el manifiesto privado real de la base de datos y preparar paquetes de importación sin inventar UUID.
7. Ejecutar validación y pruebas de importación en perfil aislado.
8. Actualizar el estado y cobertura editorial con conteos separados por redactado, revisado, aprobado e importado.

## 10. Restricciones

- Mantener este trabajo en la rama académica y PR #14; no mezclarlo con PR #17 de finalización de la aplicación.
- No tocar PR #15 ni PR #16.
- No fusionar PR #14 sin autorización.
- No crear tags ni releases.
- No alterar el DOCX maestro ni la estructura del roadmap.
- No afirmar revisión, ejecución, aprobación o publicación sin evidencia.
