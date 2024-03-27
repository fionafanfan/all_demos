#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/26 15:52
# @File     : demo.py
# @Desc     :
from pprint import pprint

def my_sorted():
    self_stock_code = 'TSLA.us'
    sorted_fields = ['pe_ratio', 'pe_ttm']
    compare_ret = {}
    for field in sorted_fields:
        sorted_ret = []
        raw_sorted_rets = [
            {'code': 'TSLA.us', 'pe_ratio': 6, 'pe_ttm': 1},
            {'code': 'T.us', 'pe_ratio': 2, 'pe_ttm': 2},
            {'code': 'LA.us', 'pe_ratio': 3, 'pe_ttm': 3},
            {'code': 'TA.us', 'pe_ratio': 4, 'pe_ttm': 4},
            {'code': 'A.us', 'pe_ratio': 5, 'pe_ttm': 5},
            {'code': 'SL.us', 'pe_ratio': 6, 'pe_ttm': 6},
            {'code': 'TLA.us', 'pe_ratio': 7, 'pe_ttm': 7},
            {'code': 'TSA.us', 'pe_ratio': 8, 'pe_ttm': 8},
           ]
        sorted_rets = sorted(raw_sorted_rets, key=lambda x: (x[field], x['code']), reverse=True)
        current_stock_data = {}
        for i, data in enumerate(sorted_rets):
            sort = i + 1
            data['sort'] = sort
            if data['code'].lower() == self_stock_code.lower():
                current_stock_data = data
        last_sorted_ret = sorted_rets[:6]

        # last_sorted_ret = sorted(sorted_ret, key=lambda x: x['sort'], reverse=False)
        compare_ret[field] = [current_stock_data, last_sorted_ret]
    return compare_ret


d = my_sorted()
pprint(d)
