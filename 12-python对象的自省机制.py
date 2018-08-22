# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 10:39'
# 自省机制：通过一定的机制查询到对象的内部结构


class Person(object):
    name = '小明'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


user = Student("北京")
print(user.__dict__)
print(Person.__dict__)
print(dir(user))












