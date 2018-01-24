"use strict";

function getRandomInt(min, max) {
  return Math.floor(Math.random() * ((max - min) + 1)) + min;
}

function CAB(gameState = 'playing', counter = 0, number = getRandomInt(1000, 9999)) {
  this.gameState = gameState;
  this.counter = counter;
  this.number = number;
  this.answer = [];
  this.guess = function (guessNumber) {
    this.answer = [];
    this.counter += 1;
    for (let i = 0; i < 4; i++) {
      Math.floor(guessNumber / (10 ** i)) % 10 === Math.floor(this.number / (10 ** i)) % 10 ? 
      this.answer.push('cow'):
      this.answer.push('bull');
    }
    this.answer.reverse();
    this.finishedGame();
  };
  this.finishedGame = function () {
    if (this.answer[0] + this.answer[1] + this.answer[2] + this.answer[3] === 'cowcowcowcow') {
      this.gameState = 'finished';
    }
  };
}

module.exports = CAB;
