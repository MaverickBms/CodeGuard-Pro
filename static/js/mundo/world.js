/* Mapas de datos del Mundo CodeGuard.
 *
 * El motor no conoce mapas concretos: consume el registro MAPS. Para añadir
 * una región basta con registrar su constructor y sus entidades, sin tocar el
 * bucle de render ni el sistema de colisiones.
 */
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
  const FLOOR = 9;

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
        if (row >= 0 && row < grid.length && column >= 0 && column < grid[0].length) {
          grid[row][column] = tile;
        }
      }
    }
  }

  function house(grid, x, y, width, height) {
    rect(grid, x, y, width, height, WALL);
    rect(grid, x, y, width, 2, ROOF);
  }

  function emptyGrid(width, height, fill) {
    return Array.from({ length: height }, () =>
      Array.from({ length: width }, () => fill)
    );
  }

  function buildAldea() {
    const grid = emptyGrid(WIDTH, HEIGHT, GRASS);
    const random = seeded(20261119);

    rect(grid, 31, 0, 5, HEIGHT, WATER);
    rect(grid, 30, 11, 6, 3, BRIDGE);
    rect(grid, 4, 12, 27, 2, PATH);
    rect(grid, 15, 4, 2, 16, PATH);
    rect(grid, 13, 9, 6, 4, PLAZA);
    rect(grid, 13, 9, 6, 1, PATH);

    house(grid, 6, 4, 5, 4);
    house(grid, 21, 3, 6, 4);
    house(grid, 4, 16, 4, 4);
    house(grid, 23, 16, 5, 4);

    for (let y = 0; y < HEIGHT; y += 1) {
      for (let x = 0; x < WIDTH; x += 1) {
        const border = x < 2 || y < 2 || x > 33 || y > 21;
        if (border && grid[y][x] === GRASS) {
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

    const clear = [
      [14, 10], [14, 11], [13, 10], [15, 10],
      [10, 11], [10, 12], [8, 18], [8, 17],
      [28, 18], [27, 18], [5, 12], [23, 7], [23, 8]
    ];
    for (const [x, y] of clear) {
      if ([TREE, FLOWER, WALL, ROOF].includes(grid[y][x])) grid[y][x] = GRASS;
    }

    const objects = [
      { id: 'ada', tipo: 'npc', nombre: 'Mentora Ada', x: 14, y: 10, color: '#f59e0b' },
      { id: 'terminal', tipo: 'objeto', nombre: 'Terminal de práctica', x: 10, y: 11, color: '#38bdf8' },
      { id: 'puerta-biblioteca', tipo: 'puerta', nombre: 'Biblioteca de la Aldea', x: 23, y: 7, color: '#8b5e3c', target: 'biblioteca-aldear', targetX: 15, targetY: 17 },
      { id: 'guardian', tipo: 'npc', nombre: 'Guardián del Error', x: 8, y: 18, color: '#ef4444' },
      { id: 'cartel', tipo: 'objeto', nombre: 'Cartel de bienvenida', x: 5, y: 12, color: '#facc15' },
      { id: 'cofre', tipo: 'objeto', nombre: 'Cofre de la aldea', x: 28, y: 18, color: '#eab308' }
    ];

    return {
      id: 'aldea-metodo',
      name: 'Aldea del Método',
      width: WIDTH,
      height: HEIGHT,
      tile: TILE,
      grid,
      objects,
      spawn: { x: 15, y: 12 }
    };
  }

  function buildBiblioteca() {
    const width = 30;
    const height = 20;
    const grid = emptyGrid(width, height, FLOOR);
    rect(grid, 0, 0, width, 1, WALL);
    rect(grid, 0, height - 1, width, 1, WALL);
    rect(grid, 0, 0, 1, height, WALL);
    rect(grid, width - 1, 0, 1, height, WALL);
    rect(grid, 3, 2, 12, 1, WALL);
    rect(grid, 17, 2, 10, 1, WALL);
    rect(grid, 3, 2, 1, 7, WALL);
    rect(grid, 26, 2, 1, 7, WALL);
    rect(grid, 14, 18, 2, 1, PATH);

    // Mesas y alfombras decorativas (sin colisión).
    rect(grid, 11, 10, 8, 3, PLAZA);
    rect(grid, 4, 13, 4, 2, PATH);
    rect(grid, 22, 13, 4, 2, PATH);

    const objects = [
      { id: 'byte', tipo: 'npc', nombre: 'Bibliotecario Byte', x: 8, y: 6, color: '#a78bfa' },
      { id: 'estanteria-1', tipo: 'objeto', nombre: 'Estantería de documentación', x: 5, y: 4, color: '#8b5e3c' },
      { id: 'estanteria-2', tipo: 'objeto', nombre: 'Estantería de tutoriales', x: 6, y: 4, color: '#8b5e3c' },
      { id: 'estanteria-3', tipo: 'objeto', nombre: 'Estantería de foros', x: 7, y: 4, color: '#8b5e3c' },
      { id: 'nexo', tipo: 'npc', nombre: 'Nexo, mentor de lógica', x: 21, y: 12, color: '#22d3ee' },
      { id: 'salida-biblioteca', tipo: 'puerta', nombre: 'Salir a la aldea', x: 15, y: 18, color: '#8b5e3c', target: 'aldea-metodo', targetX: 23, targetY: 8 }
    ];

    return {
      id: 'biblioteca-aldear',
      name: 'Biblioteca de la Aldea',
      width,
      height,
      tile: TILE,
      grid,
      objects,
      spawn: { x: 15, y: 17 }
    };
  }

  const MAPS = {
    'aldea-metodo': buildAldea(),
    'biblioteca-aldear': buildBiblioteca()
  };

  function getMap(regionId) {
    return MAPS[regionId] || MAPS['aldea-metodo'];
  }

  root.CodeGuardMundoWorld = {
    TILE,
    TILES: { GRASS, PATH, WATER, TREE, WALL, ROOF, BRIDGE, FLOWER, PLAZA, FLOOR },
    MAPS,
    getMap,
    world: MAPS['aldea-metodo']
  };
})(typeof globalThis !== 'undefined' ? globalThis : this);
