# Estado de avance de beta — CodeGuard Pro

**Fecha:** 2026-11-19  
**Rama de trabajo:** `fix/electron-ipc-origin-validation`  
**Base:** `main` en `59d08848726550fde442be1eb1e1be5522637f0b`  
**Pull request:** https://github.com/MaverickBms/CodeGuard-Pro/pull/12 (borrador)

## Trabajo realizado en esta iteración

- Se centralizó la validación de origen para IPC en `electron/ipc-security.js`.
- La comprobación exige URL válida, protocolo HTTP, host loopback esperado, puerto dinámico exacto y ausencia de credenciales.
- Se aplicó la validación a todos los canales IPC expuestos por `electron/preload.js`: tema, notificaciones, estado/solicitud de sincronización, información del sistema y selector de carpetas.
- Las notificaciones ahora limitan título (120 caracteres) y cuerpo (1000 caracteres), y solo usan el icono local de la aplicación.
- Se añadieron seis casos de regresión en `electron/ipc-security.test.js` y el comando `npm run test:electron`.

## Evidencia ejecutada

Se ejecutó el helper y sus seis pruebas en un directorio aislado de Node, usando el mismo script npm definido para el repositorio:

```text
npm run test:electron
# tests 6
# pass 6
# fail 0
```

Los casos cubren origen exacto, puerto diferente, host que suplanta el prefijo loopback, protocolo no permitido, credenciales en URL y argumentos/eventos inválidos.

Esta ejecución valida la función pura y sus pruebas. No equivale a ejecutar Electron ni prueba la integración IPC real.

## Estado de validación de beta

| Área | Estado |
|---|---|
| Validación unitaria del helper IPC | 6/6 OK en entorno aislado |
| Sintaxis completa de Electron en el checkout | Pendiente |
| Integración real de canales IPC en Electron | Pendiente |
| Suite Django completa | Pendiente |
| Migraciones y carga ASCENSO en perfil vacío | Pendiente |
| Instalación limpia Windows | Pendiente |
| Build y primer arranque Linux AppImage | Pendiente |
| Flujo offline E2E | Pendiente |
| Persistencia tras reinicio | Pendiente |
| Backup y restauración aislados | Pendiente |
| Cierre limpio y ausencia de procesos huérfanos | Pendiente |

La consulta remota no encontró ejecuciones de GitHub Actions para la rama/repo en el endpoint consultado. No se debe interpretar como build aprobado.

## Protección del trabajo local del propietario

Esta rama parte del HEAD público de `main`; no contiene modificaciones locales no publicadas. En particular, no incluye el diff previo de `electron/main.js` observado en la conversación. El PR debe revisarse junto con ese diff antes de integrar ambos trabajos. No se ha modificado ni descartado el checkout local.

## Siguiente bloque de trabajo

1. Obtener un checkout ejecutable del proyecto o un entorno local conectado al repositorio, conservando el parche de trabajo previo.
2. Ejecutar `node --check` sobre ambos archivos Electron y `npm run test:electron` en la raíz real.
3. Ejecutar los checks y las 245 pruebas Django históricamente reportadas sobre el HEAD exacto, en directorio de datos temporal.
4. Completar pruebas de arranque, persistencia, offline, backup/restore y cierre en las plataformas que se van a presentar.
5. Corregir solo fallos reproducibles y añadir regresiones.

**Criterio de salida:** CodeGuard Pro sigue en estado beta no aceptada hasta que los criterios de instalación, primer arranque, flujo académico esencial, persistencia, offline y cierre limpio tengan evidencia reproducible.
