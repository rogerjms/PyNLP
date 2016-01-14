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

#�����Ƕ���һ��class��ʱ������ʵ���ϾͶ�����һ���������͡����Ƕ�����������ͺ�Python�Դ����������ͣ�����str��list��dictûʲô����

a = list() # a��list����
b = Animal() # b��Animal����
c = Dog() # c��Dog����
#�ж�һ�������Ƿ���ĳ�����Ϳ�����isinstance()�жϣ�

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

run_twice(Tortoise()) #�������ָ��������