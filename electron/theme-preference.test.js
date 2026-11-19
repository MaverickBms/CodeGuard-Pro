'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const os = require('os');
const path = require('path');

const { FILE_NAME, readTheme, writeTheme } = require('./theme-preference');

const THEMES = ['light', 'dark', 'high-contrast', 'fantasy'];

function temporaryFile() {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'cg-theme-'));
  return { directory, file: path.join(directory, FILE_NAME) };
}

test('devuelve el tema claro cuando no hay preferencia', () => {
  const { directory, file } = temporaryFile();
  assert.equal(readTheme(file, THEMES), 'light');
  fs.rmSync(directory, { recursive: true, force: true });
});

test('escribe y recupera un tema permitido', () => {
  const { directory, file } = temporaryFile();
  assert.equal(writeTheme(file, 'fantasy', THEMES), 'fantasy');
  assert.equal(readTheme(file, THEMES), 'fantasy');
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { theme: 'fantasy' });
  fs.rmSync(directory, { recursive: true, force: true });
});

test('rechaza temas fuera del catálogo', () => {
  const { directory, file } = temporaryFile();
  assert.throws(() => writeTheme(file, 'tema-inventado', THEMES), /Tema no permitido/);
  assert.equal(fs.existsSync(file), false);
  fs.rmSync(directory, { recursive: true, force: true });
});

test('degrada a fallback ante JSON corrupto o valor inválido', () => {
  const { directory, file } = temporaryFile();
  fs.writeFileSync(file, '{no-json');
  assert.equal(readTheme(file, THEMES), 'light');
  fs.writeFileSync(file, JSON.stringify({ theme: 'tema-inventado' }));
  assert.equal(readTheme(file, THEMES), 'light');
  fs.rmSync(directory, { recursive: true, force: true });
});

test('no deja archivos temporales tras escribir', () => {
  const { directory, file } = temporaryFile();
  writeTheme(file, 'dark', THEMES);
  const restantes = fs.readdirSync(directory);
  assert.deepEqual(restantes, [FILE_NAME]);
  fs.rmSync(directory, { recursive: true, force: true });
});
