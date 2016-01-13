#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('test.txt', 'r')

print f.read()

f.close()

f = open('test.txt', 'w')
f.write('Hello, world!')
f.close()

