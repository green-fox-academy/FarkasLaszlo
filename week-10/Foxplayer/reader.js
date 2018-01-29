    var fs = require('fs');
    var files = fs.readdirSync('assets/');
    console.log(files);

    //get data for every mp3 and insert rows into the database;