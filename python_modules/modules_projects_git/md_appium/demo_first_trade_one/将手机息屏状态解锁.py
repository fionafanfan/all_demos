#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/4/17 20:06
# @File     : 将手机息屏状态解锁.py
# @Desc     :
import subprocess
import time


def wake_up_and_unlock_screen(device_id):
    # 息屏
    subprocess.run(f"adb -s {device_id} shell input keyevent 26", shell=True)
    print("息屏成功")
    time.sleep(2)
    # 唤醒设备
    subprocess.run(f"adb -s {device_id} shell input keyevent 224", shell=True)
    print("唤醒设备")
    time.sleep(2)
    print("休息2s")
    # 解锁
    subprocess.run(f"adb -s {device_id} shell input swipe 500 1000 500 50", shell=True)
    print("向上滑解锁成功")


# 使用设备ID（例如：192.168.56.101:5555）调用函数
# wake_up_and_unlock_screen('your_device_id')
wake_up_and_unlock_screen('R5CNA0C587T')
