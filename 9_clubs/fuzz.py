import socket
import sys


# options are 1,2,3

for i in range( 780,1000000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( ('127.0.0.1', 1337) )

    s.recv(1024)

    buf = b'3\x0a\x0d'

    s.send(buf)

    s.recv(1024)

    buf = '\x41'*i + '\x0a\x0dY'
    s.send(buf.encode('ascii'))
    s.recv(1024)
    s.send( 'Y\x0a\x0d'.encode('ascii'))
    print("{}: {}".format(s.recv(1024), i))
    s.close()
    
#    sys.exit(0)

