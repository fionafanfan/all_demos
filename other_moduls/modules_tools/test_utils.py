#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/8/16 18:51
# @File     : test_utils.py
# @Desc     :
from utils import makepath, abs_paths


def test_makepath():
    dir_ret, normcase_ret = makepath('a', 'b', 'c')
    print(dir_ret, "\n\n", normcase_ret)


def test_abs_paths():
    abs_paths()
