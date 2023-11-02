#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/1 15:03
# @File     : function_async.py
# @Desc     :
import asyncio


# 普通的同步函数
def sync_function():
    print("Start synchronous operation")
    result = do_some_sync_work()
    print(f"Result: {result}")
    print("End synchronous operation")


# 模拟同步工作
def do_some_sync_work():
    # 模拟同步操作，耗时1秒
    import time
    for i in range(3):
        time.sleep(1)
        print(f"休眠时间:{i+1}s")
    return "Sync Data"


# 将函数变为异步函数
async def async_function():
    print("Start asynchronous operation")
    result = await do_some_async_work()
    print(f"Result: {result}")
    print("End asynchronous operation")


# 模拟异步工作
async def do_some_async_work():
    # 模拟异步操作，耗时1秒
    for i in range(3):
        await asyncio.sleep(1)
        print(f"休眠时间:{i+1}s")
    return "Async Data"


# 同步函数调用
sync_function()


# 异步函数调用
asyncio.run(async_function())
