'use strict';

// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

const space = ' ';
const sign = '%';
let a = 0;
const linecount = 4;
while(a < linecount) {
  console.log((sign + space).repeat(linecount));
  console.log((space + sign).repeat(linecount));
  a++;
}