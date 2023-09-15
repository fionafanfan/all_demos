#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/13 11:31
# @File     : local_utils.py
# @Desc     : 本地utils
import functools
import time


def _retry_times(retries=3, delay=1):
    """
    重试装饰器
    retries:3 可以自定义重试次数
    delay: 1 可以自定义下一次重试的等待的秒数
    """

    def inner_func():
        print("内部执行函数")
        count = 0
        while count < retries:
            print(f"当前执行次数:{count+1}   最大尝试执行次数:{retries}")
            print("正在重试...")
            ret = False
            if not ret:
                print(f"重试结果:{ret}, {delay}秒后发起新一轮的重试。\n\n")
                count += 1
                time.sleep(delay)
        else:
            print(f"超过最大尝试执行次数:{retries}")

    def decorate(exec_func):
        @functools.wraps(exec_func)
        def wrapper():
            return inner_func()
        return wrapper

    return decorate


@_retry_times()
def func_a():
    print("函数a")


if __name__ == "__main__":
    func_a()
