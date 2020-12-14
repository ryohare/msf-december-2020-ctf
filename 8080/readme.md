This on required discovering a username which is valid for the site. So this required finding something unique when a known user name (which was provided as guest) and one which was invalid.

Did not get.

Where I went wrong.

I enumerated the hell out of this looking at the HTTP requests and responses for any indicators that a valid user name was entered versus not. I also inspected the traffic and resulting pages trying to identify data leakage. Couldnt find anything for this, so I figured, since the username + password combination reported a bad username, I had to see what a success message looked like, so I tried password guessing for the guest account with hydra.

Never found the password.

What I missed was there was a timing change in a valid username and an invalid username. Using this timing channel, a script can be written which would detect the long delay in the response and enumerate a username lists for the valid username.

[answer](https://rushisec.net/metasploit-ctf-2020-writeup/#3ofspadesport8080)
