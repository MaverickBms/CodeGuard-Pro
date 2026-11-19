/* CodeGuard Pro — Tutoría con IA local (Fase 3) integrada en la experiencia de lección.
   Consume los endpoints JSON de /tutoria/* (estado, pistas y análisis de intentos).
   El tutor nunca ejecuta código del estudiante ni expone la solución: la UI solo
   muestra pistas y análisis pedagógicos. */
(function () {
  'use strict';

  var ESTADO_URL = '/tutoria/estado/';
  var BASE_PISTA_URL = '/tutoria/ejercicio/';
  var TIPOS_PISTA = ['orientacion', 'estrategia', 'concretizacion'];
  var FLAG_PENDIENTE_PREFIX = 'cg-tutoria-intento-pendiente-';

  function getCookie(name) {
    var cookies = document.cookie ? document.cookie.split(';') : [];
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.indexOf(name + '=') === 0) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
    return '';
  }

  function postJsonLike(url, params) {
    var body = new URLSearchParams(params);
    var headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' };
    var csrfToken = getCookie('csrftoken');
    if (csrfToken) {
      headers['X-CSRFToken'] = csrfToken;
    }
    return fetch(url, {
      method: 'POST',
      headers: headers,
      body: body,
      credentials: 'same-origin',
    }).then(function (response) {
      return response
        .json()
        .then(function (data) { return { ok: response.ok, data: data || {} }; })
        .catch(function () {
          return { ok: false, data: { exito: false, error: 'La respuesta del servidor no es válida.' } };
        });
    });
  }

  function renderEstado(statusElement, data) {
    var disponible = Boolean(data && data.disponible);
    var modelo = (data && data.modelo) || 'tutor local';
    var limite = (data && data.limite_pistas) || 3;
    var texto = disponible
      ? 'Tutor IA disponible · modelo ' + modelo + ' · ' + limite + ' pistas por ejercicio.'
      : 'Tutor IA no disponible · se usan las pistas de apoyo de la lección.';
    var textoElement = statusElement.querySelector('.lesson-tutor-status-text');
    if (textoElement) textoElement.textContent = texto;
  }

  function cargarEstado() {
    var statusElement = document.getElementById('tutoriaStatus');
    if (!statusElement) return Promise.resolve(null);
    return fetch(ESTADO_URL, { credentials: 'same-origin' })
      .then(function (response) { return response.json(); })
      .then(function (data) { renderEstado(statusElement, data); return data; })
      .catch(function () { renderEstado(statusElement, null); });
  }

  function solicitarPista(boton) {
    var ejercicioId = boton.getAttribute('data-ejercicio-id');
    var tipo = boton.getAttribute('data-tipo') || TIPOS_PISTA[0];
    var hintElement = document.getElementById('tutoriaHint-' + ejercicioId);
    var hintTexto = hintElement ? hintElement.querySelector('.lesson-tutor-hint-text') : null;
    var hintMeta = hintElement ? hintElement.querySelector('.lesson-tutor-hint-meta') : null;
    boton.disabled = true;

    return postJsonLike(BASE_PISTA_URL + ejercicioId + '/pista/', { tipo: tipo }).then(function (response) {
      boton.disabled = false;
      var data = response.data || {};
      if (response.ok && data.exito) {
        if (hintElement) {
          hintElement.hidden = false;
          if (hintTexto) hintTexto.textContent = data.pista || '';
          if (hintMeta) {
            hintMeta.textContent = 'Pista ' + (data.numero || '') + ' de 3 · quedan ' + (data.restantes || 0) + ' pistas disponibles.';
          }
        }
        var indice = TIPOS_PISTA.indexOf(tipo);
        var siguiente = TIPOS_PISTA[indice + 1];
        if (siguiente) {
          boton.setAttribute('data-tipo', siguiente);
        }
        if ((data.restantes || 0) <= 0) {
          boton.disabled = true;
        }
      } else if (hintElement) {
        hintElement.hidden = false;
        if (hintTexto) hintTexto.textContent = (data && data.error) || 'No se pudo obtener la pista en este momento.';
        if (hintMeta) hintMeta.textContent = '';
      }
    }).catch(function () {
      boton.disabled = false;
      if (hintElement) {
        hintElement.hidden = false;
        if (hintTexto) hintTexto.textContent = 'No fue posible conectar con el servicio de tutoría. Comprueba el servidor e inténtalo de nuevo.';
        if (hintMeta) hintMeta.textContent = '';
      }
    });
  }

  function obtenerIntentoReciente(ejercicioElemento) {
    if (!ejercicioElemento) return null;
    var intentos = ejercicioElemento.querySelectorAll('.lesson-attempt');
    var intentoElemento = intentos.length ? intentos[0] : null;
    if (!intentoElemento) return null;
    return intentoElemento.getAttribute('data-intento-id');
  }

  function renderAnalisis(contenedor, data) {
    var resultado = data ? data.resultado_evaluacion : null;
    var texto = (data && data.analisis_tutor) || '';
    var resultadoElement = contenedor.querySelector('.lesson-tutor-analysis-result');
    var textoElement = contenedor.querySelector('.lesson-tutor-analysis-text');
    if (resultadoElement) {
      var etiqueta = resultado === 'aprobado'
        ? 'Aprobado'
        : resultado === 'no_aprobado'
          ? 'No aprobado'
          : 'Pendiente de revisión';
      resultadoElement.textContent = etiqueta;
    }
    if (textoElement) textoElement.textContent = texto;
  }

  function analizarIntento(ejercicioId, intentoId) {
    var contenedor = document.getElementById('tutoriaAnalisis-' + ejercicioId);
    if (!contenedor) return Promise.resolve(null);
    contenedor.hidden = true;
    return postJsonLike(BASE_PISTA_URL + ejercicioId + '/analizar/', {
      intento_ejercicio_id: intentoId,
    }).then(function (response) {
      var data = response.data || {};
      var contenedorActual = document.getElementById('tutoriaAnalisis-' + ejercicioId);
      if (response.ok && data.exito && contenedorActual) {
        contenedorActual.hidden = false;
        renderAnalisis(contenedorActual, data);
      }
      return response;
    });
  }

  function procesarIntentosPendientes() {
    var formularios = Array.prototype.slice.call(document.querySelectorAll('.lesson-submission'));
    formularios.forEach(function (formulario) {
      var ejercicioId = formulario.getAttribute('data-ejercicio-id');
      if (!ejercicioId) return;
      var clave = FLAG_PENDIENTE_PREFIX + ejercicioId;
      var pendiente = false;
      try {
        pendiente = sessionStorage.getItem(clave) === '1';
        sessionStorage.removeItem(clave);
      } catch (error) { /* almacenamiento opcional */ }
      if (!pendiente) return;

      var articulo = typeof formulario.closest === 'function'
        ? formulario.closest('.lesson-exercise')
        : null;
      var intentoId = obtenerIntentoReciente(articulo);
      if (!intentoId) return;
      analizarIntento(ejercicioId, intentoId);
    });
  }

  function inicializar() {
    cargarEstado();

    document.addEventListener('click', function (event) {
      var objetivo = event.target;
      var boton = objetivo && typeof objetivo.closest === 'function'
        ? objetivo.closest('.lesson-tutor-pista-btn')
        : null;
      if (!boton) return;
      event.preventDefault();
      solicitarPista(boton);
    });

    document.addEventListener('submit', function (event) {
      var formulario = event.target;
      if (!formulario || typeof formulario.matches !== 'function') return;
      if (!formulario.matches('.lesson-submission')) return;
      var ejercicioId = formulario.getAttribute('data-ejercicio-id');
      if (!ejercicioId) return;
      try {
        sessionStorage.setItem(FLAG_PENDIENTE_PREFIX + ejercicioId, '1');
      } catch (error) { /* almacenamiento opcional */ }
    });

    document.addEventListener('DOMContentLoaded', procesarIntentosPendientes);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializar);
  } else {
    inicializar();
  }
})();
