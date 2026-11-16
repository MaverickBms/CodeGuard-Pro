'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const distDir = path.join(root, 'dist-server');
const serverDir = path.join(distDir, 'CodeGuardServer');
const executableName = process.platform === 'win32' ? 'CodeGuardServer.exe' : 'CodeGuardServer';
const executablePath = path.join(serverDir, executableName);
const manifestPath = path.join(distDir, '.codeguard-server-build.json');

function fail(message) {
  console.error(`[CodeGuard build] ERROR: ${message}`);
  process.exit(1);
}

const candidates = process.platform === 'win32'
  ? [
      path.join(root, '.venv', 'Scripts', 'python.exe'),
      'py',
      'python'
    ]
  : [
      path.join(root, '.venv', 'bin', 'python'),
      'python3',
      'python'
    ];

let python;
let pythonArgs = [];
for (const candidate of candidates) {
  if (path.isAbsolute(candidate) && !fs.existsSync(candidate)) continue;
  const probe = spawnSync(candidate, [...(candidate === 'py' ? ['-3'] : []), '--version'], {
    cwd: root,
    encoding: 'utf8',
    windowsHide: true
  });
  if (!probe.error && probe.status === 0) {
    python = candidate;
    if (candidate === 'py') pythonArgs = ['-3'];
    break;
  }
}
if (!python) fail('No se encontró Python. Instala Python o crea el entorno .venv.');

fs.mkdirSync(distDir, { recursive: true });
try { fs.rmSync(manifestPath, { force: true }); } catch (_error) {}
try { fs.rmSync(serverDir, { recursive: true, force: true }); } catch (_error) {}

console.log(`[CodeGuard build] Python: ${python} ${pythonArgs.join(' ')}`);
console.log('[CodeGuard build] Generando CodeGuardServer en dist-server...');
const result = spawnSync(python, [
  ...pythonArgs,
  '-m', 'PyInstaller',
  '--clean',
  '--noconfirm',
  '--distpath', 'dist-server',
  '--workpath', path.join('build', 'pyinstaller-server'),
  'CodeGuardServer.spec'
], {
  cwd: root,
  stdio: 'inherit',
  windowsHide: true
});

if (result.error) fail(`No se pudo ejecutar PyInstaller: ${result.error.message}`);
if (result.status !== 0) fail(`PyInstaller terminó con código ${result.status}.`);
if (!fs.existsSync(executablePath)) fail(`PyInstaller terminó sin generar ${path.relative(root, executablePath)}.`);

if (process.platform !== 'win32') {
  fs.chmodSync(executablePath, fs.statSync(executablePath).mode | 0o111);
}

const sha256 = crypto.createHash('sha256').update(fs.readFileSync(executablePath)).digest('hex');
const manifest = {
  platform: process.platform,
  architecture: process.arch,
  executable: executableName,
  sha256,
  builtAt: new Date().toISOString()
};
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n', { mode: 0o600 });

console.log(`[CodeGuard build] Servidor generado: ${path.relative(root, executablePath)}`);
console.log(`[CodeGuard build] SHA-256: ${sha256}`);
