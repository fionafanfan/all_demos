#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/8 14:48
# @File     : check_app_foreground.py
# @Desc     :
import time
import subprocess
import re

from appium import webdriver
from appium.options.android import UiAutomator2Options

check_pkg = 'com.cmschina.cmschina_hk_app'


capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "192.168.0.151:5555",
    "noRes": True,
    "disableWindowAnimation": True,
    "skipDeviceInitialization": True,
    "autoGrantPermissions": True,
    "suppressKillServer": True,
    "hideKeyboard": True,
    "noSign": True,
    "skipUnlock": True,
    "unlockStrategy": "uiautomator2"
  },
  "appPackage": "com.cmschina.cmschina_hk_app",
  "appActivity": "com.cmschina.cmschina_hk_app.MainActivity",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}


appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")


def is_app_in_foreground(check_pkg, check_act):
    # 获取当前应用的包名
    current_package = driver.current_package
    # 获取当前应用的活动（Activity）
    current_activity = driver.current_activity

    print(f"Current Package: {current_package}, Current Activity: {current_activity}")

    # 判断应用是否在前台
    return current_package == check_pkg and current_activity == check_act


def get_run_apps():
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


def check_run_app(background_apps, check_pkg, check_act):
    apps = []
    for background_app in background_apps:
        if check_pkg in background_app and check_act in background_app:
            apps.append(background_app)
    return apps


# 检测应用状态
"""
应用在前台运行：Current Package: com.cmschina.cmschina_hk_app, Current Activity: .MainActivity
应用在后台运行: Current Package: com.huawei.android.launcher, Current Activity: .unihome.UniHomeLauncher
应用没有在运行，已关闭状态: 
"""
def check_app_status():
    while True:
        check_pkg = 'com.cmschina.cmschina_hk_app'
        check_act = '.MainActivity'
        if is_app_in_foreground(check_pkg, check_act):
            print("应用在前台运行")
        else:
            run_apps = get_run_apps()
            if check_run_app(run_apps, check_pkg, check_act):
                print("应用在后台运行")
            else:
                print("应用没有在运行，已关闭状态")
        time.sleep(1)


def check_app_status2():
    while True:
        status_map = {
            1: "应用没有在运行，已关闭状态",
            3: "应用在后台运行",
            4: "应用在前台运行"
        }
        check_pkg = 'com.cmschina.cmschina_hk_app'
        pkg_state = driver.query_app_state(check_pkg)
        print(f"{check_pkg} >> {pkg_state}  {status_map.get(pkg_state)}")
        time.sleep(1)


def test_driver_application_method():
    r = driver.app_strings(check_pkg)
    print(r)


if __name__ == '__main__':
    # check_app_status2()
    test_driver_application_method()
