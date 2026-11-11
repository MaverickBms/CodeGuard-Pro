/* CodeGuard Pro — panel de ajustes accesible y sincronizado con el gestor de temas. */
(function () {
  'use strict';

  var trigger = document.getElementById('btnAjustes');
  var closeButton = document.getElementById('btnCerrarAjustes');
  var doneButton = document.getElementById('btnGuardarAjustes');
  var panel = document.getElementById('ajustesPanel');
  var overlay = document.getElementById('ajustesOverlay');
  var themeButtons = Array.prototype.slice.call(document.querySelectorAll('.ajustes-tema-btn[data-theme]'));
  if (!trigger || !closeButton || !doneButton || !panel || !overlay) return;

  var previousFocus = null;
  panel.inert = true;
  var themes = ['light', 'dark', 'high-contrast', 'retro-pixel', 'cyberpunk', 'fantasy', 'sci-fi', 'warrior', 'mage', 'rogue', 'paladin', 'dark-mage'];

  function currentTheme() {
    try {
      var saved = localStorage.getItem('cg-theme');
      return themes.indexOf(saved) >= 0 ? saved : 'light';
    } catch (error) {
      return document.documentElement.getAttribute('data-theme') || 'light';
    }
  }

  function syncThemeButtons(theme) {
    themeButtons.forEach(function (button) {
      var selected = button.getAttribute('data-theme') === theme;
      button.classList.toggle('activo', selected);
      button.setAttribute('aria-pressed', selected ? 'true' : 'false');
    });
  }

  function applySelectedTheme(theme) {
    if (themes.indexOf(theme) < 0) return;
    if (window.codeguardUI && typeof window.codeguardUI.setTheme === 'function') {
      window.codeguardUI.setTheme(theme);
    } else {
      document.documentElement.setAttribute('data-theme', theme);
      document.body.setAttribute('data-theme', theme);
      try { localStorage.setItem('cg-theme', theme); } catch (error) { /* almacenamiento opcional */ }
    }
    syncThemeButtons(theme);
  }

  function openPanel() {
    if (panel.classList.contains('activo')) return;
    previousFocus = document.activeElement;
    panel.inert = false;
    panel.classList.add('activo');
    panel.setAttribute('aria-hidden', 'false');
    trigger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('ajustes-abierto');
    closeButton.focus();
  }

  function closePanel() {
    if (!panel.classList.contains('activo')) return;
    panel.classList.remove('activo');
    panel.setAttribute('aria-hidden', 'true');
    panel.inert = true;
    trigger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('ajustes-abierto');
    if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
    else trigger.focus();
  }

  function trapFocus(event) {
    if (event.key !== 'Tab' || !panel.classList.contains('activo')) return;
    var focusable = panel.querySelectorAll('button:not([disabled]), a[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])');
    if (!focusable.length) {
      event.preventDefault();
      panel.focus();
      return;
    }
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  trigger.addEventListener('click', openPanel);
  closeButton.addEventListener('click', closePanel);
  doneButton.addEventListener('click', closePanel);
  overlay.addEventListener('click', closePanel);
  themeButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      applySelectedTheme(button.getAttribute('data-theme'));
    });
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && panel.classList.contains('activo')) closePanel();
    trapFocus(event);
  });

  syncThemeButtons(currentTheme());
  document.addEventListener('cg:theme-change', function (event) {
    if (event.detail && event.detail.theme) syncThemeButtons(event.detail.theme);
  });
})();
