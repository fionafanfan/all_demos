#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 12:00
# @File     : test_base_gpt_api2.py
# @Desc     :
def messages_to_prompt(messages):
    return "\n".join([f"{i['role']}: {i['content']}" for i in messages])


def messages_to_dict(messages):
    """objects to [{"role": "user", "content": msg}] etc."""
    return [i.to_dict() for i in messages]


ret = messages_to_prompt([{"role": "user", "content": '答案....'}])
dict_ret = messages_to_dict([{"role": "user", "content": '答案....'}])
print(ret)
print(dict_ret)
