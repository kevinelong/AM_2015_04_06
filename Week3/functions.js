//Classic
function add(x, y) {
    return x + y;
}
console.log(add(2, 2))

//Modern
var add = function (x, y) {
    return x + y;
};
console.log(add(2, 2))


//IIFE
console.log(
    function (x, y) {
        return x + y;
    }(2, 2)
);

//In a "class/module/namespace"
var calc = {
    add: function (x, y) {
        return x + y;
    }
};
console.log(calc.add(2, 2))


//In an IIFE Factory made "class"
// in this case a singleton(a class with only one instance ever)
var calcSingleton = function () {
    function add(x, y) {
        return x + y;
    }
    //Not returned in the object below like add is
    function i_am_private(){
        return 0;
    }
    //Public methods are returned
    return {
        add: add
    };
}();
console.log(calcSingleton.add(2, 2))