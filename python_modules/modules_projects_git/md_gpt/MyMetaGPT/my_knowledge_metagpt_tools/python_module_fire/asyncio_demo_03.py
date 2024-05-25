#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/3/27 15:09
# @File     : asyncio_demo_02.py
# @Desc     :
import asyncio
import time
import aiohttp


async def download_one(n):
    print(n)
    await asyncio.sleep(5)


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [i for i in range(5)]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))



async def task1():
    while True:
        await asyncio.sleep(3)
        print('task1 over')


async def task2():
    await asyncio.sleep(1)
    print('task2 over')


async def task3():
    await asyncio.sleep(2)
    print('task3 over')



def main2():
    async def _main():
        tasks = [asyncio.create_task(t()) for t in (task1, task2, task3)]
        await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(_main())


if __name__ == '__main__':
    main2()
