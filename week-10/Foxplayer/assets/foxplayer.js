let songlist = [];
let currentPlayList = 1;
const media = document.querySelector('audio');
let randomPlay = false;

loadAllPlaylist();

function selectCurrentData(currentSongTitle, currentId, target) {
  let title = document.querySelector(currentSongTitle);
  let songId = songlist[currentId].replace(/[^0-9]/g, '');
  changeCurrentMedia(num, title, target);
}

function lastTrack(target) {
  changeColor();
  const index = songlist.indexOf(target.className);
  index === 0 ?
    selectCurrentData(`songtitle.${songlist[songlist.length - 1]}`, songlist.length - 1, target) :
    selectCurrentData(`songtitle.${songlist[index - 1]}`, index - 1, target);
}

function nextTrack(target) {
  changeColor();
  const index = songlist.indexOf(target.className);
  if (randomPlay === false) {
    index === (songlist.length - 1) ?
      selectCurrentData(`songtitle.${songlist[0]}`, 0, target) :
      selectCurrentData(`songtitle.${songlist[index + 1]}`, index + 1, target);
  } else {
    const randNumber = getRandomInt(0, songlist.length - 1);
    selectCurrentData(`songtitle.${songlist[randNumber]}`, randNumber, target);
  }
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * ((max - min) + 1)) + min;
}

function changeColor() {
  const currentdata = document.querySelector('currentdata');
  const currentclass = currentdata.className;
  const mysong = document.querySelector(`songs.${currentclass}`);
  if (currentclass !== undefined && songlist.indexOf(currentclass) % 2 === 0) {
    mysong.style.backgroundColor = 'rgb(200,200,200)';
  } else if (currentclass !== undefined && songlist.indexOf(currentclass) % 2 === 1) {
    mysong.style.backgroundColor = 'rgb(230,230,230)';
  }
}

function getCurrentData() {
  const currentData = document.querySelector('currentdata');
  const currentTitle = document.querySelector('currentdata > h3');
  const currentArtist = document.querySelector('currentdata > h5');
  return [currentData, currentTitle, currentArtist];
}

function changeCurrentMedia(num, title, target) {
  [currentData, currentTitle, currentArtist] = getCurrentData();
  const source = title.textContent.split('(');
  if (currentArtist.textContent !== source[1].substring(0, source[1].length - 1)) {
    getNewPicture(source[1].substring(0, source[1].length - 1));
    currentArtist.textContent = source[1].substring(0, source[1].length - 1);
  }
  source[0] = source[0].substring(0, source[0].length - 1);
  const filename = title.getAttribute('filename');
  media.setAttribute('class', `song${num}`);
  media.setAttribute('src', filename);
  currentTitle.textContent = source[0];
  currentData.setAttribute('class', target.className);
  const mysong = document.querySelector(`songs.${currentData.className}`);
  mysong.style.backgroundColor = 'deepskyblue';
}

function addPlaylist() {
  const tablename = window.prompt('Give a name to the playlist');
  if (tablename.includes('Playlists') || tablename.includes('playlists')) {
    alert("You can't create this table, it's already created");
    throw new Error("You can't create this table, it's already created");
  }
  const playListAdd = new XMLHttpRequest();
  playListAdd.open('POST', '/Playlist');
  playListAdd.setRequestHeader('Content-Type', 'application/json');
  playListAdd.onreadystatechange = () => {
    if (playListAdd.readyState === playListAdd.DONE) {
      const playlists = JSON.parse(playListAdd.responseText);
      createPlaylist(playlists);
    }
  };
  playListAdd.send(JSON.stringify({ name: tablename }));
}

function loadAllPlaylist() {
  addClickToAudio();
  addKeyPressEvent();
  addClickToLogo();
  addClickToSongAdderButtons();
  const loadPlaylists = new XMLHttpRequest();
  loadPlaylists.open('GET', '/playlists');
  loadPlaylists.setRequestHeader('Accept', 'application/json');
  loadPlaylists.onreadystatechange = () => {
    if (loadPlaylists.readyState === loadPlaylists.DONE) {
      const playlists = JSON.parse(loadPlaylists.responseText);
      createPlaylist(playlists);
    }
  };
  loadPlaylists.send();
}

function addClickToLogo() {
  const logotext = document.querySelector('logo > p');
  logotext.addEventListener('click', addPlaylist);
}

function createPlaylist(data) {
  $('main').empty();
  const main = document.querySelector('main');
  data.map((list) => {
    if (i === 0) {
      const logo = document.querySelector('logo > img');
      logo.setAttribute('class', `list${list.id}`);
    }
    const playlist = document.createElement('div');
    const listname = document.createElement('p');
    playlist.setAttribute('class', `list${list.id}`);
    listname.setAttribute('class', `list${list.id}`);
    listname.textContent = list.name;
    playlist.appendChild(listname);
    if (i > 1) {
      const deleteList = document.createElement('p');
      deleteList.setAttribute('class', `list${list.id}`);
      deleteList.textContent = 'x';
      playlist.appendChild(deleteList);
    }
    main.appendChild(playlist);
  });
  addClickToList();
  addClickToDelete();
}

function addClickToList() {
  $(() => {
    $('main > div').bind('click', displayList);
  });
  const logo = document.querySelector('logo > img');
  logo.addEventListener('click', displayList);
}

function displayList(e) {
  $('article').empty();
  const oldlist = document.querySelector(`div.list${currentPlayList}`);
  currentPlayList % 2 === 0 ? oldlist.style.backgroundColor = 'rgb(230,230,230)' : oldlist.style.backgroundColor = 'rgb(200,200,200)';
  currentPlayList = e.target.className.replace(/[^0-9]/g, '');
  const num = e.target.className.replace(/[^0-9]/g, '');
  const mydiv = document.querySelector(`main > div.${e.target.className}`);
  mydiv.style.backgroundColor = 'deepskyblue';
  const playListRequest = new XMLHttpRequest();
  playListRequest.open('GET', `/${num}`);
  playListRequest.setRequestHeader('Accept', 'application/json');
  playListRequest.onreadystatechange = () => {
    if (playListRequest.readyState === playListRequest.DONE) {
      const playlist = JSON.parse(playListRequest.responseText);
      createSongs(playlist);
    }
  };
  playListRequest.send();
}

function addClickToDelete() {
  $('main > div > p:nth-child(2)').bind('click', (e) => {
    const main = document.querySelector('main');
    const list = document.querySelector(`main > .${e.target.className}`);
    main.removeChild(list);
    const num = e.target.className.replace(/[^0-9]/g, '');
    const deleteListElement = new XMLHttpRequest();
    deleteListElement.open('DELETE', `/Playlist/:${num}`);
    deleteListElement.setRequestHeader('Accept', 'application/json');
    deleteListElement.send();
  });
}

function createSongs(data) {
  songlist = [];
  $('article').empty();
  if (data !== undefined) {
    const article = document.querySelector('article');
    data.map((song) => {
      songlist.push(`song${song.id}`);
      const place = createPlace(song);
      const songtitle = createSongTitle(song);
      const time = createTime(song);
      const songs = createMusic(song);
      songs.appendChild(place);
      songs.appendChild(songtitle);
      songs.appendChild(time);
      article.appendChild(songs);
    });
    addClickToSongs();
  }
}

function createPlace(data) {
  const place = document.createElement('place');
  place.setAttribute('class', `song${data.id}`);
  place.textContent = data.id;
  return place;
}

function createSongTitle(data) {
  const songtitle = document.createElement('songtitle');
  songtitle.setAttribute('class', `song${data.id}`);
  songtitle.innerHTML = `${data.title} <span class='song${data.id}'>(${data.artist})</span>`;
  songtitle.setAttribute('filename', data.filename);
  return songtitle;
}

function createTime(data) {
  const time = document.createElement('p');
  time.setAttribute('class', `song${data.id}`);
  time.textContent = countDuration(data.duration);
  return time;
}

function createMusic(data) {
  const songs = document.createElement('songs');
  songs.setAttribute('class', `song${data.id}`);
  return songs;
}

function addClickToSongs() {
  $('article > songs').bind('click', (e) => {
    [currentData, currentTitle, currentArtist] = getCurrentData();
    const myclass = currentdata.className;
    if (myclass !== undefined && songlist.indexOf(myclass) % 2 === 0) {
      const mysong = document.querySelector(`songs.${myclass}`);
      mysong.style.backgroundColor = 'rgb(200,200,200)';
    } else if (myclass !== undefined && songlist.indexOf(myclass) % 2 === 1) {
      const mysong = document.querySelector(`songs.${myclass}`);
      mysong.style.backgroundColor = 'rgb(230,230,230)';
    }
    const title = document.querySelector(`songtitle.${e.target.className}`);
    const source = title.textContent.split('(');
    if (currentArtist.textContent !== source[1].substring(0, source[1].length - 1)) {
      getNewPicture(source[1].substring(0, source[1].length - 1));
      currentArtist.textContent = source[1].substring(0, source[1].length - 1);
    }
    source[0] = source[0].substring(0, source[0].length - 1);
    const num = e.target.className.replace(/[^0-9]/g, '');
    media.setAttribute('class', `song${num}`);
    const filename = title.getAttribute('filename');
    media.setAttribute('src', filename);
    media.autoplay = true;
    currentTitle.textContent = source[0];
    currentData.setAttribute('class', e.target.className);
    const mysong = document.querySelector(`songs.${currentData.className}`);
    mysong.style.backgroundColor = 'deepskyblue';
  });
}

function countDuration(duration) {
  let time = 0;
  for (let i = 60; i < duration; duration -= 60) {
    time += 1;
  }
  return `${time}:${duration}`;
}

function addSongToList() {
  const addSongToPlayList = new XMLHttpRequest();
  addSongToPlayList.open('PUT', `/addtoplaylist/${currentPlayList}&${media.className.replace(/[^0-9]/g, '')}`);
  addSongToPlayList.setRequestHeader('Accept', 'application/json');
  addSongToPlayList.onreadystatechange = () => {
    if (addSongToPlayList.readyState === addSongToPlayList.DONE) {
      const playlist = JSON.parse(addSongToPlayList.responseText);
      createSongs(playlist);
    }
  };
  addSongToPlayList.send();
}

function addSongToFav() {
  const addSongToFavourite = new XMLHttpRequest();
  addSongToFavourite.open('PUT', `/addfavourite/${media.className.replace(/[^0-9]/g, '')}`);
  addSongToFavourite.setRequestHeader('Accept', 'application/json');
  addSongToFavourite.send();
}

function addKeyPressEvent() {
  $(document).keypress((e) => {
    if (e.keyCode === 32 && media.paused) {
      e.preventDefault();
      media.play();
    } else if (e.keyCode === 32 && media.paused !== true) {
      e.preventDefault();
      media.pause();
    } else if (e.keyCode === 80 || e.keyCode === 112) {
      lastTrack(media);
    } else if (e.keyCode === 78 || e.keyCode === 110) {
      nextTrack(media);
    }
  });
  
  $(document).on('keydown', (happening) => {
    const e = happening || window.event;
    if ((e.which === 38 || e.keyCode === 38) && media.volume < 0.95) {
      e.preventDefault();
      media.volume += 0.05;
    } else if ((e.which === 40 || e.keyCode === 40) && media.volume > 0.05) {
      e.preventDefault();
      media.volume -= 0.05;
    } else if ((e.which === 37 || e.keyCode === 37) && media.currentTime > media.duration * 0.05) {
      media.currentTime -= media.duration * 0.05;
    } else if ((e.which === 39 || e.keyCode === 39) && media.currentTime < media.duration * 0.95) {
      media.currentTime += media.duration * 0.05;
    }
  });
}

function addClickToSongAdderButtons() {
  const songToFav = document.querySelector('currentdata > img');
  const songToList = document.querySelector('currentdata > p');
  songToFav.addEventListener('click', addSongToFav);
  songToList.addEventListener('click', addSongToList);
}

function addClickToAudio() {
  const shuffle = document.querySelector('.shuffle');
  const forward = document.querySelector('.forward');
  const rewind = document.querySelector('.rewind');

  shuffle.addEventListener('click', () => {
    if (randomPlay === false) {
      randomPlay = true;
      shuffle.style.backgroundColor = 'deepskyblue';
    } else {
      randomPlay = false;
      shuffle.style.backgroundColor = 'rgb(230,230,230)';
    }
  });
  
  media.addEventListener('keydown', (e) => {
    if (e.keyCode === 27 && media.muted) {
      media.muted = false;
    } else if (e.keyCode === 27 && media.muted !== true) {
      media.muted = true;
    }
  });
  
  media.addEventListener('ended', (e) => {
    nextTrack(media, e);
  });
  
  forward.addEventListener('click', (e) => {
    nextTrack(media, e);
  });
  
  rewind.addEventListener('click', (e) => {
    lastTrack(media, e);
  });
}

function getNewPicture(authordata) {
  const imagedata = new XMLHttpRequest();
  imagedata.open('GET', `http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=${authordata}&api_key=ee125f318852fc7d1c2f4e21458a0035&format=json`);
  imagedata.onreadystatechange = () => {
    if (imagedata.readyState === imagedata.DONE) {
      const artistData = JSON.parse(imagedata.responseText);
      const img = document.querySelector('logo > img.placeholder');
      if (artistData.artist !== undefined) {
        img.setAttribute('src', artistData.artist.image[3]['#text']);
      } else {
        img.setAttribute('src', 'assets/galaxy.jpg');
      }
    }
  };
  imagedata.send();
}
