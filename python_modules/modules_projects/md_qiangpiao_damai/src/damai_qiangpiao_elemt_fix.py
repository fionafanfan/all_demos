#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/11 10:42
# @File     : damai_demo.py
# @Desc     : 大麦app请求
import pyautogui
import time


class DaMai(object):

    def __init__(self):
        pass

    def get_page_elem_pix(self, filename, page_elem_name_list):
        print(f"开始收集【{filename}】元素位置")
        elem_name_list = []
        for i, elem in enumerate(page_elem_name_list):
            page, elems = elem[0], elem[1]
            page_elem = f"page【{i + 1}-{page}】: {elems}"
            print(page_elem)
            for e in elems:
                elem_name_list.append(f"{page}-{e}")

        for i, elem_name in enumerate(elem_name_list):
            # elem_name = input(f"输入需要获取的像素点元素名称:")
            step = input(f"将鼠标放到【{elem_name}-{i+1}/{len(elem_name_list)}】元素上，按回车完成像素点采集:")
            if step != "q":
                currentMouseX, currentMouseY = pyautogui.position()  # 获取鼠标当前位置
                log_msg = f"elem_name:{elem_name} x:{currentMouseX} y: {currentMouseY}"
                print(log_msg)
                content = f"pyautogui.click(x={currentMouseX}, y={currentMouseY})  # {elem_name}"
                pyautogui.click(x=currentMouseX, y=currentMouseY)
                with open(filename, 'a', encoding='utf-8') as fw:
                    fw.write(f'{content}\n')
            else:
                print("元素位置收集完毕")
                break
        print("结束收集元素位置")


if __name__ == "__main__":
    damai = DaMai()

    filename = "elem_pix_guding_空白.txt"
    page_elem_name_list = [
        # ("所有页面", ["回退"]),
        # ("确定界面", ["回退"]),
        ("确定界面", ["画面外"]),
        # ("空白页面", ["空白"]),
        # ("临时", ["定位抢票判断的参照点"])
    ]

    # filename = "elem_pix.txt"
    # page_elem_name_list = [("立即购买页面", ["立即购买"]),
    #                   ("选票页面", ["场次", "票档", "数量", "确定"]),
    #                   ("选购票人页面", ["实名观演人1", "实名观演人2", "提交订单"])
    #                   ]

    # filename = "elem_pix_wangfeng_jijiang.txt"
    # page_elem_name_list = [
    #     ("选票页面", ["场次",
    #                   "票档-380", "票档-480", "票档-580", "票档-780", "票档-1080"
    #                   ])
    # ]

    # filename = "elem_pix_xuezhiqian_jijiang.txt"
    # page_elem_name_list = [
    #                        ("选票页面", ["场次",
    #                                     "票档-317", "票档-517", "票档-717", "票档-1017", "票档-1317","票档-1717",
    #                                 ])
    #                   ]


    # 苏有朋
    # filename = "elem_pix.txt"
    # filename = "elem_pix_suyoupeng_jijiang.txt"
    # page_elem_name_list = [
    #                        ("选票页面", ["场次", "看台-380", "看台-580", "看台780", "内场-1080", "内场-1280"])
    #                   ]

    # 钟汉良
    filename = "elem_pix_zhonghanliang_jijiang.txt"
    page_elem_name_list = [
                           ("选票页面", ["场次", "看台-380", "看台-680", "看台880", "看台-1280", "内场-1980"])
                      ]


    filename = "elem_pix_update_选购票人页面.txt"
    page_elem_name_list = [
                      ("选购票人页面", ["实名观演人1", "实名观演人2", "提交订单"])
                      ]
    damai.get_page_elem_pix(filename, page_elem_name_list)  # 定制
