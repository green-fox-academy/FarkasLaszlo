
      var pictures = [
        { name: "asian_tiger.jpg",
          title: "Ghost tiger",
          description: "It's made of air, so it won't bite."
        }, 
        { name: "sky.jpg",
          title: "Sky",
          description: "A nice view through clouds."
        }, 
        { name: "sunset.jpg",
          title: "Sunset",
          description: "If everything is good, by this time workshop is done."
        }, 
        { name: "forest.jpg",
          title: "Forest",
          description: "If you are lost, well, it could be a dark forest, so be happy."
        },
        { name: "city.jpg",
          title: "Big City",
          description: "Looks great at night."
        },
        { name: "vulcano.jpg",
          title: "Vulcano",
          description: "It can be an extreme sport to live close to this."
        },
      ];
      var footer_list = document.querySelector("footer");
      for(var i =0;i < pictures.length;i++) {
        var new_div = document.createElement("div");
        var new_pic = document.createElement("button");
        var new_title = document.createElement("p");
        new_pic.setAttribute("style", "background-image: url(" + pictures[i].name + ");background-size: 55px 55px");
        new_pic.setAttribute("id", "img" + i);
        new_title.textContent = pictures[i].title;
        new_div.appendChild(new_title);
        new_div.appendChild(new_pic);
        footer_list.appendChild(new_div);
      }

      var left_shift = document.querySelector(".left");
      left_shift.addEventListener('click', shift_left);
      function shift_left() {
        var img = document.querySelector("main > img").getAttribute("src");
        for(var i = 0; i < pictures.length;i++) {
          if(img == pictures[i].name && i != 0) {
            document.querySelector("main > img").setAttribute("src", pictures[i - 1].name);
            document.querySelector("main > h1").textContent = pictures[i - 1].title;
            document.querySelector("main > p").textContent = pictures[i - 1].description;
          }else if(img == pictures[i].name && i == 0){
            document.querySelector("main > img").setAttribute("src", pictures[pictures.length-1].name);
            document.querySelector("main > h1").textContent = pictures[pictures.length-1].title;
            document.querySelector("main > p").textContent = pictures[pictures.length-1].description;
          }
        }
      }

      var right_shift = document.querySelector(".right");
      function shift_right() {
        var img = document.querySelector("main > img").getAttribute("src");
        for(var i = 0; i < pictures.length;i++) {
          if(img == pictures[i].name && i != pictures.length -1 ) {
            document.querySelector("main > img").setAttribute("src", pictures[i + 1].name);
            document.querySelector("main > h1").textContent = pictures[i + 1].title;
            document.querySelector("main > p").textContent = pictures[i + 1].description;
          }else if(img == pictures[i].name && i == pictures.length -1){
            document.querySelector("main > img").setAttribute("src", pictures[0].name);
            document.querySelector("main > h1").textContent = pictures[0].title;
            document.querySelector("main > p").textContent = pictures[0].description;
          }
        }
      }
      right_shift.addEventListener('click', shift_right);
      

      function GetActive () {
        var img_list = document.querySelectorAll("footer > div > button");
        for(var i = 0; i < pictures.length;i++) {
          if (document.activeElement.id == img_list[i].id) {
            document.querySelector("main > img").setAttribute("src", pictures[i].name);
            document.querySelector("main > h1").textContent = pictures[i].title;
            document.querySelector("main > p").textContent = pictures[i].description;
          }
        }
      }