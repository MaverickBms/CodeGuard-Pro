/* Utilidades puras del Mundo CodeGuard.
 * UMD ligero: funciona como script clásico en Electron y con require() en Node.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.CodeGuardMundoModel = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const SOLID_TILES = new Set([2, 3, 4, 5]);

  function isInside(map, x, y) {
    return Number.isInteger(x) && Number.isInteger(y) &&
      x >= 0 && y >= 0 && x < map.width && y < map.height;
  }

  function tileAt(map, x, y) {
    if (!isInside(map, x, y)) return 2;
    return map.grid[y][x];
  }

  function isWalkable(map, x, y) {
    return isInside(map, x, y) && !SOLID_TILES.has(tileAt(map, x, y));
  }

  function rectsOverlap(a, b) {
    return a.x < b.x + b.w && a.x + a.w > b.x &&
      a.y < b.y + b.h && a.y + a.h > b.y;
  }

  function collideCircleRect(cx, cy, radius, rect) {
    const nearestX = Math.max(rect.x, Math.min(cx, rect.x + rect.w));
    const nearestY = Math.max(rect.y, Math.min(cy, rect.y + rect.h));
    const dx = cx - nearestX;
    const dy = cy - nearestY;
    return dx * dx + dy * dy < radius * radius;
  }

  function moveWithCollision(map, x, y, dx, dy, radius = 0.28) {
    const next = { x, y };
    const candidateX = x + dx;
    const tileX = Math.floor(candidateX);
    if (
      isWalkable(map, tileX, Math.floor(y - radius)) &&
      isWalkable(map, tileX, Math.floor(y + radius))
    ) {
      next.x = candidateX;
    }
    const candidateY = y + dy;
    const tileY = Math.floor(candidateY);
    if (
      isWalkable(map, Math.floor(next.x - radius), tileY) &&
      isWalkable(map, Math.floor(next.x + radius), tileY)
    ) {
      next.y = candidateY;
    }
    return next;
  }

  function cameraFor(target, viewportWidth, viewportHeight, mapWidth, mapHeight) {
    const halfW = viewportWidth / 2;
    const halfH = viewportHeight / 2;
    return {
      x: Math.max(0, Math.min(target.x - halfW, mapWidth - viewportWidth)),
      y: Math.max(0, Math.min(target.y - halfH, mapHeight - viewportHeight))
    };
  }

  function distance(ax, ay, bx, by) {
    return Math.hypot(ax - bx, ay - by);
  }

  function nearestInteractable(player, objects, maxDistance = 1.5) {
    let best = null;
    let bestDistance = maxDistance;
    for (const object of objects) {
      if (object.disabled) continue;
      const d = distance(player.x, player.y, object.x + 0.5, object.y + 0.5);
      if (d <= bestDistance) {
        best = object;
        bestDistance = d;
      }
    }
    return best;
  }

  function directionFromDelta(dx, dy, fallback = 'down') {
    if (Math.abs(dx) > Math.abs(dy)) return dx < 0 ? 'left' : 'right';
    if (Math.abs(dy) > 0) return dy < 0 ? 'up' : 'down';
    return fallback;
  }

  function clampInt(value, min, max) {
    return Math.max(min, Math.min(max, Math.trunc(value)));
  }

  function formatTime(totalSeconds) {
    const seconds = Math.max(0, Math.trunc(totalSeconds || 0));
    const minutes = Math.floor(seconds / 60);
    return `${String(minutes).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;
  }

  function questStatusLabel(status) {
    return ({
      disponible: 'Disponible',
      en_progreso: 'En progreso',
      lista: 'Lista para reclamar',
      completada: 'Completada'
    })[status] || 'Disponible';
  }

  return {
    SOLID_TILES,
    isInside,
    tileAt,
    isWalkable,
    rectsOverlap,
    collideCircleRect,
    moveWithCollision,
    cameraFor,
    distance,
    nearestInteractable,
    directionFromDelta,
    clampInt,
    formatTime,
    questStatusLabel
  };
});
