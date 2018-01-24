"use strict";

//  Search back in your own project the Sharpie class you made on the OO workshop
//  Create tests that covers all types of input (like in the previous workshop exercise)

function Sharpie(color, width) {
  this.color = color;
  this.width = width;
  this.inkAmount = 100;
  this.use = function () {
    while (this.inkAmount > 0) {
      this.inkAmount -= this.width;
      console.log(this.inkAmount);
    }
  };
}

module.exports = Sharpie;
