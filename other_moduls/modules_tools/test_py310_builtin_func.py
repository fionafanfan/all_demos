#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/16 18:30
# @File     : test_py310_builtin_func.py
# @Desc     :

class TestBuiltinFunc(object):
    def test_abs(self):
        test_datas = [(-1, 1), (-1.1, 1.1)]
        ret = [abs(test_data[0]) == test_data[1] for test_data in
               test_datas]
        assert all(ret)

    def test_iter(self):
        for i in iter(range(0, 10)):
            print(i)
