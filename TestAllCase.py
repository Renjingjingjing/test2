#!/usr/bin/env python
# encoding: utf-8
'''
@author: renjing
@file: TestAllCase.py
@time: 2018/8/22 15:06
'''
from testcase.testvote import *


def TestCass_Case1():
    post_vote()
    get_polls()
    get_login()


def TestCass_Case2():
    toupiao_login()
    get_novelApi()
    get_createUserKey()
    get_findStatistics()
