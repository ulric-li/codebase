#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    #s.sendto(data, ('127.0.0.1', 9999))
    s.sendto(data, ('192.168.12.133', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()
