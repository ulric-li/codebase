#!/usr/bin/env python3

'''
python3.4 爬虫教程
一个简单的示例爬虫
林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
'''

import urllib.request

url = 'http://www.douban.com/'
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
