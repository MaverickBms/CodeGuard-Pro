# Revisión de escritorio — Módulo 0.2 «Investigación técnica»

**Fecha:** 2026-11-24  
**Rama:** `content/ascenso-stage-0-learning-method`  
**Tipo:** inspección documental y de alineación curricular; no equivale a auditoría de seguridad, revisión externa ni ejecución práctica.  
**Estado del registro:** vigente como revisión de escritorio; no constituye aprobación independiente ni validación experimental.

## Alcance

Se revisaron los siete temas del módulo contra el orden curricular: buscar documentación; buscar soluciones a errores; leer Stack Overflow; consultar GitHub; investigar repositorios; diferenciar información verificada de opiniones; formular preguntas técnicas. Se inspeccionaron talleres, evidencias, rúbricas, fuentes y límites de seguridad. Se incorporó una sección de claves modelo con ejemplos explícitamente simulados.

No se clonaron repositorios de terceros, no se ejecutaron scripts, no se hicieron pruebas de vulnerabilidad, no se escucharon los videos y no se evaluó a estudiantes.

## Resultado ejecutivo

- Temas curriculares cubiertos en la ampliación: **7/7**.
- Talleres específicos con procedimiento y evidencia esperada: **7/7**.
- Claves o retroalimentación modelo añadidas: **7/7**.
- Rúbrica de transferencia: **incorporada**.
- Revisión externa: **0**.
- Laboratorios ejecutados: **0**.
- Videos con audio verificado: **0**.

La presencia de un procedimiento no demuestra que el estudiante pueda ejecutarlo con autonomía. La evaluación práctica y la revisión independiente siguen pendientes.

## Matriz por tema

| Tema oficial | Producto que demuestra desempeño | Hallazgo de escritorio | Riesgo o mejora pendiente |
|---|---|---|---|
| Buscar documentación | Ficha con versión, firma/API, parámetros, fuente y límites | El taller exige localizar documentación de la versión correspondiente y distinguir tutorial de referencia oficial. | Revisar un ejemplo real con versión fijada y validar que los enlaces de referencia sigan vigentes. |
| Buscar soluciones a errores | Bitácora de error, dos hipótesis, prueba discriminante y conclusión | El taller propone preservar mensaje, contexto y cambiar una variable a la vez; se añadió caso simulado de intérprete/entorno Python. | Reforzar la advertencia de no compartir rutas privadas y no instalar/actualizar dependencias a ciegas. |
| Leer Stack Overflow | Ficha con fecha, versión, estado de API y contraste primario | Se distinguen votos/aceptación de garantía técnica y se incluye un veredicto orientativo. | Para una evaluación real, seleccionar una respuesta concreta y verificar el estado actual de su API. |
| Consultar GitHub | Cadena issue → PR → commit → release | El taller advierte que cerrar una issue no demuestra que una corrección esté distribuida. | Añadir un caso real versionado en revisión futura, sin atribuir una solución sin evidencia. |
| Investigar repositorios | Matriz de licencia, mantenimiento, pruebas, dependencias y seguridad | Se diferencia popularidad de mantenimiento, licencia y seguridad. | Una revisión documental no es análisis de código ni auditoría de cadena de suministro. Mantener explícito ese límite. |
| Diferenciar hechos y opiniones | Matriz de afirmaciones con condiciones, métrica y evidencia | El ejemplo de rendimiento muestra por qué una comparación necesita carga, versiones, hardware y métrica. | Añadir práctica con datos medidos solo cuando exista entorno y registro de ejecución. |
| Formular preguntas técnicas | Reporte reproducible que un tercero pueda seguir | El taller propone plantilla completa y prueba de reproducción por otra persona. | Requiere piloto con un compañero/docente; no se ha comprobado reproducibilidad externa. |

## Hallazgos transversales

### Seguridad y privacidad

El módulo contiene advertencias útiles sobre secretos, repositorios desconocidos y ejecución aislada. En futuras versiones conviene convertirlas en controles observables: inspeccionar scripts de instalación, permisos, workflows y dependencias; no ejecutar artefactos no confiables en el equipo habitual; usar datos sintéticos; y registrar el entorno aislado utilizado. No se debe presentar la inspección superficial de un README como evaluación de seguridad.

### Calidad de evidencia

La jerarquía de fuentes es una orientación, no una regla mecánica: una fuente oficial puede ser incompleta, una issue puede contener evidencia valiosa y una respuesta comunitaria puede revelar un caso que la documentación no cubre. La decisión debe basarse en alcance, fecha, versión, evidencia y posibilidad de reproducción.

### Versiones y releases

El material acierta al distinguir issue cerrada, PR integrado y versión publicada. Esta distinción debe mantenerse en cualquier futura guía: no afirmar que un defecto está corregido en una release sin confirmar que el cambio llegó a ella.

### Rúbricas

El módulo contiene una rúbrica de proyecto y una rúbrica analítica de transferencia con pesos distintos. Debe definirse cuál es formativa y cuál determina el resultado, para evitar puntuaciones contradictorias. Ninguna rúbrica local sustituye las reglas oficiales de finalización de ASCENSO.

### Recursos audiovisuales

Los dos videos continúan como candidatos. No se escuchó su audio en esta revisión; el idioma hablado, duración, contenido real y correspondencia exacta con los objetivos permanecen sin verificar.

## Criterios de salida para revisión independiente

1. Confirmar la correspondencia exacta de los siete títulos con el JSON maestro.
2. Comprobar enlaces y versiones de la documentación primaria.
3. Ejecutar los pasos informativos de diagnóstico en un entorno de práctica limpio, registrando comandos y resultados reales.
4. Validar con un caso real la cadena issue/PR/commit/release.
5. Revisar una licencia real y distinguir el análisis legal del técnico.
6. Hacer que una persona externa reproduzca un reporte sin asistencia oral.
7. Revisar privacidad, accesibilidad y claridad de todas las plantillas.
8. Escuchar y mapear los videos antes de recomendarlos.
9. Registrar revisor, fecha, hallazgos, correcciones y re-verificación; no inventar firmas.

## Seguimiento de iteración

Se añadieron claves modelo para los siete temas y una lista de control de calidad de fuentes. Los casos se identifican expresamente como simulados; no se atribuyen a repositorios o incidencias reales. Los comandos de consulta de Python se muestran como ejemplos didácticos y no se ejecutaron en esta sesión.

**Estado final:** módulo en base de trabajo activa; 0/7 temas con revisión independiente completa; 0 laboratorios ejecutados; 0 videos verificados; 0 aprobaciones y 0 publicaciones.
