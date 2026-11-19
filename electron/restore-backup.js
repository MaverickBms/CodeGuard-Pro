'use strict';

const fs = require('fs');
const path = require('path');

/**
 * Valida una ruta elegida por el usuario para restaurar una copia.
 * Solo acepta archivos .zip regulares existentes. La validación profunda del
 * contenido la realiza el servidor (manifest, hashes e integridad SQLite).
 */
function resolveBackupPath(candidate) {
  if (typeof candidate !== 'string') return null;
  const value = candidate.trim();
  if (!value) return null;

  const resolved = path.resolve(value);
  if (path.extname(resolved).toLowerCase() !== '.zip') return null;

  try {
    const stats = fs.lstatSync(resolved);
    if (!stats.isFile() || stats.isSymbolicLink()) return null;
  } catch (_error) {
    return null;
  }
  return resolved;
}

module.exports = { resolveBackupPath };
