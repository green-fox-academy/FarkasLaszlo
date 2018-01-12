'use strict';
// Create a simple calculator application which does read the parameters from the standard input 
// and prints the result to the console.

// It should support the following operations: 
// +, -, *, /, % and it should support two operands. 

// The format of the expressions must be: {operation} {operand} {operand}. 
// Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

// You should use the command line arguments to accept user input

// It should work like this:

// Start the program with "node calculator.js + 5 6"
// If number of arguments are not correct, print some nice errors
// Else print the result
// Say goodbye
var command = [];

process.stdin.on('readable', function() {
  var sum;
  var d = process.stdin.read();
  if(d) {
    command = d.split(" ");
    }
  if(command[0] == "+") {
    sum = Number(command[1]) + Number(command[2]);
    console.log(sum);
  }else if(command[0] == "-") {
    sum = Number(command[1]) - Number(command[2]);
    console.log(sum);
  }else if(command[0] == "*") {
    sum = Number(command[1]) * Number(command[2]);
    console.log(sum);
  }else if(command[0] == "/") {
    sum = Number(command[1]) / Number(command[2]);
    console.log(sum);
  }else if(command[0] == "%") {
    sum = Number(command[1]) % Number(command[2]);
    console.log(sum);
  }
  if(sum != undefined){
  throw new Error("Goodbye!");
}
}
)

process.stdin.setEncoding("utf8");

console.log(command);