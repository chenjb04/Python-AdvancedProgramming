# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 10:52'


# 函数也是对象，可以赋值给一个变量
def fun(name="chen"):
    print(name)


# 类也是对象，可以赋值给一个变量
class Person(object):
    def __init__(self):
        print('Chen')


# 类和函数可以添加到集合和对象中
# obj_list = list()
# obj_list.append(fun)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# ask = fun
# ask()
# my_class = Person
# my_class()


# 可以作为参数传递给函数，可以当做函数的返回值
def fun1():
    print("start")
    return fun


ask1 = fun1()
ask1("tom")
