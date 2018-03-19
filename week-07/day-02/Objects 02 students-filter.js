'use strict';

const students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function candy_counter(student_array) {
  const student_list = [];
  student_array.map(student => {
    student.candies > 4 ? student_list.push(student.name) : null;
  });
  return student_list;
}

console.log(candy_counter(students));

function get_average(student_array) {
  let average_candy = 0;
  student_array.map(student => {
    average_candy += student.candies;
  });
  average_candy /= student_array.length;
  return average_candy;
}

console.log(get_average(students));