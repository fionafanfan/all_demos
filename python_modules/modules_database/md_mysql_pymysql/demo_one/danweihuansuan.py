#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/27 15:43
# @File     : danweihuansuan.py
# @Desc     :

# 营业收入: 根据万、亿、万亿进行换算，保留两位小数，千位符
operatingIncome = 89498000000.0

new_operatingIncome = 89498000000.0

# 负号，用红绿区分，保留两位小数，乘以100%
netIncomeYoY = 0.1078615896916172
new_netIncomeYoY = str(round(netIncomeYoY, 2)) + '%'
print(new_netIncomeYoY)
