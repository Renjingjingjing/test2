#!/usr/bin/env python
# encoding: utf-8
'''
@author: renjing
@file: initdata.py
@time: 2018/9/5 17:17
'''
from mysqloperation import MySQLcaozuo


def insert_data(table, datas):
    db = MySQLcaozuo()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

table_poll_question = "toupiao_question"
datas_poll_question = [{'id': 1, 'question_text': '你喜欢的语言是什么?'}]
table_poll_choice = "toupiao_choice"
datas_poll_choice = [{'id': 1, 'choice_text': 'java', 'votes': 0, 'question_id': 1},
                     {'id': 2, 'choice_text': 'python', 'votes': 0, 'question_id': 1}]


def init_data():
    insert_data(table_poll_question, datas_poll_question)
    insert_data(table_poll_choice, datas_poll_choice)


def update_data(table, id, datas):
    db = MySQLcaozuo()
    for data in datas:
        db.update(table, id, data)
    db.close()

table_poll_question = "toupiao_choice"
datas_poll_id = 1
datas_poll_question = [{'choice_text': 'c++', 'votes': 3, 'question_id': 1}]

def update():
    update_data(table_poll_question, datas_poll_id, datas_poll_question)

def select_data(table, id):
    db = MySQLcaozuo()
    db.select(table, id)
    db.close()

table_poll_question = "toupiao_choice"
datas_poll_id = 1

def select():
    select_data(table_poll_question, datas_poll_id)


if __name__ == '__main__':
    # init_data()
    # update()
    select()
