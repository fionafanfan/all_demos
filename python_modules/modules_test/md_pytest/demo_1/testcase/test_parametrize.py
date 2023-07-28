#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/24 18:04
# @File     : test_parametrize.py
# @Desc     :
import pytest
import allure

cases = [("检查今开", "open"), ("检查昨收", "preClose"), ("检查最新价", "last"), ("检查最高价", "high")]


def case(title, stand_field):
    print(f"{title} {stand_field}")
    ret = [True, False]
    return ret


@allure.epic("测试项目：投管系统")
@allure.feature("测试模块：行情")
@allure.story("美股行情指标测试")
@allure.severity("一般")
@allure.tag("一般关注")
@pytest.mark.parametrize("title,stand_field", cases)
class TestParam:

    @allure.title("检查美股行情字段")  # 用例标题
    def test_case(self, title, stand_field):
        print(f"测试函数case的数据: title={title}, stand_field={stand_field}")
        assert all(case(title, stand_field)), f"【{title}】不通过"
