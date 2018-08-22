# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 16:43'

# 鸭子类型：当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。不关心对象是什么类型，只关心它的行为


class Cat(object):
    def say(self):
        print('this is a cat')


class Dog(object):
    def say(self):
        print('this is a dog')


class Duck(object):
    def say(self):
        print('this is a duck')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# 鸭子类型，不需要关心extend的参数是否为list，只要他是可以迭代的
a = [1, 2, 3]
b = [4, 5]
c = (6, 7)
d = {8, 9}
a.extend(b)
a.extend(c)
a.extend(d)
print(a)
