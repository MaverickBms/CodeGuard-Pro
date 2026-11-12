const { contextBridge, ipcRenderer } = require('electron');

// Exponer API segura al renderer
contextBridge.exposeInMainWorld('codeguardAPI', {
  // Temas
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
