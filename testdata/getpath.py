#!/usr/bin/env python
# encoding: utf-8

import os
import time
import xlrd

def GetTestDataPath():
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testdata", "TestData.xls")


def GetTestReport():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testreport", now + "TestReport.xls")


def GetTestlogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "logs", "log.txt")


def GetTestConfig(configname):
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", configname)


# testdata=xlrd.open_workbook(GetTestDataPath())
# table = testdata.sheets()[1]
# choice = table.cell(3, 0).value
# status = table.cell(3, 1).value
# print(choice)
# print(status)