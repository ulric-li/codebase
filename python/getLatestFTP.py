#!/usr/bin/env python3

'''
这个程序用于下载网站中最新版本的文件。你可以修改这个程序让它下载你喜欢的程序。
'''

import ftplib
import os
import socket

HOST = 'ftp.bupt.edu.cn'
DIRN = 'pub/software/Network/Proxy/'
FILE = 'squid-2.5.STABLE10.tar.bz2'

def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymously"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print ('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('*** Downloaded "%s" to CWD' % FILE)
        f.quit()
        return

if __name__ == '__main__':
    main()

