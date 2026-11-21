'use strict';

/**
 * Smoke test de la interfaz servida por Django dentro de Electron.
 *
 * Uso:
 *   node scripts/cdp-smoke.js <ws-url> basic
 *   node scripts/cdp-smoke.js <ws-url> set <tema>
 *   node scripts/cdp-smoke.js <ws-url> expect <tema>
 *
 * Comprueba las rutas principales, el catálogo de 12 temas y, opcionalmente,
 * aplica o verifica el tema persistido. Cierra la ventana al terminar para que
 * Electron detenga Django mediante su ciclo de vida normal.
 */

const THEMES = [
  'light', 'dark', 'high-contrast', 'retro-pixel', 'cyberpunk', 'fantasy',
  'sci-fi', 'warrior', 'mage', 'rogue', 'paladin', 'dark-mage'
];

async function main() {
  const [wsUrl, mode = 'basic', expectedTheme] = process.argv.slice(2);
  if (!wsUrl) throw new Error('Falta la URL WebSocket de CDP.');

  const ws = new WebSocket(wsUrl);
  let nextId = 1;
  const pending = new Map();

  ws.addEventListener('message', (event) => {
    const message = JSON.parse(event.data);
    if (message.id && pending.has(message.id)) {
      const { resolve, reject } = pending.get(message.id);
      pending.delete(message.id);
      if (message.error) reject(new Error(message.error.message));
      else resolve(message.result);
    }
  });

  await new Promise((resolve, reject) => {
    ws.addEventListener('open', resolve);
    ws.addEventListener('error', reject);
  });

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });

  const evaluate = (expression) => send('Runtime.evaluate', {
    expression,
    awaitPromise: true,
    returnByValue: true
  });

  const title = await evaluate('document.title');
  const statuses = await evaluate(`
    (async () => {
      const paths = ['/', '/roadmaps/', '/roadmaps/evaluaciones/',
        '/roadmaps/evidencias/', '/roadmaps/conocimiento/', '/roadmaps/cobertura/',
        '/roadmaps/editorial/', '/biblioteca/', '/backups/'];
      const result = {};
      for (const path of paths) {
        const response = await fetch(path, { credentials: 'same-origin' });
        result[path] = response.status;
      }
      return JSON.stringify(result);
    })()
  `);

  const parsed = JSON.parse(statuses.result.value);
  for (const [path, status] of Object.entries(parsed)) {
    if (status !== 200) throw new Error(`${path} devolvió HTTP ${status}`);
  }

  // Verificación básica de responsive: la página no debe desbordar el ancho
  // de un portátil (1024) ni una ventana estrecha (768).
  for (const [width, height] of [[1024, 720], [768, 900]]) {
    await send('Emulation.setDeviceMetricsOverride', {
      width, height, deviceScaleFactor: 1, mobile: false
    });
    const overflow = await evaluate(`JSON.stringify({
      scroll: document.documentElement.scrollWidth,
      client: document.documentElement.clientWidth
    })`);
    const metrics = JSON.parse(overflow.result.value);
    if (metrics.scroll > metrics.client + 2) {
      throw new Error(
        `Desbordamiento horizontal a ${width}px: ${metrics.scroll} > ${metrics.client}`
      );
    }
  }
  await send('Emulation.clearDeviceMetricsOverride');

  const activeNav = await evaluate(
    `document.querySelectorAll('.nav-item.cg-nav-active').length`
  );
  if (activeNav.result.value > 1) {
    throw new Error(`Hay ${activeNav.result.value} accesos marcados como activos; se esperaba como máximo 1.`);
  }

  const themeCount = await evaluate(
    `document.querySelectorAll('.ajustes-tema-btn[data-theme]').length`
  );
  if (themeCount.result.value !== 12) {
    throw new Error(`Se esperaban 12 temas; encontrados ${themeCount.result.value}`);
  }

  if (mode === 'set') {
    if (!THEMES.includes(expectedTheme)) throw new Error('Tema de prueba inválido.');
    await evaluate(`window.codeguardUI.setTheme(${JSON.stringify(expectedTheme)})`);
    await new Promise(resolve => setTimeout(resolve, 800));
  }

  const applied = await evaluate(
    `document.documentElement.getAttribute('data-theme')`
  );
  if (mode === 'set' || mode === 'expect') {
    if (!THEMES.includes(expectedTheme)) throw new Error('Tema esperado inválido.');
    if (applied.result.value !== expectedTheme) {
      throw new Error(
        `Tema aplicado ${applied.result.value}; se esperaba ${expectedTheme}`
      );
    }
  }

  console.log(`TITLE=${title.result.value}`);
  console.log(`STATUSES=${statuses.result.value}`);
  console.log(`THEMES=${themeCount.result.value}`);
  console.log(`THEME=${applied.result.value}`);

  await evaluate('window.close()');
  ws.close();
}

main().catch((error) => {
  console.error(`CDP_ERROR=${error.message}`);
  process.exit(1);
});
