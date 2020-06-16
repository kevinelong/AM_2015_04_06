//Consider using this instead of the array check

function isDigit(c) {
    return !isNaN(parseInt(c));
}

//function isDigit2(c) {
//    var re = /[\d]/;
//    var output = re.test(c);
//    return output;
//}
function isDigit2(c) {
    return /[\d]/.test(c);
}

//function isDigit3(c) {
//    var numbers = '1234567890';
//    var index = numbers.indexOf(c);
//    return index != -1;
//}
function isDigit3(c) {
    return '1234567890'.indexOf(c) != -1;
}

function isDigit4(c) {
    return '1234567890'.hasOwnProperty(c);
}

function isValidPhoneNumber(phone) {
    var count = 0;

    for (var i = 0; i < phone.length; i++) {
        //One letter at a time
        var character = phone[i];
        console.log(character);
        console.log(i);

        //CAll out function on each letter in turn
        //if ('1234567890'.indexOf(character) != -1) {
        if (isDigit4(character)) {
            count++;
        } else {
            //console.log(character + " is not a number");
        }
    }

    console.log(count);
    var result = (count >= 9 && count <= 11);
    console.log("result: " + result);
    return result;
}

var goodPhone = '1-503-888-6879';
var tooManyPhone = '1342124-123--3--13';
var badPhone = '1.34';
console.log(isValidPhoneNumber(goodPhone));
console.log(isValidPhoneNumber(tooManyPhone));
console.log(isValidPhoneNumber(badPhone));
