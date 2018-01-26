'use strict';

const test = require('tape');
const calculateSum = require('./03_Sum.js');

test('sum integers', function sumInteger(t) {
  const actual = calculateSum.sum([5, 5, 5, 4, 5, 6]);
  const expected = 30;

  t.equal(actual, expected);
  t.end();
});

test('sum empty list', function sumInteger(t) {
  const actual = calculateSum.sum([]);
  const expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('sum one element', function sumInteger(t) {
  const actual = calculateSum.sum([6]);
  const expected = 6;

  t.equal(actual, expected);
  t.end();
});

test('sum null', function sumInteger(t) {
  const actual = calculateSum.sum([null]);
  const expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('sum string', function sumInteger(t) {
  const actual = calculateSum.sum(['apple', 'pear']);
  const expected = '0applepear';

  t.equal(actual, expected);
  t.end();
});
