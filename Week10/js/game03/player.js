function Player(symbol) {
    Sprite.call(this, symbol);
}
Player.prototype = Object.create(Sprite.prototype);
