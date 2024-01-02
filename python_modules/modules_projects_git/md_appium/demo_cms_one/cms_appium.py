#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/27 16:43
# @File     : cms_appium.py
# @Desc     :

"""
定位策略:
id
xpath
name
class name
accessibility id
ui automator
"""
# 登录


class Login(object):
    login_button = 'descriptionContains("我的账户").descriptionContains("登录")'  # 登录触发按钮元素
