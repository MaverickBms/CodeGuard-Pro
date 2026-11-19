'use strict';

const fs = require('fs');
const path = require('path');

const FILE_NAME = 'ui-preferences.json';

/**
 * Lee el tema persistido en el perfil. Un archivo ausente, ilegible o con un
 * valor no permitido se degrada al tema claro sin bloquear el arranque.
 */
function readTheme(filePath, allowedThemes, fallback = 'light') {
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    const parsed = JSON.parse(raw);
    const theme = parsed && parsed.theme;
    if (typeof theme === 'string' && allowedThemes.includes(theme)) return theme;
  } catch (_error) {
    // Sin preferencias previas o archivo corrupto: usar fallback.
  }
  return fallback;
}

/**
 * Guarda el tema de forma atómica. Solo acepta identificadores del catálogo
 * oficial; nunca escribe rutas ni valores proporcionados sin validar.
 */
function writeTheme(filePath, theme, allowedThemes) {
  if (typeof theme !== 'string' || !allowedThemes.includes(theme)) {
    throw new Error('Tema no permitido.');
  }
  const directory = path.dirname(filePath);
  fs.mkdirSync(directory, { recursive: true });
  const temporary = `${filePath}.tmp-${process.pid}`;
  try {
    fs.writeFileSync(
      temporary,
      JSON.stringify({ theme }, null, 2) + '\n',
      { mode: 0o600 }
    );
    fs.renameSync(temporary, filePath);
  } finally {
    try {
      fs.unlinkSync(temporary);
    } catch (_error) {
      // El rename ya movió el archivo o no llegó a crearse.
    }
  }
  return theme;
}

module.exports = { FILE_NAME, readTheme, writeTheme };
