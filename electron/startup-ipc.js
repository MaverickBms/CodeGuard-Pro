'use strict';

function classifyInteractiveSignal(payload) {
  const source = payload && typeof payload.source === 'string' ? payload.source : 'unknown';
  const verified = source === 'frontend-explicit';
  return { source, verified };
}

function shouldAcceptInteractiveSignal({ trusted, senderIsMain, alreadyInteractive, alreadyFallback }) {
  if (!trusted) return { ok: false, reason: 'untrusted' };
  if (!senderIsMain) return { ok: false, reason: 'wrong-sender' };
  if (alreadyInteractive || alreadyFallback) return { ok: false, reason: 'already-resolved' };
  return { ok: true };
}

function startupPhaseFromBootEvent(event) {
  const phaseMap = { database: 'database', profile: 'profile', roadmap: 'roadmap', content: 'roadmap', ready: 'services', services: 'services' };
  const phase = phaseMap[event && event.phase];
  if (!phase) return null;
  let status = 'active';
  if (event.status === 'ready' || event.status === 'ok' || event.status === 'loaded' || event.status === 'seeded') status = 'done';
  if (event.status === 'unavailable' || event.status === 'error') status = 'error';
  return { phase, status };
}

module.exports = { classifyInteractiveSignal, shouldAcceptInteractiveSignal, startupPhaseFromBootEvent };
