#!/usr/bin/env python3

'''
使用fork创建新的进程
'''

import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
