#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 15:08
# @File     : allure_app.py
# @Desc     :
from tornado.httpserver import HTTPServer
import tornado.ioloop
import tornado.web

from logger.logger import logger

ALLURE_DIR_NAME = "allure-reports"
ROOT_DIR = f"D:/aGitData/local_fiona_projects/all_demos/python_modules/modules_web/md_tornado/demo/tornado_demo_pytest"


class AutoTestHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        # 重定向到Allure报告的index.html页面
        allure_report = self.request.uri.split("/")[-1]
        self.redirect(f"/{ALLURE_DIR_NAME}/{allure_report}/index.html")


def gen_allure_report_routes():
    allure_reports = ["uscompare", "hkyidong"]
    routes = []
    for report in allure_reports:
        static_path = f"{ROOT_DIR}/{ALLURE_DIR_NAME}/{report}"
        routes.append((r"/allure-reports/" + report, ReportHandler))
        routes.append((r"/allure-reports/" + report + "/(.*)", tornado.web.StaticFileHandler, {"path": static_path}))
    return routes


def make_app():
    report_routes = gen_allure_report_routes()
    return tornado.web.Application(report_routes + [
                                       (r"/autotest/run", AutoTestHandler)]
                                   )


if __name__ == "__main__":
    PORT = 8888
    application = make_app()
    myserver = HTTPServer(application)
    myserver.listen(PORT)
    logger.info('server is running at {}....!!'.format(PORT))
    print('server is running at {}....!!'.format(PORT))
    tornado.ioloop.IOLoop.current().start()
