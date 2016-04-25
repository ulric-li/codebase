#!/usr/bin/env python3

'''
创建一个能接收客户的消息，在消息前加一个时间戳后返回的TCP 服务器。
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        else:
            print('data:', data)
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())

    tcpCliSock.close()

tcpSerSock.close()
