'use strict';

/**
 * Comprueba que un mensaje IPC procede del origen HTTP local exacto
 * que Electron asignó al servidor Django de esta ejecución.
 *
 * No confía en prefijos de URL (que aceptarían hosts como 127.0.0.1.evil)
 * ni en el hostname aislado: también exige protocolo y puerto exactos.
 */
function isTrustedIpcSender(event, host, port) {
  if (
    typeof host !== 'string' ||
    !host ||
    !Number.isInteger(port) ||
    port < 1 ||
    port > 65535
  ) {
    return false;
  }

  const frameUrl = event?.senderFrame?.url;
  if (typeof frameUrl !== 'string' || !frameUrl) return false;

  try {
    const parsed = new URL(frameUrl);
    return (
      parsed.protocol === 'http:' &&
      parsed.hostname === host &&
      parsed.port === String(port) &&
      !parsed.username &&
      !parsed.password
    );
  } catch (_error) {
    return false;
  }
}

module.exports = { isTrustedIpcSender };
