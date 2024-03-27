#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/3/1 14:38
# @File     : fire_demo_2.py
# @Desc     :
import fire
import asyncio
""""
# 执行示例: python asyncio_demo_1.py 'haha' 6
输入示例如下：
n_round=6
message:1
message:2
message:3

n_round=5
message:1
message:2
message:3

n_round=4
message:1
message:2
message:3

n_round=3
message:1
message:2
n_round=1
message:1
message:2
message:3
"""
roles_values = [1, 2, 3]


async def role_run(message=None):
    print(f'message:{message}')


async def env_run(k=1):
    for _ in range(k):
        futures = []
        for role in roles_values:
            future = role_run(message=role)
            futures.append(future)
        await asyncio.gather(*futures)


async def team_run(n_round):
    while n_round > 0:
        print(f'\nn_round={n_round}')
        n_round -= 1
        await env_run()


async def startup(idea: str, n_round: int=5):
    await team_run(n_round=n_round)


def main(idea: str, n_round: int = 5):
    asyncio.run(startup(idea, n_round))


if __name__ == "__main__":
    fire.Fire(main)
