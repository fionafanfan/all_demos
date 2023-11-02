#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/1 11:20
# @File     : tornado_asyn.py
# @Desc     :
import tornado.ioloop
import tornado.web
import asyncio


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        # 模拟异步操作，例如从数据库或网络获取数据
        await asyncio.sleep(9)  # 模拟异步操作
        self.write({"ret": "Hello, Async Tornado!"})


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
