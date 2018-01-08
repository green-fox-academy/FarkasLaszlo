'use strict';

var lineCount = 7;

// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

var n = 0;
var space = " ";
var star = "*";
while(n <= lineCount / 2) {
  console.log(space.repeat(lineCount - n) + star.repeat(2 * n + 1));
  n++;
}
n -= 2;

while(0 <= n && n < lineCount/2 ) {
  console.log(space.repeat(lineCount - n) + star.repeat(2 * n + 1));
  n--;
}