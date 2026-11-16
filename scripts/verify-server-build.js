'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const root = path.resolve(__dirname, '..');
const serverDir = path.join(root, 'dist-server', 'CodeGuardServer');
const executableName = process.platform === 'win32' ? 'CodeGuardServer.exe' : 'CodeGuardServer';
const executablePath = path.join(serverDir, executableName);
const manifestPath = path.join(root, 'dist-server', '.codeguard-server-build.json');

function fail(message) {
  console.error(`[CodeGuard build] ERROR: ${message}`);
  process.exit(1);
}

if (!fs.existsSync(executablePath)) {
  fail(`No existe el servidor esperado: ${path.relative(root, executablePath)}. Ejecuta npm run build:server.`);
}
if (process.platform !== 'win32' && (fs.statSync(executablePath).mode & 0o111) === 0) {
  fail('El servidor existe, pero no tiene permisos de ejecución.');
}
if (!fs.existsSync(manifestPath)) {
  fail('Falta el manifiesto de la última compilación. No se permite empaquetar un servidor sin procedencia verificada.');
}

let manifest;
try {
  manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
} catch (_error) {
  fail('El manifiesto de compilación no es JSON válido.');
}

const actualHash = crypto.createHash('sha256').update(fs.readFileSync(executablePath)).digest('hex');
if (
  manifest.platform !== process.platform ||
  manifest.executable !== executableName ||
  manifest.sha256 !== actualHash
) {
  fail('El ejecutable no coincide con el manifiesto de la compilación actual. Reconstruye con npm run build:server.');
}

console.log(`[CodeGuard build] Servidor verificado: ${path.relative(root, executablePath)}`);
console.log(`[CodeGuard build] SHA-256: ${actualHash}`);
