# Diseño técnico — Publicador central de conocimiento

**Producto:** CodeGuard Pro  
**Fase:** 2 — Motor de aprendizaje y contenido interactivo  
**Estado:** Diseño técnico previo a implementación  
**Fecha:** 11 de noviembre de 2026  
**Rama de trabajo:** `docs/phase-2-hybrid-knowledge-sync`

## 1. Objetivo

Construir el componente editorial que convierte versiones de lecciones aprobadas y publicadas en paquetes académicos inmutables, compatibles con el verificador local de distribución. El publicador no modifica el roadmap, no toca progreso ni intentos y no se ejecuta en el cliente del estudiante.

## 2. Entrada autorizada

El publicador solo seleccionará registros `VersionContenidoLeccion` cuyo estado sea `publicada`. No leerá el contenido editable actual de `ContenidoLeccion`, ni ejemplos/ejercicios mutables: el origen será exclusivamente el snapshot congelado de cada versión.

Antes de empaquetar cada lección debe comprobar:

- Hash SHA-256 del snapshot recalculado con JSON canónico (UTF-8, claves ordenadas y separadores compactos).
- Esquema académico soportado y UUID estable de lección, ejemplos y ejercicios.
- Referencias de fuente completas y congeladas al entrar en revisión.
- Evidencia de revisión de licencia y estado permitido: `compatible` o `solo_referencia`.
- Si la fuente está en `solo_referencia`, el uso declarado debe ser exclusivamente `original`.
- Para `compatible`, debe existir evidencia HTTPS, responsable/fecha de revisión y alcance de reutilización documentado.
- Ninguna fuente puede estar inactiva o tener una decisión de licencia incompatible con la publicación.

La salida por lección seguirá exactamente el contrato JSON v1 que consume `content_import._validate_document`: `schema_version`, `resumen_cambios`, `snapshot` y `fuentes`. Las referencias incluirán UUID de fuente, rol, localizador, nota de atribución y uso declarado.

## 3. Artefactos de distribución

Cada publicación producirá tres artefactos externos:

- `package.zip`: ZIP determinista con `package-index.json` y un JSON por lección bajo `payload/lessons/<uuid>.json`.
- `manifest.json`: manifiesto v1 con canal, secuencia, fecha UTC, versión mínima de aplicación, esquema, UUID/versión del paquete, URL HTTPS, tamaño, SHA-256 y `key_id`.
- `manifest.ed25519`: firma Ed25519 detached en Base64 sobre los bytes exactos de `manifest.json`.

El ZIP será reproducible para la misma entrada e identidad de paquete: orden estable de archivos, JSON canónico, timestamps ZIP fijos, permisos regulares normalizados y compresión definida. No se incluirán binarios, scripts, archivos ejecutables, datos de usuarios, progreso, intentos, credenciales ni configuraciones privadas.

## 4. Secuencia e historial de publicaciones

La secuencia es monotónica por canal y no puede depender únicamente de un argumento CLI ni de inspeccionar una carpeta arbitraria. Antes del publicador operativo se incorporará un registro central de releases con:

- Canal y secuencia únicos.
- UUID y SemVer del paquete.
- Hash del ZIP y hash del manifiesto.
- `key_id`, fecha de publicación y editor responsable.
- Identificador/ruta inmutable de los artefactos.

La reserva de secuencia se realizará bajo transacción y restricción única por canal. Un release ya registrado no se sobrescribe ni se vuelve a firmar con el mismo número. Los artefactos se prepararán en staging y se promoverán atómicamente; si falla la promoción, el release no se marcará como publicado. La política de recuperación de fallos entre almacenamiento y base de datos debe quedar explícita y probada.

## 5. Custodia de claves

- La clave privada Ed25519 se suministra fuera del repositorio mediante archivo PEM protegido o gestor de secretos.
- El publicador comprobará tipo de clave, permisos restrictivos del archivo y correspondencia con el `key_id` configurado.
- La clave privada nunca se registra, imprime, copia al ZIP ni almacena en SQLite.
- No se generarán claves de producción automáticamente durante una ejecución.
- La rotación de claves requerirá registrar previamente la clave pública correspondiente en los clientes y mantener un periodo de compatibilidad controlado.
- Las claves de prueba serán efímeras y solo existirán en fixtures de tests.

## 6. Separación de responsabilidades

El primer incremento implementará generación/validación local de artefactos y un comando editorial explícito. No realizará upload, despliegue CDN, cambios DNS ni configuración de proveedor. La URL pública declarada en el manifiesto deberá corresponder a una ubicación HTTPS autorizada y aprobada antes de una publicación real.

El cliente local seguirá siendo pull-only. La implementación del publicador no inicia conexiones desde el equipo del estudiante ni transmite información personal.

## 7. Pruebas de aceptación

- Solo versiones publicadas pueden empaquetarse.
- Rechazo de snapshot/hash alterado o esquema incompatible.
- Rechazo de fuente sin evidencia, licencia pendiente, permiso requerido, no reutilizable o inactiva.
- Rechazo de uso no permitido bajo `solo_referencia`.
- Validación de UUID y ausencia de colisiones entre recursos del paquete.
- ZIP determinista para la misma entrada.
- Round-trip: los artefactos generados pasan `verify_signed_manifest` y `validate_package_archive`.
- Rechazo de clave privada ausente, PEM inválido, tipo de clave incorrecto o permisos inseguros.
- Secuencia duplicada/descendente rechazada bajo concurrencia.
- Release y artefactos existentes nunca se sobrescriben.
- Fallo de escritura/promoción no deja un release marcado como publicado.
- Los paquetes no contienen información del estudiante ni código ejecutable.
- La generación no altera versiones editoriales, roadmap, progreso ni intentos.

## 8. Orden de implementación

1. Registro central de releases y migración.
2. Servicio puro de selección, validación y serialización de snapshots publicados.
3. Generador ZIP determinista y manifiesto firmado.
4. Comando editorial con dry-run y publicación explícita.
5. Pruebas unitarias, de integración y de fallos de almacenamiento.
6. Documentación operativa de custodia de claves, publicación y recuperación.

La implementación se mantendrá en la rama de trabajo. No se publicarán artefactos reales ni se desplegará infraestructura hasta que se aprueben proveedor, dominio, URL, política de claves y procedimiento de operación.
