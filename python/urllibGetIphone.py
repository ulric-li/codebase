#!/usr/bin/env python3

'''
模拟iPhone 6去请求豆瓣首页
'''

from urllib import request

req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (ipone; CPU iphone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    
    for k, v in f.getheaders():
        print('%s: %s' % (k, v)) 

    print('Data:', f.read().decode('utf-8')) 
