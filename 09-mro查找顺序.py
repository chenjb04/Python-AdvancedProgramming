# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 18:54'
# mro采用的是c3算法 python2旧式类采用深度优先算法


# class A:
#     num = 1
#
#     def __init__(self, num):
#         self.num = num
#
#
# a = A(2)
# print(a.num)


# 菱形继承
# class D(object):
#     pass
#
#
# class C(D):
#     pass
#
#
# class B(D):
#     pass
#
#
# class A(B, C):
#     pass
#
#
# print(A.__mro__)


class D(object):
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)



