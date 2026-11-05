const { app, BrowserWindow, ipcMain, dialog, notification } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');

let mainWindow = null;
let djangoProcess = null;
let isDev = process.env.NODE_ENV === 'development';

const DJANGO_PORT = 8000;
const DJANGO_HOST = '127.0.0.1';
const DJANGO_URL = `http://${DJANGO_HOST}:${DJANGO_PORT}`;

// Función para iniciar Django como proceso hijo
function startDjango() {
  const pythonPath = process.platform === 'win32'
    ? path.join(__dirname, '..', '.venv', 'Scripts', 'python.exe')
    : path.join(__dirname, '..', '.venv', 'bin', 'python');

  // Si no existe el venv, usar python del sistema
  if (!fs.existsSync(pythonPath)) {
    pythonPath = 'python3';
  }

  const managePy = path.join(__dirname, '..', 'manage.py');

  djangoProcess = spawn(pythonPath, [
    managePy,
    'runserver',
    `${DJANGO_HOST}:${DJANGO_PORT}`
  ], {
    cwd: path.join(__dirname, '..'),
    env: {
      ...process.env,
      DJANGO_SETTINGS_MODULE: 'config.settings.development',
      PYTHONUNBUFFERED: '1'
    },
    stdio: ['ignore', 'pipe', 'pipe']
  });

  djangoProcess.stdout.on('data', (data) => {
    console.log(`[Django] ${data.toString().trim()}`);
  });

  djangoProcess.stderr.on('data', (data) => {
    console.error(`[Django ERR] ${data.toString().trim()}`);
  });

  djangoProcess.on('close', (code) => {
    console.log(`[Django] Proceso terminado con código ${code}`);
  });
}

// Detener Django al salir
function stopDjango() {
  if (djangoProcess) {
    try {
      if (process.platform === 'win32') {
        spawn('taskkill', ['/PID', djangoProcess.pid, '/F', '/T']);
      } else {
        process.kill(-djangoProcess.pid);
      }
    } catch (e) {
      console.error('Error deteniendo Django:', e);
    }
    djangoProcess = null;
  }
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1024,
    minHeight: 768,
    title: 'CodeGuard Pro',
    icon: path.join(__dirname, '..', 'static', 'icons', 'icon.png'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      webSecurity: true,
      allowRunningInsecureContent: false
    },
    show: false,
    titleBarStyle: 'hiddenInset',
    backgroundColor: '#0f172a'
  });

  // Cargar la aplicación Django localmente
  mainWindow.loadURL(DJANGO_URL);

  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  // Menú de aplicación personalizado
  const { Menu } = require('electron');
  const template = [
    {
      label: 'CodeGuard Pro',
      submenu: [
        { label: 'Acerca de', click: () => showAbout() },
        { type: 'separator' },
        { label: 'Preferencias', accelerator: 'CmdOrCtrl+,', click: () => openPreferences() },
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
        { label: 'Pegar', accelerator: 'CmdOrCtrl+V', role: 'paste' }
      ]
    },
    {
      label: 'Ver',
      submenu: [
        { label: 'Recargar', accelerator: 'CmdOrCtrl+R', click: () => mainWindow.reload() },
        { label: 'Herramientas de desarrollador', accelerator: 'F12', click: () => mainWindow.webContents.toggleDevTools() },
        { type: 'separator' },
        { label: 'Tema claro', click: () => setTheme('light') },
        { label: 'Tema oscuro', click: () => setTheme('dark') },
        { label: 'Alto contraste', click: () => setTheme('high-contrast') }
      ]
    },
    {
      label: 'Ayuda',
      submenu: [
        { label: 'Documentación', click: () => openDocs() },
        { label: 'Verificar actualizaciones', click: () => checkUpdates() }
      ]
    }
  ];

  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
}

function setTheme(theme) {
  if (mainWindow) {
    mainWindow.webContents.send('set-theme', theme);
  }
}

function showAbout() {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Acerca de CodeGuard Pro',
    message: 'CodeGuard Pro',
    detail: 'Plataforma educativa personal, offline-first.\nArquitectura: Electron + Django API local.\nVersión: 1.0.0\n\n© 2026 CodeGuard Pro'
  });
}

function openPreferences() {
  if (mainWindow) {
    mainWindow.webContents.send('open-preferences');
  }
}

function openDocs() {
  const { shell } = require('electron');
  shell.openExternal('https://github.com/MaverickBms/CodeGuard-Pro.git');
}

function checkUpdates() {
  dialog.showMessageBox(mainWindow, {
    type: 'info',
    title: 'Actualizaciones',
    message: 'Verificando actualizaciones...',
    detail: 'No se encontraron actualizaciones disponibles.'
  });
}

// IPC: manejar notificaciones del sistema
ipcMain.on('show-notification', (event, { title, body, icon }) => {
  const notif = new notification.Notification({
    title: title || 'CodeGuard Pro',
    body: body || '',
    icon: icon || path.join(__dirname, '..', 'static', 'icons', 'icon.png')
  });
  notif.show();
});

// IPC: obtener información del sistema
ipcMain.handle('get-system-info', async () => {
  return {
    platform: os.platform(),
    arch: os.arch(),
    totalmem: os.totalmem(),
    freemem: os.freemem(),
    hostname: os.hostname()
  };
});

// IPC: seleccionar carpeta para backup/restauración
ipcMain.handle('select-folder', async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    properties: ['openDirectory', 'createDirectory']
  });
  return result;
});

// Manejar cierre de la aplicación
app.whenReady().then(() => {
  startDjango();
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  stopDjango();
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', () => {
  stopDjango();
});

// Manejo de errores no capturados
process.on('uncaughtException', (error) => {
  console.error('Error no capturado:', error);
  dialog.showErrorBox('Error', error.message || 'Ocurrió un error inesperado');
});
