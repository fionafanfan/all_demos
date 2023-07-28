#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/24 18:04
# @File     : test_parametrize.py
# @Desc     :
import pytest
import allure

list1 = [(1, 1, 1), (3, 3, 9), (5, 6, 30)]


def multi(a, b):
    return a*b


@pytest.mark.parametrize("a,b,c", list1)
class TestParam:

    @allure.title("用例1")  # 用例标题
    def test_1_multi(self, a, b, c):
        print("测试函数1的数据a是{},b是{}，c是{}".format(a, b, c))
        assert multi(a, b) == c

    @allure.title("用例2")  # 用例标题
    def test_2_multi(self, a, b, c):
        print("测试函数2的数据a是{},b是{}，c是{}".format(a, b, c))
        assert multi(a, b) == c
        assert multi(a, b) == c
