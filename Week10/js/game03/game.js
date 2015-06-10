function Game(gameArea) {
    this.players = [];
    World.call(this, gameArea);
}
Game.prototype = Object.create(World.prototype);

Game.prototype.addPlayer = function (player) {
    this.players.push(player);
    this.addElement(player);
    this.currentElement = player;
    player.moveRandom();
};
