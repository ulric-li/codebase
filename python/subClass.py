#!/usr/bin/env python3

'''
类继承的简单例子
'''

class Animal(object):
    def run(self):
        print ('Animal is running...')

class Dog(Animal):
    def run(self):
        print ('Dog is running...')

    def eat(self):
        print ('Dog is eating meat...')

class Cat(Animal):
    def run(self):
        print ('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    dog.eat()

    cat = Cat()
    cat.run()

    run_twice(Dog())
    run_twice(Cat())
    run_twice(cat)
    print(dir(Dog))
