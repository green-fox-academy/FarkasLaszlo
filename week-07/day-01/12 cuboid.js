'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

const a = 10;
const b = 10;
const c = 10;

console.log('Surface Area: ' + ((2 * a * b) + (2 * c * b) + (2 * a * c)));
console.log('Volume: ' + (a * b * c));