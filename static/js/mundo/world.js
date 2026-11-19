/* Mapa y entidades de la Aldea del Método (prototipo vertical). */
(function (root) {
  'use strict';

  const WIDTH = 36;
  const HEIGHT = 24;
  const TILE = 16;
  const GRASS = 0;
  const PATH = 1;
  const WATER = 2;
  const TREE = 3;
  const WALL = 4;
  const ROOF = 5;
  const BRIDGE = 6;
  const FLOWER = 7;
  const PLAZA = 8;

  function seeded(seed) {
    let value = seed >>> 0;
    return function next() {
      value = (value * 1664525 + 1013904223) >>> 0;
      return value / 4294967296;
    };
  }

  function rect(grid, x, y, width, height, tile) {
    for (let row = y; row < y + height; row += 1) {
      for (let column = x; column < x + width; column += 1) {
        if (row >= 0 && row < HEIGHT && column >= 0 && column < WIDTH) {
          grid[row][column] = tile;
        }
      }
    }
  }

  function house(grid, x, y, width, height) {
    rect(grid, x, y, width, height, WALL);
    rect(grid, x, y, width, 2, ROOF);
  }

  function build() {
    const grid = Array.from({ length: HEIGHT }, () =>
      Array.from({ length: WIDTH }, () => GRASS)
    );
    const random = seeded(20261119);

    // Río y puente.
    rect(grid, 31, 0, 5, HEIGHT, WATER);
    rect(grid, 30, 11, 6, 3, BRIDGE);

    // Caminos principales y plaza.
    rect(grid, 4, 12, 27, 2, PATH);
    rect(grid, 15, 4, 2, 16, PATH);
    rect(grid, 13, 9, 6, 4, PLAZA);
    rect(grid, 13, 9, 6, 1, PATH);

    // Edificios.
    house(grid, 6, 4, 5, 4);
    house(grid, 21, 3, 6, 4);
    house(grid, 4, 16, 4, 4);
    house(grid, 23, 16, 5, 4);

    // Bosque perimetral y decoración determinista.
    for (let y = 0; y < HEIGHT; y += 1) {
      for (let x = 0; x < WIDTH; x += 1) {
        const borde = x < 2 || y < 2 || x > 33 || y > 21;
        if (borde && grid[y][x] === GRASS) {
          grid[y][x] = TREE;
        } else if (
          grid[y][x] === GRASS &&
          random() < 0.045 &&
          !(x > 11 && x < 20 && y > 8 && y < 14)
        ) {
          grid[y][x] = random() < 0.55 ? TREE : FLOWER;
        }
      }
    }

    // Despejar accesos a objetos y NPC.
    const clear = [
      [14, 10], [14, 11], [13, 10], [15, 10],
      [10, 11], [10, 12], [20, 8], [21, 8], [19, 8],
      [8, 18], [8, 17], [28, 18], [27, 18], [5, 12]
    ];
    for (const [x, y] of clear) {
      if (grid[y][x] === TREE || grid[y][x] === FLOWER) grid[y][x] = GRASS;
    }

    const objects = [
      { id: 'ada', tipo: 'npc', nombre: 'Mentora Ada', x: 14, y: 10, color: '#f59e0b' },
      { id: 'terminal', tipo: 'objeto', nombre: 'Terminal de práctica', x: 10, y: 11, color: '#38bdf8' },
      { id: 'byte', tipo: 'npc', nombre: 'Bibliotecario Byte', x: 20, y: 8, color: '#a78bfa' },
      { id: 'estanteria-1', tipo: 'objeto', nombre: 'Estantería de documentación', x: 21, y: 8, color: '#8b5e3c' },
      { id: 'estanteria-2', tipo: 'objeto', nombre: 'Estantería de tutoriales', x: 22, y: 8, color: '#8b5e3c' },
      { id: 'estanteria-3', tipo: 'objeto', nombre: 'Estantería de foros', x: 23, y: 8, color: '#8b5e3c' },
      { id: 'guardian', tipo: 'npc', nombre: 'Guardián del Error', x: 8, y: 18, color: '#ef4444' },
      { id: 'cartel', tipo: 'objeto', nombre: 'Cartel de bienvenida', x: 5, y: 12, color: '#facc15' },
      { id: 'cofre', tipo: 'objeto', nombre: 'Cofre de la aldea', x: 28, y: 18, color: '#eab308' }
    ];

    return {
      width: WIDTH,
      height: HEIGHT,
      tile: TILE,
      grid,
      objects,
      spawn: { x: 15, y: 12 }
    };
  }

  const world = build();
  root.CodeGuardMundoWorld = {
    TILE,
    TILES: { GRASS, PATH, WATER, TREE, WALL, ROOF, BRIDGE, FLOWER, PLAZA },
    world
  };
})(typeof globalThis !== 'undefined' ? globalThis : this);
