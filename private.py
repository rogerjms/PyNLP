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
#���Ҫ���ڲ����Բ����ⲿ���ʣ����԰����Ե�����ǰ���������»���__����Python�У�ʵ���ı����������__��ͷ���ͱ����һ��˽�б�����private����ֻ���ڲ����Է��ʣ��ⲿ���ܷ���
#print bart.__name
print bart._Student__name

#�ܵ���˵���ǣ�Python����û���κλ�����ֹ��ɻ��£�һ��ȫ���Ծ���