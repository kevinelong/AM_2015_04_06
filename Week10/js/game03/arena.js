function Arena(area) {
    Game.call(this, area);
}
Arena.prototype = Object.create(Game.prototype);
Arena.prototype.gameLoop = function () {
    gameLoopParent = this == window ? gameLoopParent : this;
    requestAnimationFrame(gameLoopParent.gameLoop)
    gameLoopParent.detectCollisions();
};
Arena.prototype.isColliding = function (sprite1, sprite2) {
    var rect1 = sprite1.element.getBoundingClientRect();
    var rect2 = sprite2.element.getBoundingClientRect();

    var dx, dy, r1 = {}, r2 = {};
    r1.cx = rect1.left + (r1.hw = (rect1.width / 2));
    r1.cy = rect1.top + (r1.hh = (rect1.height / 2));
    r2.cx = rect2.left + (r2.hw = (rect2.width / 2));
    r2.cy = rect2.top + (r2.hh = (rect2.height / 2));

    dx = Math.abs(r1.cx - r2.cx) - (r1.hw + r2.hw);
    dy = Math.abs(r1.cy - r2.cy) - (r1.hh + r2.hh);

    return (dx < 0 && dy < 0);
};


Arena.prototype.detectCollisions = function () {
    //Loop through all sprites
    for (var i = 0; i < this.sprites.length; i++) {
        var sprite1 = this.sprites[i];
        //Loop through remaining sprites
        for (var c = i + 1; c < this.sprites.length; c++) {
            var sprite2 = this.sprites[c];
            if (this.isColliding(sprite1, sprite2)) {
                sprite1.collided(sprite2);
                sprite2.collided(sprite1);
            }
        }

    }
};
