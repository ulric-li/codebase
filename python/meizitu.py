#!/usr/bin/env python3

import multiprocessing
import time
import requests
from bs4 import BeautifulSoup

def crawl():
    j = 0
    for i in range(5093, 5113):
        url = 'http://www.meizitu.com/a/%d.html' % i
        print('url: %s' % url)
        try:
            print('try')
            soup = BeautifulSoup(requests.get(url).text, 'html5lib')
            print('soup')
            content = soup('div', id = 'picture')[0]
            print('contend')
            img = content.findALL('img')
            print('img')
            imgsrc = [c.get('src') for c in img]
            print('imgsrc')
            for photo in imgsrc:
                r = requests.get(photo, stream = True)
                print('requests')
                with open(u'./meizi/' + './' + str(j) + '.jpg', 'wb') as fd:
                    for chunk in r.iter_content():
                        fd.write(chunk)
                        print('write')
                    j += 1
            print('except')
        except Exception as e:
            continue
        print(u'进行到第%d页' % i).encode('gbk')

def process_link_crawler():
    num_cpus = multiprocessing.cpu_count()
    print('num_cpus:%d' % num_cpus)
    process = []
    for i in range(num_cpus):
        p = multiprocessing.Process(target = crawl)
        p.start()
        process.append(p)
    print('process_link_crawler for 1')
    for p in process:
        p.join()
    print('process_link_crawler for 2')

if __name__ == '__main__':
    #start = time.clock()
    process_link_crawler()
    #end = time.clock()
