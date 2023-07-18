# -*-coding:utf-8-*-
# @作   者: fionafanfan
# @创建时间: 2023/7/18:23:45
# @项目名称: all_demos
# @文件名称：all.py 
# @描   述:
"""
【详情描述】
"""
import os
import pytest


if __name__ == '__main__':
    pytest.main()
    # os.system("allure generate temp -o reports  --clean")
    # pytest.main(['-v'])
    # pytest.main(['-s'])
    # pytest.main(['-vs'])
    # pytest.main(['-vs', 'testcase/test_login.py'])
    # pytest.main(['-vs', 'interface_testcase/'])
    # pytest.main(['-vs', 'interface_testcase/test_interface.py::test_interface_01_func'])
    # pytest.main(['-vs', './interface_testcase/test_interface.py::TestInterface::test_01_interface'])
