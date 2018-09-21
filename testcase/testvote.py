# -*- coding:utf-8 -*-
import xlrd
import sys
sys.path.append('../')
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath

testurl="http://127.0.0.1:8000"
testdata=xlrd.open_workbook(GetTestDataPath())


def post_vote():
    try:
        table = testdata.sheets()[1]
        for i in range(3, 5):
            choice = table.cell(i, 0).value
            status = table.cell(i, 1).value
            qiwang = table.cell(i, 2).value
            hdata={
                'choice': int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid = "1-1"
            testname = "testvote"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = qiwang
            r=TestPostRequest(testurl+'/polls/1/vote/', hdata, header, testcaseid, testname, testhope, fanhuitesthpe)
    except Exception as e:
        print(e)
# post_vote()

def get_polls():
    try:
        table = testdata.sheets()[1]
        for i in range(13, 14):
            status = table.cell(i, 0).value
            qiwang = table.cell(i, 1).value
            hdata = ""
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid = "1-1"
            testname = "testpolls"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = qiwang
            r=TestGetRequest(testurl+'/polls/1/', hdata, header, testcaseid, testname, testhope, fanhuitesthpe, "status")
    except Exception as e:
        print(e)

# get_polls()

def get_login():
    try:
        table = testdata.sheets()[2]
        for i in range(3, 5):
            key = table.cell(i, 0).value
            phone = table.cell(i, 1).value
            phone = str(int(phone))
            passwd = table.cell(i, 2).value
            passwd = str(int(passwd))
            status = table.cell(i, 3).value
            hope = table.cell(i, 4).value
            hope = str(hope)
            hdata = {'key': key, 'phone': phone, 'passwd': passwd}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-1"
            testname = "testdemo"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = hope
            r = TestGetRequest("https://www.apiopen.top/login", hdata, header, testcaseid, testname, testhope, fanhuitesthpe, 'code')
    except Exception as e:
        print(e)

#get_login()


def toupiao_login():
    try:
        table = testdata.sheets()[3]
        for i in range(3, 5):
            username = table.cell(i, 0).value
            username = str(username)
            password = table.cell(i, 1).value
            password = str(password)
            status = table.cell(i, 2).value
            hope = table.cell(i, 3).value
            hope = str(hope)
            hdata = {'username': username, 'password': password}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-4"
            testname = "testdemo"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = hope
            r = TestPostRequest("http://127.0.0.1:8000/toupiao/login/", hdata, header, testcaseid, testname, testhope, fanhuitesthpe)
    except Exception as e:
        print(e)

def get_novelApi():
    try:
        table = testdata.sheets()[2]
        for i in range(9, 10):
            status = table.cell(i, 0).value
            hope = table.cell(i, 1).value
            hdata = ""
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-2"
            testname = "testnovelApi"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = str(hope)
            r = TestGetRequest("https://www.apiopen.top/novelApi", hdata, header, testcaseid, testname, testhope, fanhuitesthpe, 'code')
    except Exception as e:
        print(e)


def get_createUserKey():
    try:
        table = testdata.sheets()[2]
        for i in range(14, 16):
            appid = table.cell(i, 0).value
            appid = str(appid)
            passwd = table.cell(i, 1).value
            passwd = str(int(passwd))
            status = table.cell(i, 2).value
            hope = table.cell(i, 3).value
            hdata = {'appId': appid, 'passwd': passwd}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-3"
            testname = "testcreateUserKey"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = str(hope)
            r = TestGetRequest("https://www.apiopen.top/createUserKey", hdata, header, testcaseid, testname, testhope, fanhuitesthpe, 'code')
    except Exception as e:
        print(e)


def get_findStatistics():
    try:
        table = testdata.sheets()[2]
        for i in range(20, 22):
            appKey = table.cell(i, 0).value
            appKey = str(appKey)
            status = table.cell(i, 1).value
            hope = table.cell(i, 2).value
            hdata = {'appKey': appKey}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-4"
            testname = "testfindStatistics"+testcaseid
            testhope = str(int(status))
            fanhuitesthpe = str(hope)
            r = TestGetRequest("https://www.apiopen.top/findStatistics", hdata, header, testcaseid, testname, testhope, fanhuitesthpe, 'code')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    toupiao_login()
    # get_novelApi()
    # get_createUserKey()
    # get_findStatistics()