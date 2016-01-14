#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
file = open('D:\\bank\\export_30000.csv', 'r')
f = open('test.txt', 'w')
# while 1:
    # line = file.readline()
    # if not line:
        # break
    # pass # do something
	# print line
pattern = re.compile(r'´óÌü')
for eachline in file:
    match=pattern.search(eachline)
    if match:
    #print eachline,;
	    f.write(eachline)
file.close()

f.close()

