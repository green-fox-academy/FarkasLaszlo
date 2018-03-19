'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ['Eve', 'Joe', 'Ashley', 'Fred'...]

const girls = ['Eve', 'Ashley', 'Bözsi', 'Kat', 'Jane'];
const boys = ['Joe', 'Fred', 'Béla', 'Todd', 'Neef', 'Jeff'];
let order = [];

let maxlength = 0;
girls.length >= boys.length ? maxlength = girls.length : maxlength = boys.length;


for(var i = 0; i < maxlength;i++) {
  if(girls[i] != undefined) {
    order.push(girls[i]);
  }
  if(boys[i] != undefined) {
    order.push(boys[i]);
  }
}

console.log(order);