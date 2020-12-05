At this point we know the hash, the prefix it starts with and the regexp for filtering, e.g. character set.

Regexp, [a-z0-9]{9,14}

The prefix is 'ihatesalt' which is 9 chars, so we can brute or dictionary character positions 10-14 with hashcat using a mask.

So, this one started with enumerating the web page and seeing all the out links and following them up. Found a password hint function which said the password started with 'ihatesalt' If you issue the request as a cmd line or in the browser network console you can see the full response which gives the username AND the hash of the password. So we set this up as a hashcat cracking event. Did the following.

Mask File (mask.txt)
```text
ihatesalt?1
ihatesalt?1?1
ihatesalt?1?1?1
ihatesalt?1?1?1?1
ihatesalt?1?1?1?1?1
```

Hash file (ihatesalt.txt)
```
7f35f82c933186704020768fd08c2f69
```

Hash cat command on Windows
```batch
hashcat64.exe -m 0 -a 3 -1 ?l?d ihatesalt.txt masks.txt
hashcat64.exe -m 0 -a 3 -1 ?l?d ihatesalt.txt masks.txt --show
```

This gave us the password, ihatesaltalot7. While enumerating the webpage, there was an admin endpoint. Going to that, it asked for the username and password, using the creds, it gave us the joker picture.

Resources robbed.

https://hashcat.net/wiki/doku.php?id=mask_attack#hashcat_mask_files
https://hashcat.net/forum/thread-8907.html

