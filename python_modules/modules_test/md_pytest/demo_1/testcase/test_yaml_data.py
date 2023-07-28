#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/7/21 10:56
# @File     : test_yaml_data.py
# @Desc     :
import pytest
import yaml
import json
import requests


def read_yaml(filepath):
    try:
        with open(filepath, encoding="utf-8") as f:
            value = yaml.safe_load(f)
            return value
    except Exception as e:
        print(f"错误:{e}")
        return None


def run_requests(req_method='post', req_url='', req_data=None, header=None):
    ret = {}
    if req_method == 'post':
        ret = requests.post(req_url, json=req_data, headers=header)
    else:
        print(f"【{req_method}】为不支持的请求method")

    return ret


root_path = "D:\\aGitData\local_fiona_projects\\all_demos\python_modules\modules_test\md_pytest\demo_1\\testcase"


class TestYamlApi(object):
    @pytest.mark.skip()
    @pytest.mark.parametrize("a,b", read_yaml(f"{root_path}\\num_array.yaml"))
    def test_fool(self, a, b):
        """
        测试结果:
        testcase/test_yaml_data.py::test_fool[1-2] a + b = 3
        PASSED
        testcase/test_yaml_data.py::test_fool[20-30] a + b = 50
        PASSED
        testcase/test_yaml_data.py::test_fool[33-44] a + b = 77
        PASSED
        """
        print(f"a + b = {a + b}")

    @pytest.mark.parametrize('data', read_yaml(f"{root_path}\\request_quotation_data.yaml"))
    def test_api_success(self, data):
        print(data)
        response = run_requests(data['request']['method'],
                                data['request']['url'],
                                json.dumps(data['request']['data']),
                                data['request']['header'])
        print(f"response:{response}")
        assert data['request']['extract']['code'] == response.status_code
