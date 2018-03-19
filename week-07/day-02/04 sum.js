'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(number) {
  if (number > 0){
    return number + sum(number - 1);
  } else if (number == 0) {
    return 0;
  }
}

console.log(sum(3));
console.log(sum(4));
console.log(sum(5));
console.log(sum(10));
console.log(sum(15));