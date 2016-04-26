#!/usr/bin/env python3

'''
创建一个UDP 客户端，程序会提示用户输入要传给服务器的信息，显示服务器返回的加了时间
戳的结果。
'''

from socket import *

HOST = '192.168.12.168'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.strip())

udpCliSock.close()
