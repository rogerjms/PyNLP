#!/usr/bin/env python
# -*- coding: utf-8 -*-

from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞')

s.words # [u'这个', u'东西', u'真心',
# u'很', u'赞']

s.tags # [(u'这个', u'r'), (u'东西', u'n'),
# (u'真心', u'd'), (u'很', u'd'),
# (u'赞', u'Vg')]

s.sentiments # 0.9769663402895832 positive的概率

s.pinyin # [u'zhe', u'ge', u'dong', u'xi',
# u'zhen', u'xin', u'hen', u'zan']

s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
