'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function candy_counter(student_data) {
  var student_list = [];
  for( var i = 0; i < student_data.length;i++) {
    if(student_data[i].candies > 4) {
      student_list += student_data[i].name;
    }
  }
  return student_list;
}

console.log(candy_counter(students));

function get_average(student_data) {
  var average_candy = 0;
  for(var i = 0; i < student_data.length;i++) {
    average_candy += student_data[i].candies;
  }
  average_candy /= student_data.length;
  return average_candy;
}

console.log(get_average(students));