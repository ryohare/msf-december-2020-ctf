<?php
print("fuck\n");

$options = [
	'cost' => 12
];

#$_POST=[
#	'hash' => 0 
#];
print($_POST['hash']);
print("\n");
print(gettype($_POST['hash']));
print("\n");
$hash = password_hash( "s", PASSWORD_DEFAULT, $options);
print(gettype($hash));
print("\n");
print($hash);
print("\n");
var_dump( $hash == $_POST['hash']);
print("\n");

#var_dump("0e174892301580325162390102935332" == "0");print("\n");
