'use strict';

const test = require('tape');
const apple = require('./02_Apples.js');

function Tester(actual, expected) {
  this.actual = actual;
  this.expected = expected;
}

test('log apple', function logApple(t) {
  const tester1 = new Tester(apple.getApple(), 'apple');

  t.equal(tester1.actual, tester1.expected);
  t.end();
});
