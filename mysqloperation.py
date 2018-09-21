#!/usr/bin/env python
# encoding: utf-8
'''
@author: renjing
@file: mysqloperation.py
@time: 2018/9/5 15:14
'''
import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig

config = configparser.ConfigParser()
config.read(GetTestConfig('dbconfig.conf'))
db = 'TestDB'
host = config[db]['host']
user = config[db]['user']
password = config[db]['password']
db = config[db]['db']

# host = '10.1.198.84'
# user = 'renjing'
# password = 'renjing'
# db = 'django_t'


class MySQLcaozuo():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def update(self, table_name, id, data):
        values = []
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
            value = key + "=" +data[key]
            values.append(value)
        values = ','.join(values)
        # print(values)
        real_sql = "UPDATE " + table_name + " SET " + values + " WHERE id =" + str(id)
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def select(self, table_name, id):
        real_sql = "SELECT * FROM " + table_name + " WHERE id =" + str(id)
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            data = cursor.fetchone()
            print(data)
        self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db = MySQLcaozuo()
    table_name = "toupiao_question"
    data = {'id': 1, 'question_text': '你喜欢的游戏是什么？'}
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()



