"use strict";

let TennisGame3 = function(player1Name, player2Name) {
  this.score2 = 0;
  this.score1 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
  this.getScore = function() {
    let score;
    let texts = ["Love", "Fifteen", "Thirty", "Forty"];
    if ((this.score1 < 4 && this.score2 < 4) && (this.score1 + this.score2 < 6)) 
    {return (this.score1 == this.score2) ? texts[this.score1] + "-All" : texts[this.score1] + "-" + texts[this.score2];}
    else if (this.score1 == this.score2){return "Deuce";}
    score = this.score1 > this.score2 ? this.player1Name : this.player2Name;
    return ((this.score1 - this.score2) * (this.score1 - this.score2) == 1) ? "Advantage " + score : "Win for " + score;
  };
  this.wonPoint = function(playerName) {
    playerName == "player1" ? this.score1 += 1 : this.score2 += 1;
  };
};

if (typeof window === "undefined") {
  module.exports = TennisGame3;
}