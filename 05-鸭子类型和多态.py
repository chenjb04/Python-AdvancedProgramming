# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 16:43'

# 鸭子类型：当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。


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
