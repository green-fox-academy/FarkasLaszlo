'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function count_candies(student_data) {
  var candy_count = 0;
  for(var i = 0; i < student_data.length;i++){
    candy_count += student_data[i].candies;
  }
  return candy_count;
}

console.log(count_candies(students));

function sum_age(student_data) {
  var age = 0;
  for(var i = 0; i < student_data.length;i++) {
    if(student_data[i].candies < 5) {
      age += student_data[i].age;
    }
  }
  return age;
}

console.log(sum_age(students));