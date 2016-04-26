#!/usr/bin/env python3

'''
创建一个TCP 客户端，程序会提示用户输入要传给服务器的信息，显示服务器返回的加了
时间戳的结果.
'''

from socket import *

HOST = '192.168.12.168'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break

    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break

    print(data)

tcpCliSock.close()
