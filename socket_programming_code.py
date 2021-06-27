#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket


import time
s=socket.socket()

#s.setpocket(socket.SOL_SOCKET,socket.SO.REUSEADDR,1)
port=9001
ip="192.168.43.69"
s.connect((ip,port))


s=socket.socket()

s.connect(("192.168.43.145",12345))


# In[ ]:


def socketP():
    #s=socket.socket()
    #s=connect(("192.168.43.69",9001))
    s.send("on".encode())
    print("Hellllllllllooooooooooooooooooooo")
    #s.send("off".encode())
    

