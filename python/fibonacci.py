#!/usr/bin/env python3

'''
斐波那契数列
'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

i = int(input("Enter an integer:"))
print (fact(i))
