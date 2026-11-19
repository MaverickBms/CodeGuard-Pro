'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { isTrustedIpcSender } = require('./ipc-security');

const HOST = '127.0.0.1';
const PORT = 43127;
const sender = url => ({ senderFrame: { url } });

test('acepta el origen local exacto y el puerto dinámico esperado', () => {
  assert.equal(
    isTrustedIpcSender(sender(`http://${HOST}:${PORT}/`), HOST, PORT),
    true
  );
});

test('rechaza un puerto distinto', () => {
  assert.equal(
    isTrustedIpcSender(sender(`http://${HOST}:43128/`), HOST, PORT),
    false
  );
});

test('rechaza hosts que solo comparten el prefijo loopback', () => {
  assert.equal(
    isTrustedIpcSender(sender(`http://127.0.0.1.attacker.test:${PORT}/`), HOST, PORT),
    false
  );
});

test('rechaza protocolo remoto o inseguro', () => {
  assert.equal(
    isTrustedIpcSender(sender(`https://${HOST}:${PORT}/`), HOST, PORT),
    false
  );
  assert.equal(
    isTrustedIpcSender(sender(`file:///`), HOST, PORT),
    false
  );
});

test('rechaza credenciales incrustadas en la URL', () => {
  assert.equal(
    isTrustedIpcSender(sender(`http://user@127.0.0.1:${PORT}/`), HOST, PORT),
    false
  );
});

test('rechaza eventos, frames y puertos inválidos', () => {
  assert.equal(isTrustedIpcSender(null, HOST, PORT), false);
  assert.equal(isTrustedIpcSender({}, HOST, PORT), false);
  assert.equal(isTrustedIpcSender(sender('not a url'), HOST, PORT), false);
  assert.equal(isTrustedIpcSender(sender(`http://${HOST}:${PORT}/`), HOST, 0), false);
  assert.equal(isTrustedIpcSender(sender(`http://${HOST}:${PORT}/`), HOST, null), false);
});
