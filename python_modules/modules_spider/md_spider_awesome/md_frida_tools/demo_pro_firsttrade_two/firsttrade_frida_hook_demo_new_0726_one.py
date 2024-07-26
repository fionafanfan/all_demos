#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/24 14:24
# @File     : firsttrade_frida_hook_demo_one.py
# @Desc     :
import frida
import sys
import time


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


time_array = time.localtime(int(time.time()))
log_time = time.strftime("%Y%m%d_%H_%M_%S", time_array)
sys.stdout = Logger(f"log_frida_hook_{log_time}.txt")  # 保存到文件中

DEVICE_UID = 'emulator-5554'


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def main(process_matches):
    # 连接到本地 Frida 服务器
    try:
        device = frida.get_device(DEVICE_UID)
    except Exception as e:
        print("Failed to connect to USB device:", e)
        sys.exit(1)

    print("[*] Connected to USB device:", device)

    target_name = ''
    # 启动 Frida 客户端
    try:
        processes = device.enumerate_processes()
        found = False
        for i, process in enumerate(processes):
            if not found:
                for match in process_matches:
                    if process.name.find(match) != -1:
                        target_name = process.name
                        print(f'设备上运行的进程{i + 1}:{process}, {target_name}')
                        found = True 
    except Exception as e:
        print("Failed to enumerate_processes:", e)
        sys.exit(1)

    if not target_name:
        print('找不到对应的进程: ', process_matches)
        return

    # 启动 Frida 客户端
    try:
        session = device.attach(target_name)
    except Exception as e:
        print("Failed to attach to target app:", e)
        sys.exit(1)

    print("[*] Attached to target app:", target_name)

    # 在目标进程中注入脚本
    # frida_js = """目标进程中注入脚本"""
    from frida_ft_js import frida_js
    script = session.create_script(frida_js)

    # 设置消息回调函数
    script.on('message', on_message)

    # 加载并运行脚本
    script.load()

    # 保持脚本运行，直到按下 Ctrl+C 或者脚本自行退出
    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        pass

    # 断开连接并清理资源
    session.detach()
    print("[*] Script finished and detached.")


if __name__ == '__main__':
    process_matches = ['firstsechk', '第一证券']  # 自动匹配所需进程，有时进程名会在两个之间变化
    main(process_matches)
