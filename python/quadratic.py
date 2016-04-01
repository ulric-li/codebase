#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'''
求平方根
'''

import math
import sys

def quadratic(a, b, c):
    if ( b * b < 4 * a * c):
        print ('data error: b * b < 4 * a * c')
        sys.exit()
    s1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c))/(2 * a)
    s2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c))/(2 * a)
    return s1, s2

print (quadratic(2, 3, 1))
print (quadratic(8, 3, 4))
