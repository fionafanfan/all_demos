#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/4/16 17:45
# @File     : check_touch_action.py
# @Desc     :
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options

"""
模拟手势，可以用， 但是不适合用来做返回和前进页面。
"""

# 初始化 Appium 驱动
capabilities = {
  "platformName": "Android",
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
  "appPackage": "com.firstsechk.tc.trade",
  "appActivity": "com.afe.mobilecore.tcuicore.SplashBaseActivity",
  "appium.settings": {
    "ignoreUnimportantViews": True,
    "allowInvisibleElements": True
  },
  "noReset": True
}

appium_server_url = 'http://localhost:4723'


driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

print("driver启动app成功")

# 执行向后滑动操作
action = TouchAction(driver)
# 设置起始点坐标和终点坐标
start_x = 50
start_y = 200
end_x = 100
end_y = 200
# 执行滑动操作
action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

# 等待一段时间，让页面响应
time.sleep(2)

# # 关闭驱动
# driver.quit()
