'use strict';

const test = require('tape');
const fibonacci = require('./06_Fibonacci.js');

test('fibonacci1', function fibonacci1(t) {
  const actual = fibonacci(4);
  const expected = 24;

  t.equal(actual, expected);
  t.end();
});

test('fibonacci2', function fibonacci2(t) {
  const actual = fibonacci(5);
  const expected = 120;

  t.equal(actual, expected);
  t.end();
});

test('fibonacci3', function fibonacci3(t) {
  const actual = fibonacci();
  const expected = 1;

  t.equal(actual, expected);
  t.end();
});
