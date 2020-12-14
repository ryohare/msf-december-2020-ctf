The site gives the login code, in which we provide a username (which doesnt matter), a password and a hash which is verified in the code and prints the success code. The unknown here is the salt used. The code is below.

```php
        $options = [
            'salt' => *secret*,
            'cost' => 12
        ];
        if (password_hash($_POST['password'], PASSWORD_DEFAULT, $options) == $_POST['hash'] ){
            *success code goes here to send the challenge card back to the user*
        }
        else{
            echo "Invalid login! Maybe you should read the source code more closely?\n";
            echo "<script>setTimeout(() => { document.location = '/index.php'; }, 6000)</script>";
        }
```

As per the hint, it says look closely at the code, so there is likely a common mitake here.

The cost parameter is 1 level above the default.

Some ideas
1. Obscure properties of == and type interpoliation since we can control the 'hash' parameter
	* Tried using a number didnt work
2. Code injection via the 'hash' parameter
3. Null password to only hash the salt
	* Don't appear to get any hash output feedback, just a yes or no decision so brute forcing this would have to go over the web.
4. Induce a failure in password_hash, inwhich case it will return type:bool value:false. The Post parametmer looks up 'hash' for the key. If this is not provided, it will return false.
	* Not looking promising: https://stackoverflow.com/questions/39729941/php-password-hash-returns-false


So based on the research, it seems to be the issue is type juggling with PHP. The only issue is I cannot seem to figure out a 'hash' value to pass via post which is interpolated in a way the fixed output of the `password_hash` is handled. What I tried is.

* hash=<some substring>
	* This doesnt work because they are the same type, so it will look for an exact match. Need to get a type mismatch
* hash[]=
	* this evalutes to null as an emtpy array so we have `"some string"==NULL`
* hash[]="test"&hash[]="param"
	* This evaluates to hash[0]='test',hash[1]='param' which is `"some string" == array`
* hash=0
	* doesnt work because all POST parameters are rendered as strings.
* tried injection by passing in the hash function as the code but doesnt executed and rendered as a string
	* curl http://localhost:4444/test.php -X POST -d 'hash=<?php echo $test;  ?>'

 
The only way I can find to enter non-string data is with an array.

## Answer
What did I miss?
* I can pass in an array to the password field which would cause the hash function to return a NULL, which when compared to `hash=` equates to true.
[answer](https://rushisec.net/metasploit-ctf-2020-writeup/#4ofclubsport8092)

## Refs
https://www.netsparker.com/blog/web-security/php-type-juggling-vulnerabilities/
