# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 11:08'


# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#         super().__init__()


# 重写了B的构造函数，为什么还要调用super
# super函数的调用顺序,mro算法


class A(object):
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


if __name__ == '__main__':
    # b = B()
    d = D()
    print(D.__mro__)


