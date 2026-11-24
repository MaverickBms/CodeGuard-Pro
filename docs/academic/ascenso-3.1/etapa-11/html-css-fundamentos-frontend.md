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

HTML define un árbol DOM que el navegador interpreta. La estructura mínima contiene doctype, html, head y body; declara idioma y metadatos.

**Ejemplo técnico:** Documento en español con UTF-8, viewport, title y h1.

**Práctica guiada:** Crea index.html y revisa el DOM.

**Actividad independiente:** Página de curso sin CSS.

**Criterios de aceptación:** Idioma, metadatos y anidamiento correctos.

**Errores frecuentes:** Omitir doctype o anidar mal.

**Comprobación:** ¿Qué representa el DOM?

**Laboratorio de profundización — Documento HTML mínimo y validación.**

1. Crea un documento HTML con declaración de tipo, elemento raíz, head y body. 2. Añade idioma del documento y codificación. 3. Valida anidamiento y jerarquía. 4. Comprueba el resultado en dos navegadores.

**Evidencia esperada.** El documento tiene estructura válida, idioma declarado y contenido separado de metadatos.

**Seguridad y límites.** No usar HTML como sustituto de validación de entradas ni insertar contenido no confiable sin escape.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.02 — DOCTYPE

`<!doctype html>` activa el modo estándar; es una declaración, no un elemento.

**Ejemplo técnico:** Sin doctype el navegador puede activar quirks mode.

**Práctica guiada:** Compara archivos con y sin doctype.

**Actividad independiente:** Documenta por qué va al inicio.

**Criterios de aceptación:** Aparece antes de html.

**Errores frecuentes:** Escribirlo como etiqueta.

**Comprobación:** ¿Qué modo activa?

**Laboratorio de profundización — Modo de estándares y declaración HTML.**

1. Crea una página con `<!doctype html>`. 2. Comprueba que la declaración esté al inicio. 3. Observa el modo de documento desde herramientas del navegador. 4. Explica el comportamiento de páginas antiguas sin doctype.

**Evidencia esperada.** Se explica la finalidad de activar modo estándares y la declaración correcta para HTML moderno.

**Seguridad y límites.** No copiar DOCTYPE antiguos salvo que el proyecto requiera compatibilidad documentada.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.03 — Head

head contiene metadatos, title y enlaces a recursos; no el contenido principal.

**Ejemplo técnico:** charset, viewport, title y description.

**Práctica guiada:** Añade y verifica metadatos.

**Actividad independiente:** Diseña head para una página de producto.

**Criterios de aceptación:** Metadatos pertinentes.

**Errores frecuentes:** Contenido visible dentro de head.

**Comprobación:** ¿Qué diferencia head de body?

**Laboratorio de profundización — Metadatos y recursos del documento.**

1. Añade charset, viewport, title y description. 2. Incluye un stylesheet local. 3. Distingue metadatos de contenido visible. 4. Comprueba carga y orden de recursos en DevTools.

**Evidencia esperada.** El head contiene metadatos pertinentes y no incluye contenido destinado al cuerpo.

**Seguridad y límites.** No duplicar metadatos contradictorios ni cargar scripts externos no confiables.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.04 — Body

body contiene contenido, navegación, formularios y regiones semánticas.

**Ejemplo técnico:** header, nav, main y footer.

**Práctica guiada:** Organiza una página y revisa landmarks.

**Actividad independiente:** Reestructura una página hecha solo con div.

**Criterios de aceptación:** Jerarquía coherente.

**Errores frecuentes:** Duplicar landmarks sin nombre.

**Comprobación:** ¿Qué aporta semántica a lectores de pantalla?

**Laboratorio de profundización — Estructuración del contenido visible.**

1. Construye una página con encabezado, contenido principal y pie. 2. Separa contenido y presentación. 3. Comprueba orden de lectura en DOM. 4. Navega sin CSS para validar comprensión.

**Evidencia esperada.** El contenido mantiene estructura y significado aun sin estilos visuales.

**Seguridad y límites.** No usar body para almacenar información secreta ni depender de CSS para ocultar contenido sensible.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.05 — Etiquetas

Los elementos expresan semántica y comportamiento; se eligen por función.

**Ejemplo técnico:** button para acción, a para navegación, p para párrafo.

**Práctica guiada:** Reemplaza div clicables por controles nativos.

**Actividad independiente:** Justifica cinco decisiones semánticas.

**Criterios de aceptación:** Elementos y comportamiento apropiados.

**Errores frecuentes:** Controles custom sin teclado.

**Comprobación:** ¿Por qué preferir button nativo?

**Laboratorio de profundización — Selección de elementos HTML.**

1. Crea un contenido con párrafos, listas, enlaces, botones y elementos de énfasis. 2. Selecciona cada etiqueta por su semántica. 3. Comprueba anidamiento válido. 4. Revisa el árbol de accesibilidad.

**Evidencia esperada.** Cada etiqueta corresponde al propósito del contenido y los controles son operables.

**Seguridad y límites.** No elegir etiquetas solo por apariencia ni usar elementos interactivos anidados incorrectamente.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.06 — Atributos

Los atributos configuran elementos; algunos son globales y otros específicos.

**Ejemplo técnico:** img usa src/alt; a usa href; input usa type/name; id es único.

**Práctica guiada:** Añade y valida atributos.

**Actividad independiente:** Audita formulario y galería.

**Criterios de aceptación:** Valores válidos e IDs únicos.

**Errores frecuentes:** Repetir id u omitir alt.

**Comprobación:** ¿Qué diferencia class de id?

**Laboratorio de profundización — Atributos globales y específicos.**

1. Añade id, class, lang, title y atributos específicos a controles. 2. Distingue atributo booleano y valor textual. 3. Comprueba unicidad de id. 4. Valida que atributos no estándar no sustituyan semántica nativa.

**Evidencia esperada.** Los atributos tienen valores válidos, propósito claro y no duplican identificadores.

**Seguridad y límites.** No insertar datos sensibles en atributos HTML ni confiar en atributos personalizados como control de seguridad.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.07 — HTML semántico

HTML semántico refleja función y jerarquía mediante elementos especializados.

**Ejemplo técnico:** main, nav, article y section.

**Práctica guiada:** Reestructura landing y revisa árbol accesible.

**Actividad independiente:** Diseña artículo técnico semántico.

**Criterios de aceptación:** Cada elemento se justifica por función.

**Errores frecuentes:** Usar section como div universal.

**Comprobación:** ¿Cuándo usar article?

**Laboratorio de profundización — Selección semántica de regiones.**

1. Convierte una maqueta genérica en header, nav, main, section y footer. 2. Identifica landmarks. 3. Comprueba el árbol de accesibilidad. 4. Justifica cada elemento según el contenido.

**Evidencia esperada.** La estructura comunica propósito y regiones a navegadores y tecnologías de asistencia.

**Seguridad y límites.** No utilizar elementos semánticos solo para obtener estilos; el significado debe corresponder al contenido.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.08 — Headings

h1–h6 expresan jerarquía; CSS controla apariencia.

**Ejemplo técnico:** h1 título, h2 capítulos, h3 subsecciones.

**Práctica guiada:** Corrige árbol de encabezados.

**Actividad independiente:** Esquema de títulos para una guía.

**Criterios de aceptación:** Niveles coherentes.

**Errores frecuentes:** Elegir nivel por tamaño.

**Comprobación:** ¿Por qué cambiar tamaño con CSS?

**Laboratorio de profundización — Jerarquía de encabezados.**

1. Construye un documento con título principal y secciones. 2. Ordena h1–h3 según jerarquía temática. 3. Comprueba navegación por encabezados con lector de pantalla o herramienta equivalente. 4. Corrige saltos injustificados.

**Evidencia esperada.** Los encabezados representan la estructura del contenido y no se eligen por tamaño visual.

**Seguridad y límites.** No usar headings para agrandar texto ni omitir niveles por conveniencia estética.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.09 — Sections

section agrupa contenido temático, normalmente con encabezado; div es genérico.

**Ejemplo técnico:** Objetivos, Contenido y Evaluación.

**Práctica guiada:** Clasifica contenedores.

**Actividad independiente:** Organiza documentación en secciones.

**Criterios de aceptación:** Propósito temático claro.

**Errores frecuentes:** Convertir todos los div en section.

**Comprobación:** ¿Qué distingue section de div?

**Laboratorio de profundización — Agrupación temática con section.**

1. Divide un artículo largo en secciones con encabezado propio. 2. Compara section con div. 3. Comprueba que cada sección tenga propósito temático. 4. Revisa navegación por landmarks.

**Evidencia esperada.** Cada section representa una agrupación temática identificable y contiene encabezado apropiado cuando corresponde.

**Seguridad y límites.** No envolver cada bloque de estilo en section si no existe una unidad temática.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.10 — Articles

article representa contenido autónomo y reutilizable.

**Ejemplo técnico:** Noticia con título, fecha y cuerpo.

**Práctica guiada:** Marca noticias y comprueba que tengan sentido aisladas.

**Actividad independiente:** Estructura un artículo técnico.

**Criterios de aceptación:** Contenido autónomo.

**Errores frecuentes:** Usar article para cualquier bloque.

**Comprobación:** ¿Qué característica justifica article?

**Laboratorio de profundización — Contenido independiente con article.**

1. Modela una tarjeta de noticia que pueda reutilizarse fuera de la página. 2. Incluye título, autor y fecha con elementos apropiados. 3. Compara article con section. 4. Comprueba lectura independiente.

**Evidencia esperada.** El article representa una unidad autónoma y su contexto se entiende al extraerlo.

**Seguridad y límites.** No utilizar article como contenedor genérico de cualquier bloque.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.11 — Header

header contiene información introductoria o navegación; no es head.

**Ejemplo técnico:** Header global y header de artículo.

**Práctica guiada:** Identifica ambos contextos.

**Actividad independiente:** Diseña header responsive accesible.

**Criterios de aceptación:** Uso contextual.

**Errores frecuentes:** Ubicar header dentro de head.

**Comprobación:** ¿Qué diferencia head de header?

**Laboratorio de profundización — Encabezado de página y sección.**

1. Crea un encabezado global y otro dentro de un article. 2. Añade título y metadatos pertinentes. 3. Comprueba que header no se confunda con head. 4. Revisa landmarks resultantes.

**Evidencia esperada.** Se diferencia metadato del documento y encabezado visible de una región.

**Seguridad y límites.** No anidar header como si fuera un elemento exclusivo del inicio del documento.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.12 — Footer

footer contiene información de cierre de página o sección.

**Ejemplo técnico:** Contacto global y autoría de artículo.

**Práctica guiada:** Incorpora ambos contextos.

**Actividad independiente:** Diseña pie con enlaces agrupados.

**Criterios de aceptación:** Contenido asociado al contexto.

**Errores frecuentes:** Usarlo como contenedor fijo sin semántica.

**Comprobación:** ¿Puede haber varios footer?

**Laboratorio de profundización — Pie de página y contexto.**

1. Diseña un footer global con contacto y enlaces legales ficticios. 2. Añade footer de un article con autor y fecha. 3. Comprueba jerarquía y enlaces. 4. Navega por teclado.

**Evidencia esperada.** El pie proporciona información relacionada con su contexto y enlaces tienen nombres claros.

**Seguridad y límites.** No usar footer para esconder información ni incluir enlaces vacíos.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.13 — Nav

nav identifica una región principal de navegación; no todo grupo de enlaces lo requiere.

**Ejemplo técnico:** Navegación principal e índice con aria-label distinto.

**Práctica guiada:** Crea ambas regiones y recorre con teclado.

**Actividad independiente:** Diseña menú móvil accesible.

**Criterios de aceptación:** Regiones distinguibles.

**Errores frecuentes:** Envolver todos los enlaces en nav.

**Comprobación:** ¿Por qué nombrar dos nav?

**Laboratorio de profundización — Navegación y enlaces funcionales.**

1. Construye navegación principal con enlaces a secciones reales. 2. Añade nombre accesible al nav. 3. Comprueba orden de tabulación y estado activo. 4. Verifica destino de cada enlace.

**Evidencia esperada.** Los enlaces tienen destino real, texto comprensible y navegación operable por teclado.

**Seguridad y límites.** No usar href vacío o javascript:void(0) como sustituto de botones.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.14 — Forms

form agrupa controles y define envío; requiere etiquetas y validación cliente/servidor.

**Ejemplo técnico:** Formulario con label, email y mensaje.

**Práctica guiada:** Construye y prueba con teclado.

**Actividad independiente:** Diseña inscripción con resumen de errores.

**Criterios de aceptación:** Campos etiquetados y validación servidor.

**Errores frecuentes:** Placeholder como única etiqueta.

**Comprobación:** ¿Por qué validar en servidor?

**Laboratorio de profundización — Formulario con validación nativa.**

1. Crea formulario de contacto ficticio. 2. Define método y destino de prueba. 3. Añade labels y validación requerida. 4. Comprueba mensajes y envío con datos válidos e inválidos.

**Evidencia esperada.** El formulario identifica campos, valida entradas y ofrece una ruta de envío explícita.

**Seguridad y límites.** La validación del navegador no sustituye validación del servidor ni protección CSRF.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.15 — Inputs

input ofrece controles variados; el tipo debe reflejar el dato.

**Ejemplo técnico:** type=password oculta texto, pero no cifra transporte.

**Práctica guiada:** Crea email, fecha y checkbox etiquetados.

**Actividad independiente:** Selecciona tipos y autocomplete.

**Criterios de aceptación:** Tipo y etiqueta correctos.

**Errores frecuentes:** Usar number para códigos con ceros iniciales.

**Comprobación:** ¿Por qué un código postal suele ser texto?

**Laboratorio de profundización — Tipos de input y validación.**

1. Utiliza email, number, date, checkbox y radio según semántica. 2. Define min, max, required y autocomplete cuando corresponda. 3. Prueba entradas límite. 4. Comprueba accesibilidad del nombre del campo.

**Evidencia esperada.** Cada control corresponde al tipo de dato y comunica restricciones y estado.

**Seguridad y límites.** No confiar en type=email o required como validación de seguridad del lado servidor.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.16 — Selects

select permite elegir opciones; option requiere texto y value estable.

**Ejemplo técnico:** País visible y código enviado.

**Práctica guiada:** Crea select etiquetado y prueba teclado.

**Actividad independiente:** Diseña opción Otra accesible.

**Criterios de aceptación:** Opciones claras.

**Errores frecuentes:** Usar placeholder como valor.

**Comprobación:** ¿Qué diferencia texto y value?

**Laboratorio de profundización — Selección de opciones.**

1. Crea un select con label y option. 2. Agrupa opciones relacionadas con optgroup. 3. Define placeholder o opción inicial sin valor cuando corresponda. 4. Prueba teclado y selección en móvil.

**Evidencia esperada.** Las opciones tienen valores inequívocos y el control es operable con teclado y táctil.

**Seguridad y límites.** No utilizar select para navegación sin anunciar el cambio ni ocultar opciones importantes.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.17 — Textareas

textarea permite texto multilínea; label, ayuda y límites deben asociarse.

**Ejemplo técnico:** Descripción con maxlength y aria-describedby.

**Práctica guiada:** Crea campo con ayuda y límite.

**Actividad independiente:** Diseña contador accesible.

**Criterios de aceptación:** Etiqueta y errores accesibles.

**Errores frecuentes:** Confiar en maxlength como seguridad.

**Comprobación:** ¿Por qué escapar texto al mostrarlo?

**Laboratorio de profundización — Campos de texto multilínea.**

1. Crea textarea con label, rows y maxlength. 2. Añade ayuda contextual y contador accesible. 3. Prueba contenido largo y saltos de línea. 4. Comprueba tratamiento del contenido en servidor.

**Evidencia esperada.** El campo comunica propósito, límites y errores y preserva el texto introducido.

**Seguridad y límites.** Sanitizar y validar contenido en servidor; no renderizar HTML introducido directamente.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.18 — Tables

Las tablas representan datos, no layout. caption, thead, tbody, th y scope relacionan encabezados.

**Ejemplo técnico:** Tabla de notas con encabezados de filas y columnas.

**Práctica guiada:** Semantiza tabla y revisa accesibilidad.

**Actividad independiente:** Diseña tabla con encabezados agrupados.

**Criterios de aceptación:** Caption y encabezados identificables.

**Errores frecuentes:** Usar tablas para maquetación.

**Comprobación:** ¿Qué aporta scope?

**Laboratorio de profundización — Tablas de datos accesibles.**

1. Diseña tabla con caption, thead, tbody y th. 2. Define scope o asociaciones header/cell. 3. Comprueba lectura con lector de pantalla. 4. Añade diseño responsive sin eliminar contexto de celdas.

**Evidencia esperada.** La tabla representa datos tabulares y las relaciones encabezado-celda son comprensibles.

**Seguridad y límites.** No utilizar tablas para maquetar ni eliminar encabezados al adaptar a móvil.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.19 — Multimedia

HTML integra imagen, audio y video; se requieren alt, subtítulos o transcripciones.

**Ejemplo técnico:** Video con controls y track captions.

**Práctica guiada:** Integra video de prueba con subtítulos.

**Actividad independiente:** Diseña galería accesible.

**Criterios de aceptación:** Alternativas y controles accesibles.

**Errores frecuentes:** Video sin subtítulos.

**Comprobación:** ¿Qué alternativa ofrecer si el dato solo está en audio?

**Laboratorio de profundización — Audio y video con controles accesibles.**

1. Inserta video de prueba con controls y poster. 2. Añade subtítulos mediante track cuando corresponda. 3. Proporciona transcripción o alternativa para audio. 4. Comprueba reproducción por teclado y preferencias de movimiento.

**Evidencia esperada.** El contenido multimedia dispone de controles, subtítulos o alternativas pertinentes.

**Seguridad y límites.** No iniciar audio automáticamente ni publicar material sin derechos de uso.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.20 — SVG

SVG es vectorial basado en XML; gráficos informativos requieren nombre y descripción.

**Ejemplo técnico:** title/desc para gráfico; aria-hidden para icono decorativo.

**Práctica guiada:** Crea SVG con viewBox y alternativa.

**Actividad independiente:** Diseña gráfico con descripción y tabla.

**Criterios de aceptación:** No depende solo de color.

**Errores frecuentes:** Omitir alternativa.

**Comprobación:** ¿Por qué describir un gráfico?

**Laboratorio de profundización — Gráficos vectoriales accesibles.**

1. Crea un SVG simple con formas y texto. 2. Decide si es decorativo o informativo. 3. Añade nombre accesible o lo excluye del árbol cuando sea decorativo. 4. Comprueba escalado y contraste.

**Evidencia esperada.** El SVG tiene alternativa textual cuando transmite información y no duplica anuncios para contenido decorativo.

**Seguridad y límites.** No incluir scripts externos ni referencias remotas no confiables en SVG embebido.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.

#### 11.1.21 — Canvas

canvas dibuja mediante JavaScript, pero sus formas no son nodos DOM accesibles automáticamente.

**Ejemplo técnico:** Gráfico con tabla equivalente.

**Práctica guiada:** Dibuja datos y añade tabla HTML.

**Actividad independiente:** Diseña visualización con leyenda y alternativa.

**Criterios de aceptación:** Alternativa equivalente.

**Errores frecuentes:** Usar canvas como reemplazo de HTML.

**Comprobación:** ¿Qué pierde quien no percibe el bitmap sin alternativa?


**Laboratorio de profundización — Canvas y alternativa semántica.**

1. Dibuja una gráfica simple en canvas con JavaScript. 2. Proporciona descripción y tabla equivalente en DOM. 3. Comprueba qué contenido queda fuera del árbol de accesibilidad. 4. Evalúa interacción con teclado si existe.

**Evidencia esperada.** La información esencial del canvas está disponible como contenido alternativo accesible.

**Seguridad y límites.** No depender exclusivamente de píxeles para transmitir datos o controles.

**Registro sugerido.** Conserva fragmento HTML, navegador/versión, resultado de validación, prueba de teclado y observaciones de accesibilidad. No marques la práctica como ejecutada sin evidencia real.
#### 11.2.01 — WCAG

WCAG define principios POUR: perceptible, operable, comprensible y robusto. Los criterios tienen niveles A, AA y AAA; la conformidad requiere evaluar páginas y procesos completos, no solo ejecutar una herramienta automática.

**Ejemplo técnico:** Una aplicación puede tener contraste correcto y aun fallar porque el formulario no anuncia errores o el flujo no opera con teclado.

**Práctica guiada:** Evalúa una página con lista de verificación POUR y registra evidencia para cada principio.

**Actividad independiente:** Prioriza cinco barreras y propone correcciones verificables.

**Criterios de aceptación:** Relaciona hallazgo con criterio y nivel WCAG aplicable; no declara conformidad por una sola prueba.

**Errores frecuentes:** Confundir accesibilidad con contraste o afirmar cumplimiento por escaneo automático.

**Comprobación:** ¿Por qué WCAG exige revisar procesos completos y no solo elementos aislados?

**Laboratorio de profundización — Auditoría básica con criterios WCAG.**

1. Selecciona una página de laboratorio. 2. Evalúa percepción, operabilidad, comprensión y robustez. 3. Identifica criterios aplicables de nivel A/AA. 4. Registra evidencia, impacto y propuesta de corrección.

**Evidencia esperada.** La auditoría identifica criterio y evidencia concreta; no se limita a una puntuación automática.

**Seguridad y límites.** No afirmar conformidad WCAG completa a partir de una sola herramienta automática o una revisión parcial.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.02 — ARIA

WAI-ARIA aporta roles, estados y propiedades para comunicar semántica a tecnologías de asistencia cuando HTML nativo no basta. No reemplaza elementos nativos ni agrega comportamiento por sí sola; un widget ARIA debe implementar teclado, foco y estados.

**Ejemplo técnico:** aria-expanded informa estado de un control, pero el código también debe abrir/cerrar el panel y mantener el foco coherente.

**Práctica guiada:** Inspecciona un acordeón nativo y otro custom; identifica rol, estado y comportamiento de teclado.

**Actividad independiente:** Diseña un menú custom solo si un elemento nativo no cubre el caso; especifica teclado y estados.

**Criterios de aceptación:** ARIA coincide con comportamiento real y no duplica semántica nativa.

**Errores frecuentes:** Agregar role=button a un botón nativo o usar ARIA sin implementar interacción.

**Comprobación:** ¿Por qué se prefiere HTML nativo antes de añadir ARIA?

**Laboratorio de profundización — Uso mínimo y correcto de ARIA.**

1. Inspecciona controles nativos y sus roles implícitos. 2. Añade ARIA solo cuando HTML nativo no expresa el patrón requerido. 3. Compara aria-label, aria-labelledby y aria-describedby. 4. Comprueba árbol de accesibilidad.

**Evidencia esperada.** Se prefiere semántica HTML nativa y los atributos ARIA no contradicen el rol ni el estado real.

**Seguridad y límites.** No añadir roles ARIA redundantes ni crear controles personalizados sin teclado y estados completos.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.03 — Navegación por teclado

Toda funcionalidad debe poder operarse con teclado sin trampas de foco. Tab y Shift+Tab recorren controles; Enter y Space activan según semántica; flechas se utilizan en widgets con patrón definido. El orden de foco debe seguir el orden lógico del contenido.

**Ejemplo técnico:** Un botón nativo recibe foco y se activa con teclado; un div con onclick no lo hace automáticamente.

**Práctica guiada:** Recorre una página solo con teclado y registra foco visible, orden y posibilidad de salir de componentes.

**Actividad independiente:** Corrige un menú que atrapa foco o tiene orden distinto al visual.

**Criterios de aceptación:** Todas las acciones principales son alcanzables, identificables y operables sin ratón.

**Errores frecuentes:** Eliminar outline sin alternativa o usar tabindex positivo para forzar orden.

**Comprobación:** ¿Qué problema causa un componente que recibe foco pero no permite salir de él?

**Laboratorio de profundización — Recorrido completo sin ratón.**

1. Navega la página usando Tab, Shift+Tab, Enter, Space y flechas según control. 2. Verifica orden lógico y foco visible. 3. Abre y cierra menú y diálogo. 4. Comprueba que no exista trampa de teclado.

**Evidencia esperada.** Todos los controles son alcanzables y operables y el foco sigue orden comprensible.

**Seguridad y límites.** No eliminar outline sin alternativa visible ni utilizar tabindex positivo como reparación general.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.04 — Etiquetas accesibles

Los controles necesitan nombre accesible que comunique propósito. label asociado, texto visible, aria-label y aria-labelledby tienen usos distintos; placeholder no reemplaza label. El nombre debe coincidir con la etiqueta visible para facilitar reconocimiento por voz.

**Ejemplo técnico:** Un input con label for/id conserva nombre al desaparecer placeholder; aria-label puede nombrar un control sin texto visible, pero debe usarse con criterio.

**Práctica guiada:** Inspecciona nombre accesible de botones e inputs en herramientas del navegador.

**Actividad independiente:** Repara formulario donde campos solo tienen placeholder y botones solo iconos.

**Criterios de aceptación:** Cada control tiene nombre único, descriptivo y asociado correctamente.

**Errores frecuentes:** Usar texto ambiguo como «clic aquí» o duplicar nombres en controles distintos sin contexto.

**Comprobación:** ¿Por qué placeholder no es sustituto de label?

**Laboratorio de profundización — Nombre, descripción y asociación de campos.**

1. Crea controles con label explícito mediante for/id. 2. Añade instrucciones con aria-describedby cuando sea necesario. 3. Comprueba nombre accesible. 4. Verifica que placeholder no sustituya label.

**Evidencia esperada.** Cada control tiene nombre accesible y las instrucciones se anuncian en contexto.

**Seguridad y límites.** No usar solo placeholder ni asociar múltiples controles al mismo id.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.05 — Contraste

El contraste entre texto y fondo debe evaluarse con luminancia relativa y umbrales WCAG aplicables al tamaño y tipo de texto. El color no debe ser el único medio para transmitir estado; foco, errores y gráficos necesitan señales adicionales.

**Ejemplo técnico:** Texto normal suele requerir ratio 4.5:1 en WCAG AA; texto grande tiene umbral distinto. Componentes gráficos y foco también tienen criterios aplicables.

**Práctica guiada:** Mide combinaciones de una página con herramienta y registra colores, ratio y tamaño de texto.

**Actividad independiente:** Rediseña alertas para que estado no dependa solo de rojo/verde.

**Criterios de aceptación:** Contraste cumple umbral pertinente y estados incluyen texto/ícono u otra señal.

**Errores frecuentes:** Evaluar solo el color del botón o usar color como única señal.

**Comprobación:** ¿Por qué un mensaje de error debe tener texto además de color?

**Laboratorio de profundización — Medición de contraste de texto y controles.**

1. Selecciona combinaciones de color de primer plano y fondo. 2. Calcula contraste para texto normal y grande. 3. Revisa estados hover, focus, error y deshabilitado. 4. Ajusta paleta y repite medición.

**Evidencia esperada.** La medición documenta ratios y el umbral WCAG aplicable a cada tipo de contenido.

**Seguridad y límites.** No comunicar estado solo mediante color; verificar también contraste de componentes y foco.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.06 — Lectores de pantalla

Los lectores de pantalla exponen estructura, nombres, roles, estados y relaciones del árbol de accesibilidad. La experiencia depende de semántica HTML, orden de lectura, etiquetas, encabezados y actualizaciones dinámicas anunciadas apropiadamente.

**Ejemplo técnico:** Una región de resultados que cambia puede requerir aria-live o un mecanismo de foco apropiado, evitando anunciar cada cambio irrelevante.

**Práctica guiada:** Prueba navegación por headings, landmarks, enlaces y formularios con lector de pantalla disponible o inspección del árbol accesible.

**Actividad independiente:** Diseña una actualización dinámica que informe el resultado sin mover foco innecesariamente.

**Criterios de aceptación:** La información y acciones esenciales se entienden sin depender de vista visual.

**Errores frecuentes:** Agregar aria-live a contenedores enormes o anunciar mensajes repetitivos.

**Comprobación:** ¿Qué diferencia existe entre anunciar una actualización y mover el foco?

**Laboratorio de profundización — Prueba de lectura y landmarks.**

1. Activa un lector de pantalla disponible. 2. Recorre encabezados, landmarks, enlaces, botones y formularios. 3. Compara orden anunciado con orden visual. 4. Registra etiquetas ambiguas o contenido repetido.

**Evidencia esperada.** El contenido se comprende sin depender de la presentación visual y los controles anuncian propósito y estado.

**Seguridad y límites.** No suponer que una sola combinación de navegador y lector representa todas las tecnologías de asistencia.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.07 — Formularios accesibles

Un formulario accesible asocia etiquetas, instrucciones, agrupaciones y errores con controles. fieldset/legend agrupan opciones relacionadas; aria-describedby enlaza ayuda; el error debe identificarse en texto y asociarse al campo. La validación debe preservar datos y permitir corregir.

**Ejemplo técnico:** Tras un envío inválido, un resumen de errores puede enlazar a campos y el foco puede dirigirse al resumen o primer error según diseño.

**Práctica guiada:** Crea formulario con fieldset, legend, labels y mensajes asociados; prueba teclado y lector de pantalla.

**Actividad independiente:** Diseña flujo de errores para campos requeridos, formato inválido y fallo del servidor.

**Criterios de aceptación:** Errores identificables, asociados y corregibles sin perder valores.

**Errores frecuentes:** Mostrar errores solo en tooltip o depender de color y placeholder.

**Comprobación:** ¿Qué debe poder comprender y hacer una persona después de recibir un error de validación?

**Laboratorio de profundización — Errores y ayudas anunciadas.**

1. Construye un formulario con campos obligatorios. 2. Provoca error de validación. 3. Asocia mensaje al campo y comunica resumen de errores. 4. Comprueba foco y anuncio de estado sin perder datos.

**Evidencia esperada.** El error se identifica en texto, se asocia al campo y el usuario puede corregirlo con teclado.

**Seguridad y límites.** No borrar valores introducidos al mostrar errores ni depender solo de color o alertas temporales.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.

#### 11.2.08 — HTML semántico

La semántica nativa ofrece roles y comportamientos reconocibles. Utilizar elementos adecuados reduce ARIA y código adicional. La estructura debe probarse con tecnologías de asistencia y teclado, porque una etiqueta semántica mal aplicada puede confundir.

**Ejemplo técnico:** button para acción, a para navegación y table para datos tabulares ofrecen comportamientos esperados sin roles manuales.

**Práctica guiada:** Audita un componente y reemplaza roles redundantes por HTML nativo cuando corresponda.

**Actividad independiente:** Reestructura un dashboard para que controles, navegación y tablas expongan semántica correcta.

**Criterios de aceptación:** El árbol accesible refleja intención y el teclado opera los controles.

**Errores frecuentes:** Usar role=link en un span sin implementar interacción o role redundante sobre elemento nativo.

**Comprobación:** ¿Qué se gana al usar la semántica HTML correcta desde el inicio?


**Laboratorio de profundización — Comparación de árbol DOM y árbol accesible.**

1. Crea una página con divs genéricos y otra con landmarks semánticos. 2. Compara navegación por regiones y encabezados. 3. Revisa roles implícitos. 4. Documenta cuándo usar section, article, nav y main.

**Evidencia esperada.** La versión semántica comunica estructura y reduce necesidad de roles ARIA explícitos.

**Seguridad y límites.** No asignar roles manuales que contradigan la semántica nativa.

**Registro sugerido.** Anota navegador, sistema operativo, tecnología de asistencia o herramienta, criterio evaluado, pasos reproducibles y barreras detectadas. No marques conformidad completa sin evaluación integral.
#### 11.3.01 — Selectores

Los selectores CSS identifican elementos por tipo, clase, ID, atributo, estado o relación. Deben mantenerse legibles y limitar alcance para evitar estilos difíciles de sobrescribir.

**Ejemplo técnico:** `.card > h2` selecciona encabezados directos; `.card h2` incluye descendientes a cualquier profundidad.

**Práctica guiada:** Aplica selectores de tipo, clase, atributo y descendiente en una página de prueba.

**Actividad independiente:** Refactoriza selectores excesivamente específicos y elimina duplicación.

**Criterios de aceptación:** Cada regla afecta solo componentes previstos y la cascada resulta predecible.

**Errores frecuentes:** Usar IDs para todos los estilos o selectores globales que afectan controles no relacionados.

**Comprobación:** ¿Qué diferencia existe entre selector hijo y selector descendiente?

**Laboratorio de profundización — Selección y alcance de reglas CSS.**

1. Crea HTML con clases, ids, elementos y atributos. 2. Escribe selectores de tipo, clase, id, atributo y combinadores. 3. Usa DevTools para identificar reglas coincidentes. 4. Evalúa impacto de selectores demasiado amplios.

**Evidencia esperada.** Cada selector afecta exactamente los elementos previstos y su alcance está justificado.

**Seguridad y límites.** No depender de selectores frágiles basados en estructura accidental del DOM.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.02 — Cascade

La cascada decide qué declaración prevalece según origen, importancia, capa, especificidad y orden. Herencia y valores iniciales también influyen. Comprenderla evita resolver conflictos con `!important` indiscriminadamente.

**Ejemplo técnico:** Una regla de componente puede sobrescribir estilo heredado, pero una declaración importante puede alterar prioridades.

**Práctica guiada:** Crea dos reglas que compitan y predice el resultado antes de inspeccionarlo.

**Actividad independiente:** Organiza estilos por capas o convenciones para reducir conflictos.

**Criterios de aceptación:** Puedes explicar por qué gana cada declaración.

**Errores frecuentes:** Agregar `!important` sin investigar origen y especificidad.

**Comprobación:** ¿Qué factores principales intervienen en la cascada?

**Laboratorio de profundización — Resolución de cascada y origen.**

1. Define reglas en hoja externa, bloque style y atributo style en laboratorio. 2. Compara origen, importancia, capas y orden. 3. Inspecciona estilos computados. 4. Elimina !important innecesarios.

**Evidencia esperada.** Se explica por qué gana una declaración concreta considerando cascada y origen.

**Seguridad y límites.** No resolver todos los conflictos con !important ni estilos inline indiscriminados.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.03 — Specificity

La especificidad compara selectores mediante componentes de ID, clase/atributo/pseudoclase y tipo/pseudoelemento. No es el único factor de la cascada. `:where()` aporta especificidad cero y `:is()` toma la del selector más específico de sus argumentos.

**Ejemplo técnico:** `.nav a.active` tiene más especificidad que `a`, pero no necesariamente vence a una regla de mayor prioridad por origen/capa.

**Práctica guiada:** Calcula especificidad de cinco selectores y verifica con DevTools.

**Actividad independiente:** Reduce reglas con ID y construye estilos de componentes reutilizables.

**Criterios de aceptación:** Calcula y explica precedencia sin recurrir a prueba/error.

**Errores frecuentes:** Confundir número de clases con suma simple de todos los selectores o ignorar capas.

**Comprobación:** ¿Por qué una regla con mayor especificidad puede no ganar?

**Laboratorio de profundización — Cálculo de especificidad.**

1. Calcula especificidad de selectores de elemento, clase, id y :where(). 2. Compara dos reglas en conflicto. 3. Reestructura selectores para reducir acoplamiento. 4. Verifica resultado en DevTools.

**Evidencia esperada.** El cálculo es correcto y la solución evita aumentar especificidad sin necesidad.

**Seguridad y límites.** No usar IDs para todos los estilos ni encadenar selectores largos como mecanismo de prioridad.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.04 — Inheritance

Algunas propiedades CSS se heredan desde el elemento padre; otras no. color y font-family suelen heredarse, mientras margin, border y padding no. `inherit`, `initial`, `unset` y `revert` controlan valores según reglas distintas.

**Ejemplo técnico:** Un font-family en body puede aplicarse a descendientes; un margin de section no se transmite a sus hijos.

**Práctica guiada:** Prueba propiedades heredadas y no heredadas en árbol simple.

**Actividad independiente:** Define tipografía y color a nivel raíz y sobrescribe solo componentes necesarios.

**Criterios de aceptación:** Distingue herencia de cascada y aplica valores de forma deliberada.

**Errores frecuentes:** Suponer que todas las propiedades se heredan o usar inherit para arreglar cualquier conflicto.

**Comprobación:** ¿Por qué margin no suele heredarse?

**Laboratorio de profundización — Herencia y valores iniciales.**

1. Define color y font-family en contenedor. 2. Observa qué propiedades heredan. 3. Compara inherit, initial, unset y revert. 4. Identifica propiedades que no se heredan por defecto.

**Evidencia esperada.** Se distingue herencia de cascada y se predice el valor computado.

**Seguridad y límites.** No asumir que todas las propiedades CSS se heredan.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.05 — Box Model

El box model define content, padding, border y margin. Con content-box el width aplica al contenido; con border-box incluye padding y borde. Márgenes pueden colapsar en ciertos contextos y el modelo debe considerarse al calcular layout.

**Ejemplo técnico:** Con `box-sizing:border-box; width:200px`, el ancho declarado incluye padding y border.

**Práctica guiada:** Crea cajas con ambos box-sizing y mide dimensiones en DevTools.

**Actividad independiente:** Aplica border-box global y documenta excepciones.

**Criterios de aceptación:** Las dimensiones observadas coinciden con el modelo esperado.

**Errores frecuentes:** Olvidar padding/border al calcular ancho o compensar con márgenes arbitrarios.

**Comprobación:** ¿Qué cambia al aplicar border-box?

**Laboratorio de profundización — Cálculo de dimensiones.**

1. Crea un elemento con width, padding, border y margin. 2. Calcula tamaño exterior con content-box. 3. Aplica border-box y compara. 4. Verifica medidas en DevTools.

**Evidencia esperada.** Los cálculos coinciden con el modelo de caja y se explica box-sizing.

**Seguridad y límites.** No fijar anchuras que provoquen overflow en viewport pequeños.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.06 — Display

display determina cómo participa un elemento en layout: block, inline, inline-block, flex, grid, none y otros valores. `display:none` retira del árbol de layout y accesibilidad; visibility y opacity tienen efectos distintos.

**Ejemplo técnico:** Un botón inline-block permite dimensiones; un contenedor flex distribuye hijos en un eje.

**Práctica guiada:** Compara block, inline, inline-block y none en una página.

**Actividad independiente:** Selecciona display para una navegación sin alterar semántica.

**Criterios de aceptación:** Layout y comportamiento corresponden a objetivo.

**Errores frecuentes:** Usar display:none para contenido que debe estar disponible o forzar elementos inline a layout complejo.

**Comprobación:** ¿Qué diferencia práctica existe entre display:none y visibility:hidden?

**Laboratorio de profundización — Flujo y formato de cajas.**

1. Compara block, inline, inline-block, flex, grid y none. 2. Observa dimensiones y saltos de línea. 3. Evalúa visibility:hidden frente a display:none. 4. Relaciona presentación con orden del DOM.

**Evidencia esperada.** Se explica cómo cada valor afecta flujo y presencia visual/accesible.

**Seguridad y límites.** No alterar orden visual respecto del orden lógico de lectura y foco.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.07 — Position

position controla ubicación: static, relative, absolute, fixed y sticky. Los elementos absolute se posicionan respecto a un containing block; fixed suele referirse al viewport; sticky depende del contenedor de scroll y límites.

**Ejemplo técnico:** Un badge absolute dentro de una tarjeta relative se ubica respecto a la tarjeta.

**Práctica guiada:** Prueba cada modo en una página con scroll y observa containing block.

**Actividad independiente:** Diseña encabezado sticky sin ocultar contenido al enfocar enlaces.

**Criterios de aceptación:** Posición y foco no se superponen y el contenido permanece accesible.

**Errores frecuentes:** Usar fixed para todo o crear elementos que cubren controles al hacer zoom.

**Comprobación:** ¿Qué elemento sirve de referencia para un absolute?

**Laboratorio de profundización — Contexto de posicionamiento.**

1. Compara static, relative, absolute, fixed y sticky. 2. Identifica containing block y stacking context. 3. Prueba un menú superpuesto. 4. Evalúa comportamiento al hacer scroll y zoom.

**Evidencia esperada.** La posición se justifica por relación con contenedor y contexto de apilamiento.

**Seguridad y límites.** No ocultar contenido detrás de elementos fijos ni depender de z-index arbitrario.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.08 — Flexbox

Flexbox organiza elementos en una dimensión principal y una transversal. flex-direction, justify-content, align-items, gap y flex-wrap permiten distribuir espacio; tamaño base, shrink y grow determinan ajuste.

**Ejemplo técnico:** Una barra de acciones usa display:flex y gap; flex-wrap permite adaptarse a pantallas estrechas.

**Práctica guiada:** Crea una fila de tarjetas y prueba wrap, gap y alineación.

**Actividad independiente:** Construye header adaptable con logo y acciones.

**Criterios de aceptación:** No hay desbordamiento ni pérdida de orden lógico.

**Errores frecuentes:** Usar flexbox para estructuras bidimensionales complejas que requieren grid.

**Comprobación:** ¿Qué diferencia principal existe entre eje principal y transversal?

**Laboratorio de profundización — Distribución unidimensional.**

1. Crea una fila y columna con flex container. 2. Prueba justify-content, align-items, gap y flex-wrap. 3. Evalúa crecimiento y contracción de elementos. 4. Comprueba orden en viewport estrecho.

**Evidencia esperada.** La distribución funciona en ambos ejes y conserva orden de lectura.

**Seguridad y límites.** No usar order para crear un orden visual que contradiga secuencia semántica.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.09 — Grid

CSS Grid organiza layout en dos dimensiones mediante filas, columnas, tracks, áreas y gaps. Puede definir columnas flexibles, minmax y auto-fit/auto-fill. El contenido y el tamaño mínimo automático pueden provocar desbordamiento.

**Ejemplo técnico:** `grid-template-columns: repeat(auto-fit,minmax(15rem,1fr))` adapta tarjetas al ancho disponible.

**Práctica guiada:** Crea grid de tarjetas y prueba distintos anchos de viewport.

**Actividad independiente:** Diseña dashboard con áreas nombradas y fallback razonable.

**Criterios de aceptación:** Columnas y filas se adaptan sin scroll horizontal innecesario.

**Errores frecuentes:** Fijar anchos rígidos o confundir auto-fit y auto-fill sin probar.

**Comprobación:** ¿Cuándo es preferible Grid frente a Flexbox?

**Laboratorio de profundización — Diseño bidimensional con CSS Grid.**

1. Construye layout con columnas y filas. 2. Utiliza fr, minmax y repeat. 3. Define áreas nombradas. 4. Prueba auto-fit/auto-fill con distintos anchos.

**Evidencia esperada.** El layout responde al tamaño disponible sin desbordamiento y la estructura se mantiene comprensible.

**Seguridad y límites.** No fijar dimensiones rígidas que impidan zoom o reflujo.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.10 — Pseudoclases

Las pseudoclases seleccionan estados o relaciones, como :hover, :focus-visible, :checked, :disabled, :first-child y :not(). Deben incluir estados de interacción accesibles; no depender solo de hover porque pantallas táctiles y teclado difieren.

**Ejemplo técnico:** `:focus-visible` resalta controles al navegar con teclado sin forzar el mismo estilo en cada clic de ratón.

**Práctica guiada:** Prueba estados hover, focus-visible, checked y disabled en controles nativos.

**Actividad independiente:** Diseña estados de botón con contraste y foco visibles.

**Criterios de aceptación:** Cada estado es perceptible y no altera funcionalidad.

**Errores frecuentes:** Eliminar outline o usar solo hover como indicador de interacción.

**Comprobación:** ¿Por qué focus-visible es esencial en una interfaz accesible?

**Laboratorio de profundización — Estados de interacción.**

1. Implementa :hover, :focus-visible, :active, :checked y :disabled. 2. Comprueba teclado y puntero. 3. Define estados de formulario. 4. Verifica que focus no dependa de hover.

**Evidencia esperada.** Los estados son distinguibles y funcionan con diferentes modalidades de entrada.

**Seguridad y límites.** No ocultar foco ni comunicar estado solo mediante color.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.11 — Pseudoelementos

Los pseudoelementos como ::before, ::after, ::first-line y ::marker permiten estilizar partes sin agregar nodos DOM. El contenido generado no debe ser el único lugar donde se comunica información esencial.

**Ejemplo técnico:** Un icono decorativo ::before puede acompañar una etiqueta, pero el texto del estado debe existir en el DOM.

**Práctica guiada:** Añade marcadores visuales y revisa lectura sin CSS.

**Actividad independiente:** Crea indicador decorativo que no sustituya texto ni nombre accesible.

**Criterios de aceptación:** La información esencial permanece en el contenido DOM.

**Errores frecuentes:** Insertar mensajes importantes solo con content CSS.

**Comprobación:** ¿Por qué no debe dependerse de ::before para comunicar un error?

**Laboratorio de profundización — Contenido generado y decoración.**

1. Usa ::before y ::after para decoración. 2. Compara ::first-line y ::selection. 3. Comprueba lectura accesible del contenido generado. 4. Decide qué información debe permanecer en HTML.

**Evidencia esperada.** Los pseudoelementos se usan para presentación y el contenido esencial está en el DOM.

**Seguridad y límites.** No insertar instrucciones, etiquetas o datos críticos solo mediante content.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.12 — Variables

Custom properties CSS almacenan valores reutilizables y participan en cascada/herencia. Se declaran con `--nombre` y se consumen con var(), que admite fallback. Pueden definir tokens de color, espaciado, tipografía y temas.

**Ejemplo técnico:** `:root { --space-2: .5rem }` y `gap: var(--space-2)` centralizan consistencia.

**Práctica guiada:** Define tokens de color y espacio y cambia un tema en un contenedor.

**Actividad independiente:** Crea dos temas que reutilicen la misma estructura de componentes.

**Criterios de aceptación:** Tokens tienen nombres semánticos y fallback razonable.

**Errores frecuentes:** Nombrar variables por color literal y duplicar valores arbitrariamente.

**Comprobación:** ¿Qué ventaja ofrece un token semántico frente a repetir un valor hexadecimal?

**Laboratorio de profundización — Custom properties y temas.**

1. Define variables en :root. 2. Crea tema alternativo con atributo data-theme. 3. Usa fallback y alcance local. 4. Comprueba contraste y preferencia de color del sistema.

**Evidencia esperada.** Las variables permiten consistencia y los temas conservan contraste y legibilidad.

**Seguridad y límites.** No utilizar variables CSS para almacenar secretos ni asumir que sustituyen tokens de diseño documentados.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.13 — Media Queries

Media queries aplican estilos según viewport, preferencias y capacidades como prefers-reduced-motion o hover. Breakpoints deben surgir del contenido y no de modelos concretos de dispositivo.

**Ejemplo técnico:** `@media (max-width: 48rem)` puede reorganizar una navegación si el contenido deja de caber.

**Práctica guiada:** Prueba varios anchos y reduce motion en DevTools.

**Actividad independiente:** Define reglas responsive y respeta preferencia de movimiento reducido.

**Criterios de aceptación:** Contenido y controles siguen disponibles en distintos tamaños.

**Errores frecuentes:** Elegir breakpoints solo por marcas de teléfono o ignorar preferencias de usuario.

**Comprobación:** ¿Qué diferencia existe entre media query de viewport y prefers-reduced-motion?

**Laboratorio de profundización — Adaptación a condiciones del dispositivo.**

1. Crea breakpoints basados en contenido. 2. Usa media queries para ancho, orientación y prefers-reduced-motion. 3. Prueba zoom y viewport intermedio. 4. Registra comportamiento de cada breakpoint.

**Evidencia esperada.** Las reglas responden a necesidades reales del contenido y respetan preferencias de usuario.

**Seguridad y límites.** No diseñar solo para tamaños de dispositivos específicos ni desactivar zoom.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.14 — Responsive Design

Diseño responsive adapta estructura y contenido a tamaños y capacidades diversos mediante layouts fluidos, imágenes adaptables, tipografía flexible y media queries. Debe soportar zoom y orientación sin perder información.

**Ejemplo técnico:** Grid fluido, max-width y unidades relativas permiten adaptar tarjetas sin fijar cada dispositivo.

**Práctica guiada:** Prueba página a 320px, tablet y escritorio; verifica zoom al 200%.

**Actividad independiente:** Adapta una página con tabla, navegación y formulario para móvil.

**Criterios de aceptación:** No hay pérdida de contenido ni scroll horizontal injustificado.

**Errores frecuentes:** Ocultar información en móvil o usar tamaños rígidos que desbordan.

**Comprobación:** ¿Por qué responsive no significa simplemente reducir todo el tamaño?

**Laboratorio de profundización — Reflujo y adaptación progresiva.**

1. Construye layout móvil, tablet y escritorio. 2. Usa unidades flexibles, imágenes fluidas y max-width. 3. Comprueba a 320 CSS px y zoom. 4. Identifica scroll horizontal innecesario.

**Evidencia esperada.** El contenido refluye sin pérdida de información ni interacción a distintos anchos.

**Seguridad y límites.** No ocultar funciones esenciales en móvil ni usar escalas de texto ilegibles.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.15 — Animations

CSS animations define secuencias con @keyframes, duración, iteración y timing. El movimiento debe aportar significado, ser breve y respetar prefers-reduced-motion. Animaciones intensas pueden causar distracción o malestar.

**Ejemplo técnico:** Una transición de estado puede animar opacity; la alternativa reduced-motion elimina desplazamientos no esenciales.

**Práctica guiada:** Crea animación breve y prueba prefers-reduced-motion.

**Actividad independiente:** Diseña feedback de carga que también tenga alternativa estática.

**Criterios de aceptación:** Movimiento no esencial se reduce y no bloquea interacción.

**Errores frecuentes:** Animaciones infinitas intensas o transmitir estado solo mediante movimiento.

**Comprobación:** ¿Cómo debe responder la interfaz a prefers-reduced-motion?

**Laboratorio de profundización — Animaciones CSS accesibles.**

1. Anima un elemento decorativo con keyframes. 2. Limita duración y repeticiones. 3. Añade alternativa con prefers-reduced-motion. 4. Comprueba que la animación no distraiga ni bloquee interacción.

**Evidencia esperada.** La animación tiene propósito, duración moderada y respeta reducción de movimiento.

**Seguridad y límites.** No usar destellos rápidos ni animaciones persistentes sin control del usuario.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.16 — Transitions

Transitions interpolan cambios de propiedades entre estados. Deben especificar propiedades concretas, duración y curva; `transition: all` puede producir efectos inesperados y costos de mantenimiento.

**Ejemplo técnico:** Un botón puede transicionar background-color y transform en 150ms, sin animar dimensiones inesperadas.

**Práctica guiada:** Aplica transición a hover/focus y prueba con teclado.

**Actividad independiente:** Define transiciones consistentes con reducción de movimiento.

**Criterios de aceptación:** Solo propiedades necesarias se animan y la respuesta es inmediata.

**Errores frecuentes:** Usar duración excesiva o `transition: all`.

**Comprobación:** ¿Por qué es preferible indicar propiedades específicas en transition?

**Laboratorio de profundización — Transiciones de estado.**

1. Aplica transition a color, transform y opacity. 2. Define duración y easing. 3. Comprueba estado focus/hover/active. 4. Desactiva transición para reduced-motion.

**Evidencia esperada.** La transición refuerza feedback sin retrasar acciones ni ocultar estados.

**Seguridad y límites.** No animar propiedades costosas en grandes cantidades sin medir rendimiento.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.

#### 11.3.17 — Transformations

transform modifica representación visual mediante translate, scale, rotate o skew sin alterar el flujo normal. Puede crear contextos de apilamiento y afectar elementos posicionados. Debe evitarse ocultar foco o provocar desbordamiento.

**Ejemplo técnico:** translateY puede elevar una tarjeta al hover, pero su posición de layout no cambia.

**Práctica guiada:** Prueba transform y observa flujo, stacking context y foco.

**Actividad independiente:** Diseña microinteracción que no dependa solo de hover y no mueva contenido esencial.

**Criterios de aceptación:** Transformación no oculta controles ni rompe layout/zoom.

**Errores frecuentes:** Usar scale para texto pequeño o crear overlays que tapan foco.

**Comprobación:** ¿Por qué transform no modifica el espacio que el elemento ocupa en el flujo normal?


**Laboratorio de profundización — Transformaciones y contexto visual.**

1. Aplica translate, scale y rotate a elementos de prueba. 2. Compara transform-origin. 3. Observa stacking context y espacio ocupado. 4. Verifica que el contenido transformado no interfiera con controles.

**Evidencia esperada.** La transformación es visual y se comprenden sus efectos sobre composición y apilamiento.

**Seguridad y límites.** No depender de transform para ocultar controles fuera de pantalla ni crear solapamientos inaccesibles.

**Registro sugerido.** Conserva HTML/CSS mínimo, navegador y viewport, capturas de estilos computados, pruebas de teclado/zoom y observaciones de reflujo. No marques la práctica como ejecutada sin evidencia real.
#### 11.4.01 — Jerarquía visual

La jerarquía visual guía la atención mediante tamaño, peso, contraste, agrupación y posición; debe reflejar prioridades reales.

**Ejemplo técnico:** Título, resumen, acción principal y contenido secundario.

**Práctica guiada:** Audita una pantalla y marca el recorrido visual.

**Actividad independiente:** Rediseña una pantalla saturada sin eliminar información.

**Criterios de aceptación:** La prioridad visual coincide con la tarea principal.

**Errores frecuentes:** Usar color o tamaño como única señal.

**Comprobación:** ¿Cómo comprobarías que la jerarquía guía la tarea?

**Laboratorio de profundización — Auditoría de jerarquía visual.**

1. Selecciona una página de laboratorio. 2. Identifica objetivo principal, títulos, acciones y contenido secundario. 3. Ordena por peso visual, contraste, tamaño y posición. 4. Comprueba comprensión en escala de grises y zoom.

**Evidencia esperada.** El usuario identifica objetivo y acción principal sin depender de adornos ni color exclusivamente.

**Seguridad y límites.** No ocultar acciones importantes ni crear jerarquías engañosas.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.02 — Espaciado

El espaciado crea agrupación y ritmo. Una escala de tokens reduce variaciones y mejora consistencia.

**Ejemplo técnico:** Escala inicial 4/8/16/24 px adaptada al producto.

**Práctica guiada:** Mide distancias y clasifícalas por función.

**Actividad independiente:** Aplica escala a formulario y tarjetas.

**Criterios de aceptación:** Espaciados repetibles y jerarquía clara.

**Errores frecuentes:** Márgenes arbitrarios por elemento.

**Comprobación:** ¿Qué comunica un espacio menor entre elementos?

**Laboratorio de profundización — Sistema de espaciado consistente.**

1. Define escala modular de espaciado. 2. Aplica tokens a márgenes, padding y gaps. 3. Compara ritmo vertical y alineación entre componentes. 4. Prueba densidad en móvil y escritorio.

**Evidencia esperada.** Los espacios siguen una escala coherente y facilitan agrupación y lectura.

**Seguridad y límites.** No utilizar espaciado para sustituir agrupación semántica ni reducir áreas táctiles.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.03 — Tipografía

La tipografía afecta legibilidad y jerarquía; define familia, tamaño, peso, interlineado y longitud de línea.

**Ejemplo técnico:** Escala tipográfica con cuerpo legible y line-height suficiente.

**Práctica guiada:** Compara escalas y prueba zoom móvil.

**Actividad independiente:** Define tokens para títulos, cuerpo, código y ayuda.

**Criterios de aceptación:** Texto legible y jerarquía clara.

**Errores frecuentes:** Texto pequeño o líneas demasiado largas.

**Comprobación:** ¿Por qué importa la longitud de línea?

**Laboratorio de profundización — Sistema tipográfico y legibilidad.**

1. Define familias, tamaños, pesos y alturas de línea. 2. Establece escala fluida con unidades relativas. 3. Prueba zoom y ancho reducido. 4. Evalúa contraste y longitud de línea.

**Evidencia esperada.** El sistema mantiene legibilidad, jerarquía y adaptación a preferencias del usuario.

**Seguridad y límites.** No fijar tamaños en píxeles sin considerar zoom ni usar fuentes externas sin revisar licencia y rendimiento.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.04 — Layouts

Un layout distribuye regiones según tareas, contenido y viewport. Grid y Flexbox resuelven estructuras distintas.

**Ejemplo técnico:** Dashboard con navegación, área principal y panel contextual.

**Práctica guiada:** Dibuja wireframe para móvil y escritorio.

**Actividad independiente:** Implementa layout responsive con áreas.

**Criterios de aceptación:** Sin solapamiento y orden DOM lógico.

**Errores frecuentes:** Posicionar toda la página con absolute.

**Comprobación:** ¿Qué diferencia wireframe y layout implementado?

**Laboratorio de profundización — Composición de página por regiones.**

1. Diseña layout con header, nav, main, aside y footer. 2. Implementa con Grid o Flexbox. 3. Define comportamiento de aside en móvil. 4. Comprueba orden DOM y lectura.

**Evidencia esperada.** La composición es adaptable y el orden semántico coincide con el recorrido lógico.

**Seguridad y límites.** No cambiar orden visual para contradecir el orden de foco o lectura.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.05 — Componentes

Un componente encapsula estructura, estilo y comportamiento reutilizable; define variantes, estados, API y accesibilidad.

**Ejemplo técnico:** Botón con variantes, disabled/loading y foco visible.

**Práctica guiada:** Identifica componentes repetidos y estados.

**Actividad independiente:** Implementa tarjeta y botón documentados.

**Criterios de aceptación:** API coherente y semántica preservada.

**Errores frecuentes:** API excesiva o duplicación innecesaria.

**Comprobación:** ¿Qué estados debe documentar un componente?

**Laboratorio de profundización — Especificación de componente UI.**

1. Define un botón con variantes, estados y tamaños. 2. Documenta propiedades, eventos y comportamiento accesible. 3. Implementa estilos reutilizables. 4. Prueba hover, focus, disabled y loading.

**Evidencia esperada.** El componente tiene API consistente y estados visibles y accesibles.

**Seguridad y límites.** No crear componentes interactivos sin semántica nativa ni estado de foco.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.06 — Design Systems

Un design system reúne principios, tokens, componentes, patrones, documentación y gobierno; no es solo una librería visual.

**Ejemplo técnico:** Tokens de color/espacio alimentan componentes y plantillas.

**Práctica guiada:** Distingue token, componente y patrón.

**Actividad independiente:** Define contribución y versionado.

**Criterios de aceptación:** Reglas documentadas y criterios de calidad.

**Errores frecuentes:** Cambiar tokens sin evaluar impacto.

**Comprobación:** ¿Qué diferencia design system de librería de componentes?

**Laboratorio de profundización — Tokens y reglas de diseño.**

1. Define tokens de color, tipografía, espaciado, radios y sombras. 2. Crea componentes que consuman tokens. 3. Documenta criterios de uso. 4. Evalúa consistencia y cambio de tema.

**Evidencia esperada.** Los tokens reducen duplicación y permiten modificar el sistema de forma coherente.

**Seguridad y límites.** No copiar design systems protegidos sin licencia ni documentar tokens sin contraste validado.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.07 — Consistencia visual

La consistencia reduce carga cognitiva al mantener reglas previsibles. Excepciones deben justificarse por contexto.

**Ejemplo técnico:** Patrones equivalentes para confirmaciones y mensajes.

**Práctica guiada:** Compara pantallas y registra divergencias.

**Actividad independiente:** Define patrones y excepciones justificadas.

**Criterios de aceptación:** Acciones equivalentes se comunican de forma coherente.

**Errores frecuentes:** Uniformidad rígida o variaciones sin razón.

**Comprobación:** ¿Cuándo se justifica una excepción?

**Laboratorio de profundización — Revisión de patrones entre pantallas.**

1. Compara tres pantallas del mismo producto. 2. Identifica variaciones de botones, formularios, encabezados y espaciado. 3. Clasifica inconsistencia justificada y accidental. 4. Define correcciones priorizadas.

**Evidencia esperada.** Los patrones repetidos comparten comportamiento y apariencia, y las excepciones tienen motivo.

**Seguridad y límites.** No uniformar componentes que tienen propósitos o riesgos de interacción diferentes.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.4.08 — Mobile-first

Mobile-first inicia con restricciones de pantalla pequeña y amplía capacidades según espacio; prioriza contenido, navegación y rendimiento.

**Ejemplo técnico:** Una columna móvil puede convertirse en grid de tres columnas.

**Práctica guiada:** Prueba flujo a 320px antes de ampliar.

**Actividad independiente:** Diseña formulario móvil y adapta a escritorio.

**Criterios de aceptación:** Acciones disponibles sin pérdida ni scroll horizontal injustificado.

**Errores frecuentes:** Ocultar funciones clave en móvil.

**Comprobación:** ¿Por qué mobile-first no es solo reducir tamaños?

**Laboratorio de profundización — Diseño progresivo desde viewport pequeño.**

1. Diseña primero una pantalla estrecha. 2. Prioriza contenido y acciones. 3. Amplía con media queries para anchos mayores. 4. Comprueba teclado, zoom, orientación y áreas táctiles.

**Evidencia esperada.** La experiencia móvil conserva funciones esenciales y escala sin duplicar contenido innecesariamente.

**Seguridad y límites.** No eliminar contenido o controles en móvil solo para simplificar el layout.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.01 — Metadatos

Los metadatos describen documento, codificación, viewport, idioma y recursos. No todos afectan ranking; sí ayudan a interpretación y presentación.

**Ejemplo técnico:** charset, viewport y description cumplen propósitos distintos.

**Práctica guiada:** Inspecciona head de páginas y clasifica metadatos.

**Actividad independiente:** Define metadatos únicos para página de curso.

**Criterios de aceptación:** Valores precisos y coherentes.

**Errores frecuentes:** Repetir meta keywords como si determinara ranking.

**Comprobación:** ¿Qué metadatos configuran codificación y viewport?

**Laboratorio de profundización — Inventario de metadatos por página.**

1. Define charset, viewport, title, description, canonical y robots cuando aplique. 2. Identifica metadatos globales y específicos. 3. Comprueba consistencia entre URL y canonical. 4. Revisa vista previa social como metadato separado.

**Evidencia esperada.** Cada página tiene metadatos coherentes con su contenido y no existen instrucciones contradictorias de indexación.

**Seguridad y límites.** No utilizar canonical o noindex para ocultar contenido sensible; la seguridad se implementa en servidor.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.02 — Títulos

title identifica el documento en pestañas, marcadores y resultados; debe ser único, descriptivo y fiel.

**Ejemplo técnico:** «Guía de SQL: consultas y modelado | Academia».

**Práctica guiada:** Compara títulos genéricos y descriptivos.

**Actividad independiente:** Redacta títulos para cinco rutas.

**Criterios de aceptación:** Cada título distingue su página.

**Errores frecuentes:** Repetir title o rellenar keywords.

**Comprobación:** ¿Qué problema genera reutilizar title en todo el sitio?

**Laboratorio de profundización — Títulos únicos y descriptivos.**

1. Redacta title para página principal, categoría y detalle. 2. Mantén precisión y diferenciación. 3. Compara title con h1 visible. 4. Verifica duplicados en el conjunto de páginas.

**Evidencia esperada.** Cada título describe la página y ayuda a distinguirla de otras del sitio.

**Seguridad y límites.** No rellenar títulos con palabras clave repetidas ni prometer contenido que la página no contiene.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.03 — Descripciones

meta description resume contenido y puede influir en el fragmento mostrado, pero el buscador puede generar otro.

**Ejemplo técnico:** Descripción que resume objetivo y público de una lección.

**Práctica guiada:** Compara description con contenido real.

**Actividad independiente:** Redacta descripciones para landing y artículo.

**Criterios de aceptación:** Resumen preciso y diferenciado.

**Errores frecuentes:** Prometer contenido no existente o tratarlo como ranking garantizado.

**Comprobación:** ¿Por qué no se garantiza que el buscador muestre la description literal?

**Laboratorio de profundización — Meta description informativa.**

1. Redacta descripción específica para tres páginas. 2. Resume propósito y contenido sin afirmaciones engañosas. 3. Evita duplicados. 4. Comprueba que coincide con el contenido visible.

**Evidencia esperada.** La descripción es precisa y diferenciada y puede resumirse sin omitir la propuesta central.

**Seguridad y límites.** No tratar meta description como factor garantizado de ranking ni incluir información privada.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.04 — Estructura semántica

La semántica ayuda a tecnologías de asistencia y sistemas de indexación a interpretar contenido.

**Ejemplo técnico:** article con h1, secciones h2 y enlaces descriptivos.

**Práctica guiada:** Audita headings, landmarks y enlaces.

**Actividad independiente:** Reestructura un artículo y valida títulos.

**Criterios de aceptación:** Jerarquía lógica y enlaces comprensibles.

**Errores frecuentes:** Enlaces «clic aquí» o headings solo para keywords.

**Comprobación:** ¿Qué aporta un texto de enlace descriptivo?

**Laboratorio de profundización — Auditoría semántica de una página.**

1. Inspecciona landmarks, headings, enlaces, listas y tablas. 2. Comprueba main y jerarquía. 3. Revisa nombres accesibles. 4. Corrige divs usados como controles o encabezados.

**Evidencia esperada.** La estructura expresa contenido y navegación a usuarios y agentes automatizados.

**Seguridad y límites.** No insertar datos estructurados que contradigan el contenido visible.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.05 — Indexación

Indexación implica descubrir, rastrear, procesar y almacenar contenido. robots.txt controla rastreo, no protege información privada; noindex debe poder ser leído por crawler.

**Ejemplo técnico:** Una página bloqueada en robots.txt puede seguir conocida por enlaces, aunque el crawler no lea su noindex.

**Práctica guiada:** Inspecciona robots.txt y meta robots en un sitio de prueba.

**Actividad independiente:** Diseña política para páginas públicas, privadas y duplicadas.

**Criterios de aceptación:** Privacidad protegida por autenticación y controles reales.

**Errores frecuentes:** Usar robots.txt como seguridad.

**Comprobación:** ¿Por qué robots.txt no protege información privada?

**Laboratorio de profundización — Diagnóstico de indexabilidad.**

1. Revisa status HTTP, robots.txt, meta robots y canonical de una página propia. 2. Comprueba enlaces internos y sitemap. 3. Distingue rastreo de indexación. 4. Diseña prueba de URL en herramienta oficial si el sitio está autorizado.

**Evidencia esperada.** El diagnóstico identifica directivas y posibles bloqueos sin afirmar indexación por el mero hecho de que la URL exista.

**Seguridad y límites.** No utilizar robots.txt como mecanismo de confidencialidad ni solicitar indexación de contenido privado.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.

#### 11.5.06 — Datos estructurados (introducción)

Datos estructurados describen entidades mediante vocabularios como Schema.org y formatos como JSON-LD. Deben reflejar contenido real; no garantizan resultados enriquecidos.

**Ejemplo técnico:** Article con headline, author y datePublished cuando son datos reales.

**Práctica guiada:** Añade JSON-LD de artículo y valida sintaxis.

**Actividad independiente:** Diseña marcado para curso y omite datos no confirmados.

**Criterios de aceptación:** JSON válido y propiedades coherentes con contenido visible.

**Errores frecuentes:** Inventar reseñas, precios o autoría.

**Comprobación:** ¿Por qué el marcado debe coincidir con contenido visible?


**Laboratorio de profundización — Validación de JSON-LD básico.**

1. Selecciona un tipo de entidad aplicable, como Article o Product, solo si coincide con el contenido. 2. Construye JSON-LD con propiedades verificables. 3. Valida sintaxis y herramienta de resultados enriquecidos. 4. Compara datos marcados con contenido visible.

**Evidencia esperada.** El marcado representa hechos presentes en la página y pasa validación sintáctica y de tipo.

**Seguridad y límites.** No inventar ratings, precios, autoría o disponibilidad ni usar marcado engañoso para manipular resultados.

**Registro sugerido.** Conserva prototipo, criterios, navegador, viewport, validación automatizada y revisión manual. No marques conformidad o indexación como lograda sin evidencia real.
## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 60 orientaciones genéricas del desglose granular por explicaciones específicas de cada entrada oficial. Cada apartado precisa la función del concepto, decisiones de uso, límites y/o una comprobación contextual; el desarrollo se articula con la guía principal, el sitio profesional del proyecto y los ejercicios de accesibilidad/responsive.

**Revisión interna:** 60/60 entradas cubiertas y cotejadas con el roadmap. Se revisaron semántica HTML, formularios, SVG/Canvas, principios WCAG/ARIA, cascada, especificidad, modelos de layout, movimiento reducido, diseño de componentes y SEO. La revisión es documental, no certificación WCAG ni auditoría automatizada. Pendiente: validar el HTML/CSS con herramientas actuales, probar teclado y lector de pantalla, medir contraste, revisar responsive en navegadores y ejecutar el proyecto antes de aprobación externa.
