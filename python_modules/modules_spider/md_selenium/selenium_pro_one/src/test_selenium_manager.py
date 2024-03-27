#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/23 17:20
# @File     : test_selenium_manager.py
# @Desc     :
import pytest 


@pytest.fixture(scope="module", autouse=True)
def global_module_fixture():
    
    print(f"模块_前置操作")
    yield
    try:
        pass
    except Exception as e:
        print(f"错误详情:{e}")
    else:
        print(f"模块_后置操作成功")


class TestBaiduBot(object):
    
    def test_baidu_bot(self):
        from selm_webdriver_manager import TestBaiduBot
        baidu_bot = TestBaiduBot()
        baidu_bot.open_start_page()
        print("-- end --")
