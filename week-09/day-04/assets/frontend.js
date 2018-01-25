/**
 * Created by aze on 2017.05.09..
 */
window.baseUrl = "http://localhost:8080";
$("#server_change").on("submit", function (e) {
    e.preventDefault();
    window.baseUrl = $("#server_address").val();
    console.log(window.baseUrl);
});
handle = function handle (id, info, where, data) {
    if(data) {
        console.log(where +" "+ info);
        console.log(data);
    }
    $(id).append("<li>" + info + (data ? " - check the console for the response " : "")+"</li>");
}
$("#doubling").on("click", function () {
    $.get(window.baseUrl + "/doubling", {}).done(function (data) {
       if("error" in data && data["error"] == "Please provide an input!") {
           handle("#doubling_response", "OK - without data");
       } else {
           handle("#doubling_response", "not ok - without data", "Doubling", data);
       }
    }).error(function (err) {
        handle("#doubling_response", "not ok - without data", "Doubling", err);
    });
    $.get(window.baseUrl + "/doubling", {input: 5}).done(function (data) {
        if("received" in data && "result" in data && data["received"] == 5 && data["result"] == 10) {
            handle("#doubling_response", "OK - with input=5");
        } else {
            handle("#doubling_response", "not ok - with input=5", "Doubling", data);
        }
    }).error(function (err) {
        handle("#doubling_response", "not ok - with input=5", "Doubling", err);
    });
});

$("#greeter").on("click", function () {
    $.get(window.baseUrl + "/greeter", {}).done(function (data) {
        if("error" in data && data["error"] == "Please provide a name!") {
            handle("#greeter_response", "OK - without name");
        } else {
            handle("#greeter_response", "not ok - without name", "Greeter", data);
        }
    }).error(function (err) {
        handle("#greeter_response", "not ok - without name", "Greeter", err);
    });
    $.get(window.baseUrl + "/greeter", {name: "petike"}).done(function (data) {
        if("error" in data && data["error"] == "Please provide a title!") {
            handle("#greeter_response", "OK - without title");
        } else {
            handle("#greeter_response", "not ok - without title", "Greeter", data);
        }
    }).error(function (err) {
        handle("#greeter_response", "not ok - without title", "Greeter", err);
    });
    $.get(window.baseUrl + "/greeter", {name: "petike", title: "student"}).done(function (data) {
        if("welcome_message" in data && data["welcome_message"] == "Oh, hi there petike, my dear student!") {
            handle("#greeter_response", "OK - with petike and student");
        } else {
            handle("#greeter_response", "not ok - with petike and student", "Greeter", data);
        }
    }).error(function (err) {
        handle("#greeter_response", "not ok - with petike and student", "Greeter", err);
    });
});

$("#appenda").on("click", function () {
    $.get(window.baseUrl + "/appenda", {}).done(function (data) {
        handle("#appenda_response", "not ok - without appendable", "Appenda", data);
    }).error(function (err) {
        handle("#appenda_response", "OK - without appendable");
    });
    $.get(window.baseUrl + "/appenda/kuty", {}).done(function (data) {
        if("appended" in data && data["appended"] == "kutya") {
            handle("#appenda_response", "OK - with /kuty");
        } else {
            handle("#appenda_response", "not ok - with /kuty", "Appenda", data);
        }
    }).error(function (err) {
        handle("#appenda_response", "not ok - with /kuty", "Appenda", err);
    });
});

$("#dountil").on("click", function () {
    $.post({url: window.baseUrl + "/dountil/sum", data: JSON.stringify({until: 7}), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("result" in data && data["result"] == 28) {
            handle("#dountil_response", "OK - with /sum until=7");
        } else {
            handle("#dountil_response", "not ok - with /sum until=7", "Dountil", data);
        }
    }).error(function (err) {
        handle("#dountil_response", "not ok - with /sum until=7", "Dountil", err);
    });
    $.post({url: window.baseUrl + "/dountil/factor", data: JSON.stringify({until: 4}), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("result" in data && data["result"] == 24) {
            handle("#dountil_response", "OK - with /factor until=4");
        } else {
            handle("#dountil_response", "not ok - with /factor until=4", "Dountil", data);
        }
    }).error(function (err) {
        handle("#dountil_response", "not ok - with /factor until=4", "Dountil", err);
    });
});

$("#handlearray").on("click", function () {
    $.post({url: window.baseUrl + "/arrays", data: JSON.stringify({
        "what": "sum",
        "numbers": [1, 2, 5, 10]
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("result" in data && data["result"] == 18) {
            handle("#handlearray_response", "OK sum of 1,2,5,10 = 18");
        } else {
            handle("#handlearray_response", "not ok", "Handle", data);
        }
    }).error(function (err) {
        handle("#handlearray_response", "not ok", "Handle", err);
    });
    $.post({url: window.baseUrl + "/arrays", data: JSON.stringify({
        "what": "multiply",
        "numbers": [1, 2, 5, 10]
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("result" in data && data["result"] == 100) {
            handle("#handlearray_response", "OK multiply of 1,2,5,10 = 100");
        } else {
            handle("#handlearray_response", "not ok", "Handle", data);
        }
    }).error(function (err) {
        handle("#handlearray_response", "not ok", "Handle", err);
    });
    $.post({url: window.baseUrl + "/arrays", data: JSON.stringify({
        "what": "double",
        "numbers": [1, 2, 5, 10]
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("result" in data && JSON.stringify(data["result"]) === JSON.stringify([2, 4, 10, 20])) {
            handle("#handlearray_response", "OK double of [1,2,5,10] = [2,4,10,20]");
        } else {
            handle("#handlearray_response", "not ok", "Handle", data);
        }
    }).error(function (err) {
        handle("#handlearray_response", "not ok", "Handle", err);
    });
    $.post({url: window.baseUrl + "/arrays", data: JSON.stringify({
        "numbers": [1, 2, 5, 10]
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("error" in data && data["error"] === "Please provide what to do with the numbers!") {
            handle("#handlearray_response", "OK error is fine");
        } else {
            handle("#handlearray_response", "error not ok", "Handle", data);
        }
    }).error(function (err) {
        handle("#handlearray_response", "error not ok", "Handle", err);
    });
});

$("#tevenyelv").on("click", function () {
    $.post({url: window.baseUrl + "/translate", data: JSON.stringify({
        "text": "Ez egy példamondat. Remélem célbatalál.",
        "lang": "hu"
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("translated" in data && data["translated"] === "Evez evegy pévéldavamovondavat. Revemévélevem cévélbavatavalávál." && data["lang"] == "teve") {
            handle("#tevenyelv_response", "OK it works fine");
        } else {
            handle("#tevenyelv_response", "not okk", "Camel language", data);
        }
    }).error(function (err) {
        handle("#tevenyelv_response", "not ok", "Camel language", err);
    });
    $.post({url: window.baseUrl + "/translate", data: JSON.stringify({
        "text": "Ez egy példamondat. Remélem célbatalál."
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("error" in data && data["error"] == "I can't translate that!") {
            handle("#tevenyelv_response", "Error OK when no language to translate");
        } else {
            handle("#tevenyelv_response", "not ok", "Camel language", data);
        }
    }).error(function (err) {
        handle("#tevenyelv_response", "not ok", "Camel language", err);
    });
    $.post({url: window.baseUrl + "/translate", data: JSON.stringify({
        "lang": "hu"
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("error" in data && data["error"] == "There is nothing to translate!") {
            handle("#tevenyelv_response", "Error OK when there is no text to translate");
        } else {
            handle("#tevenyelv_response", "not ok", "Camel language", data);
        }
    }).error(function (err) {
        handle("#tevenyelv_response", "not ok", "Camel language", err);
    });
});

$("#sith").on("click", function () {
    $.post({url: window.baseUrl + "/sith", data: JSON.stringify({
        "text": "This is my example sentence. Just for fun."
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("sith_text" in data && data["sith_text"] === "Is this example my. Just fun for. ") {
            handle("#sith_response", "The force is with you!");
        } else {
            handle("#sith_response", "The force is not with you", "Sith language", data);
        }
    }).error(function (err) {
        console.log(data["sith_text"]);
        handle("#sith_response", "The force is not with you at all", "Sith language", err);
    });
    $.post({url: window.baseUrl + "/sith", data: JSON.stringify({
      }), contentType: 'application/json; charset=utf-8'}).done(function (data) {
        if("error" in data && data["error"] == "Feed me some text you have to, padawan young you are. Hmmm.") {
            handle("#sith_response", "The force is with you, even when you make error!");
        } else {
            handle("#sith_response", "Error is not good enough", "Sith language", data);
        }
    }).error(function (err) {
        handle("#sith_response", "Error is much worse", "Sith language", err);
    });
});