#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/23 11:09
# @Author  : Jeffrey
# @Site    : 
# @File    : log.py
# @Software: PyCharm
import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('starting program')
logging.info('trying to divide 1 by 0')
print 1/0
logging.info('divide sucess')
logging.info('ending program')