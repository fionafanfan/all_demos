#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:14
# @File     : web_api_test.py
# @Desc     :
import requests
import datetime


def req_demo1(testcase):
    url = "http://127.0.0.1:8888/autotest/run"
    req_body = {"testcase": testcase}

    # 响应： {'code': 0, 'msg': '請求成功', 'data': {'answer': '答案内容', 'question': '问题：xxxx'}}
    res = requests.post(url=url, json=req_body)
    # res = requests.get(url=url)

    return res


def req_demo():
    """
[2023/11/16 18:05:21.869][INFO][auto_test] server_shape_indicator_check.py:1341 => begin---
[2023/11/16 18:05:27.336][INFO][auto_test] server_shape_indicator_check.py:1344 => 姝ｅ湪璁＄畻: 00700.hk, min5
    [2023/11/16 18:05:27.776][INFO][auto_test] server_shape_indicator_check.py:1347 => calculate ok
[2023/11/16 18:05:27.778][INFO][auto_test] server_shape_indicator_check.py:1355 => choose
[2023/11/16 18:05:27.779][INFO][auto_test] server_shape_indicator_check.py:1363 => end
    :return:
    """
    # url = "http://127.0.0.1:8888/getShapeIndicator"
    end_time = int(datetime.datetime.strptime("2023-11-17 2:00:00", "%Y-%m-%d %H:%M:%S").timestamp())
    req_body = {"market": "us",
                "kType": "min15",
                "time": end_time,
                "stockCode": "AAPL.us"
                }
    import time
    s = time.time()

    res = requests.post(url=url, json=req_body).json()
    data = res.get("data", {})
    print(type(data), data, time.time()-s)

    return res


if __name__ == '__main__':
    print(req_demo())


#
# if __name__ == '__main__':
#     # print(req_demo("hk_quotation_yidong_check").text)
#     print(req_demo("hk_quotation_yidong_").text)
#     # print(req_demo("us_quotation_check").text)
#     # print(req_demo("hk_shape").text)
#     # print(req_demo("us_shape").text)


