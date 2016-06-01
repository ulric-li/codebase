#!/usr/bin/env python3
# _*_ coding: utf_8 _*_

# Python Network Programming Cookbook -- Chapter – 1
# This program is optimized for Python 3.4.
# It may run on any other version with/without modifications.

import socket

def get_remote_machine_info():
    #remote_host = 'www.python.org'
    remote_host = 'www.pytgo.org'
    #remote_host = 'www.baidu.com'
    #remote_host = 'www.qq.com'
    try:
        print("IP address: %s" %socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print("%s: %s" %(remote_host, err_msg))

if __name__ == '__main__':
    get_remote_machine_info()
