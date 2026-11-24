'use strict';

/**
 * Smoke E2E de formularios reales dentro de Electron.
 *
 * Comprueba que la política de referrer permite CSRF en peticiones same-origin,
 * que la importación multipart de la biblioteca persiste y que un POST de
 * cambio de estado funciona. Se ejecuta contra una ventana Electron con
 * `--remote-debugging-port` abierta y un perfil temporal.
 *
 * Uso:
 *   node scripts/cdp-form-smoke.js <ws-url>
 */

const fs = require('fs');
const os = require('os');
const path = require('path');

const pdfBytes = () => Buffer.from(
  `%PDF-1.4\n% CodeGuard form smoke ${Date.now()}\n` +
  '1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n' +
  '2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n' +
  '3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] >>\nendobj\n' +
  'trailer\n<< /Root 1 0 R >>\n%%EOF\n'
);

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function main() {
  const wsUrl = process.argv[2];
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

  const evaluate = async (expression) => {
    const result = await send('Runtime.evaluate', {
      expression,
      awaitPromise: true,
      returnByValue: true
    });
    if (result.exceptionDetails) {
      throw new Error(result.exceptionDetails.text || 'Error de evaluación en el renderer');
    }
    return result.result.value;
  };

  const temporal = path.join(os.tmpdir(), `codeguard-form-${process.pid}.pdf`);
  fs.writeFileSync(temporal, pdfBytes(), { mode: 0o600 });

  try {
    await send('Page.enable');
    await send('Runtime.enable');
    await send('DOM.enable');

    const origin = await evaluate('location.origin');
    await send('Page.navigate', { url: `${origin}/biblioteca/importar/` });
    await sleep(1000);

    const documentNode = await send('DOM.getDocument', { depth: -1 });
    const fileInput = await send('DOM.querySelector', {
      nodeId: documentNode.root.nodeId,
      selector: 'input[type=file]'
    });
    if (!fileInput.nodeId) throw new Error('No se encontró el campo de archivo de la biblioteca.');
    await send('DOM.setFileInputFiles', { nodeId: fileInput.nodeId, files: [temporal] });

    const titulo = `Documento E2E ${Date.now()}`;
    await evaluate(`(() => {
      document.querySelector('#id_titulo').value = ${JSON.stringify(titulo)};
      document.querySelector('#id_categoria').value = 'manual';
      document.querySelector('#id_etiquetas').value = 'e2e, formulario';
      return true;
    })()`);
    await evaluate("document.querySelector('form[enctype] button[type=submit]').click(); true");
    await sleep(1800);

    const url = await evaluate('location.pathname');
    if (!/^\/biblioteca\/\d+\/$/.test(url)) {
      const body = await evaluate('document.body.innerText.slice(0, 500)');
      throw new Error(`La importación no redirigió al detalle: ${url}\n${body}`);
    }
    const contieneTitulo = await evaluate(`document.body.innerText.includes(${JSON.stringify(titulo)})`);
    if (!contieneTitulo) throw new Error('El detalle no muestra el título importado.');
    const iframe = await evaluate("(() => { const f = document.querySelector('iframe'); return f ? f.getAttribute('src') : ''; })()");
    if (!/\/archivo\/$/.test(iframe)) throw new Error('El visor PDF no apunta al archivo local.');

    await evaluate("Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Archivar')).click(); true");
    await sleep(1200);
    const archivado = await evaluate("document.body.innerText.includes('Archivado')");
    if (!archivado) throw new Error('El cambio de estado del documento no se aplicó.');

    console.log(`FORM_SMOKE_OK=${url}`);
  } finally {
    try {
      fs.unlinkSync(temporal);
    } catch (_error) {
      // El archivo temporal pudo eliminarse ya.
    }
    ws.close();
  }
}

main().catch((error) => {
  console.error(`[ERROR] ${error.message}`);
  process.exit(1);
});
