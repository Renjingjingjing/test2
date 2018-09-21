#!/usr/bin/env python
# encoding: utf-8
'''
@author: renjing
@file: TestAllRunner.py
@time: 2018/8/24 8:59
'''

import threading
from TestAllCase import *

def threads():
    threads=[]
    threads.append(threading.Thread(target=TestCass_Case1()))
    threads.append(threading.Thread(target=TestCass_Case2()))
    for th in threads:
        th.start()
    th.join()

# threads()