#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/30 17:13
# @File     : gen_key.py
# @Desc     :
import os


def generate_DESede_key():
    try:
        # Generate a 24-byte (192-bit) key for DESede
        key = os.urandom(24)
        return key
    except Exception as e:
        print(e)
        return None


k = generate_DESede_key()
print(k)
