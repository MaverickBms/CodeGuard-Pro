'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { isAllowedExternalUrl } = require('./external-links');

test('acepta HTTPS sin credenciales', () => {
  assert.equal(isAllowedExternalUrl('https://www.youtube.com/watch?v=abc'), true);
  assert.equal(isAllowedExternalUrl('https://doi.org/10.1000/xyz'), true);
});

test('rechaza esquemas y URLs peligrosas', () => {
  for (const value of [
    'http://example.com',
    'file:///etc/passwd',
    'javascript:alert(1)',
    'https://user:pass@example.com',
    'https://example.com/#fragment',
    '',
    null,
    42
  ]) {
    assert.equal(isAllowedExternalUrl(value), false, String(value));
  }
});
