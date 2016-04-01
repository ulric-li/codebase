#!/usr/bin/env python3
# _*_ utf-8 *_*

'''
函数参数组合
'''

def f1(a, b, c = 0, *argv, **kw):
    print ('a = ', a, 'b = ', b, 'c = ', c, 'argv = ', argv, 'kw = ', kw)

def f2(a, b, c = 0, *, d, **kw):
    print ('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 99, ext = None)

argv = (1, 2, 3, 4)
kw = {'d':88, 'x':'#'}
f1(*argv, **kw)
argv = (1, 2, 3)
kw = {'d':88, 'x':'#'}
f2(*argv, **kw)
