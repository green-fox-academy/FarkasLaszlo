'use strict';

class ElevatorController {
  constructor() {
    this.elevator = new ElevatorModel(20,10);
    this.view = new ElevatorView(this.elevator.maximum_floor);
    this.view.draw();
    this.buttonup = document.querySelector(".up");
    this.buttondown = document.querySelector(".down");
    this.buttonadd = document.querySelector(".add");
    this.buttonremove = document.querySelector(".remove");
    var addp = this.elevator.remove_people.bind(this.elevator);
    var removep = this.elevator.add_people.bind(this.elevator);
    var moveupp = this.elevator.moveup.bind(this.elevator);
    var movedownn = this.elevator.movedown.bind(this.elevator);
    this.buttondown.addEventListener("click", movedownn);
    this.buttonup.addEventListener("click", moveupp);
    this.buttonremove.addEventListener("click", addp);
    this.buttonadd.addEventListener("click", removep);
    document.querySelector(".elevator > div:last-child").style.backgroundColor = "green";
  }


}

class ElevatorModel {
  constructor(maximum_floor, maximum_people) {
    this.maximum_floor = maximum_floor;
    this.maximum_people = maximum_people;
    this.elevator_position = maximum_floor - 1;
    this.people = 0;
  }

  remove_people() {
    if(this.people > 0) {
      this.people -= 1;
    }
    var levelnumbers = document.querySelectorAll(".elevator > div > p");
    for(var i = 0; i < levelnumbers.length; i++) {
      levelnumbers[i].textContent = "" + this.people;
    }
  }    
  
  add_people() {
    if(this.people < this.maximum_people) {
      this.people += 1;
    }
    var levelnumbers = document.querySelectorAll(".elevator > div > p");
    for(var i = 0; i < levelnumbers.length; i++) {
      levelnumbers[i].textContent = String(this.people);
    }
  }

  moveup() {
    var levels = document.querySelectorAll(".elevator > div");
    if(this.elevator_position < this.maximum_floor - 1) {
      this.elevator_position += 1;
    }
    for(var i = 0; i< levels.length;i++) {
      levels[i].style.backgroundColor = "white";
      if(i == this.elevator_position) {
        levels[i].style.backgroundColor = "green";
      }
    }
  }
  movedown() {
    var levels = document.querySelectorAll(".elevator > div");
    if(this.elevator_position >= 1) {
      this.elevator_position -= 1;
    }
    for(var i = 0; i< levels.length;i++) {
      levels[i].style.backgroundColor = "white";
      if(i == this.elevator_position) {
        levels[i].style.backgroundColor = "green";
      }
    }
  }

}

class ElevatorView {
  constructor(max_floor) {
    this.max_floor = max_floor;
    this.elevatora = document.querySelector(".elevator");
  }

  draw() {
    for(var i = 0; i < this.max_floor;i++) {
      var floor = document.createElement("div");
      floor.setAttribute("class","level" + (this.max_floor -i));
      var par = document.createElement("p");
      par.setAttribute("class","level" + (this.max_floor -i));
      par.textContent = 0;
      floor.appendChild(par);
      this.elevatora.appendChild(floor);
    }
  }
}


var controller = new ElevatorController;