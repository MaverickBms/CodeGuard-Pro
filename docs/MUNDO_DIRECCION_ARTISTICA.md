# Mundo CodeGuard — dirección artística y pipeline

**Estado:** estándar de diseño y reglas de implementación.  
**Implementación actual:** sprites procedurales de 16×16, tiles de 16 px y mapas
de 36×24 / 30×20; no hay spritesheets externos.

## 1. Lenguaje visual

- **Pixel art top-down**, lectura clara a escala de ventana de escritorio.
- Paleta terrosa para exteriores (verdes, ocres, azules de agua) y piedra/madera
  para interiores.
- Contornos oscuros coherentes, sombras breves y luces cálidas en interiores.
- Personajes con silueta reconocible: cabeza ligeramente grande, cuerpo compacto,
  ropa y accesorio distintivo.
- Una identidad original: las referencias visuales del propietario orientan
  proporciones y atmósfera, pero **no se copian ni se redistribuyen**.

## 2. Formatos

| Elemento | Formato actual | Regla de expansión |
|---|---|---|
| Tile | 16×16 px | Un tileset por bioma/interior, sin mezclar escalas |
| Personaje | 16×24 px de caja lógica (sprite 16×16 dibujado) | Cuatro direcciones y dos frames de caminar |
| NPC | 16×16 | Misma línea de contorno y paleta base |
| Objeto | 16×16 | Ancla al suelo, sin sombras que invadan tiles vecinos |
| Retrato de diálogo | HTML/CSS o 32×32 futuro | No bloquear el juego si falta |
| Mapa general | SVG/CSS ilustrado | Nodos de región; no es un mapa jugable |

## 3. Animación

- Caminar: dos frames por dirección (contacto/impulso), alternancia a ~160 ms.
- Reposo: frame 0, con micro-oscilación opcional de un píxel.
- Interacción: destello de prompt y tono breve; no requiere frame extra.
- Diálogo: retrato estático y texto HTML.
- Combate/daño/celebración: **no implementados**; no simularlos hasta existir
  una mecánica real.
- `prefers-reduced-motion` desactiva animaciones no esenciales de la interfaz.

## 4. Paleta semántica

Los sprites usan colores propios del juego, no los HEX de los 12 temas de la
interfaz. La interfaz circundante conserva las variables `--cg-*` para mantener
la coherencia con CodeGuard Pro.

## 5. Pipeline de recursos

Estructura prevista para assets futuros:

```
static/assets/mundo/
├── tilesets/
│   ├── aldea.png
│   └── biblioteca.png
├── characters/
│   ├── hero/
│   └── npcs/
├── objects/
├── ui/
└── manifest.json
```

Reglas:

1. Cada asset debe declarar autor, licencia y fecha en `manifest.json`.
2. No se aceptan imágenes de referencia sin licencia de distribución.
3. Los sprites deben usar la misma cuadrícula de 16 px o un múltiplo exacto.
4. El motor debe cargar el manifiesto; nunca rutas sueltas desde el código de
   una región.
5. Si falta un asset, usar el sprite procedural de respaldo; nunca dejar el
   juego bloqueado.

Hoy los sprites se generan en `static/js/mundo/sprites.js`. Esa capa es el
respaldo oficial y la referencia de siluetas para futuros spritesheets.

## 6. Categorías de personajes previstas

Humanos y civilizaciones: guerreros, caballeros, reyes, reinas, príncipes,
princesas, nórdicos, vikingos, arqueros, exploradores, comerciantes, herreros,
alquimistas, bibliotecarios, investigadores y aventureros.

Mágicos: magos, hechiceros, druidas, brujas, sacerdotes, guardianes e
invocadores.

Otras especies: orcos, elfos, enanos, dragones y criaturas fantásticas.

No se implementan todos ahora. Cada nuevo personaje requiere:

- identificador estable;
- nombre, especie, profesión y facción;
- sprite/silueta diferenciada;
- diálogo y misión o función narrativa;
- ubicación y condiciones de aparición;
- pruebas de interacción y persistencia.

## 7. Criterios de aceptación visual

- Todos los personajes comparten contorno, escala y estilo de sombreado.
- Ningún sprite se ve borroso: `imageSmoothingEnabled = false` y escalado entero.
- Los edificios tienen entrada reconocible y conexión con su interior cuando
  exista.
- Los interiores incluyen mobiliario, iluminación y puntos de interés; no son
  habitaciones vacías con un NPC.
- El HUD no tapa el área jugable crítica a 1024×720 ni a 768×900.
- Los recursos sin licencia no se distribuyen.

## 8. Referencias y límites

Las cuatro imágenes aportadas por el propietario se tratan como **dirección
artística**, no como assets. No se han incorporado al repositorio ni se
redistribuyen. Cualquier recurso final debe ser original o tener licencia
compatible y quedar registrado en el manifiesto.
