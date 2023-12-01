#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/29 11:56
# @File     : messages.py
# @Desc     :
class ServerTradeOrderMsg(object):
    """
    交易指令
    """

    def __init__(self):
        self.stockCode = ""  # 股票代码
        self.regionType = 0  # 地区类型 type: int

