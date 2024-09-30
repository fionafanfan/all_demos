#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/9/27 15:53
# @File     : request_mock_demo_1.py
# @Desc     :
from requests_mock import Mocker
import unittest

import requests


# coding:utf-8

import requests

import requests_mock


def t_01():
    url = "http://127.0.0.1:8016/demo"
    resp = {'code': 0, 'msg': '請求成功', 'data': {'answer': '答案内容', 'question': '问题：xxxx'}}

    url = "https://api-app.cmschina.com.hk/user/login/qr/statusQry"  # 模拟请求的url
    resp = {'code': '0', 'msg': '请求成功', 'result': {'status': 'NON_SCAN'}, 'success': True}  # 模拟的返回结果
    with requests_mock.Mocker() as m:

        # 模拟post请求内容，返回的json格式，返回码为200

        m.post(url, json=resp, status_code=200)

        # 根据模拟的请求进行通过requests进行发送模拟信息，查看返回结果内容
        r = requests.post(url, json=resp)

        # 响应结果r.json:{'code': '0', 'msg': '请求成功', 'result': {'status': 'NON_SCAN'}, 'success': True}
        print(f'r.json:{r.json()}')
        assert r.status_code == 200


t_01()

