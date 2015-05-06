document.addEventListener("DOMContentLoaded", function () {

var COUNTDOWN = 0;

var countdown_display = document.getElementById("countdown_display");
var go = document.getElementById("go");
var pause = document.getElementById("pause");

var hours = document.getElementById("hh");
var minutes = document.getElementById("mm");
var seconds = document.getElementById("ss");


function counter() {
    COUNTDOWN += (hours.value * 3600000);
    COUNTDOWN += (minutes.value * 60000);
    COUNTDOWN += (seconds.value * 1000);
}


function convert_time() {

    var hours_left = Math.floor(((COUNTDOWN / (1000*60*60)) % 24));
    var minutes_left = Math.floor(((COUNTDOWN / (1000*60)) % 60));
    var seconds_left = (COUNTDOWN / 1000) % 60;

    var hours_str = hours_left.toString().concat(" : ");
    var minutes_str = minutes_left.toString().concat(" : ");
    var seconds_str = seconds_left.toString();
    console.log("Seconds Left : ", seconds_str);

    return "".concat(hours_str, minutes_str, seconds_str);
}


function update_counter() {
    countdown_display.innerHTML = (convert_time(COUNTDOWN));
}


var ticker = 0;

    function tick() {

        update_counter();
        setTimeout(tick, 1000);

        ticker++;
        console.log(ticker);
        COUNTDOWN -= 1000;
        console.log(COUNTDOWN);
        var now = new Date();
        console.log(now);
        console.log(minutes_left);
        console.log(seconds_left);
}

    go.addEventListener("click", function (event) {
        console.log(event);
        console.log(this);
        counter();
        tick();
    });
});