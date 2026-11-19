'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const os = require('os');
const path = require('path');

const { resolveBackupPath } = require('./restore-backup');

test('acepta un archivo ZIP regular existente', () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'cg-restore-'));
  const archive = path.join(directory, 'copia.zip');
  fs.writeFileSync(archive, 'zip');
  assert.equal(resolveBackupPath(archive), archive);
  fs.rmSync(directory, { recursive: true, force: true });
});

test('rechaza extensiones distintas de .zip', () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'cg-restore-'));
  const archive = path.join(directory, 'copia.txt');
  fs.writeFileSync(archive, 'texto');
  assert.equal(resolveBackupPath(archive), null);
  fs.rmSync(directory, { recursive: true, force: true });
});

test('rechaza rutas inexistentes y valores no textuales', () => {
  assert.equal(resolveBackupPath('/ruta/que-no-existe/copia.zip'), null);
  assert.equal(resolveBackupPath(''), null);
  assert.equal(resolveBackupPath(null), null);
  assert.equal(resolveBackupPath(42), null);
});

test('rechaza un directorio con extensión .zip', () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'cg-restore-'));
  const folder = path.join(directory, 'carpeta.zip');
  fs.mkdirSync(folder);
  assert.equal(resolveBackupPath(folder), null);
  fs.rmSync(directory, { recursive: true, force: true });
});
