const {
  app,
  BrowserWindow,
  ipcMain,
  dialog,
  shell,
  Notification,
  Menu
} = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');
const http = require('http');
const net = require('net');
const { isTrustedIpcSender } = require('./ipc-security');
const { getChildStartupFailure } = require('./process-health');
const { resolveBackupPath } = require('./restore-backup');

let mainWindow = null;
let djangoProcess = null;
let djangoPort = null;
let syncProcess = null;
let syncTimer = null;
let syncInitialTimer = null;
let syncStatus = { state: 'idle', message: 'Sin comprobaciones recientes.', checkedAt: null };
let quitting = false;
let restoring = false;

const DJANGO_HOST = '127.0.0.1';
const SYNC_POLL_INTERVAL_MS = 5 * 60 * 1000;
const SYNC_INITIAL_DELAY_MS = 30 * 1000;
const THEMES = [
  ['light', 'Claro Diurno'],
  ['dark', 'Oscuro Nocturno'],
  ['high-contrast', 'Alto Contraste'],
  ['retro-pixel', 'Retro Pixel'],
  ['cyberpunk', 'Cyberpunk'],
  ['fantasy', 'Reino Fantasía'],
  ['sci-fi', 'Ciencia Ficción'],
  ['warrior', 'Guerrero'],
  ['mage', 'Mago'],
  ['rogue', 'Pícaro'],
  ['paladin', 'Paladín'],
  ['dark-mage', 'Oscuro Mago']
];

function projectRoot() {
  return path.join(__dirname, '..');
}

function dataDir() {
  const dir = process.env.CODEGUARD_DATA_DIR
    || (app.isPackaged
      ? app.getPath('userData')
      : path.join(projectRoot(), 'data'));
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

function iconPath() {
  const candidate = path.join(projectRoot(), 'static', 'icons', 'icon.png');
  return fs.existsSync(candidate) ? candidate : undefined;
}

function getFreePort() {
  return new Promise((resolve, reject) => {
    const server = net.createServer();
    server.unref();
    server.on('error', reject);
    server.listen(0, DJANGO_HOST, () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });
}

function waitForServer(url, child, timeoutMs = 120000) {
  const started = Date.now();
  return new Promise((resolve, reject) => {
    const retry = () => {
      const startupFailure = getChildStartupFailure(child);
      if (startupFailure) {
        reject(startupFailure);
        return;
      }
      if (Date.now() - started > timeoutMs) {
        reject(new Error(
          `El servidor local no superó la comprobación de salud en ${Math.round(timeoutMs / 1000)} s. ` +
          'Revisa la inicialización de la base de datos y el roadmap.'
        ));
        return;
      }
      setTimeout(attempt, 250);
    };

    const attempt = () => {
      let retryScheduled = false;
      const scheduleRetry = () => {
        if (retryScheduled) return;
        retryScheduled = true;
        retry();
      };

      const request = http.get(url, { timeout: 3000 }, (response) => {
        let body = '';
        response.setEncoding('utf8');
        response.on('data', chunk => {
          if (body.length < 4096) body += chunk;
        });
        response.on('end', () => {
          if (response.statusCode !== 200) {
            scheduleRetry();
            return;
          }
          try {
            const health = JSON.parse(body);
            const ready = health.status === 'ok' &&
              health.database === 'ok' &&
              health.migrations === 'ok' &&
              health.roadmap === 'ok';
            if (ready) resolve();
            else scheduleRetry();
          } catch (_error) {
            scheduleRetry();
          }
        });
      });
      request.on('error', scheduleRetry);
      request.on('timeout', () => {
        request.destroy();
        scheduleRetry();
      });
    };

    attempt();
  });
}

function attachProcessLogs(child) {
  child.stdout.on('data', (data) => {
    console.log(`[Django] ${data.toString().trim()}`);
  });
  child.stderr.on('data', (data) => {
    console.error(`[Django ERR] ${data.toString().trim()}`);
  });
  child.on('error', (error) => {
    child.spawnError = error;
    console.error('[Django] No se pudo iniciar el proceso:', error);
  });
  child.on('close', (code) => {
    console.log(`[Django] Proceso terminado con código ${code}`);
    djangoProcess = null;
  });
}

async function startDjango() {
  djangoPort = await getFreePort();
  const env = {
    ...process.env,
    DJANGO_SETTINGS_MODULE: app.isPackaged
      ? 'config.settings.desktop'
      : 'config.settings.development',
    CODEGUARD_DATA_DIR: dataDir(),
    CODEGUARD_PORT: String(djangoPort),
    PYTHONUNBUFFERED: '1'
  };

  if (app.isPackaged) {
    const serverDir = path.join(process.resourcesPath, 'server');
    const executable = process.platform === 'win32'
      ? 'CodeGuardServer.exe'
      : 'CodeGuardServer';
    const serverPath = path.join(serverDir, executable);

    if (!fs.existsSync(serverPath)) {
      throw new Error(
        `No se encontró el servidor local empaquetado en:\n${serverPath}\n\n` +
        'Vuelve a generar el paquete con build_windows.bat.'
      );
    }

    djangoProcess = spawn(serverPath, [], {
      cwd: serverDir,
      env,
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true
    });
  } else {
    let pythonPath = process.env.CODEGUARD_PYTHON;
    if (!pythonPath) {
      pythonPath = process.platform === 'win32'
        ? path.join(projectRoot(), '.venv', 'Scripts', 'python.exe')
        : path.join(projectRoot(), '.venv', 'bin', 'python');
    }
    if (!fs.existsSync(pythonPath)) {
      pythonPath = process.platform === 'win32' ? 'python' : 'python3';
    }

    djangoProcess = spawn(
      pythonPath,
      [
        path.join(projectRoot(), 'manage.py'),
        'runserver',
        `${DJANGO_HOST}:${djangoPort}`,
        '--noreload'
      ],
      {
        cwd: projectRoot(),
        env,
        stdio: ['ignore', 'pipe', 'pipe'],
        detached: process.platform !== 'win32'
      }
    );
  }

  attachProcessLogs(djangoProcess);

  await waitForServer(`http://${DJANGO_HOST}:${djangoPort}/healthz/`, djangoProcess);
  return `http://${DJANGO_HOST}:${djangoPort}`;
}

function emitKnowledgeSyncStatus(state, message, checkedAt = syncStatus.checkedAt) {
  syncStatus = { state, message, checkedAt };
  if (mainWindow && !mainWindow.isDestroyed()) {
    mainWindow.webContents.send('knowledge-sync-status', syncStatus);
  }
}

function syncConfiguration() {
  const channel = (process.env.CODEGUARD_SYNC_CHANNEL || 'stable').trim();
  const manifestUrl = (process.env.CODEGUARD_SYNC_MANIFEST_URL || '').trim();
  const signatureUrl = (process.env.CODEGUARD_SYNC_SIGNATURE_URL || '').trim();
  const hosts = (process.env.CODEGUARD_SYNC_ALLOWED_HOSTS || '')
    .split(',')
    .map(host => host.trim())
    .filter(Boolean);
  let trustedKeys;
  try {
    trustedKeys = JSON.parse(process.env.CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS || '');
  } catch (_error) {
    return null;
  }
  const normalizeHost = host => host.toLowerCase().endsWith('.') ? host.slice(0, -1).toLowerCase() : host.toLowerCase();
  const allowedHosts = new Set(hosts.map(normalizeHost));
  const validEndpoint = value => {
    try {
      const parsed = new URL(value);
      return parsed.protocol === 'https:' &&
        allowedHosts.has(normalizeHost(parsed.hostname)) &&
        !parsed.username &&
        !parsed.password &&
        (!parsed.port || parsed.port === '443') &&
        !parsed.hash;
    } catch (_error) {
      return false;
    }
  };
  if (
    !['stable', 'beta'].includes(channel) ||
    !validEndpoint(manifestUrl) ||
    !validEndpoint(signatureUrl) ||
    hosts.length === 0 ||
    !trustedKeys ||
    Array.isArray(trustedKeys) ||
    typeof trustedKeys !== 'object' ||
    Object.keys(trustedKeys).length === 0
  ) {
    return null;
  }
  return { channel };
}

function syncEnvironment() {
  return {
    ...process.env,
    DJANGO_SETTINGS_MODULE: app.isPackaged
      ? 'config.settings.desktop'
      : 'config.settings.development',
    CODEGUARD_DATA_DIR: dataDir(),
    CODEGUARD_APP_VERSION: app.getVersion(),
    PYTHONUNBUFFERED: '1'
  };
}

function startKnowledgeSync(force = false) {
  if (quitting) return false;
  if (syncProcess) {
    emitKnowledgeSyncStatus('running', 'Ya hay una sincronización en curso.');
    return false;
  }

  const config = syncConfiguration();
  if (!config) {
    emitKnowledgeSyncStatus(
      'not-configured',
      'Actualizaciones automáticas desactivadas: falta la configuración de distribución de confianza.'
    );
    return false;
  }

  const env = syncEnvironment();
  env.CODEGUARD_SYNC_CHANNEL = config.channel;
  let executable;
  let args;
  let cwd;

  if (app.isPackaged) {
    const serverDir = path.join(process.resourcesPath, 'server');
    executable = path.join(
      serverDir,
      process.platform === 'win32' ? 'CodeGuardServer.exe' : 'CodeGuardServer'
    );
    if (!fs.existsSync(executable)) {
      emitKnowledgeSyncStatus('error', 'No se encontró el ejecutable local de sincronización.', new Date().toISOString());
      return false;
    }
    args = ['--sync-knowledge'];
    cwd = serverDir;
  } else {
    executable = process.env.CODEGUARD_PYTHON || (
      process.platform === 'win32'
        ? path.join(projectRoot(), '.venv', 'Scripts', 'python.exe')
        : path.join(projectRoot(), '.venv', 'bin', 'python')
    );
    if (!fs.existsSync(executable)) {
      executable = process.platform === 'win32' ? 'python' : 'python3';
    }
    args = [
      path.join(projectRoot(), 'manage.py'),
      'sincronizar_conocimiento',
      '--channel',
      config.channel
    ];
    cwd = projectRoot();
  }

  if (force && !app.isPackaged) args.push('--force');
  env.CODEGUARD_SYNC_FORCE = force ? '1' : '0';

  const startedAt = new Date().toISOString();
  emitKnowledgeSyncStatus('running', 'Comprobando actualizaciones de conocimiento…', startedAt);

  try {
    syncProcess = spawn(executable, args, {
      cwd,
      env,
      stdio: ['ignore', 'pipe', 'pipe'],
      windowsHide: true
    });
  } catch (error) {
    syncProcess = null;
    console.error('[Knowledge Sync] No se pudo iniciar el proceso:', error);
    emitKnowledgeSyncStatus('error', 'No se pudo iniciar la comprobación de actualizaciones.', startedAt);
    return false;
  }

  let stderr = '';
  syncProcess.stdout.on('data', data => {
    const line = data.toString().trim();
    if (line) console.log('[Knowledge Sync]', line.slice(0, 1000));
  });
  syncProcess.stderr.on('data', data => {
    stderr = (stderr + data.toString()).slice(-3000);
    console.error('[Knowledge Sync ERR]', data.toString().trim().slice(0, 1000));
  });
  syncProcess.on('error', error => {
    console.error('[Knowledge Sync] Error de proceso:', error);
    emitKnowledgeSyncStatus('error', 'No se pudo completar la comprobación de actualizaciones.', startedAt);
  });
  syncProcess.on('close', code => {
    syncProcess = null;
    if (quitting) return;
    if (code === 0) {
      emitKnowledgeSyncStatus('success', 'Comprobación de conocimiento completada.', startedAt);
    } else {
      const safeDetail = stderr.includes('Sincronización no completada')
        ? 'El servicio de conocimiento no pudo completar la actualización.'
        : 'No fue posible comprobar las actualizaciones; se conserva el contenido local.';
      emitKnowledgeSyncStatus('error', safeDetail, startedAt);
    }
  });
  return true;
}

function scheduleKnowledgeSync() {
  if (syncTimer) return;
  // La primera consulta ocurre después de que la interfaz y Django estén disponibles.
  syncInitialTimer = setTimeout(() => {
    syncInitialTimer = null;
    startKnowledgeSync(false);
  }, SYNC_INITIAL_DELAY_MS);
  syncInitialTimer.unref();
  syncTimer = setInterval(() => startKnowledgeSync(false), SYNC_POLL_INTERVAL_MS);
  syncTimer.unref();
}

function stopKnowledgeSync() {
  if (syncInitialTimer) {
    clearTimeout(syncInitialTimer);
    syncInitialTimer = null;
  }
  if (syncTimer) {
    clearInterval(syncTimer);
    syncTimer = null;
  }
  if (syncProcess) {
    const child = syncProcess;
    syncProcess = null;
    try {
      child.kill('SIGTERM');
    } catch (_error) {
      // El proceso puede haber terminado durante el cierre.
    }
  }
}

function stopDjango() {
  if (!djangoProcess) return;
  const child = djangoProcess;
  djangoProcess = null;

  try {
    if (process.platform === 'win32') {
      spawn('taskkill', ['/PID', String(child.pid), '/F', '/T'], {
        windowsHide: true,
        stdio: 'ignore'
      });
    } else {
      // El proceso se lanzó con detached=true: matar todo el grupo.
      try {
        process.kill(-child.pid, 'SIGTERM');
      } catch (_error) {
        child.kill('SIGTERM');
      }
      setTimeout(() => {
        try {
          process.kill(-child.pid, 'SIGKILL');
        } catch (_error) {
          // El proceso ya terminó.
        }
      }, 3000).unref();
    }
  } catch (error) {
    console.error('[Django] Error al detener el servidor:', error);
  }
}

function restoreCommand(backupPath) {
  if (app.isPackaged) {
    const serverDir = path.join(process.resourcesPath, 'server');
    const executable = path.join(
      serverDir,
      process.platform === 'win32' ? 'CodeGuardServer.exe' : 'CodeGuardServer'
    );
    if (!fs.existsSync(executable)) return null;
    return {
      executable,
      args: ['--restore-backup', backupPath],
      cwd: serverDir
    };
  }

  let pythonPath = process.env.CODEGUARD_PYTHON;
  if (!pythonPath) {
    pythonPath = process.platform === 'win32'
      ? path.join(projectRoot(), '.venv', 'Scripts', 'python.exe')
      : path.join(projectRoot(), '.venv', 'bin', 'python');
  }
  if (!fs.existsSync(pythonPath)) {
    pythonPath = process.platform === 'win32' ? 'python' : 'python3';
  }
  return {
    executable: pythonPath,
    args: [
      path.join(projectRoot(), 'manage.py'),
      'restaurar_backup',
      backupPath,
      '--confirm'
    ],
    cwd: projectRoot()
  };
}

function runRestoreProcess(backupPath) {
  return new Promise((resolve) => {
    const command = restoreCommand(backupPath);
    if (!command) {
      resolve({ ok: false, detail: 'No se encontró la herramienta de restauración del paquete.' });
      return;
    }

    let child;
    try {
      child = spawn(command.executable, command.args, {
        cwd: command.cwd,
        env: {
          ...process.env,
          DJANGO_SETTINGS_MODULE: app.isPackaged
            ? 'config.settings.desktop'
            : 'config.settings.development',
          CODEGUARD_DATA_DIR: dataDir(),
          PYTHONUNBUFFERED: '1'
        },
        stdio: ['ignore', 'pipe', 'pipe'],
        windowsHide: true
      });
    } catch (error) {
      resolve({ ok: false, detail: error.message });
      return;
    }

    let stderr = '';
    child.stdout.on('data', data => {
      const line = data.toString().trim();
      if (line) console.log('[Restore]', line.slice(0, 1000));
    });
    child.stderr.on('data', data => {
      stderr = (stderr + data.toString()).slice(-3000);
      console.error('[Restore ERR]', data.toString().trim().slice(0, 1000));
    });
    child.on('error', error => resolve({ ok: false, detail: error.message }));
    child.on('close', code => {
      if (code === 0) {
        resolve({ ok: true, detail: '' });
      } else {
        const detail = stderr
          .split('\n')
          .filter(Boolean)
          .slice(-4)
          .join('\n') || `La restauración terminó con código ${code}.`;
        resolve({ ok: false, detail });
      }
    });
  });
}

async function promptRestoreBackup() {
  if (restoring) return;

  const selection = await dialog.showOpenDialog(mainWindow, {
    title: 'Restaurar copia de seguridad',
    buttonLabel: 'Seleccionar copia',
    properties: ['openFile'],
    filters: [{ name: 'Copias de CodeGuard Pro', extensions: ['zip'] }]
  });
  if (selection.canceled || selection.filePaths.length === 0) return;

  const backupPath = resolveBackupPath(selection.filePaths[0]);
  if (!backupPath) {
    dialog.showErrorBox(
      'Copia no válida',
      'Selecciona un archivo .zip regular generado por CodeGuard Pro.'
    );
    return;
  }

  const confirmation = await dialog.showMessageBox(mainWindow, {
    type: 'warning',
    title: 'Restaurar copia de seguridad',
    message: 'Se reemplazarán la base de datos y los archivos multimedia actuales.',
    detail:
      'La aplicación se cerrará, restaurará la copia y volverá a iniciarse. ' +
      'Se conservará una copia de reversión del perfil anterior.',
    buttons: ['Cancelar', 'Restaurar y reiniciar'],
    defaultId: 0,
    cancelId: 0,
    noLink: true
  });
  if (confirmation.response !== 1) return;

  restoring = true;
  quitting = true;
  stopKnowledgeSync();
  stopDjango();
  // Dar tiempo a que Waitress libere la base antes de sustituirla.
  await new Promise(resolve => setTimeout(resolve, 800));

  const result = await runRestoreProcess(backupPath);
  if (result.ok) {
    await dialog.showMessageBox(mainWindow, {
      type: 'info',
      title: 'Restauración completada',
      message: 'La copia se restauró y verificó correctamente.',
      detail: 'CodeGuard Pro se reiniciará con el perfil restaurado.'
    });
  } else {
    dialog.showErrorBox(
      'No se pudo restaurar la copia',
      `${result.detail}\n\nEl perfil anterior se conserva o se revierte automáticamente. ` +
      'CodeGuard Pro se reiniciará para comprobarlo.'
    );
  }

  app.relaunch();
  app.exit(0);
}

function splashHtml() {
  return `data:text/html;charset=utf-8,${encodeURIComponent(`
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>CodeGuard Pro</title>
        <style>
          :root { color-scheme: dark; }
          * { box-sizing: border-box; }
          body {
            margin: 0; min-height: 100vh; display: grid; place-items: center;
            font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
            background: radial-gradient(circle at 30% 20%, #1e3a8a, #0f172a 65%);
            color: #f8fafc;
          }
          .card { text-align: center; padding: 40px; }
          .shield {
            width: 84px; height: 84px; margin: 0 auto 22px;
            border-radius: 22px; display: grid; place-items: center;
            background: linear-gradient(135deg, #3b82f6, #1e3a8a);
            box-shadow: 0 18px 50px rgba(0,0,0,.45);
            font-size: 42px;
          }
          h1 { margin: 0 0 10px; font-size: 1.6rem; letter-spacing: -.02em; }
          p { margin: 0; color: #cbd5e1; font-size: .95rem; }
          .spinner {
            width: 28px; height: 28px; margin: 26px auto 0;
            border: 3px solid rgba(255,255,255,.18);
            border-top-color: #60a5fa; border-radius: 50%;
            animation: spin .9s linear infinite;
          }
          @keyframes spin { to { transform: rotate(360deg); } }
        </style>
      </head>
      <body>
        <div class="card">
          <div class="shield">🛡️</div>
          <h1>CodeGuard Pro</h1>
          <p>Iniciando el servidor local seguro…</p>
          <div class="spinner"></div>
        </div>
      </body>
    </html>
  `)}`;
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1024,
    minHeight: 720,
    title: 'CodeGuard Pro',
    icon: iconPath(),
    backgroundColor: '#0f172a',
    show: false,
    autoHideMenuBar: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      webSecurity: true,
      allowRunningInsecureContent: false
    }
  });

  mainWindow.loadURL(splashHtml());

  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
    // Forzar maximizado después de un breve delay para asegurar que se aplique
    setTimeout(() => {
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.maximize();
      }
    }, 100);
  });

  mainWindow.webContents.setWindowOpenHandler(() => ({ action: 'deny' }));

  mainWindow.webContents.on('will-navigate', (event, url) => {
    const allowed = djangoPort
      ? url.startsWith(`http://${DJANGO_HOST}:${djangoPort}/`)
      : false;
    if (!allowed) {
      event.preventDefault();
    }
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  buildMenu();
}

function buildMenu() {
  const themeItems = THEMES.map(([id, label]) => ({
    label,
    click: () => sendTheme(id)
  }));

  const template = [
    {
      label: 'CodeGuard Pro',
      submenu: [
        { label: 'Acerca de', click: showAbout },
        { type: 'separator' },
        { label: 'Abrir carpeta de datos', click: () => shell.openPath(dataDir()) },
        { label: 'Comprobar actualizaciones de conocimiento', click: () => startKnowledgeSync(true) },
        { type: 'separator' },
        { label: 'Restaurar copia de seguridad…', click: () => promptRestoreBackup() },
        { type: 'separator' },
        { label: 'Salir', accelerator: 'CmdOrCtrl+Q', click: () => app.quit() }
      ]
    },
    {
      label: 'Editar',
      submenu: [
        { label: 'Deshacer', accelerator: 'CmdOrCtrl+Z', role: 'undo' },
        { label: 'Rehacer', accelerator: 'Shift+CmdOrCtrl+Z', role: 'redo' },
        { type: 'separator' },
        { label: 'Cortar', accelerator: 'CmdOrCtrl+X', role: 'cut' },
        { label: 'Copiar', accelerator: 'CmdOrCtrl+C', role: 'copy' },
        { label: 'Pegar', accelerator: 'CmdOrCtrl+V', role: 'paste' },
        { label: 'Seleccionar todo', accelerator: 'CmdOrCtrl+A', role: 'selectAll' }
      ]
    },
    {
      label: 'Ver',
      submenu: [
        { label: 'Recargar', accelerator: 'CmdOrCtrl+R', click: () => mainWindow && mainWindow.reload() },
        { label: 'Herramientas de desarrollador', accelerator: 'F12', click: () => mainWindow && mainWindow.webContents.toggleDevTools() },
        { type: 'separator' },
        { label: 'Tema', submenu: themeItems }
      ]
    },
    {
      label: 'Ayuda',
      submenu: [
        { label: 'Documentación local', click: showDocs },
        { label: 'Información de versión', click: showVersion }
      ]
    }
  ];

  Menu.setApplicationMenu(Menu.buildFromTemplate(template));
}

function sendTheme(theme) {
  if (mainWindow) {
    mainWindow.webContents.send('theme-changed', theme);
  }
}

function showAbout() {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Acerca de CodeGuard Pro',
    message: 'CodeGuard Pro',
    detail:
      'Plataforma educativa personal, offline-first.\n' +
      'Arquitectura: Electron + Django API local.\n' +
      `Versión: ${app.getVersion()}\n\n` +
      'Servidor local en 127.0.0.1 · Sin telemetría\n' +
      '© 2026 CodeGuard Pro'
  });
}

function showDocs() {
  const root = app.isPackaged ? process.resourcesPath : projectRoot();
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Documentación local',
    message: 'Documentación de CodeGuard Pro',
    detail:
      'La documentación incluida con la aplicación es:\n\n' +
      '• README.md — instalación, ejecución, backups y empaquetado.\n' +
      '• README_WINDOWS.md — guía específica de Windows.\n\n' +
      'La documentación técnica extendida (arquitectura, ADRs, seguridad, ' +
      'modelo de datos e informes QA) se mantiene en la rama documentation ' +
      'del repositorio oficial.\n\n' +
      `Carpeta de referencia: ${root}`
  });
}

function showVersion() {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Información de versión',
    message: `CodeGuard Pro ${app.getVersion()}`,
    detail:
      `Electron: ${process.versions.electron}\n` +
      `Chromium: ${process.versions.chrome}\n` +
      `Node.js: ${process.versions.node}\n` +
      `Plataforma: ${process.platform} ${process.arch}\n\n` +
      'Aplicación local, sin telemetría. La consulta de conocimiento es opcional y no transmite datos del estudiante.'
  });
}

// Los canales IPC solo aceptan mensajes del documento local servido por Django.
function isTrustedIpcEvent(event) {
  return isTrustedIpcSender(event, DJANGO_HOST, djangoPort);
}

// IPC: el renderer solicita cambiar el tema; el proceso principal lo difunde.
ipcMain.on('set-theme', (event, theme) => {
  if (!isTrustedIpcEvent(event)) return;
  if (THEMES.some(([id]) => id === theme)) {
    sendTheme(theme);
  }
});

// IPC: notificaciones nativas del sistema. El icono siempre es local y
// los textos tienen límites para evitar abuso del canal privilegiado.
ipcMain.on('show-notification', (event, options = {}) => {
  if (!isTrustedIpcEvent(event) || !Notification.isSupported()) return;
  if (!options || typeof options !== 'object' || Array.isArray(options)) return;

  const title = typeof options.title === 'string'
    ? options.title.slice(0, 120)
    : 'CodeGuard Pro';
  const body = typeof options.body === 'string'
    ? options.body.slice(0, 1000)
    : '';

  const notification = new Notification({
    title: title || 'CodeGuard Pro',
    body,
    icon: iconPath()
  });
  notification.show();
});

// IPC: estado de sincronización; solo se acepta desde la ventana local de CodeGuard.
ipcMain.handle('get-knowledge-sync-status', event => {
  if (!isTrustedIpcEvent(event)) {
    throw new Error('Origen IPC no autorizado.');
  }
  return syncStatus;
});

ipcMain.handle('check-knowledge-updates', event => {
  if (!isTrustedIpcEvent(event)) {
    throw new Error('Origen IPC no autorizado.');
  }
  startKnowledgeSync(true);
  return syncStatus;
});

// IPC: información del sistema (sin datos sensibles).
ipcMain.handle('get-system-info', async event => {
  if (!isTrustedIpcEvent(event)) {
    throw new Error('Origen IPC no autorizado.');
  }
  return {
    platform: os.platform(),
    arch: os.arch(),
    totalmem: os.totalmem(),
    freemem: os.freemem(),
    hostname: os.hostname()
  };
});

// IPC: seleccionar carpeta para backup/restauración.
ipcMain.handle('select-folder', async event => {
  if (!isTrustedIpcEvent(event)) {
    throw new Error('Origen IPC no autorizado.');
  }
  return dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory', 'createDirectory']
  });
});

const gotLock = app.requestSingleInstanceLock();
if (!gotLock) {
  app.quit();
} else {
  app.on('second-instance', () => {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore();
      mainWindow.focus();
    }
  });

  app.whenReady().then(async () => {
    if (process.platform === 'win32') {
      app.setAppUserModelId('com.codeguard.pro');
    }

    createWindow();

    try {
      const url = await startDjango();
      if (mainWindow) {
        await mainWindow.loadURL(url);
      }
      scheduleKnowledgeSync();
    } catch (error) {
      console.error('No se pudo iniciar la aplicación:', error);
      dialog.showErrorBox(
        'No se pudo iniciar CodeGuard Pro',
        `${error.message}\n\nRevisa los registros en:\n${path.join(dataDir(), 'logs')}`
      );
      quitting = true;
      stopDjango();
      app.quit();
    }

    app.on('activate', () => {
      if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
      }
    });
  });
}

app.on('window-all-closed', () => {
  stopKnowledgeSync();
  stopDjango();
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', () => {
  quitting = true;
  stopKnowledgeSync();
  stopDjango();
});

process.on('exit', () => {
  if (!quitting) stopDjango();
});

process.on('uncaughtException', (error) => {
  console.error('Error no capturado:', error);
  dialog.showErrorBox('Error inesperado', error.message || 'Ocurrió un error inesperado.');
});
