#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/8 15:11
# @File     : get_background_apps.py
# @Desc     :
import subprocess
import re
import time

"""
日志：
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 正在运行（不区分前后台）
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
com.cmschina.cmschina_hk_app 没有运行， app没有启动
"""

def get_background_apps():
    """
    TaskRecord{7d61abd #41 A=10022:com.cmschina.cmschina_hk_app U=0 StackId=41 sz=1}
    Run #0: ActivityRecord{cb2f73d u0 com.cmschina.cmschina_hk_app/.MainActivity t41}
    :return:
    """
    # 执行 adb shell dumpsys activity 命令
    command_output = subprocess.check_output(['adb', 'shell', 'dumpsys', 'activity', 'activities']).decode('utf-8')
    # print(command_output)
    # 使用正则表达式提取包名
    # pattern = re.compile(r"Stack #\d+ tasks=\d+ running=\d+/(.+)", re.MULTILINE)

    # 从输出文本中提取包名的正则表达式
    # pattern = re.compile(r'\* TaskRecord{\S+? userId=\d+ (.+?)\s+?[*}]', re.DOTALL)
    pattern = re.compile(r'Run #\d+: ActivityRecord{\S+? (.+?)\s+?}', re.DOTALL)

    # 从文本中匹配所有包名
    matches = pattern.findall(command_output)
    return matches


def check_backgroupd_app(background_apps, check_pkg, check_act):
    apps = []
    for background_app in background_apps:
        if check_pkg in background_app and check_act in background_app:
            apps.append(background_app)
    return apps


while True:
    # 获取在后台运行的应用列表
    background_apps = get_background_apps()

    check_pkg = 'com.cmschina.cmschina_hk_app'
    check_act = '.MainActivity'
    ret = check_backgroupd_app(background_apps, check_pkg, check_act)
    # print(f"ret_num:{len(ret)}, ret_num_0: {ret[0] if ret else ''}")

    if ret:
        print(f"{check_pkg} 正在运行（不区分前后台）")
    else:
        print(f"{check_pkg} 没有运行， app没有启动")

    time.sleep(1)

