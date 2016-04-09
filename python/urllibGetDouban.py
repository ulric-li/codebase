#!/usr/bin/env python3

'''
对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应
'''

from urllib import request

#with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
with request.urlopen('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', data.decode('utf-8'))
