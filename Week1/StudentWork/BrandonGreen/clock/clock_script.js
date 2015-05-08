document.addEventListener("DOMContentLoaded", function () {


    var countdown_display = document.getElementById("countdown_display");
    var go = document.getElementById("go");
    var pause = document.getElementById("pause");
    var hours = document.getElementById("hh");
    var minutes = document.getElementById("mm");
    var seconds = document.getElementById("ss");


    var COUNTDOWN = 0;


    pause.style.display = "none";
    var paused;


    function convert_time() {
        var hours_left = Math.floor(((COUNTDOWN / (1000*60*60)) % 24));
        var minutes_left = Math.floor(((COUNTDOWN / (1000*60)) % 60));
        var seconds_left = (COUNTDOWN / 1000) % 60;
        var hours_str = hours_left.toString().concat(" : ");
        var minutes_str = minutes_left.toString().concat(" : ");
        var seconds_str = seconds_left.toString();

        return "".concat(hours_str, minutes_str, seconds_str);
    }


    function update_counter() {
        countdown_display.innerHTML = (convert_time(COUNTDOWN));
    }


    function update_inputs() {
        var hours_left = Math.floor(((COUNTDOWN / (1000*60*60)) % 24));
        var minutes_left = Math.floor(((COUNTDOWN / (1000*60)) % 60));
        var seconds_left = (COUNTDOWN / 1000) % 60;

        hours.value = hours_left;
        minutes.value = minutes_left;
        seconds.value = seconds_left;
    }


    function pause_counter() {
        clearTimeout(paused);
        update_inputs();
    }


    function stupid_pause_bug() {
        COUNTDOWN += 1000;
    }


    function toggle_button() {
        if (go.style.display == "none") {
            go.style.display = "inline-block";
            pause.style.display = "none";
        } else {
            pause.style.display = "inline-block";
            go.style.display = "none";
        }
    }


    var incrementer = 16;
    function call_flash() {

        function flash() {
            incrementer--;
            if (incrementer % 2 != 0) {
                countdown_display.classList.add("flashy");
            } else {
                countdown_display.classList.remove("flashy");
            }
            if (incrementer > 1) {
                setTimeout(call_flash, 250);
            }
        }
        flash();
    }


    var ticker = 0;
    function tick() {
        if (COUNTDOWN >= 0) {
            paused = setTimeout(tick, 1000);
            update_counter();
            update_inputs();
        }
        if (COUNTDOWN == 0) {
            call_flash();
            toggle_button();
            update_inputs();
        }

        COUNTDOWN -= 1000;
        console.log("Countdown:", COUNTDOWN);

        ticker++;
        console.log("Ticker:", ticker);

        var now = new Date();
        console.log(now);
    }


    go.addEventListener("click", function (event) {
        console.log(event);
        console.log(this);
        COUNTDOWN = ((hours.value * 3600000) + (minutes.value * 60000) + (seconds.value * 1000));
        tick();
        toggle_button();

    });


    pause.addEventListener("click", function (event) {
        console.log(event);
        console.log(this);
        pause_counter();
        stupid_pause_bug();
        update_inputs();
        toggle_button();
    });


});