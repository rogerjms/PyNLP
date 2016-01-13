#!/usr/bin/env python
# -*- coding: utf-8 -*-

#��Python�У�����һ������Ҫʹ��def��䣬����д�������������š������еĲ�����ð��:��Ȼ�����������б�д�����壬�����ķ���ֵ��return��䷵�ء�

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-100)
		
#�պ���		
def nop():
    pass

#pass���ʲô������������ʲô�ã�ʵ����pass����������Ϊռλ�����������ڻ�û�����ôд�����Ĵ��룬�Ϳ����ȷ�һ��pass���ô���������������

#��Ӳ������
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#���ض��ֵ����perl��ͨ�����鷵��

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
x, y = move(100, 100, 60, math.pi / 6)
print x, y
#����ʵ��ֻ��һ�ּ���Python�������ص���Ȼ�ǵ�һֵ��

r = move(100, 100, 60, math.pi / 6)
print r
#ԭ������ֵ��һ��tuple�����ǣ����﷨�ϣ�����һ��tuple����ʡ�����ţ��������������ͬʱ����һ��tuple����λ�ø�����Ӧ��ֵ�����ԣ�Python�ĺ������ض�ֵ��ʵ���Ƿ���һ��tuple����д���������㡣

#���ǿ��԰�����ͳ�����ΪĬ�ϲ���
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

#����Ĭ�ϲ���Ҫ�μ�һ�㣺Ĭ�ϲ�������ָ�򲻱����

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
	

#����������ȷ��������1
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc([1, 2, 3])
 calc((1, 3, 5, 7))	

#����������ȷ��������2

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 3, 5, 7)

#����ɱ�����Ͷ���list��tuple������ȣ������ڲ���ǰ�����һ��*�š�


#�ؼ��ֲ���

�Ϳɱ�������ƣ�Ҳ��������װ��һ��dict��Ȼ�󣬰Ѹ�dictת��Ϊ�ؼ��ֲ�������ȥ��

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#��Ȼ�����渴�ӵĵ��ÿ����ü򻯵�д����

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#�������

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
#�ں������õ�ʱ��Python�������Զ����ղ���λ�úͲ������Ѷ�Ӧ�Ĳ�������ȥ��

#>>> func(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
#>>> func(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
#>>> func(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
#>>> func(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}


#���������ͨ��һ��tuple��dict����Ҳ���Ե��øú�����

#>>> args = (1, 2, 3, 4)
#>>> kw = {'x': 99}
#>>> func(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
#���ԣ��������⺯����������ͨ������func(*args, **kw)����ʽ���������������Ĳ�������ζ���ġ�


#�ɼ���abs(-10)�Ǻ������ã���abs�Ǻ�������

#������Ҳ�Ǳ���

#��ô��������ʲô�أ���������ʵ����ָ�����ı���������abs()�����������ȫ���԰Ѻ�����abs���ɱ�������ָ��һ�����Լ������ֵ�ĺ�����

#�����absָ���������󣬻���ʲô���������


