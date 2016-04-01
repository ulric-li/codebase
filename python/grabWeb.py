#!/usr/bin/env python

import urllib.request

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print (firstNonBlank(lines), end = '')
    lines.reverse()
    print (firstNonBlank(lines), end = '')

def download(url='http://www.baidu.com', process=firstLast):
    try:
        retval = urllib.request.urlretrieve(url)[0]
    except IOError:
        retval = None

    if retval:
        process(retval)

if __name__ == '__main__':
    download()
