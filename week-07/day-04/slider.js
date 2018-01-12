

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
        { name: "CSSGRIDexplain.jpg",
          title: "3D GRID",
          description: "You can see, how easy grid can be."
        },
        { name: "Collision.jpg",
          title: "Collision",
          description: "Ruuunnnn!!!"
        },
        { name: "storm.jpg",
          title: "Storm",
          description: "Looks nice from distance."
        },
        { name: "winterfog.jpg",
          title: "Winter Fog",
          description: "Fog can be great when you are not in it."
        },
      ];
      var footer_list = document.querySelector("footer");
      for(var i =0;i < pictures.length;i++) {
        var new_div = document.createElement("div");
        var new_pic = document.createElement("button");
        var new_title = document.createElement("p");
        new_pic.setAttribute("style", "background-image: url(" + pictures[i].name + ");background-size: 55px 55px");
        new_pic.setAttribute("class", "img" + i);
        new_title.textContent = pictures[i].title;
        new_div.appendChild(new_title);
        new_div.appendChild(new_pic);
        footer_list.appendChild(new_div);
      }
      
      document.querySelector("footer > div > button").style.border = "3px solid white";

      function GetActive () {
        var img_list = document.querySelectorAll("footer > div > button");
        for(var i = 0; i < pictures.length;i++) {
          img_list[i].style.border = "6px solid white";
          if (document.activeElement.className == img_list[i].className) {
            document.querySelector("main > img").setAttribute("src", pictures[i].name);
            document.querySelector("main > img").setAttribute("class", "img" + i);
            document.querySelector("main > h1").textContent = pictures[i].title;
            document.querySelector("main > p").textContent = pictures[i].description;
            img_list[i].style.border = "3px solid white";
          }
        }
      }
  
  function replace_right() {
    var img = document.querySelector("main > img").getAttribute("src");
    for(var i = 0; i < pictures.length;i++) {
      if(img == pictures[i].name && i != pictures.length -1 ) {
        document.querySelector("main > img").setAttribute("src", pictures[i + 1].name);
        document.querySelector("main > img").setAttribute("class", "img" + Number(i+1));
        document.querySelector("main > h1").textContent = pictures[i + 1].title;
        document.querySelector("main > p").textContent = pictures[i + 1].description;
      }else if(img == pictures[i].name && i == pictures.length -1){
        document.querySelector("main > img").setAttribute("src", pictures[0].name);
        document.querySelector("main > img").setAttribute("class", "img" + 0);
        document.querySelector("main > h1").textContent = pictures[0].title;
        document.querySelector("main > p").textContent = pictures[0].description;
      }
    }
  }

  $(document).ready(function(){
    $(".right").click(function(){
        $("main").slideUp(0);
        $("main").slideDown(1000);
        replace_right();   
    });
});

function replace_left() {
  var img = document.querySelector("main > img").getAttribute("src");
  for(var i = 0; i < pictures.length;i++) {
    if(img == pictures[i].name && i != 0) {
      document.querySelector("main > img").setAttribute("src", pictures[i - 1].name);
      document.querySelector("main > img").setAttribute("class", "img" + Number(i-1));
      document.querySelector("main > h1").textContent = pictures[i - 1].title;
      document.querySelector("main > p").textContent = pictures[i - 1].description;
    }else if(img == pictures[i].name && i == 0){
      document.querySelector("main > img").setAttribute("src", pictures[pictures.length-1].name);
      document.querySelector("main > img").setAttribute("class", "img" + (pictures.length - 1));
      document.querySelector("main > h1").textContent = pictures[pictures.length-1].title;
      document.querySelector("main > p").textContent = pictures[pictures.length-1].description;
    }
  }

}

$(document).ready(function(){
  $(".left").click(function(){
      $("main").fadeOut(0);
      $("main").fadeIn(1000);
      replace_left();   
  });
});

$(document).ready(function(){
  $(".side").click(function(){
    var small_pic = document.querySelectorAll("footer > div > button");
    var big_pic = document.querySelector("main > img");
    for(var i =0; i < pictures.length;i++) {
      small_pic[i].style.border = "6px solid white";
      if(small_pic[i].className == big_pic.className) {
        small_pic[i].style.border = "3px solid white";

      }
    }
  });
});