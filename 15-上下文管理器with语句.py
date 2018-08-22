# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/22 15:09'
# 上下文管理器：上下文管理器规定了某个对象的使用范围，当进入或者离开了使用范围，都会有相应的一些调用，比如代码块开始时执行一些准备，代码块结束时结束一些操作。它更多的是用于资源的分配和释放上，即在开始时分配资源，结束时释放一些资源。比如在执行数据库查询时要建立连接，查询结束后要释放连接；写文件时要先打开文件，写结束后，要关闭文件等等。还有，就是资源的加锁和解锁，比如在使用多线程时，可能会用到加锁和解锁。


class Sample:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_something(self):
        print('do something')


with Sample() as sample:
    sample.do_something()

import contextlib


@contextlib.contextmanager
def fun():
    print('begin')
    yield
    print('end')


with fun() as f:
    print('do something')