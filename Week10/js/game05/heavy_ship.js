function HeavyShip(symbol) {
    Ship.call(this, symbol);
    this.mx = 0;
    this.my = 0;
    this.element.style.border = "1px solid green"
}
HeavyShip.prototype = Object.create(Ship.prototype);


HeavyShip.prototype.moveRight = function () {
    this.mx += .5;
};
HeavyShip.prototype.moveLeft = function () {
    this.mx -= .5;
};
HeavyShip.prototype.moveUp = function () {
    this.my -= .5;
};
HeavyShip.prototype.moveDown = function () {
    this.my += .5;
};
HeavyShip.prototype.collided = function (other) {
    this.element.style.backgroundColor = "red";

    //this.mx = this.mx + other.mx;
    //this.my = this.my + other.my;

    this.mx = -(this.mx);
    this.my = -(this.my);
};

function EnemyShip(symbol) {
    HeavyShip.call(this, symbol);
    this.mx = 0;
    this.my = 0;
    this.element.style.border = "1px solid red"
}
EnemyShip.prototype = Object.create(HeavyShip.prototype);

EnemyShip.prototype.collided = function (other) {
    HeavyShip.prototype.collided.call(this, other);
    this.element.style.backgroundColor = "red";
};
