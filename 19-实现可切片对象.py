# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 17:24'
import numbers


class Group(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(name=self.name)
        elif isinstance(item, numbers.Integral):
            return cls(name=self.name)

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        return iter(self.name)

    def __reversed__(self):
        self.name.reverse()

    def __contains__(self, item):
        if item in self.name:
            return True
        else:
            return False


if __name__ == '__main__':
    name_list = ["张三", '李四', '王五']
    group = Group(name=name_list)
    sub_group = group[:1]
    if "张三1" in group:
        print('yes')
    pass
