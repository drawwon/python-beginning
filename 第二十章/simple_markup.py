#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/23 21:07
# @Author  : Jeffrey
# @Site    : 
# @File    : simple_markup.py.py
# @Software: PyCharm
from util import *
import re, sys
print '<html><head><title>...</title><body>.'
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\l</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'