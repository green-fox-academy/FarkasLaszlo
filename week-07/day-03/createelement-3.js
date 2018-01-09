const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]
  var ul_list = document.querySelector("ul.asteroids");
  ul_list.removeChild(document.querySelector("li"));
  for(var i = 0; i < planetData.length;i++) {
    if(planetData[i].asteroid == true) {
    var new_li = document.createElement("li");
    new_li.classList.add(planetData[i].category);
    new_li.textContent = planetData[i].content;
    ul_list.appendChild(new_li);
    }
  }