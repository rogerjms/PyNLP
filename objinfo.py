#!/usr/bin/env python
# -*- coding: utf-8 -*-

#�ж϶������ͣ�ʹ��type()����
type(123)
type('str')
type(None)

#Python��ÿ��type���Ͷ�������˳���������typesģ����

import types
type('abc')==types.StringType
type(u'abc')==types.UnicodeType
type([])==types.ListType
type(str)==types.TypeType
#���ע�⵽��һ�����;ͽ�TypeType���������ͱ�������;���TypeType��

#����class�ļ̳й�ϵ��˵��ʹ��type()�ͺܲ����㡣����Ҫ�ж�class�����ͣ�����ʹ��isinstance()����

#���Ҫ���һ��������������Ժͷ���������ʹ��dir()������������һ�������ַ�����list�����磬���һ��str������������Ժͷ�����

#�������ַ����ȼ�
len('ABC')
'ABC'.__len__()


#���getattr()��setattr()�Լ�hasattr()�����ǿ���ֱ�Ӳ���һ�������״̬������ǳ���R����

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
