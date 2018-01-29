'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(word) {
  this.word = word;
}

Animal.prototype.say = function() {
  console.log(this.word);
}

const animal1 = new Animal('Hello');
animal1.say();