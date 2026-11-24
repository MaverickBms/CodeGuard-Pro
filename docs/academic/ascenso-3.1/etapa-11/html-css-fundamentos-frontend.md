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

#### 11.1.02 — DOCTYPE

`<!doctype html>` activa el modo estándar; es una declaración, no un elemento.

**Ejemplo técnico:** Sin doctype el navegador puede activar quirks mode.

**Práctica guiada:** Compara archivos con y sin doctype.

**Actividad independiente:** Documenta por qué va al inicio.

**Criterios de aceptación:** Aparece antes de html.

**Errores frecuentes:** Escribirlo como etiqueta.

**Comprobación:** ¿Qué modo activa?

#### 11.1.03 — Head

head contiene metadatos, title y enlaces a recursos; no el contenido principal.

**Ejemplo técnico:** charset, viewport, title y description.

**Práctica guiada:** Añade y verifica metadatos.

**Actividad independiente:** Diseña head para una página de producto.

**Criterios de aceptación:** Metadatos pertinentes.

**Errores frecuentes:** Contenido visible dentro de head.

**Comprobación:** ¿Qué diferencia head de body?

#### 11.1.04 — Body

body contiene contenido, navegación, formularios y regiones semánticas.

**Ejemplo técnico:** header, nav, main y footer.

**Práctica guiada:** Organiza una página y revisa landmarks.

**Actividad independiente:** Reestructura una página hecha solo con div.

**Criterios de aceptación:** Jerarquía coherente.

**Errores frecuentes:** Duplicar landmarks sin nombre.

**Comprobación:** ¿Qué aporta semántica a lectores de pantalla?

#### 11.1.05 — Etiquetas

Los elementos expresan semántica y comportamiento; se eligen por función.

**Ejemplo técnico:** button para acción, a para navegación, p para párrafo.

**Práctica guiada:** Reemplaza div clicables por controles nativos.

**Actividad independiente:** Justifica cinco decisiones semánticas.

**Criterios de aceptación:** Elementos y comportamiento apropiados.

**Errores frecuentes:** Controles custom sin teclado.

**Comprobación:** ¿Por qué preferir button nativo?

#### 11.1.06 — Atributos

Los atributos configuran elementos; algunos son globales y otros específicos.

**Ejemplo técnico:** img usa src/alt; a usa href; input usa type/name; id es único.

**Práctica guiada:** Añade y valida atributos.

**Actividad independiente:** Audita formulario y galería.

**Criterios de aceptación:** Valores válidos e IDs únicos.

**Errores frecuentes:** Repetir id u omitir alt.

**Comprobación:** ¿Qué diferencia class de id?

#### 11.1.07 — HTML semántico

HTML semántico refleja función y jerarquía mediante elementos especializados.

**Ejemplo técnico:** main, nav, article y section.

**Práctica guiada:** Reestructura landing y revisa árbol accesible.

**Actividad independiente:** Diseña artículo técnico semántico.

**Criterios de aceptación:** Cada elemento se justifica por función.

**Errores frecuentes:** Usar section como div universal.

**Comprobación:** ¿Cuándo usar article?

#### 11.1.08 — Headings

h1–h6 expresan jerarquía; CSS controla apariencia.

**Ejemplo técnico:** h1 título, h2 capítulos, h3 subsecciones.

**Práctica guiada:** Corrige árbol de encabezados.

**Actividad independiente:** Esquema de títulos para una guía.

**Criterios de aceptación:** Niveles coherentes.

**Errores frecuentes:** Elegir nivel por tamaño.

**Comprobación:** ¿Por qué cambiar tamaño con CSS?

#### 11.1.09 — Sections

section agrupa contenido temático, normalmente con encabezado; div es genérico.

**Ejemplo técnico:** Objetivos, Contenido y Evaluación.

**Práctica guiada:** Clasifica contenedores.

**Actividad independiente:** Organiza documentación en secciones.

**Criterios de aceptación:** Propósito temático claro.

**Errores frecuentes:** Convertir todos los div en section.

**Comprobación:** ¿Qué distingue section de div?

#### 11.1.10 — Articles

article representa contenido autónomo y reutilizable.

**Ejemplo técnico:** Noticia con título, fecha y cuerpo.

**Práctica guiada:** Marca noticias y comprueba que tengan sentido aisladas.

**Actividad independiente:** Estructura un artículo técnico.

**Criterios de aceptación:** Contenido autónomo.

**Errores frecuentes:** Usar article para cualquier bloque.

**Comprobación:** ¿Qué característica justifica article?

#### 11.1.11 — Header

header contiene información introductoria o navegación; no es head.

**Ejemplo técnico:** Header global y header de artículo.

**Práctica guiada:** Identifica ambos contextos.

**Actividad independiente:** Diseña header responsive accesible.

**Criterios de aceptación:** Uso contextual.

**Errores frecuentes:** Ubicar header dentro de head.

**Comprobación:** ¿Qué diferencia head de header?

#### 11.1.12 — Footer

footer contiene información de cierre de página o sección.

**Ejemplo técnico:** Contacto global y autoría de artículo.

**Práctica guiada:** Incorpora ambos contextos.

**Actividad independiente:** Diseña pie con enlaces agrupados.

**Criterios de aceptación:** Contenido asociado al contexto.

**Errores frecuentes:** Usarlo como contenedor fijo sin semántica.

**Comprobación:** ¿Puede haber varios footer?

#### 11.1.13 — Nav

nav identifica una región principal de navegación; no todo grupo de enlaces lo requiere.

**Ejemplo técnico:** Navegación principal e índice con aria-label distinto.

**Práctica guiada:** Crea ambas regiones y recorre con teclado.

**Actividad independiente:** Diseña menú móvil accesible.

**Criterios de aceptación:** Regiones distinguibles.

**Errores frecuentes:** Envolver todos los enlaces en nav.

**Comprobación:** ¿Por qué nombrar dos nav?

#### 11.1.14 — Forms

form agrupa controles y define envío; requiere etiquetas y validación cliente/servidor.

**Ejemplo técnico:** Formulario con label, email y mensaje.

**Práctica guiada:** Construye y prueba con teclado.

**Actividad independiente:** Diseña inscripción con resumen de errores.

**Criterios de aceptación:** Campos etiquetados y validación servidor.

**Errores frecuentes:** Placeholder como única etiqueta.

**Comprobación:** ¿Por qué validar en servidor?

#### 11.1.15 — Inputs

input ofrece controles variados; el tipo debe reflejar el dato.

**Ejemplo técnico:** type=password oculta texto, pero no cifra transporte.

**Práctica guiada:** Crea email, fecha y checkbox etiquetados.

**Actividad independiente:** Selecciona tipos y autocomplete.

**Criterios de aceptación:** Tipo y etiqueta correctos.

**Errores frecuentes:** Usar number para códigos con ceros iniciales.

**Comprobación:** ¿Por qué un código postal suele ser texto?

#### 11.1.16 — Selects

select permite elegir opciones; option requiere texto y value estable.

**Ejemplo técnico:** País visible y código enviado.

**Práctica guiada:** Crea select etiquetado y prueba teclado.

**Actividad independiente:** Diseña opción Otra accesible.

**Criterios de aceptación:** Opciones claras.

**Errores frecuentes:** Usar placeholder como valor.

**Comprobación:** ¿Qué diferencia texto y value?

#### 11.1.17 — Textareas

textarea permite texto multilínea; label, ayuda y límites deben asociarse.

**Ejemplo técnico:** Descripción con maxlength y aria-describedby.

**Práctica guiada:** Crea campo con ayuda y límite.

**Actividad independiente:** Diseña contador accesible.

**Criterios de aceptación:** Etiqueta y errores accesibles.

**Errores frecuentes:** Confiar en maxlength como seguridad.

**Comprobación:** ¿Por qué escapar texto al mostrarlo?

#### 11.1.18 — Tables

Las tablas representan datos, no layout. caption, thead, tbody, th y scope relacionan encabezados.

**Ejemplo técnico:** Tabla de notas con encabezados de filas y columnas.

**Práctica guiada:** Semantiza tabla y revisa accesibilidad.

**Actividad independiente:** Diseña tabla con encabezados agrupados.

**Criterios de aceptación:** Caption y encabezados identificables.

**Errores frecuentes:** Usar tablas para maquetación.

**Comprobación:** ¿Qué aporta scope?

#### 11.1.19 — Multimedia

HTML integra imagen, audio y video; se requieren alt, subtítulos o transcripciones.

**Ejemplo técnico:** Video con controls y track captions.

**Práctica guiada:** Integra video de prueba con subtítulos.

**Actividad independiente:** Diseña galería accesible.

**Criterios de aceptación:** Alternativas y controles accesibles.

**Errores frecuentes:** Video sin subtítulos.

**Comprobación:** ¿Qué alternativa ofrecer si el dato solo está en audio?

#### 11.1.20 — SVG

SVG es vectorial basado en XML; gráficos informativos requieren nombre y descripción.

**Ejemplo técnico:** title/desc para gráfico; aria-hidden para icono decorativo.

**Práctica guiada:** Crea SVG con viewBox y alternativa.

**Actividad independiente:** Diseña gráfico con descripción y tabla.

**Criterios de aceptación:** No depende solo de color.

**Errores frecuentes:** Omitir alternativa.

**Comprobación:** ¿Por qué describir un gráfico?

#### 11.1.21 — Canvas

canvas dibuja mediante JavaScript, pero sus formas no son nodos DOM accesibles automáticamente.

**Ejemplo técnico:** Gráfico con tabla equivalente.

**Práctica guiada:** Dibuja datos y añade tabla HTML.

**Actividad independiente:** Diseña visualización con leyenda y alternativa.

**Criterios de aceptación:** Alternativa equivalente.

**Errores frecuentes:** Usar canvas como reemplazo de HTML.

**Comprobación:** ¿Qué pierde quien no percibe el bitmap sin alternativa?

#### 11.2.01 — WCAG
WCAG 2.2 organiza la accesibilidad en principios perceptible, operable, comprensible y robusto, con criterios verificables y niveles A, AA y AAA. Selecciona el nivel exigido por el producto o normativa, registra evidencia por criterio y no declares conformidad a partir de una única herramienta automática.


**Práctica y evidencia:** Evalúa una página con una lista de comprobación WCAG 2.2 AA para teclado, contraste, estructura y formularios. **Evidencia:** registra criterio, resultado y corrección, sin afirmar conformidad completa por una revisión parcial.

#### 11.2.02 — ARIA
ARIA añade roles, propiedades y estados para comunicar semántica a tecnologías de asistencia cuando HTML nativo no alcanza. Prioriza controles HTML estándar; un `role` no implementa teclado, foco ni comportamiento, por lo que un widget personalizado debe reproducir el patrón de interacción completo.


**Práctica y evidencia:** Usa ARIA solo donde HTML nativo no exprese el patrón; implementa un control expandible con estado actualizado. **Evidencia:** comprueba nombre, rol y estado con herramientas de accesibilidad.

#### 11.2.03 — Navegación por teclado
La navegación por teclado debe permitir alcanzar, operar y abandonar los controles sin ratón. Verifica orden de tabulación, foco visible, activación con Enter/Espacio según el control y gestión de foco en diálogos; no crees trampas ni elimines el indicador de foco.


**Práctica y evidencia:** Navega toda la interfaz solo con teclado y comprueba foco visible, orden lógico y ausencia de trampas. **Evidencia:** registra secuencia de Tab/Shift+Tab y puntos problemáticos.

#### 11.2.04 — Etiquetas accesibles
Una etiqueta accesible proporciona el nombre que una tecnología de asistencia anuncia para un control. Vincula `label` con `for`/`id` o utiliza el mecanismo semántico apropiado; el texto de ayuda y los errores deben asociarse al campo sin reemplazar su nombre.


**Práctica y evidencia:** Asocia cada campo con un nombre accesible y prueba el anuncio con tecnología de asistencia o inspector del navegador. **Evidencia:** muestra nombre y rol del control.

#### 11.2.05 — Contraste
El contraste compara la luminancia del primer plano y el fondo para comprobar legibilidad. Evalúa texto normal, texto grande, iconos y componentes de interfaz según WCAG; revisa también estados de foco, error y deshabilitado, y no comuniques información solo mediante color.


**Práctica y evidencia:** Mide contraste de texto normal, texto grande y controles contra sus fondos. **Evidencia:** registra ratios y umbrales aplicables; corrige combinaciones que no alcancen el criterio.

#### 11.2.06 — Lectores de pantalla
Un lector de pantalla anuncia nombres, roles, estados y relaciones expuestos por el árbol de accesibilidad. Prueba recorridos reales con al menos una combinación navegador/lector disponible, escucha el orden de lectura y corrige semántica antes de añadir atributos ARIA redundantes.


**Práctica y evidencia:** Recorre una página con lector de pantalla y compara el orden anunciado con el orden visual. **Evidencia:** identifica encabezados, landmarks y controles sin nombre.

#### 11.2.07 — Formularios accesibles
Un formulario accesible identifica cada campo, comunica requisitos, conserva datos y presenta errores comprensibles. Asocia mensajes con `aria-describedby` cuando corresponda, resume errores importantes y mueve el foco de manera predecible sin interrumpir innecesariamente al usuario.


**Práctica y evidencia:** Implementa mensajes de error asociados al campo y resumen de errores que no dependan solo del color. **Evidencia:** prueba formulario inválido mediante teclado y verifica anuncio comprensible.

#### 11.2.08 — HTML semántico
La semántica HTML proporciona estructura interoperable para encabezados, regiones, listas, tablas y controles. Comprueba el documento con el árbol de accesibilidad y utiliza elementos nativos antes de construir roles personalizados; una estructura correcta facilita teclado, lectores de pantalla e indexación.


**Práctica y evidencia:** Comprueba que regiones y controles usan elementos HTML semánticos antes de añadir roles ARIA. **Evidencia:** documenta un caso donde HTML nativo evita ARIA innecesario.

### Módulo 11.3 — CSS

#### 11.3.01 — Selectores
Los selectores CSS identifican elementos por tipo, clase, ID, atributo, estado o relación. Prefiere clases con significado de componente y selectores acotados; selectores globales complejos aumentan acoplamiento y hacen más difícil predecir qué regla afecta a cada elemento.


**Práctica y evidencia:** Crea reglas con selectores de elemento, clase, ID, atributo y combinadores. **Evidencia:** predice qué reglas coinciden con cada nodo y confirma en DevTools.

#### 11.3.02 — Cascade
La cascada decide qué declaración prevalece considerando origen, importancia, capas, especificidad y orden de aparición. Depurar CSS exige revisar la cascada completa y no asumir que la última regla siempre gana; herramientas del navegador muestran declaraciones aplicadas y sobrescritas.


**Práctica y evidencia:** Ordena dos reglas con igual especificidad y cambia su orden para observar la cascada. **Evidencia:** explica origen, importancia y orden de aparición.

#### 11.3.03 — Specificity
La especificidad es un peso comparativo de selectores dentro de la cascada, no una puntuación universal que resuelva todos los conflictos. Mantén selectores sencillos y evita encadenar IDs o `!important` para compensar una arquitectura de estilos desordenada.


**Práctica y evidencia:** Compara selectores de distinta especificidad y resuelve un conflicto sin recurrir automáticamente a `!important`. **Evidencia:** calcula la especificidad y justifica la regla ganadora.

#### 11.3.04 — Inheritance
La herencia transmite determinadas propiedades desde un elemento ancestro a sus descendientes, como algunas propiedades tipográficas y de color. Otras propiedades, como márgenes y bordes, normalmente no se heredan; utiliza `inherit`, `initial` y `unset` solo cuando la intención sea explícita.


**Práctica y evidencia:** Prueba herencia de `color` y `font-family` frente a propiedades no heredadas. **Evidencia:** identifica qué valores se heredan y cuándo conviene usar `inherit` o `initial`.

#### 11.3.05 — Box Model
El Box Model combina contenido, padding, borde y margen para determinar el espacio de un elemento. `box-sizing: border-box` hace que ancho y alto incluyan padding y borde, lo que simplifica layouts; prueba además el comportamiento con contenido largo y traducciones.


**Práctica y evidencia:** Construye tres cajas y observa content, padding, border y margin con DevTools. **Evidencia:** calcula el tamaño exterior con `content-box` y `border-box`.

#### 11.3.06 — Display
`display` determina cómo participa un elemento en el flujo y el layout: block, inline, flex, grid y otros valores tienen reglas distintas. No confundas `display: none` con ocultación visual: también elimina el elemento del árbol de accesibilidad en el uso habitual.


**Práctica y evidencia:** Compara `block`, `inline`, `inline-block`, `flex`, `grid` y `none` con elementos de prueba. **Evidencia:** explica cómo cambia el flujo y el espacio ocupado.

#### 11.3.07 — Position
`position` controla el posicionamiento estático, relativo, absoluto, fijo o sticky y define el contexto de referencia de elementos posicionados. Reserva `absolute` para elementos superpuestos que realmente lo necesiten y verifica que el contenido no se solape con zoom o pantallas estrechas.


**Práctica y evidencia:** Posiciona elementos con `static`, `relative`, `absolute`, `fixed` y `sticky`. **Evidencia:** identifica el containing block y el contexto de desplazamiento.

#### 11.3.08 — Flexbox
Flexbox distribuye elementos en un eje principal y otro transversal, con alineación y distribución flexibles. Practica `flex-direction`, `justify-content`, `align-items`, `gap`, `flex-wrap` y factores de crecimiento/reducción; prueba contenido de longitud variable para detectar desbordamientos.


**Práctica y evidencia:** Construye una barra flexible con `display:flex`, `gap`, `justify-content` y `align-items`. **Evidencia:** demuestra adaptación al cambiar el ancho del viewport.

#### 11.3.09 — Grid
Grid organiza elementos en dos dimensiones mediante tracks, líneas y áreas. Define columnas y filas con unidades flexibles como `fr`, funciones `minmax()` y `repeat()`; evita fijar dimensiones rígidas que impidan que el contenido crezca.


**Práctica y evidencia:** Diseña una cuadrícula de tarjetas con columnas responsivas y áreas nombradas. **Evidencia:** explica tracks, gaps y comportamiento en un viewport estrecho.

#### 11.3.10 — Pseudoclases
Las pseudoclases seleccionan elementos según estados o relaciones, como `:hover`, `:focus-visible`, `:checked` y `:first-child`. No dependas solo de hover, porque dispositivos táctiles y usuarios de teclado requieren estados equivalentes y visibles.


**Práctica y evidencia:** Aplica `:hover`, `:focus-visible`, `:checked` y `:disabled` a controles. **Evidencia:** verifica estados con ratón y teclado.

#### 11.3.11 — Pseudoelementos
Los pseudoelementos representan partes de un elemento o contenido generado, como `::before`, `::after` y `::placeholder`. El contenido generado es apropiado para decoración y señales complementarias, pero no debe contener la única etiqueta, instrucción o información crítica.


**Práctica y evidencia:** Añade un indicador decorativo con `::before` o `::after` sin introducir contenido esencial solo en CSS. **Evidencia:** confirma que el significado permanece disponible sin pseudo-elementos.

#### 11.3.12 — Variables
Las custom properties (`--token`) almacenan valores reutilizables y participan en la cascada. Define tokens semánticos para color, tipografía y espaciado, y cambia sus valores por tema o contexto; documenta valores de respaldo para propiedades que consumen variables.


**Práctica y evidencia:** Define tokens de color y espaciado en `:root` y reutilízalos en varios componentes. **Evidencia:** cambia un token y demuestra actualización coherente.

#### 11.3.13 — Media Queries
Las media queries aplican estilos según características del entorno, como ancho, orientación o preferencia de movimiento. Define breakpoints cuando el contenido lo necesite y prueba entre puntos de corte; evita asociar cada breakpoint a un modelo de dispositivo específico.


**Práctica y evidencia:** Crea breakpoints basados en el contenido y no en modelos concretos de dispositivo. **Evidencia:** registra el punto donde el layout deja de funcionar y justifica el breakpoint.

#### 11.3.14 — Responsive Design
Responsive design adapta contenido y layout a distintos tamaños, densidades y formas de interacción. Comprueba reflow, zoom, navegación, imágenes fluidas y tablas; el objetivo es que la tarea siga siendo posible, no que cada viewport tenga una copia visual idéntica.


**Práctica y evidencia:** Prueba una página en anchos móvil, tableta y escritorio, incluyendo zoom. **Evidencia:** demuestra ausencia de scroll horizontal no intencional y preservación de jerarquía.

#### 11.3.15 — Animations
CSS animations describen secuencias mediante `@keyframes` y propiedades de duración, retraso, iteración y dirección. Úsalas para comunicar cambios de estado con moderación, proporciona alternativas cuando el movimiento no sea esencial y respeta la preferencia de movimiento reducido.


**Práctica y evidencia:** Anima una propiedad no crítica y respeta `prefers-reduced-motion`. **Evidencia:** verifica movimiento normal y alternativa reducida.

#### 11.3.16 — Transitions
Transitions interpolan cambios de propiedades entre estados, por ejemplo al enfocar un botón. Anima solo propiedades adecuadas, evita transiciones excesivas y no retrases acciones o mensajes que deban percibirse inmediatamente.


**Práctica y evidencia:** Añade transiciones específicas para estados de interacción, evitando `transition: all`. **Evidencia:** comprueba duración, propiedad y comportamiento con movimiento reducido.

#### 11.3.17 — Transformations
Transformations modifican visualmente traslación, escala, rotación o inclinación sin cambiar necesariamente el flujo del documento. Considera el origen de transformación, el contexto de apilamiento y el movimiento reducido; no uses transformaciones para ocultar problemas de layout.


**Práctica y evidencia:** Aplica `transform` para desplazar o escalar un elemento sin alterar el flujo normal. **Evidencia:** explica el origen de transformación y verifica que el foco y contenido no queden ocultos.

### Módulo 11.4 — Diseño de interfaces

#### 11.4.01 — Jerarquía visual
La jerarquía visual establece prioridades mediante tamaño, peso, contraste, posición y agrupación. Diseña primero qué debe comprender y hacer el usuario; valida que la prioridad visual coincide con la importancia funcional y no depende únicamente de color o tamaño.


**Práctica y evidencia:** Ordena título, acción principal y contenido secundario mediante tamaño, peso y contraste. **Evidencia:** realiza una prueba de cinco segundos y pide identificar la acción prioritaria.

#### 11.4.02 — Espaciado
El espaciado organiza grupos y relaciones entre elementos. Define una escala consistente y utiliza espacio cercano para señalar pertenencia; comprueba densidad, alineación y respiración visual con contenido real, no solo con textos de muestra de longitud uniforme.


**Práctica y evidencia:** Define una escala de espaciado y aplícala entre secciones, componentes y controles. **Evidencia:** muestra consistencia sin márgenes arbitrarios repetidos.

#### 11.4.03 — Tipografía
La tipografía combina familia, tamaño, peso, altura de línea y longitud de lectura. Selecciona fuentes legibles, reserva estilos para jerarquías claras y verifica acentos, caracteres especiales, fallback y ampliación de texto sin pérdida de contenido.


**Práctica y evidencia:** Selecciona familias, tamaños, interlineado y longitud de línea para lectura prolongada. **Evidencia:** compara legibilidad en móvil y escritorio.

#### 11.4.04 — Layouts
Un layout distribuye regiones y contenido según una estructura visual y funcional. Elige Grid para organización bidimensional y Flexbox para distribución en un eje cuando encaje; documenta las restricciones y verifica que el orden visual no contradiga el orden del DOM.


**Práctica y evidencia:** Construye una página con encabezado, sidebar, contenido y panel auxiliar usando Grid o Flexbox. **Evidencia:** documenta cómo colapsa el layout en móvil.

#### 11.4.05 — Componentes
Un componente encapsula una unidad de interfaz con propósito, estructura, estilos, comportamiento y estados definidos. Establece entradas y salidas claras, evita dependencias globales innecesarias y documenta variantes, accesibilidad y comportamiento en error o carga.


**Práctica y evidencia:** Crea componentes visuales reutilizables para botón, tarjeta y campo de formulario. **Evidencia:** demuestra variantes y estados sin duplicar reglas inconexas.

#### 11.4.06 — Design Systems
Un design system reúne principios, tokens, componentes, patrones y documentación para mantener decisiones coherentes. No es solo una biblioteca de botones: incluye criterios de uso, accesibilidad, gobernanza y proceso para introducir cambios sin fragmentar la experiencia.


**Práctica y evidencia:** Define tokens, componentes, patrones y reglas de uso en un pequeño design system. **Evidencia:** muestra una pantalla construida únicamente con esos elementos.

#### 11.4.07 — Consistencia visual
La consistencia visual hace que componentes equivalentes se comporten y se vean de manera predecible. Define reglas para tipografía, color, espaciado, estados e iconografía y permite excepciones justificadas cuando el contexto de uso lo exige.


**Práctica y evidencia:** Compara varias páginas del mismo producto y corrige inconsistencias de tipografía, color, espaciado y controles. **Evidencia:** presenta una lista de decisiones unificadas.

#### 11.4.08 — Mobile-first
Mobile-first comienza por priorizar contenido y tareas bajo restricciones de espacio y amplía progresivamente. No significa reducir funciones en móvil; valida navegación, foco, objetivos táctiles y lectura en anchuras pequeñas y luego añade mejoras para pantallas mayores.


**Práctica y evidencia:** Diseña primero para una columna y mejora progresivamente para pantallas mayores. **Evidencia:** demuestra que contenido y acciones esenciales funcionan antes de añadir columnas.

### Módulo 11.5 — SEO

#### 11.5.01 — Metadatos
Los metadatos describen el documento para navegadores, buscadores y plataformas de compartición. Incluye codificación, viewport, idioma, título y descripción adecuados; nunca coloques secretos ni información personal que no deba hacerse pública.


**Práctica y evidencia:** Añade metadatos de idioma, viewport, título y descripción coherentes con el contenido real. **Evidencia:** inspecciona el HTML generado y corrige valores duplicados o ausentes.

#### 11.5.02 — Títulos
El elemento `title` identifica de forma concisa y única la página y suele aparecer en pestañas y resultados de búsqueda. Escribe títulos específicos, coherentes con el contenido y comprensibles fuera de contexto; no repitas una plantilla idéntica en todo el sitio.


**Práctica y evidencia:** Escribe títulos únicos, descriptivos y concisos para páginas distintas. **Evidencia:** compara título de navegador con encabezado principal y propósito de la página.

#### 11.5.03 — Descripciones
La meta description resume la utilidad de una página y puede utilizarse como fragmento en resultados, aunque el buscador puede generar otro. Redacta una descripción veraz, diferenciada y orientada al contenido real; no la trates como garantía de ranking.


**Práctica y evidencia:** Redacta descripciones que resuman la página sin prometer contenido inexistente ni repetir palabras clave artificialmente. **Evidencia:** verifica correspondencia entre descripción y contenido visible.

#### 11.5.04 — Estructura semántica
La estructura semántica facilita que personas, navegadores y motores comprendan las regiones y relaciones del contenido. Usa headings, enlaces descriptivos, landmarks y datos visibles coherentes; no añadas etiquetas solo para insertar palabras clave.


**Práctica y evidencia:** Comprueba que encabezados, landmarks y enlaces describan la estructura de la página. **Evidencia:** genera un esquema semántico y detecta regiones duplicadas o vacías.

#### 11.5.05 — Indexación
La indexación es el proceso por el que un buscador incorpora y puede recuperar contenido rastreado. Facilita descubrimiento mediante enlaces internos, sitemap cuando proceda y respuestas HTTP correctas; `robots.txt` no es un mecanismo de confidencialidad ni sustituye autenticación.


**Práctica y evidencia:** Revisa robots, enlaces internos, canonicals y respuestas HTTP en un sitio de prueba. **Evidencia:** distingue indexabilidad técnica de garantía de posicionamiento.

#### 11.5.06 — Datos estructurados (introducción)
Los datos estructurados describen entidades y propiedades con vocabularios como Schema.org, habitualmente en JSON-LD. Los valores deben coincidir con contenido visible y políticas del buscador; no inventes reseñas, precios, eventos o disponibilidad para intentar obtener resultados enriquecidos.



**Práctica y evidencia:** Añade datos estructurados únicamente cuando correspondan al contenido visible y al vocabulario admitido. **Evidencia:** valida el JSON-LD y explica que su presencia no garantiza un resultado enriquecido.

## Registro de desarrollo profundo y revisión editorial interna — 2026-11-24

Se sustituyeron las 60 orientaciones genéricas del desglose granular por explicaciones específicas de cada entrada oficial. Cada apartado precisa la función del concepto, decisiones de uso, límites y/o una comprobación contextual; el desarrollo se articula con la guía principal, el sitio profesional del proyecto y los ejercicios de accesibilidad/responsive.

**Revisión interna:** 60/60 entradas cubiertas y cotejadas con el roadmap. Se revisaron semántica HTML, formularios, SVG/Canvas, principios WCAG/ARIA, cascada, especificidad, modelos de layout, movimiento reducido, diseño de componentes y SEO. La revisión es documental, no certificación WCAG ni auditoría automatizada. Pendiente: validar el HTML/CSS con herramientas actuales, probar teclado y lector de pantalla, medir contraste, revisar responsive en navegadores y ejecutar el proyecto antes de aprobación externa.
