#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/10/31 10:39
# @File     : demo_handler.py
# @Desc     :
import time
import traceback

from logger.logger import logger
from handles.base_handler import BaseHandler


class DemoHandler(BaseHandler):

    @staticmethod
    def demo_get_last_result(**kwargs):
        question = kwargs.get("question", "")
        ret = {"answer": "答案内容", "question": question}
        return ret

    def get(self):
        self.write('Please use post method')

    def post(self):
        args = self.args_parse
        logger.info('\n*********************接收參數*************************:{}'.format(args))
        stime = time.time()
        try:
            question = args.get('question', '')  # 必填
            assert question, "question 不能为空"
            assert len(question) <= 256, "questiont太長啦"  # 不能超過256個字符長度
            request_kwargs = {
                "question": question,
            }
            logger.info('补充默认參數后的完整参数:{}'.format(request_kwargs))
            try:
                res = self.demo_get_last_result(**request_kwargs)
                logger.info("請求结果:{}".format(res))
                ret = {"code": 0, "msg": "請求成功", "data": res}
            except Exception as e:
                msg = '請求出錯，出錯詳情:{}'.format(e)
                logger.info(msg)
                logger.info("错误追蹤详情： {}".format(traceback.print_exc()), no_uid=True)
                ret = {"code": 1, "msg": msg, "data": {}}
        except AttributeError as e:
            msg = "AttributeError,{}".format(e)
            logger.info(msg)
            ret = {"code": 1, "msg": msg, "data": {}}
        except AssertionError as e:
            msg = "AssertionError,{}".format(e)
            logger.info(msg)
            ret = {"code": 1, "msg": msg, "data":{}}
        endtime = time.time()
        logger.info("最終返回的数据:{} 所耗時間:{} 秒".format(ret, endtime-stime))
        self.write(ret)
