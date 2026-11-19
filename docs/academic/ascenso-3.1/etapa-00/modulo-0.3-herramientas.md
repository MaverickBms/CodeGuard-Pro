# Etapa 0 · Módulo 0.3 — Herramientas

**Estado:** borrador didáctico v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 0, apartado 0.3.  
**Temas exactos del roadmap:** Visual Studio Code, Terminal, Git, GitHub, navegador y DevTools, Markdown, Draw.io y herramientas de diagramación.

## Objetivo

Preparar un entorno de trabajo organizado y comprender la función de cada herramienta. Esta introducción no reemplaza la profundización posterior en Git, sistemas operativos, desarrollo web o ingeniería de software.

## Resultados de aprendizaje

Al terminar, podrás explicar para qué sirve cada herramienta, utilizar operaciones iniciales de forma segura, documentar un proyecto y entregar evidencias reproducibles.

## 0.3.1 — Visual Studio Code

Visual Studio Code es un editor de código con extensiones, terminal integrada, búsqueda y depuración. No es un compilador universal: la ejecución depende del lenguaje y de las herramientas instaladas.

- Abre una carpeta de proyecto para conservar el contexto.
- Identifica explorador, editor, búsqueda, control de código fuente y terminal.
- Instala extensiones desde fuentes confiables; revisa editor, permisos y mantenimiento.
- Mantén formato consistente y secretos fuera del repositorio.

**Ejercicio:** crea ascenso-herramientas, ábrela en VS Code y crea README.md y notas/objetivos.md. Registra la estructura.

## 0.3.2 — Terminal

La terminal ejecuta comandos en un shell. Bash, Zsh, PowerShell y CMD no comparten exactamente la misma sintaxis.

Conceptos:
- directorio actual;
- rutas absolutas y relativas;
- listar archivos y cambiar de directorio;
- crear carpetas y archivos;
- consultar ayuda de comandos;
- permisos y privilegios;
- redirección y tuberías.

Evita ejecutar todo como administrador/root. No copies comandos destructivos ni scripts remotos sin entenderlos.

**Ejercicio:** registra sistema operativo y shell. Navega a tu proyecto, lista contenido y crea evidencias/. Explica cada comando.

## 0.3.3 — Git

Git es un sistema distribuido de control de versiones y funciona localmente.

- Working tree: archivos de trabajo.
- Staging area: selección de cambios para el siguiente commit.
- Commit: registro del historial.
- Branch: referencia a una línea de desarrollo.
- Merge: integración de historiales.
- Remote: repositorio remoto configurado.

Flujo inicial: consultar estado, revisar diferencias, seleccionar cambios, crear commit y revisar historial.

No uses reset --hard, clean -fd ni force push sin comprender sus efectos y verificar que existe una copia recuperable.

**Ejercicio:** inicializa Git en una carpeta de práctica, crea dos archivos, registra un commit y examina estado e historial.

## 0.3.4 — GitHub

GitHub aloja repositorios Git y facilita colaboración mediante issues, pull requests, revisiones y automatización.

**Diferencia:** Git es el sistema de control de versiones; GitHub es un servicio de alojamiento y colaboración.

Flujo:
1. Crear o clonar repositorio.
2. Crear rama para un cambio acotado.
3. Realizar commits descriptivos.
4. Publicar la rama.
5. Abrir pull request con contexto y pruebas.
6. Revisar comentarios y checks.
7. Integrar según el flujo autorizado.

Nunca publiques .env, contraseñas, tokens, llaves privadas ni información confidencial.

**Ejercicio:** crea un repositorio de práctica con contenido no sensible, agrega README y realiza un cambio mediante rama y pull request. Puede ser privado.

## 0.3.5 — Navegador y DevTools

DevTools permite inspeccionar páginas web:
- Elements/Inspector: DOM y estilos.
- Console: errores y ejecución de JavaScript.
- Network: solicitudes, respuestas y tiempos.
- Application/Storage: cookies y almacenamiento.
- Performance: actividad y rendimiento.

**Práctica:** abre una página propia o de demostración. Inspecciona un elemento, identifica una regla CSS y revisa una solicitud. No pruebes ni alteres sitios ajenos.

## 0.3.6 — Markdown

Markdown es una sintaxis ligera para documentar proyectos.

- Encabezados: #, ##, ###.
- Énfasis: **negrita** y *cursiva*.
- Listas ordenadas y no ordenadas.
- Enlaces: [texto](URL).
- Código en línea y bloques de código.
- Tablas para datos comparables.

**Ejercicio:** escribe instrucciones de un proyecto ficticio con objetivo, requisitos, instalación, ejecución, resultado esperado y solución de dos problemas.

## 0.3.7 — Draw.io y diagramación

Draw.io (diagrams.net) permite representar procesos y sistemas. La herramienta no valida la arquitectura: las decisiones deben justificarse.

Tipos iniciales:
- flujo: pasos y decisiones;
- componentes: piezas y relaciones;
- despliegue: nodos y entornos;
- entidad-relación: datos y cardinalidades;
- secuencia: mensajes en el tiempo.

Usa un propósito por diagrama, nombres consistentes, leyenda cuando haga falta y conexiones no ambiguas. Conserva fuente editable.

**Ejercicio:** representa «crear una nota de aprendizaje y revisarla» con inicio, actividades, una decisión y dos resultados.

## Laboratorio integrador — Kit de herramientas ASCENSO

Construye ascenso-kit-herramientas con:
- README en Markdown;
- carpeta notas/ con bitácora;
- carpeta diagramas/ con un diagrama editable;
- historial Git de al menos tres commits;
- repositorio remoto con rama y pull request de práctica;
- evidencia de uso de VS Code y terminal;
- captura de DevTools inspeccionando página propia o de demostración.

No incluyas secretos ni archivos innecesarios. Otra persona debe poder comprender el propósito y reproducir los pasos.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| VS Code y organización | 10 |
| Terminal segura y explicada | 15 |
| Historial Git claro | 20 |
| Flujo GitHub | 15 |
| DevTools | 10 |
| Markdown | 15 |
| Diagrama editable y claro | 15 |

Aprobación sugerida: 80/100 y sin secretos expuestos ni comandos destructivos ejecutados sin control.

## Video candidato — Git y GitHub (audio pendiente de verificación)

**[Curso COMPLETO de GIT y GITHUB desde CERO para PRINCIPIANTES — MoureDev by Brais Moure](https://www.youtube.com/watch?v=3GymExBkKjE)**  
Idioma hablado: pendiente de verificación mediante escucha. Pertinencia prevista: explica Git, comandos básicos de terminal, init, status, add, commit, ramas, merge, conflictos, remotos, GitHub, pull requests y Markdown. No aprobar ni recomendar hasta confirmar audio real en español y correspondencia con el contenido.  
Actividad: estudiar las secciones necesarias y realizar el laboratorio en un repositorio separado. No necesitas memorizar todos los comandos en esta etapa; se profundizarán posteriormente.

No se agregan videos genéricos de VS Code, terminal o diagramación en esta entrega: no se ha verificado una pieza concreta que cubra con precisión esos objetivos. Se añadirán solo cuando exista correspondencia temática comprobable.

## Autoevaluación

1. ¿Qué diferencia existe entre Git y GitHub?
2. ¿Qué problema evita el staging area?
3. ¿Por qué debes conocer el directorio actual antes de ejecutar un comando?
4. ¿Qué información permite inspeccionar Network?
5. ¿Qué elementos hacen reproducible un README?
6. ¿Qué diagrama elegirías para representar decisiones de un proceso?

## Referencias

- VS Code: https://code.visualstudio.com/docs
- Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/
- Chrome DevTools: https://developer.chrome.com/docs/devtools/
- Markdown Guide: https://www.markdownguide.org/
- diagrams.net: https://www.drawio.com/doc/
- MoureDev, Git y GitHub: https://www.youtube.com/watch?v=3GymExBkKjE

**Fecha de consulta:** 19-11-2026. Revisar enlaces y contenido antes de aprobar o publicar.
