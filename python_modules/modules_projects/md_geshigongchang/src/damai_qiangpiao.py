#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/4/10 10:51
# @File     : damai_demo.py
# @Desc     : 大麦app请求
import pyautogui
import time


class DaMai(object):

    def __init__(self):
        pass

    def click_kaiqiang_page_wangfeng(self):
        page_common_wait = 0.1000  # 0.001秒=1毫秒
        elem_common_wait = 0.0100
        pyautogui.click(x=985, y=990)  # 立即购买页面-立即购买
        time.sleep(page_common_wait)

        pyautogui.click(x=763, y=240)  # 选票页面-场次

        # pyautogui.click(x=806, y=331)  # 选票页面-票档-380
        pyautogui.click(x=981, y=336)  # 选票页面-票档-480
        # pyautogui.click(x=1137, y=332)  # 选票页面-票档-580
        # pyautogui.click(x=797, y=384)  # 选票页面-票档-780
        # pyautogui.click(x=974, y=383)  # 选票页面-票档-1080

        # pyautogui.click(x=1175, y=936)  # 选票页面-数量
        pyautogui.click(x=1069, y=992)  # 选票页面-确定
        time.sleep(1)
        pyautogui.click(x=1183, y=357)  # 选购票人页面-实名观演人1
        # pyautogui.click(x=1182, y=390)  # 选购票人页面-实名观演人2
        time.sleep(elem_common_wait)
        # pyautogui.click(x=1147, y=988)  # 选购票人页面-提交订单

    def quit_back(self):
        """
        回退一步
        """
        pyautogui.click(x=1564, y=554)  # 确定界面-画面外
        pyautogui.press('q')  # 所有页面-回退


    def click_kaiqiang_page_xuezhiqian(self):
        page_common_wait = 0.1000  # 0.001秒=1毫秒
        elem_common_wait = 0.0100
        pyautogui.click(x=985, y=990)  # 立即购买页面-立即购买
        time.sleep(page_common_wait)

        pyautogui.click(x=772, y=267)  # 选票页面-场次

        # pyautogui.click(x=801, y=423)  # 选票页面-票档-317
        pyautogui.click(x=972, y=421)  # 选票页面-票档-517
        # pyautogui.click(x=1145, y=420)  # 选票页面-票档-717
        # pyautogui.click(x=808, y=474)  # 选票页面-票档-1017
        # pyautogui.click(x=980, y=473)  # 选票页面-票档-1317
        # pyautogui.click(x=1153, y=475)  # 选票页面-票档-1717

        # pyautogui.click(x=1175, y=936)  # 选票页面-数量
        pyautogui.click(x=1069, y=992)  # 选票页面-确定
        time.sleep(0.5)
        pyautogui.click(x=1183, y=357)  # 选购票人页面-实名观演人1
        # pyautogui.click(x=1182, y=390)  # 选购票人页面-实名观演人2
        time.sleep(elem_common_wait)
        pyautogui.click(x=1147, y=988)  # 选购票人页面-提交订单

    def click_kaiqiang_page_suyoupeng(self):
        page_common_wait = 0.1000  # 0.001秒=1毫秒
        elem_common_wait = 0.0100
        pyautogui.click(x=985, y=990)  # 立即购买页面-立即购买
        time.sleep(page_common_wait)

        pyautogui.click(x=779, y=272)  # 选票页面-场次

        # pyautogui.click(x=731, y=368)  # 选票页面-看台-380
        # pyautogui.click(x=893, y=366)  # 选票页面-看台-580
        # pyautogui.click(x=1062, y=362)  # 选票页面-看台780
        # pyautogui.click(x=723, y=421)  # 选票页面-内场-1080
        pyautogui.click(x=888, y=422)  # 选票页面-内场-1280

        pyautogui.click(x=1175, y=936)  # 选票页面-数量
        pyautogui.click(x=1069, y=992)  # 选票页面-确定
        time.sleep(0.5)
        pyautogui.click(x=1183, y=402)  # 选购票人页面-实名观演人1
        pyautogui.click(x=1185, y=431)  # 选购票人页面-实名观演人2
        time.sleep(elem_common_wait)
        pyautogui.click(x=1142, y=987)  # 选购票人页面-提交订单

    def click_kaiqiang_page_zhognhangliang(self):
        page_common_wait = 0.1000  # 0.001秒=1毫秒
        elem_common_wait = 0.0100
        pyautogui.click(x=985, y=990)  # 立即购买页面-立即购买
        time.sleep(page_common_wait)

        pyautogui.click(x=711, y=237)  # 选票页面-场次

        # pyautogui.click(x=719, y=332)  # 选票页面-看台-380
        pyautogui.click(x=893, y=335)  # 选票页面-看台-680
        # pyautogui.click(x=1055, y=331)  # 选票页面-看台880
        # pyautogui.click(x=712, y=384)  # 选票页面-看台-1280
        # pyautogui.click(x=892, y=384)  # 选票页面-内场-1980

        pyautogui.click(x=1175, y=936)  # 选票页面-数量
        pyautogui.click(x=1069, y=992)  # 选票页面-确定
        time.sleep(0.5)
        pyautogui.click(x=1183, y=402)  # 选购票人页面-实名观演人1
        pyautogui.click(x=1185, y=431)  # 选购票人页面-实名观演人2

        time.sleep(elem_common_wait)
        pyautogui.click(x=1142, y=987)  # 选购票人页面-提交订单

    def qiangpiao_main(self):
         check_buy_lijigoumai = pyautogui.locateOnScreen('lijigoumai.png', grayscale=True)
         check_buy_lijiyuding = pyautogui.locateOnScreen('lijiyuding.png', grayscale=True)
         check_buy = check_buy_lijigoumai or check_buy_lijiyuding
         print("check_buy:", check_buy, "check_buy_lijigoumai:", check_buy_lijigoumai, "check_buy_lijiyuding:", check_buy_lijiyuding)
         tijiao_page = pyautogui.locateOnScreen('tijiaodingdan.png', grayscale=True)
         print("判定当前界面tijiao_page", tijiao_page)
         xuanpiao_page = pyautogui.locateOnScreen('queding.png', grayscale=True)
         print("判定当前界面xuanpiao_page", xuanpiao_page)
         no_xuanpiao_page = pyautogui.locateOnScreen('weiqueding.png', grayscale=True)
         flag = False
         if check_buy:
             print("---立即购票---")
             # self.click_kaiqiang_page_wangfeng()  # 汪峰
             # self.click_kaiqiang_page_zhognhangliang()
             self.click_kaiqiang_page_suyoupeng()  # 苏有朋

             print("---一轮购票结束---")
             return True
         elif no_xuanpiao_page:
             self.quit_back()
             print("返回购买界面")
         elif tijiao_page:
             self.quit_back()
             self.quit_back()
             time.sleep(0.05)
             print("返回购买界面")
         elif xuanpiao_page:
             self.quit_back()
             print("返回购买界面")
         else:
             print("还没有开始，不能购买")


if __name__ == "__main__":
    damai = DaMai()
    while True:
        ret = damai.qiangpiao_main()
        if ret:
            print("买到票，停止循环")
            break
        time.sleep(0.001)
