#!/usr/bin/env python3

'''
创建一个能接收客户的消息，在消息前加一个时间戳后返回的UDP 服务器。
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print('...received from and return to :',addr)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data.decode())).encode(), addr)

udpSerSock.close()
