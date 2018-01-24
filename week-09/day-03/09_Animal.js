"use strict";

function Animal() {
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function () {
    this.hunger -= 1;
  };
  this.drink = function () {
    this.thirst -= 1;
  };
  this.play = function () {
    this.hunger += 1;
    this.thirst += 1;
  };
}

module.exports = Animal;
