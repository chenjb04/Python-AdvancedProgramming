# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 19:58'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


pr = Person('小明', 20)
# 私有属性无法通过这种方式访问
print(pr.age)
# 可以这样访问，但是帅的人不会这么做
print(pr._Person__age)
