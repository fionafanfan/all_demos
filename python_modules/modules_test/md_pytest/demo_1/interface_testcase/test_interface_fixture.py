# -*-coding:utf-8-*-
# @作   者: fionafanfan
# @创建时间: 2023/7/19:4:16
# @项目名称: all_demos
# @文件名称：test_interface_setup_teardown.py 
# @描   述:
"""
【详情描述】 
"""
import pytest


@pytest.fixture(scope="module", params=["hello", "world"], autouse=True)
def my_module_fixture(request):
    print("module前置操作")
    yield request.param
    print("module后置操作")


@pytest.fixture(scope="class", params=["aa", "bb"], autouse=True)
def my_class_fixture(request):
    print("class前置操作")
    yield request.param
    print("class后置操作")


@pytest.fixture(scope="function", params=[1, 2], autouse=True)
def my_function_fixture(request):
    print("function前置操作")
    yield request.param
    print("function后置操作")


class TestInterfaceFixture(object):

    def test_01(self):
        print("测试用例-1")

    def test_02(self):
        print("测试用例-2")

