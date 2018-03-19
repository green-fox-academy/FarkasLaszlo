'use strict';

let lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

lineCount -= 1;
let n = 1;
const sign = '%';
const space = ' ';
console.log(sign.repeat(lineCount + 1));
while(n < lineCount) {
  console.log(sign + space.repeat(n - 1) + sign + space.repeat(lineCount - n - 1) + sign);
  n++;
}
console.log(sign.repeat(lineCount + 1));