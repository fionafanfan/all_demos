#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/22 16:22
# @File     : high_func_b.py
# @Desc     :

class Linear(object):

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):
        return self.a * x + self.b


class Exponential(Linear):

    def __call__(self, x):
        return self.a * (x ** self.b)


class Counter(object):

    value = 0

    def set(self, x):
        self.value = x

    def up(self):
        self.value = self.value + 1

    def down(self):
        self.value = self.value - 1


if __name__ == "__main__":
    taxes = Linear(0.3, 2)  # taxes = 0.3 * x + 2
    print(taxes(5))  # taxes = 0.3 * 5 + 2

    taxes2 = Exponential(0.3, 2)  # taxes = 0.3 * (x **2)
    print(taxes2(5))  # taxes = 0.3 * (5 ** 2)

    count = Counter()
    inc, dec, reset = count.up, count.down, count.set

