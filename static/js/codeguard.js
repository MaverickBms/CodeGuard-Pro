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
  try {
    const saved = localStorage.getItem('cg-theme');
    return themes.includes(saved) ? saved : 'light';
  } catch (error) {
    return 'light';
  }
}

function applyTheme(theme) {
  if (!themes.includes(theme)) theme = 'light';
  document.documentElement.setAttribute('data-theme', theme);
  document.body.setAttribute('data-theme', theme);
  try {
    localStorage.setItem('cg-theme', theme);
  } catch (error) {
    // El tema sigue aplicándose aunque el almacenamiento esté restringido.
  }
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
  document.dispatchEvent(new CustomEvent('cg:theme-change', { detail: { theme } }));
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

// Aplicar el tema guardado inmediatamente al cargar el módulo (con `defer`,
// se ejecuta tras el parseo del HTML y antes del primer paint).
applyTheme(getCurrentTheme());

document.addEventListener('DOMContentLoaded', () => {
  // Aplicar tema guardado antes del primer paint (ya se ejecutó arriba con defer).
  applyTheme(getCurrentTheme());

  if (window.codeguardAPI && typeof window.codeguardAPI.onThemeChange === 'function') {
    window.codeguardAPI.onThemeChange(applyTheme);
  }

  document.querySelectorAll('.theme-option').forEach((option) => {
    option.addEventListener('click', () => {
      const theme = option.getAttribute('data-theme');
      setTheme(theme);
      showToast(`Tema: ${themeNames[theme]}`, 'info');
      if (window.bootstrap && window.bootstrap.Dropdown) {
        const dropdownButton = document.getElementById('themeDropdownButton');
        const dropdown = dropdownButton ? window.bootstrap.Dropdown.getInstance(dropdownButton) : null;
        if (dropdown) dropdown.hide();
      }
    });
  });

  // La navegación y el colapso del sidebar se gestionan en ui-v14.js.

});

function getPrimaryColor() {
  return (
    getComputedStyle(document.documentElement).getPropertyValue('--cg-primary').trim() ||
    '#DC586D'
  );
}

function showAlert(title, text, type = 'info') {
  if (typeof Swal !== 'undefined') {
    Swal.fire({
      icon: type,
      title: title,
      text: text,
      confirmButtonColor: getPrimaryColor(),
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
      confirmButtonColor: getPrimaryColor(),
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
