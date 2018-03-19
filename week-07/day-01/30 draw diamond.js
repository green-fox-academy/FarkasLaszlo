'use strict';

const lineCount = 7;

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
var space = ' ';
var star = '*';

for (let i = 1; i < lineCount + 2; i++) {
  if(i <= lineCount / 2) {
    console.log(space.repeat(lineCount - n) + star.repeat(2 * n + 1));
    n += 1;
  }
  if(i > lineCount / 2 && n >= 0) {
    console.log(space.repeat(lineCount - n) + star.repeat(2 * n + 1));
    n -= 1;
  }
}
    
        