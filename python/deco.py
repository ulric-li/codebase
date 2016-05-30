#!/usr/bin/env python3
'''
装饰器 使用显例
这个装饰器（以及闭包）示范表明装饰器仅仅是用来“装饰“（或者修饰）函数的包装，返回一
个修改后的函数对象，将其重新赋值原来的标识符，并永久失去对原始函数对象的访问。
'''

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' %(ctime(), func.__name__))
        return func()

    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

