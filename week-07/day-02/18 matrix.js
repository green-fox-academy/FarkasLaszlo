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

const matrix = [];
const size = 4;
for(let i = 0; i < size; i++) {
  const empty_list = []
  for(let j = 0; j < size; j++) {
    if(i + j == size - 1){
      empty_list[j] = 1;
    }else {
      empty_list[j] = 0;
    }
  }
  matrix[i] = empty_list;
}

matrix.map(item => console.log(item));
