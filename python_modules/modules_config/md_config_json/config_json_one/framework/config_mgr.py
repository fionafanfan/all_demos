#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/24 15:21
# @File     : config_mgr.py
# @Desc     :
import os
import json

from framework import utils
from framework.decorators import singleton


@singleton
class ConfigMgr(object):
    def __init__(self):
        self._config = dict()

    def init(self, dir_seconds=None):
        cfg_files = self._get_files()
        for cfg_file, name in cfg_files:
            with open(cfg_file, 'r', encoding='utf-8') as f:
                self._config[name] = json.load(f)

            if dir_seconds:
                for dir_second in dir_seconds:
                    cfg_files = self._get_files(dir_second_name=dir_second)
                    for cfg_file, name in cfg_files:
                        with open(cfg_file, 'r', encoding='utf-8') as f:
                            self._config[dir_second] = {name: json.load(f)}

    def replace(self, configs: dict):
        """
        替换配置
        :param configs: 新配置，格式如{('bot', 'account_id'): value}
        """
        for keys, value in configs.items():
            final_cfg = self._config[keys[0]]
            for k in keys[1:-1]:
                final_cfg = final_cfg[k]
            final_cfg[keys[-1]] = value

    @staticmethod
    def _get_files(dir_root_name='config', dir_second_name=''):
        if not dir_second_name:
            filenames = os.listdir(utils.abs_path(dir_root_name))
            config_files = [(utils.abs_path(dir_root_name, f), f[:-5]) for f in filenames if f.endswith('.json')]
        else:
            filenames = os.listdir(utils.abs_path(os.path.join(dir_root_name, dir_second_name)))
            config_files = [(utils.abs_path(dir_root_name, dir_second_name, f), f[:-5]) for f in filenames if f.endswith('.json')]

        return config_files

    def get(self, filename, *args, default=None):
        cfg = self._config.get(filename, {})
        for cfg_name in args:
            if cfg_name is None:
                continue
            cfg = cfg.get(cfg_name, default)
            if not isinstance(cfg, dict):
                return cfg
        return cfg


gConfigMgr = ConfigMgr()




