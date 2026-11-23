'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const splashPath = path.join(__dirname, 'splash.html');
const html = fs.readFileSync(splashPath, 'utf8');
const main = fs.readFileSync(path.join(__dirname, 'main.js'), 'utf8');
const preload = fs.readFileSync(path.join(__dirname, 'preload.js'), 'utf8');

test('splash contiene elementos requeridos', () => {
  for (const token of ['CodeGuard Pro', 'id="spinner"', 'id="pct"', 'id="fill"', 'id="task"', 'id="detail"', 'id="phases"', 'id="quote"', 'id="errorBox"', 'role="status"']) {
    assert.ok(html.includes(token), `falta ${token}`);
  }
});

test('splash no depende de recursos externos', () => {
  assert.ok(!/https?:\/\//i.test(html), 'no debe tener URLs externas');
  assert.ok(!/<link[^>]+href="http/i.test(html), 'no debe enlazar CSS externo');
  assert.ok(!/<script[^>]+src="http/i.test(html), 'no debe cargar JS externo');
});

test('splash tiene spinner animado con prefers-reduced-motion', () => {
  assert.match(html, /@keyframes\s+spin/);
  assert.match(html, /prefers-reduced-motion/);
});

test('main.js mantiene seguridad Electron y señal explícita', () => {
  assert.match(main, /contextIsolation:\s*true/);
  assert.match(main, /nodeIntegration:\s*false/);
  assert.match(main, /sandbox:\s*true/);
  assert.match(main, /isTrustedIpcEvent\(event\)/);
  assert.match(main, /app-interactive-signal/);
  assert.match(main, /splash_window_shown/);
  assert.match(main, /splash_first_paint/);
  assert.match(main, /splash_dom_ready/);
  assert.match(main, /splash_document_loaded/);
});

test('preload expone señal interactiva y progreso de solo lectura', () => {
  assert.match(preload, /signalAppInteractive/);
  assert.match(preload, /onStartupProgress/);
  assert.doesNotMatch(preload, /ipcRenderer\.send\(['"](?!set-theme|show-notification|app-interactive-signal)/);
});
