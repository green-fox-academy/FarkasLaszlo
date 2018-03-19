'use strict';

const watchlist = [];
let security_alcohol_loot = 0;
const queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

// Queue of festivalgoers at entry
// no. of alcohol units 
// no. of guns

// Create a security_check function that returns a list of festivalgoers who can enter the festival

// If guns are found, remove them and put them on the watchlist (only the names)
// If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

function security_check(entry) {
  entry.map(person => {
    if(person.guns !== 0) {
      watchlist.push(person.name);
      person.guns = 0;
    }
    if (person.alcohol !== 0) {
      security_alcohol_loot += person.alcohol;
      person.alcohol = 0;
    }
  });
  
  console.log(`They are in the watchlist: ${watchlist}`);
  console.log(`This many alcohol has been confiscated: ${security_alcohol_loot}`);
  console.log(entry);

  const festivalgoers = [];
  entry.map(person => {
    festivalgoers.push(person.name);
  });
  return festivalgoers;
}

console.log(`They can enter the festival: ${security_check(queue)}`);