# ADR-004 — Sincronización híbrida del conocimiento académico

- **Estado:** Aprobada
- **Fecha:** 11 de noviembre de 2026
- **Decisor:** Propietario del proyecto
- **Fase:** Fase 2 — Motor de aprendizaje y contenido interactivo
- **Relacionado:** `docs/PLAN_MAESTRO_CODEGUARD.md`, `docs/FASE_2_APRENDIZAJE.md`, `docs/ARQUITECTURA.md`

## Contexto

El conocimiento técnico puede cambiar con el tiempo. Una aplicación exclusivamente offline corre el riesgo de conservar documentación desactualizada; una aplicación que dependa permanentemente de Internet pierde disponibilidad cuando no existe conexión. CodeGuard debe mantener la continuidad local y, al mismo tiempo, permitir actualizar el contenido académico con información revisada.

El repositorio actual implementa una aplicación local Electron + Django + SQLite y modelos iniciales para lecciones, ejemplos, ejercicios, intentos y evaluadores. En `main` todavía no existe un servicio central ni un mecanismo de sincronización de contenido.

## Decisión

Se adopta un **modelo híbrido de distribución de conocimiento** dentro de la Fase 2:

1. El contenido académico se mantiene en un repositorio/editorial maestro, con fuentes, licencias, versiones y revisiones.
2. Un servicio central publica paquetes inmutables de contenido aprobado y un manifiesto firmado.
3. El cliente local consulta el manifiesto cuando tiene conexión y descarga las versiones compatibles.
4. El contenido se almacena localmente y sigue disponible sin Internet.
5. La sincronización es iniciada por el cliente (pull-only) mediante HTTPS. No se expone el servidor local a conexiones remotas.
6. Los paquetes se validan por firma, hash, tamaño, esquema y compatibilidad antes de instalarse.
7. La activación es atómica y conserva la versión anterior para rollback.
8. El servicio central no recibe progreso, intentos, respuestas, código, calificaciones, notas privadas ni datos personales del estudiante.
9. Los cambios detectados en documentación externa generan propuestas de revisión; nunca actualizan automáticamente contenido publicado sin aprobación editorial.

## Decisiones de alcance

- La sincronización de conocimiento forma parte de la Fase 2; no se crea una fase adicional.
- La sincronización entre dispositivos y la subida de progreso quedan fuera de alcance.
- La actualización del contenido es independiente de las actualizaciones del ejecutable, sistema operativo o dependencias.
- El servicio central es un distribuidor de contenido, no el backend operativo de la aplicación de escritorio.
- Los intentos deben conservar la versión de contenido y evaluación que los originó.
- La detección de antigüedad no implica que el contenido sea incorrecto; la vigencia debe considerar la tecnología y versión objetivo.

## Consecuencias positivas

- CodeGuard conserva disponibilidad offline.
- El contenido puede corregirse y ampliarse de forma centralizada.
- Se puede auditar la procedencia, revisión y versión del conocimiento.
- Las actualizaciones fallidas no destruyen la última versión válida.
- Los datos académicos privados permanecen en el dispositivo.

## Costes y riesgos aceptados

- Se requiere infraestructura para publicar y distribuir paquetes.
- Se necesita un flujo editorial y de revisión técnica/pedagógica.
- La gestión de firmas, claves y compatibilidad añade complejidad.
- Deben definirse límites de almacenamiento, tamaño de paquetes, reintentos y política de versiones.
- El cliente offline no puede garantizar que su contenido sea el más reciente mientras no se conecte; debe mostrar fecha y estado de última sincronización.

## Requisitos de seguridad

- HTTPS/TLS para transporte y firma digital para autenticidad.
- Clave privada protegida en el entorno de publicación; cliente solo con clave pública.
- No ejecutar código ni scripts incluidos en los paquetes.
- Validar archivos, rutas, tamaños, esquemas y versiones.
- Evitar path traversal, zip bombs, paquetes truncados y downgrade no autorizado.
- Instalar desde una ubicación temporal y activar de forma atómica.
- Registrar fallos y permitir reintento/rollback.

## Alternativas consideradas

| Alternativa | Motivo de descarte |
|---|---|
| 100 % offline sin actualizaciones | No resuelve el envejecimiento del conocimiento técnico. |
| Internet obligatorio en cada sesión | Rompe la continuidad de estudio y crea dependencia permanente. |
| Consultar fuentes oficiales directamente desde cada lección | Produce disponibilidad y formatos inconsistentes, acopla la interfaz a terceros y no garantiza revisión pedagógica. |
| Publicar automáticamente cualquier cambio detectado | Puede propagar errores, cambios irrelevantes o contenido incompatible sin control editorial. |

## Criterios de cumplimiento

La decisión se considerará implementada cuando las pruebas `SYNC-001` a `SYNC-020` de `docs/PLAN_PRUEBAS.md` estén cubiertas, el flujo editorial y el cliente estén integrados, y se demuestre que las actualizaciones no alteran el progreso ni las evidencias del estudiante.

**Importante:** aprobar esta ADR registra la dirección arquitectónica; no significa que la sincronización ya esté construida o validada.