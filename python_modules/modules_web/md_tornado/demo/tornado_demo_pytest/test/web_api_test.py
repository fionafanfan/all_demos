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


def req_demo2():
    """
[2023/11/16 18:05:21.869][INFO][auto_test] server_shape_indicator_check.py:1341 => begin---
[2023/11/16 18:05:27.336][INFO][auto_test] server_shape_indicator_check.py:1344 => 姝ｅ湪璁＄畻: 00700.hk, min5
    [2023/11/16 18:05:27.776][INFO][auto_test] server_shape_indicator_check.py:1347 => calculate ok
[2023/11/16 18:05:27.778][INFO][auto_test] server_shape_indicator_check.py:1355 => choose
[2023/11/16 18:05:27.779][INFO][auto_test] server_shape_indicator_check.py:1363 => end
    :return:
    """
    # url = "http://172.16.6.196:8888/getShapeIndicator"
    # url = "http://127.0.0.1:8888/getShapeIndicator"
    url = "http://127.0.0.1:8888/getStockShapeIndicator"
    end_time = int(datetime.datetime.strptime("2023-11-17 2:00:00", "%Y-%m-%d %H:%M:%S").timestamp())
    req_body = {"market": "us",
                "kType": "min15",
                "time": end_time,
                "stockCode": "AAPL.us",
                "stockId": 1000000603
                }
    import time
    s = time.time()

    res = requests.post(url=url, json=req_body).json()
    data = res.get("data", {})
    print(type(data), data, time.time()-s)

    return res


def req_demo_vv(code):
    """
    """
    base_url = "http://fat-inv.uwintrader.com"
    param = f"/inv-pc/f10/estimation/v2/peAnalyze?code={code}"
    import time
    s = time.time()
    url = base_url + param
    headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Authorization': 'Bearer 27bf16d2dc6742a1965ea9a60bfc88078f93dd0c24c21860e1903649e3beb3da',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'DeviceType': '3',
            'SystemId': '11',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
        }
    res = requests.get(url=url, headers=headers).json()
    print(res)
    data = res.get("data", {})
    # print(type(data), data, time.time()-s)

    return res


def req_duckduckgo(keywords):
    """
    https://duckduckgo.com/?t=h_&q=%E5%88%98%E5%BE%B7%E5%8D%8E&ia=web
    :param keywords:
    :return:
    """
    url = "https://duckduckgo.com"
    req_body = {"q": keywords}
    res = requests.get(url=url, json=req_body, verify=False)

    return res


if __name__ == '__main__':
    # print(req_duckduckgo("刘德华"))
    # req_demo_vv('00700.hk')
    req_demo2()

#
# if __name__ == '__main__':
#     # print(req_demo("hk_quotation_yidong_check").text)
#     print(req_demo("hk_quotation_yidong_").text)
#     # print(req_demo("us_quotation_check").text)
#     # print(req_demo("hk_shape").text)
#     # print(req_demo("us_shape").text)


