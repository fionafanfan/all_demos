#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 16:46
# @File     : chatgpt_webui_provider.py
# @Desc     :
from typing import NamedTuple, Union
from metagpt.schema import Message


class ChatgptWebuiProvider(object):

    def __init__(self):
        pass

    def completion(self, messages: list[dict]) -> dict:
        return self._chat_completion(messages)

    def ask_code(self, messages: Union[str, Message, list[dict]], **kwargs) -> dict:
        """
        messages = "Write a python hello world code."
        rsp = {'language': 'python', 'code': "print('Hello, World!')"}

        messages = [{'role': 'user', 'content': "Write a python hello world code."}]
        rsp = {'language': 'python', 'code': "print('Hello, World!')"}
        """
        rsp = self._chat_completion_function(messages, **kwargs)
        return rsp

    def _chat_completion(self, messages: list[dict]) -> dict:
        # rsp = {}  # 真正的获取答案的地方
        rsp = {}  # 先默认回复空的答案
        return rsp

    def _chat_completion_function(self, messages: list[dict], **kwargs) -> dict:
        # rsp = {}  # 真正的获取答案的地方
        rsp = {}  # 先默认回复空的答案
        return rsp
