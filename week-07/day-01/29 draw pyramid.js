'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

var space = " ";
var star = "*";
for(var i = 0; i < lineCount;i++){
  console.log(space.repeat(lineCount - i) + star.repeat(2 * i + 1));
}