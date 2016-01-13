#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""

#python的print语句
print u'中文测试正常'
print "I'm Python. Nice to meet you!"

# 赋值之前不需要声明
some_var = 5    
some_var  # => 5
#没有定义赋值的变量名会报错
#some_other_var

#三目操作符
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

#python内置数据类型之一 list列表 list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates = ['科科', '松松', '楠楠']
classmates.append('明明')
#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
#要删除list末尾的元素，用pop()方法：
classmates.pop()#很想Perl的数组
print classmates[1].decode('utf-8')
for key in classmates:
    print key.decode('utf-8')
print len(classmates)
#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')

print classmates[1]

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

#一个“可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t


#birth = int(raw_input('birth: '))


#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
d['Adam']

#判断key时候存在
'Thomas' in d

d.get('Thomas')

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除

d.pop('Bob')
#和list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：

#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print s
#set([1, 2, 3])




 
 


