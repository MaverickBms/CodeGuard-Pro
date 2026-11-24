# Etapa 0 · Módulo 0.3 — Herramientas

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · referencia operativa vigente de la lección 0.3. No implica publicación ni aprobación editorial.  
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

## Apéndice didáctico — Draw.io y diagramación

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


---

## Profundización didáctica — versión 0.2.0 (24-11-2026)

Esta ampliación mantiene los ocho temas oficiales y convierte las instrucciones iniciales en tareas observables. Los comandos se presentan como ejemplos de referencia; deben adaptarse al shell y al sistema operativo declarados por el estudiante. No se afirma que se hayan ejecutado en esta entrega.

### 0.3.1 — Visual Studio Code: preparar un espacio de trabajo verificable

**Objetivos específicos**
- distinguir editor, terminal, extensiones y depurador;
- abrir una carpeta de proyecto y reconocer su raíz;
- localizar archivos y buscar texto sin alterar el proyecto;
- justificar la instalación de una extensión.

**Recorrido guiado**
1. Crea una carpeta de práctica sin información privada.
2. Abre la carpeta completa en VS Code, no solo un archivo suelto.
3. Identifica Explorer, Search, Source Control, Run and Debug y Terminal.
4. Abre README.md y crea una nota con fecha, objetivo y próximos pasos.
5. Abre la paleta de comandos y localiza «Preferences: Open Settings».
6. Revisa las extensiones instaladas; no instales una extensión solo porque un tutorial la exige.
7. Antes de instalar, verifica editor, identificador, permisos, repositorio de origen, actividad y política de privacidad.

**Ejemplo resuelto:** un archivo Java no se ejecuta porque el estudiante solo instaló VS Code. El editor no sustituye JDK ni herramientas de compilación. La investigación correcta separa editor, runtime/SDK, extensión de lenguaje y configuración del proyecto.

**Ejercicio:** entrega un inventario con versión de VS Code, sistema operativo, extensiones imprescindibles y razón de cada una. No incluyas capturas que revelen rutas personales, nombres de usuario o secretos.

### 0.3.2 — Terminal: trabajar con contexto y mínimo privilegio

La terminal ejecuta un shell; el shell interpreta comandos. Los nombres y opciones varían entre Bash/Zsh, PowerShell y CMD. No copies una secuencia de un shell a otro sin traducirla y comprobarla.

**Comprobaciones iniciales**
- Bash/Zsh: `pwd`, `ls`, `whoami`, `command -v git`
- PowerShell: `Get-Location`, `Get-ChildItem`, `$env:USERNAME`, `Get-Command git`
- CMD: `cd`, `dir`, `whoami`, `where git`

**Secuencia de práctica no destructiva**
1. Consulta el directorio actual.
2. Crea una carpeta de práctica dentro de un directorio propio.
3. Entra en ella y confirma la ruta.
4. Crea un archivo de texto con una nota.
5. Lista los archivos y lee el contenido.
6. Regresa al directorio anterior y explica qué cambió.

Ejemplos de creación:
- Bash/Zsh: `mkdir -p ascenso-terminal` y `cd ascenso-terminal`
- PowerShell: `New-Item -ItemType Directory -Name ascenso-terminal` y `Set-Location ascenso-terminal`
- CMD: `mkdir ascenso-terminal` y `cd ascenso-terminal`

**Advertencia:** no ejecutes `rm -rf`, `del /s`, `Remove-Item -Recurse`, comandos de formateo ni instrucciones que descarguen y ejecuten scripts remotos como parte de una primera práctica. Comprueba siempre el destino y los privilegios.

**Ejercicio:** repite el recorrido en el shell disponible. Adjunta una transcripción sin datos personales y explica qué comandos son específicos del shell.

### 0.3.3 — Git: entender el ciclo antes de registrar cambios

Git separa tres estados importantes:
- árbol de trabajo: cambios en archivos;
- índice/staging: selección preparada para el próximo commit;
- historial: commits confirmados.

**Laboratorio guiado**
1. Crea una carpeta nueva y ejecuta `git init`.
2. Crea README.md con el propósito del proyecto.
3. Ejecuta `git status --short` y describe el estado.
4. Ejecuta `git diff` (todavía no habrá cambios preparados).
5. Añade el archivo con `git add README.md`.
6. Ejecuta `git diff --cached` para inspeccionar exactamente lo que entrará en el commit.
7. Crea un commit con mensaje descriptivo.
8. Ejecuta `git log -1 --oneline` y `git status`.

**Ejemplo de razonamiento:** si `git diff` no muestra el cambio después de ejecutar `git add`, no significa que el cambio haya desaparecido; puede estar en el índice. Se comprueba con `git diff --cached`.

**Ejercicio de aplicación:** modifica una línea, añade solo ese archivo, inspecciona el diff preparado y crea un segundo commit. Explica qué diferencia hay entre el primer y el segundo snapshot.

**Seguridad:** no practiques con el repositorio real del trabajo. No uses `reset --hard`, `clean`, `push --force` ni reescritura de historial como ejercicios introductorios.

### 0.3.4 — GitHub: colaborar sin confundir remoto y local

**Flujo de práctica**
1. Crea un repositorio privado o público con contenido no sensible.
2. Configura el remoto siguiendo la URL que GitHub muestra para ese repositorio.
3. Crea una rama para una modificación concreta.
4. Realiza un commit y publica la rama.
5. Abre un pull request con propósito, alcance, pruebas y limitaciones.
6. Revisa el diff en GitHub.
7. Responde a una observación y actualiza la rama.
8. No integres el PR si el objetivo del ejercicio es practicar revisión; la integración puede quedar pendiente.

**Ejemplo resuelto:** una rama aparece en el equipo pero no en GitHub. La explicación más probable no debe asumirse sin comprobar: primero verifica `git branch --show-current`, `git remote -v` y el estado de publicación. Una rama local no se convierte automáticamente en una rama remota.

**Ejercicio:** entrega el enlace al PR de práctica y una lista de archivos modificados. El repositorio no debe contener tokens, claves privadas, archivos .env ni datos de terceros.

### 0.3.5 — Navegador y DevTools: observar antes de intervenir

Utiliza una página local o un sitio de demostración autorizado.

**Recorrido**
1. Abre DevTools y selecciona Elements/Inspector.
2. Selecciona un elemento y registra qué regla CSS determina una propiedad visible.
3. Abre Console y distingue errores, advertencias y mensajes informativos.
4. Abre Network, recarga y selecciona una solicitud.
5. Registra método, URL sin parámetros sensibles, estado HTTP, tipo de recurso y duración observada.
6. Abre Application/Storage y reconoce cookies y almacenamiento; no copies valores de sesión.
7. Cierra DevTools y explica qué observación puede hacerse sin modificar la página.

**Límite importante:** los datos de Network dependen de caché, conexión, extensiones y estado de la página. Una medición aislada no demuestra rendimiento general. No inspecciones sesiones ajenas ni alteres servicios de terceros.

**Ejercicio:** documenta una solicitud de una página propia: qué la inicia, qué respuesta recibió y qué hipótesis podrías investigar si falla.

### 0.3.6 — Markdown: documentar para otra persona

Crea un README con:
- propósito y alcance;
- requisitos y versiones;
- instalación;
- ejecución;
- resultado esperado;
- estructura de carpetas;
- pruebas;
- solución de problemas;
- licencia o nota de autoría cuando corresponda.

**Ejemplo mínimo**
```markdown
# Proyecto de práctica

## Propósito
Registrar notas técnicas reproducibles.

## Requisitos
- Git instalado.
- Un editor de texto.

## Uso
1. Clonar o descargar el proyecto.
2. Abrir la carpeta.
3. Leer las instrucciones de cada actividad.

## Resultado esperado
Una bitácora con fecha, pasos y evidencias no sensibles.
```

**Ejercicio:** intercambia el README con otra persona. Si necesita preguntarte cómo empezar, registra qué instrucción falta y mejora el documento.

### 0.3.7 — Draw.io: elegir el diagrama por la pregunta

Antes de dibujar, define qué pregunta debe responder el diagrama:
- flujo: ¿qué pasos y decisiones ocurren?;
- secuencia: ¿quién envía qué mensaje y en qué orden?;
- componentes: ¿qué piezas existen y cómo se relacionan?;
- despliegue: ¿en qué nodos se ejecutan?;
- entidad-relación: ¿qué datos se relacionan y con qué cardinalidad?

**Ejemplo resuelto:** para representar el registro de una nota, un diagrama de flujo es apropiado si interesan validación y decisiones; un diagrama de secuencia es más apropiado si interesa el intercambio entre navegador, API y base de datos. Un único diagrama no tiene que contestar todas las preguntas.

**Ejercicio:** crea dos diagramas del mismo caso con propósitos distintos. Incluye título, alcance, leyenda si hay notación no obvia y fuente editable.


### 0.3.8 — Herramientas de diagramación

**Objetivos específicos**
- seleccionar una herramienta de diagramación según el tipo de representación y el flujo de colaboración;
- comparar facilidad de edición, control de versiones, exportación, accesibilidad y portabilidad;
- mantener el archivo fuente además de una exportación visual;
- explicar los límites de un diagrama y evitar que sustituya una especificación necesaria.

**Criterios de selección**
1. Tipo de diagrama requerido: flujo, secuencia, componentes, despliegue o datos.
2. Audiencia: equipo técnico, usuario, docente o persona evaluadora.
3. Colaboración: edición simultánea, comentarios, permisos y control de cambios.
4. Mantenibilidad: posibilidad de editar el original, revisar diferencias y conservar historial.
5. Interoperabilidad: formatos de exportación y posibilidad de reutilizar el archivo fuente.
6. Privacidad: ubicación de almacenamiento, acceso compartido y tratamiento de información sensible.
7. Accesibilidad: contraste, tamaño de texto, lectura y alternativa textual.

**Ejemplo resuelto:** un diagrama de arquitectura que cambia con frecuencia necesita una fuente editable y un proceso de revisión. Una imagen PNG aislada facilita la lectura, pero dificulta rastrear cambios. La entrega recomendada conserva el archivo fuente y exporta una imagen o PDF para consulta.

**Ejercicio:** toma el proceso de registro de una nota y produce una versión de flujo y otra de secuencia. Para cada una registra herramienta, formato fuente, formato de entrega, audiencia, ventajas y una limitación.

**Criterios de dominio:** la herramienta se elige por necesidad explícita; el archivo fuente puede abrirse y editarse; el diagrama tiene alcance y leyenda; la exportación coincide con la fuente; se proporciona descripción textual cuando la imagen no sea accesible.

**Errores frecuentes:** elegir una herramienta por popularidad, exportar solo una imagen y perder la fuente, mezclar varios propósitos en un solo diagrama, usar conectores ambiguos o incluir secretos en diagramas compartidos.

**Referencia:** diagrams.net, documentación oficial: https://www.drawio.com/doc/ (consultada 2026-11-24). La selección de herramienta es una decisión contextual; esta fuente documenta diagrams.net, no una comparación neutral de todos los productos.

## Proyecto práctico de módulo — Kit de herramientas ASCENSO, versión ampliada

**Contexto:** un estudiante debe entregar a otra persona un espacio de trabajo que pueda comprenderse y reproducirse sin asistencia verbal.

**Entregables**
1. repositorio con README y notas;
2. estructura de carpetas explicada;
3. dos commits con cambios deliberados y diff inspeccionado;
4. rama y pull request de práctica;
5. inventario de herramientas y versiones;
6. transcripción de terminal adaptada al shell usado;
7. evidencia de inspección de una página autorizada con DevTools;
8. diagrama editable con propósito explícito;
9. reflexión de seguridad sobre secretos, permisos y archivos excluidos.

### Rúbrica analítica (100 puntos)

| Criterio | Evidencia | Peso |
|---|---|---:|
| Entorno y editor | Versiones, carpeta raíz y extensiones justificadas | 10 |
| Terminal | Comandos apropiados al shell y rutas verificadas | 15 |
| Git | Estado, diff, staging e historial explicados | 20 |
| GitHub | Rama, PR y revisión comprensibles | 15 |
| DevTools | Solicitud y estilos observados sin exponer datos | 10 |
| Markdown | README suficiente para un tercero | 15 |
| Diagramación | Tipo de diagrama adecuado y archivo editable | 10 |
| Seguridad | Sin secretos y con mínimo privilegio | 5 |

**Dominio:** mínimo sugerido 80/100, sin exposición de secretos ni uso de comandos destructivos sin control. La rúbrica no sustituye una revisión docente.

## Evaluación de transferencia

Responde con evidencia:
1. ¿Por qué VS Code no sustituye un SDK o runtime?
2. ¿Qué cambia entre `git diff` y `git diff --cached`?
3. ¿Qué evidencia demuestra que una rama existe en remoto?
4. ¿Por qué una solicitud HTTP vista en DevTools no basta para afirmar que una API es segura?
5. ¿Qué diferencia de propósito hay entre un diagrama de flujo y uno de secuencia?
6. ¿Qué información mínima permite que otra persona ejecute un proyecto?

**Soluciones orientativas**
1. El editor ofrece herramientas de edición; la compilación o ejecución depende del toolchain del lenguaje.
2. El primero compara el árbol de trabajo con el índice; el segundo muestra lo preparado en el índice frente al último commit.
3. La rama aparece en el remoto consultado o se confirma con la referencia remota; su existencia local no basta.
4. DevTools observa tráfico de una sesión; no evalúa todos los controles, roles, entradas ni condiciones de seguridad.
5. El flujo representa pasos/decisiones; la secuencia representa mensajes ordenados entre participantes.
6. Requisitos, versiones, pasos, configuración no secreta, comando de ejecución y resultado esperado.

## Fuentes técnicas y fecha de consulta

- Visual Studio Code, documentación: https://code.visualstudio.com/docs — documentación oficial del editor; consultar la guía específica del lenguaje y versión.
- Git, documentación: https://git-scm.com/doc — documentación oficial del sistema de control de versiones.
- Git, `git-diff`: https://git-scm.com/docs/git-diff — referencia de comparación entre árbol de trabajo, índice y commits.
- GitHub Docs, repositorios: https://docs.github.com/en/repositories — documentación oficial de alojamiento y colaboración.
- GitHub Docs, búsqueda: https://docs.github.com/en/search-github — documentación oficial de búsqueda.
- Chrome DevTools: https://developer.chrome.com/docs/devtools/ — documentación oficial de DevTools.
- Markdown Guide: https://www.markdownguide.org/ — guía comunitaria de sintaxis; no es una especificación única de todos los renderizadores.
- diagrams.net: https://www.drawio.com/doc/ — documentación del producto.

Consulta de enlaces: 2026-11-24. La disponibilidad de funciones puede variar por versión, sistema operativo y configuración.

## Registro de verificación

- Revisión documental: ampliación alineada con los ocho temas del JSON maestro.
- Comandos: ejemplos estáticos revisados conceptualmente; no se declara ejecución en Bash, PowerShell ni CMD.
- Laboratorio: diseñado, no ejecutado.
- Evidencias de estudiantes: no disponibles.
- Videos: no se añade ni verifica ninguno.
- Estado: BORRADOR; requiere revisión técnica, pedagógica, práctica y editorial independiente.
