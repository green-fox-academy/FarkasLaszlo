'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

var matrix = [];
var size = 4;
for(var i = 0; i < size; i++) {
  var empty_list = []
  for(var j = 0; j < size; j++) {
    if(i + j == size - 1){
      empty_list[j] = 1;
    }else {
      empty_list[j] = 0;
    }
  }
  matrix[i] = empty_list;
}

console.log(matrix);
