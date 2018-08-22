# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 15:54'
from collections import abc

# + 会产生一个新的序列，+= 实际上类似于extend方法

a = [1, 2, 3]
b = a + [5]
print(b)

a += [4, 5]
print(a)

a.extend([4, 5])
print(a)
