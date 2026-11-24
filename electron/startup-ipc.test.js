'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { classifyInteractiveSignal, shouldAcceptInteractiveSignal, startupPhaseFromBootEvent } = require('./startup-ipc');

test('classifyInteractiveSignal: frontend-explicit es verificada', () => {
  assert.deepEqual(classifyInteractiveSignal({ source: 'frontend-explicit' }), { source: 'frontend-explicit', verified: true });
});

test('classifyInteractiveSignal: fallback no es verificada', () => {
  assert.deepEqual(classifyInteractiveSignal({ source: 'preload-fallback' }), { source: 'preload-fallback', verified: false });
  assert.deepEqual(classifyInteractiveSignal({}), { source: 'unknown', verified: false });
  assert.deepEqual(classifyInteractiveSignal(null), { source: 'unknown', verified: false });
});

test('shouldAcceptInteractiveSignal: rechaza no confiable, otra ventana, duplicado', () => {
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: false, senderIsMain: true, alreadyInteractive: false, alreadyFallback: false, verified: true }), { ok: false, reason: 'untrusted' });
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: true, senderIsMain: false, alreadyInteractive: false, alreadyFallback: false, verified: true }), { ok: false, reason: 'wrong-sender' });
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: true, senderIsMain: true, alreadyInteractive: true, alreadyFallback: false, verified: true }), { ok: false, reason: 'already-resolved' });
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: true, senderIsMain: true, alreadyInteractive: false, alreadyFallback: true, verified: false }), { ok: false, reason: 'already-resolved' });
});

test('shouldAcceptInteractiveSignal: permite upgrade de fallback por señal verificada', () => {
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: true, senderIsMain: true, alreadyInteractive: false, alreadyFallback: true, verified: true }), { ok: true, upgrade: true });
});

test('shouldAcceptInteractiveSignal: acepta señal válida de ventana principal', () => {
  assert.deepEqual(shouldAcceptInteractiveSignal({ trusted: true, senderIsMain: true, alreadyInteractive: false, alreadyFallback: false }), { ok: true });
});

test('startupPhaseFromBootEvent mapea fases conocidas', () => {
  assert.deepEqual(startupPhaseFromBootEvent({ phase: 'database', status: 'ready' }), { phase: 'database', status: 'done' });
  assert.deepEqual(startupPhaseFromBootEvent({ phase: 'roadmap', status: 'verifying' }), { phase: 'roadmap', status: 'active' });
  assert.deepEqual(startupPhaseFromBootEvent({ phase: 'services', status: 'error' }), { phase: 'services', status: 'error' });
  assert.equal(startupPhaseFromBootEvent({ phase: 'unknown', status: 'ready' }), null);
});
