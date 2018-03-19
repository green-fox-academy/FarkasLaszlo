'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

const listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16];

function numChecker(numbers) {
  if (numbers.includes(4) && numbers.includes(8) && numbers.includes(12) && numbers.includes(16)) {
      return true;
  }
  return false;
}

console.log(numChecker(listOfNumbers));