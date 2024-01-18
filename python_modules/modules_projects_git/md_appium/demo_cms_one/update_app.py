#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/1/9 16:06
# @File     : update_app.py
# @Desc     :
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options


capabilities = {
  "platformName": "Android",
  "automationName": "uiautomator2",
  "appium:newCommandTimeout": 0,
  # "appium:udid": "192.168.0.151:5555",
  "appium:udid": "10.18.20.13:5555",
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


appium_server_url = 'http://192.168.1.35:4723'

print(f"开始启动driver, appium_server_url:{appium_server_url}")
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")


try:
    pkg = 'com.cmschina.cmschina_hk_app'
    # 执行你的测试代码
    network_status = driver.network_connection
    print("网络状态:", network_status)
    if network_status == 0:  # 0 表示无网络连接
        print("网络连接断开，用户可能已掉线")
    else:
        print("未断开网络")  # 网络状态: 6

    pkg_state = driver.query_app_state(pkg)

    print("后台应用置为前台")
    driver.activate_app(pkg)
    print(pkg, "状态:",  pkg_state)
except WebDriverException as e:
    pass
finally:
    # 关闭驱动
    driver.quit()
