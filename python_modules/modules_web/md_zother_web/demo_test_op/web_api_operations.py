#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:14
# @File     : web_api_test.py
# @Desc     :
import json

import requests
import datetime


def req_demo1():
    url = "http://192.168.0.176:5000/orderConfig/send"
    d = json.dumps({"id": 1592})
    req_body = {'data': d}

    res = requests.post(url=url, data=req_body)
    print(res.text)
    return res


if __name__ == '__main__':
    req_demo1()


