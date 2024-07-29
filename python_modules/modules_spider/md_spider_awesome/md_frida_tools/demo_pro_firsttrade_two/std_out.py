#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/7/26 16:43
# @File     : std_out.py
# @Desc     : python 控制台输出的内容保存到txt文件
import sys
import time


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


time_array = time.localtime(int(time.time()))
log_time = time.strftime("%Y_%m_%d_%H_%M_%S", time_array)
sys.stdout = Logger(f"log_{log_time}.log")  # 保存到文件中

for i in range(1, 10):
    print(i)


# while True:
#     s = input('输入:')
#     print(s)
#     if s == 'q':
#         print('已退出')
#         break

