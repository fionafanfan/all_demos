#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/21 17:13
# @File     : test_config.py
# @Desc     :
from framework.config_mgr import gConfigMgr
from framework.config_utils import config


gConfigMgr.init(dir_seconds=['config_one', 'config_two'])
ret = config("config_one", "database")
