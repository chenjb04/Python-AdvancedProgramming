# -*- coding:utf-8 -*-
__author__ = 'ChenJiaBao'
__date__ = '2018/8/21 17:22'


# 抽象基类：抽象基类的作用类似于JAVA中的接口。在接口中定义各种方法，然后继承接口的各种类进行具体方法的实现。抽象基类就是定义各种方法而不做具体实现的类，任何继承自抽象基类的类必须实现这些方法，否则无法实例化。
"""那么抽象基类这样实现的目的是什么呢？ 假设我们在写一个关于动物的代码。涉及到的动物有鸟，狗，牛。首先鸟，狗，牛都是属于动物的。既然是动物那么肯定需要吃饭，发出声音。但是具体到鸟，狗，牛来说吃饭和声音肯定是不同的。需要具体去实现鸟，狗\
牛吃饭和声音的代码。概括一下抽象基类的作用：定义一些共同事物的规则和行为。
"""
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

    # def get(self, key):
    #     pass


redis_cache = RedisCache()
redis_cache.set('key', 'value')