function HyperArena(area) {
    Arena.call(this, area);
}
HyperArena.prototype = Object.create(Arena.prototype);

HyperArena.prototype.gameLoop = function () {
    gameLoopParent = this == window ? gameLoopParent : this;
    requestAnimationFrame(gameLoopParent.gameLoop)
    gameLoopParent.detectCollisions();
    gameLoopParent.handleOffScreen();
};

HyperArena.prototype.applyTunnel = function (sprite) {
    var sprite_rect = sprite.element.getBoundingClientRect();
    var world_rect = this.element.getBoundingClientRect();
    var x = sprite_rect.left;
    var y = sprite_rect.top;

    if (x <= 0 - sprite_rect.width) {
        x = world_rect.width - 1;
    } else if (x >= world_rect.width) {
        x = 0 - sprite_rect.width;
    }

    if (y <= 0 - sprite_rect.height) {
        y = world_rect.height - 1;
    } else if (y >= world_rect.height) {
        y = 0 - sprite_rect.height;
    }
    sprite.x = x;
    sprite.y = y;
    //sprite.setPosition(x, y);
};

HyperArena.prototype.handleOffScreen = function () {
    //Loop through all sprites
    for (var i = 0; i < this.sprites.length; i++) {
        var sprite = this.sprites[i];
        this.applyTunnel(sprite);
    }
};
