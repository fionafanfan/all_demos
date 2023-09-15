#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/23 14:23
# @File     : module_sys_source.py
# @Desc     :
import sys


# 一个包含所有被编译进 Python 解释器的模块的名称的字符串元组。
# 一个字符串元组。
# 被编译进 Python 解释器的模块的名称
print(sys.builtin_module_names)

print("\n\n")
print(sys.stdlib_module_names)

print(sys.thread_info)
