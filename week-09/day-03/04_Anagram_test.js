'use strict';

const test = require('tape');
const anagramchecker = require('./04_Anagram.js');

test('check anagram', function anagram(t) {
  const actual = anagramchecker('safetyrail', 'Fairytales');
  const expected = true;

  t.equal(actual, expected);
  t.end();
});
