#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/11/13 14:53
# @File     : pd_iloc_compare.py
# @Desc     :
import pandas as pd
import time


def pd_iloc_compare():
    """
    结果：
    df iloc耗时: 1.8575046062469482
    df itertuples耗时: 0.04683518409729004
    list耗时: 0.004994869232177734
    :return:
    """
    N = 100000
    df = pd.DataFrame({'c1': list(range(N))})
    df_list = list(df.itertuples())
    s = time.time()
    for i in range(N):
        row = df.iloc[i]
    print("df iloc耗时:", time.time()-s)

    s = time.time()
    for row in df.itertuples():
        r = row
    print("df itertuples耗时:", time.time() - s)

    s = time.time()
    for i in range(N):
        row = df_list[i]
    print("list耗时:", time.time() - s)


if __name__ == '__main__':
    pd_iloc_compare()
