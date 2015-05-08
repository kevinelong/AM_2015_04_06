document.addEventListener("DOMContentLoaded", function () {


    var countdown_display = document.getElementById("countdown_display");
    var go = document.getElementById("go");
    var pause = document.getElementById("pause");
    var reset = document.getElementById("reset");
    var engage_audio = document.getElementById("engage_audio");
    var done_audio = document.getElementById("done_audio");
    var reset_audio = document.getElementById("reset_audio");
    var pause_audio = document.getElementById("pause_audio");
    var hours = document.getElementById("hh");
    var minutes = document.getElementById("mm");
    var seconds = document.getElementById("ss");
    //var number_inputs = document.getElementsByTagName("input");


    var COUNTDOWN = 0;


    pause.style.display = "none";
    var paused;


    function pad(time_unit) {
        var preppender = "0";

        if (time_unit.length == 1) {
            return preppender.concat(time_unit);
        } else {
            return time_unit;
        }
    }


    function convert_time() {
        var hours_left = Math.floor(((COUNTDOWN / (1000*60*60)) % 24));
        var minutes_left = Math.floor(((COUNTDOWN / (1000*60)) % 60));
        var seconds_left = (COUNTDOWN / 1000) % 60;
        var hours_str = hours_left.toString();
        var minutes_str = minutes_left.toString();
        var seconds_str = seconds_left.toString();
        var time_array = [pad(hours_str), pad(minutes_str), pad(seconds_str)];

        return time_array.join(" : ");
    }

    function update_counter() {
        countdown_display.innerHTML = (convert_time(COUNTDOWN));
    }


    function update_inputs() {
        var hours_left = Math.floor(((COUNTDOWN / (1000*60*60)) % 24));
        var minutes_left = Math.floor(((COUNTDOWN / (1000*60)) % 60));
        var seconds_left = (COUNTDOWN / 1000) % 60;

        var hours_str = hours_left.toString();
        var minutes_str = minutes_left.toString();
        var seconds_str = seconds_left.toString();

        hours.value = pad(hours_str);
        minutes.value = pad(minutes_str);
        seconds.value = pad(seconds_str);
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
            done_audio.play();
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
        engage_audio.play();
        console.log(event);
        console.log(this);
        COUNTDOWN = ((hours.value * 3600000) + (minutes.value * 60000) + (seconds.value * 1000));
        incrementer = 16;
        tick();
        toggle_button();

    });


    pause.addEventListener("click", function (event) {
        pause_audio.play();
        console.log(event);
        console.log(this);
        pause_counter();
        stupid_pause_bug();
        update_inputs();
        toggle_button();
    });


    reset.addEventListener("click", function (event) {
        reset_audio.play();
        console.log(event);
        console.log(this);
        COUNTDOWN = 0;
        pause_counter();
        update_counter();

        if (go.style.display == "none") {
            toggle_button();
        }
    });


});