#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 10:22
# @File     : tornado_server.py
# @Desc     :
import traceback
import tornado
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from logger.logger import logger, set_logger_uid
from handles.demo_handler import DemoHandler
from handles.hello_handler import HelloHandler
import tornado_swagger
from tornado_swagger.setup import setup_swagger


PORT = 8016


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print('protocol:{}'.format(self.request.protocol))
        self.render('index.html')

    def post(self):
        self.write('please use post method')


def make_app():
    # return tornado.web.Application([
    #     (r"/demo", DemoHandler),  # demo handler
    #     (r"/hello", HelloHandler),  # hello handler
    #     (r'.*', IndexHandler),  # 首页
    #     ],
    #     template_path="templates",
    #     static_path='templates',
    #     debug=True
    # )

    return tornado.web.Application([
        (r"/demo", DemoHandler),  # demo handler
        (r"/hello", HelloHandler),  # hello handler
        (r'.*', IndexHandler),  # 首页
        ],
        swagger_url='/swagger',
        api_base_url="/spec",
        description="用于模板展示的API接口事例和说明",
        title="模板API列表", schemes=["http"],
        template_path="templates",
        static_path='templates',
        debug=True
    )


def main():
    app = make_app()
    setup_swagger(app)
    # myserver = HTTPServer(app)
    # myserver.listen(PORT)
    app.listen(PORT)
    logger.info('server is running at {}....!!'.format(PORT))
    print('server is running at {}....!!'.format(PORT))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
