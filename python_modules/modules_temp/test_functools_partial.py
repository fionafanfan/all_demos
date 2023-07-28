#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/26 15:53
# @File     : test_functools_partial.py
# @Desc     : functools。partial 和 types.MethodType
from functools import partial


def func(domain, user):
    echo = f"Hello, {user}@{domain}!"
    print(echo)


class A(object):
    pass


func_userA = partial(func, user="userA")
func_userB = partial(func, user="userB")
