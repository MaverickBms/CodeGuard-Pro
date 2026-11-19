# Etapa 11 — HTML y CSS: fundamentos profesionales del frontend

**Estado:** borrador didáctico v0.1.0.  
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
**Estado editorial:** borrador.
