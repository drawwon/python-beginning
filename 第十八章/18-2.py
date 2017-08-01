#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/23 10:46
# @Author  : Jeffrey
# @Site    : 
# @Software: PyCharm
from distutils.core import setup,Extension

setup(name='hello',
      version='1.0',
      ext_module = [Extension('hello',['hello.c'])]
      )