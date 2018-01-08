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

var space = " ";
var sign = "%";
var a = 0;
var linecount = 4;
while(a < linecount) {
  console.log((sign + space).repeat(linecount));
  console.log((space + sign).repeat(linecount));
  a++;
}