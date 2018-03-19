'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
  if (number > 1) {
    return number * factorio(number - 1);
  } else if (number == 1) {
    return 1;
  }
}

console.log(factorio(3));
console.log(factorio(4));
console.log(factorio(5));
console.log(factorio(10));
console.log(factorio(15));