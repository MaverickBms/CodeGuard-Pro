# Revisión de escritorio — Módulo 0.3 «Herramientas»

**Fecha:** 2026-11-24  
**Tipo:** revisión documental y de correspondencia curricular; no es ejecución de comandos ni auditoría de seguridad.  
**Estado:** BORRADOR.

## Alcance

Se revisó la secuencia canónica de ocho temas: Visual Studio Code, terminal, Git, GitHub, navegador/DevTools, Markdown, Draw.io y herramientas de diagramación. Se contrastaron objetivos, ejercicios, entregables, rúbrica, referencias y advertencias de seguridad.

No se ejecutaron comandos en Bash, PowerShell o CMD; no se creó un repositorio de práctica, no se abrió un navegador para inspeccionar tráfico y no se generaron diagramas en diagrams.net.

## Resultado ejecutivo

- Temas canónicos presentes: **8/8**.
- Talleres y ejercicios específicos: **8/8**.
- Proyecto integrador con entregables y rúbrica: **presente**.
- Soluciones orientativas para evaluación de transferencia: **presentes**.
- Ejecución real de comandos/laboratorio: **0**.
- Revisión independiente: **0**.
- Videos verificados: **0**.

## Matriz de revisión

| Tema | Evidencia esperada | Hallazgo | Pendiente |
|---|---|---|---|
| 0.3.1 VS Code | Espacio de trabajo con raíz, extensiones y configuración justificadas | Contenido orientado a contexto de proyecto y editor; diferencia editor de runtime/toolchain | Verificar instrucciones en versión actual de VS Code y al menos un SO |
| 0.3.2 Terminal | Transcripción de comandos con shell, ruta y resultado esperado | Se enfatiza contexto y mínimo privilegio | Probar comandos en Bash y PowerShell por separado; señalar diferencias de sintaxis |
| 0.3.3 Git | Historial con diff, staging y commits explicados | Referencia oficial de Git y distinción entre árbol de trabajo e índice | Ejecutar flujo en repositorio descartable y revisar estado antes/después de cada comando |
| 0.3.4 GitHub | Rama, PR y revisión documentados | Se diferencia remoto/local y colaboración | Validar el flujo en repositorio de práctica sin abrir PR innecesario en proyecto real |
| 0.3.5 DevTools | Registro de solicitud/estilo observado en sitio autorizado | Se advierte que observación de red no demuestra seguridad o rendimiento general | Comprobar pasos en navegador actual y reforzar redacción de datos sensibles/cookies |
| 0.3.6 Markdown | README suficiente para un tercero | Incluye ejemplo y revisión por otra persona | Probar renderizado en GitHub y comprobar enlaces, encabezados y bloques |
| 0.3.7 Draw.io | Dos diagramas con objetivos diferentes y fuente editable | Se diferencia flujo y secuencia; se solicita fuente editable | Verificar archivo fuente, exportación y descripción textual accesible |
| 0.3.8 Herramientas de diagramación | Matriz de elección por formato, colaboración, privacidad y accesibilidad | Criterios adecuados y limitaciones de una imagen exportada | Comparación neutral requiere probar más de una herramienta; no inferir superioridad desde una sola fuente |

## Riesgos y observaciones

1. **Comandos destructivos:** toda instrucción con borrado, sobrescritura, permisos o cambios de configuración debe advertir alcance, confirmar ruta y proponer alternativa reversible. No se considera seguro un comando solo porque aparezca en documentación.
2. **Git:** explicar que `git reset`, `git clean`, `checkout`/ `switch` y operaciones de rebase pueden alterar o descartar trabajo. Las primeras prácticas deben realizarse en un repositorio descartable y con `status`/ `diff` antes de actuar.
3. **GitHub:** no publicar tokens ni secretos en commits, issues, capturas o logs; explicar revisión de permisos y alcance del repositorio.
4. **DevTools:** Network puede mostrar cookies, cabeceras, tokens y datos personales. Usar únicamente sitios propios o expresamente autorizados y sanitizar capturas.
5. **Diagramas:** conservar el archivo editable, exportación y alternativa textual; no incluir arquitectura privada, credenciales ni datos de clientes.
6. **Portabilidad:** comandos y rutas dependen del shell y del sistema operativo. El estudiante debe declarar cuál utiliza.

## Criterios para revisión independiente

- Ejecutar cada comando en un entorno descartable con Bash y PowerShell, registrando versiones.
- Confirmar que las instrucciones no destruyen datos fuera del proyecto de práctica.
- Completar el flujo Git local/remoto y documentar el estado antes y después.
- Verificar los pasos DevTools en una página autorizada y con datos sintéticos.
- Renderizar el README y validar enlaces.
- Abrir y editar la fuente de los diagramas; comprobar que exportación y fuente coinciden.
- Revisar accesibilidad y privacidad de capturas/diagramas.
- Registrar resultados reales, revisor y fecha.

## Límites

El contenido se inspeccionó estáticamente. Las referencias oficiales documentan las herramientas, pero no prueban que el laboratorio esté ejecutado ni que una instrucción funcione sin variación en todos los sistemas. No se asigna APROBADO.

**Estado final:** 0/8 temas con validación práctica independiente; 0 laboratorios ejecutados; 0 videos verificados; 0 aprobaciones y 0 publicaciones.
