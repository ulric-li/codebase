#!/usr/bin/env python3

'''
地址类
涉及类定义、类继承
'''

class AddrBookEntry(object): # 类定义
    'address book entry class'
    def __init__(self, nm, ph): # 定义构造器
        self.name = nm # 设置 name
        self.phone = ph # 设置 phone
        print('Created instance for:', self.name)

    def updatePhone(self, newph): # 定义方法
        self.phone = newph
        print('Updated phone# for:', self.name)


class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'#员工地址本类
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em
        print('Employee Address Book Entry class')
        
    def updateEmail(self, newem):
        self.email = newem
        print('Updated e-mail address for:', self.nam)



if __name__ == '__main__':
    john = AddrBookEntry('John Doe', '408-555-1212') #为John Doe 创建实例
    jane = AddrBookEntry('Jane Doe', '650-555-1212') #为Jane Doe 创建实例
    kobe = EmplAddrBookEntry('kobe bryant', '408-555-1212',42, 'kobe@spam.doe')
    print(john)
    print(john.name)
    print(john.phone)
    print(jane.name)
    print(jane.phone)
    john.updatePhone('415-555-1212') #更新John Doe 的电话
    print(john.phone)

