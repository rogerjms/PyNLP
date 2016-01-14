#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print 'Animal is running...'
		
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
class Cat(Animal):
    pass
	
dog = Dog()
dog.run()

#当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
#判断一个变量是否是某个类型可以用isinstance()判断：

#isinstance(a, list)
#True
# isinstance(b, Animal)
#True
# isinstance(c, Dog)
#True
def run_twice(animal):
    animal.run()
    animal.run()
class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

run_twice(Tortoise()) #子类对象指向父类引用