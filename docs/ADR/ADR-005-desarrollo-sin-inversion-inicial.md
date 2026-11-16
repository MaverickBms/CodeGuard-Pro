# ADR-005 — Desarrollo inicial sin inversión y expansión diferida

- **Estado:** Aprobada
- **Fecha:** 15 de noviembre de 2026
- **Decisor:** Propietario del proyecto
- **Fase:** Estrategia transversal de producto y desarrollo
- **Relacionado:** `docs/ESTRATEGIA_SIN_INVERSION_INICIAL.md`, `docs/PLAN_MAESTRO_CODEGUARD.md`, `docs/ADR/ADR-004-sincronizacion-hibrida-conocimiento.md`

## Contexto

CodeGuard Pro necesita una aplicación local estable, contenido académico de calidad y un flujo de aprendizaje validado antes de asumir los costos y la operación de servicios remotos. El proyecto ya contempla un modelo híbrido de distribución de conocimiento (ADR-004), pero ese diseño no obliga a desplegar hosting o una base de datos central durante el desarrollo inicial.

## Decisión

Se aprueba desarrollar y completar primero la versión local de CodeGuard Pro **sin inversión en infraestructura externa**. No se contratarán hosting, VPS, base de datos alojada, dominio ni APIs de IA de pago en esta etapa.

La persistencia del producto seguirá en SQLite local. El contenido académico y los paquetes de conocimiento deberán poder utilizarse localmente. Las actualizaciones podrán prepararse mediante paquetes e importación manual, una vez validado integralmente ese flujo.

La expansión remota queda diferida hasta que exista una necesidad real, una propuesta de costos y la aprobación explícita del propietario.

## Relación con ADR-004

ADR-004 conserva la decisión arquitectónica de permitir distribución centralizada y sincronización automática opcional de conocimiento. ADR-005 define el orden de ejecución y el límite financiero inicial:

- ADR-004: **cómo podrá funcionar** la distribución híbrida cuando se despliegue.
- ADR-005: **cuándo se implementará la infraestructura remota**: después de consolidar la versión local y solo si se aprueba invertir.

Por tanto, ADR-005 no cancela ni reemplaza ADR-004. Posponer hosting no exige eliminar el publicador, el verificador, el instalador o el cliente de sincronización ya desarrollados. La sincronización remota debe permanecer inactiva hasta disponer de endpoint, allowlist, claves públicas confiables y validación de producción.

## Consecuencias

### Positivas

- No se asumen gastos recurrentes de infraestructura durante la etapa inicial.
- La aplicación conserva su propósito offline-first.
- Se evita diseñar una base de datos remota sin una necesidad comprobada.
- El proyecto puede concentrar tiempo y recursos en contenido, evaluación, seguridad y experiencia educativa.
- La futura expansión puede añadirse sin convertirla en requisito para el funcionamiento local.

### Costos y límites aceptados

- Las actualizaciones de conocimiento podrán requerir intervención manual.
- No habrá sincronización automática central ni distribución pública administrada mientras no se despliegue infraestructura.
- La publicación local de paquetes no equivale por sí sola a un servicio remoto operativo.
- El costo de infraestructura externa objetivo es cero, pero el equipo, la electricidad, la conexión y el tiempo de desarrollo siguen siendo costos indirectos.

## Condiciones para reconsiderar

La inversión podrá evaluarse cuando la versión local esté consolidada y exista una necesidad demostrable, como distribuir contenido a varias instalaciones, gestionar un catálogo remoto o habilitar colaboración. La evaluación debe comparar alternativas gratuitas y de pago, costos recurrentes, límites, seguridad, mantenimiento y portabilidad. La evaluación no autoriza el gasto: se requiere aprobación explícita.

## Regla de cumplimiento

No introducir servicios cloud obligatorios ni costos recurrentes sin una decisión documentada del propietario. La versión local debe seguir siendo utilizable sin conexión y conservar los datos académicos del estudiante en el dispositivo.
