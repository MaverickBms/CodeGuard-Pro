// Gestión de temas y utilidades de CodeGuard Pro.
// Se sirve como recurso local para permitir una CSP sin 'unsafe-inline' en scripts.

const themes = [
  'light', 'dark', 'high-contrast',
  'retro-pixel', 'cyberpunk', 'fantasy',
  'sci-fi', 'warrior', 'mage', 'rogue',
  'paladin', 'dark-mage'
];

const themeNames = {
  'light': 'Claro Diurno',
  'dark': 'Oscuro Nocturno',
  'high-contrast': 'Alto Contraste',
  'retro-pixel': 'Retro Pixel',
  'cyberpunk': 'Cyberpunk',
  'fantasy': 'Reino Fantasía',
  'sci-fi': 'Ciencia Ficción',
  'warrior': 'Guerrero',
  'mage': 'Mago',
  'rogue': 'Pícaro',
  'paladin': 'Paladín',
  'dark-mage': 'Oscuro Mago'
};

function getCurrentTheme() {
  return localStorage.getItem('cg-theme') || 'light';
}

function applyTheme(theme) {
  if (!themes.includes(theme)) theme = 'light';
  document.documentElement.setAttribute('data-theme', theme);
  document.body.setAttribute('data-theme', theme);
  localStorage.setItem('cg-theme', theme);
  document.body.classList.remove(...themes.map((t) => `theme-${t}`));
  document.body.classList.add(`theme-${theme}`);

  const themeBtn = document.getElementById('themeSelector');
  if (themeBtn) {
    themeBtn.title = `Tema actual: ${themeNames[theme]}`;
    themeBtn.setAttribute('aria-label', `Cambiar tema (actual: ${themeNames[theme]})`);
  }

  document.querySelectorAll('.theme-option').forEach((option) => {
    const isActive = option.getAttribute('data-theme') === theme;
    option.classList.toggle('active-theme', isActive);
  });
}

function setTheme(theme) {
  applyTheme(theme);
  if (window.codeguardAPI && typeof window.codeguardAPI.setTheme === 'function') {
    window.codeguardAPI.setTheme(theme);
  }
}

function cycleTheme() {
  const current = getCurrentTheme();
  const idx = themes.indexOf(current);
  const next = themes[(idx + 1) % themes.length];
  setTheme(next);
  showToast(`Tema: ${themeNames[next]}`, 'info');
}

document.addEventListener('DOMContentLoaded', () => {
  applyTheme(getCurrentTheme());

  if (window.codeguardAPI && typeof window.codeguardAPI.onThemeChange === 'function') {
    window.codeguardAPI.onThemeChange(applyTheme);
  }

  document.querySelectorAll('.theme-option').forEach((option) => {
    option.addEventListener('click', () => {
      const theme = option.getAttribute('data-theme');
      setTheme(theme);
      showToast(`Tema: ${themeNames[theme]}`, 'info');
      const dropdown = bootstrap.Dropdown.getInstance(document.getElementById('themeDropdownButton'));
      if (dropdown) dropdown.hide();
    });
  });

  const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebar');
  const mainContent = document.getElementById('mainContent');
  if (toggleBtn && sidebar && mainContent) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('collapsed');
      mainContent.classList.toggle('collapsed');
      const icon = toggleBtn.querySelector('i');
      if (sidebar.classList.contains('collapsed')) {
        icon.classList.remove('fa-chevron-left');
        icon.classList.add('fa-chevron-right');
      } else {
        icon.classList.remove('fa-chevron-right');
        icon.classList.add('fa-chevron-left');
      }
    });

    document.querySelectorAll('.nav-item[data-url]').forEach((item) => {
      item.addEventListener('click', (e) => {
        if (item.classList.contains('disabled')) return;
        const url = item.getAttribute('data-url');
        if (url && url !== '#') {
          window.location.href = url;
        }
      });
    });
  }
});

function showAlert(title, text, type = 'info') {
  if (typeof Swal !== 'undefined') {
    Swal.fire({
      icon: type,
      title: title,
      text: text,
      confirmButtonColor: '#1e3a8a',
      customClass: {
        popup: 'glass-card'
      }
    });
  } else {
    alert(title + ': ' + text);
  }
}

function showConfirm(title, text, onConfirm) {
  if (typeof Swal !== 'undefined') {
    Swal.fire({
      icon: 'question',
      title: title,
      text: text,
      showCancelButton: true,
      confirmButtonText: 'Confirmar',
      cancelButtonText: 'Cancelar',
      confirmButtonColor: '#1e3a8a',
      customClass: {
        popup: 'glass-card'
      }
    }).then((result) => {
      if (result.isConfirmed && onConfirm) onConfirm();
    });
  } else {
    if (confirm(title + ': ' + text) && onConfirm) onConfirm();
  }
}

function showToast(message, type = 'info') {
  if (typeof Swal !== 'undefined') {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000,
      timerProgressBar: true,
      customClass: {
        popup: 'glass-card'
      }
    });
    Toast.fire({ icon: type, title: message });
  }
}

window.codeguardUI = { showAlert, showConfirm, showToast, setTheme, cycleTheme };
