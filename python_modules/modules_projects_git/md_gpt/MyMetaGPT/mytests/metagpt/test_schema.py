#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 15:30
# @File     : test_schema.py
# @Desc     :
from metagpt.schema import AIMessage, Message, SystemMessage, UserMessage


def test_messages():
    test_content = 'test_message'
    msgs = [
        UserMessage(test_content),
        SystemMessage(test_content),
        AIMessage(test_content),
        Message(test_content, role='QA')
    ]
    text = str(msgs)
    roles = ['user', 'system', 'assistant', 'QA']
    assert all([i in text for i in roles])
