# Estabilización previa a la continuación del desarrollo

**Fecha:** 15 de noviembre de 2026  
**Rama de trabajo:** `chore/stabilizacion-pre-fase-2`  
**Objetivo:** corregir documentación desactualizada y retirar residuos confirmados sin alterar la lógica de negocio ni los datos.

## Cambios realizados

1. **README.md**
   - Actualiza el estado de sincronización: cliente HTTP, comando, publicador local, instalador y scheduler Electron implementados.
   - Aclara que hosting, endpoint público, allowlist y claves públicas de producción siguen pendientes.
   - Añade `publicar_paquete_conocimiento` y `sincronizar_conocimiento` a la tabla de comandos.
   - Sustituye la cifra obsoleta de 93 pruebas por el último resultado reportado (138), indicando expresamente que debe reproducirse.

2. **docs/MODO_SIN_AUTENTICACION.md**
   - Corrige las rutas inexistentes `apps/account/` por `apps/accounts/`.
   - Describe con precisión que `SesionInactividadMiddleware` conserva su implementación y omite el control de inactividad cuando `AUTH_DISABLED=True`; no es un middleware no-op general.

3. **docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md**
   - Marca la auditoría inicial de modelos y riesgos como histórica.
   - Actualiza los estados de verificador, publicador, catálogo, instalador y sincronizador para que no contradigan los incrementos posteriores.
   - Distingue explícitamente publicación local de despliegue remoto.

4. **docs/PLAN_PRUEBAS.md**
   - Ordena las cifras históricas de 93, 119, 136 y 138 pruebas.
   - Aclara que son resultados reportados en diferentes líneas base y que el resultado actual debe reproducirse en el commit candidato.
   - Separa pruebas unitarias/automatizadas de aceptación GUI y despliegue.

5. **docs/PLAN_MAESTRO_CODEGUARD.md**
   - Actualiza fecha, alcance integrado y pendientes reales de la Fase 2.
   - Evita marcar como pendientes el cliente HTTP, el publicador local y el instalador que ya existen.

6. **templates/base.html.patch**
   - Eliminado porque el único cambio que contenía (incluir `css/polish.css`) ya está presente en `templates/base.html`. No se eliminó ni modificó la plantilla activa.

## Validación que debe ejecutarse en el entorno del proyecto

Esta intervención se hizo mediante cambios de repositorio. No se ejecutó Python, Django, Electron, PyInstaller ni la GUI en un equipo con las dependencias y sistema gráfico del proyecto. Por ello no se declara que la suite haya pasado como resultado de esta rama.

Desde la raíz del repositorio, con el entorno virtual del proyecto activado y las dependencias de `requirements.txt` instaladas:

```bash
python --version
python -m pip check
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test apps.core apps.accounts apps.audit apps.roadmaps
```

Después, verificar el arranque local y los empaquetados siguiendo los pasos de `docs/PLAN_DESARROLLO.md` y `docs/DISENO_SINCRONIZACION_Y_PUBLICACION.md`.

**No ejecutar `cargar_ascenso --recrear` sobre la base de datos habitual:** puede eliminar progreso asociado. Para pruebas de migración/carga, utilizar un `CODEGUARD_DATA_DIR` temporal y una base de datos desechable.

## Criterios que siguen bloqueando el cierre integral de Fase 2

- Aceptación GUI completa de Electron + Django + Waitress: apertura, navegación por ASCENSO, vista de lección y cierre limpio.
- Distribuidor central desplegado con endpoint HTTPS, hosting, allowlist y claves públicas de producción.
- Prueba de extremo a extremo de actualización firmada, descarga, instalación, rollback e interrupciones.
- Revisión del contenido académico real, fuentes, vigencia y compatibilidad.
- Reproducción de la suite y de las verificaciones de migraciones en el commit que se integre.

## Criterio de seguridad

La sincronización debe permanecer cerrada/fallar de forma segura mientras no estén configurados endpoint, allowlist y claves públicas confiables. No introducir claves privadas, credenciales ni endpoints ficticios en el repositorio.

## Estado de esta intervención

**Correcciones documentales y limpieza de un archivo residual: implementadas en esta rama.**  
**Validación de ejecución de la aplicación: pendiente en el entorno local.**  
**Fase 2: sigue en progreso; no se declara completada.**
