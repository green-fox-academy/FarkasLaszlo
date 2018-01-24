'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){
  let newStr = "";
  typeof str1 != "string" ? throwError(str1):
  typeof str2 != "string" ? throwError(str2):
  typeof printStr != "function" ? throwError(printStr):
  newStr = str1 + str2;
  
  function throwError(wrongParameter) {
    throw wrongParameter + ' is a ' + typeof wrongParameter + ' and not a string';
  }
  
  printStr(newStr);
}

let printStr = function(str) {
  console.log(str);
}

addString("It's", " cool", printStr);