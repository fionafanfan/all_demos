#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/21 10:39
# @File     : yaml_demo.py
# @Desc     :
import yaml


def read_yaml(filepath):
    try:
        with open(filepath, encoding="utf-8") as f:
            value = yaml.safe_load(f)
            return value
    except Exception as e:
        print(f"错误:{e}")
        return None


if __name__ == "__main__":
    print("request_demo", read_yaml('request_demo.yaml'))
