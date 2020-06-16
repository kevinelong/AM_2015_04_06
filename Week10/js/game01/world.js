function World(element) {
    var self = this;
    this.element = element;
    this.sprites = [];
    this.fillParentElement();
    this.currentElement = undefined;
    this.width = Math.max(element.clientWidth, element.innerWidth || 0);
    this.height = Math.max(element.clientHeight, element.innerHeight || 0);

    document.addEventListener("keydown", function (e) {
        var key = e.which;
        if (key === self.keyCodes.LEFT) {
            self.currentElement.moveLeft();
        } else if (key === self.keyCodes.UP) {
            self.currentElement.moveUp();
        } else if (key === self.keyCodes.RIGHT) {
            self.currentElement.moveRight();
        } else if (key === self.keyCodes.DOWN) {
            self.currentElement.moveDown();
        }
    });
}
World.prototype.fillParentElement = function () {
    this.element.setAttribute("style",
        "overflow:hidden;position:absolute;top:0;bottom:0;left:0;right:0;"
    );
};
World.prototype.keyCodes = {LEFT: 37, UP: 38, RIGHT: 39, DOWN: 40};
World.prototype.addElement = function (sprite) {
    this.sprites.push(sprite);
    sprite.world = this;
    sprite.init(this.element);
    this.element.appendChild(sprite.element);
};
World.prototype.moveRandom = function (sprite) {
    sprite.x = Math.floor(Math.random() * this.width);
    sprite.y = Math.floor(Math.random() * this.height);
    sprite.updatePosition();
};
