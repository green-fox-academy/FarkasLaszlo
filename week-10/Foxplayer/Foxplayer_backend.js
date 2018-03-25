const express = require('express');
const mysql = require('mysql');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, '/assets')));
app.use(express.static('E:/tracks'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '/assets/foxplayer.html'));
});

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'mymusic',
});

conn.connect((err) => {
  if (err) {
    throw new Error('Error connecting to Db');
  }
});

app.get('/playlists', (req, res) => {
  conn.query('SELECT * FROM Playlists ORDER BY id;', (err, result) => {
    if (err) {
      res.json({ error: 'Something wrong with the Playlists table' });
      return;
    }
    res.json(result);
  });
});

app.get('/:id', (req, res) => {
  const table = `SELECT * FROM Playlists WHERE id = ${req.params.id} ;`;
  conn.query(table, choosePlaylist);

  function choosePlaylist(err, results) {
    if (err) {
      throw err;
    }
    if (results[0] !== undefined && results[0].name === 'allsongs') {
      const sql = `SELECT * FROM ${results[0].name};`;
      sendDataBack(sql);
    } else if (results[0] !== undefined) {
      const sql = `SELECT * FROM ${results[0].name}  INNER JOIN allsongs ON ${results[0].name}.id = allsongs.id;`;
      sendDataBack(sql);
    }
  }

  function sendDataBack(sql) {
    conn.query(sql, (error, resultstext) => {
      if (error) {
        throw error;
      }
      res.json(resultstext);
    });
  }
});

app.delete('/Playlist/:id', (req) => {
  conn.query(`SELECT * FROM Playlists WHERE id = ${req.params.id.substring(1)};`, deleteTable);

  function deleteTable(err, result) {
    conn.query(`DROP TABLE ${result[0].name};`);
    conn.query(`DELETE FROM Playlists WHERE id = ${req.params.id.substring(1)};`);
  }
});

app.post('/Playlist', (req, res) => {
  conn.query('ALTER TABLE Playlists ADD UNIQUE (name)', insertIntoPlaylists);

  function insertIntoPlaylists(err) {
    if (err) {
      throw err;
    }
    conn.query(`INSERT IGNORE INTO Playlists (name) VALUES ("${req.body.name}")`, createTable);
  }

  function createTable(err) {
    if (err) {
      throw err;
    }
    conn.query(`CREATE TABLE IF NOT EXISTS ${req.body.name} (id VARCHAR(255));`, sendDataBack);
  }

  function sendDataBack(err) {
    if (err) {
      throw err;
    }
    conn.query('SELECT * FROM Playlists ORDER BY id', (error, result) => {
      if (error) {
        throw error;
      }
      res.json(result);
    });
  }
});

app.put('/addfavourite/:id', (req) => {
  conn.query('ALTER TABLE Favourites ADD UNIQUE (id)', insertIntoFav);

  function insertIntoFav(err) {
    if (err) {
      throw err;
    }
    conn.query(`INSERT IGNORE INTO Favourites (id) VALUES (${req.params.id});`, (error) => {
      if (error) {
        throw error;
      }
    });
  }
});

app.put('/addtoplaylist/:id', (req, res) => {
  const listAndSong = req.params.id.split('&');
  conn.query(`SELECT * FROM Playlists Where id = ${listAndSong[0]};`, (err, results) => {
    if (err) {
      throw err;
    }
    if (results[0].name !== 'Favourites') {
      addUnique(results);
    }
  });

  function addUnique(results) {
    conn.query(`ALTER TABLE ${results[0].name} ADD UNIQUE (id)`, (err) => {
      if (err) {
        throw err;
      }
    });
    insertIntoPlaylist(results);
  }

  function insertIntoPlaylist(results) {
    conn.query(`INSERT IGNORE INTO ${results[0].name} (id) VALUES ("${listAndSong[1]}");`, (err) => {
      if (err) {
        throw err;
      }
      sendDataBack(results);
    });
  }

  function sendDataBack(results) {
    conn.query(`SELECT * FROM ${results[0].name} INNER JOIN allsongs ON ${results[0].name}.id = allsongs.id`, (err, result) => {
      if (err) {
        throw err;
      }
      res.json(result);
    });
  }
});

app.listen(8080, () => {
  console.log('The app is running');
});
