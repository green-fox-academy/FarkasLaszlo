'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var n = 2;
var sign = "%";
var space = " ";
console.log(sign.repeat(lineCount));
while(n < lineCount) {
  console.log(sign + space.repeat(lineCount - 2) + sign);
  n++;
}
console.log(sign.repeat(lineCount));
