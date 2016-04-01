#!/usr/bin/env python3

'''
读取文件
'''

#get file name
fname = input('enter file name:')
print

# attemp to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print ("*** file open error:", e)
else:
# display contents to the screen
    for eachline in fobj:
        print (eachline, end = ' ')
    fobj.close()
