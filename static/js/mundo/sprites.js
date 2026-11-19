/* Sprites procedurales de 16×16. Sin imágenes externas ni licencias de terceros. */
(function (root) {
  'use strict';

  const T = 16;

  function fill(ctx, x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
  }

  function drawGrass(ctx, x, y) {
    fill(ctx, x, y, T, T, '#78a75a');
    fill(ctx, x + 2, y + 5, 2, 2, '#6b9a4e');
    fill(ctx, x + 11, y + 11, 2, 2, '#8ab86a');
  }

  function drawPath(ctx, x, y) {
    fill(ctx, x, y, T, T, '#c2a878');
    fill(ctx, x + 3, y + 4, 3, 2, '#b09262');
    fill(ctx, x + 10, y + 11, 3, 2, '#d2b98a');
  }

  function drawWater(ctx, x, y, tick) {
    fill(ctx, x, y, T, T, '#2f6f9f');
    const offset = Math.floor(tick / 400) % 2 === 0 ? 0 : 4;
    fill(ctx, x + 2 + offset, y + 4, 6, 2, '#7ec8e3');
    fill(ctx, x + 8 - offset, y + 10, 5, 2, '#5aa9c9');
  }

  function drawTree(ctx, x, y) {
    fill(ctx, x, y, T, T, '#6b9a4e');
    fill(ctx, x + 6, y + 9, 4, 6, '#6b4a2f');
    fill(ctx, x + 2, y + 2, 12, 9, '#2f6b3a');
    fill(ctx, x + 4, y + 1, 8, 2, '#3e8349');
    fill(ctx, x + 4, y + 4, 3, 3, '#4c9a58');
  }

  function drawWall(ctx, x, y) {
    fill(ctx, x, y, T, T, '#a66b4f');
    fill(ctx, x, y + 7, T, 1, '#7d4b37');
    fill(ctx, x + 7, y, 1, 7, '#7d4b37');
    fill(ctx, x + 3, y + 8, 1, 8, '#7d4b37');
    fill(ctx, x + 12, y + 8, 1, 8, '#7d4b37');
  }

  function drawRoof(ctx, x, y) {
    fill(ctx, x, y, T, T, '#8f3b3b');
    fill(ctx, x, y + 5, T, 2, '#6f2b2b');
    fill(ctx, x, y + 11, T, 2, '#6f2b2b');
  }

  function drawBridge(ctx, x, y) {
    fill(ctx, x, y, T, T, '#b07a45');
    fill(ctx, x, y + 4, T, 2, '#8a5b30');
    fill(ctx, x, y + 11, T, 2, '#8a5b30');
  }

  function drawFlower(ctx, x, y) {
    fill(ctx, x, y, T, T, '#78a75a');
    fill(ctx, x + 6, y + 6, 4, 4, '#fef08a');
    fill(ctx, x + 7, y + 5, 2, 6, '#f472b6');
  }

  function drawPlaza(ctx, x, y) {
    fill(ctx, x, y, T, T, '#b7b7a8');
    fill(ctx, x + 1, y + 1, 6, 6, '#c9c9b9');
    fill(ctx, x + 9, y + 9, 6, 6, '#a3a394');
  }

  function drawTile(ctx, tile, x, y, tick) {
    switch (tile) {
      case 1: drawPath(ctx, x, y); break;
      case 2: drawWater(ctx, x, y, tick || 0); break;
      case 3: drawTree(ctx, x, y); break;
      case 4: drawWall(ctx, x, y); break;
      case 5: drawRoof(ctx, x, y); break;
      case 6: drawBridge(ctx, x, y); break;
      case 7: drawFlower(ctx, x, y); break;
      case 8: drawPlaza(ctx, x, y); break;
      default: drawGrass(ctx, x, y);
    }
  }

  function drawPlayer(ctx, px, py, direction, frame) {
    const bob = frame ? 1 : 0;
    fill(ctx, px + 3, py + 1 + bob, 10, 4, '#1e293b');
    fill(ctx, px + 4, py + 5 + bob, 8, 5, '#f2c6a0');
    fill(ctx, px + 4, py + 10 + bob, 8, 5, '#2563eb');
    fill(ctx, px + 3, py + 14, 3, 2, '#111827');
    fill(ctx, px + 10, py + 14, 3, 2, '#111827');
    if (direction === 'left') fill(ctx, px + 3, py + 6, 2, 2, '#111827');
    if (direction === 'right') fill(ctx, px + 11, py + 6, 2, 2, '#111827');
    if (direction === 'down') {
      fill(ctx, px + 6, py + 7, 1, 1, '#111827');
      fill(ctx, px + 9, py + 7, 1, 1, '#111827');
    }
  }

  function drawNpc(ctx, px, py, color, frame) {
    const bob = frame ? 1 : 0;
    fill(ctx, px + 4, py + 2 + bob, 8, 5, '#f2c6a0');
    fill(ctx, px + 3, py + 7 + bob, 10, 7, color);
    fill(ctx, px + 5, py + 5 + bob, 2, 2, '#111827');
    fill(ctx, px + 10, py + 5 + bob, 2, 2, '#111827');
    fill(ctx, px + 5, py + 14, 2, 2, '#111827');
    fill(ctx, px + 10, py + 14, 2, 2, '#111827');
  }

  function drawObject(ctx, id, px, py, color, tick) {
    if (id === 'terminal') {
      fill(ctx, px + 2, py + 3, 12, 9, '#334155');
      fill(ctx, px + 3, py + 4, 10, 6, '#38bdf8');
      fill(ctx, px + 6, py + 12, 4, 3, '#1e293b');
      if (Math.floor((tick || 0) / 500) % 2 === 0) fill(ctx, px + 5, py + 6, 5, 1, '#e0f2fe');
      return;
    }
    if (id.startsWith('estanteria')) {
      fill(ctx, px + 2, py + 1, 12, 14, '#6b4a2f');
      fill(ctx, px + 3, py + 3, 10, 3, '#c2a878');
      fill(ctx, px + 3, py + 8, 10, 3, '#c2a878');
      fill(ctx, px + 4, py + 3, 2, 3, color);
      fill(ctx, px + 8, py + 8, 2, 3, '#38bdf8');
      return;
    }
    if (id === 'cofre') {
      fill(ctx, px + 2, py + 6, 12, 8, '#8a5b30');
      fill(ctx, px + 2, py + 4, 12, 4, '#b07a45');
      fill(ctx, px + 7, py + 6, 2, 3, '#facc15');
      return;
    }
    if (id === 'cartel') {
      fill(ctx, px + 7, py + 7, 2, 8, '#6b4a2f');
      fill(ctx, px + 2, py + 2, 12, 6, '#facc15');
      fill(ctx, px + 4, py + 4, 8, 1, '#78350f');
      return;
    }
    fill(ctx, px + 2, py + 4, 12, 10, color);
  }

  function drawPrompt(ctx, px, py, tick) {
    const offset = Math.floor((tick || 0) / 300) % 2;
    fill(ctx, px + 5, py - 8 - offset, 6, 6, '#fef08a');
    fill(ctx, px + 7, py - 6 - offset, 2, 3, '#78350f');
  }

  root.CodeGuardMundoSprites = {
    T,
    drawTile,
    drawPlayer,
    drawNpc,
    drawObject,
    drawPrompt
  };
})(typeof globalThis !== 'undefined' ? globalThis : this);
