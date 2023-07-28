#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/26 16:03
# @File     : test_pytest_types_methodtype.py
# @Desc     :
import types

import allure
import pytest


class TestUsQuotationCheck(object):
    def __init__(self, title):
        self.title = title


def test_case(self):
    ret = f'{self.title}'
    print(all(ret), f"【{self.title}】不通过")
    assert all(ret), f"【{self.title}】不通过"


titles = ['open', 'last']


case1 = TestUsQuotationCheck("case1")
case1.test_case = types.MethodType(test_case, case1)

# case1.test_case()
