'use strict';

const test = require('tape');
const lettercounter = require('./05_Count_Letters.js');

test('count letters1', function countLetters1(t) {
  const actual = lettercounter('alma');
  const expected = { a: 2, l: 1, m: 1 };

  t.deepEqual(actual, expected);
  t.end();
});

test('count letters2', function countLetters1(t) {
  const actual = lettercounter('almmm');
  const expected = { a: 1, l: 1, m: 3 };

  t.deepEqual(actual, expected);
  t.end();
});