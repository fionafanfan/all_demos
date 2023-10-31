#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 11:16
# @File     : hello_handler.py
# @Desc     :
import tornado.web


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print('protocol:{}'.format(self.request.protocol))
        self.render('hello.html')

    def post(self):
        self.write('please use post method')
