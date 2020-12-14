Socks5 server open on this port.

Can configure to run proxy chains through it, however don't know whats on the other side of the proxy.

#LL
When the proxy is open, can use proxychains to scan the localhost of the proxy to see what ports are listenting on the loopback.

```bash
# after adding the port (1080) and target in the /etc/proxychains.conf
proxychains nmap -n -v -p- -sCTV -T4 127.0.0.1
```

[answer](https://rushisec.net/metasploit-ctf-2020-writeup/#8ofspadesport1080)
