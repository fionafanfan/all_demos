#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/3/27 14:03
# @File     : asyncio_demo_01.py
# @Desc     :
import asyncio

"""
http://www.codebaoku.com/it-python/it-python-246244.html  python中的asyncio异步协程
内容关键点：
一、定义协程
二、运行协程
三、协程回调
四、运行多个协程
五、run_forever
    通过run_until_complete 运行协程，协程运行完，程序也就结束退出了
    使用run_forever 运行，程序并不会退出，除非调用 loop.stop()
    如果想让其退出，需要调用 loop.stop()
    我们可以在协程中调用
六、多协程中关闭run_forever
    单个协程中可以通过在协程中关闭，但是如果是两个以上的协程的时候
    如果有一个协程先做完了就stop了，将会导致其他的协程也会异常退出，这肯定是不允许的
    所以我们可以在回调函数中进行关闭
https://zhuanlan.zhihu.com/p/336617921  Python 并发编程实现方式之 Asyncio
https://blog.csdn.net/szial/article/details/131028770

国际象棋大师Judit Polgár在一次展览中与多名业余棋手对局。她有两种进行展览的方式：同步和异步。
假设条件：
24位对手
Judit每步棋耗时5秒
对手每步棋耗时55秒
每场比赛平均30个对子的走法（总共60步）
同步版本：Judit一次只玩一场比赛，直到完成这场比赛后才开始下一场。每场比赛需要(55 + 5) * 30 == 1800秒，即30分钟。整个展览需要24 * 30 == 720分钟，即12小时。
异步版本：Judit在不同的桌子间移动，每张桌子只走一步。她离开桌子，在等待对手走下一步的时间里进行下一步。在24场比赛中每场比赛只需要Judit花费5 * 24 == 120秒，即2分钟。整个展览时间缩短到了120 * 30 == 3600秒，即1小时。
Judit Polgár只有一个人，只有两只手，一次只能走一步棋。但是通过异步对局，展览时间从12小时缩短到了1小时。因此，协作式多任务处理就是程序的事件循环（稍后会详细介绍）与多个任务进行通信，在最佳时间让每个任务轮流运行。
当你深入一点时，异步编程也可能很困难！Python的异步模型是围绕回调、事件、传输、协议和期物等概念构建的，光是术语就可能令人生畏。此外，其API一直在不断变化，这使得情况更加复杂。

幸运的是，asyncio已经发展到一个阶段，其中大部分功能不再是试验性的，同时其文档也经过了重大改进，还出现了一些优质资源来帮助理解这一主题。

asyncio包和async/await关键字
Python的asyncio包（在Python 3.4中引入）以及它的两个关键字async和await，分别担当着不同的角色，协助你声明、构建、执行和管理异步代码
事件循环和 asyncio.run()
"""


# 通过 async 定义一个协程
async def task1():
    print('这是一个协程')


# 判断是否是一个协程，返回True
# print(asyncio.iscoroutinefunction(task1))

# ----------------------


# 通过 async 定义一个协程
async def task2(s):
    print('请等待 {} 秒'.format(s))
    await asyncio.sleep(s)
    print('协程结束')

# 协程运行
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task2(3))
# 结果如下：
# 请等待 3 秒
# 协程结束

# -------------------------


# 通过 async 定义一个协程
async def task3(s):
    print('请等待 {} 秒'.format(s))
    await asyncio.sleep(s)
    return '这里task结束了，其他的继续吧'


def callback(future):
    print(future.result() + "+ ending...")

# 运行
# future = asyncio.ensure_future(task3(5))
# future.add_done_callback(callback)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(future)
# 结果如下：
# 请等待 3 秒
# 这里task结束了，其他的继续吧

# -----------------------------


# 通过 async 定义一个协程
async def task_41(s):
    print('请等待 {} 秒'.format(s))
    await asyncio.sleep(s)
    print('这里task_11结束了')


# 通过 async 定义一个协程
async def task_42(s):
    print('请等待 {} 秒'.format(s))
    await asyncio.sleep(s)
    print('这里task_12结束了')


# 运行公共方法
# loop = asyncio.get_event_loop()
# 运行方法一
# loop.run_until_complete(asyncio.gather(task_41(1), task_42(3)))
# 运行方法二
# coros = [task_41(1), task_42(3)]
# loop.run_until_complete(asyncio.gather(*coros))
# 结果如下：
# 请等待 1 秒
# 请等待 3 秒
# 这里task1结束了
# 这里task2结束了


# ------------------------------


import functools


async def task_6(x):
    await asyncio.sleep(x)
    print('这是协程任务')


def callback(loop):
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.gather(task_6(1), task_6(3))
future.add_done_callback(functools.partial(callback, loop))
loop.run_forever()
