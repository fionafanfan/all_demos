#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/24 14:24
# @File     : hook_demo.py
# @Desc     :
import frida
import sys

# 设备id
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
            print(f'设备上运行的进程{i+1}:{process}')
            if not found:
                for match in process_matches:
                    if process.name.find(match) != -1:
                        target_name = process.name
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
    js = """
        Java.perform(() => {
        // Function to hook is defined here
        function showStacks() {
                Java.perform(function () {
                            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
                        });
        };
 
        function hook1() {
            var URL = Java.use('java.net.URL');
            URL.$init.overload('java.lang.String').implementation = function (a) {
                console.log('加密前URL：' + a)
                showStacks()
                this.$init(a)
            }
        };
        hook1();
        });
    """

    script = session.create_script(js)

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
    # target_app = 'com.firstsechk.tc.trade'
    # target_app = '第一证券(香港)'

    process_matches = ['firstsechk', '第一证券']  # 自动匹配所需进程，有时进程名会在两个之间变化
    main(process_matches)
