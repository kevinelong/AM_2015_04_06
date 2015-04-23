//Consider using this instead of the array check
function isDigit(c){
    return !isNaN(parseInt(c));
}

function isValidPhoneNumber(phone) {
    var numbers = '1234567890';
    var count = 0;
    for (var i = 0; i < phone.length; i++) {
        var c = phone[i];
        //console.log(c);
        var index = numbers.indexOf(c);
        //console.log(index);
        if (index != -1) {
            count++;
        }else{
            //console.log(c + " is not a number");
        }
    }
    //console.log(count);
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
