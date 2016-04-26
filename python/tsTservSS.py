#!/usr/bin/env python3

'''
使用SocketServer 里的TCPServer 和StreamRequestHandler 类创建一个时间戳TCP 服务器
'''

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print ('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline().decode())).encode())

tcpServ = TCP(ADDR, MyRequestHandler)
print ('waiting for connection...')
tcpServ.serve_forever()
