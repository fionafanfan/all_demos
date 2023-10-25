#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/24 15:26
# @File     : main.py
# @Desc     :
from framework.config_mgr import gConfigMgr
from framework.config_utils import config


gConfigMgr.init(dir_seconds=['config_one', 'config_two'])
ret = config("config_one", "database")
print("获取配置", ret)
ret = config("config_two")
print("获取配置", ret)
ret = config("api")
print("获取配置", ret)
