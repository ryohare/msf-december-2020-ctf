# MSF December CTF 2020
## Lessions Learned
1. When looking at a network service which excepts and replies with ascii text, check for format string issues as well as fuzzing
2. Look for user controllable files with SUID programs and check if the /etc/passwd or other sensitive files could be overwritten.
	* SUID programs cannot be influenced by LD_\* env var modificdations
3. Always scan the localhost when a proxy or socks server is detected with proxychains, and http_tunnel
4. When looking for changes in a web response for enumeration, look for timing changes too e.g. valid user takes X seconds, invalid user takes Y seconds.
5. Use `ffuf` to do subdomain discovery. In addition, can use `FinalRecon`
