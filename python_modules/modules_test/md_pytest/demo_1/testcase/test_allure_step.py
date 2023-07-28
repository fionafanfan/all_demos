#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/26 17:41
# @File     : test_allure_step.py
# @Desc     :
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 8:34
# @Author  : longrong.lang
# @FileName: test_allure.py
# @Software: PyCharm
# @
import allure


@allure.step("打开网站首页")
def open():
    pass


@allure.step("输入账号、密码")
def input_UsernameAndPassWord():
    sendAndClickLogin("xiaoqiang", "1")


@allure.step("输入账号、密码{arg1}，{arg2}，并点击登录")
def sendAndClickLogin(arg1, arg2):
    pass


@allure.step("验证登录过程")
def test_login():
    open()
    input_UsernameAndPassWord()