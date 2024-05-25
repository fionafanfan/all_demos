#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/11 10:42
# @File     : damai_demo.py
# @Desc     : 大麦app请求
import pyautogui
import time


class ElementPix(object):

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
    elem_pix = ElementPix()

    # 格式工厂分段录屏
    filename = "geshigongchang_element.txt"
    page_elem_name_list = [
                           ("区域按钮", ["P5", "全屏", "录像", "停止"])
                      ]
    elem_pix.get_page_elem_pix(filename, page_elem_name_list)  # 定制
