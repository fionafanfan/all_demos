#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/26 15:59
# @File     : test_types_methodtype.py
# @Desc     :
import types


class Person(object):
    def __init__(self, name):
        self.name = name


def run(self):
    print('%s在奔跑' % self.name)


p1 = Person('p1')
p1.run = types.MethodType(run, p1)

p1.run()


class Car(object):
    country = 'china'

    def __init__(self, name):
        self.name = name


@classmethod
def run(cls):
    print('%s在奔跑' % cls.country)


Car.run = run
Car.run()

