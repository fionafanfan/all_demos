#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/4/20 17:07
# @File     : 统计元素.py
# @Desc     :
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy

# 初始化 Appium 驱动
capabilities = {
  "platformName": "Android",
  "appium:udid": "R5CNA0C587T",
  "automationName": "uiautomator2",
  "appium.options": {
    "automationName": "uiautomator2",
    "deviceName": "R5CNA0C587T",
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
  "appPackage": "com.gt.shk",
  "appActivity": "com.gt.shk.MainActivity ",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}

appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")
input('input text>>')

try:
    pkg = 'com.firstsechk.tc.trade'
    # 执行你的测试代码
    network_status = driver.network_connection
    print("网络状态:", network_status)
    if network_status == 0:  # 0 表示无网络连接
        print("网络连接断开，用户可能已掉线")
    else:
        print("未断开网络")  # 网络状态: 6

    pkg_state = driver.query_app_state(pkg)

    print(f"后台应用置为前台， 状态1:{pkg_state}")
    driver.activate_app(pkg)
    new_pkg_state = driver.query_app_state(pkg)
    print(pkg, "状态2:",  new_pkg_state)
    go_to_account = '//android.widget.ImageButton[@resource-id="com.firstsechk.tc.trade:id/btn_Account"]'  # 首页左上角按钮
    go_to_account_el = driver.find_element(AppiumBy.XPATH, go_to_account)
    print('find element [go_to_account_el]: ', go_to_account_el)
    go_to_account_el.click()
    time.sleep(1)  # 暂停等待
except WebDriverException as e:
    print("错误>>", e)
finally:
    # 关闭驱动
    driver.quit()
