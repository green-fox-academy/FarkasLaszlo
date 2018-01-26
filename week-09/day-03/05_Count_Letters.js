"use strict";
// Write a function, that takes a string as an argument
// and returns a dictionary with all letters in the string as keys,
// and numbers as values that shows how many occurrences there are.
// Create a test for that.

function letterCounter(string) {
  const object = {};
  string.split('').forEach(function createObject(str) {
    object[str] = (object[str] || 0) + 1;
  });
  return object;
}

module.exports = letterCounter;
