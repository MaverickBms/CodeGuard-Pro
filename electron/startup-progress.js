'use strict';

const PHASES = [
  { id: 'electron', label: 'Entorno de escritorio', weight: 20 },
  { id: 'database', label: 'Base de datos local', weight: 20 },
  { id: 'profile', label: 'Perfil local', weight: 10 },
  { id: 'roadmap', label: 'Estructura ASCENSO', weight: 20 },
  { id: 'services', label: 'Servicios de aprendizaje', weight: 15 },
  { id: 'ui', label: 'Interfaz principal', weight: 15 },
];

const QUOTES = [
  { t: 'Un paso a la vez sigue siendo avanzar.' },
  { t: 'Hoy estás más cerca de tu meta que ayer.' },
  { t: '15 minutos diarios superan a 3 horas una vez al mes.' },
  { t: 'La constancia le gana al talento cuando el talento no practica.' },
  { t: 'Ya hiciste lo más difícil: empezar.' },
  { t: 'No tienes que saberlo todo hoy, solo un poco más que ayer.' },
  { t: 'Aprender algo nuevo siempre se siente incómodo al principio. ¡Vas bien!' },
  { t: 'La vida es como andar en bicicleta. Para mantener el equilibrio, debes seguir moviéndote.', a: 'Albert Einstein' },
  { t: 'La forma de empezar es dejar de hablar y comenzar a hacer.', a: 'Walt Disney' },
  { t: 'No me preocupa que me hayan robado la idea, me preocupa que no tengan ninguna propia.', a: 'Nikola Tesla' },
  { t: 'He fallado una y otra vez en mi vida. Por eso he tenido éxito.', a: 'Michael Jordan' },
  { t: 'No puedes poner un límite a nada. Cuanto más sueñas, más lejos llegas.', a: 'Michael Phelps' },
  { t: 'Primero resuelve el problema. Después, escribe el código.', a: 'John Johnson' },
];

function createStartupProgress(options = {}) {
  const now = options.now || (() => Date.now());
  const quotes = options.quotes || QUOTES;
  const quoteIntervalMs = options.quoteIntervalMs ?? 15000;
  const phases = PHASES.map(p => ({ ...p }));
  const state = {
    phases: Object.fromEntries(phases.map(p => [p.id, 'pending'])),
    percent: 0,
    task: 'Preparando CodeGuard Pro…',
    detail: 'Iniciando el entorno de escritorio.',
    error: '',
    interactive: false,
    quoteIdx: -1,
    lastQuoteAt: 0,
  };

  function pickQuote(force = false) {
    const ts = now();
    if (!force && state.quoteIdx !== -1 && ts - state.lastQuoteAt < quoteIntervalMs) return null;
    let idx = 0;
    if (quotes.length <= 1) {
      idx = 0;
    } else {
      const rnd = options.random || Math.random;
      for (let tries = 0; tries < 10; tries += 1) {
        idx = Math.floor(rnd() * quotes.length);
        if (idx !== state.quoteIdx) break;
      }
      if (idx === state.quoteIdx) idx = (state.quoteIdx + 1) % quotes.length;
    }
    state.quoteIdx = idx;
    state.lastQuoteAt = ts;
    const q = quotes[idx];
    return q.a ? `“${q.t}” — ${q.a}` : `“${q.t}”`;
  }

  function computePercent() {
    let done = 0;
    let active = 0;
    for (const p of phases) {
      const st = state.phases[p.id];
      if (st === 'done') done += p.weight;
      else if (st === 'active') active += p.weight * 0.5;
    }
    let pct = Math.round(done + active);
    if (!state.interactive && pct > 99) pct = 99;
    if (state.interactive) pct = 100;
    return Math.max(state.percent, Math.min(100, pct));
  }

  function update(input = {}) {
    const allowed = new Set(['pending', 'active', 'done', 'error']);
    if (input.phase && state.phases[input.phase] !== undefined && allowed.has(input.status)) {
      state.phases[input.phase] = input.status;
    }
    if (Array.isArray(input.phases)) {
      for (const it of input.phases) {
        if (it && it.id && state.phases[it.id] !== undefined && allowed.has(it.status)) {
          state.phases[it.id] = it.status;
        }
      }
    }
    if (typeof input.task === 'string' && input.task) state.task = input.task.slice(0, 160);
    if (typeof input.detail === 'string') state.detail = input.detail.slice(0, 300);
    if (typeof input.error === 'string') state.error = input.error.slice(0, 500);
    if (input.interactive === true) state.interactive = true;
    state.percent = computePercent();
    const quote = pickQuote(Boolean(input.forceQuote));
    return snapshot(quote);
  }

  function snapshot(quote = null) {
    return {
      percent: state.percent,
      task: state.task,
      detail: state.detail,
      error: state.error,
      interactive: state.interactive,
      phases: phases.map(p => ({ id: p.id, label: p.label, status: state.phases[p.id] })),
      quote: quote || undefined,
    };
  }

  return { update, snapshot: () => snapshot(null), pickQuote, state, PHASES: phases };
}

module.exports = { PHASES, QUOTES, createStartupProgress };
