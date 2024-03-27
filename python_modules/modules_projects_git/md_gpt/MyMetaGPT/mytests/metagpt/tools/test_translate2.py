#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/30 11:07
# @File     : test_translate.py
# @Desc     :
from metagpt.tools.translator import Translator


def test_translate():
    poetries = [
        ("Let life be beautiful like summer flowers", "花"),
        ("The ancient Chinese poetries are all songs.", "中国")
    ]
    for i, j in poetries:
        prompt = Translator.translate_prompt(i)
        print('prompt', prompt)
        # print(rsp)
        # assert j in rsp


test_translate()


