# Cierre de fase — Integración técnica ASCENSO 3.1

- **Fecha:** 2026-11-24
- **Rama:** `content/ascenso-stage-0-learning-method`
- **PR:** #14 (borrador, sin fusionar)
- **Estado:** **CERRADA CON BLOQUEOS EXTERNOS DOCUMENTADOS** (ver §13 y §14)
- **Actualización de cierre final:** 2026-11-24 — pendientes 1-4 atendidos con evidencia; persisten bloqueos externos editoriales/DB-scope.

> Este documento es el cierre único de la fase de preparación e integración técnica de ASCENSO 3.1. Sustituye como referencia operativa los informes de continuidad previos para esta fase; esos documentos se conservan como historial.

## 1. Alcance exacto de la fase

Incluido:
- Auditoría de inventario curricular contra la base de desarrollo real identificada (solo lectura).
- Conciliación individual roadmap JSON / manifiesto / DB / documentación.
- Endurecimiento del contrato de fuentes/licencias en validación e importación.
- Auditoría de seguridad y robustez del exportador/importador JSON v1.
- Investigación y conciliación de diferencias de migraciones 0020–0023 / library.0002.
- Preparación y validación de paquete piloto (sin importación).
- Ejecución de pruebas en el HEAD final.
- Documentación de cierre y limitaciones.

Excluido (prohibido o fuera de fase):
- Modificación de `apps/roadmaps/data/ascenso_3_1.json`.
- Migraciones, escrituras, restauraciones o copias de la base de datos real.
- Importación, aprobación, publicación, sustitución o retiro de versiones editoriales.
- Fusión de PRs, creación de tags/releases, cambios en PR #15/#16/#17.
- Publicación de manifiestos, UUID reales, datos de usuarios o paquetes privados.

## 2. Inventario curricular conciliado

| Capa | Etapas | Módulos | Lecciones | Prerrequisitos | Resultado |
|---|---:|---:|---:|---:|---|
| Roadmap oficial JSON (`apps/roadmaps/data/ascenso_3_1.json`) | 33 | 212 | 1946 | 7 | Fuente de verdad, sin cambios |
| Manifiesto privado (DB dev real, solo lectura) | 33 | 212 | 1946 | 7 (verificados en DB) | Coincide individualmente |
| DB dev (`/home/mvxbms/.config/CodeGuard Pro/db.sqlite3`) | 33 | 212 | 1946 | 7 | Coincide |
| Markdown (`docs/academic/ascenso-3.1/**/*.md`) | — | — | 1946 IDs presentes | — | Presencia estructural, no validación |

Verificaciones realizadas (solo lectura):
- Conteos 33/212/1946/7 conciliados.
- Comparación individual por etapa/módulo/lección: títulos, objetivos, prioridad, proyecto, orden, jerarquía y títulos de lección coinciden entre JSON y manifiesto (0 diferencias).
- Prerrequisitos DB vs JSON: 7/7 coinciden (etapa origen, etapa requerida, justificación).
- UUID: 1946 UUID de lección únicos en manifiesto; sin duplicados en el conjunto inspeccionado (lecciones, ejemplos, ejercicios, fuentes).
- Ejemplos/ejercicios en manifiesto pertenecen a sus lecciones; no se detectaron huérfanos en la comparación estructural.
- Etapa 25 conserva objetivo oficial vacío.

## 3. Resultado de la comparación completa roadmap/manifiesto

- **Diferencias estructurales:** 0.
- **Diferencias de prerrequisitos:** 0.
- **UUID duplicados/ausentes:** 0 detectados.
- **Lecciones huérfanas / módulos o etapas faltantes:** 0 detectados.
- **Títulos/orden/relaciones:** coinciden.

La comparación se realizó con script de solo lectura sobre el manifiesto privado y el JSON oficial; el informe no expone UUID.

## 4. Estado real de la instalación

Base candidata (solo lectura, no modificada):
- Ruta: `/home/mvxbms/.config/CodeGuard Pro/db.sqlite3`
- Identidad: `PROYECTO ASCENSO — Roadmap Maestro Consolidado`, edición `3.1`, activo, sha256 de fuente coincide con el JSON oficial.
- Tamaño/mtime observados en auditoría: 1.556.480 B, 2026-11-23T17:02:01.
- Esquema: migraciones hasta `roadmaps.0023_progreso_unicidad_por_nivel`, `library.0002_unique_document_sha256`.

Estado editorial observado (agregado):
- Versiones de contenido: 8 (todas `borrador`).
- Contenido activo: 0.
- Contenido legacy con cuerpo: 8.
- Ejemplos: 8. Ejercicios: 16.
- Fuentes: 13, todas `solo_referencia`, todas activas, todas con evidencia HTTPS y auditoría; **0/13 con `alcance_licencia` documentado**.
- Referencias de versiones existentes: 16, todas `uso_declarado=original`.

Distinción requerida:
- **Inventario curricular:** completo en JSON/DB/manifiesto (33/212/1946).
- **Documentación Markdown:** 1946 IDs presentes; presencia estructural, no validación pedagógica/técnica ni aprobación.
- **Contenido importado/editorial en DB:** 8 borradores, 0 en revisión, 0 aprobados, 0 publicados, 0 activos.
- **Contenido publicado:** 0.

## 5. Resultado de la auditoría de fuentes y licencias

Matriz detallada: `docs/academic/MATRIZ_LICENCIAS_FUENTES_ASCENSO_3_1.md` (13/13 fuentes investigadas; clasificación conservadora basada en evidencia accesible; sin cambios en BD).

**Conclusión de auditoría:** completada y verificable. **Conclusión operativa:** 12/13 fuentes quedan restringidas (`requiere_permiso`/`pendiente`) para reutilización; 1/13 (`Facione`, ERIC ED315423) es viable como `solo_referencia` con alcance explícito, pero su alcance no está documentado en BD, por lo que el validador técnico la rechaza hasta revisión editorial autorizada.

### Hallazgos
1. **Política anterior insuficiente:** la validación permitía pasar con advertencia para fuentes no `compatible`; la revisión de licencia se aplicaba principalmente al enviar a revisión. Corregido.
2. **Fuentes DB sin alcance:** las 13 fuentes reales son `solo_referencia` con evidencia/auditoría pero `alcance_licencia` vacío. Bajo la nueva política no superan validación para importación. No se modificaron.

### Política implementada (código)
- `pendiente`, `requiere_permiso`, `no_reutilizable`: **rechazadas** en validación.
- `compatible`: exige evidencia auditable, auditoría (`revisada_por`, `revisada_en`) y `alcance_licencia` documentado; uso declarado debe ser permitido.
- `solo_referencia`: exige evidencia auditable, auditoría y alcance de consulta documentado; solo permite `uso_declarado=original` (no cita/adaptación/reproducción).
- Fuente inactiva, inexistente, sin evidencia/auditoría: **rechazada**.
- La política se aplica en `validar_directorio_contenido` y se vuelve a comprobar dentro de `importar_documentos_validados` (revalidación transaccional). No se puede eludir con informe fabricado o cambio posterior a la validación.
- `knowledge.revisar_licencia_fuente` exige alcance para `compatible` y `solo_referencia`. `_validar_version_para_revision` mantiene coherencia.

Archivos modificados:
- `apps/roadmaps/content_import.py`
- `apps/roadmaps/knowledge.py`
- `apps/roadmaps/management/commands/revisar_licencia_fuente.py`
- `apps/roadmaps/tests/test_content_import.py`

## 6. Contrato JSON v1 definitivo

Contrato aplicado por `apps/roadmaps/content_import.py` (sin cambios incompatibles de esquema; endurecimiento de política):
- `schema_version`: 1. `snapshot.esquema_version`: 1.
- Claves top-level exactas: `schema_version`, `resumen_cambios`, `snapshot`, `fuentes`.
- Rechazo de claves duplicadas, propiedades desconocidas, profundidad > 8, tipos inválidos.
- UUID canónicos en minúsculas; rechazo de duplicados/reasignaciones en documento y lote.
- Límites: 2 MiB/doc, 100 MiB/lote, 500 docs, 50 ejemplos, 50 ejercicios, 20 fuentes.
- Rechazo de symlinks, subdirectorios, no-JSON, no UTF-8.
- Identidad curricular verificada contra DB (lección, título, descripción, tipo; recursos pertenecen a la lección).
- Fuentes: registradas, activas, con política de licencia cumplida.
- Hash SHA-256 determinista del snapshot canónico (`sort_keys=True`, separators `(",",":")`).
- Idempotencia por hash+procedencia; importación crea solo borradores; nunca publica.
- Revalidación dentro de transacción; `select_for_update`; control de concurrencia por unicidad de versión y transacción.

## 7. Resultado de la auditoría de seguridad

| Control | Resultado | Evidencia |
|---|---|---|
| Claves JSON duplicadas / desconocidas | PASS | `_pairs_without_duplicates`, `_expect_keys` |
| UUID inválidos/no canónicos/duplicados | PASS | `_uuid`, checks de duplicados |
| Recursos de otra lección | PASS | `_validate_against_database` |
| Fuentes no registradas/no autorizadas/inactivas/sin evidencia | PASS | política estricta implementada |
| Límites tamaño/lote/profundidad/cantidad | PASS | constantes y checks |
| Symlinks/rutas no regulares | PASS | validación de entrada; export endurecido (symlink padre) |
| Hash SHA-256 determinista | PASS | canonical JSON |
| Idempotencia | PASS | prueba `test_reimportacion_del_mismo_hash_es_idempotente` |
| Concurrencia/atomicidad | PASS | `@transaction.atomic`, `select_for_update`, revalidación, `IntegrityError` en comando |
| No sobrescribir versiones/contenido existente | PASS | solo crea borradores nuevos |
| Restricción editor activo | PASS | servicio y comando |
| Exportador: sobrescritura/symlinks | PASS | `is_symlink`, `exists`, `open('x')`, padre no symlink |
| Exportador: sin datos personales/secretos | PASS | no exporta usuarios/progreso/credenciales |

## 8. Resultado de la revisión de migraciones

### Hallazgo
La DB real tiene aplicadas migraciones posteriores al worktree:
- `roadmaps.0020_estado_instalacion_roadmap`
- `roadmaps.0021_contenido_academico_ampliado_y_videos`
- `roadmaps.0022_recursoaudiovisual_revision_pedagogica`
- `roadmaps.0023_progreso_unicidad_por_nivel`
- `library.0002_unique_document_sha256`

Los commits existen en `release/1.0.0-final` (historial Git). El worktree académico estaba en 0019.

### Acción tomada (segura, sin migrar DB)
- Se incorporaron al worktree los archivos de migración 0020–0023 de roadmaps desde commits históricos (`5a1862e`, `4d632ae`, `24d04b6`, `4fd8127`).
- Se actualizaron modelos de `apps/roadmaps/models.py` para reflejar el esquema: campos de `ContenidoLeccion` (0021), `EstadoInstalacionRoadmap` (0020), `RecursoAudiovisual` + revisión pedagógica (0021/0022), restricciones de unicidad de `Progreso` (0023).
- Verificación: `python manage.py makemigrations --check --dry-run` = **No changes detected**.

### Bloqueo/documentación
- `library.0002` existe en DB pero la app `library` no está presente en esta rama académica. No se integró la app completa por ser cambio amplio no directamente requerido para la integración académica; se documenta como divergencia de rama. `makemigrations --check` no la evalúa porque no está instalada en este worktree.
- No se ejecutaron migraciones. No se marcaron migraciones como aplicadas.

## 9. Paquete piloto y resultado de validación

- **Paquete original conservado como evidencia:** `etapa-00-modulo-0.1-leccion-01-aprendizaje-activo.json` (Etapa 0, Módulo 0.1, Lección 1, “Aprendizaje activo.”). SHA-256: `ef346af25b5a09d1462062a37ec46f81aba764ade60e3d3ca77a145863a1831d`.
- **Estructura:** JSON v1 válido en forma, UUID reales de lección/ejemplo/ejercicios/fuente desde manifiesto privado, contenido original, uso declarado `original`, sin importación.
- **Validación oficial contra DB real (solo lectura, `validar_paquete_contenido`):** **NO SUPERA** la validación por política de fuentes. Error: la fuente real referenciada es `solo_referencia` activa con evidencia/auditoría pero sin `alcance_licencia` documentado. El validador la rechaza correctamente.
- **Alternativa:** no es posible construir un paquete piloto que supere la validación completa contra la DB real sin modificar registros de fuentes (prohibido) ni inventar UUID/fuentes (prohibido). Las 13 fuentes registradas carecen de alcance documentado en BD; el contrato exige ≥1 fuente registrada y autorizada. No se debilitó la política.
- **No se ejecutó** `importar_paquete_contenido`. **No se escribió** en la base de datos.

Conclusión: bloqueo externo/editorial. El paquete es correcto y la política funciona; el paso pendiente es revisión editorial autorizada de licencias/alcances en BD.

## 10. Pruebas ejecutadas y resultados

Ejecutadas en el worktree con `/tmp/opencode/cg-venv` (Django 5.2.19), `DJANGO_SETTINGS_MODULE=config.settings.development`, `CODEGUARD_DATA_DIR=/tmp/opencode/cgdata`:

| Prueba | Resultado |
|---|---|
| `python manage.py check` | PASS (0 issues) |
| `python manage.py makemigrations --check --dry-run` | PASS (No changes detected) |
| `apps.roadmaps.tests.test_content_import` | PASS (20/20) |
| `apps.roadmaps.tests.test_exportar_manifiesto_academico` | PASS (3/3) |
| `python manage.py test apps.roadmaps -v 1` | PASS (192/192) |
| `python manage.py test apps -v 1` | PASS (306/306) |
| Validación oficial paquete piloto (DB real, ro) | FAIL esperado por alcance de fuente en DB; política aplicada correctamente |

No se declararon PASS pruebas no ejecutadas.

## 11. Commit final y estado de CI

- **HEAD final verificado:** `ce9e4b7a8c9e1a75bc070c574c02ff17084b8960` — `docs(ascenso): cerrar pendientes de integración con matriz de licencias y evidencia CI`
- **Commits previos de la fase:** `8dc59754f7e59a4b5d9b5adf8f2c2a6b8df7f5ad` (contenido), `122f0a6fa5611a1f0c505a1c8d6f85fb692051c4` (documentación de cierre).
- **CI verificada (GitHub Actions):** run `45528884424` — `CodeGuard Pro CI`, evento `push`, rama `content/ascenso-stage-0-learning-method`, SHA `ce9e4b7a8c9e1a75bc070c574c02ff17084b8960`, conclusión **success**.
  - URL: https://github.com/MaverickBms/CodeGuard-Pro/actions/runs/45528884424
  - Jobs: `Django checks and test suite` (success), `PyInstaller server build and smoke test` (success), `Electron IPC unit tests` (success), `Windows x64 package` (skipped por condición de workflow: solo workflow_dispatch/PR/release/1.0.0; no es fallo).
- No se atribuyen resultados de commits anteriores al HEAD nuevo.

## 12. Preservación privada de artefactos

- **Ubicación privada persistente (fuera del repo):** `~/.local/share/codeguard-pro/ascenso_3_1/` (permisos 700/600).
- **Contenido:** `manifiesto/` (manifiesto privado), `piloto/` (paquete piloto), `evidencias/` (matriz de licencias, inventario), `checksums/SHA256SUMS.txt`.
- **Verificación:** hashes SHA-256 calculados y verificados (`sha256sum -c` OK). Archivos originales en `/tmp/opencode/private_ascenso/` no eliminados por la copia.
- **Git:** la ubicación está fuera del repositorio; `git status` limpio respecto a estos artefactos.

## 13. Limitaciones reales fuera de esta fase

1. **Alcances de licencia pendientes en BD (bloqueo externo):** 13/13 fuentes registradas carecen de `alcance_licencia` documentado en BD. Hasta que se revise cada fuente por el flujo editorial autorizado (`revisar_licencia_fuente`) con evidencia y alcance, los paquetes que las referencien no pasarán la validación estricta. La investigación documental no equivale a actualización de BD.
2. **Evidencia específica/permisos de titulares no verificados (bloqueo externo):** la matriz clasificó conservadoramente 12/13 fuentes como `requiere_permiso`/`pendiente` y 1/13 como `solo_referencia` viable solo para consulta sin reproducción. La clasificación documental no constituye autorización legal ni permiso de reproducción/adaptación.
3. **Divergencia `library` app/migración (bloqueo externo):** la DB real tiene `library.0002` aplicada; la app `library` no está presente en esta rama. Requiere decisión de integración de rama.
4. **Contenido editorial masivo no importado:** 1946 lecciones documentadas estructuralmente en Markdown, pero solo 8 borradores en DB y 0 aprobadas/publicadas. La importación es una fase editorial posterior.
5. **Validación profunda 1.946 lecciones:** no realizada (pedagógica/técnica/ejecución/referencias). La presencia estructural no equivale a aprobación.

## 14. Procedimiento concreto para la siguiente fase editorial

1. **Revisar licencias de fuentes** (flujo autorizado, con evidencia y alcance): completar `alcance_licencia` para fuentes `solo_referencia`/`compatible` según corresponda, sin modificar datos fuera del flujo auditado.
2. **Revalidar paquete piloto** contra DB real tras actualizar alcance de fuente; confirmar PASS.
3. **Importar solo tras autorización explícita:** `validar_paquete_contenido` PASS → `importar_paquete_contenido --confirmar --usuario EDITOR` → borrador creado. Nunca publicar en importación.
4. **Flujo editorial por lote:** borrador → revisión → aprobación → publicación, con actor staff activo y evidencia/licencia congelada.
5. **Auditoría profunda por lotes:** 7–10, 11–16, 17–20, 21–25, 26–32; registrar evidencia en `AUDITORIA_CONTINUIDAD_ASCENSO_3_1.md`.
6. **No tocar** `apps/roadmaps/data/ascenso_3_1.json`, ni inventar UUID, ni exponer manifiestos privados.
