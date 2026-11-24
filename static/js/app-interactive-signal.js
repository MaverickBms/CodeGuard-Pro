(function () {
  'use strict';
  function criticalReady() {
    try {
      var hasShell = !!(document.getElementById('sidebar') && document.getElementById('mainContent'));
      var hasNav = !!document.querySelector('.sidebar-nav, .cg-sidebar-nav');
      var hasHeader = !!document.querySelector('.main-header, .cg-page-title');
      var hasContent = !!document.querySelector('main.page-container, main[role="main"]');
      var themeOk = !!document.documentElement.getAttribute('data-theme');
      return document.readyState === 'complete' && hasShell && hasNav && hasHeader && hasContent && themeOk;
    } catch (_e) { return false; }
  }
  function sendOnce() {
    if (window.__cgInteractiveSignaled) return;
    if (!criticalReady()) return;
    window.__cgInteractiveSignaled = true;
    try {
      if (window.codeguardAPI && typeof window.codeguardAPI.signalAppInteractive === 'function') {
        window.codeguardAPI.signalAppInteractive({ source: 'frontend-explicit', readyState: document.readyState, ts: Date.now() });
      }
    } catch (_e) {}
  }
  function trySignal(attempt) {
    if (window.__cgInteractiveSignaled) return;
    if (criticalReady()) { requestAnimationFrame(sendOnce); return; }
    if (attempt < 120) setTimeout(function () { trySignal(attempt + 1); }, 250);
  }
  if (document.readyState === 'complete') trySignal(0);
  else window.addEventListener('load', function () { trySignal(0); }, { once: true });
})();
