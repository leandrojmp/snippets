import socket
import sys
from sys import argv

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('192.168.1.51', 5001)

for line in open(argv[1],"r").read():
    sock.sendto(bytes(line,"utf-8"), address)

sock.close()
