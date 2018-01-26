'use strict';

const test = require('tape');
const Sharpie = require('./08_Sharpie.js');

const sharpie1 = new Sharpie('red', 5);

test('sharpie', function doSharpie1(t) {
  const actual = sharpie1.inkAmount;
  const expected = 100;

  t.equal(actual, expected);
  t.end();
});

test('use sharpie', function doSharpie2(t) {
  sharpie1.use();
  const actual = sharpie1.inkAmount;
  const expected = 0;

  t.equal(actual, expected);
  t.end();
});