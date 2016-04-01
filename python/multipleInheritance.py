#!/usr/bin/env python3

'''
类的多重继承
'''

class Animal(object):
    def __init__(self):
        print ('Animal')

class Mammal(Animal):
    def __init__(self):
        print ('Mammal')

class Bird(Animal):
    def __init__(self):
        print ('Bird')

class Runnable(object):
    def run(self):
        print ('running ...')

class Flyable(object):
    def fly(self):
        print ('flying ...')

#####################################################

class Dog(Mammal, Runnable):
    def __init__(self):
        print ('Dog')

class Bat(Mammal, Flyable):
    def __init__(self):
        print ('Bat')

class Parrot(Bird, Flyable):
    def __init__(self):
        print ('Parrot')

class Ostrich(Bird, Runnable):
    def __init__(self):
        print ('Ostrich')

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    bird = Bird()
