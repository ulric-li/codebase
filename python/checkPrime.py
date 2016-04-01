#!/usr/bin/env python3

'''
素数
'''

def isprime(number):
    flag = True

    a = int(number / 2)
    while a > 1:
        if number % a == 0:
            flag = False
            break
        else:
            a -= 1

    return flag


if __name__ == '__main__':
    while True:
        num = int(input("Enter an integer:"))
        if isprime(num):
            print ("%d is prime." % num)
        else:
            print ("%d is not prime." % num)
