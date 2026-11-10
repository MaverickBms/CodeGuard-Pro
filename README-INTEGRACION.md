# CodeGuard Pro — paquete de refinamiento Frontend

Este paquete es una **capa de estilos aditiva** para el frontend existente. No reemplaza Django, Bootstrap, HTMX, Electron ni la lógica de negocio.

## Archivos

- `static/css/polish.css`: refinamiento visual global, dashboard, roadmap, navegación y responsive.
- `templates/base.html.patch`: cambio de una línea para cargar la nueva hoja de estilos.

## Instalación

1. Haz una copia de seguridad o crea una rama de trabajo.
2. Copia `static/css/polish.css` del paquete a `static/css/polish.css` del proyecto.
3. En `templates/base.html`, agrega esta línea inmediatamente después de cargar `layout.css` y antes de `fontawesome.min.css`:

   ```django
   <link rel="stylesheet" href="{% static 'css/polish.css' %}">
   ```

4. Ejecuta `python manage.py collectstatic` si tu configuración lo requiere.
5. Inicia la aplicación y verifica el panel, el roadmap y los formularios con los temas claro, oscuro y alto contraste.

## Criterios de compatibilidad

- Consume variables CSS ya definidas por `themes.css`; no reemplaza las paletas P01–P12.
- No introduce CDN, fuentes remotas, dependencias npm ni JavaScript adicional.
- Mantiene los nombres de clases y los bloques de plantillas actuales.
- Incluye reglas responsive y `prefers-reduced-motion`.

## Alcance y validación

El repositorio fue inspeccionado desde GitHub, pero este paquete no incluye el repositorio completo ni afirma que se haya ejecutado una prueba de integración local. Antes de integrar en producción, verifica visualmente las vistas autenticadas, las pantallas de acceso y los 12 temas en la aplicación Electron.
