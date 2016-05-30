#!/usr/bin/env python3

'''
一个将函数作为参数传递，并在函数体内调用这些函数，更加实际的例子。这个脚本用传入的
转换函数简单将一个序列的数转化为相同的类型。特别地，test()函数传入一个内建函数int(),
或者float()来执行转换。
'''

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 9999999999999999)

print(convert(int, myseq))
print(convert(float, myseq))

