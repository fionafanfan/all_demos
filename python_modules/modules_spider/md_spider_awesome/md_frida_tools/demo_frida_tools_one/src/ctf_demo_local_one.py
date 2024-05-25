#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/24 14:24
# @File     : ctf_demo_raw.py
# @Desc     :
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def main(target_app):
    # 连接到本地 Frida 服务器
    try:
        device = frida.get_usb_device()
    except Exception as e:
        print("Failed to connect to USB device:", e)
        sys.exit(1)

    print("[*] Connected to USB device:", device)

    # 启动 Frida 客户端
    try:
        processes = device.enumerate_processes()
        for i, process in enumerate(processes):
            print(f'设备上运行的进程{i+1}:{process}')
    except Exception as e:
        print("Failed to attach to target app:", e)
        sys.exit(1)

    print("[*] Attached to target app:", target_app)

    # 启动 Frida 客户端
    try:
        session = device.attach(target_app)
    except Exception as e:
        print("Failed to attach to target app:", e)
        sys.exit(1)

    print("[*] Attached to target app:", target_app)

    # 设置消息回调函数
    session.on('message', on_message)

    # 在目标进程中注入脚本
    script = session.create_script("""
    // 这里是你的 JavaScript 代码，用来执行 Frida 操作
    console.log("[*] Frida script loaded!");

    // 示例：在目标进程中 Hook Java 方法
    Java.perform(function () {
        var Activity = Java.use("android.app.Activity");
        Activity.onResume.implementation = function () {
            console.log("[*] onResume() called!");
            this.onResume();
        };
    });
    """)

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
    target_app = 'com.firstsechk.tc.trade'
    main(target_app)
