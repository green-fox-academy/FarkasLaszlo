"use strict";

let TennisGame1 = function(player1Name, player2Name) {
  this.playerscore_1 = 0;
  this.playerscore_2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
  this.wonPoint = function(playerName) {playerName === "player1" ? this.playerscore_1 += 1 : this.playerscore_2 += 1;};
  this.getScore = function() {
    let score = "";
    this.playerscore_1 === this.playerscore_2 ? score = getEvenResults(this.playerscore_1) : 
    this.playerscore_1 >= 4 || this.playerscore_2 >= 4 ? score = getWinner(this.playerscore_1,this.playerscore_2) : 
    score = getNoWinner(this.playerscore_1,this.playerscore_2);
    return score;
  };
}

if (typeof window === "undefined") {module.exports = TennisGame1;}

function getEvenResults(player1score) {
  let scores = ["Love-All","Fifteen-All","Thirty-All","Deuce","Deuce"];
  return scores[player1score];
}

function getWinner(player1score, player2score) {
  let difference = player1score - player2score + 4;
  let scores = ["Win for player2","Win for player2","Win for player2","Advantage player2"," ","Advantage player1","Win for player1","Win for player1","Win for player1"];
  return scores[difference];
}

function getNoWinner(player1score, player2score) {
  return chooseScore(player1score) + "-" + chooseScore(player2score);

  function chooseScore(scores) {
    let scoretexts = ["Love","Fifteen","Thirty","Forty","Forty"];
    return scoretexts[scores];
  }
}