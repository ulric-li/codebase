#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
闰年
'''

def leapYear(year):
    if (((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0))):
        print (year, 'is leap year')
    else:
        print (year, 'is not leap year')

if __name__ == '__main__':
    tag = True
    while(tag):
        iYear = int(input("Enter year:"))
        leapYear(iYear)
        flag = input("enter Y/y to continue:")
        if(flag == 'Y' or flag == 'y'):
            tag = True
        else:
            tag = False
