#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/22 16:15
# @File     : high_func_a.py
# @Desc     :
def linear(a, b):
    def result(x):
        return a * x + b
    return result


if __name__ == "__main__":
    taxes = linear(0.3, 2)  # taxes = 0.3 * x + 2
    print(taxes(5))  # taxes = 0.3 * 5 + 2
