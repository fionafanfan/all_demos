#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/3/1 14:38
# @File     : fire_demo_2.py
# @Desc     :
import fire

""""
# 执行示例: python fire_demo_2.py 'haha' 8
输入示例如下：
8: haha
7: haha
6: haha
5: haha
4: haha
3: haha
2: haha
1: haha
"""


def main(idea: str, n_round: int = 5):
    while n_round > 0:
        print(f'{n_round}: {idea}')
        n_round -= 1


if __name__ == "__main__":
    fire.Fire(main)
