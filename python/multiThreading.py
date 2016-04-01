#!/usr/bin/env python3

'''
多线程练习脚本
线程是操作系统直接支持的执行单元。进程是由若干线程组成的，一个进程至少有一个线程。
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
'''

import time
import threading

# 新线程执行的代码:
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)

    print('Thread %s ended.' % threading.current_thread().name)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)

