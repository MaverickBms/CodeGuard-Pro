/* ==========================================================================
   CodeGuard Pro — Ajustes JS (WP-REDESIGN-02 / FASE 4)
   Archivo: static/js/settings.js
   
   JavaScript vanilla, sin dependencias externas.
   Degradación graciosa: si este script falla, el panel de ajustes no se abre
   pero el resto de la aplicación sigue funcionando.
   
   Funcionalidad:
   - Abrir/cerrar panel de ajustes
   - Cambiar tema (claro/oscuro) con persistencia en localStorage
   - Cerrar al hacer clic fuera del panel o en la tecla Esc
   - No manipula cookies, localStorage salvo el tema seleccionado
   - No realiza fetch a URLs externas
   ========================================================================== */

(function () {
  'use strict';

  var btnAjustes = document.getElementById('btnAjustes');
  var btnCerrarAjustes = document.getElementById('btnCerrarAjustes');
  var btnGuardarAjustes = document.getElementById('btnGuardarAjustes');
  var ajustesPanel = document.getElementById('ajustesPanel');
  var ajustesOverlay = document.getElementById('ajustesOverlay');
  var btnsTema = document.querySelectorAll('.ajustes-tema-btn');
  var btnVerTerminos = document.getElementById('btnVerTerminos');
  var btnVerPrivacidad = document.getElementById('btnVerPrivacidad');

  if (!btnAjustes || !btnCerrarAjustes || !ajustesPanel || !ajustesOverlay) {
    return;
  }

  // Cargar tema guardado al iniciar
  function cargarTemaGuardado() {
    var temaGuardado = localStorage.getItem('codeguard-tema');
    if (temaGuardado && (temaGuardado === 'light' || temaGuardado === 'dark')) {
      aplicarTema(temaGuardado);
      marcarTemaSeleccionado(temaGuardado);
    }
  }

  // Aplicar tema al documento
  function aplicarTema(tema) {
    document.documentElement.setAttribute('data-theme', tema);
    document.body.setAttribute('data-theme', tema);
    localStorage.setItem('codeguard-tema', tema);
  }

  // Marcar botón de tema seleccionado en la UI
  function marcarTemaSeleccionado(tema) {
    btnsTema.forEach(function (btn) {
      if (btn.dataset.theme === tema) {
        btn.classList.add('activo');
      } else {
        btn.classList.remove('activo');
      }
    });
  }

  // Abrir panel de ajustes
  function abrirAjustes() {
    ajustesPanel.classList.add('activo');
    btnCerrarAjustes.focus();
  }

  // Cerrar panel de ajustes
  function cerrarAjustes() {
    ajustesPanel.classList.remove('activo');
    btnAjustes.focus();
  }

  // Cambiar tema
  function cambiarTema(tema) {
    aplicarTema(tema);
    marcarTemaSeleccionado(tema);
    cerrarAjustes();
  }

  // Event listeners
  btnAjustes.addEventListener('click', abrirAjustes);

  btnCerrarAjustes.addEventListener('click', cerrarAjustes);

  btnGuardarAjustes.addEventListener('click', function () {
    cerrarAjustes();
  });

  btnsTema.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tema = btn.dataset.theme;
      cambiarTema(tema);
    });
  });

  // Cerrar al hacer clic fuera del panel (sobre el overlay)
  ajustesOverlay.addEventListener('click', cerrarAjustes);

  // Cerrar con tecla Esc
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && ajustesPanel.classList.contains('activo')) {
      cerrarAjustes();
    }
  });

  // Inicializar
  cargarTemaGuardado();

})();
