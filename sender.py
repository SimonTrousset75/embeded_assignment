# Save as server.py 
# Message Sender
import os
from socket import *
import datetime
import time
host = "127.0.0.1" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    now = datetime.datetime.now()
    UDPSock.sendto(str(now), addr)
    time.sleep(1) 
UDPSock.close()
os._exit(0)
