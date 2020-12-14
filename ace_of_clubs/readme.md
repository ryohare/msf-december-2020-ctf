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

unable to figure out how to replace the the lib. Tried LD_PRELOAD and LD_LIBRARY_PATH to replace the library with an msf generated one and root shell one wrote locally. LD_ are not usable when SUID is used as well.

## LL
The trick here is to use the fact that the log file name is user controllable and is read/writen as root meaning any file on the filesystem is game. This is only helpful if input is user controllable. The logger will log the user input arguments as the first log entry. Therefore, any thing that can interpret a file which ignores errors until it finds something it likes, (like PHP for example), can be mdified or executed as root. In the case of this, and the posted solutions, they modified the `/etc/passwd` file to get this working.

[answer](https://sec.stealthcopter.com/metasploit-community-ctf-2020-dec-write-up-ace-of-clubs-port-9009/) 
