/* ==========================================================================
   CodeGuard Pro — Onboarding JS (WP-REDESIGN-02, FASE 2)
   Archivo: static/js/onboarding.js
   
   JavaScript vanilla, sin dependencias externas.
   Degradación graciosa: si este script falla o no se carga, el formulario
   de setup funciona normalmente como envío estándar de Django.
   
   Funcionalidad:
   - Habilita/deshabilita el botón de envío según completitud de campos.
   - No manipula cookies, localStorage ni datos sensibles.
   - No realiza fetch a URLs externas.
   ========================================================================== */

(function () {
  'use strict';

  var form = document.getElementById('form-setup-inicial');
  var btn = document.getElementById('btn-setup-siguiente');
  var usernameInput = document.getElementById('id_username');
  var password1Input = document.getElementById('id_password1');
  var password2Input = document.getElementById('id_password2');
  var terminosInput = document.getElementById('id_aceptar_terminos');

  if (!form || !btn) {
    return;
  }

  function actualizarEstadoBoton() {
    var usuarioValido = usernameInput && usernameInput.value.trim().length > 0;
    var pass1Valido = password1Input && password1Input.value.trim().length >= 8;
    var pass2Valido = password2Input && password2Input.value.trim().length > 0;
    var terminosValido = terminosInput && terminosInput.checked;

    if (usuarioValido && pass1Valido && pass2Valido && terminosValido) {
      btn.removeAttribute('disabled');
      btn.classList.remove('cg-btn-disabled');
    } else {
      btn.setAttribute('disabled', 'disabled');
      btn.classList.add('cg-btn-disabled');
    }
  }

  function inicializar() {
    actualizarEstadoBoton();

    [usernameInput, password1Input, password2Input].forEach(function (input) {
      if (input) {
        input.addEventListener('input', actualizarEstadoBoton);
        input.addEventListener('change', actualizarEstadoBoton);
      }
    });

    if (terminosInput) {
      terminosInput.addEventListener('change', actualizarEstadoBoton);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializar);
  } else {
    inicializar();
  }
})();
