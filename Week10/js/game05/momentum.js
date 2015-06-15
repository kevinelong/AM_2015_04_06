function Space(area) {
    HyperArena.call(this, area);
}
Space.prototype = Object.create(HyperArena.prototype);

Space.prototype.gameLoop = function () {
    gameLoopParent = this == window ? gameLoopParent : this;
    requestAnimationFrame(gameLoopParent.gameLoop)
    gameLoopParent.detectCollisions();
    gameLoopParent.handleMomentum();
    gameLoopParent.handleOffScreen();
};

Space.prototype.applyMomentum = function (sprite) {
    sprite.x += sprite.mx;
    sprite.y += sprite.my;
    sprite.updatePosition()
};

Space.prototype.handleMomentum = function () {
    //Loop through all sprites
    for (var i = 0; i < this.sprites.length; i++) {
        var sprite = this.sprites[i];
        this.applyMomentum(sprite);
    }
};
