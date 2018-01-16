// Create an Animal constructor function
// Every animal has a hunger property, which is a number
// Every animal has a thirst property, which is a number
// When creating a new animal object these properties are created with the default 5 value
// Every animal can eat() which decreases their hunger by one
// Every animal can drink() which decreases their thirst by one
// Every animal can play() which increases both by one

function Animal() {
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function() {
    this.hunger -= 1;
  }
  this.drink = function() {
    this.thirst -= 1;
  }
  this.play = function() {
    this.hunger += 1;
    this.thirst += 1;
  }
}

// Create a Farm constructor function
// The farm has slots which defines the number of free places for animals
// The farm has list of Animals
// The farm can breed() which creates a new animal if there's place for it
// The farm can slaughter() which removes the least hungry animal
// The farm can print reports about their current state:
// The farm has 11 living animals we are bankrupt
// The farm can progress from day to a new day by calling it's progress() method:
// All animals should have their methods called randomly with 50% chance
// The farm should call its breed and slaughter method at the end of each day
// The farm should print report at the end of each day
// Print the number of sheeps
// Print "bankrupt" if no animals left
// Print "okay" if the number of animals is above zero and under the slot number
// Print "full" if the number of animals are at the maximum allowed

function getRandomInt() {
  return Math.floor(Math.random() * (2 - 1 + 1)) + 1;
}

function Farm(slots) {
  this.slots = slots;
  this.animals = [];
  this.breed = function() {
    if(this.slots > 0) {
      this.animals.push(new Animal());
      this.slots -= 1;
    }
  }
  this.slaughter = function() {
    var least_hungry = 0;
    for(var i = 0; i< this.animals.length;i++) {
      if(this.animals[i].hunger < this.animals[least_hungry].hunger) {
        least_hungry = i;
      }
    }
    this.animals.splice(least_hungry,1);
    this.slots += 1;
  }
  this.progress = function() {
    for(var i = 0; i< this.animals.length;i++) {
      if(getRandomInt() == 2) {
        this.animals[i].eat();
      }
      if(getRandomInt() == 2) {
        this.animals[i].drink();
      }
      if(getRandomInt() == 2) {
        this.animals[i].play();
      }
    }
    this.breed();
    this.slaughter();
    console.log("The farm has" + this.animals.length + "animals.");
    if(this.animals.length == 0) {
      console.log("We are bankrupt.");
    }else if(this.animals.length > 0 && this.slots != 0) {
      console.log("We are okay");
    }else if(this.slots == 0) {
      console.log("We are full");
    }
  }
}

var sheepfarm = new Farm(20);
for(var i = 0;i < 20;i++) {
  sheepfarm.breed();
}

function click_event() {
  sheepfarm.progress();
}