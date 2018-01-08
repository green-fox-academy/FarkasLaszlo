'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

var maxlength = 0;
if(girls.length >= boys.length) {
  maxlength = girls.length;
}else {
  maxlength = boys.length;
}

for(var i = 0; i < maxlength;i++) {
  if(girls[i] != undefined) {
    order += girls[i] + " ";
  }
  if(boys[i] != undefined) {
    order += boys[i] + " ";
  }
}

console.log(order);