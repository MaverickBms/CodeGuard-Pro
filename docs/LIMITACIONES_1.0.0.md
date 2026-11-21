# Limitaciones de CodeGuard Pro 1.0.0

**Fecha:** 2026-11-21
**Regla:** una limitación no se convierte en funcionalidad por aparecer en la
interfaz. Si algo no está implementado, se identifica como no disponible o se
documenta aquí.

## 1. Fuera de alcance de esta versión

- Mundo CodeGuard: personajes, NPCs, criaturas, combate, mapas abiertos,
  misiones e inventario del videojuego. Los PR #15 y #16 no forman parte de esta
  entrega y no se modificaron.
- Laboratorios con ejecución de código.
- Competencias, vigencia y ética como módulos operativos.
- macOS y ARM64.
- Sandbox de código del estudiante.
- Publicación remota de conocimiento en producción.

## 2. Contenido académico

- Hay **1.946 títulos** curriculares, pero solo **8 lecciones** tienen cuerpo
  desarrollado. Las otras **1.938** están pendientes.
- Las 8 lecciones están en **borrador editorial**; no se aprobaron ni publicaron
  automáticamente durante esta misión.
- La etapa 25 no tiene objetivo formal en el documento maestro. No se inventó
  uno; se documenta la ausencia.
- Los 8 videos tienen enlace y metadatos verificados, pero **ninguno** tiene
  revisión pedagógica aprobada. La interfaz lo declara como pendiente.
- No existe revisión humana independiente del módulo 0.1.
- No hay quizzes publicados en un perfil limpio. Los quizzes de ejemplo se cargan
  como borrador mediante comando.

## 3. Evaluaciones y aprendizaje

- Las respuestas abiertas quedan en `requiere_revision`; no se autoaprueban, pero
  tampoco existe todavía una interfaz docente para resolverlas.
- No hay límite configurable de intentos por evaluación.
- El progreso de una lección depende de ejercicios configurados para completarla;
  actualmente solo el módulo 0.1 tiene ejercicios.
- No se ejecuta ni se evalúa dinámicamente código; solo comparaciones estáticas.

## 4. Tutor

- Requiere Ollama y el modelo configurado instalado para respuestas generativas.
- Sin Ollama se usa el fallback determinista de la lección; la interfaz lo indica.
- El tutor no decide aprobaciones.
- La disponibilidad de Ollama depende de un servicio externo local no empaquetado.

## 5. Distribución

### Linux

- El AppImage se verificó en el host de auditoría.
- El montaje FUSE quedó bloqueado en este equipo; se usó extracción
  (`APPIMAGE_EXTRACT_AND_RUN=1`). No se declara verificado el montaje directo en
  todos los equipos.
- La restauración desde el menú de Electron requiere entorno gráfico.

### Windows

- El ciclo NSIS/portable se validó en CI (`windows-latest`), no en hardware
  Windows físico.
- No se probó con antivirus corporativo, políticas de grupo ni hardware real.
- No se declara aceptación física de Windows.

### macOS y ARM64

- No configurados ni validados. No se declara soporte.

## 6. Servicios externos

- La sincronización remota de conocimiento no está operativa: no hay endpoint
  público, allowlist ni claves públicas de producción.
- El cliente falla cerrado y no realiza conexiones sin esa configuración.
- Los enlaces de video abren YouTube en el navegador externo; requieren Internet
  para reproducirse. La lección sigue disponible sin conexión.
- Las fuentes DOI/URL pueden requerir Internet y pueden devolver 403 a clientes
  automatizados.

## 7. Seguridad y entorno

- El modo `AUTH_DISABLED=True` es una decisión de producto para uso local. No hay
  credenciales de acceso.
- Cualquier proceso del mismo usuario puede leer o modificar el perfil. No se
  promete integridad frente al propietario del sistema operativo.
- Si un perfil tiene varias cuentas activas y ninguna marcada como propietario,
  la aplicación falla cerrado y no elige ni eleva ninguna.
- La aplicación no abre puertos fuera de `127.0.0.1`.

## 8. Calidad y documentación

- La suite local tiene 356 pruebas Django y 26 de Electron; no cubre todos los
  flujos visuales posibles.
- El smoke y el responsive se ejecutaron sobre Electron en Linux; no sustituyen
  pruebas manuales en Windows.
- La documentación de arquitectura extendida sigue en la rama `documentation` y
  puede no reflejar cada cambio de esta rama; los documentos de esta carpeta son
  la referencia de 1.0.0.

## 9. Decisiones pendientes del propietario

1. Autorizar la publicación editorial del módulo 0.1.
2. Decidir el alcance del MVP de las 33 etapas (P-002).
3. Aprobar el objetivo propuesto de la etapa 25.
4. Autorizar una revisión pedagógica humana de los 8 videos.
5. Decidir si se amplía el recorrido inicial antes de la entrega.
6. Autorizar o no la aceptación en hardware Windows físico.
7. Definir la infraestructura remota y las claves de firma de producción.

Ninguna de estas decisiones se tomó de forma unilateral.
