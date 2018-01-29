'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function createRectangles(sideA, sideB) {
  this.sideA = sideA;
  this.sideB = sideB;
}

createRectangles.prototype.getArea = function() {
  console.log(this.sideA * this.sideB);
}

createRectangles.prototype.getCircumreference = function() {
  console.log((this.sideA ** 2 + this.sideB ** 2) ** 0.5);
}

const rectangle1 = new createRectangles(3, 4);
rectangle1.getArea();
rectangle1.getCircumreference();