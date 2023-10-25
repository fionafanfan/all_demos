#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/24 15:31
# @File     : config_utils.py
# @Desc     :

def config(filename, *args, default=None):
    """
    获取配置
    """
    from framework.config_mgr import gConfigMgr
    return gConfigMgr.get(filename, *args, default)



