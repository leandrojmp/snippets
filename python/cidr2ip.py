# reads a file with a list of networks and convert to a ip list
# input.txt
# 192.168.0.0/24
#
# usage: cidr2ip.py input.txt
# output is a file callet cidr2ip.txt with one ip per line
#
# cidr2ip.txt
# 192.168.0.1
# 192.168.0.2
# ...
# 192.168.0.255

from ipaddress import ip_network as cidr
from sys import argv
from os import remove

try:
    remove("cidr2ip.txt")
except OSError:
    pass

cidr_in = argv[1]

ipList = open(argv[1],'r').read().split('\n')
ipList.remove('')

with open("cidr2ip.txt",'a') as cidr_out:
    for i in ipList:
        for ip in cidr(i):
            print('{}'.format(ip),file=cidr_out)
