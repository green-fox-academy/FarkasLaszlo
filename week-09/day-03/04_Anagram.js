"use strict";

// Write a function, that takes two strings and returns a boolean value 
// based on if the two strings are Anagramms or not.
// Create a test for that.

function Anagram(string1, string2) {
  string1 = string1.toLocaleLowerCase().split('').sort().join('');
  string2 = string2.toLocaleLowerCase().split('').sort().join('');
  let ret;
  string1 === string2 ? ret = true : ret = false;
  return ret;
}

module.exports = Anagram;
