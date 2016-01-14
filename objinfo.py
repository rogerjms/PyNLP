#!/usr/bin/env python
# -*- coding: utf-8 -*-

#判断对象类型，使用type()函数
type(123)
type('str')
type(None)

#Python把每种type类型都定义好了常量，放在types模块里

import types
type('abc')==types.StringType
type(u'abc')==types.UnicodeType
type([])==types.ListType
type(str)==types.TypeType
#最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

#以下两种方法等价
len('ABC')
'ABC'.__len__()


#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态，这里非常像R语言

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
