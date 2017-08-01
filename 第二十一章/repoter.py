#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/25 11:10
# @Author  : Jeffrey
# @Site    : 
# @File    : repoter.py
# @Software: PyCharm
from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'hello,world!', textAnchor = 'middle')

d.add(s)
renderPDF.drawToFile(d,'hello.pdf','a simple pdf')
