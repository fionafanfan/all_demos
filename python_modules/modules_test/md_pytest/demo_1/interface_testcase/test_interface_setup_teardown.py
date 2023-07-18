# -*-coding:utf-8-*-
# @作   者: fionafanfan
# @创建时间: 2023/7/19:4:16
# @项目名称: all_demos
# @文件名称：test_interface_setup_teardown.py 
# @描   述:
"""
【详情描述】 
"""


class TestInterfaceSetupTeardown(object):

    def setup_class(self):
        print("在每个类执行前的初始化的工作，比如：创建日志对西昂，创建数据库的链接，创建接口的请求对象。")

    def setup(self):
        print("\n在执行每个测试用例之前初始化的代码， 如： 打开浏览器，加载网页")

    def test_01(self):
        print("测试用例-1")

    def test_02(self):
        print("测试用例-2")

    def teardown(self):
        print("\n在下hi下每个测试用例之后扫尾的代码， 如： 关闭浏览器")

    def teardown_class(self):
        print("在每个类执行后的扫尾的工作， 比如： 销毁日志对象， 销毁数据的连接，销毁接口的请求对象。")