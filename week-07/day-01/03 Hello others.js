'use strict';

// Greet 3 of your classmates with this program, in three separate lines
// like:
//
// Hello, Esther!
// Hello, Mary!
// Hello, Joe!

const classmates = ['Nándi', 'Andris', 'Miki'];

classmates.map((mate) => {
  console.log(`Hello, ${mate}!`);
})