'use strict';

const test = require('tape');
const CAB = require('./10_CaB.js');

const cab1 = new CAB('playing', 0, 4000);

test('original number', function number(t) {
  const actual = cab1.number;
  const expected = 4000;
  t.equal(actual, expected);
  t.end();
});

test('state', function state(t) {
  const actual = cab1.gameState;
  const expected = 'playing';
  t.equal(actual, expected);
  t.end();
});

test('original counter', function originalCounter(t) {
  const actual = cab1.counter;
  const expected = 0;
  t.equal(actual, expected);
  t.end();
});

test('counter works', function counter(t) {
  cab1.guess(2000);
  const actual = cab1.counter;
  const expected = 1;
  t.equal(actual, expected);
  t.end();
});

test('guess works', function guess(t) {
  cab1.guess(2000);
  const actual = cab1.answer;
  const expected = ['bull', 'cow', 'cow', 'cow'];
  t.deepEqual(actual, expected);
  t.end();
});

test('finished', function finished(t) {
  cab1.guess(4000);
  const actual = cab1.gameState;
  const expected = 'finished';
  t.equal(actual, expected);
  t.end();
});