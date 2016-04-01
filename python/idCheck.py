#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
检查输入的字符是否符合变量的命名要求
'''

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits
keywords = keyword.kwlist

print ('Welcome to the Identifier Checker V1.0')
print ('Testees must be at least 2 chars long.')
myInp = input('Identifier to test?')

flag = True

if len(myInp) > 1:
    if myInp in keywords:
        flag = False
        print ('invalid: the identifier must not be keyword.')
    elif myInp[0] not in alphas:
        print ('invalid: first symbol must be alphabetic')
        flag = False
    else:
        for otherChar in myInp[1:]:
            if otherChar not in alphas + nums:
                print ('invalid: remaining symbols must be alphanumeric')
                flag = False
                break

if flag == True:
    print ('okay as an identifier')
