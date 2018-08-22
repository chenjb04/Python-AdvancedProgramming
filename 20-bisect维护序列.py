# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 17:43'
import bisect

# 用来维护一个已经有序的序列
test_list = []
bisect.insort(test_list, 8)
bisect.insort(test_list, 5)
bisect.insort(test_list, 7)
bisect.insort(test_list, 3)
bisect.insort(test_list, 9)
bisect.insort(test_list, 6)
bisect.insort(test_list, 1)
print(bisect.bisect_right(test_list, 4))
print(bisect.bisect_left(test_list, 4))
print(test_list)
