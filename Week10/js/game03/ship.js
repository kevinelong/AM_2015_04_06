function Ship(symbol) {
    Player.call(this, symbol);
    this.element.style.border = "1px solid black"
}
Ship.prototype = Object.create(Player.prototype);
Ship.prototype.collided = function (otherSprite) {
    this.element.style.backgroundColor = "red";
    console.log(
        this.element.innerHTML +
        " collided with " +
        otherSprite.element.innerHTML);
};