#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:14
# @File     : web_api_test.py
# @Desc     :
import requests


def req_demo():
    url = "http://127.0.0.1:8016/demo"
    req_body = {"question": "问题：xxxx"}

    # 响应： {'code': 0, 'msg': '請求成功', 'data': {'answer': '答案内容', 'question': '问题：xxxx'}}
    res = requests.post(url=url, json=req_body).json()
    # res = requests.get(url=url)

    return res


if __name__ == '__main__':
    data = req_demo()

    print(data)