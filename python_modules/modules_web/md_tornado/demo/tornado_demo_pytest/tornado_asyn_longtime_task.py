#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/1 15:09
# @File     : tornado_asyn_longtime_task.py
# @Desc     :
import tornado.ioloop
import tornado.web
import asyncio


class LongRunningTaskHandler(tornado.web.RequestHandler):
    async def get(self):
        # 异步返回响应
        self.write({"ret": "Request received. Processing in the background."})
        await self.flush()
        # 在后台执行时间长的任务
        await self.run_long_task()
        self.write({"ret": f"long time task:"})
        await self.finish()  # 结束响应

    async def run_long_task(self):
        # 模拟一个时间长的任务，比如数据库查询或网络请求
        await asyncio.sleep(5)  # 模拟5秒的任务执行时间
        # return "Task Completed"


def make_app():
    return tornado.web.Application([
        (r"/long-task", LongRunningTaskHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
