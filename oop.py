#!/usr/bin/env python
# -*- coding: utf-8 -*-

#class�������������������Student������ͨ���Ǵ�д��ͷ�ĵ��ʣ���������(object)����ʾ�����Ǵ��ĸ���̳������ģ��̳еĸ������Ǻ����ٽ���ͨ�������û�к��ʵļ̳��࣬��ʹ��object�࣬�������������ն���̳е��ࡣ
#
#�����������ģ������ã���ˣ������ڴ���ʵ����ʱ�򣬰�һЩ������Ϊ����󶨵�����ǿ����д��ȥ��ͨ������һ�������__init__�������ڴ���ʵ����ʱ�򣬾Ͱ�name��score�����԰���ȥ��

#����ͨ�ĺ�����ȣ������ж���ĺ���ֻ��һ�㲻ͬ�����ǵ�һ��������Զ��ʵ������self�����ң�����ʱ�����ô��ݸò���������֮�⣬��ķ�������ͨ����û��ʲô�������ԣ�����Ȼ������Ĭ�ϲ������ɱ�����͹ؼ��ֲ�����
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)
		
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()		