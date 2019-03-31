# ----- sender.py ------

#!/usr/bin/env python

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host = "127.0.0.1"
port = 60002
buf =1024
addr = (host,port)
file_name=sys.argv[1]
s.sendto(b'file_name',addr)
f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf)
s.close()
f.close()