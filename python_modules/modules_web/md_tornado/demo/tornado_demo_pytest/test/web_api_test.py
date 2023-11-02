#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:14
# @File     : web_api_test.py
# @Desc     :
import requests


def req_demo(testcase):
    url = "http://127.0.0.1:8888/autotest/run"
    req_body = {"testcase": testcase}

    # 响应： {'code': 0, 'msg': '請求成功', 'data': {'answer': '答案内容', 'question': '问题：xxxx'}}
    res = requests.post(url=url, json=req_body)
    # res = requests.get(url=url)

    return res


if __name__ == '__main__':
    # print(req_demo("hk_quotation_yidong_check").text)
    # print(req_demo("hk_quotation_yidong_").text)
    # print(req_demo("us_quotation_check").text)
    print(req_demo("hk_shape").text)
    # print(req_demo("us_shape").text)


