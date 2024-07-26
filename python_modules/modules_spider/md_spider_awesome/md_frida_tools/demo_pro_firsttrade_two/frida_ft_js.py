#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/7/26 13:50
# @File     : frida_ft_js.py
# @Desc     :

js_file_path_name = 'debug_7_26_有用.js'
with open(js_file_path_name, 'r') as fr:
    lines = fr.readlines()
    debug_js = "\n".join(lines)

print(f"{debug_js[:60]}")

# 使用js
frida_js = debug_js
