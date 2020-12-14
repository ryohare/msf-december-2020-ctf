Site redirects to an internal site, intranet.metasploit.ctf. Apple to access this via setting the host header to the intranet.metasploit.ctf while still curling the localhost. The landing page indicates there are subdirectories and subpages which will have stuff in them. I tried running gobuster on this with the -H setting (header) but the Host header still seems to be set to localhost.

To get gobuster working with a host header, it was discovered that golang has bugs ignoring it The Best way to get going, as I saw it, was to use burp and have it re-write the host header in the proxy which appeared to be working.

Ran default gobuster can was not able to find any subdomains. (full...txt). Will re-run with a bigger wordlist.

# Where I Went Wrong
I didnt realize it was subdomain enumeration and I tried looking using the main domain and looking for pages on that. The hit said, subdomain's but I blew over it. People who did this successfully used ffuf to do this enumerating the subdomain.

```bash
# fs = filter size (the 404)
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://localhost:8201/ -H "Host: FUZZ.intranet.metasploit.ctf" -fs 145
```

[Answer](https://rushisec.net/metasploit-ctf-2020-writeup/#9ofdiamondsport8201)
