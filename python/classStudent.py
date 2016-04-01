#!/usr/bin/env python3

'''
类（Class）和实例（Instance）
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问.

'''

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print ('%s:%s' %(self.__name, self.__score))

if __name__ == '__main__':
    bart = Student('Bart Simpson', 59)
    bart.print_score()
    print(bart.get_grade())
# 可以通过以下方式访问私有变量
    print(bart._Student__name)
# 不能直接访问私有变量
    print(bart.__name)
