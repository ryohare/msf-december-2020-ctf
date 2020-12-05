Site redirects to an internal site, intranet.metasploit.ctf. Apple to access this via setting the host header to the intranet.metasploit.ctf while still curling the localhost. The landing page indicates there are subdirectories and subpages which will have stuff in them. I tried running gobuster on this with the -H setting (header) but the Host header still seems to be set to localhost.

To get gobuster working with a host header, it was discovered that golang has bugs ignoring it The Best way to get going, as I saw it, was to use burp and have it re-write the host header in the proxy which appeared to be working.

Ran default gobuster can was not able to find any subdomains. (full...txt). Will re-run with a bigger wordlist.
