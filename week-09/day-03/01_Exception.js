'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

function throwError(wrongParameter) {
  throw String(wrongParameter) + ' is a ' + typeof wrongParameter + ' and not a string';
}

const printStr = function (str) {
  console.log(str);
};

const addString = function (str1, str2, printString) {
  let newStr;
  typeof str1 !== 'string' ? throwError(str1):
  typeof str2 !== 'string' ? throwError(str2):
  typeof printString !== 'function' ? throwError(printString):
  newStr = str1 + str2;
  printStr(newStr);
};

addString("It's", ' cool', printStr);
