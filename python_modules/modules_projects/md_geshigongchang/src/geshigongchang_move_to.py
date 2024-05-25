#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/9/11 10:42
# @File     : damai_demo.py
# @Desc     : 大麦app请求
import pyautogui
import time



def main():
    start_time = time.time()
    print(f"移动鼠标:{start_time}, {time.localtime()}")
    end_time = start_time + (0.5* 3600 + 6*3600)  # 多少时间之后停止录制
    time_len = 60  # 每隔60s一次鼠标
    count = 1
    while time.time() < end_time:
        print('move to: 500  100')
        pyautogui.moveTo(500, 100)
        print(f"移动鼠标次数:{count}")   

        time.sleep(time_len)
        print('move back:500  800')
        pyautogui.moveTo(500, 800)
        count += 1


if __name__ == "__main__":
    main()
