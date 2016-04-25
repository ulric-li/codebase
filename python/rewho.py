#!/usr/bin/env python3

'''
使用正则表达式
将linux的who命令中的用户名、登录时间等打印出来
'''

import re
from os import popen
from re import split

f = popen('who', 'r')

for eachLine in f.readlines():
    print(re.split('\s\s+|\t', eachLine))

f.close()
