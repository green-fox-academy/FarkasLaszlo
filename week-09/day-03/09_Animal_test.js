'use strict';

const test = require('tape');
const Animal = require('./09_Animal.js');

const animal1 = new Animal(); 

test('animal hunger', function animalHunger(t) {
  const actual = animal1.hunger;
  const expected = 5;
  t.equal(actual, expected);
  t.end();
});

test('animal thirst', function animalThirst(t) {
  const actual = animal1.thirst;
  const expected = 5;
  t.equal(actual, expected);
  t.end();
});

test('animal eat', function animalEat(t) {
  animal1.eat()
  const actual = animal1.hunger;
  const expected = 4;

  t.equal(actual, expected);
  t.end();
});

test('animal drink', function animalDrink(t) {
  animal1.drink();
  const actual = animal1.thirst;
  const expected = 4;

  t.equal(actual, expected);
  t.end();
});

test('animal play', function animalPlay(t) {
  animal1.play();
  const actual = animal1.thirst + animal1.hunger;
  const expected = 10;

  t.equal(actual, expected);
  t.end();
});