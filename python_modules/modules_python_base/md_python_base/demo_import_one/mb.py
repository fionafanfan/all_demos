#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/22 14:57
# @File     : mb.py
# @Desc     :

"""
tst_one和test_two 都导入了ma模块， 但是只执行了一次导入操作
a我被导入了
b我被导入了

因为模块有一次初始化过程，所以第一次加载模块的代价可能会比较高，
但多次加载几乎没有什么花费，代价只是进行几次字典检索而已
"""
import ma
import importlib


def test_one():
    import ma
    importlib.reload(ma)  # 警告：这种技术并非万无一失。尤其是模块包含了以下语句时: 警告：from modname import some_objects


def test_two():
    import ma
    importlib.reload(ma)


if __name__ == "__main__":
    test_one()
    test_two()

