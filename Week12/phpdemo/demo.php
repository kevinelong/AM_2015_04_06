<?php
require_once("math.php");

$m = new MathDemo();

$result = $m->DoubleIt(3);

print_r($result . "\n");

print("The result is: " . $result . "\n");

echo("The result is: $result\n");


