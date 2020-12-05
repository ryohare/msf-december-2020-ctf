#!/bin/bash 
ssh -i ssh-key kali@34.224.168.2 -L $1:172.15.23.149:$1 -N -f
