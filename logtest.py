#!/usr/bin/env python
# encoding: utf-8
'''
@author: renjing
@file: logtest.py
@time: 2018/8/29 9:28
'''
import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     filename='testlog.log',
#                     filemode='w')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


logger = logging.getLogger()
fh = logging.FileHandler('test.log')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
