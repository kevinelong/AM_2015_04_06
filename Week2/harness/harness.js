//document.write(6 * 7);

//document.body.innerHTML = (6*7);
var p = document.createElement("div");
p.innerHTML = 6 * 7;

var q = document.createElement("span");
q.innerHTML = "pollenate";

p.appendChild(q);
document.body.appendChild(p);
//document.body.appendChild(q);


