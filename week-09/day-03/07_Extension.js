'use strict';

// Adds a and b, returns as result
const addNumbers = function (a, b) {
  if ( typeof a != "number" || typeof b != "number") {
    throw new Error("Invalid value");
  }
  return a + b;
}

// Returns the highest value from the three given params
const maxOfThree = function (a, b, c) {
  if ( typeof a != "number" || typeof b != "number" || typeof c != "number") {
    throw new Error("Invalid value");
  }
  let highest;
  a > b && a > c ? highest = a : b > a && b > c ? highest = b : highest = c;
  return highest;
}

// Returns the median value of a list given as param

const median = function (pool) {
  let medianvalue = 0;
  pool.map(function mapper(i) {
    if (typeof i !== 'number') {
      throw new Error('Invalid value');
    }
    medianvalue += i;
    return medianvalue;
  });
  medianvalue /= pool.length;
  return medianvalue;
};

// Returns true if the param is a vovel
const isVovel = function (char) {
  if(char.length == 0 || char.length > 1) {
    return 'Please, give me one character';
  }
  if (char.length == 1) {
    if ('aeiouéáőűöüóí'.includes(char)) {
      return true;
    } else if ('AEIOUÉÁŐŰÖÜÓÍ'.includes(char)) {
      return true;
    }
    return false;
  }
};

// Create a method that translates hungarian into the teve language
const translate = function (hungarian) {
  if( typeof hungarian != "string") {
    return 'Invalid value';
  }
  if (hungarian == '') {
    return '';
  } else if ("aeiouéáőűöüóí".includes(hungarian[0]) || "AEIOUÉÁŐŰÖÜÓÍ".includes(hungarian[0])) {
    if ("AEIOUÉÁŐŰÖÜÓÍ".includes(hungarian[0])) {
      return hungarian[0] + "v" + hungarian[0].toLocaleLowerCase() + translate(hungarian.substring(1));
    }
    return hungarian[0] + "v" + hungarian[0] + translate(hungarian.substring(1));
  }
  return hungarian[0] + translate(hungarian.substring(1));
};

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}