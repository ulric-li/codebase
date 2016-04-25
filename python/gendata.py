#!/usr/bin/env python3

'''
为练习使用正则表达式生成随机数据，并将产生的数据输出到屏幕
'''

from random import randint, choice
from string import ascii_lowercase
from sys import maxsize 
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
    dtint = randint(0, maxsize - 1) % 10000000000
    dtstr = ctime(dtint)

    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(ascii_lowercase)

    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer))
