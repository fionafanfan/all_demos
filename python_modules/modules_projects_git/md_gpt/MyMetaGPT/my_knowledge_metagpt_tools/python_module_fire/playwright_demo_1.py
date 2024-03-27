#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/2/4 16:23
# @File     : playwright_demo_1.py
# @Desc     :
"""

https://zhuanlan.zhihu.com/p/507247029?utm_id=0
https://zhuanlan.zhihu.com/p/566082651?utm_id=0
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page2 = browser.new_page()

    page.goto('http://www.baidu.com')
    page.screenshot(path='baidu.png')

    page2.goto('https://www.baidu.com/s?wd=%E6%98%A5%E8%8A%82%E5%89%8D%E5%A4%95%E8%80%83%E5%AF%9F%E5%A4%A9%E6%B4%A5+%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%BC%BA%E8%B0%83%E4%BB%80%E4%B9%88&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1')
    page2.screenshot(path='baidu_xw.png')
    print('------')
    browser.close()
