//BAD
$("#p1").css("color", "red").slideUp(2000).slideDown(2000);

//SLIGHTLY BETTER
$("#p1").css("color", "red")
  .slideUp(2000)
  .slideDown(2000);

//OK
var p = $("#p1");
p.css("color", "red");
//This must be a chained call back to wait until the first is complete.
p.slideUp(2000).slideDown(2000);

//alternately we could do the more verbose explicit setTimeout
p.slideUp(2000);
setTimeout(function(){
    p.slideDown(2000);
},2000);

//In all these cases using a new CSS3 animation and simple adding and removing a class would be better.