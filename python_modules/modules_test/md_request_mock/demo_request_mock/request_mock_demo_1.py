#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/9/27 15:53
# @File     : request_mock_demo_1.py
# @Desc     :
from requests_mock import Mocker
import unittest

import requests


def get_data_from_api(url):
    response = requests.get(url)
    return response.json()


class TestApi(unittest.TestCase):

    def setUp(self):
        self.mock_requests = Mocker()

    def tearDown(self):
        self.mock_requests.stop()

    def test_get_data_from_api(self):
        # 设置模拟的响应
        mock_result = self.mock_requests.get('http://example.com/api', json={

            'data': 'mocked data'})
        print(f'mock_result:{mock_result} {dir(mock_result)}  {mock_result.request_history}')
        # 调用函数并检查结果
        # result = get_data_from_api('http://example.com/api')
        # self.assertEqual(result, {
        #
        #     'data': 'mocked data'})


if __name__ == '__main__':
    unittest.main()
