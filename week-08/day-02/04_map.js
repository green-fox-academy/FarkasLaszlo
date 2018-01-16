'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana',
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.
var e_list = fruits.map(function(i) {
  var count = 0;
  i.split("").map(function(x) {
    if(x == "e") {
      count++;
    }
  })
  return count;
})

console.log(e_list);