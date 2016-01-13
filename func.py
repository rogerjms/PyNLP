#!/usr/bin/env python
# -*- coding: utf-8 -*-

#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-100)
		
#空函数		
def nop():
    pass

#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#添加参数检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#返回多个值，在perl中通过数组返回

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
x, y = move(100, 100, 60, math.pi / 6)
print x, y
#但其实这只是一种假象，Python函数返回的仍然是单一值：

r = move(100, 100, 60, math.pi / 6)
print r
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

#我们可以把年龄和城市设为默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

#定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
	

#函数参数不确定，方法1
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc([1, 2, 3])
 calc((1, 3, 5, 7))	

#函数参数不确定，方法2

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 3, 5, 7)

#定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。


#关键字参数

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#当然，上面复杂的调用可以用简化的写法：

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#参数组合

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

#>>> func(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
#>>> func(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
#>>> func(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
#>>> func(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}


#最神奇的是通过一个tuple和dict，你也可以调用该函数：

#>>> args = (1, 2, 3, 4)
#>>> kw = {'x': 99}
#>>> func(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。


#可见，abs(-10)是函数调用，而abs是函数本身。

#函数名也是变量

#那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

#如果把abs指向其他对象，会有什么情况发生？


