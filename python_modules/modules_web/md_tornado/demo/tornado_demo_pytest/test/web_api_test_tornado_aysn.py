#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:14
# @File     : web_api_test.py
# @Desc     :
import requests


def req_demo():
    url = "http://127.0.0.1:8889/long-task"
    res = requests.get(url=url)

    return res


if __name__ == '__main__':
    for i in range(5):
        data = req_demo()
        print(data.text)
