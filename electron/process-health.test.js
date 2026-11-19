'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { getChildStartupFailure } = require('./process-health');

test('no informa fallo mientras el proceso sigue activo', () => {
  assert.equal(getChildStartupFailure({ exitCode: null, signalCode: null }), null);
});

test('informa errores de spawn', () => {
  const error = getChildStartupFailure({
    spawnError: new Error('EACCES'),
    exitCode: null,
    signalCode: null
  });
  assert.match(error.message, /EACCES/);
});

test('informa salida prematura con código', () => {
  const error = getChildStartupFailure({ exitCode: 7, signalCode: null });
  assert.match(error.message, /código 7/);
});

test('informa salida prematura por señal', () => {
  const error = getChildStartupFailure({ exitCode: null, signalCode: 'SIGTERM' });
  assert.match(error.message, /señal SIGTERM/);
});

test('rechaza un proceso hijo ausente', () => {
  assert.match(getChildStartupFailure(null).message, /no disponible/);
});
