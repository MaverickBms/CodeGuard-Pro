'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { createStartupProgress } = require('./startup-progress');

test('el progreso avanza por fases reales y no retrocede', () => {
  const p = createStartupProgress({ now: () => 1000, random: () => 0 });
  let s = p.update({ phase: 'electron', status: 'active', task: 'A' });
  assert.ok(s.percent > 0);
  const pct = s.percent;
  s = p.update({ phase: 'electron', status: 'done' });
  assert.ok(s.percent >= pct);
  const pct2 = s.percent;
  s = p.update({ phase: 'database', status: 'active' });
  assert.ok(s.percent >= pct2);
});

test('no llega al 100% antes de interactiva', () => {
  const p = createStartupProgress({ now: () => 1000, random: () => 0 });
  for (const id of ['electron','database','profile','roadmap','services','ui']) {
    p.update({ phase: id, status: 'done' });
  }
  const s = p.snapshot();
  assert.equal(s.interactive, false);
  assert.ok(s.percent <= 99);
  const done = p.update({ interactive: true, phase: 'ui', status: 'done' });
  assert.equal(done.percent, 100);
  assert.equal(done.interactive, true);
});

test('maneja eventos fuera de orden y duplicados', () => {
  const p = createStartupProgress({ now: () => 1000, random: () => 0 });
  p.update({ phase: 'roadmap', status: 'done' });
  p.update({ phase: 'database', status: 'active' });
  p.update({ phase: 'database', status: 'active' });
  p.update({ phase: 'roadmap', status: 'done' });
  const s = p.snapshot();
  assert.equal(s.phases.find(x => x.id === 'roadmap').status, 'done');
  assert.equal(s.phases.find(x => x.id === 'database').status, 'active');
  assert.ok(s.percent >= 0 && s.percent <= 99);
});

test('registra error sin avanzar ficticiamente a completado', () => {
  const p = createStartupProgress({ now: () => 1000, random: () => 0 });
  p.update({ phase: 'services', status: 'active' });
  const before = p.snapshot().percent;
  const s = p.update({ phase: 'services', status: 'error', error: 'falló' });
  assert.equal(s.phases.find(x => x.id === 'services').status, 'error');
  assert.match(s.error, /falló/);
  assert.ok(s.percent <= 99);
  assert.ok(s.percent >= 0);
});

test('las frases no se repiten inmediatamente y respetan intervalo', () => {
  let t = 0;
  const p = createStartupProgress({ now: () => t, random: () => 0, quoteIntervalMs: 15000, quotes: [{t:'A'},{t:'B'},{t:'C'}] });
  const q1 = p.update({ forceQuote: true }).quote;
  const q2 = p.update({ forceQuote: true }).quote;
  assert.notEqual(q1, q2);
  t = 1000;
  const q3 = p.update({}).quote;
  assert.equal(q3, undefined);
  t = 20000;
  const q4 = p.update({}).quote;
  assert.ok(typeof q4 === 'string');
});
