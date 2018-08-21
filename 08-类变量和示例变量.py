# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 17:49'


class A:
    # num为类变量
    num = 1

    def __init__(self, x):
        self.x = x


a = A(5)
print(a.x, a.num)
a.num = 10
A.num = 6
print(A.num, a.num)
b = A(3)
print(b.num)
