'use strict';

/**
 * Valida enlaces externos abiertos desde contenido académico local.
 * Solo se permite HTTPS sin credenciales; el renderer nunca decide el comando
 * que se ejecuta, únicamente solicita abrir una URL.
 */
function isAllowedExternalUrl(value) {
  if (typeof value !== 'string' || value.length === 0 || value.length > 2000) {
    return false;
  }
  let parsed;
  try {
    parsed = new URL(value);
  } catch (_error) {
    return false;
  }
  return parsed.protocol === 'https:'
    && !parsed.username
    && !parsed.password
    && Boolean(parsed.hostname)
    && !parsed.hash;
}

module.exports = { isAllowedExternalUrl };
