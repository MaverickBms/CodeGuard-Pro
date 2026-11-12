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

let mainWindow = null;
let djangoProcess = null;
let djangoPort = null;
let syncProcess = null;
let syncTimer = null;
let syncStatus = { state: 'idle', message: 'Sin comprobaciones recientes.', checkedAt: null };
let quitting = false;

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

function waitForServer(url, timeoutMs = 45000) {
  const started = Date.now();
  return new Promise((resolve, reject) => {
    const retry = () => {
      if (Date.now() - started > timeoutMs) {
        reject(new Error(`El servidor local no respondió en ${Math.round(timeoutMs / 1000)} s.`));
        return;
      }
      setTimeout(attempt, 400);
    };

    const attempt = () => {
      const request = http.get(url, { timeout: 2500 }, (response) => {
        response.resume();
        if (response.statusCode && response.statusCode < 500) {
          resolve();
        } else {
          retry();
        }
      });
      request.on('error', retry);
      request.on('timeout', () => {
        request.destroy();
        retry();
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

  await waitForServer(`http://${DJANGO_HOST}:${djangoPort}/`);
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
  const required = [
    process.env.CODEGUARD_SYNC_MANIFEST_URL,
    process.env.CODEGUARD_SYNC_SIGNATURE_URL,
    process.env.CODEGUARD_SYNC_ALLOWED_HOSTS,
    process.env.CODEGUARD_SYNC_TRUSTED_PUBLIC_KEYS
  ];
  if (!['stable', 'beta'].includes(channel) || required.some(value => !value || !value.trim())) {
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
  if (force && app.isPackaged) env.CODEGUARD_SYNC_FORCE = '1';

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
  const initial = setTimeout(() => startKnowledgeSync(false), SYNC_INITIAL_DELAY_MS);
  initial.unref();
  syncTimer = setInterval(() => startKnowledgeSync(false), SYNC_POLL_INTERVAL_MS);
  syncTimer.unref();
}

function stopKnowledgeSync() {
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
      'La documentación se distribuye junto con la aplicación:\n\n' +
      '• README.md — instalación, ejecución y empaquetado.\n' +
      '• IEEE830.md — especificación de requisitos.\n' +
      '• docs/ — modelo de datos, plan de desarrollo y decisiones.\n\n' +
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

// IPC: el renderer solicita cambiar el tema; el proceso principal lo difunde.
ipcMain.on('set-theme', (_event, theme) => {
  if (THEMES.some(([id]) => id === theme)) {
    sendTheme(theme);
  }
});

// IPC: notificaciones nativas del sistema.
ipcMain.on('show-notification', (_event, options = {}) => {
  if (!Notification.isSupported()) return;
  const notification = new Notification({
    title: options.title || 'CodeGuard Pro',
    body: options.body || '',
    icon: options.icon || iconPath()
  });
  notification.show();
});

// IPC: estado de sincronización; solo se acepta desde la ventana local de CodeGuard.
ipcMain.handle('get-knowledge-sync-status', event => {
  const trustedUrl = `http://${DJANGO_HOST}:${djangoPort}/`;
  if (!djangoPort || !event.senderFrame?.url?.startsWith(trustedUrl)) {
    throw new Error('Origen IPC no autorizado.');
  }
  return syncStatus;
});

ipcMain.handle('check-knowledge-updates', event => {
  const trustedUrl = `http://${DJANGO_HOST}:${djangoPort}/`;
  if (!djangoPort || !event.senderFrame?.url?.startsWith(trustedUrl)) {
    throw new Error('Origen IPC no autorizado.');
  }
  startKnowledgeSync(true);
  return syncStatus;
});

// IPC: información del sistema (sin datos sensibles).
ipcMain.handle('get-system-info', async () => ({
  platform: os.platform(),
  arch: os.arch(),
  totalmem: os.totalmem(),
  freemem: os.freemem(),
  hostname: os.hostname()
}));

// IPC: seleccionar carpeta para backup/restauración.
ipcMain.handle('select-folder', async () => {
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
