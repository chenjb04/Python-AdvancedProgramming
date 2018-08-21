# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 15:50'

# 魔法函数：双下划线__开头和双下划线__结尾的python内置函数


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(["张三", "李四", "王五"])
for em in company:
    print(em)



