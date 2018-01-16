'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds
function Printer() {
  console.log("apple");
  setTimeout(function() {
    console.log("pear");
    setTimeout(function() {
      console.log("melon");
      setTimeout(function() {
        console.log("grapes");
      }, 2000);
    }, 2000);
  
  }, 1000);
}

Printer();
