#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/4 16:18
# @File     : demobank.py
# @Desc     : demobank机器手
from bank_login.biz.base.bot import Bot


class Demobank(Bot):
    """
    demobank机器手
    """
    def __init__(self):
        super(Demobank, self).__init__()

        self._order_mgr = None
        self._position_mgr = None
        self._statement_mgr = None

