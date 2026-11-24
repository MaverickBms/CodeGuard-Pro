const { contextBridge, ipcRenderer } = require('electron');

// Exponer API segura al renderer
contextBridge.exposeInMainWorld('codeguardAPI', {
  // Temas (persistidos en el perfil por el proceso principal)
  getTheme: () => ipcRenderer.invoke('get-theme'),
  setTheme: (theme) => ipcRenderer.send('set-theme', theme),
  
  // Notificaciones
  showNotification: (options) => ipcRenderer.send('show-notification', options),
  
  // Sincronización de conocimiento (sin exponer argumentos ni procesos).
  getKnowledgeSyncStatus: () => ipcRenderer.invoke('get-knowledge-sync-status'),
  checkKnowledgeUpdates: () => ipcRenderer.invoke('check-knowledge-updates'),
  onKnowledgeSyncStatus: (callback) => {
    const handler = (_event, status) => callback(status);
    ipcRenderer.on('knowledge-sync-status', handler);
    return () => ipcRenderer.removeListener('knowledge-sync-status', handler);
  },

  // Recursos externos verificados (HTTPS) del contenido académico.
  openExternal: (url) => ipcRenderer.invoke('open-external', url),

  // Progreso de arranque (solo lectura, eventos emitidos por el proceso principal).
  onStartupProgress: (callback) => {
    const handler = (_event, payload) => callback(payload);
    ipcRenderer.on('startup-progress', handler);
    return () => ipcRenderer.removeListener('startup-progress', handler);
  },

  // Señal explícita: la interfaz principal terminó su inicialización crítica.
  signalAppInteractive: (payload) => ipcRenderer.send('app-interactive-signal', payload || { source: 'renderer' }),

  // Información del sistema
  getSystemInfo: () => ipcRenderer.invoke('get-system-info'),
  
  // Seleccionar carpeta
  selectFolder: () => ipcRenderer.invoke('select-folder'),
  
  // Escuchar eventos de tema
  onThemeChange: (callback) => {
    const handler = (_event, theme) => callback(theme);
    ipcRenderer.on('theme-changed', handler);
    return () => ipcRenderer.removeListener('theme-changed', handler);
  }
});

// Fallback de seguridad: si la interfaz no emite señal explícita, evitar bloqueo indefinido.
// La señal principal debe enviarla el frontend cuando los componentes críticos estén inicializados.
window.addEventListener('load', () => {
  try {
    const href = window.location.href || '';
    if (href.includes('splash.html') || href.startsWith('data:')) return;
    setTimeout(() => {
      try { ipcRenderer.send('app-interactive-signal', { source: 'preload-fallback', ts: Date.now() }); } catch (_e) {}
    }, 20000);
  } catch (_e) {}
});

// Exponer utilidades de SweetAlert2 si está disponible
contextBridge.exposeInMainWorld('swalUtils', {
  alert: (options) => {
    if (window.Swal) {
      return window.Swal.fire(options);
    }
    return Promise.resolve({});
  },
  confirm: (options) => {
    if (window.Swal) {
      return window.Swal.fire({
        ...options,
        showCancelButton: true,
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
      });
    }
    return Promise.resolve({});
  },
  toast: (options) => {
    if (window.Swal) {
      const Toast = window.Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true
      });
      return Toast.fire(options);
    }
    return Promise.resolve({});
  }
});
