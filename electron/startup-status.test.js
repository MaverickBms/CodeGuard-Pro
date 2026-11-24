'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const {
  BOOT_PREFIX,
  DEFAULT_STARTUP_TIMEOUT_MS,
  parseBootEvent,
  formatBootMessage,
  startupTimeoutMs,
  describeHealth
} = require('./startup-status');

test('parsea un evento de arranque válido y rechaza texto libre', () => {
  const event = parseBootEvent(`${BOOT_PREFIX}{"phase":"roadmap","status":"ready","stages":33}`);
  assert.deepEqual(event, { phase: 'roadmap', status: 'ready', stages: 33 });
  assert.equal(parseBootEvent('texto normal'), null);
  assert.equal(parseBootEvent(`${BOOT_PREFIX}no-json`), null);
  assert.equal(parseBootEvent(`${BOOT_PREFIX}{"phase":"x"}`), null);
});

test('formatea las fases principales sin inventar datos', () => {
  assert.match(formatBootMessage({ phase: 'database', status: 'start' }), /base de datos/i);
  assert.match(
    formatBootMessage({ phase: 'database', status: 'migrating', pending: 7 }),
    /7 migraciones/
  );
  const loaded = formatBootMessage({
    phase: 'roadmap',
    status: 'loaded',
    stages: 33,
    modules: 212,
    lessons: 1946
  });
  assert.match(loaded, /33 etapas/);
  assert.match(loaded, /1\.946 lecciones/);
  assert.equal(formatBootMessage({ phase: 'desconocida', status: 'x' }), '');
});

test('el límite de espera es configurable y está acotado', () => {
  assert.equal(startupTimeoutMs({}), DEFAULT_STARTUP_TIMEOUT_MS);
  assert.equal(startupTimeoutMs({ CODEGUARD_STARTUP_TIMEOUT_MS: '60000' }), 60000);
  assert.equal(startupTimeoutMs({ CODEGUARD_STARTUP_TIMEOUT_MS: '1' }), DEFAULT_STARTUP_TIMEOUT_MS);
  assert.equal(startupTimeoutMs({ CODEGUARD_STARTUP_TIMEOUT_MS: '999999' }), DEFAULT_STARTUP_TIMEOUT_MS);
});

test('describe el health pendiente sin exponer detalles internos', () => {
  assert.equal(describeHealth({ database: 'ok', migrations: 'ok', roadmap: 'ok' }), '');
  assert.match(
    describeHealth({ database: 'ok', migrations: 'pending', roadmap: 'missing' }),
    /migraciones: pending/
  );
  assert.equal(describeHealth(null), '');
});
