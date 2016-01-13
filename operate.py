#!/usr/bin/env python
# -*- coding: utf-8 -*-
#取一个list或tuple的部分元素是非常常见的操作


#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

#可以看出，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可#以作用在其他可迭代对象上。

#list这种数据类型虽然有下标，#但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
	
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v

	

#for 好随意啊 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。



#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代True

