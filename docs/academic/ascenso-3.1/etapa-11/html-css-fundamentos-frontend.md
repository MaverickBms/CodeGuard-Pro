# Etapa 11 — HTML y CSS: fundamentos profesionales del frontend

**Estado de trabajo:** BASE DE TRABAJO ACTIVA · v0.1.0.  
**Alineación:** ASCENSO 3.1, Etapa 11.  
**Prioridad oficial:** P1 · Obligatoria.  
**Objetivo oficial:** construir interfaces web correctamente estructuradas, accesibles y adaptables.

## Temario oficial

### 11.1. HTML
Estructura de documentos; DOCTYPE; head; body; etiquetas; atributos; HTML semántico; headings; sections; articles; header; footer; nav; forms; inputs; selects; textareas; tables; multimedia; SVG; Canvas.

### 11.2. Accesibilidad
WCAG; ARIA; navegación por teclado; etiquetas accesibles; contraste; lectores de pantalla; formularios accesibles; HTML semántico.

### 11.3. CSS
Selectores; cascade; specificity; inheritance; box model; display; position; Flexbox; Grid; pseudoclases; pseudoelementos; variables; media queries; responsive design; animations; transitions; transformations.

### 11.4. Diseño de interfaces
Jerarquía visual; espaciado; tipografía; layouts; componentes; design systems; consistencia visual; mobile-first.

### 11.5. SEO
Metadatos; títulos; descripciones; estructura semántica; indexación; datos estructurados (introducción).

**Proyecto oficial:** construir una web profesional responsive, accesible y con varias páginas.

## Resultados de aprendizaje

Podrás construir documentos HTML válidos y semánticos; seleccionar elementos nativos adecuados; crear formularios y tablas comprensibles; evaluar accesibilidad con teclado y lector de pantalla; aplicar cascada, especificidad y herencia; construir layouts con Flexbox y Grid; adaptar interfaces con media queries; aplicar tipografía, espaciado y jerarquía; crear componentes consistentes; y preparar metadatos y estructura para indexación.

## 11.1 — HTML

### Estructura de documento

HTML describe la estructura y el significado del contenido web. Un documento mínimo contiene declaración DOCTYPE, elemento raíz, metadatos en head y contenido visible en body.

Ejemplo:

    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Catálogo de biblioteca</title>
        <meta name="description" content="Consulta el catálogo de la biblioteca.">
      </head>
      <body>
        <header>
          <h1>Biblioteca</h1>
          <nav aria-label="Navegación principal">
            <a href="/">Inicio</a>
            <a href="/catalogo">Catálogo</a>
          </nav>
        </header>
        <main>
          <section aria-labelledby="catalogo-titulo">
            <h2 id="catalogo-titulo">Catálogo</h2>
            <p>Explora los libros disponibles.</p>
          </section>
        </main>
        <footer><p>Información de la biblioteca</p></footer>
      </body>
    </html>

El atributo lang declara el idioma principal. El viewport ayuda a que el navegador adapte el layout al ancho del dispositivo. El title identifica la página en pestañas y resultados.

### Etiquetas y atributos

Los elementos representan estructura o contenido; los atributos configuran o describen elementos. Utiliza atributos válidos para el elemento y evita crear atributos inventados cuando existe data-* para datos personalizados.

Los elementos deben anidarse correctamente. No utilices etiquetas solo por su apariencia: la presentación corresponde principalmente a CSS.

### HTML semántico

Headings, header, nav, main, section, article y footer comunican estructura. Utiliza headings en una jerarquía lógica; no elijas h1, h2 o h3 solo por tamaño visual.

- header: contenido introductorio o cabecera de una sección/página.
- nav: conjunto importante de enlaces de navegación.
- main: contenido principal de la página.
- section: sección temática, normalmente con encabezado.
- article: contenido autónomo que puede distribuirse por separado.
- footer: información de cierre de página o sección.

No es necesario usar todas las etiquetas en cada página. Selecciona según el significado real.

### Forms, inputs, selects y textareas

Los formularios recogen datos. Cada control debe tener una etiqueta asociada, instrucciones y mensajes de error comprensibles. Selecciona el tipo de input apropiado para el dato. Utiliza required y restricciones nativas cuando correspondan, sin depender solo de ellas para validación del servidor.

Ejemplo conceptual:

    <form action="/buscar" method="get">
      <label for="termino">Buscar libro</label>
      <input id="termino" name="q" type="search" required>
      <button type="submit">Buscar</button>
    </form>

No uses placeholder como sustituto de label. Un select debe tener opciones claras; textarea es adecuado para texto multilínea.

### Tables

Utiliza tablas para datos tabulares, no para maquetar páginas. Incluye encabezados adecuados y asocia celdas cuando la tabla sea compleja. En tablas extensas, proporciona caption y estructura que permita comprender filas y columnas.

### Multimedia, SVG y Canvas

Imágenes deben incluir texto alternativo apropiado según propósito: descriptivo si aportan información, vacío si son decorativas. Audio y video requieren controles y alternativas accesibles según contenido.

SVG describe gráficos vectoriales escalables y puede incluir título/descripcion accesibles según contexto. Canvas ofrece una superficie de dibujo mediante scripts; el contenido visual no se vuelve accesible automáticamente. Proporciona alternativa semántica y controles equivalentes.

## 11.2 — Accesibilidad

### WCAG

WCAG organiza recomendaciones alrededor de cuatro principios: perceptible, operable, comprensible y robusto. Los criterios de conformidad tienen niveles A, AA y AAA. El nivel aplicable depende del requisito del producto o normativa; no afirmes conformidad sin evaluación.

### ARIA

ARIA añade semántica y estados accesibles cuando HTML nativo no basta. Regla práctica: prefiere HTML nativo antes de añadir roles ARIA. ARIA no corrige automáticamente interacción defectuosa ni hace accesible un componente por asignarle un role.

No sobrescribas roles y nombres accesibles nativos sin una razón técnica.

### Navegación por teclado

Toda funcionalidad interactiva debe poder utilizarse con teclado cuando corresponda. Comprueba:
- orden de foco lógico;
- foco visible;
- ausencia de trampas;
- activación mediante teclas esperadas;
- diálogo/modal con gestión correcta de foco;
- posibilidad de cerrar o abandonar componentes.

No elimines outline sin reemplazarlo por un indicador perceptible.

### Etiquetas, contraste y lectores de pantalla

Cada control necesita nombre accesible. El texto visible y el nombre anunciado deben ser coherentes. El contraste debe permitir distinguir texto y componentes; evalúa también estados hover, focus, disabled y error.

Un lector de pantalla interpreta semántica, roles, nombres, estados y relaciones. Prueba la página con tecnologías de asistencia cuando sea posible; un validador automático no detecta todos los problemas.

### Formularios accesibles

Asocia label, instrucciones y errores al control. No comuniques errores solo con color. Sitúa mensajes cerca del campo, identifica el problema y explica cómo corregirlo. Conserva datos introducidos cuando haya error y mueve el foco de forma razonable sin desorientar.

### Lista de comprobación

- estructura semántica y headings;
- idioma declarado;
- nombres accesibles;
- navegación por teclado;
- foco visible;
- contraste;
- zoom y reflow;
- formularios con etiquetas y errores;
- alternativas para contenido no textual;
- tablas con encabezados;
- mensajes de estado anunciables;
- pruebas con lector de pantalla.

## 11.3 — CSS

### Selectores, cascade, specificity e inheritance

CSS aplica reglas a elementos. Los selectores identifican objetivos; la cascada resuelve declaraciones en conflicto considerando origen, importancia, capas, especificidad y orden. La especificidad compara selectores según sus componentes, pero no es el único factor de la cascada.

La herencia permite que algunas propiedades se transmitan desde ancestros; no todas las propiedades se heredan.

Evita abusar de !important y selectores demasiado específicos. Mantén estilos predecibles y reutilizables.

### Box Model

El modelo de caja considera contenido, padding, border y margin. Con content-box, width/height describen el contenido; con border-box, incluyen padding y border. Muchos proyectos aplican box-sizing: border-box globalmente para facilitar cálculos.

### Display y Position

Display define cómo participa un elemento en el layout, por ejemplo block, inline, inline-block, flex, grid o none. Position define posicionamiento static, relative, absolute, fixed o sticky según contexto.

No uses position absolute para construir todo el layout: puede sacar elementos del flujo y provocar superposiciones en pantallas pequeñas.

### Flexbox

Flexbox organiza elementos en una dimensión principal y una transversal. Es adecuado para filas o columnas, alineación, distribución y espacios entre elementos. Comprende flex-direction, justify-content, align-items, flex-wrap, gap, flex-grow, flex-shrink y flex-basis.

### Grid

CSS Grid organiza layouts en dos dimensiones con filas y columnas. Permite definir tracks, áreas, gaps y alineación. Es útil para estructuras de página y colecciones que necesitan control simultáneo de ambas dimensiones.

No elijas Flexbox o Grid por moda: utiliza el modelo que describa mejor el problema.

### Pseudoclases y pseudoelementos

Las pseudoclases seleccionan elementos según estado o relación, como hover, focus-visible, checked o first-child. Los pseudoelementos representan partes o contenido generado, como before, after y placeholder. El contenido generado no debe ser el único lugar donde se comunica información esencial.

### Variables CSS

Custom properties permiten definir valores reutilizables y pueden variar según cascada y ámbito. Son útiles para tokens de color, espacio, tipografía y temas. Nombra tokens por propósito, no solo por color literal.

### Media Queries y responsive design

Media queries aplican reglas según características del entorno, como ancho, orientación o preferencias de movimiento. Diseña desde contenido y restricciones reales; no dependas de una lista rígida de dispositivos.

Responsive design debe considerar:
- reflow sin scroll horizontal innecesario;
- imágenes y medios flexibles;
- tipografía legible;
- navegación utilizable;
- controles táctiles adecuados;
- tablas y contenido ancho con estrategia clara;
- preferencias de movimiento reducido.

### Animations, transitions y transformations

Transitions suavizan cambios entre estados; animations definen secuencias mediante keyframes; transformations modifican visualmente posición, escala, rotación o inclinación sin alterar necesariamente el flujo normal.

Respeta prefers-reduced-motion. No uses animación que distraiga, cause malestar o comunique estado únicamente por movimiento.

## 11.4 — Diseño de interfaces

### Jerarquía visual

La jerarquía ayuda a reconocer qué es principal, secundario y accionable. Se construye mediante tamaño, peso, contraste, posición, agrupación y espacio. La jerarquía debe reflejar la importancia real del contenido.

### Espaciado y tipografía

Define una escala de espaciado consistente. La tipografía debe priorizar legibilidad, jerarquía y compatibilidad. Limita familias y variantes; controla longitud de línea, altura de línea y contraste.

### Layouts y componentes

Un layout organiza regiones de la página. Los componentes encapsulan patrones de interfaz reutilizables. Un componente debe tener propósito, estados, comportamiento y API comprensibles.

Documenta estados: default, hover, focus, active, disabled, loading, empty, error y success cuando correspondan.

### Design Systems y consistencia visual

Un design system reúne principios, tokens, componentes, patrones y documentación. Evita crear variantes casi idénticas sin una razón. Los tokens deben expresar decisiones de diseño y facilitar cambios globales.

### Mobile-first

Mobile-first comienza por la experiencia con restricciones de espacio y amplía progresivamente. No significa diseñar solo para móviles ni ocultar funciones importantes. Prioriza contenido, navegación y acciones esenciales y verifica en tamaños intermedios y grandes.

## 11.5 — SEO

### Metadatos, títulos y descripciones

Cada página debe tener title único, descriptivo y alineado con su contenido. La meta description resume la página y puede influir en el fragmento mostrado, aunque el buscador puede elegir otro texto. Los metadatos no garantizan posicionamiento.

### Estructura semántica e indexación

Los buscadores descubren e interpretan páginas mediante enlaces, contenido, metadatos y otras señales. Facilita rastreo con navegación clara, enlaces descriptivos, URLs estables y contenido accesible.

Robots directives, canonical y sitemap deben configurarse según la arquitectura real. No bloquees por error páginas que deban indexarse ni publiques contenido privado pensando que un archivo robots.txt lo protege.

### Datos estructurados (introducción)

Los datos estructurados describen entidades y propiedades mediante vocabularios como Schema.org y formatos compatibles, por ejemplo JSON-LD. Deben corresponder al contenido visible y cumplir las directrices del buscador. No inventes reseñas, precios, disponibilidad o entidades para manipular resultados.

## Proyecto oficial — Sitio web profesional responsive

### Alcance

Construye un sitio de varias páginas para un servicio o proyecto ficticio. Debe incluir navegación, contenido semántico, formulario accesible y diseño adaptable.

### Requisitos

1. Página de inicio con propuesta de valor clara.
2. Página de información/servicios.
3. Página de catálogo o contenido.
4. Página de contacto con formulario accesible.
5. Navegación consistente y enlaces funcionales.
6. HTML semántico y headings coherentes.
7. CSS con tokens, Flexbox y Grid según corresponda.
8. Responsive design y pruebas de reflow.
9. Estados visibles de interacción y foco.
10. Metadatos y títulos únicos por página.
11. Datos estructurados solo cuando el contenido lo justifique.
12. Informe de accesibilidad y correcciones.

### Entregables

- código fuente HTML/CSS;
- mapa de páginas y navegación;
- inventario de componentes;
- escala de tipografía y espaciado;
- capturas en varios anchos;
- checklist WCAG y evidencias;
- pruebas de teclado;
- pruebas de formulario;
- auditoría de metadatos;
- README con ejecución y limitaciones.

### Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| HTML semántico y estructura | 15 |
| Accesibilidad y teclado | 20 |
| CSS, cascada y layout | 20 |
| Responsive design | 15 |
| Jerarquía visual y consistencia | 15 |
| SEO técnico básico | 10 |
| Documentación y pruebas | 5 |

## Ejercicios de comprensión

1. ¿Qué diferencia hay entre HTML y CSS?  
   **Respuesta:** HTML expresa estructura/semántica; CSS define presentación y layout.

2. ¿Para qué sirve DOCTYPE?  
   **Respuesta:** declara el tipo de documento y ayuda al navegador a utilizar el modo estándar.

3. ¿Por qué no debe usarse placeholder como label?  
   **Respuesta:** puede desaparecer, no siempre proporciona nombre persistente y no sustituye una etiqueta asociada.

4. ¿Qué diferencia hay entre section y div?  
   **Respuesta:** section representa una sección temática; div es un contenedor genérico sin semántica propia.

5. ¿Qué es especificidad?  
   **Respuesta:** un componente de la cascada para resolver conflictos entre selectores, junto con otros factores.

6. ¿Cuándo elegir Flexbox frente a Grid?  
   **Respuesta:** Flexbox suele resolver distribución unidimensional; Grid controla filas y columnas en dos dimensiones.

7. ¿ARIA sustituye HTML semántico?  
   **Respuesta:** no; se prefiere HTML nativo y ARIA solo cuando hace falta semántica adicional.

8. ¿Qué significa foco visible?  
   **Respuesta:** que el usuario de teclado puede identificar claramente el elemento que recibirá la interacción.

9. ¿Responsive design es solo reducir el tamaño?  
   **Respuesta:** no; adapta estructura, navegación, tipografía y contenido a distintas condiciones.

10. ¿Los datos estructurados garantizan un resultado enriquecido?  
    **Respuesta:** no; deben cumplir requisitos y el buscador decide su presentación.

## Autoevaluación práctica

Navega todo el sitio sin ratón; completa el formulario con teclado; revisa el nombre accesible de cada control; amplía el zoom; prueba un ancho estrecho; inspecciona contraste y foco; valida estructura HTML y comprueba que cada página tenga metadatos propios. Registra problemas encontrados y correcciones.

## Recursos audiovisuales

No se incluyen videos en esta versión. HTML, CSS, accesibilidad y SEO requieren recursos separados; se incorporarán solo cuando el audio hablado esté en español y cada pieza cubra el subtema correspondiente. No se aprobará un video general de maquetación como formación suficiente en WCAG.

## Referencias oficiales y técnicas

- WHATWG HTML Living Standard: https://html.spec.whatwg.org/
- MDN — HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
- MDN — CSS: https://developer.mozilla.org/en-US/docs/Web/CSS
- W3C Web Accessibility Initiative: https://www.w3.org/WAI/
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WAI-ARIA 1.2: https://www.w3.org/TR/wai-aria-1.2/
- web.dev — Learn Accessibility: https://web.dev/learn/accessibility/
- Google Search Central — SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Schema.org: https://schema.org/

**Consulta de fuentes:** 2026-11-19.  
**Verificación práctica:** sitio y ejercicios propuestos; no desplegados ni sometidos a auditoría automatizada en esta sesión.  
**Estado editorial:** en desarrollo; no aprobado ni publicado.


## Desglose granular de lecciones oficiales — etapa 11

Este desglose conserva los títulos y el orden del roadmap maestro. Los apartados desarrollan las lecciones a partir del contenido conceptual de esta guía; no representan evaluación, aprobación ni ejecución práctica.

### Módulo 11.1 — HTML

#### 11.1.01 — Estructura de documentos
Un documento HTML es un árbol de nodos cuyo elemento raíz es `html`; dentro de él, `head` contiene metadatos y referencias a recursos, mientras `body` contiene el contenido del documento. Mantén una estructura completa y declara el idioma principal para que navegadores y tecnologías de asistencia interpreten correctamente el contenido.

#### 11.1.02 — DOCTYPE
`<!doctype html>` activa el modo estándar de renderizado en navegadores modernos; no es una etiqueta HTML ni una instrucción de presentación. Colócalo al inicio del documento y evita omitirlo, porque el modo de compatibilidad puede producir diferencias de layout difíciles de depurar.

#### 11.1.03 — Head
`head` aloja información no presentada como contenido principal: codificación, viewport, título, descripción, iconos, hojas de estilo y metadatos. Declara UTF-8 y un título específico; carga únicamente recursos necesarios y evita incluir información privada en metadatos públicos.

#### 11.1.04 — Body
`body` contiene el contenido que el usuario puede explorar e interactuar. Organiza sus regiones con elementos semánticos y garantiza que el contenido esencial no dependa de scripts que fallen o de estilos que puedan no cargarse.

#### 11.1.05 — Etiquetas
Las etiquetas delimitan elementos y aportan significado según el estándar; algunos elementos tienen etiqueta de apertura y cierre y otros son elementos vacíos. Usa elementos válidos para el contexto, respeta el anidamiento y no inventes etiquetas para conseguir un efecto visual.

#### 11.1.06 — Atributos
Los atributos configuran un elemento o aportan información como `id`, `class`, `href`, `src`, `alt`, `type` y `name`. Respeta los atributos globales y los específicos de cada elemento; los atributos booleanos se expresan por presencia y los valores dinámicos deben escaparse según el contexto.

#### 11.1.07 — HTML semántico
HTML semántico expresa la función de una región, no su apariencia: `main`, `nav`, `article`, `section` y `aside` ofrecen estructura comprensible. Elige el elemento por el significado del contenido y reserva `div` para agrupaciones sin semántica específica.

#### 11.1.08 — Headings
Los encabezados `h1`–`h6` describen títulos y niveles de sección. Mantén una jerarquía lógica que permita comprender el documento sin depender del tamaño tipográfico; utiliza CSS para ajustar la apariencia y no saltes niveles solo para obtener un estilo.

#### 11.1.09 — Sections
`section` agrupa contenido temáticamente relacionado y suele tener un encabezado que identifica su propósito. Si solo necesitas un contenedor para estilos, utiliza `div`; una página no necesita multiplicar secciones vacías ni convertir cada bloque visual en una región semántica.

#### 11.1.10 — Articles
`article` representa una composición autónoma que puede distribuirse o reutilizarse de forma independiente, como una noticia, entrada o ficha completa. Comprueba si el bloque conserva sentido fuera de la página; si depende totalmente del contexto circundante, probablemente corresponda a otra estructura.

#### 11.1.11 — Header
`header` introduce una página o una sección y puede contener título, marca o navegación contextual. No debe confundirse con `head`, que contiene metadatos; un documento puede tener varios `header` asociados a regiones distintas.

#### 11.1.12 — Footer
`footer` reúne información de cierre de una página o sección, como autoría, enlaces relacionados o datos legales. Su significado depende del contexto del elemento que lo contiene; evita utilizarlo únicamente como una caja posicionada al final de la pantalla.

#### 11.1.13 — Nav
`nav` identifica un bloque importante de enlaces de navegación. No todos los grupos de enlaces requieren `nav`; cuando hay varias regiones de navegación, asigna nombres accesibles distintos para que el usuario pueda diferenciarlas.

#### 11.1.14 — Forms
`form` agrupa controles que envían datos mediante una acción y un método. Define `action` y `method` de forma consciente, utiliza botones con tipo explícito y recuerda que la validación del navegador mejora la experiencia, pero no reemplaza la validación y autorización del servidor.

#### 11.1.15 — Inputs
`input` ofrece controles de distintos tipos: texto, correo, número, fecha, búsqueda, contraseña y otros. Selecciona el tipo que refleje el dato esperado, asocia un `label`, define `name` para el envío y no uses `type=number` para identificadores que no representan cantidades.

#### 11.1.16 — Selects
`select` permite elegir una opción de un conjunto definido; `option` representa cada alternativa y `optgroup` puede agruparlas. Proporciona una etiqueta clara, una opción inicial comprensible y valida en servidor que el valor recibido pertenezca a las opciones permitidas.

#### 11.1.17 — Textareas
`textarea` recoge texto multilínea y su tamaño visual se controla con atributos o CSS. Define límites y ayudas cuando sean necesarios, conserva el texto del usuario ante errores y evita interpretar el contenido como HTML confiable.

#### 11.1.18 — Tables
`table` representa datos con relaciones entre filas y columnas, no sirve como técnica de maquetación. Utiliza `caption`, `thead`, `tbody`, `th` y `scope` cuando corresponda para que los encabezados se asocien con los datos, especialmente en tablas complejas.

#### 11.1.19 — Multimedia
Los elementos multimedia `img`, `audio`, `video`, `source` y `track` incorporan medios al documento. Ofrece texto alternativo útil, subtítulos o transcripciones cuando el contenido lo requiera y evita reproducción automática con sonido; comprueba formatos, controles y alternativas.

#### 11.1.20 — SVG
SVG describe gráficos vectoriales mediante elementos XML como `svg`, `path`, `circle` y `rect`, por lo que escala sin pixelarse. Para gráficos informativos proporciona título y descripción o una alternativa textual; si es decorativo, evita que tecnologías de asistencia anuncien ruido innecesario.

#### 11.1.21 — Canvas
Canvas ofrece una superficie de dibujo controlada por JavaScript y no expone automáticamente el significado de los píxeles. Si el gráfico contiene información o controles, acompáñalo con una alternativa DOM accesible y sincroniza esa alternativa con el estado de la visualización.

### Módulo 11.2 — Accesibilidad

#### 11.2.01 — WCAG
WCAG 2.2 organiza la accesibilidad en principios perceptible, operable, comprensible y robusto, con criterios verificables y niveles A, AA y AAA. Selecciona el nivel exigido por el producto o normativa, registra evidencia por criterio y no declares conformidad a partir de una única herramienta automática.

#### 11.2.02 — ARIA
ARIA añade roles, propiedades y estados para comunicar semántica a tecnologías de asistencia cuando HTML nativo no alcanza. Prioriza controles HTML estándar; un `role` no implementa teclado, foco ni comportamiento, por lo que un widget personalizado debe reproducir el patrón de interacción completo.

#### 11.2.03 — Navegación por teclado
La navegación por teclado debe permitir alcanzar, operar y abandonar los controles sin ratón. Verifica orden de tabulación, foco visible, activación con Enter/Espacio según el control y gestión de foco en diálogos; no crees trampas ni elimines el indicador de foco.

#### 11.2.04 — Etiquetas accesibles
Una etiqueta accesible proporciona el nombre que una tecnología de asistencia anuncia para un control. Vincula `label` con `for`/`id` o utiliza el mecanismo semántico apropiado; el texto de ayuda y los errores deben asociarse al campo sin reemplazar su nombre.

#### 11.2.05 — Contraste
El contraste compara la luminancia del primer plano y el fondo para comprobar legibilidad. Evalúa texto normal, texto grande, iconos y componentes de interfaz según WCAG; revisa también estados de foco, error y deshabilitado, y no comuniques información solo mediante color.

#### 11.2.06 — Lectores de pantalla
Un lector de pantalla anuncia nombres, roles, estados y relaciones expuestos por el árbol de accesibilidad. Prueba recorridos reales con al menos una combinación navegador/lector disponible, escucha el orden de lectura y corrige semántica antes de añadir atributos ARIA redundantes.

#### 11.2.07 — Formularios accesibles
Un formulario accesible identifica cada campo, comunica requisitos, conserva datos y presenta errores comprensibles. Asocia mensajes con `aria-describedby` cuando corresponda, resume errores importantes y mueve el foco de manera predecible sin interrumpir innecesariamente al usuario.

#### 11.2.08 — HTML semántico
La semántica HTML proporciona estructura interoperable para encabezados, regiones, listas, tablas y controles. Comprueba el documento con el árbol de accesibilidad y utiliza elementos nativos antes de construir roles personalizados; una estructura correcta facilita teclado, lectores de pantalla e indexación.

### Módulo 11.3 — CSS

#### 11.3.01 — Selectores
Los selectores CSS identifican elementos por tipo, clase, ID, atributo, estado o relación. Prefiere clases con significado de componente y selectores acotados; selectores globales complejos aumentan acoplamiento y hacen más difícil predecir qué regla afecta a cada elemento.

#### 11.3.02 — Cascade
La cascada decide qué declaración prevalece considerando origen, importancia, capas, especificidad y orden de aparición. Depurar CSS exige revisar la cascada completa y no asumir que la última regla siempre gana; herramientas del navegador muestran declaraciones aplicadas y sobrescritas.

#### 11.3.03 — Specificity
La especificidad es un peso comparativo de selectores dentro de la cascada, no una puntuación universal que resuelva todos los conflictos. Mantén selectores sencillos y evita encadenar IDs o `!important` para compensar una arquitectura de estilos desordenada.

#### 11.3.04 — Inheritance
La herencia transmite determinadas propiedades desde un elemento ancestro a sus descendientes, como algunas propiedades tipográficas y de color. Otras propiedades, como márgenes y bordes, normalmente no se heredan; utiliza `inherit`, `initial` y `unset` solo cuando la intención sea explícita.

#### 11.3.05 — Box Model
El Box Model combina contenido, padding, borde y margen para determinar el espacio de un elemento. `box-sizing: border-box` hace que ancho y alto incluyan padding y borde, lo que simplifica layouts; prueba además el comportamiento con contenido largo y traducciones.

#### 11.3.06 — Display
`display` determina cómo participa un elemento en el flujo y el layout: block, inline, flex, grid y otros valores tienen reglas distintas. No confundas `display: none` con ocultación visual: también elimina el elemento del árbol de accesibilidad en el uso habitual.

#### 11.3.07 — Position
`position` controla el posicionamiento estático, relativo, absoluto, fijo o sticky y define el contexto de referencia de elementos posicionados. Reserva `absolute` para elementos superpuestos que realmente lo necesiten y verifica que el contenido no se solape con zoom o pantallas estrechas.

#### 11.3.08 — Flexbox
Flexbox distribuye elementos en un eje principal y otro transversal, con alineación y distribución flexibles. Practica `flex-direction`, `justify-content`, `align-items`, `gap`, `flex-wrap` y factores de crecimiento/reducción; prueba contenido de longitud variable para detectar desbordamientos.

#### 11.3.09 — Grid
Grid organiza elementos en dos dimensiones mediante tracks, líneas y áreas. Define columnas y filas con unidades flexibles como `fr`, funciones `minmax()` y `repeat()`; evita fijar dimensiones rígidas que impidan que el contenido crezca.

#### 11.3.10 — Pseudoclases
Las pseudoclases seleccionan elementos según estados o relaciones, como `:hover`, `:focus-visible`, `:checked` y `:first-child`. No dependas solo de hover, porque dispositivos táctiles y usuarios de teclado requieren estados equivalentes y visibles.

#### 11.3.11 — Pseudoelementos
Los pseudoelementos representan partes de un elemento o contenido generado, como `::before`, `::after` y `::placeholder`. El contenido generado es apropiado para decoración y señales complementarias, pero no debe contener la única etiqueta, instrucción o información crítica.

#### 11.3.12 — Variables
Las custom properties (`--token`) almacenan valores reutilizables y participan en la cascada. Define tokens semánticos para color, tipografía y espaciado, y cambia sus valores por tema o contexto; documenta valores de respaldo para propiedades que consumen variables.

#### 11.3.13 — Media Queries
Las media queries aplican estilos según características del entorno, como ancho, orientación o preferencia de movimiento. Define breakpoints cuando el contenido lo necesite y prueba entre puntos de corte; evita asociar cada breakpoint a un modelo de dispositivo específico.

#### 11.3.14 — Responsive Design
Responsive design adapta contenido y layout a distintos tamaños, densidades y formas de interacción. Comprueba reflow, zoom, navegación, imágenes fluidas y tablas; el objetivo es que la tarea siga siendo posible, no que cada viewport tenga una copia visual idéntica.

#### 11.3.15 — Animations
CSS animations describen secuencias mediante `@keyframes` y propiedades de duración, retraso, iteración y dirección. Úsalas para comunicar cambios de estado con moderación, proporciona alternativas cuando el movimiento no sea esencial y respeta la preferencia de movimiento reducido.

#### 11.3.16 — Transitions
Transitions interpolan cambios de propiedades entre estados, por ejemplo al enfocar un botón. Anima solo propiedades adecuadas, evita transiciones excesivas y no retrases acciones o mensajes que deban percibirse inmediatamente.

#### 11.3.17 — Transformations
Transformations modifican visualmente traslación, escala, rotación o inclinación sin cambiar necesariamente el flujo del documento. Considera el origen de transformación, el contexto de apilamiento y el movimiento reducido; no uses transformaciones para ocultar problemas de layout.

### Módulo 11.4 — Diseño de interfaces

#### 11.4.01 — Jerarquía visual
La jerarquía visual establece prioridades mediante tamaño, peso, contraste, posición y agrupación. Diseña primero qué debe comprender y hacer el usuario; valida que la prioridad visual coincide con la importancia funcional y no depende únicamente de color o tamaño.

#### 11.4.02 — Espaciado
El espaciado organiza grupos y relaciones entre elementos. Define una escala consistente y utiliza espacio cercano para señalar pertenencia; comprueba densidad, alineación y respiración visual con contenido real, no solo con textos de muestra de longitud uniforme.

#### 11.4.03 — Tipografía
La tipografía combina familia, tamaño, peso, altura de línea y longitud de lectura. Selecciona fuentes legibles, reserva estilos para jerarquías claras y verifica acentos, caracteres especiales, fallback y ampliación de texto sin pérdida de contenido.

#### 11.4.04 — Layouts
Un layout distribuye regiones y contenido según una estructura visual y funcional. Elige Grid para organización bidimensional y Flexbox para distribución en un eje cuando encaje; documenta las restricciones y verifica que el orden visual no contradiga el orden del DOM.

#### 11.4.05 — Componentes
Un componente encapsula una unidad de interfaz con propósito, estructura, estilos, comportamiento y estados definidos. Establece entradas y salidas claras, evita dependencias globales innecesarias y documenta variantes, accesibilidad y comportamiento en error o carga.

#### 11.4.06 — Design Systems
Un design system reúne principios, tokens, componentes, patrones y documentación para mantener decisiones coherentes. No es solo una biblioteca de botones: incluye criterios de uso, accesibilidad, gobernanza y proceso para introducir cambios sin fragmentar la experiencia.

#### 11.4.07 — Consistencia visual
La consistencia visual hace que componentes equivalentes se comporten y se vean de manera predecible. Define reglas para tipografía, color, espaciado, estados e iconografía y permite excepciones justificadas cuando el contexto de uso lo exige.

#### 11.4.08 — Mobile-first
Mobile-first comienza por priorizar contenido y tareas bajo restricciones de espacio y amplía progresivamente. No significa reducir funciones en móvil; valida navegación, foco, objetivos táctiles y lectura en anchuras pequeñas y luego añade mejoras para pantallas mayores.

### Módulo 11.5 — SEO

#### 11.5.01 — Metadatos
Los metadatos describen el documento para navegadores, buscadores y plataformas de compartición. Incluye codificación, viewport, idioma, título y descripción adecuados; nunca coloques secretos ni información personal que no deba hacerse pública.

#### 11.5.02 — Títulos
El elemento `title` identifica de forma concisa y única la página y suele aparecer en pestañas y resultados de búsqueda. Escribe títulos específicos, coherentes con el contenido y comprensibles fuera de contexto; no repitas una plantilla idéntica en todo el sitio.

#### 11.5.03 — Descripciones
La meta description resume la utilidad de una página y puede utilizarse como fragmento en resultados, aunque el buscador puede generar otro. Redacta una descripción veraz, diferenciada y orientada al contenido real; no la trates como garantía de ranking.

#### 11.5.04 — Estructura semántica
La estructura semántica facilita que personas, navegadores y motores comprendan las regiones y relaciones del contenido. Usa headings, enlaces descriptivos, landmarks y datos visibles coherentes; no añadas etiquetas solo para insertar palabras clave.

#### 11.5.05 — Indexación
La indexación es el proceso por el que un buscador incorpora y puede recuperar contenido rastreado. Facilita descubrimiento mediante enlaces internos, sitemap cuando proceda y respuestas HTTP correctas; `robots.txt` no es un mecanismo de confidencialidad ni sustituye autenticación.

#### 11.5.06 — Datos estructurados (introducción)
Los datos estructurados describen entidades y propiedades con vocabularios como Schema.org, habitualmente en JSON-LD. Los valores deben coincidir con contenido visible y políticas del buscador; no inventes reseñas, precios, eventos o disponibilidad para intentar obtener resultados enriquecidos.


## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 60 orientaciones genéricas del desglose granular por explicaciones específicas de cada entrada oficial. Cada apartado precisa la función del concepto, decisiones de uso, límites y/o una comprobación contextual; el desarrollo se articula con la guía principal, el sitio profesional del proyecto y los ejercicios de accesibilidad/responsive.

**Revisión interna:** 60/60 entradas cubiertas y cotejadas con el roadmap. Se revisaron semántica HTML, formularios, SVG/Canvas, principios WCAG/ARIA, cascada, especificidad, modelos de layout, movimiento reducido, diseño de componentes y SEO. La revisión es documental, no certificación WCAG ni auditoría automatizada. Pendiente: validar el HTML/CSS con herramientas actuales, probar teclado y lector de pantalla, medir contraste, revisar responsive en navegadores y ejecutar el proyecto antes de aprobación externa.
