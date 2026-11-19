'use strict';

/**
 * Devuelve un error si el proceso hijo no puede seguir arrancando.
 * ChildProcess mantiene exitCode y signalCode en null mientras sigue activo.
 */
function getChildStartupFailure(child) {
  if (!child || typeof child !== 'object') {
    return new Error('No se pudo iniciar el servidor local: proceso hijo no disponible.');
  }
  if (child.spawnError) {
    return new Error(`No se pudo iniciar el servidor local: ${child.spawnError.message}`);
  }
  if (child.exitCode != null || child.signalCode != null) {
    const reason = child.signalCode
      ? `señal ${child.signalCode}`
      : `código ${child.exitCode}`;
    return new Error(
      `El servidor local terminó antes de estar disponible (${reason}). Revisa los registros de CodeGuard Pro.`
    );
  }
  return null;
}

module.exports = { getChildStartupFailure };
