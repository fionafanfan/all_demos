#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/1 11:56
# @File     : temp.py
# @Desc     :
import enum


# 测试用例运行选项
class TsCaseRunChoise(enum.Enum):
    ALL = "all"
    US_QUOTATION_CHECK = "us_quotation_check"
    HK_QUOTATION_YIDONG_CHECK = "hk_quotation_yidong_check"


print([member.value for member in TsCaseRunChoise])
