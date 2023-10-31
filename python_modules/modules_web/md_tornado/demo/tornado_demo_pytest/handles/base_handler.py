#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 10:31
# @File     : base_handler.py
# @Desc     :
import json
import tornado
import tornado.escape
import tornado.web
from tornado import gen
from logger.logger import logger


class BaseHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write("None")
        logger.info("request.uri : {}".format(self.request.uri), no_uid=True)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 允许跨域访问
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Content-Type", "text/plain; charset=UTF-8")
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")

    def options(self):
        self.set_status(204)
        self.finish()

    @property
    def args_parse(self):
        """解析传入的参数"""
        # from tornado.httputil import parse_body_arguments
        # logger.info("传入参数: {}".format(self.request.arguments), no_uid=True)
        # logger.info("self.request.body.{}".format(self.request.body))
        # logger.info("self.request.query: {}".format(self.request.query))
        # logger.info("self.request.body_arguments: {}".format(self.request.body_arguments))
        # logger.info("self.request.query_arguments; {}".format(self.request.query_arguments))
        logger.info("--------------baseHandler args_parse begin--------------")
        _ip = self.request.headers.get('X-Forwarded-For') or self.request.headers.get(
            'X-Real-IP') or self.request.remote_ip  # 有可能是nginx代理； proxy_set_header X-Forwarded-For  $remote_addr;
        content_type = self.request.headers.get("Content-Type", "")
        args_data = {}
        # if 'application/json' in content_type.lower():
        body_data = self.request.body
        logger.info("---base---handler-body_data:{}".format(body_data))
        if isinstance(body_data, bytes):
            body_data = self.request.body.decode('utf8', errors='ignore')
        try:
            args_data = json.loads(body_data)
        except Exception as e:
            logger.info(f"当成json格式解析出错:{e}", exc_info=True)

        for name, values in self.request.arguments.items():
            if not values:
                continue
            else:
                args_data[name] = values[0].decode('utf8').strip()
        uid = self.request.headers.get('uid', '')
        if not args_data and body_data:
            if isinstance(body_data, bytes):
                body_data = self.request.body.decode('utf8')
            args_data = tornado.escape.json_decode(body_data)
        if uid:
            args_data['uid'] = uid

        args_data['ip'] = _ip

        logger.info("传入参数: {}".format(args_data), no_uid=True)
        return args_data