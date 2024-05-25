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
    print(f"开始定时录制视频:{start_time}, {time.localtime()}")
    end_time = start_time + (0.5* 3600 + 6*3600)  # 多少时间之后停止录制
    time_len = 2*60  # 每隔多久录制一段视频保存
    count = 1
    while time.time() < end_time:
        print(f"开始定时录制视频:{count}")   
        pyautogui.press('f6')  # 录像
        time.sleep(time_len)
        print(f"开始保存录制视频:{count}") 
        pyautogui.press('f8')
        time.sleep(5) # 3s时间其保存视频
        print(f"保存成功录制视频:{count}") 
        count += 1


if __name__ == "__main__":
    main()
