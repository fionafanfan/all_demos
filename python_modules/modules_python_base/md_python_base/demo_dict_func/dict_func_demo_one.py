#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/22 15:43
# @File     : dict_func_demo_one.py
# @Desc     :
"""
大家往往希望，函数调用会为默认值创建新的对象。但事实并非如此。
【默认值只会在函数定义时创建一次】。如果对象发生改变，就如上例中的字典那样，则后续调用该函数时将会引用这个改动的对象。
"""


def foo(k, v, mydict={}):
    mydict[k] = v
    return mydict


def foo2(k, v, mydict=None):
    if mydict is None:
        mydict = {}  # create a new dict for local namespace

    mydict[k] = v
    return mydict


if __name__ == "__main__":
    print(foo('a', 1))
    print(foo('b', 2))
    print(foo('b', 2, mydict={}))
    print("----------")
    print(foo2('a', 1))
    print(foo2('b', 2))
    print(foo2('b', 2, mydict={}))
