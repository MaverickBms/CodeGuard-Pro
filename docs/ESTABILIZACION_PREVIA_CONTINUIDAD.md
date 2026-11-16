# Estabilización previa a la continuación del desarrollo

**Fecha:** 15 de noviembre de 2026  
**Rama de trabajo:** `chore/stabilizacion-pre-fase-2`  
**Objetivo:** corregir documentación desactualizada y retirar residuos confirmados sin alterar la lógica de negocio ni los datos.

## Cambios realizados

1. **README.md**
   - Actualiza el estado de sincronización: cliente HTTP, comando, publicador local, instalador y scheduler Electron implementados.
   - Aclara que hosting, endpoint público, allowlist y claves públicas de producción siguen pendientes.
   - Añade `publicar_paquete_conocimiento` y `sincronizar_conocimiento` a la tabla de comandos.
   - Sustituye la cifra obsoleta de 93 pruebas por el resultado inicial reportado (138), pendiente de reproducirse.

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

## Validación ejecutada en el entorno del proyecto — 15-11-2026

El propietario reportó que, en `chore/estabilizacion-pre-fase-2` y Python 3.14.10 desde `.venv`, se ejecutaron correctamente `git fetch origin`, checkout de la rama, `python -m pip check` (sin dependencias rotas), `python manage.py check` (sin incidencias), `python manage.py makemigrations --check --dry-run` (sin cambios) y `python manage.py test apps.core apps.accounts apps.audit apps.roadmaps` (**197 pruebas OK, sin fallos**). Esta validación cubre las pruebas automatizadas de esas aplicaciones y las comprobaciones de Django; no sustituye aceptación GUI ni sincronización remota end-to-end.

## Validación que debe repetirse después de cambios funcionales

La intervención inicial se hizo mediante cambios de repositorio y no ejecutó Python, Django, Electron, PyInstaller ni GUI. Posteriormente, el propietario ejecutó satisfactoriamente las comprobaciones descritas arriba. No se ejecutaron desde esta sesión Electron, PyInstaller ni la GUI.

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
**Validación automatizada Django: reportada satisfactoria (197 pruebas). Aceptación GUI, Electron/Waitress y distribución remota: pendientes.**  
**Fase 2: sigue en progreso; no se declara completada.**
