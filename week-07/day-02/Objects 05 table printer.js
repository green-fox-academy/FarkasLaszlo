'use strict';
// Create a function that prints the ingredient list of dictionaries to the console in the following format:
//
// +--------------------+---------------+----------+
// | Ingredient         | Needs cooling | In stock |
// +--------------------+---------------+----------+
// | vodka              | Yes           | 1        |
// | coffee_liqueur     | Yes           | -        |
// | fresh_cream        | Yes           | 1        |
// | captain_morgan_rum | Yes           | 2        |
// | mint_leaves        | No            | -        |
// +--------------------+---------------+----------+
//
// OPTIONAL
// The frist columns should be automatically as wide as the longest key

const ingredients = [
  { 'name': 'vodka', 'in_stock': 1, 'needs_cooling': true },
  { 'name': 'coffee_liqueur', 'in_stock': 0, 'needs_cooling': true },
  { 'name': 'fresh_cream', 'in_stock': 1, 'needs_cooling': true },
  { 'name': 'captain_morgan_rum', 'in_stock': 2, 'needs_cooling': true },
  { 'name': 'mint_leaves', 'in_stock': 0, 'needs_cooling': false },
  { 'name': 'sugar', 'in_stock': 0, 'needs_cooling': false },
  { 'name': 'lime juice', 'in_stock': 0, 'needs_cooling': true },
  { 'name': 'soda', 'in_stock': 0, 'needs_cooling': true },
  { 'name': 'something with very long name', 'in_stock': 0, 'needs_cooling': true }
]

function drawBorder(first, second, third) {
  console.log(`+${'-'.repeat(first.length + 2)}+${'-'.repeat(second)}+${'-'.repeat(third)}+`);
}

function box(ingredients) {
  let first_length = [];
  const second_length = ' Needs cooling '.length;
  const third_length = ' In stock '.length;
  const stock = [];
  const cool_list = [];
  ingredients.map(ingredient => {
    first_length.length < ingredient.name.length ? first_length = ingredient.name : null;
    ingredient.needs_cooling === true ? cool_list.push('Yes') : cool_list.push('No');
    ingredient.in_stock === 0 ? stock.push('-') : stock.push(ingredient.in_stock);
  });

  drawBorder(first_length, second_length, third_length);
  console.log(`| Ingredient${' '.repeat(first_length.length - 'Ingredient '.length + 2)}| Needs cooling | In stock |`);
  drawBorder(first_length, second_length, third_length);
  ingredients.map((ingredient, index) => {
    console.log(`| ${ingredient.name}${' '.repeat(first_length.length - ingredient.name.length + 1)}| ${cool_list[index]}${' '.repeat(second_length - 1 - cool_list[index].length)}| ${stock[index]}${' '.repeat(third_length - 2)}|`);
  });
  drawBorder(first_length, second_length, third_length);
}

box(ingredients);
