'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');

const Model = require('../../../static/js/mundo/model');
require('../../../static/js/mundo/world');

const world = globalThis.CodeGuardMundoWorld.world;

test('el mapa tiene dimensiones y spawn válidos', () => {
  assert.equal(world.width, 36);
  assert.equal(world.height, 24);
  assert.equal(world.grid.length, world.height);
  assert.equal(world.grid[0].length, world.width);
  assert.equal(Model.isWalkable(world, world.spawn.x, world.spawn.y), true);
});

test('los límites y tiles sólidos bloquean el movimiento', () => {
  assert.equal(Model.isWalkable(world, -1, 0), false);
  assert.equal(Model.isWalkable(world, 0, -1), false);
  assert.equal(Model.isWalkable(world, world.width, 0), false);
  assert.equal(Model.isWalkable(world, 31, 0), false); // agua
});

test('moveWithCollision no atraviesa un tile sólido', () => {
  const map = {
    width: 3,
    height: 3,
    grid: [
      [0, 2, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
  };
  const next = Model.moveWithCollision(map, 0.5, 0.5, 0.6, 0, 0.2);
  assert.ok(next.x < 1);
});

test('la cámara queda dentro de los límites del mapa', () => {
  assert.deepEqual(Model.cameraFor({ x: 0, y: 0 }, 10, 8, 20, 16), { x: 0, y: 0 });
  assert.deepEqual(Model.cameraFor({ x: 20, y: 16 }, 10, 8, 20, 16), { x: 10, y: 8 });
  assert.deepEqual(Model.cameraFor({ x: 10, y: 8 }, 10, 8, 20, 16), { x: 5, y: 4 });
});

test('la interacción elige el objeto más cercano dentro del alcance', () => {
  const objects = [
    { id: 'lejos', x: 10, y: 10 },
    { id: 'cerca', x: 2, y: 2 },
    { id: 'inactivo', x: 1, y: 1, disabled: true }
  ];
  const found = Model.nearestInteractable({ x: 1.5, y: 1.5 }, objects, 2);
  assert.equal(found.id, 'cerca');
});

test('dirección y formato de tiempo son estables', () => {
  assert.equal(Model.directionFromDelta(-1, 0), 'left');
  assert.equal(Model.directionFromDelta(0, 1), 'down');
  assert.equal(Model.formatTime(65), '01:05');
  assert.equal(Model.formatTime(-1), '00:00');
});

test('los objetos del mapa tienen identificadores únicos', () => {
  const ids = world.objects.map((item) => item.id);
  assert.equal(new Set(ids).size, ids.length);
  for (const item of world.objects) {
    assert.equal(Model.isWalkable(world, item.x, item.y), true, item.id);
  }
});
