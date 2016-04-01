#!/usr/bin/env python3

'''
模仿登录的脚本
数据存在dict中，所以本次新加用户，不能在下一次运行程序时使用

'''

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if name in db.keys():
            prompt = 'name taken, try another:'
            continue
        else:
            break

    pwd = input('passwd:')
    db[name] = pwd

def olduser():
    name = input('login:')
    pwd = input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print ('welcome back', name)
    else:
        print ('login incorrect')

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Example 7.1 Dictionary Example (userpw.py) (continued)

    Enter choice: '''

    while True:
        try:
            choice = input(prompt).strip()[0].lower()
        except(EOFError, KeyboardInterrupt):
            choice = 'q'

        print ("\nYou picked:[%s]" % choice)

        if choice not in 'neq':
            print ('invalid option, try again')
        else:
            if choice == 'n':
                newuser()
            elif choice == 'e':
                olduser()
            else:
                print ('quit')
                return


if __name__ == '__main__':
    showmenu()
