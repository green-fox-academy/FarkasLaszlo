"use strict";

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// app.use(function (req, res, next) {
//   console.log('middleware');
//   next();
// });

let urlencoded = bodyParser.urlencoded({extended: false });

app.use(bodyParser.json());

app.use('/assets', express.static('assets'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  console.log(req.query);
  if(req.query.input != undefined) {
      res.json({
      received: req.query.input,
      result: req.query.input * 2,
    });
  } else {res.json({
    error: "Please provide an input!",
  });
  }
});

app.get('/greeter', function (req, res) {
  if(req.query.name != undefined && req.query.title != undefined) {
      res.json({
      welcome_message: "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!",
    });
  } else if (req.query.name == undefined && req.query.title != undefined) {res.json({
    error: "Please provide a name!",
  });
  } else if (req.query.name != undefined && req.query.title == undefined) {res.json({
    error: "Please provide a title!",
  });
}
});

app.get('/appenda/:name', function (req, res) {
   if(req.params.name != undefined) {
     res.json({appended: req.params.name + "a"})
   };
});

app.post('/dountil/:name', urlencoded, function (req, res) {
  console.log(req.params.name);
  console.log(req.body.until);
  if (req.body.until != undefined) {
    let processedNumber = 0;
    if (req.params.name == "sum") {
      processedNumber = sum(req.body.until);
      res.json({result: processedNumber});
    } else if (req.params.name == "factor") {
      processedNumber = factor(req.body.until);
      res.json({ result: processedNumber });
    }
  } else {
    res.json({ error: "Please provide a number!" });
  }
});

function sum(number) {
  if (number > 1) {
    return number + sum(number - 1);
  } else {
    return 1;
  }
}

function factor(number) {
  if (number > 1) {
    return number * sum(number - 1);
  } else {
    return 1;
  }
}

app.post('/arrays', urlencoded, function (req, res) {
  if(req.body.what == "sum") {
    let resultNumbers = 0;
    req.body.numbers.map(function(i) {
      resultNumbers += i;
    });
    res.json({ result: resultNumbers });
  } else if(req.body.what == "multiply") {
    let resultNumbers = 1;
    req.body.numbers.map(function(i) {
      resultNumbers *= i;
    });
    res.json({ result: resultNumbers });
  } else if(req.body.what == "double") {
    let resultNumbers = [];
    req.body.numbers.map( function (item, index) {
      resultNumbers[index] = item * 2;
    });
    res.json({ result: resultNumbers });
  } else if(req.body.what == undefined) {
    res.json({ error: "Please provide what to do with the numbers!" });
  }
});

const translate = function (hungarian) {
  if( typeof hungarian != "string") {
    return 'Invalid value';
  }
  if (hungarian == '') {
    return '';
  } else if ("aeiouéáőűöüóí".includes(hungarian[0]) || "AEIOUÉÁŐŰÖÜÓÍ".includes(hungarian[0])) {
    if ("AEIOUÉÁŐŰÖÜÓÍ".includes(hungarian[0])) {
      return hungarian[0] + "v" + hungarian[0].toLocaleLowerCase() + translate(hungarian.substring(1));
    }
    return hungarian[0] + "v" + hungarian[0] + translate(hungarian.substring(1));
  }
  return hungarian[0] + translate(hungarian.substring(1));
};

app.post('/translate', urlencoded, function (req, res) {
  if(req.body.text != undefined && req.body.lang != undefined) {
    let translatedText = "";
    translatedText = translate(req.body.text);
    res.json({ 
      translated: translatedText,
      lang: "teve" });
  } else if(req.body.text == undefined && req.body.lang != undefined) {
    res.json({ 
      error: "There is nothing to translate!"
       });
  } else {
    res.json({ 
      error: "I can't translate that!"
       });
  }
});

app.post('/sith', urlencoded, function (req, res) {
  if(req.body.text != undefined) {
    let translatedText = "";
    translatedText = translate(req.body.text);
    res.json({ 
      translated: translatedText,
    });
  } else if(req.body.text == undefined) {
    res.json({ 
      error: "Feed me some text you have to, padawan young you are. Hmmm."
       });
  }
});

app.listen(8080, function () {
  console.log('The app is running');
});
