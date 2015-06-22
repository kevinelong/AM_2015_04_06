function Sprite(content) {
    this.element = document.createElement("div");
    //this.element.style.transition = "all 0.33s ease-in-out";
    this.element.innerHTML = content;
}

Sprite.prototype.init = function (parentElement) {
    this.element.style.position = "absolute";
    this.self = this;
    this.parentElement = parentElement;
};

Sprite.prototype.setPosition = function (x, y) {
    this.x = x;
    this.y = y;
    this.updatePosition();
};

Sprite.prototype.updatePosition = function () {
    this.box = this.element.getBoundingClientRect();
    this.element.style.transform = "translate3d(" + this.x + "px," + this.y + "px,0)";
};

Sprite.prototype.setX = function (x) {
    this.x = x;
    this.updatePosition();
};

Sprite.prototype.setY = function (y) {
    this.y = y;
    this.updatePosition();
};

Sprite.prototype.moveRight = function () {
    this.setX(this.x += this.box.width)
};
Sprite.prototype.moveLeft = function () {
    this.setX(this.x -= this.box.width)
};
Sprite.prototype.moveUp = function () {
    this.setY(this.y -= this.box.height)
};
Sprite.prototype.moveDown = function () {
    this.setY(this.y += this.box.height)
};
