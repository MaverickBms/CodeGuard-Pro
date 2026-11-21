'use strict';

/**
 * Utilidades del arranque de Electron.
 *
 * El servidor empaquetado emite líneas `[CodeGuard BOOT] {json}` con el estado
 * real de migraciones y verificación del roadmap. Este módulo las interpreta
 * sin confiar en texto libre y calcula límites de espera reproducibles.
 */

const BOOT_PREFIX = '[CodeGuard BOOT] ';
const DEFAULT_STARTUP_TIMEOUT_MS = 90000;
const MIN_STARTUP_TIMEOUT_MS = 10000;
const MAX_STARTUP_TIMEOUT_MS = 300000;

const BOOT_MESSAGES = {
  'database:start': 'Preparando la base de datos local…',
  'database:migrating': 'Aplicando migraciones pendientes…',
  'database:ready': 'Base de datos disponible.',
  'profile:checking': 'Preparando el propietario local…',
  'profile:ready': 'Perfil local listo.',
  'roadmap:verifying': 'Verificando el roadmap ASCENSO…',
  'roadmap:ready': 'Roadmap verificado. No se reconstruye contenido.',
  'roadmap:loaded': 'Roadmap instalado correctamente.',
  ready: 'Iniciando la interfaz…'
};

function parseBootEvent(line) {
  if (typeof line !== 'string') return null;
  const trimmed = line.trim();
  if (!trimmed.startsWith(BOOT_PREFIX)) return null;
  let payload;
  try {
    payload = JSON.parse(trimmed.slice(BOOT_PREFIX.length));
  } catch (_error) {
    return null;
  }
  if (!payload || typeof payload !== 'object' || Array.isArray(payload)) return null;
  if (typeof payload.phase !== 'string' || typeof payload.status !== 'string') return null;
  return payload;
}

function numberOrNull(value) {
  return Number.isFinite(value) && value >= 0 ? Math.round(value) : null;
}

function formatThousands(value) {
  return String(value).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
}

function formatBootMessage(event) {
  if (!event || typeof event !== 'object') return '';
  const key = `${event.phase}:${event.status}`;
  let message = BOOT_MESSAGES[key];
  if (!message && event.phase === 'ready' && event.status === 'ok') {
    message = BOOT_MESSAGES.ready;
  }
  if (!message) return '';

  if (event.phase === 'roadmap' && event.status === 'loaded') {
    const stages = numberOrNull(event.stages);
    const modules = numberOrNull(event.modules);
    const lessons = numberOrNull(event.lessons);
    if (stages != null && modules != null && lessons != null) {
      message = `Roadmap instalado: ${stages} etapas · ${modules} módulos · ${formatThousands(lessons)} lecciones.`;
    }
  } else if (event.phase === 'roadmap' && event.status === 'ready') {
    const stages = numberOrNull(event.stages);
    const lessons = numberOrNull(event.lessons);
    if (stages != null && lessons != null) {
      message = `Roadmap verificado: ${stages} etapas · ${formatThousands(lessons)} lecciones.`;
    }
  } else if (event.phase === 'database' && event.status === 'migrating') {
    const pending = numberOrNull(event.pending);
    if (pending > 0) message = `Aplicando ${pending} migraciones pendientes…`;
  }

  const ms = numberOrNull(event.ms);
  if (ms != null && ms >= 1000) {
    message += ` (${(ms / 1000).toFixed(1)} s)`;
  }
  return message;
}

function startupTimeoutMs(env = process.env) {
  const raw = Number(env && env.CODEGUARD_STARTUP_TIMEOUT_MS);
  if (Number.isFinite(raw) && raw >= MIN_STARTUP_TIMEOUT_MS && raw <= MAX_STARTUP_TIMEOUT_MS) {
    return Math.round(raw);
  }
  return DEFAULT_STARTUP_TIMEOUT_MS;
}

function describeHealth(health) {
  if (!health || typeof health !== 'object') return '';
  const parts = [];
  if (health.database && health.database !== 'ok') parts.push(`base de datos: ${health.database}`);
  if (health.migrations && health.migrations !== 'ok') parts.push(`migraciones: ${health.migrations}`);
  if (health.roadmap && health.roadmap !== 'ok') parts.push(`roadmap: ${health.roadmap}`);
  return parts.join(' · ');
}

module.exports = {
  BOOT_PREFIX,
  DEFAULT_STARTUP_TIMEOUT_MS,
  parseBootEvent,
  formatBootMessage,
  startupTimeoutMs,
  describeHealth
};
