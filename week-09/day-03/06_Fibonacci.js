"use strict";
// Write a function that computes a member of the fibonacci sequence by a given index
// Create tests that covers all types of input (like in the previous workshop exercise)

function fibonacci(n) {
  if (n > 1) {
    return n * fibonacci(n - 1);
  }
  return 1;
}

module.exports = fibonacci;