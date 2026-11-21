/* Abre recursos externos (videos y fuentes) mediante el navegador del sistema.
   En un navegador normal se conserva el enlace; en Electron se usa el IPC
   restringido a HTTPS para no abrir ventanas internas no controladas. */
(function () {
  'use strict';
  document.addEventListener('click', function (event) {
    var enlace = event.target && typeof event.target.closest === 'function'
      ? event.target.closest('[data-external-url]')
      : null;
    if (!enlace) return;
    if (window.codeguardAPI && typeof window.codeguardAPI.openExternal === 'function') {
      event.preventDefault();
      var url = enlace.getAttribute('data-external-url');
      Promise.resolve(window.codeguardAPI.openExternal(url)).catch(function () {
        window.open(url, '_blank', 'noopener,noreferrer');
      });
    }
  });
})();
