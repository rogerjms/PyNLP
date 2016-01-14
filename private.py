#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
		
bart = Student('Bart Simpson', 98)
#bart.print_score()
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
#print bart.__name
print bart._Student__name

#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。