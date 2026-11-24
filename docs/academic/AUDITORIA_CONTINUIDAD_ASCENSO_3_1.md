# Auditoría de continuidad académica ASCENSO 3.1

**Fecha:** 2026-11-19  
**Rama examinada:** `content/ascenso-stage-0-learning-method`  
**Base técnica:** `release/1.0.0`  
**Estado:** diagnóstico documental; no equivale a aprobación editorial ni a pruebas de runtime.

## 1. Alcance y precisión del estado

La rama contiene 33 documentos de etapa (0–32), además de cuatro documentos de módulos de la etapa 0, cinco documentos de módulos de la etapa 1 y dos estándares editoriales. Esto representa una **primera cobertura documental de las 33 etapas**, no 1.946 lecciones terminadas. El roadmap oficial contiene 33 etapas, 212 módulos y 1.946 títulos de lección. Los documentos actuales son guías de desarrollo de etapa/módulo; aún debe desglosarse y redactarse cada lección con el nivel de profundidad exigido por el estándar editorial.

No se deben comunicar las 33 etapas como «curso completo», «lecciones completas» ni «contenido listo para publicar».

## 2. Hallazgos confirmados

### 2.1 Contrato real de importación

La inspección de `apps/roadmaps/content_import.py` en `release/1.0.0` confirma que el importador no acepta Markdown directamente. Acepta documentos JSON v1 con estas claves:

- Documento: `schema_version`, `resumen_cambios`, `snapshot`, `fuentes`.
- Snapshot: `esquema_version`, `leccion`, `contenido`, `ejemplos`, `ejercicios`.
- Identidad de lección: UUID canónico, título, descripción y tipo que deben coincidir exactamente con una lección ya existente.
- Ejemplos y ejercicios: cada elemento requiere sus propios UUID canónicos y debe pertenecer a la lección indicada.
- Fuentes: entre 1 y 20 referencias registradas, activas y asociadas a la versión.

El importador valida el UUID contra la base de datos, verifica identidad curricular, comprueba pertenencia de ejemplos/ejercicios y valida las fuentes. No crea ni inventa lecciones, UUID curriculares, ejemplos o ejercicios.

### 2.2 Flujo editorial real

Los comandos existentes establecen un flujo explícito:

1. Registrar fuente con `registrar_fuente_conocimiento`.
2. Revisar licencia y alcance con `revisar_licencia_fuente`.
3. Validar un lote JSON sin escrituras con `validar_paquete_contenido`.
4. Crear borradores con `importar_paquete_contenido --confirmar --usuario EDITOR`.
5. Enviar, aprobar y publicar mediante `gestionar_version_leccion` y sus transiciones.

La importación crea borradores, no publicaciones. La aprobación y publicación son transiciones separadas con actor editorial. No se debe saltar este flujo.

### 2.3 Límite de la inspección

La revisión se hizo leyendo código de la rama base a través de GitHub. No se ejecutó Django, no se consultó la SQLite real de una instalación de CodeGuard Pro y no se crearon registros. Por ello, todavía no se dispone de un inventario operativo de UUID de las 1.946 lecciones ni de las fuentes ya registradas en la base de datos del usuario.

### 2.4 Excepción curricular documentada

La etapa 25 del documento maestro no contiene un objetivo formal en el campo `objetivo`. El inventario `docs/ROADMAP_ASCENSO_INVENTARIO.md` ya registra esta ausencia. No se debe inventar un objetivo ni escribirlo en el JSON curricular como si fuera oficial. La guía académica puede explicar el propósito a partir de sus módulos, dejando claro que es una interpretación didáctica propuesta y pendiente de aprobación.

### 2.5 Regla audiovisual

La política se corrigió en los documentos editoriales: el audio hablado debe ser español y la relación temática debe ser directa. Un video hablado en inglés no se acepta aunque tenga subtítulos o doblaje automático. Cuando no se haya comprobado el audio, el recurso es candidato, no aprobado.

## 3. Riesgos y trabajo pendiente

| Riesgo | Acción requerida antes de publicación |
|---|---|
| Las guías de etapa no equivalen a 1.946 lecciones desarrolladas | Desglosar cada módulo y redactar cada lección con la plantilla editorial. |
| No se dispone del UUID de cada lección en este entorno | Exportar un manifiesto de UUID desde la instalación/DB de destino; cotejar título, etapa y módulo. |
| Los ejemplos/ejercicios también requieren claves estables existentes | Inventariar sus UUID reales o acordar, mediante el flujo de ingeniería correspondiente, cómo se crean antes de importar. |
| Fuentes no registradas/licencia sin revisar | Registrar fuentes reales, verificar edición/licencia/alcance y asociar IDs existentes. |
| Los Markdown no son el formato del importador | Crear un conversor Markdown/autoría → JSON v1 con pruebas de contrato; nunca inferir UUID. |
| Videos no reproducidos | No aprobar hasta verificar audio español, tema, enlace y actividad asociada. |
| Código/laboratorios no ejecutados | Mantener estado «no verificado» hasta probar entorno, instrucciones y resultado. |
| Etapa 25 sin objetivo oficial | Mantenerlo como vacío/propuesta, sin alterar el documento maestro ni el JSON. |

## 4. Próxima secuencia técnica segura

1. Crear un manifiesto de solo lectura desde la base de datos destino con UUID, etapa, módulo, título, tipo y claves de ejemplos/ejercicios.
2. Compararlo con el JSON oficial y detectar faltantes, duplicados y diferencias exactas de título.
3. Completar lecciones individuales con teoría, explicación sencilla, ejemplos, ejercicios, referencias y evidencia de verificación.
4. Registrar y revisar fuentes mediante los comandos editoriales existentes.
5. Convertir un lote piloto pequeño a JSON v1, usando exclusivamente UUID reales y fuentes registradas.
6. Ejecutar primero `validar_paquete_contenido`; no usar `--confirmar` hasta que el reporte sea limpio y el editor responsable esté identificado.
7. Importar solo borradores. Revisión, aprobación y publicación deben permanecer como actos editoriales separados.
8. Añadir pruebas de conversión, fidelidad curricular, trazabilidad y regresión.

## 5. Estado de esta auditoría

- Cobertura documental de etapas: 33/33.
- Lecciones curriculares redactadas y listas para importar: no determinado; no afirmar que sean 1.946.
- UUIDs de destino inventariados desde una base SQLite real: pendiente.
- Paquete JSON v1 generado y validado: pendiente.
- Contenido importado a SQLite: no.
- Contenido aprobado/publicado: no.
- Documento maestro y JSON curricular modificados por esta rama: no.

La prioridad siguiente es obtener un manifiesto curricular real y desarrollar contenido a nivel de lección, no declarar completado el roadmap por la mera existencia de 33 archivos.

## 6. Exportador de manifiesto de solo lectura añadido

Se añadió `apps.roadmaps.management.commands.exportar_manifiesto_academico` junto con pruebas Django en `apps/roadmaps/tests/test_exportar_manifiesto_academico.py`.

El comando:
- Selecciona el roadmap por nombre y edición exactos.
- Exporta jerarquía de etapas, módulos y lecciones.
- Incluye los UUID estables existentes de lecciones, ejemplos y ejercicios.
- Puede incluir el catálogo de fuentes registradas y su estado de licencia.
- No exporta progreso, cuentas, contraseñas ni datos de usuarios.
- No crea ni actualiza registros de la base de datos.
- Por defecto imprime JSON en stdout; con `--salida` crea un archivo nuevo y se niega a sobrescribir uno existente.

Ejemplo de ejecución en una instalación de desarrollo o una copia controlada de la base de datos:

```bash
python manage.py exportar_manifiesto_academico \
  --nombre "NOMBRE EXACTO DEL ROADMAP EN LA INSTALACIÓN" \
  --edicion "3.1" \
  --salida ./var/ascenso-manifest.json \
  --incluir-fuentes
```

El directorio `./var` debe existir y el archivo de salida no debe existir. Se recomienda ejecutar primero en una copia de la base de datos y almacenar el manifiesto en una ubicación privada, pues contiene identificadores internos de contenido. No subir ese manifiesto con UUID de una instalación real a un repositorio público.

**Verificación automatizada:** el workflow de GitHub Actions `CodeGuard Pro CI` terminó correctamente para el commit `510d0f8bbcaf560ce8027c8298da74fcd22baa03`: validación de sintaxis Python, `manage.py check`, comprobación de migraciones, suite Django, pruebas IPC de Electron y compilación/smoke test del servidor PyInstaller. El paquete Windows fue omitido por las condiciones del workflow. Los commits posteriores en esta rama modificaron únicamente documentación. **Pendiente de entorno real:** todavía no se ha ejecutado el exportador contra la base de datos local del usuario ni se ha generado el manifiesto real; esa comprobación requiere acceso a la instalación y su base de datos.


## Continuidad de las etapas 1–32 — 2026-11-24

Se consolidó la clasificación documental de las etapas 1–32 como **BASE DE TRABAJO ACTIVA**. Se actualizaron sus metadatos de estado para que la documentación sea la referencia operativa del desarrollo, sin presentarla como aprobada, revisada independientemente, validada en laboratorios ni publicada.

Se añadió [la guía de continuidad académica de las etapas 1–32](ASCENSO_3_1_GUIA_CONTINUIDAD_ETAPAS_01_32.md), construida a partir del inventario curricular existente. La guía resume la progresión por bloques, enumera los módulos oficiales y sus cantidades nominales de lecciones, conserva los proyectos del roadmap y explica cómo conectar los proyectos a lo largo del recorrido.

### Inventario confirmado

- Etapas 1–32: 32 etapas, 208 módulos y 1.916 lecciones nominales.
- Etapa 0: 4 módulos y 30 lecciones nominales.
- Total ASCENSO 3.1: 33 etapas, 212 módulos y 1.946 lecciones nominales.
- La etapa 25 conserva su objetivo oficial vacío; no se infirió ni se completó.
- No se modificó `apps/roadmaps/data/ascenso_3_1.json`, no se crearon UUID y no se importó contenido.

### Alcance de la actualización

La clasificación como base activa establece qué documentación debe utilizarse para continuar el trabajo. No significa que las 1.916 lecciones nominales de las etapas 1–32 estén desarrolladas individualmente con el mismo nivel de detalle, ni que todos los ejemplos, laboratorios, videos o proyectos se hayan ejecutado. El desarrollo granular por lección continúa como trabajo pendiente y se realizará sin alterar el inventario oficial.

La secuencia de bloques de la guía es una organización didáctica para facilitar continuidad; no introduce prerrequisitos curriculares obligatorios nuevos ni modifica los siete prerrequisitos registrados.


### Primera expansión granular — etapa 1

Se alinearon los módulos 1.1 y 1.2 con la granularidad exacta de sus lecciones en el roadmap, separando temas que antes aparecían combinados bajo un mismo encabezado:

- **Módulo 1.1 — Hardware:** 16 encabezados de lección, desde CPU y ALU hasta fuente de alimentación y periféricos.
- **Módulo 1.2 — Representación de información:** 9 encabezados de lección, separando sistemas binario, decimal y hexadecimal, y ASCII, Unicode y UTF-8.

La separación conserva las explicaciones y ejemplos existentes y mejora la correspondencia entre identificador curricular y contenido. No se afirma ejecución del laboratorio de hardware ni del codificador. Los módulos 1.3, 1.4 y 1.5 ya presentan 8, 7 y 6 encabezados temáticos respectivamente, en correspondencia con las cantidades nominales del roadmap.
