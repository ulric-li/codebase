#!/usr/bin/env python3

# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 3.4.
# It may run on any other version with/without modifications.

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
        print("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_service_name()
