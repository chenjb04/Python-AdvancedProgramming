# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 11:27'
"""mixin模式特点：
1.功能单一，表示某一种功能
2.不和基类关联，可以被多个基类使用，基类可以不和mixin关联就能初始化成功
3.在mixin中不要使用super这种用法
"""


class Vehicle(object):
    pass


class PlaneMixin(object):
    def fly(self):
        print('I am flying')


class Airplane(Vehicle, PlaneMixin):
    pass


"""
以看到，上面的Airplane类实现了多继承，不过它继承的第二个类我们起名为PlaneMixin,
而不是Plane，这个并不影响功能，但是会告诉后来读代码的人，这个类是一个Mixin类。\
所以从含义上理解，Airplane只是一个Vehicle，不是一个Plane。这个Mixin，表示混入(mix-in)，它告诉别人，这个类是作为功能添加到子类中，而不是作为父类"""