'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function selectLastEvenNumber(number_array, callback) {
  var last_even_number = 0;
  number_array.forEach(
    function(i) {
      if(i % 2 == 0) {
        last_even_number = i;
      }
    }
  )
  callback.call(this, last_even_number);
}

function printNumber(num) {
  console.log(num);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8