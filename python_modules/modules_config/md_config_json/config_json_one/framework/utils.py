#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/24 15:23
# @File     : utils.py
# @Desc     :
import os


def root_path():
    """
    项目根目录
    """
    abs_path = os.path.abspath(__file__)
    rootpath = os.path.dirname(abs_path)
    rootpath = os.path.dirname(rootpath)
    return rootpath


def abs_path(*args):
    """
    绝对路径
    """
    return os.path.join(root_path(), *args)
